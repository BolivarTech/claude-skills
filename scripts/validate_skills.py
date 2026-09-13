#!/usr/bin/env python3
"""Release gate for the skills in this repository.

Checks the properties that are invisible from the source alone: a skill can be
perfectly well written and still fail on upload, install stale, or ship a
version number that three files disagree about. Each of those only shows up
against the *published* artifact, so the suite of the repo -- there isn't one --
could never see them.

Scenarios are declared before they run and reconciled afterwards, so one that
disappears makes the harness fail instead of quietly shrinking the report.

A skill may carry variants for other targets at ``<name>/<variant>/SKILL.md``,
packaged as ``<name>-<variant>.zip`` next to them. A variant is checked for
its frontmatter, its zip, and a version equal to the parent's; it releases
with the parent, so the README and CHANGELOG checks stay the parent's.

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
    python scripts/validate_skills.py --check-installed  # also check local copies
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


class SkillSource:
    """One ``SKILL.md`` on disk: its bytes and its parsed frontmatter.

    Base for the skill proper and for its variants; both are a Markdown file
    with a frontmatter block, and only the files around them differ.
    """

    def __init__(self, directory: Path) -> None:
        """Read ``<directory>/SKILL.md``.

        Args:
            directory: The directory holding the file.

        Raises:
            HarnessError: The directory holds no readable ``SKILL.md``.
        """
        self.directory = directory
        self.source = directory / "SKILL.md"
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


class SkillPackage(SkillSource):
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
        super().__init__(directory)
        self.name = directory.name
        self.repo_root = repo_root
        self.installed = INSTALL_ROOT / self.name / "SKILL.md"
        self.archive = directory / f"{self.name}.zip"
        self.changelog = directory / "CHANGELOG.md"


class SkillVariant(SkillSource):
    """A skill rewritten for another target, kept under its parent.

    Lives at ``<name>/<variant>/SKILL.md`` and ships as
    ``<name>/<variant>/<name>-<variant>.zip``. It carries the parent's name
    and version: it is the same skill, released together with it, not a
    sibling with a life of its own.

    Example:
        >>> variant = SkillVariant(Path("humanize/chatgpt"), pkg)
        >>> variant.label
        'humanize/chatgpt'
    """

    def __init__(self, directory: Path, parent: SkillPackage) -> None:
        """Load a variant from its directory.

        Args:
            directory: The variant directory, inside the parent's.
            parent: The skill this is a variant of.

        Raises:
            HarnessError: The directory holds no readable ``SKILL.md``.
        """
        super().__init__(directory)
        self.parent = parent
        self.variant = directory.name
        self.label = f"{parent.name}/{self.variant}"
        self.archive = directory / f"{parent.name}-{self.variant}.zip"


def frontmatter_problems(frontmatter: dict, expected_name: str) -> list[str]:
    """List what is wrong with a frontmatter block, empty when nothing is.

    Args:
        frontmatter: The parsed block, empty when the file has none.
        expected_name: The ``name`` the block must declare.

    Returns:
        One human-readable problem per line, in a stable order.
    """
    keys = set(frontmatter)
    if not keys:
        return ["no frontmatter block"]
    unexpected = sorted(keys - ALLOWED_FRONTMATTER_KEYS)
    missing = sorted(REQUIRED_FRONTMATTER_KEYS - keys)
    problems = []
    if unexpected:
        problems.append(f"unexpected {unexpected} -- breaks the Desktop upload")
    if missing:
        problems.append(f"missing {missing}")
    for key in sorted(REQUIRED_FRONTMATTER_KEYS & keys):
        value = frontmatter[key]
        if not isinstance(value, str) or not value.strip():
            problems.append(f"{key} must be a non-empty string")
    if frontmatter.get("name") != expected_name:
        problems.append(
            f"name is {frontmatter.get('name')!r}, expected {expected_name!r}"
        )
    return problems


def archive_problem(archive: Path, expected_entry: str, raw: bytes) -> str:
    """Say why a zip is not exactly one entry holding ``raw``, or nothing.

    The uploader requires the skill folder at the archive root; a flat
    ``SKILL.md`` is rejected, and that is invisible until upload time.

    Args:
        archive: The zip to inspect.
        expected_entry: The one path the archive must hold.
        raw: The bytes that entry must carry.

    Returns:
        The problem, or an empty string when the layout is right.
    """
    if not archive.exists():
        return f"{archive} is absent"
    try:
        with zipfile.ZipFile(archive) as package:
            names = package.namelist()
            if names != [expected_entry]:
                return f"holds {names}, expected exactly ['{expected_entry}']"
            if package.read(expected_entry) != raw:
                return "the packaged SKILL.md differs from the source"
    except (zipfile.BadZipFile, OSError) as exc:
        return f"unreadable: {exc}"
    return ""


class ScenarioRunner:
    """Runs every ``check_*`` method of a subclass, in declared order.

    Each ``check_*`` method returns one Result. The scenario list is derived
    from the method names, so a scenario cannot be added without appearing in
    the declared list, and cannot vanish without the reconciliation catching it.
    Subclasses set ``self.label``, the name the results are reported under.
    """

    label: str

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
        return Result(self.label, scenario, outcome, detail)


class SkillValidator(ScenarioRunner):
    """Runs every scenario against one skill."""

    def __init__(self, package: SkillPackage, *, check_installed: bool = False) -> None:
        """Bind the validator to a skill.

        Args:
            package: The skill to check.
            check_installed: Also compare the personal installation with the source.
        """
        self.pkg = package
        self.label = package.name
        self.include_installed = check_installed

    def check_frontmatter_keys(self) -> Result:
        """Only the six accepted keys, and the two mandatory ones present."""
        problems = frontmatter_problems(self.pkg.frontmatter, self.pkg.name)
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
        if not self.include_installed:
            return self._result(
                "installed-copy", Outcome.OUT_OF_SCOPE,
                "use --check-installed to compare the personal installation",
            )
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
        problem = archive_problem(
            self.pkg.archive, f"{self.pkg.name}/SKILL.md", self.pkg.raw
        )
        if problem:
            return self._result("package-layout", Outcome.FAIL, problem)
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
        version_cells = [row.split("|")[2].strip() for row in rows if len(row.split("|")) >= 4]
        def version_label(cell: str) -> str:
            link = re.fullmatch(r"\[([^\]]+)\]\([^\n]+\)", cell)
            return link.group(1) if link else cell

        if len(rows) != 1 or len(version_cells) != 1 or version_label(version_cells[0]) != version:
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


class VariantValidator(ScenarioRunner):
    """Runs the scenarios a variant answers for itself.

    Three of them: its frontmatter, its version (which must equal the
    parent's, since they release together) and its zip. Installation,
    README and CHANGELOG are the parent's business.
    """

    def __init__(self, variant: SkillVariant) -> None:
        """Bind the validator to a variant.

        Args:
            variant: The variant to check.
        """
        self.variant = variant
        self.label = variant.label

    def check_frontmatter_keys(self) -> Result:
        """Same accepted keys as the parent, and the parent's ``name``."""
        problems = frontmatter_problems(self.variant.frontmatter, self.variant.parent.name)
        if problems:
            return self._result("frontmatter-keys", Outcome.FAIL, "; ".join(problems))
        return self._result("frontmatter-keys", Outcome.PASS)

    def check_version_declared(self) -> Result:
        """``metadata.version`` equal to the parent's."""
        version = self.variant.version
        expected = self.variant.parent.version
        if version is None:
            return self._result(
                "version-declared", Outcome.FAIL, "metadata.version is absent"
            )
        if version != expected:
            return self._result(
                "version-declared",
                Outcome.FAIL,
                f"{version!r} differs from the parent's {expected!r}",
            )
        return self._result("version-declared", Outcome.PASS, version)

    def check_package_layout(self) -> Result:
        """The zip holds exactly ``<parent name>/SKILL.md``, byte-identical."""
        problem = archive_problem(
            self.variant.archive, f"{self.variant.parent.name}/SKILL.md", self.variant.raw
        )
        if problem:
            return self._result("package-layout", Outcome.FAIL, problem)
        return self._result("package-layout", Outcome.PASS)


def discover_variants(skill_directory: Path) -> list[Path]:
    """Find the variant directories nested inside one skill directory.

    Args:
        skill_directory: The skill directory to look under.

    Returns:
        Directories holding a ``SKILL.md``, sorted by name. Empty when there
        are none or the skill directory does not exist.
    """
    return sorted(
        path.parent for path in skill_directory.glob("*/SKILL.md") if path.is_file()
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
    parser.add_argument(
        "--check-installed", action="store_true",
        help="also compare personal copies under ~/.claude/skills with the source",
    )
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parent.parent
    try:
        packages = [SkillPackage(d, repo_root) for d in discover(repo_root, args.skill)]
        validators: list[ScenarioRunner] = []
        for pkg in packages:
            validators.append(SkillValidator(pkg, check_installed=args.check_installed))
            validators.extend(
                VariantValidator(SkillVariant(d, pkg)) for d in discover_variants(pkg.directory)
            )
        declared = [(v.label, s) for v in validators for s in v.scenarios()]
        print(f"declared {len(declared)} scenarios over {len(packages)} skill(s)\n")
        results = [result for v in validators for result in v.run()]
        return report(results, declared)
    except HarnessError as exc:
        print(f"HARNESS FAILURE: {exc}", file=sys.stderr)
        return EXIT_HARNESS


if __name__ == "__main__":
    sys.exit(main())
