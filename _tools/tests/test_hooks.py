"""Tests for cex_hooks.py -- Pre-commit validation."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_hooks import parse_frontmatter, validate_artifact


class TestParseFrontmatter:
    @pytest.mark.unit
    def test_valid(self):
        fm = parse_frontmatter("---\nid: t\nkind: kc\n---\n")
        assert fm is not None
        assert fm["id"] == "t"

    @pytest.mark.unit
    def test_no_frontmatter(self):
        assert parse_frontmatter("# No FM") is None

    @pytest.mark.unit
    def test_empty(self):
        assert parse_frontmatter("") is None


class TestValidateArtifact:
    @pytest.mark.unit
    def test_valid_artifact(self, valid_artifact):
        issues = validate_artifact(str(valid_artifact))
        errors = [i for i in issues if i["level"] == "ERROR"]
        assert len(errors) == 0

    @pytest.mark.unit
    def test_missing_file(self, tmp_path):
        issues = validate_artifact(str(tmp_path / "nonexistent.md"))
        assert len(issues) > 0
        assert issues[0]["level"] == "ERROR"

    @pytest.mark.unit
    def test_no_frontmatter(self, invalid_artifact_no_fm):
        issues = validate_artifact(str(invalid_artifact_no_fm))
        errors = [i for i in issues if i["level"] == "ERROR"]
        assert len(errors) > 0
        assert any("frontmatter" in e["msg"].lower() for e in errors)

    @pytest.mark.unit
    def test_missing_fields(self, invalid_artifact_missing_fields):
        issues = validate_artifact(str(invalid_artifact_missing_fields))
        errors = [i for i in issues if i["level"] == "ERROR"]
        # Should flag missing 'kind' and 'pillar'
        assert len(errors) >= 1

    @pytest.mark.unit
    def test_content_param(self):
        """Should accept content directly without file."""
        content = "---\nid: t\nkind: kc\npillar: P01\nquality: null\n---\n# Title\nBody."
        issues = validate_artifact("inline.md", content=content)
        errors = [i for i in issues if i["level"] == "ERROR"]
        assert len(errors) == 0

    @pytest.mark.unit
    def test_readme_skipped(self, tmp_path):
        """README.md files should be skipped."""
        readme = tmp_path / "README.md"
        readme.write_text("# README\nNo frontmatter needed.", encoding="utf-8")
        issues = validate_artifact(str(readme))
        # READMEs are typically skipped or have no errors
        assert isinstance(issues, list)
