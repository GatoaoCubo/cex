#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
cex_user_model.py -- Honcho-pattern Peer/Session/Message store (HERMES W4.3)

SQLite default (FTS5 full-text search), pgvector optional via CEX_USER_MODEL_PG.
Implements the `user_model` kind (P10) dialectic loop:
  pre-response insight -> inject -> generate -> post-derive -> compact.

Storage: .cex/user_models/{peer_id}.db  (one DB per peer for isolation)

Usage:
    python _tools/cex_user_model.py init --peer-id alice
    python _tools/cex_user_model.py add-message --peer-id alice --session s1 --role user --content "..."
    python _tools/cex_user_model.py insight --peer-id alice --query "what does this user want?"
    python _tools/cex_user_model.py context --peer-id alice --token-budget 500
    python _tools/cex_user_model.py compact --peer-id alice
    python _tools/cex_user_model.py search --peer-id alice --query "preferences"
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Optional: pgvector (production vector search)
# ---------------------------------------------------------------------------
_pgvector_ok = False
try:
    import psycopg2  # noqa: F401
    _pgvector_ok = True
except ImportError:
    pass

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CEX_ROOT = Path(__file__).resolve().parent.parent
USER_MODEL_DIR = CEX_ROOT / ".cex" / "user_models"

COMPACT_THRESHOLD = 50          # messages per session before auto-compaction
COMPACT_KEEP = 10               # messages kept after compaction (most recent)
CHARS_PER_TOKEN = 4             # rough token estimator (4 chars ~ 1 token)
DEFAULT_COLLECTIONS = ["preferences", "working_style", "context_history"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _tokens(text: str) -> int:
    return max(1, len(text) // CHARS_PER_TOKEN)


def _new_session_id() -> str:
    return "sess_" + uuid.uuid4().hex[:12]


def _get_db_path(peer_id: str, db_dir: Optional[Path] = None) -> Path:
    base = db_dir if db_dir is not None else USER_MODEL_DIR
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{peer_id}.db"


# ---------------------------------------------------------------------------
# DB layer
# ---------------------------------------------------------------------------

_SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS peers (
    peer_id   TEXT PRIMARY KEY,
    workspace TEXT NOT NULL DEFAULT 'default',
    created   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    peer_id    TEXT NOT NULL,
    started    TEXT NOT NULL,
    FOREIGN KEY(peer_id) REFERENCES peers(peer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS messages (
    msg_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT    NOT NULL,
    role       TEXT    NOT NULL,
    content    TEXT    NOT NULL,
    ts         TEXT    NOT NULL,
    FOREIGN KEY(session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS collections (
    coll_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    peer_id    TEXT    NOT NULL,
    name       TEXT    NOT NULL,
    UNIQUE(peer_id, name),
    FOREIGN KEY(peer_id) REFERENCES peers(peer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS documents (
    doc_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    coll_id   INTEGER NOT NULL,
    content   TEXT    NOT NULL,
    ts        TEXT    NOT NULL,
    embedding BLOB,
    FOREIGN KEY(coll_id) REFERENCES collections(coll_id) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts
    USING fts5(content, content='messages', content_rowid='msg_id');
"""


def _open_db(peer_id: str, workspace: str = "default",
             db_dir: Optional[Path] = None) -> sqlite3.Connection:
    db_path = _get_db_path(peer_id, db_dir)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.executescript(_SCHEMA_SQL)
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# Peer
# ---------------------------------------------------------------------------

class Peer:
    """Cross-session dialectic representation of a human peer."""

    def __init__(self, conn: sqlite3.Connection, peer_id: str) -> None:
        self.conn = conn
        self.peer_id = peer_id

    def exists(self) -> bool:
        row = self.conn.execute(
            "SELECT 1 FROM peers WHERE peer_id=?", (self.peer_id,)
        ).fetchone()
        return row is not None

    def create(self, workspace: str = "default") -> None:
        self.conn.execute(
            "INSERT OR IGNORE INTO peers(peer_id, workspace, created) VALUES(?,?,?)",
            (self.peer_id, workspace, _now_iso())
        )
        for name in DEFAULT_COLLECTIONS:
            self.conn.execute(
                "INSERT OR IGNORE INTO collections(peer_id, name) VALUES(?,?)",
                (self.peer_id, name)
            )
        self.conn.commit()

    def chat(self, query: str) -> str:
        """NL query against peer's derived fact graph.

        Uses heuristic keyword scoring by default.
        Set CEX_USER_MODEL_LLM=claude to enable LLM-backed insight.
        """
        llm_env = os.environ.get("CEX_USER_MODEL_LLM", "").strip()
        if llm_env:
            return self._llm_insight(query)
        return self._heuristic_insight(query)

    def _heuristic_insight(self, query: str) -> str:
        rows = self.conn.execute("""
            SELECT d.content, c.name
            FROM documents d
            JOIN collections c ON d.coll_id = c.coll_id
            WHERE c.peer_id = ?
            ORDER BY d.doc_id DESC
            LIMIT 20
        """, (self.peer_id,)).fetchall()

        if not rows:
            return "No derived facts yet for this peer."

        qwords = set(query.lower().split())
        scored: List[tuple] = []
        for row in rows:
            overlap = sum(1 for w in qwords if w in row["content"].lower())
            scored.append((overlap, row["content"], row["name"]))
        scored.sort(key=lambda x: x[0], reverse=True)

        top = [f"[{name}] {content}" for _, content, name in scored[:3]]
        return "\n".join(top)

    def _llm_insight(self, query: str) -> str:
        try:
            from cex_sdk.models.chat import chat
            context = self._build_fact_context(token_budget=800)
            _prompt = (
                "User model context:\n" + context +
                "\n\nQuery: " + query +
                "\n\nAnswer in 1-2 sentences."
            )
            try:
                from _tools.cex_model_resolver import resolve_model_for_tool
                _model = resolve_model_for_tool("cex_user_model", "light")["model"]
            except Exception:
                _model = "claude-haiku-4-5-20251001"
            return chat(_prompt, model=_model, max_tokens=200)
        except Exception as exc:
            return "LLM insight failed: " + str(exc)

    def _build_fact_context(self, token_budget: int = 500) -> str:
        rows = self.conn.execute("""
            SELECT d.content, c.name
            FROM documents d
            JOIN collections c ON d.coll_id = c.coll_id
            WHERE c.peer_id = ?
            ORDER BY d.doc_id DESC
        """, (self.peer_id,)).fetchall()

        parts: List[str] = []
        used = 0
        for row in rows:
            chunk = "[" + row["name"] + "] " + row["content"]
            t = _tokens(chunk)
            if used + t > token_budget:
                break
            parts.append(chunk)
            used += t
        return "\n".join(parts)

    def add_to_collection(self, collection_name: str, content: str) -> int:
        """Write a derived fact to a named collection."""
        row = self.conn.execute(
            "SELECT coll_id FROM collections WHERE peer_id=? AND name=?",
            (self.peer_id, collection_name)
        ).fetchone()
        if not row:
            cur = self.conn.execute(
                "INSERT INTO collections(peer_id, name) VALUES(?,?)",
                (self.peer_id, collection_name)
            )
            coll_id = cur.lastrowid
        else:
            coll_id = row["coll_id"]
        cur2 = self.conn.execute(
            "INSERT INTO documents(coll_id, content, ts) VALUES(?,?,?)",
            (coll_id, content, _now_iso())
        )
        self.conn.commit()
        return cur2.lastrowid


# ---------------------------------------------------------------------------
# Session
# ---------------------------------------------------------------------------

class Session:
    """Peer <-> Peer interaction container."""

    def __init__(self, conn: sqlite3.Connection, peer_id: str,
                 session_id: str) -> None:
        self.conn = conn
        self.peer_id = peer_id
        self.session_id = session_id

    def ensure(self) -> None:
        self.conn.execute(
            "INSERT OR IGNORE INTO sessions(session_id, peer_id, started) VALUES(?,?,?)",
            (self.session_id, self.peer_id, _now_iso())
        )
        self.conn.commit()

    def add_message(self, role: str, content: str) -> int:
        """Insert message + update FTS + trigger auto-compaction if threshold hit."""
        cur = self.conn.execute(
            "INSERT INTO messages(session_id, role, content, ts) VALUES(?,?,?,?)",
            (self.session_id, role, content, _now_iso())
        )
        msg_id = cur.lastrowid
        # manual FTS insert (triggers not present in in-memory schema)
        try:
            self.conn.execute(
                "INSERT INTO messages_fts(rowid, content) VALUES(?,?)",
                (msg_id, content)
            )
        except sqlite3.OperationalError:
            pass  # FTS unavailable (edge case: fts5 not compiled in)
        self.conn.commit()
        self._maybe_compact()
        return msg_id

    def _msg_count(self) -> int:
        row = self.conn.execute(
            "SELECT COUNT(*) FROM messages WHERE session_id=?",
            (self.session_id,)
        ).fetchone()
        return row[0] if row else 0

    def _maybe_compact(self) -> None:
        count = self._msg_count()
        if count >= COMPACT_THRESHOLD and count % COMPACT_THRESHOLD == 0:
            self.compact()

    def compact(self) -> int:
        """Summarize oldest messages into context_history; remove compacted rows.

        Returns number of messages removed.
        """
        rows = self.conn.execute("""
            SELECT msg_id, role, content FROM messages
            WHERE session_id = ?
            ORDER BY msg_id
        """, (self.session_id,)).fetchall()

        total = len(rows)
        if total <= COMPACT_KEEP:
            return 0

        to_compact = rows[:total - COMPACT_KEEP]
        lines = [r["role"] + ": " + r["content"][:80] for r in to_compact]
        summary = (
            "Compacted " + str(len(to_compact)) + " messages. "
            "Sample: " + " | ".join(lines[:5]) +
            (" ..." if len(lines) > 5 else "")
        )

        # write summary to context_history collection
        coll = self.conn.execute(
            "SELECT coll_id FROM collections WHERE peer_id=? AND name='context_history'",
            (self.peer_id,)
        ).fetchone()
        if coll:
            self.conn.execute(
                "INSERT INTO documents(coll_id, content, ts) VALUES(?,?,?)",
                (coll["coll_id"], summary, _now_iso())
            )

        # remove from FTS (must pass original content for external-content FTS5)
        ids = [r["msg_id"] for r in to_compact]
        for row in to_compact:
            try:
                self.conn.execute(
                    "INSERT INTO messages_fts(messages_fts, rowid, content)"
                    " VALUES('delete',?,?)",
                    (row["msg_id"], row["content"])
                )
            except sqlite3.OperationalError:
                pass
        placeholders = ",".join("?" * len(ids))
        self.conn.execute(
            "DELETE FROM messages WHERE msg_id IN (" + placeholders + ")",
            ids
        )
        self.conn.commit()
        return len(ids)

    def representation(self) -> str:
        """Static insight string for prompt injection (last 10 messages)."""
        rows = self.conn.execute("""
            SELECT role, content FROM messages
            WHERE session_id = ?
            ORDER BY msg_id DESC LIMIT 10
        """, (self.session_id,)).fetchall()
        if not rows:
            return "No session context available."
        lines = [r["role"] + ": " + r["content"][:80] for r in reversed(rows)]
        return "Recent context:\n" + "\n".join(lines)

    def context(self, token_budget: int = 500) -> str:
        """Token-budgeted context: peer facts + recent session messages."""
        msg_budget = int(token_budget * 0.6)
        doc_budget = token_budget - msg_budget

        # recent messages (newest first, reversed for chronological output)
        msg_rows = self.conn.execute("""
            SELECT role, content FROM messages
            WHERE session_id = ?
            ORDER BY msg_id DESC
        """, (self.session_id,)).fetchall()

        msg_parts: List[str] = []
        used_msg = 0
        for row in reversed(msg_rows):
            chunk = row["role"] + ": " + row["content"]
            t = _tokens(chunk)
            if used_msg + t > msg_budget:
                break
            msg_parts.append(chunk)
            used_msg += t

        # peer documents (newest first)
        doc_rows = self.conn.execute("""
            SELECT d.content, c.name
            FROM documents d
            JOIN collections c ON d.coll_id = c.coll_id
            WHERE c.peer_id = ?
            ORDER BY d.doc_id DESC LIMIT 15
        """, (self.peer_id,)).fetchall()

        doc_parts: List[str] = []
        used_doc = 0
        for row in doc_rows:
            chunk = "[" + row["name"] + "] " + row["content"]
            t = _tokens(chunk)
            if used_doc + t > doc_budget:
                break
            doc_parts.append(chunk)
            used_doc += t

        sections: List[str] = []
        if doc_parts:
            sections.append("Peer knowledge:\n" + "\n".join(doc_parts))
        if msg_parts:
            sections.append("Recent messages:\n" + "\n".join(msg_parts))
        return "\n\n".join(sections) if sections else "No context available."


# ---------------------------------------------------------------------------
# CLI handlers
# ---------------------------------------------------------------------------

def cmd_init(args: argparse.Namespace,
             db_dir: Optional[Path] = None) -> None:
    conn = _open_db(args.peer_id, workspace=getattr(args, "workspace", "default"),
                    db_dir=db_dir)
    peer = Peer(conn, args.peer_id)
    if peer.exists():
        print("Peer '" + args.peer_id + "' already exists.")
    else:
        peer.create(workspace=getattr(args, "workspace", "default"))
        print("[OK] Peer '" + args.peer_id + "' initialized with collections: " +
              str(DEFAULT_COLLECTIONS))
    conn.close()


def cmd_add_message(args: argparse.Namespace,
                    db_dir: Optional[Path] = None) -> None:
    conn = _open_db(args.peer_id, db_dir=db_dir)
    peer = Peer(conn, args.peer_id)
    if not peer.exists():
        peer.create()
    session = Session(conn, args.peer_id, args.session)
    session.ensure()
    msg_id = session.add_message(args.role, args.content)
    print("[OK] Message " + str(msg_id) + " added to session '" + args.session + "'.")
    conn.close()


def cmd_insight(args: argparse.Namespace,
                db_dir: Optional[Path] = None) -> None:
    conn = _open_db(args.peer_id, db_dir=db_dir)
    peer = Peer(conn, args.peer_id)
    if not peer.exists():
        print("[FAIL] Peer '" + args.peer_id + "' not found. Run init first.")
        conn.close()
        sys.exit(1)
    result = peer.chat(args.query)
    print(result)
    conn.close()


def cmd_context(args: argparse.Namespace,
                db_dir: Optional[Path] = None) -> None:
    conn = _open_db(args.peer_id, db_dir=db_dir)
    peer = Peer(conn, args.peer_id)
    if not peer.exists():
        print("[FAIL] Peer '" + args.peer_id + "' not found.")
        conn.close()
        sys.exit(1)

    session_id = getattr(args, "session", None)
    if not session_id:
        row = conn.execute(
            "SELECT session_id FROM sessions WHERE peer_id=? ORDER BY started DESC LIMIT 1",
            (args.peer_id,)
        ).fetchone()
        session_id = row["session_id"] if row else _new_session_id()

    session = Session(conn, args.peer_id, session_id)
    print(session.context(args.token_budget))
    conn.close()


def cmd_compact(args: argparse.Namespace,
                db_dir: Optional[Path] = None) -> None:
    conn = _open_db(args.peer_id, db_dir=db_dir)
    peer = Peer(conn, args.peer_id)
    if not peer.exists():
        print("[FAIL] Peer '" + args.peer_id + "' not found.")
        conn.close()
        sys.exit(1)

    session_rows = conn.execute(
        "SELECT session_id FROM sessions WHERE peer_id=?", (args.peer_id,)
    ).fetchall()

    total_removed = 0
    for row in session_rows:
        sess = Session(conn, args.peer_id, row["session_id"])
        total_removed += sess.compact()

    print("[OK] Compacted " + str(total_removed) + " messages for peer '" +
          args.peer_id + "'.")
    conn.close()


def cmd_search(args: argparse.Namespace,
               db_dir: Optional[Path] = None) -> None:
    conn = _open_db(args.peer_id, db_dir=db_dir)
    peer = Peer(conn, args.peer_id)
    if not peer.exists():
        print("[FAIL] Peer '" + args.peer_id + "' not found.")
        conn.close()
        sys.exit(1)

    results: List[Dict[str, Any]] = []

    # FTS5 search in messages
    try:
        msg_rows = conn.execute("""
            SELECT m.msg_id, m.role, m.content, m.session_id
            FROM messages_fts
            JOIN messages m ON messages_fts.rowid = m.msg_id
            WHERE messages_fts MATCH ?
            LIMIT 10
        """, (args.query,)).fetchall()
        for r in msg_rows:
            results.append({
                "type": "message",
                "id": r["msg_id"],
                "session": r["session_id"],
                "role": r["role"],
                "content": r["content"][:120]
            })
    except sqlite3.OperationalError:
        pass

    # keyword search in documents
    doc_rows = conn.execute("""
        SELECT d.doc_id, d.content, c.name
        FROM documents d
        JOIN collections c ON d.coll_id = c.coll_id
        WHERE c.peer_id = ? AND d.content LIKE ?
        LIMIT 10
    """, (args.peer_id, "%" + args.query + "%")).fetchall()
    for r in doc_rows:
        results.append({
            "type": "document",
            "id": r["doc_id"],
            "collection": r["name"],
            "content": r["content"][:120]
        })

    if not results:
        print("No results found.")
    else:
        print(json.dumps(results, indent=2))
    conn.close()


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cex_user_model",
        description="Honcho-pattern Peer/Session/Message store (HERMES W4.3)"
    )
    sub = p.add_subparsers(dest="command", required=True)

    # init
    pi = sub.add_parser("init", help="Create peer + default collections")
    pi.add_argument("--peer-id", required=True)
    pi.add_argument("--workspace", default="default")

    # add-message
    pm = sub.add_parser("add-message", help="Insert message into session")
    pm.add_argument("--peer-id", required=True)
    pm.add_argument("--session", required=True)
    pm.add_argument("--role", required=True, choices=["user", "assistant", "system"])
    pm.add_argument("--content", required=True)

    # insight
    pq = sub.add_parser("insight", help="NL query against peer fact graph")
    pq.add_argument("--peer-id", required=True)
    pq.add_argument("--query", required=True)

    # context
    pc = sub.add_parser("context", help="Token-budgeted context extraction")
    pc.add_argument("--peer-id", required=True)
    pc.add_argument("--session", default=None)
    pc.add_argument("--token-budget", type=int, default=500)

    # compact
    pcp = sub.add_parser("compact", help="Summarize old messages into documents")
    pcp.add_argument("--peer-id", required=True)

    # search
    ps = sub.add_parser("search", help="FTS5 + keyword search")
    ps.add_argument("--peer-id", required=True)
    ps.add_argument("--query", required=True)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    dispatch: Dict[str, Any] = {
        "init": cmd_init,
        "add-message": cmd_add_message,
        "insight": cmd_insight,
        "context": cmd_context,
        "compact": cmd_compact,
        "search": cmd_search,
    }
    fn = dispatch.get(args.command)
    if fn:
        fn(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
