#!/usr/bin/env python3
"""Smoke tests for the CEX autodiscovery system (A2+A4+C1).

Tests:
1. cex_query returns results for "criar agente"
2. cex_query returns content-monetization-builder for "monetizar hotmart"
3. Motor 8F with unknown intent uses fallback query
4. Index has keywords for >= 100 manifests
5. --rebuild-cache works without errors
"""

import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = ROOT / ".cex" / "index.db"
TOOLS = ROOT / "_tools"

sys.path.insert(0, str(TOOLS))


@pytest.fixture(autouse=True)
def require_index():
    """Skip all tests if index.db is missing."""
    if not DB_PATH.exists():
        pytest.skip("index.db not found -- run cex_index.py first")


class TestCexQuery:
    """Tests for cex_query.py query_builders function."""

    def test_query_returns_results_for_agent(self):
        """cex_query returns results for 'criar agente'."""
        from cex_query import query_builders
        results = query_builders("criar agente", top_k=5)
        assert len(results) > 0, "Expected results for 'criar agente'"
        builder_ids = [r["builder_id"] for r in results]
        assert any("agent" in bid for bid in builder_ids), \
            f"Expected agent-related builder in results, got: {builder_ids}"

    def test_query_finds_content_monetization(self):
        """cex_query returns content-monetization-builder for 'monetizar hotmart'."""
        from cex_query import query_builders
        results = query_builders("monetizar hotmart", top_k=5)
        assert len(results) > 0, "Expected results for 'monetizar hotmart'"
        builder_ids = [r["builder_id"] for r in results]
        assert "content-monetization-builder" in builder_ids, \
            f"Expected content-monetization-builder in results, got: {builder_ids}"


class TestMotorFallback:
    """Tests for Motor 8F fallback to cex_query."""

    def test_unknown_intent_uses_query_fallback(self):
        """Motor 8F with unknown object falls back to cex_query."""
        from cex_8f_motor import classify_objects

        # "monetizacao_hotmart" is NOT in OBJECT_TO_KINDS
        results = classify_objects(["monetizacao"])
        assert len(results) > 0, "Expected fallback results"
        # Should NOT be generic if query finds a match
        kinds = [r["kind"] for r in results]
        has_real_match = any(k != "generic" for k in kinds)
        assert has_real_match, f"Expected non-generic fallback, got: {kinds}"


class TestIndexKeywords:
    """Tests for keyword coverage in index.db."""

    def test_index_has_keywords_for_100_plus_manifests(self):
        """Index has keywords for >= 100 manifests."""
        conn = sqlite3.connect(str(DB_PATH))
        count = conn.execute(
            "SELECT COUNT(*) FROM files WHERE path LIKE '%bld_model%' AND keywords_json != '[]'"
        ).fetchone()[0]
        conn.close()
        assert count >= 100, f"Expected >= 100 manifests with keywords, got {count}"


class TestRebuildCache:
    """Tests for --rebuild-cache flag."""

    def test_rebuild_cache_succeeds(self):
        """--rebuild-cache runs without errors."""
        result = subprocess.run(
            [sys.executable, str(TOOLS / "cex_query.py"), "--rebuild-cache"],
            capture_output=True, text=True, timeout=60
        )
        assert result.returncode == 0, f"rebuild-cache failed: {result.stderr}"
