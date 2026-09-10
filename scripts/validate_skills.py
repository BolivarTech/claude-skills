#!/usr/bin/env python3
"""Release gate for the skills in this repository.

Checks the properties that are invisible from the source alone: a skill can be
perfectly well written and still fail on upload, install stale, or ship a
version number that three files disagree about. Each of those only shows up
against the *published* artifact, so the suite of the repo -- there isn't one --
could never see them.

Scenarios are declared before they run and reconciled afterwards, so one that
disappears makes the harness fail instead of quietly shrinking the report.

Outcomes:
    PASS          the property holds
    FAIL          the property is violated
    CANNOT_TEST   tried, the environment did not allow it (never a pass)
    OUT_OF_SCOPE  declared outside this invocation

Exit codes:
    0  every scenario PASS (OUT_OF_SCOPE allowed)
    1  at least one FAIL
    2  the harness itself failed (reconciliation mismatch, unexpected error)
    3  no FAIL, but at least one CANNOT_TEST -- the run is incomplete

Usage::

    python scripts/validate_skills.py            # every skill in the repo
    python scripts/validate_skills.py humanize   # one skill
"""

from __future__ import annotations

import argparse
import enum
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path

import yaml

#: Top-level frontmatter keys accepted outside Claude Code. Anything else makes
#: the Claude Desktop uploader reject the file with "Unexpected key(s)".
ALLOWED_FRONTMATTER_KEYS: frozenset[str] = frozenset(
    {"allowed-tools", "compatibility", "description", "license", "metadata", "name"}
)
#: Keys a skill cannot omit.
REQUIRED_FRONTMATTER_KEYS: frozenset[str] = frozenset({"name", "description"})
#: Where the installed copy -- the one Claude actually executes -- lives.
INSTALL_ROOT: Path = Path.home() / ".claude" / "skills"
#: Semantic version, as stored under ``metadata.version``.
SEMVER: re.Pattern[str] = re.compile(r"^\d+\.\d+\.\d+$")
#: Frontmatter delimited by the first two ``---`` lines of the file.
FRONTMATTER: re.Pattern[str] = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

EXIT_OK, EXIT_FAIL, EXIT_HARNESS, EXIT_INCOMPLETE = 0, 1, 2, 3


class Outcome(enum.Enum):
    """How a scenario ended. Four values, deliberately -- see module docstring."""

    PASS = "PASS"
    FAIL = "FAIL"
    CANNOT_TEST = "CANNOT_TEST"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"


@dataclass(frozen=True)
class Result:
    """One scenario's verdict.

    Attributes:
        skill: Name of the skill the scenario ran against.
        scenario: Scenario identifier, matching the declared list.
        outcome: The verdict.
        detail: One line of evidence. Empty for an unremarkable pass.
    """

    skill: str
    scenario: str
    outcome: Outcome
    detail: str = ""


class HarnessError(RuntimeError):
    """The harness could not do its job. Never a verdict about a skill."""


class SkillPackage:
    """The three copies of one skill, plus the repo files that cite its version.

    A skill lives in three places that must stay byte-identical (source,
    installed copy, zip) and its version is repeated in two more (README table,
    CHANGELOG). This class reads all five and answers questions about them.

    Example:
        >>> pkg = SkillPackage(Path("humanize"), Path("."))
        >>> pkg.version
        '1.1.0'
    """

    def __init__(self, directory: Path, repo_root: Path) -> None:
        """Load a skill from its directory.

        Args:
            directory: The skill directory, named after the skill.
            repo_root: Repository root, holding ``README.md``.

        Raises:
            HarnessError: The directory holds no readable ``SKILL.md``.
        """
        self.name = directory.name
        self.directory = directory
        self.repo_root = repo_root
        self.source = directory / "SKILL.md"
        self.installed = INSTALL_ROOT / self.name / "SKILL.md"
        self.archive = directory / f"{self.name}.zip"
        self.changelog = directory / "CHANGELOG.md"
        try:
            self.raw = self.source.read_bytes()
        except OSError as exc:
            raise HarnessError(f"cannot read {self.source}: {exc}") from exc
        self.frontmatter = self._parse_frontmatter()

    def _parse_frontmatter(self) -> dict:
        """Return the YAML frontmatter as a mapping.

        Returns:
            The parsed mapping, or an empty one when the file has no
            frontmatter block (which the ``frontmatter-keys`` scenario reports).

        Raises:
            HarnessError: The block exists but is not valid YAML mapping.
        """
        match = FRONTMATTER.match(self.raw.decode("utf-8"))
        if match is None:
            return {}
        try:
            parsed = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            raise HarnessError(f"{self.source}: frontmatter is not valid YAML: {exc}")
        if not isinstance(parsed, dict):
            raise HarnessError(f"{self.source}: frontmatter is not a mapping")
        return parsed

    @property
    def version(self) -> str | None:
        """The version under ``metadata.version``, or None if absent."""
        metadata = self.frontmatter.get("metadata")
        if not isinstance(metadata, dict):
            return None
        value = metadata.get("version")
        return str(value) if value is not None else None


class SkillValidator:
    """Runs every scenario against one skill.

    Each ``check_*`` method returns one Result. The scenario list is derived
    from the method names, so a scenario cannot be added without appearing in
    the declared list, and cannot vanish without the reconciliation catching it.
    """

    def __init__(self, package: SkillPackage) -> None:
        """Bind the validator to a skill.

        Args:
            package: The skill to check.
        """
        self.pkg = package

    def scenarios(self) -> list[str]:
        """Return the declared scenario names, in execution order."""
        return [
            name[len("check_") :].replace("_", "-")
            for name in sorted(dir(self))
            if name.startswith("check_")
        ]

    def run(self) -> list[Result]:
        """Execute every scenario.

        Returns:
            One Result per declared scenario, same order.
        """
        results = []
        for scenario in self.scenarios():
            method = getattr(self, "check_" + scenario.replace("-", "_"))
            results.append(method())
        return results

    def _result(self, scenario: str, outcome: Outcome, detail: str = "") -> Result:
        return Result(self.pkg.name, scenario, outcome, detail)

    def check_frontmatter_keys(self) -> Result:
        """Only the six accepted keys, and the two mandatory ones present."""
        keys = set(self.pkg.frontmatter)
        if not keys:
            return self._result("frontmatter-keys", Outcome.FAIL, "no frontmatter block")
        unexpected = sorted(keys - ALLOWED_FRONTMATTER_KEYS)
        missing = sorted(REQUIRED_FRONTMATTER_KEYS - keys)
        problems = []
        if unexpected:
            problems.append(f"unexpected {unexpected} -- breaks the Desktop upload")
        if missing:
            problems.append(f"missing {missing}")
        if self.pkg.frontmatter.get("name") != self.pkg.name:
            problems.append(
                f"name is {self.pkg.frontmatter.get('name')!r}, "
                f"directory is {self.pkg.name!r}"
            )
        if problems:
            return self._result("frontmatter-keys", Outcome.FAIL, "; ".join(problems))
        return self._result("frontmatter-keys", Outcome.PASS)

    def check_version_declared(self) -> Result:
        """``metadata.version`` present and a plain semantic version."""
        version = self.pkg.version
        if version is None:
            return self._result(
                "version-declared", Outcome.FAIL, "metadata.version is absent"
            )
        if not SEMVER.match(version):
            return self._result(
                "version-declared", Outcome.FAIL, f"{version!r} is not X.Y.Z"
            )
        return self._result("version-declared", Outcome.PASS, version)

    def check_installed_copy(self) -> Result:
        """The copy Claude executes is byte-identical to the source."""
        if not self.pkg.installed.exists():
            return self._result(
                "installed-copy",
                Outcome.CANNOT_TEST,
                f"{self.pkg.installed} is absent -- skill not installed here",
            )
        if self.pkg.installed.read_bytes() != self.pkg.raw:
            return self._result(
                "installed-copy",
                Outcome.FAIL,
                f"{self.pkg.installed} differs from the source",
            )
        return self._result("installed-copy", Outcome.PASS)

    def check_package_layout(self) -> Result:
        """The zip holds exactly ``<name>/SKILL.md``, byte-identical.

        The uploader requires the skill folder at the archive root; a flat
        ``SKILL.md`` is rejected, and that is invisible until upload time.
        """
        if not self.pkg.archive.exists():
            return self._result(
                "package-layout", Outcome.FAIL, f"{self.pkg.archive} is absent"
            )
        expected = f"{self.pkg.name}/SKILL.md"
        try:
            with zipfile.ZipFile(self.pkg.archive) as archive:
                names = archive.namelist()
                if names != [expected]:
                    return self._result(
                        "package-layout",
                        Outcome.FAIL,
                        f"holds {names}, expected exactly ['{expected}']",
                    )
                if archive.read(expected) != self.pkg.raw:
                    return self._result(
                        "package-layout",
                        Outcome.FAIL,
                        "the packaged SKILL.md differs from the source",
                    )
        except (zipfile.BadZipFile, OSError) as exc:
            return self._result("package-layout", Outcome.FAIL, f"unreadable: {exc}")
        return self._result("package-layout", Outcome.PASS)

    def check_readme_version(self) -> Result:
        """The README skill table cites the version the frontmatter declares."""
        version = self.pkg.version
        if version is None:
            return self._result(
                "readme-version", Outcome.CANNOT_TEST, "no version to compare against"
            )
        readme = self.pkg.repo_root / "README.md"
        if not readme.exists():
            return self._result("readme-version", Outcome.CANNOT_TEST, "no README.md")
        rows = [
            line
            for line in readme.read_text(encoding="utf-8").splitlines()
            if line.startswith("|") and f"`{self.pkg.name}`" in line
        ]
        if not rows:
            return self._result(
                "readme-version", Outcome.FAIL, "no row for this skill in the table"
            )
        if not any(version in row for row in rows):
            return self._result(
                "readme-version",
                Outcome.FAIL,
                f"table does not cite {version}: {rows[0].strip()}",
            )
        return self._result("readme-version", Outcome.PASS, version)

    def check_changelog_version(self) -> Result:
        """The CHANGELOG carries an entry for the declared version."""
        version = self.pkg.version
        if version is None:
            return self._result(
                "changelog-version", Outcome.CANNOT_TEST, "no version to look for"
            )
        if not self.pkg.changelog.exists():
            return self._result(
                "changelog-version", Outcome.FAIL, f"{self.pkg.changelog} is absent"
            )
        text = self.pkg.changelog.read_text(encoding="utf-8")
        if f"## [{version}]" not in text:
            return self._result(
                "changelog-version", Outcome.FAIL, f"no '## [{version}]' entry"
            )
        return self._result("changelog-version", Outcome.PASS, version)

    def check_trigger_fires(self) -> Result:
        """Whether the description actually triggers the skill.

        Out of scope on purpose: it needs a live session to observe, and a
        harness cannot fake one. Declared so the gap is visible in the report
        rather than absent from it.
        """
        return self._result(
            "trigger-fires",
            Outcome.OUT_OF_SCOPE,
            "needs a live session -- verify by hand after release",
        )


def discover(repo_root: Path, only: str | None) -> list[Path]:
    """Find the skill directories of the repository.

    Args:
        repo_root: Repository root.
        only: Restrict to this skill name, or None for all of them.

    Returns:
        Skill directories, sorted by name.

    Raises:
        HarnessError: ``only`` names a directory with no SKILL.md, or the repo
            holds no skills at all.
    """
    directories = sorted(
        path.parent for path in repo_root.glob("*/SKILL.md") if path.is_file()
    )
    if only is not None:
        directories = [d for d in directories if d.name == only]
        if not directories:
            raise HarnessError(f"no skill named {only!r} with a SKILL.md")
    if not directories:
        raise HarnessError(f"no <name>/SKILL.md found under {repo_root}")
    return directories


def report(results: list[Result], declared: list[tuple[str, str]]) -> int:
    """Print the report and return the process exit code.

    Reconciles what was declared against what reported: a scenario that
    vanishes silently is the one failure mode a report cannot show by itself.

    Args:
        results: Every Result produced by the run.
        declared: The (skill, scenario) pairs declared before running.

    Returns:
        One of the module's exit codes.

    Raises:
        HarnessError: Declared and executed sets differ.
    """
    executed = [(r.skill, r.scenario) for r in results]
    if sorted(executed) != sorted(declared):
        missing = sorted(set(declared) - set(executed))
        extra = sorted(set(executed) - set(declared))
        raise HarnessError(f"declared vs executed mismatch: missing={missing} extra={extra}")

    width = max(len(r.scenario) for r in results)
    for result in results:
        detail = f"  {result.detail}" if result.detail else ""
        print(f"{result.outcome.value:<13} {result.skill}/{result.scenario:<{width}}{detail}")

    tally = {outcome: 0 for outcome in Outcome}
    for result in results:
        tally[result.outcome] += 1
    print(
        "\n"
        + "  ".join(f"{outcome.value}={tally[outcome]}" for outcome in Outcome)
        + f"  ({len(results)} scenarios declared, {len(results)} reported)"
    )

    if tally[Outcome.FAIL]:
        return EXIT_FAIL
    if tally[Outcome.CANNOT_TEST]:
        return EXIT_INCOMPLETE
    return EXIT_OK


def main(argv: list[str] | None = None) -> int:
    """Entry point.

    Args:
        argv: Command-line arguments, defaulting to ``sys.argv[1:]``.

    Returns:
        The process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("skill", nargs="?", help="check only this skill")
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parent.parent
    try:
        packages = [SkillPackage(d, repo_root) for d in discover(repo_root, args.skill)]
        validators = [SkillValidator(pkg) for pkg in packages]
        declared = [(v.pkg.name, s) for v in validators for s in v.scenarios()]
        print(f"declared {len(declared)} scenarios over {len(packages)} skill(s)\n")
        results = [result for v in validators for result in v.run()]
        return report(results, declared)
    except HarnessError as exc:
        print(f"HARNESS FAILURE: {exc}", file=sys.stderr)
        return EXIT_HARNESS


if __name__ == "__main__":
    sys.exit(main())
