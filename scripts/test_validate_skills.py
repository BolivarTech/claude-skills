"""Regression tests for package metadata and optional installation checks."""

import tempfile
import unittest
from pathlib import Path

import yaml

from validate_skills import Outcome, SkillPackage, SkillValidator


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.directory = self.root / "humanize"
        self.directory.mkdir()

    def package(self, **overrides):
        metadata = dict(name="humanize", description="Rewrite prose.",
                        metadata={"version": "3.0.0"})
        metadata.update(overrides)
        (self.directory / "SKILL.md").write_text(
            "---\n" + yaml.safe_dump(metadata) + "---\nText.\n", encoding="utf-8"
        )
        return SkillPackage(self.directory, self.root)

    def test_required_text_fields(self):
        self.assertEqual(SkillValidator(self.package()).check_frontmatter_keys().outcome,
                         Outcome.PASS)
        for field in ("name", "description"):
            for value in (None, "", "  ", 12, [], {}):
                with self.subTest(field=field, value=value):
                    result = SkillValidator(self.package(**{field: value})).check_frontmatter_keys()
                    self.assertEqual(result.outcome, Outcome.FAIL)

    def test_exact_readme_version_cell(self):
        validator = SkillValidator(self.package())
        for value, expected in (
            ("3.0.0", Outcome.PASS),
            ("[3.0.0](humanize/CHANGELOG.md)", Outcome.PASS),
            ("13.0.0", Outcome.FAIL),
            ("3.0.01", Outcome.FAIL),
            ("[13.0.0](humanize/CHANGELOG.md#3.0.0)", Outcome.FAIL),
        ):
            with self.subTest(value=value):
                (self.root / "README.md").write_text(
                    f"| `humanize` | {value} | supports 3.0.0 |\n", encoding="utf-8"
                )
                self.assertEqual(validator.check_readme_version().outcome, expected)

    def test_optional_installed_copy(self):
        package = self.package()
        package.installed = self.root / "installed.md"
        default = SkillValidator(package)
        enabled = SkillValidator(package, check_installed=True)
        self.assertEqual(default.check_installed_copy().outcome, Outcome.OUT_OF_SCOPE)
        self.assertEqual(enabled.check_installed_copy().outcome, Outcome.CANNOT_TEST)
        package.installed.write_bytes(b"outdated")
        self.assertEqual(default.check_installed_copy().outcome, Outcome.OUT_OF_SCOPE)
        self.assertEqual(enabled.check_installed_copy().outcome, Outcome.FAIL)
        package.installed.write_bytes(package.raw)
        self.assertEqual(enabled.check_installed_copy().outcome, Outcome.PASS)


if __name__ == "__main__":
    unittest.main()
