"""Tests for cex_shared.py -- the shared library."""

import json

import pytest
from cex_errors import ConfigError
from cex_shared import (BUILDER_DIR, CEX_ROOT, ensure_dir,
                        extract_frontmatter_dict, find_builder_dir,
                        load_all_isos, load_iso, load_kinds_meta, load_yaml,
                        parse_frontmatter, slugify, split_frontmatter,
                        strip_frontmatter, write_signal)

# =============================================================================
# CEX_ROOT
# =============================================================================

class TestCEXRoot:
    @pytest.mark.unit
    def test_cex_root_exists(self):
        assert CEX_ROOT.exists()

    @pytest.mark.unit
    def test_cex_root_has_tools(self):
        assert (CEX_ROOT / "_tools").exists()

    @pytest.mark.unit
    def test_builder_dir_exists(self):
        assert BUILDER_DIR.exists()


# =============================================================================
# Frontmatter Parsing
# =============================================================================

class TestParseFrontmatter:
    @pytest.mark.unit
    def test_valid_frontmatter(self):
        content = "---\nid: test\nkind: agent\npillar: P03\n---\n# Body"
        fm = parse_frontmatter(content)
        assert fm is not None
        assert fm["id"] == "test"
        assert fm["kind"] == "agent"

    @pytest.mark.unit
    def test_no_frontmatter(self):
        assert parse_frontmatter("# Just markdown") is None

    @pytest.mark.unit
    def test_empty_string(self):
        assert parse_frontmatter("") is None

    @pytest.mark.unit
    def test_incomplete_frontmatter(self):
        assert parse_frontmatter("---\nid: test\nno closing") is None

    @pytest.mark.unit
    def test_invalid_yaml(self):
        assert parse_frontmatter("---\n: : invalid\n---\n") is None

    @pytest.mark.unit
    def test_frontmatter_with_lists(self):
        content = "---\nid: t\ntags: [a, b, c]\n---\n"
        fm = parse_frontmatter(content)
        assert fm["tags"] == ["a", "b", "c"]

    @pytest.mark.unit
    def test_frontmatter_quality_null(self):
        content = "---\nid: t\nquality: null\n---\n"
        fm = parse_frontmatter(content)
        assert fm["quality"] is None


class TestStripFrontmatter:
    @pytest.mark.unit
    def test_strips_frontmatter(self):
        text = "---\nid: test\n---\n# Body\nContent"
        assert strip_frontmatter(text) == "# Body\nContent"

    @pytest.mark.unit
    def test_no_frontmatter_returns_original(self):
        text = "# Just body"
        assert strip_frontmatter(text) == text

    @pytest.mark.unit
    def test_strips_whitespace(self):
        text = "---\nid: t\n---\n\n\n  # Body  \n"
        result = strip_frontmatter(text)
        assert result.startswith("# Body")


class TestExtractFrontmatterDict:
    @pytest.mark.unit
    def test_standard_delimiters(self):
        text = "---\nid: test\nkind: agent\n---\n# Body"
        fm = extract_frontmatter_dict(text)
        assert fm["id"] == "test"

    @pytest.mark.unit
    def test_code_fenced_yaml(self):
        text = "```yaml\nid: test\nkind: agent\n```\n# Body"
        fm = extract_frontmatter_dict(text)
        assert fm.get("id") == "test"

    @pytest.mark.unit
    def test_no_frontmatter_returns_empty(self):
        assert extract_frontmatter_dict("# Just text") == {}

    @pytest.mark.unit
    def test_empty_string(self):
        assert extract_frontmatter_dict("") == {}


class TestSplitFrontmatter:
    @pytest.mark.unit
    def test_split_valid(self):
        content = "---\nid: x\n---\n# Body"
        fm, body = split_frontmatter(content)
        assert fm["id"] == "x"
        assert body == "# Body"

    @pytest.mark.unit
    def test_split_no_frontmatter(self):
        content = "# No FM"
        fm, body = split_frontmatter(content)
        assert fm == {}
        assert body == content


# =============================================================================
# Builder Operations
# =============================================================================

class TestFindBuilderDir:
    @pytest.mark.integration
    def test_find_known_kind(self):
        """Should find builder for knowledge_card (exists in real repo)."""
        result = find_builder_dir("knowledge_card")
        assert result is not None
        assert result.exists()

    @pytest.mark.integration
    def test_find_unknown_kind(self):
        assert find_builder_dir("nonexistent_kind_xyz") is None


class TestLoadIso:
    @pytest.mark.unit
    def test_load_existing_iso(self, sample_builder):
        content = load_iso(sample_builder, "bld_prompt", "knowledge_card")
        assert "Prompt" in content

    @pytest.mark.unit
    def test_load_missing_iso(self, sample_builder):
        content = load_iso(sample_builder, "bld_nonexistent", "knowledge_card")
        assert content == ""


class TestLoadAllIsos:
    @pytest.mark.unit
    def test_load_all(self, sample_builder):
        isos = load_all_isos(sample_builder, "knowledge_card")
        assert "model" in isos or "prompt" in isos
        assert len(isos) >= 2


# =============================================================================
# YAML Utilities
# =============================================================================

class TestLoadYaml:
    @pytest.mark.unit
    def test_load_valid_yaml(self, tmp_path):
        f = tmp_path / "test.yaml"
        f.write_text("key: value\nlist:\n  - a\n  - b\n", encoding="utf-8")
        result = load_yaml(f)
        assert result["key"] == "value"
        assert result["list"] == ["a", "b"]

    @pytest.mark.unit
    def test_load_missing_file(self, tmp_path):
        with pytest.raises(ConfigError):
            load_yaml(tmp_path / "missing.yaml")


class TestLoadKindsMeta:
    @pytest.mark.integration
    def test_loads_real_kinds_meta(self):
        """Should load the real kinds_meta.json from repo."""
        kinds = load_kinds_meta()
        assert len(kinds) >= 90  # We have 99 kinds
        assert "knowledge_card" in kinds


# =============================================================================
# File Utilities
# =============================================================================

class TestEnsureDir:
    @pytest.mark.unit
    def test_creates_nested_dirs(self, tmp_path):
        target = tmp_path / "a" / "b" / "c"
        result = ensure_dir(target)
        assert target.exists()
        assert result == target

    @pytest.mark.unit
    def test_existing_dir_ok(self, tmp_path):
        ensure_dir(tmp_path)  # Already exists, should not raise


class TestWriteSignal:
    @pytest.mark.unit
    def test_writes_signal_file(self, tmp_path, monkeypatch):
        import cex_shared
        monkeypatch.setattr(cex_shared, "RUNTIME_DIR", tmp_path / ".cex" / "runtime")
        path = write_signal("N03", "test_task", "complete", {"detail": "ok"})
        assert path.exists()
        data = json.loads(path.read_text())
        assert data["nucleus"] == "N03"
        assert data["status"] == "complete"


class TestSlugify:
    @pytest.mark.unit
    @pytest.mark.parametrize("input_text,expected", [
        ("Hello World", "hello-world"),
        ("knowledge_card", "knowledge-card"),
        ("  spaces  ", "spaces"),
        ("Special!@#Chars", "specialchars"),
        ("Multiple---Dashes", "multiple-dashes"),
    ])
    def test_slugify(self, input_text, expected):
        assert slugify(input_text) == expected
