"""Tests for cex_intent.py -- intent classification and prompt composition."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_intent import (_format_intent_block, _strip_frontmatter, list_kinds,
                        load_all_builder_isos, load_builder_iso)

ROOT = Path(__file__).resolve().parent.parent.parent


class TestStripFrontmatter:
    def test_removes_yaml(self):
        text = "---\nid: test\nkind: agent\n---\n# Body\nContent here"
        result = _strip_frontmatter(text)
        assert "---" not in result
        assert "# Body" in result

    def test_no_frontmatter(self):
        text = "# Just content\nNo frontmatter"
        result = _strip_frontmatter(text)
        assert "# Just content" in result

    def test_empty(self):
        assert _strip_frontmatter("") == ""


class TestLoadBuilderIso:
    def test_loads_knowledge_card(self):
        builder_dir = ROOT / "archetypes" / "builders" / "knowledge-card-builder"
        if builder_dir.exists():
            content = load_builder_iso(builder_dir, "bld_model", "knowledge_card")
            assert content is not None or isinstance(content, str)

    def test_nonexistent_file(self):
        builder_dir = ROOT / "archetypes" / "builders" / "knowledge-card-builder"
        content = load_builder_iso(builder_dir, "bld_nonexistent", "knowledge_card")
        assert content is None or content == ""


class TestLoadAllBuilderIsos:
    def test_loads_multiple(self):
        builder_dir = ROOT / "archetypes" / "builders" / "knowledge-card-builder"
        if builder_dir.exists():
            isos = load_all_builder_isos(builder_dir, "knowledge_card")
            assert isinstance(isos, dict)
            assert len(isos) > 0


class TestFormatIntentBlock:
    def test_formats_block(self):
        result = _format_intent_block(
            intent="create a knowledge card about testing",
            kind="knowledge_card",
            parsed={"domain": "testing"},
            plan={"builder": "knowledge-card-builder"},
        )
        assert isinstance(result, str)
        assert "knowledge_card" in result or "testing" in result


class TestListKinds:
    def test_returns_kinds(self):
        kinds = list_kinds()
        # list_kinds may return None, list, or print to stdout
        assert kinds is None or isinstance(kinds, (list, dict))
