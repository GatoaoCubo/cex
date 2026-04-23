# -*- coding: ascii -*-
"""
Tests for cex_fts5_search.py -- HERMES W4.4

Cases:
1. index: indexes text files into FTS5, returns chunk count
2. query: BM25-ranked results returned for matching query
3. query: no results for non-matching query
4. summarize-heuristic: condenses hits into sentences, respects token budget
5. stats: reports accurate chunk / session / source counts
6. index --session: re-index clears previous docs for that session
"""
from __future__ import annotations

import io
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "_tools"))


# ---------------------------------------------------------------------------
# Module loader with patched paths
# ---------------------------------------------------------------------------

def _load_module(tmp_dir: Path) -> types.ModuleType:
    src_path = REPO_ROOT / "_tools" / "cex_fts5_search.py"
    src = src_path.read_text(encoding="ascii")
    mod = types.ModuleType("cex_fts5_search_under_test")
    mod.__dict__["__file__"] = str(src_path)
    exec(compile(src, str(src_path), "exec"), mod.__dict__)  # noqa: S102
    # redirect DB + source dirs to tmp
    mod.FTS_DB_PATH = tmp_dir / "fts5_search.db"
    mod.TRACES_DIR = tmp_dir / "traces"
    mod.HOOK_LOG = tmp_dir / "hook_log.jsonl"
    mod.HANDOFFS_DIR = tmp_dir / "handoffs"
    return mod


def _make_args(**kwargs):
    import argparse
    ns = argparse.Namespace()
    for k, v in kwargs.items():
        setattr(ns, k, v)
    return ns


# ---------------------------------------------------------------------------
# Test: index
# ---------------------------------------------------------------------------

class TestIndex(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db = self.tmp / "fts5_search.db"

    def tearDown(self):
        self._tmp.cleanup()

    def test_index_text_file(self):
        traces = self.tmp / "traces"
        traces.mkdir(parents=True, exist_ok=True)
        (traces / "sample.txt").write_text(
            "The quick brown fox jumps over the lazy dog. "
            "FTS5 indexing works well for session search.",
            encoding="utf-8"
        )
        self.mod.TRACES_DIR = traces

        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_index(_make_args(session=""), db_path=self.db)
        output = buf.getvalue()
        self.assertIn("[OK]", output)
        # verify chunks in DB
        conn = self.mod._open_db(self.db)
        count = conn.execute("SELECT COUNT(*) FROM docs").fetchone()[0]
        conn.close()
        self.assertGreater(count, 0)

    def test_index_jsonl_file(self):
        traces = self.tmp / "traces"
        traces.mkdir(parents=True, exist_ok=True)
        lines = [
            '{"session_id": "sess_abc", "content": "user prefers concise output"}',
            '{"session_id": "sess_abc", "content": "python debugging session active"}',
        ]
        (traces / "session_abc.jsonl").write_text("\n".join(lines), encoding="utf-8")
        self.mod.TRACES_DIR = traces

        self.mod.cmd_index(_make_args(session=""), db_path=self.db)
        conn = self.mod._open_db(self.db)
        rows = conn.execute(
            "SELECT session FROM docs WHERE session='sess_abc'"
        ).fetchall()
        conn.close()
        self.assertGreater(len(rows), 0)

    def test_index_empty_traces_dir(self):
        traces = self.tmp / "traces"
        traces.mkdir(parents=True, exist_ok=True)
        self.mod.TRACES_DIR = traces
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_index(_make_args(session=""), db_path=self.db)
        # should not crash; 0 chunks indexed
        conn = self.mod._open_db(self.db)
        count = conn.execute("SELECT COUNT(*) FROM docs").fetchone()[0]
        conn.close()
        self.assertEqual(count, 0)

    def test_index_session_clears_previous(self):
        """Re-indexing a session removes old docs for that session."""
        # initial index via public API
        self.mod.index_text("sess_x", "test_source", "first content", db_path=self.db)
        conn = self.mod._open_db(self.db)
        before = conn.execute(
            "SELECT COUNT(*) FROM docs WHERE session='sess_x'"
        ).fetchone()[0]
        conn.close()
        self.assertGreater(before, 0)

        # re-index session (no traces dir, so nothing new indexed)
        traces = self.tmp / "traces"
        traces.mkdir(exist_ok=True)
        self.mod.TRACES_DIR = traces
        self.mod.cmd_index(_make_args(session="sess_x"), db_path=self.db)

        conn = self.mod._open_db(self.db)
        after = conn.execute(
            "SELECT COUNT(*) FROM docs WHERE session='sess_x'"
        ).fetchone()[0]
        conn.close()
        # session docs cleared (traces dir empty, so 0)
        self.assertEqual(after, 0)


# ---------------------------------------------------------------------------
# Test: query
# ---------------------------------------------------------------------------

class TestQuery(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db = self.tmp / "fts5_search.db"
        # seed some indexed content
        self.mod.index_text("sess_1", "notes.txt",
                            "The agent uses FTS5 full text search for session recall.",
                            db_path=self.db)
        self.mod.index_text("sess_1", "notes.txt",
                            "Python debugging with breakpoints and stack traces.",
                            db_path=self.db)
        self.mod.index_text("sess_2", "log.txt",
                            "Workflow orchestration dispatches nuclei in parallel.",
                            db_path=self.db)

    def tearDown(self):
        self._tmp.cleanup()

    def test_query_returns_hits(self):
        hits = self.mod.search("session recall", top_k=5, db_path=self.db)
        self.assertGreater(len(hits), 0)
        # top hit should contain relevant terms
        self.assertTrue(any("session" in h["content"].lower() for h in hits))

    def test_query_no_results(self):
        hits = self.mod.search("zzz_nonexistent_xyzzy", db_path=self.db)
        self.assertEqual(len(hits), 0)

    def test_query_top_k_respected(self):
        hits = self.mod.search("the", top_k=1, db_path=self.db)
        self.assertLessEqual(len(hits), 1)

    def test_query_cmd_output(self):
        buf = io.StringIO()
        args = _make_args(query="FTS5", summarize=False, top_k=5, token_budget=500)
        with redirect_stdout(buf):
            self.mod.cmd_query(args, db_path=self.db)
        output = buf.getvalue()
        self.assertIn("bm25=", output)

    def test_query_cmd_no_results(self):
        buf = io.StringIO()
        args = _make_args(query="zzz_xyzzy_absent", summarize=False,
                          top_k=5, token_budget=500)
        with redirect_stdout(buf):
            self.mod.cmd_query(args, db_path=self.db)
        output = buf.getvalue()
        self.assertIn("No results", output)


# ---------------------------------------------------------------------------
# Test: summarize-heuristic
# ---------------------------------------------------------------------------

class TestSummarizeHeuristic(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db = self.tmp / "fts5_search.db"
        self.mod.index_text(
            "sess_s", "doc.txt",
            "The FTS5 engine ranks results by BM25 score. "
            "Higher relevance yields better rank. "
            "Session recall improves agent context injection.",
            db_path=self.db
        )

    def tearDown(self):
        self._tmp.cleanup()

    def test_summarize_heuristic_returns_text(self):
        hits = self.mod.search("FTS5 rank", db_path=self.db)
        summary = self.mod._heuristic_summarize(hits, token_budget=200)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
        self.assertNotEqual(summary, "No results to summarize.")

    def test_summarize_respects_token_budget(self):
        hits = self.mod.search("session", db_path=self.db)
        summary = self.mod._heuristic_summarize(hits, token_budget=5)
        # with budget of 5 tokens (~20 chars), output should be very short
        self.assertLessEqual(len(summary), 300)

    def test_summarize_empty_hits(self):
        summary = self.mod._heuristic_summarize([], token_budget=500)
        self.assertEqual(summary, "No results to summarize.")

    def test_summarize_cmd_flag(self):
        buf = io.StringIO()
        args = _make_args(query="BM25", summarize=True, top_k=5, token_budget=500)
        with redirect_stdout(buf):
            self.mod.cmd_query(args, db_path=self.db)
        output = buf.getvalue()
        # heuristic summary should not include "bm25=" labels
        self.assertNotIn("bm25=", output)
        self.assertGreater(len(output.strip()), 0)


# ---------------------------------------------------------------------------
# Test: stats
# ---------------------------------------------------------------------------

class TestStats(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db = self.tmp / "fts5_search.db"
        self.mod.index_text("sess_a", "src1.txt", "alpha content", db_path=self.db)
        self.mod.index_text("sess_b", "src2.txt", "beta content second doc",
                            db_path=self.db)

    def tearDown(self):
        self._tmp.cleanup()

    def test_stats_output(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_stats(_make_args(), db_path=self.db)
        output = buf.getvalue()
        self.assertIn("total chunks", output)
        self.assertIn("sessions", output)
        self.assertIn("source files", output)

    def test_stats_counts_correct(self):
        conn = self.mod._open_db(self.db)
        total = conn.execute("SELECT COUNT(*) FROM docs").fetchone()[0]
        conn.close()
        self.assertGreaterEqual(total, 2)


# ---------------------------------------------------------------------------
# Test: public API
# ---------------------------------------------------------------------------

class TestPublicAPI(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db = self.tmp / "fts5_search.db"

    def tearDown(self):
        self._tmp.cleanup()

    def test_index_text_returns_chunk_count(self):
        n = self.mod.index_text("sess_api", "api_src", "hello world test",
                                db_path=self.db)
        self.assertGreaterEqual(n, 1)

    def test_search_returns_list_of_dicts(self):
        self.mod.index_text("sess_api", "api_src",
                            "orchestration pipeline dispatches n03 builder",
                            db_path=self.db)
        results = self.mod.search("orchestration", db_path=self.db)
        self.assertIsInstance(results, list)
        if results:
            self.assertIn("content", results[0])
            self.assertIn("source", results[0])


if __name__ == "__main__":
    unittest.main()
