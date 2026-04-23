"""Unit tests for cex_router_v2.py -- kind-based smart routing (W4).

Tests verify:
  - requires_live_tools -> Claude-only routing
  - requires_external_context -> preflight_needed flag + any-runtime backend
  - structural kinds -> fall through to signature routing
  - kind inference from handoff files
  - route_task() unified entry point
  - graceful handling of missing/unknown kinds
"""
from __future__ import annotations

import os
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import cex_router_v2 as router

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_kinds_meta(**kinds: dict[str, Any]) -> dict[str, Any]:
    """Build a kinds_meta dict from keyword args.

    Example: _make_kinds_meta(browser_tool={"requires_live_tools": True})
    """
    return kinds


def _stub_meta(kind: str, ext: bool = False, live: bool = False) -> dict[str, Any]:
    return {
        kind: {
            "requires_external_context": ext,
            "requires_live_tools": live,
            "pillar": "P01",
            "description": "test kind",
        }
    }


def _patch_meta(meta: dict[str, Any]):
    """Patch _load_kinds_meta to return given dict."""
    return unittest.mock.patch.object(
        router, "_load_kinds_meta", return_value=meta
    )


def _patch_credit(ok: bool = True):
    return unittest.mock.patch.object(router, "anthropic_credit_ok", return_value=ok)


# ---------------------------------------------------------------------------
# Tests: get_kind_metadata
# ---------------------------------------------------------------------------

class TestGetKindMetadata(unittest.TestCase):
    def test_returns_metadata_for_known_kind(self):
        meta = _stub_meta("agent", ext=False, live=False)
        with _patch_meta(meta):
            km = router.get_kind_metadata("agent")
        assert km["requires_external_context"] is False
        assert km["requires_live_tools"] is False

    def test_returns_empty_for_unknown_kind(self):
        with _patch_meta({}):
            km = router.get_kind_metadata("nonexistent_kind_xyz")
        assert km == {}

    def test_returns_empty_for_empty_string(self):
        km = router.get_kind_metadata("")
        assert km == {}


# ---------------------------------------------------------------------------
# Tests: route_by_kind -- requires_live_tools
# ---------------------------------------------------------------------------

class TestRouteByKindLiveTools(unittest.TestCase):
    def test_live_tools_routes_to_claude_opus(self):
        meta = _stub_meta("browser_tool", ext=False, live=True)
        with _patch_meta(meta), _patch_credit(True):
            result = router.route_by_kind("browser_tool")
        assert result is not None
        assert result["backend"] == router.BACKEND_CLAUDE_OPUS
        assert result["kind_rule"] == "requires_live_tools"
        assert result["preflight_needed"] is False

    def test_live_tools_no_credit_falls_to_sonnet(self):
        meta = _stub_meta("mcp_server", ext=False, live=True)
        with _patch_meta(meta), _patch_credit(False):
            result = router.route_by_kind("mcp_server")
        assert result is not None
        assert result["backend"] == router.BACKEND_CLAUDE_SONNET
        assert result["kind_rule"] == "requires_live_tools"

    def test_live_tools_kinds_from_spec(self):
        live_kinds = ["browser_tool", "mcp_server", "interactive_demo",
                      "computer_use", "db_connector"]
        for kind in live_kinds:
            meta = _stub_meta(kind, ext=False, live=True)
            with _patch_meta(meta), _patch_credit(True):
                result = router.route_by_kind(kind)
            assert result is not None, "Expected routing for %s" % kind
            assert "claude" in result["backend"].lower(), (
                "kind=%s should route to Claude, got %s" % (kind, result["backend"])
            )


# ---------------------------------------------------------------------------
# Tests: route_by_kind -- requires_external_context
# ---------------------------------------------------------------------------

class TestRouteByKindExternalContext(unittest.TestCase):
    def test_external_context_sets_preflight_needed(self):
        meta = _stub_meta("knowledge_card", ext=True, live=False)
        with _patch_meta(meta), _patch_credit(True):
            result = router.route_by_kind("knowledge_card")
        assert result is not None
        assert result["preflight_needed"] is True
        assert result["kind_rule"] == "requires_external_context"

    def test_external_context_allows_any_backend(self):
        meta = _stub_meta("case_study", ext=True, live=False)
        with _patch_meta(meta), _patch_credit(False):
            result = router.route_by_kind("case_study")
        assert result is not None
        assert result["preflight_needed"] is True
        # Should NOT force Claude -- any runtime is fine after pre-flight
        assert result["backend"] is not None

    def test_external_context_inherits_signature_backend(self):
        meta = _stub_meta("benchmark", ext=True, live=False)
        with _patch_meta(meta), _patch_credit(True):
            result = router.route_by_kind("benchmark", signature="production_kc")
        assert result is not None
        assert result["kind_rule"] == "requires_external_context"
        # production_kc signature should route to Opus
        assert result["backend"] == router.BACKEND_CLAUDE_OPUS


# ---------------------------------------------------------------------------
# Tests: route_by_kind -- structural (no override)
# ---------------------------------------------------------------------------

class TestRouteByKindStructural(unittest.TestCase):
    def test_structural_kind_returns_none(self):
        meta = _stub_meta("agent", ext=False, live=False)
        with _patch_meta(meta), _patch_credit(True):
            result = router.route_by_kind("agent")
        assert result is None, "Structural kind should fall through (None)"

    def test_unknown_kind_returns_none(self):
        with _patch_meta({}):
            result = router.route_by_kind("nonexistent_abc")
        assert result is None

    def test_empty_kind_returns_none(self):
        result = router.route_by_kind("")
        assert result is None


# ---------------------------------------------------------------------------
# Tests: infer_kind_from_handoff
# ---------------------------------------------------------------------------

class TestInferKindFromHandoff(unittest.TestCase):
    def test_extracts_kind_from_body(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md",
                                         delete=False, encoding="utf-8") as f:
            f.write("## Task\nBuild kind=knowledge_card for EdTech\n")
            f.flush()
            kind = router.infer_kind_from_handoff(Path(f.name))
        assert kind == "knowledge_card"
        os.unlink(f.name)

    def test_extracts_kind_from_frontmatter(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md",
                                         delete=False, encoding="utf-8") as f:
            f.write("---\nkind: landing_page\n---\n# Task\n")
            f.flush()
            kind = router.infer_kind_from_handoff(Path(f.name))
        assert kind == "landing_page"
        os.unlink(f.name)

    def test_returns_empty_for_missing_file(self):
        kind = router.infer_kind_from_handoff(Path("/tmp/does_not_exist_xyz.md"))
        assert kind == ""

    def test_returns_empty_when_no_kind(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md",
                                         delete=False, encoding="utf-8") as f:
            f.write("## Task\nJust do something.\n")
            f.flush()
            kind = router.infer_kind_from_handoff(Path(f.name))
        assert kind == ""
        os.unlink(f.name)


# ---------------------------------------------------------------------------
# Tests: route_task (unified entry)
# ---------------------------------------------------------------------------

class TestRouteTask(unittest.TestCase):
    def test_kind_takes_priority_over_signature(self):
        meta = _stub_meta("browser_tool", ext=False, live=True)
        with _patch_meta(meta), _patch_credit(True):
            result = router.route_task(kind="browser_tool", signature="smoke_test")
        assert result["kind_rule"] == "requires_live_tools"
        assert "claude" in result["backend"].lower()

    def test_signature_fallback_when_kind_structural(self):
        meta = _stub_meta("agent", ext=False, live=False)
        with _patch_meta(meta), _patch_credit(True):
            result = router.route_task(kind="agent", signature="structural_scaffold")
        assert result["kind_rule"] == "none"
        assert result["backend"] == router.BACKEND_OLLAMA_SMALL

    def test_no_kind_uses_signature_only(self):
        with _patch_credit(True):
            result = router.route_task(kind="", signature="production_kc")
        assert result["kind_rule"] == "none"
        assert result["backend"] == router.BACKEND_CLAUDE_OPUS

    def test_result_always_has_required_keys(self):
        meta = _stub_meta("agent", ext=False, live=False)
        with _patch_meta(meta), _patch_credit(True):
            result = router.route_task(kind="agent")
        required = ["backend", "reason", "fallback", "kind_rule",
                     "preflight_needed", "anthropic_credit_ok", "gemini_key_ok"]
        for key in required:
            assert key in result, "Missing key: %s" % key

    def test_handoff_inference(self):
        meta = {
            "knowledge_card": {
                "requires_external_context": True,
                "requires_live_tools": False,
                "pillar": "P01",
            }
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md",
                                         delete=False, encoding="utf-8") as f:
            f.write("---\nkind: knowledge_card\n---\n# Task\nResearch pricing\n")
            f.flush()
            with _patch_meta(meta), _patch_credit(True):
                result = router.route_task(handoff_path=Path(f.name))
        assert result["kind_rule"] == "requires_external_context"
        assert result["preflight_needed"] is True
        os.unlink(f.name)

    def test_default_routing_for_empty_inputs(self):
        with _patch_credit(False):
            result = router.route_task()
        assert result["backend"] is not None
        assert result["kind_rule"] == "none"


# ---------------------------------------------------------------------------
# Tests: backward compatibility
# ---------------------------------------------------------------------------

class TestBackwardCompatibility(unittest.TestCase):
    def test_pick_backend_still_works(self):
        with _patch_credit(True):
            result = router.pick_backend("production_kc")
        assert result["backend"] == router.BACKEND_CLAUDE_OPUS

    def test_infer_signature_from_handoff_still_works(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md",
                                         delete=False, encoding="utf-8") as f:
            f.write("kind: knowledge_card\nSome task\n")
            f.flush()
            sig = router.infer_signature_from_handoff(Path(f.name))
        assert sig == "production_kc"
        os.unlink(f.name)


if __name__ == "__main__":
    unittest.main()
