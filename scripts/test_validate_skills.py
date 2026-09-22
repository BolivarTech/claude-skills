"""Regression tests for package metadata and optional installation checks."""

import tempfile
import unittest
import zipfile
from pathlib import Path

import yaml

from validate_skills import (
    Outcome,
    SkillPackage,
    SkillValidator,
    SkillVariant,
    VariantValidator,
    discover_variants,
)


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


class VariantTests(unittest.TestCase):
    """A variant is ``<name>/<variant>/SKILL.md``: same skill, another target."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.directory = self.root / "humanize"
        self.directory.mkdir()
        self.write_skill(self.directory, "humanize", "3.0.0")
        self.parent = SkillPackage(self.directory, self.root)
        self.variant_dir = self.directory / "chatgpt"
        self.variant_dir.mkdir()

    @staticmethod
    def write_skill(directory, name, version):
        metadata = dict(name=name, description="Rewrite prose.",
                        metadata={"version": version})
        (directory / "SKILL.md").write_text(
            "---\n" + yaml.safe_dump(metadata) + "---\nText.\n", encoding="utf-8"
        )

    def variant(self, name="humanize", version="3.0.0"):
        self.write_skill(self.variant_dir, name, version)
        return SkillVariant(self.variant_dir, self.parent)

    def test_variant_is_labelled_under_its_parent(self):
        variant = self.variant()
        self.assertEqual(variant.label, "humanize/chatgpt")
        self.assertEqual(variant.archive, self.variant_dir / "humanize-chatgpt.zip")
        self.assertEqual(VariantValidator(variant).scenarios(),
                         ["frontmatter-keys", "package-layout", "source-identical",
                          "version-declared"])

    def test_variant_text_must_equal_parent_text(self):
        self.assertEqual(VariantValidator(self.variant()).check_source_identical().outcome,
                         Outcome.PASS)
        (self.variant_dir / "SKILL.md").write_bytes(self.parent.raw + b"One more rule.\n")
        variant = SkillVariant(self.variant_dir, self.parent)
        self.assertEqual(VariantValidator(variant).check_source_identical().outcome,
                         Outcome.FAIL)

    def test_variant_name_must_match_parent(self):
        self.assertEqual(VariantValidator(self.variant()).check_frontmatter_keys().outcome,
                         Outcome.PASS)
        self.assertEqual(VariantValidator(self.variant(name="chatgpt")).check_frontmatter_keys().outcome,
                         Outcome.FAIL)

    def test_variant_version_must_equal_parent_version(self):
        self.assertEqual(VariantValidator(self.variant()).check_version_declared().outcome,
                         Outcome.PASS)
        for version in ("3.0.1", "13.0.0", "3.0"):
            with self.subTest(version=version):
                result = VariantValidator(self.variant(version=version)).check_version_declared()
                self.assertEqual(result.outcome, Outcome.FAIL)

    def test_variant_archive_holds_parent_folder(self):
        variant = self.variant()
        validator = VariantValidator(variant)
        self.assertEqual(validator.check_package_layout().outcome, Outcome.FAIL)
        for entry, payload, expected in (
            ("humanize/SKILL.md", variant.raw, Outcome.PASS),
            ("chatgpt/SKILL.md", variant.raw, Outcome.FAIL),
            ("humanize/SKILL.md", b"stale", Outcome.FAIL),
        ):
            with self.subTest(entry=entry, payload=payload):
                with zipfile.ZipFile(variant.archive, "w") as archive:
                    archive.writestr(entry, payload)
                self.assertEqual(validator.check_package_layout().outcome, expected)

    def test_variant_archive_carries_every_file_beside_its_skill(self):
        """A Codex variant ships ``agents/openai.yaml`` next to its SKILL.md.

        The zip must hold that file too, under the parent folder, and the
        archive itself is never one of the expected entries.
        """
        self.variant_dir = self.directory / "codex"
        self.variant_dir.mkdir()
        variant = self.variant()
        (self.variant_dir / "agents").mkdir()
        manifest = b"interface:\n  display_name: Humanize\n"
        (self.variant_dir / "agents" / "openai.yaml").write_bytes(manifest)
        variant = SkillVariant(self.variant_dir, self.parent)
        self.assertEqual(variant.archive, self.variant_dir / "humanize-codex.zip")
        validator = VariantValidator(variant)
        for entries, expected in (
            ({"humanize/SKILL.md": variant.raw}, Outcome.FAIL),
            ({"humanize/SKILL.md": variant.raw,
              "humanize/agents/openai.yaml": manifest}, Outcome.PASS),
            ({"humanize/SKILL.md": variant.raw,
              "humanize/agents/openai.yaml": b"stale"}, Outcome.FAIL),
            ({"humanize/SKILL.md": variant.raw,
              "humanize/agents/openai.yaml": manifest,
              "humanize/extra.md": b"x"}, Outcome.FAIL),
        ):
            with self.subTest(entries=sorted(entries)):
                with zipfile.ZipFile(variant.archive, "w") as archive:
                    for entry, payload in entries.items():
                        archive.writestr(entry, payload)
                self.assertEqual(validator.check_package_layout().outcome, expected)

    def test_discover_variants_finds_only_nested_skill_files(self):
        self.variant()
        (self.directory / "notes").mkdir()
        (self.directory / "notes" / "README.md").write_text("x", encoding="utf-8")
        self.assertEqual(discover_variants(self.directory), [self.variant_dir])
        self.assertEqual(discover_variants(self.root / "missing"), [])


if __name__ == "__main__":
    unittest.main()
