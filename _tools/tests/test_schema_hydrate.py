"""Tests for cex_schema_hydrate.py -- frontmatter hydration."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_schema_hydrate import (extract_keywords_from_body,
                                extract_triggers_from_body, insert_fm_fields,
                                reassemble, split_fm, yaml_field)


class TestSplitFm:
    def test_valid_frontmatter(self):
        content = "---\nid: test\nkind: agent\n---\n# Body\nContent"
        fm, raw_fm, body = split_fm(content)
        assert fm["id"] == "test"
        assert fm["kind"] == "agent"
        assert "# Body" in body

    def test_no_frontmatter(self):
        content = "# Just body\nNo frontmatter"
        fm, raw_fm, body = split_fm(content)
        assert fm == {} or fm is None or raw_fm == ""

    def test_preserves_body(self):
        content = "---\nid: x\n---\n# Title\nParagraph 1\nParagraph 2"
        fm, raw_fm, body = split_fm(content)
        assert "Paragraph 1" in body
        assert "Paragraph 2" in body


class TestInsertFmFields:
    def test_adds_new_field(self):
        raw = "id: test\nkind: agent"
        result = insert_fm_fields(raw, {"version": "1.0.0"})
        assert "version" in result
        assert "1.0.0" in result

    def test_preserves_existing(self):
        raw = "id: test\nkind: agent"
        result = insert_fm_fields(raw, {"pillar": "P01"})
        assert "id: test" in result
        assert "kind: agent" in result


class TestYamlField:
    def test_string(self):
        assert "name: hello" in yaml_field("name", "hello")

    def test_list(self):
        result = yaml_field("tags", ["a", "b", "c"])
        assert "tags:" in result
        assert "a" in result

    def test_number(self):
        assert "score: 8.5" in yaml_field("score", 8.5)


class TestReassemble:
    def test_roundtrip(self):
        raw_fm = "id: test\nkind: agent"
        body = "# Title\nContent"
        result = reassemble(raw_fm, body)
        assert result.startswith("---")
        assert "# Title" in result
        assert "Content" in result


class TestExtractKeywords:
    def test_from_headings(self):
        body = "# Railway Deploy\n## Health Check\n### PostgreSQL Setup\nSome content."
        keywords = extract_keywords_from_body(body)
        assert isinstance(keywords, list)

    def test_empty(self):
        keywords = extract_keywords_from_body("")
        assert isinstance(keywords, list)


class TestExtractTriggers:
    def test_from_body(self):
        body = "When user asks to deploy, create a rollback plan. If health check fails, run diagnostics."
        triggers = extract_triggers_from_body(body)
        assert isinstance(triggers, list)
