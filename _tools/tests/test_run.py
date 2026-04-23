"""Tests for cex_run.py -- unified E2E entry point."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_run import discover, extract_artifact, plan, resolve_output_path

ROOT = Path(__file__).resolve().parent.parent.parent


class TestDiscover:
    def test_returns_list(self):
        results = discover("create a knowledge card about testing")
        assert isinstance(results, list)

    def test_finds_knowledge_card_builder(self):
        results = discover("create a knowledge card")
        if results:
            kinds = [r.get("kind", "") for r in results]
            assert any("knowledge" in k for k in kinds)

    def test_empty_intent(self):
        results = discover("")
        assert isinstance(results, list)


class TestPlan:
    def test_returns_dict(self):
        p = plan("create a knowledge card about API design")
        assert isinstance(p, dict)

    def test_has_classified_kinds(self):
        p = plan("create a knowledge card")
        # plan returns full execution plan with classified_kinds
        assert "classified_kinds" in p or "kind" in p or "functions" in p


class TestExtractArtifact:
    def test_extracts_frontmatter(self):
        response = "Here is the artifact:\n---\nid: test_1\nkind: knowledge_card\nquality: null\n---\n# Title\nContent body here."
        content, fm = extract_artifact(response, "knowledge_card", "test intent")
        assert "---" in content
        assert "# Title" in content

    def test_no_frontmatter(self):
        response = "Just plain text without any YAML frontmatter."
        content, fm = extract_artifact(response, "agent", "test")
        assert isinstance(content, str)

    def test_empty_response(self):
        content, fm = extract_artifact("", "agent", "test")
        assert content == "" or isinstance(content, str)


class TestResolveOutputPath:
    def test_knowledge_card(self):
        path = resolve_output_path("knowledge_card", "testing", "create kc about API")
        assert isinstance(path, Path)
        assert "P01" in str(path) or "knowledge" in str(path).lower()

    def test_agent(self):
        path = resolve_output_path("agent", "engineering", "create agent")
        assert isinstance(path, Path)

    def test_workflow(self):
        path = resolve_output_path("workflow", "operations", "deploy workflow")
        assert isinstance(path, Path)
