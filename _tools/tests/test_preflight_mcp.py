"""Unit tests for cex_preflight_mcp.py -- Phase 0 MCP external context gather.

All HTTP calls are mocked so tests run without network access or API keys.
Tests verify: query generation, kind metadata lookup, context assembly,
graceful degradation, cache I/O, and MCP data injection.
"""
from __future__ import annotations

import os
import sys
import unittest
import unittest.mock
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import cex_preflight_mcp as mcp

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_kinds_meta(kind: str, ext: bool = True, live: bool = False) -> dict[str, Any]:
    """Build a minimal kinds_meta stub for testing."""
    return {
        kind: {
            "requires_external_context": ext,
            "requires_live_tools": live,
            "pillar": "P01",
        }
    }


def _minimal_config(enabled: bool = True) -> dict[str, Any]:
    return {
        "enabled": enabled,
        "max_external_tokens": 512,
        "timeout_seconds": 5,
        "max_queries_per_provider": 2,
        "delay_between_queries_ms": 0,
        "audit_log": False,
        "providers": {
            "github": {"enabled": True, "requires_key": "GITHUB_TOKEN"},
            "fetch": {"enabled": True, "requires_key": None},
        },
    }


# ---------------------------------------------------------------------------
# Tests: kind metadata
# ---------------------------------------------------------------------------

class TestRequiresExternalContext(unittest.TestCase):
    def test_true_when_field_set(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("knowledge_card", ext=True),
        ):
            assert mcp.requires_external_context("knowledge_card") is True

    def test_false_when_field_not_set(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("agent", ext=False),
        ):
            assert mcp.requires_external_context("agent") is False

    def test_false_for_unknown_kind(self):
        with unittest.mock.patch.object(mcp, "load_kinds_meta", return_value={}):
            assert mcp.requires_external_context("nonexistent_kind") is False

    def test_false_for_empty_kind(self):
        assert mcp.requires_external_context("") is False

    def test_false_on_load_error(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta", side_effect=RuntimeError("disk error")
        ):
            assert mcp.requires_external_context("knowledge_card") is False


class TestRequiresLiveTools(unittest.TestCase):
    def test_true_for_browser_tool(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("browser_tool", ext=True, live=True),
        ):
            assert mcp.requires_live_tools("browser_tool") is True

    def test_false_for_structural_kind(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("agent", ext=False, live=False),
        ):
            assert mcp.requires_live_tools("agent") is False

    def test_false_for_empty_kind(self):
        assert mcp.requires_live_tools("") is False


# ---------------------------------------------------------------------------
# Tests: query generation
# ---------------------------------------------------------------------------

class TestGenerateQueries(unittest.TestCase):
    def test_returns_list(self):
        qs = mcp.generate_queries("competitive pricing analysis", "knowledge_card")
        assert isinstance(qs, list)
        assert 1 <= len(qs) <= 3

    def test_includes_kind_label(self):
        qs = mcp.generate_queries("pricing analysis edtech market", "knowledge_card")
        # At least one query should mention the kind
        combined = " ".join(qs).lower()
        assert "knowledge" in combined or "card" in combined

    def test_domain_hint_creates_secondary_query(self):
        qs = mcp.generate_queries("pricing model analysis", "knowledge_card", domain="edtech")
        assert len(qs) >= 2
        domain_q = [q for q in qs if "edtech" in q.lower()]
        assert domain_q, "Expected a query containing 'edtech'"

    def test_handles_empty_task(self):
        qs = mcp.generate_queries("", "agent")
        assert isinstance(qs, list)
        assert len(qs) >= 1

    def test_deduplicates_terms(self):
        qs = mcp.generate_queries("agent agent agent", "agent")
        combined = " ".join(qs)
        # Should not have excessive repetition
        assert combined.count("agent") < 6

    def test_respects_max_queries(self):
        qs = mcp.generate_queries(
            "deep research competitive benchmark analysis pricing study",
            "knowledge_card", domain="edtech"
        )
        assert len(qs) <= mcp.DEFAULT_MAX_QUERIES

    def test_fallback_for_all_stopwords(self):
        # Task is all stopwords -- should fallback to kind label
        qs = mcp.generate_queries("a the and or but i", "knowledge_card")
        assert len(qs) >= 1


# ---------------------------------------------------------------------------
# Tests: GitHub gather (mocked HTTP)
# ---------------------------------------------------------------------------

class TestGatherGithub(unittest.TestCase):
    def _fake_github_response(self) -> dict[str, Any]:
        return {
            "items": [
                {
                    "full_name": "org/repo-one",
                    "html_url": "https://github.com/org/repo-one",
                    "description": "A great repo about pricing",
                },
                {
                    "full_name": "org/repo-two",
                    "html_url": "https://github.com/org/repo-two",
                    "description": "Another edtech pricing tool",
                },
            ]
        }

    def test_returns_empty_without_token(self):
        with unittest.mock.patch.dict(os.environ, {}, clear=True):
            # Remove GITHUB_TOKEN if present
            env = {k: v for k, v in os.environ.items() if k != "GITHUB_TOKEN"}
            with unittest.mock.patch.dict(os.environ, env, clear=True):
                results = mcp.gather_github(["pricing edtech"], _minimal_config())
        assert results == []

    def test_returns_results_with_token(self):
        fake_resp = self._fake_github_response()
        with unittest.mock.patch.dict(os.environ, {"GITHUB_TOKEN": "test_token_xyz"}):
            with unittest.mock.patch.object(mcp, "_http_get_json", return_value=fake_resp):
                results = mcp.gather_github(
                    ["pricing edtech knowledge card"], _minimal_config(), delay_ms=0
                )
        assert len(results) > 0
        assert results[0]["source"] == "github"
        assert "org/repo-one" in results[0]["title"]

    def test_deduplicates_urls(self):
        # Two queries returning same URL should deduplicate
        fake_resp = self._fake_github_response()
        with unittest.mock.patch.dict(os.environ, {"GITHUB_TOKEN": "test_token_xyz"}):
            with unittest.mock.patch.object(mcp, "_http_get_json", return_value=fake_resp):
                results = mcp.gather_github(
                    ["query one", "query two"], _minimal_config(), delay_ms=0
                )
        urls = [r["url"] for r in results]
        assert len(urls) == len(set(urls)), "Duplicate URLs found"

    def test_graceful_on_http_error(self):
        with unittest.mock.patch.dict(os.environ, {"GITHUB_TOKEN": "test_token_xyz"}):
            with unittest.mock.patch.object(mcp, "_http_get_json", return_value=None):
                results = mcp.gather_github(["query"], _minimal_config())
        assert results == []


# ---------------------------------------------------------------------------
# Tests: direct URL fetch (mocked HTTP)
# ---------------------------------------------------------------------------

class TestGatherFetch(unittest.TestCase):
    def test_returns_snippet_from_html(self):
        fake_html = b"<html><body><p>Pricing info for EdTech tools in 2026.</p></body></html>"
        with unittest.mock.patch.object(mcp, "_http_get_text", return_value=fake_html.decode()):
            results = mcp.gather_fetch(["https://example.com/pricing"])
        assert len(results) == 1
        assert "Pricing info" in results[0]["snippet"]
        assert results[0]["source"] == "fetch"

    def test_graceful_on_fetch_error(self):
        with unittest.mock.patch.object(mcp, "_http_get_text", return_value=None):
            results = mcp.gather_fetch(["https://example.com/404"])
        assert results == []

    def test_limits_to_3_urls(self):
        with unittest.mock.patch.object(mcp, "_http_get_text", return_value="<p>text</p>"):
            results = mcp.gather_fetch([
                "https://a.com", "https://b.com", "https://c.com", "https://d.com"
            ])
        assert len(results) <= 3


# ---------------------------------------------------------------------------
# Tests: MCP result injection
# ---------------------------------------------------------------------------

class TestInjectMcpResults(unittest.TestCase):
    def test_parses_search_results(self):
        data = {
            "search_results": [
                {"title": "EdTech Pricing 2026", "url": "https://example.com", "snippet": "Pricing data"},
            ]
        }
        results = mcp.inject_mcp_results(data)
        assert len(results) == 1
        assert results[0]["source"] == "mcp:search"
        assert results[0]["title"] == "EdTech Pricing 2026"

    def test_parses_github_results(self):
        data = {
            "github_results": [
                {"title": "repo/name", "url": "https://github.com/repo/name", "body": "desc"},
            ]
        }
        results = mcp.inject_mcp_results(data)
        assert len(results) == 1
        assert results[0]["source"] == "mcp:github"

    def test_parses_fetch_results(self):
        data = {
            "fetch_results": [
                {"url": "https://example.com/doc", "content": "Documentation text"},
            ]
        }
        results = mcp.inject_mcp_results(data)
        assert len(results) == 1
        assert results[0]["source"] == "mcp:fetch"

    def test_handles_empty_data(self):
        assert mcp.inject_mcp_results({}) == []

    def test_truncates_long_snippets(self):
        data = {
            "search_results": [
                {"title": "Long", "url": "https://x.com", "snippet": "x" * 2000},
            ]
        }
        results = mcp.inject_mcp_results(data)
        assert len(results[0]["snippet"]) <= 500


# ---------------------------------------------------------------------------
# Tests: context assembly
# ---------------------------------------------------------------------------

class TestAssembleExternalContext(unittest.TestCase):
    def _sample_results(self) -> list[dict[str, str]]:
        return [
            {"title": "EdTech Pricing", "url": "https://example.com",
             "snippet": "Pricing data from 2026 market research.", "source": "github"},
            {"title": "Competitive Analysis", "url": "https://b.com",
             "snippet": "Competitor pricing: $29/mo to $99/mo.", "source": "fetch"},
        ]

    def test_returns_markdown_string(self):
        ctx = mcp.assemble_external_context(self._sample_results(), ["pricing edtech"])
        assert isinstance(ctx, str)
        assert len(ctx) > 0

    def test_contains_header(self):
        ctx = mcp.assemble_external_context(self._sample_results(), ["test query"])
        assert "## External Context" in ctx

    def test_contains_source_names(self):
        ctx = mcp.assemble_external_context(self._sample_results(), ["test"])
        assert "github" in ctx.lower() or "fetch" in ctx.lower()

    def test_returns_empty_for_no_results(self):
        ctx = mcp.assemble_external_context([], ["test"])
        assert ctx == ""

    def test_truncates_to_token_budget(self):
        # 20 large results should be truncated to fit tiny budget
        big_results = [
            {"title": "R%d" % i, "url": "https://x.com/%d" % i,
             "snippet": "word " * 200, "source": "github"}
            for i in range(20)
        ]
        ctx = mcp.assemble_external_context(big_results, ["test"], max_tokens=100)
        tokens = mcp.count_tokens(ctx)
        # Should be well under double the budget after truncation
        assert tokens < 250, "Context not truncated adequately (got %d tokens)" % tokens
        assert "[... truncated" in ctx

    def test_custom_gathered_at_timestamp(self):
        ts = "2026-04-20T12:00:00+00:00"
        ctx = mcp.assemble_external_context(self._sample_results(), [], gathered_at=ts)
        assert "2026-04-20" in ctx


# ---------------------------------------------------------------------------
# Tests: full gather pipeline (dry-run and mocked)
# ---------------------------------------------------------------------------

class TestGatherExternalContext(unittest.TestCase):
    def _patch_kind_true(self):
        return unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("knowledge_card", ext=True),
        )

    def _patch_kind_false(self):
        return unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("agent", ext=False),
        )

    def test_skips_when_disabled(self):
        with self._patch_kind_true():
            result = mcp.gather_external_context(
                "n01", "knowledge_card", "task text",
                config={"enabled": False},
            )
        assert result["skipped"] is True
        assert "disabled" in result["skipped_reason"]

    def test_skips_for_non_external_kind(self):
        with self._patch_kind_false():
            result = mcp.gather_external_context(
                "n03", "agent", "build an agent",
                config=_minimal_config(),
            )
        assert result["skipped"] is True
        assert "requires_external_context=false" in result["skipped_reason"]

    def test_dry_run_returns_queries_only(self):
        with self._patch_kind_true():
            result = mcp.gather_external_context(
                "n01", "knowledge_card", "competitive pricing edtech",
                config=_minimal_config(),
                dry_run=True,
            )
        assert result.get("dry_run") is True
        assert result["has_context"] is False
        assert len(result["queries"]) >= 1

    def test_mcp_injection_mode(self):
        with self._patch_kind_true():
            mcp_data = {
                "search_results": [
                    {"title": "Pricing 2026", "url": "https://x.com", "snippet": "data here"},
                ]
            }
            result = mcp.gather_external_context(
                "n01", "knowledge_card", "competitive pricing",
                config=_minimal_config(),
                mcp_data=mcp_data,
            )
        assert result["has_context"] is True
        assert "Pricing 2026" in result["context_md"]
        assert result["tokens_used"] > 0

    def test_github_direct_mode_no_token(self):
        with self._patch_kind_true():
            env = {k: v for k, v in os.environ.items()
                   if k not in ("GITHUB_TOKEN", "BRAVE_API_KEY")}
            with unittest.mock.patch.dict(os.environ, env, clear=True):
                result = mcp.gather_external_context(
                    "n01", "knowledge_card", "competitive pricing edtech",
                    config=_minimal_config(),
                )
        # No token = no results, but should not crash
        assert result["skipped"] is False
        assert result["has_context"] is False
        assert result["result_count"] == 0
        assert result["elapsed_ms"] >= 0

    def test_github_direct_mode_with_token(self):
        fake_resp = {
            "items": [
                {"full_name": "org/repo", "html_url": "https://github.com/org/repo",
                 "description": "EdTech pricing tool"},
            ]
        }
        with self._patch_kind_true():
            with unittest.mock.patch.dict(os.environ, {"GITHUB_TOKEN": "tok_test"}):
                with unittest.mock.patch.object(mcp, "_http_get_json", return_value=fake_resp):
                    result = mcp.gather_external_context(
                        "n01", "knowledge_card", "competitive pricing edtech",
                        config=_minimal_config(),
                    )
        assert result["has_context"] is True
        assert result["result_count"] > 0
        assert "github" in result["sources_used"]

    def test_returns_queries_list(self):
        with self._patch_kind_true():
            result = mcp.gather_external_context(
                "n01", "knowledge_card", "pricing edtech analysis",
                config=_minimal_config(),
                dry_run=True,
            )
        assert isinstance(result["queries"], list)
        assert len(result["queries"]) >= 1

    def test_result_structure_complete(self):
        with self._patch_kind_true():
            result = mcp.gather_external_context(
                "n01", "knowledge_card", "competitive pricing",
                config=_minimal_config(),
                dry_run=True,
            )
        required_keys = [
            "skipped", "has_context", "context_md", "tokens_used",
            "sources_used", "queries", "result_count", "context_path",
            "audit_path", "elapsed_ms",
        ]
        for key in required_keys:
            assert key in result, "Missing key: %s" % key


# ---------------------------------------------------------------------------
# Tests: graceful degradation
# ---------------------------------------------------------------------------

class TestGracefulDegradation(unittest.TestCase):
    def test_no_crash_when_kinds_meta_fails(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta", side_effect=OSError("file not found")
        ):
            result = mcp.gather_external_context(
                "n01", "knowledge_card", "task",
                config=_minimal_config(),
            )
        # Should skip gracefully (requires_external_context returns False on error)
        assert "skipped" in result

    def test_no_crash_when_github_network_fails(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("knowledge_card", ext=True),
        ):
            with unittest.mock.patch.dict(os.environ, {"GITHUB_TOKEN": "tok_test"}):
                with unittest.mock.patch.object(mcp, "_http_get_json", return_value=None):
                    result = mcp.gather_external_context(
                        "n01", "knowledge_card", "competitive pricing",
                        config=_minimal_config(),
                    )
        # No crash, just empty context
        assert result["has_context"] is False
        assert result["result_count"] == 0

    def test_no_crash_on_empty_task(self):
        with unittest.mock.patch.object(
            mcp, "load_kinds_meta",
            return_value=_make_kinds_meta("knowledge_card", ext=True),
        ):
            result = mcp.gather_external_context(
                "n01", "knowledge_card", "",
                config=_minimal_config(),
                dry_run=True,
            )
        assert "queries" in result


# ---------------------------------------------------------------------------
# Tests: cache I/O
# ---------------------------------------------------------------------------

class TestCacheIO(unittest.TestCase):
    def test_hash_is_deterministic(self):
        h1 = mcp._gather_hash("n01", "pricing analysis edtech")
        h2 = mcp._gather_hash("n01", "pricing analysis edtech")
        assert h1 == h2

    def test_different_nuclei_produce_different_hashes(self):
        h1 = mcp._gather_hash("n01", "same task")
        h2 = mcp._gather_hash("n03", "same task")
        assert h1 != h2

    def test_write_and_read_cache(self, tmp_path: Path | None = None):
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_cache = Path(tmpdir)
            with unittest.mock.patch.object(mcp, "CACHE_DIR", tmp_cache):
                context_md = "## External Context\n\nTest content here."
                audit = {"nucleus": "n01", "queries": ["test"], "tokens_consumed": 10}
                cp, ap = mcp.write_external_cache("n01", "test task", context_md, audit)
                assert cp.exists()
                assert ap.exists()

                # Read back
                cached = mcp.read_external_cache("n01", "test task")
                assert cached == context_md

    def test_read_returns_none_when_missing(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_cache = Path(tmpdir)
            with unittest.mock.patch.object(mcp, "CACHE_DIR", tmp_cache):
                cached = mcp.read_external_cache("n01", "nonexistent task")
                assert cached is None


if __name__ == "__main__":
    unittest.main()
