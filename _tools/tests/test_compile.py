"""Tests for cex_compile.py -- Markdown to YAML compilation."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_compile import parse_frontmatter


class TestCompileParseFrontmatter:
    @pytest.mark.unit
    def test_valid_frontmatter(self):
        fm, body = parse_frontmatter(
            "---\nid: test\nkind: kc\npillar: P01\n---\n# Body\nContent"
        )
        assert fm["id"] == "test"
        assert "Body" in body

    @pytest.mark.unit
    def test_no_frontmatter(self):
        fm, body = parse_frontmatter("# Just markdown")
        assert fm == {} or fm is None
        assert "markdown" in body

    @pytest.mark.unit
    def test_empty_content(self):
        _fm, body = parse_frontmatter("")
        # Should handle gracefully
        assert isinstance(body, str)

    @pytest.mark.unit
    def test_frontmatter_with_all_fields(self):
        content = (
            "---\n"
            "id: full_test\n"
            "kind: knowledge_card\n"
            "pillar: P01\n"
            "title: Test\n"
            "version: 1.0.0\n"
            "quality: 8.5\n"
            "tags: [a, b]\n"
            "---\n"
            "# Body"
        )
        fm, _body = parse_frontmatter(content)
        assert fm["id"] == "full_test"
        assert fm["quality"] == 8.5
        assert fm["tags"] == ["a", "b"]

    @pytest.mark.unit
    def test_frontmatter_preserves_types(self):
        content = "---\ncount: 42\nenabled: true\nscore: 8.5\n---\n"
        fm, _ = parse_frontmatter(content)
        if fm:
            assert isinstance(fm.get("count"), int)
            assert isinstance(fm.get("enabled"), bool)
            assert isinstance(fm.get("score"), float)
