# -*- coding: ascii -*-
"""
Tests for cex_user_model.py -- HERMES W4.3

Cases:
1. init: creates peer + 3 default collections
2. add-message: inserts message, FTS indexed, returns msg_id
3. add-message: auto-compacts at threshold
4. insight: heuristic returns top matched docs
5. context: token-budgeted extraction (messages + docs)
6. compact: manual compaction removes old messages, writes doc
7. search: FTS5 and keyword search return results
"""
from __future__ import annotations

import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "_tools"))


# ---------------------------------------------------------------------------
# Module loader with patched USER_MODEL_DIR
# ---------------------------------------------------------------------------

def _load_module(tmp_dir: Path) -> types.ModuleType:
    src_path = REPO_ROOT / "_tools" / "cex_user_model.py"
    src = src_path.read_text(encoding="ascii")
    mod = types.ModuleType("cex_user_model_under_test")
    mod.__dict__["__file__"] = str(src_path)
    exec(compile(src, str(src_path), "exec"), mod.__dict__)  # noqa: S102
    mod.USER_MODEL_DIR = tmp_dir / "user_models"
    return mod


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _make_args(**kwargs):
    """Build a minimal argparse.Namespace from kwargs."""
    import argparse
    ns = argparse.Namespace()
    for k, v in kwargs.items():
        setattr(ns, k.replace("-", "_"), v)
    return ns


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestInit(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)

    def tearDown(self):
        self._tmp.cleanup()

    def test_init_creates_peer_and_collections(self):
        db_dir = self.tmp / "user_models"
        args = _make_args(**{"peer_id": "alice", "workspace": "test"})
        self.mod.cmd_init(args, db_dir=db_dir)

        conn = self.mod._open_db("alice", db_dir=db_dir)
        row = conn.execute("SELECT * FROM peers WHERE peer_id='alice'").fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row["workspace"], "test")

        colls = conn.execute(
            "SELECT name FROM collections WHERE peer_id='alice' ORDER BY name"
        ).fetchall()
        names = [c["name"] for c in colls]
        self.assertEqual(sorted(names), sorted(self.mod.DEFAULT_COLLECTIONS))
        conn.close()

    def test_init_idempotent(self):
        db_dir = self.tmp / "user_models"
        args = _make_args(**{"peer_id": "bob", "workspace": "default"})
        self.mod.cmd_init(args, db_dir=db_dir)
        self.mod.cmd_init(args, db_dir=db_dir)  # should not raise
        conn = self.mod._open_db("bob", db_dir=db_dir)
        count = conn.execute("SELECT COUNT(*) FROM peers WHERE peer_id='bob'").fetchone()[0]
        self.assertEqual(count, 1)
        conn.close()


class TestAddMessage(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db_dir = self.tmp / "user_models"
        # init peer
        self.mod.cmd_init(
            _make_args(**{"peer_id": "carol", "workspace": "default"}),
            db_dir=self.db_dir
        )

    def tearDown(self):
        self._tmp.cleanup()

    def test_add_message_inserts_row(self):
        args = _make_args(
            **{"peer_id": "carol", "session": "s1", "role": "user", "content": "hello world"}
        )
        self.mod.cmd_add_message(args, db_dir=self.db_dir)
        conn = self.mod._open_db("carol", db_dir=self.db_dir)
        row = conn.execute("SELECT * FROM messages WHERE session_id='s1'").fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row["content"], "hello world")
        self.assertEqual(row["role"], "user")
        conn.close()

    def test_add_message_creates_session(self):
        args = _make_args(
            **{"peer_id": "carol", "session": "s2", "role": "assistant", "content": "hi"}
        )
        self.mod.cmd_add_message(args, db_dir=self.db_dir)
        conn = self.mod._open_db("carol", db_dir=self.db_dir)
        sess = conn.execute("SELECT 1 FROM sessions WHERE session_id='s2'").fetchone()
        self.assertIsNotNone(sess)
        conn.close()

    def test_add_message_auto_compacts_at_threshold(self):
        threshold = self.mod.COMPACT_THRESHOLD
        conn = self.mod._open_db("carol", db_dir=self.db_dir)
        peer = self.mod.Peer(conn, "carol")
        session = self.mod.Session(conn, "carol", "s_compact")
        session.ensure()

        for i in range(threshold):
            session.add_message("user", "message " + str(i))

        count_after = conn.execute(
            "SELECT COUNT(*) FROM messages WHERE session_id='s_compact'"
        ).fetchone()[0]
        # should have been compacted, keeping only COMPACT_KEEP messages
        self.assertLessEqual(count_after, self.mod.COMPACT_KEEP)

        # context_history should have a summary doc
        coll = conn.execute(
            "SELECT coll_id FROM collections WHERE peer_id='carol' AND name='context_history'"
        ).fetchone()
        docs = conn.execute(
            "SELECT * FROM documents WHERE coll_id=?", (coll["coll_id"],)
        ).fetchall()
        self.assertGreater(len(docs), 0)
        conn.close()


class TestInsight(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db_dir = self.tmp / "user_models"
        self.mod.cmd_init(
            _make_args(**{"peer_id": "dave", "workspace": "default"}),
            db_dir=self.db_dir
        )
        # seed a document
        conn = self.mod._open_db("dave", db_dir=self.db_dir)
        peer = self.mod.Peer(conn, "dave")
        peer.add_to_collection("preferences", "prefers concise markdown responses")
        conn.close()

    def tearDown(self):
        self._tmp.cleanup()

    def test_insight_returns_relevant_doc(self):
        import io
        from contextlib import redirect_stdout
        args = _make_args(**{"peer_id": "dave", "query": "concise responses"})
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_insight(args, db_dir=self.db_dir)
        output = buf.getvalue()
        self.assertIn("concise", output)

    def test_insight_unknown_peer_exits(self):
        args = _make_args(**{"peer_id": "ghost", "query": "anything"})
        with self.assertRaises(SystemExit):
            self.mod.cmd_insight(args, db_dir=self.db_dir)


class TestContext(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db_dir = self.tmp / "user_models"
        self.mod.cmd_init(
            _make_args(**{"peer_id": "eve", "workspace": "default"}),
            db_dir=self.db_dir
        )
        # add a message
        self.mod.cmd_add_message(
            _make_args(**{"peer_id": "eve", "session": "s1",
                          "role": "user", "content": "I love Python"}),
            db_dir=self.db_dir
        )

    def tearDown(self):
        self._tmp.cleanup()

    def test_context_includes_recent_message(self):
        import io
        from contextlib import redirect_stdout
        args = _make_args(**{"peer_id": "eve", "session": "s1", "token_budget": 500})
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_context(args, db_dir=self.db_dir)
        output = buf.getvalue()
        self.assertIn("Python", output)

    def test_context_respects_token_budget(self):
        import io
        from contextlib import redirect_stdout
        args = _make_args(**{"peer_id": "eve", "session": "s1", "token_budget": 10})
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_context(args, db_dir=self.db_dir)
        output = buf.getvalue()
        # output should be short (budget of 10 tokens ~ 40 chars)
        self.assertLess(len(output), 500)


class TestCompact(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db_dir = self.tmp / "user_models"
        self.mod.cmd_init(
            _make_args(**{"peer_id": "frank", "workspace": "default"}),
            db_dir=self.db_dir
        )

    def tearDown(self):
        self._tmp.cleanup()

    def test_compact_removes_old_messages(self):
        conn = self.mod._open_db("frank", db_dir=self.db_dir)
        try:
            session = self.mod.Session(conn, "frank", "s_frank")
            session.ensure()
            keep = self.mod.COMPACT_KEEP
            # use add_message so FTS is properly indexed
            for i in range(keep + 5):
                session.add_message("user", "msg " + str(i))

            # force one more compaction manually (threshold may have fired already)
            # just check invariant: count <= COMPACT_KEEP
            session.compact()
            remaining = conn.execute(
                "SELECT COUNT(*) FROM messages WHERE session_id='s_frank'"
            ).fetchone()[0]
            self.assertLessEqual(remaining, keep)
        finally:
            conn.close()


class TestSearch(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.mod = _load_module(self.tmp)
        self.db_dir = self.tmp / "user_models"
        self.mod.cmd_init(
            _make_args(**{"peer_id": "grace", "workspace": "default"}),
            db_dir=self.db_dir
        )
        self.mod.cmd_add_message(
            _make_args(**{"peer_id": "grace", "session": "s1",
                          "role": "user", "content": "I enjoy debugging Python code"}),
            db_dir=self.db_dir
        )

    def tearDown(self):
        self._tmp.cleanup()

    def test_search_finds_message(self):
        import io
        from contextlib import redirect_stdout
        args = _make_args(**{"peer_id": "grace", "query": "debugging"})
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_search(args, db_dir=self.db_dir)
        output = buf.getvalue()
        results = json.loads(output)
        self.assertGreater(len(results), 0)
        self.assertTrue(any(r["type"] == "message" for r in results))

    def test_search_no_results(self):
        import io
        from contextlib import redirect_stdout
        args = _make_args(**{"peer_id": "grace", "query": "zzz_nonexistent_term_zzz"})
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.mod.cmd_search(args, db_dir=self.db_dir)
        output = buf.getvalue().strip()
        self.assertIn("No results", output)


if __name__ == "__main__":
    unittest.main()
