#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
cex_fts5_search.py -- FTS5 session search + LLM summarization (HERMES W4.4)

Indexes .cex/runtime/traces/ + session transcripts into a SQLite FTS5
virtual table for cross-session recall (F3 INJECT, W2 session_state).

Usage:
    python _tools/cex_fts5_search.py index [--session SESSION]
    python _tools/cex_fts5_search.py query --query TEXT [--summarize] [--top-k N] [--token-budget N]
    python _tools/cex_fts5_search.py stats
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CEX_ROOT = Path(__file__).resolve().parent.parent
TRACES_DIR = CEX_ROOT / ".cex" / "runtime" / "traces"
HOOK_LOG = CEX_ROOT / ".cex" / "runtime" / "hook_log.jsonl"
HANDOFFS_DIR = CEX_ROOT / ".cex" / "runtime" / "handoffs"
FTS_DB_PATH = CEX_ROOT / ".cex" / "fts5_search.db"

CHUNK_SIZE = 800
DEFAULT_TOP_K = 5
DEFAULT_TOKEN_BUDGET = 500
CHARS_PER_TOKEN = 4

_INDEXABLE_SUFFIXES = {".jsonl", ".json", ".txt", ".log", ".md"}

# ---------------------------------------------------------------------------
# DB schema
# ---------------------------------------------------------------------------

_SCHEMA = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS docs (
    doc_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    session  TEXT    NOT NULL DEFAULT '',
    source   TEXT    NOT NULL,
    chunk_no INTEGER NOT NULL DEFAULT 0,
    content  TEXT    NOT NULL,
    ts       TEXT    NOT NULL
);

CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts
    USING fts5(content, session, source,
               content='docs', content_rowid='doc_id');
"""


def _open_db(db_path: Optional[Path] = None) -> sqlite3.Connection:
    path = db_path if db_path is not None else FTS_DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.executescript(_SCHEMA)
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _tokens(text: str) -> int:
    return max(1, len(text) // CHARS_PER_TOKEN)


def _chunk(text: str, size: int = CHUNK_SIZE) -> Iterator[str]:
    text = text.strip()
    if not text:
        return
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        part = text[start:end].strip()
        if part:
            yield part
        start = end


def _rel_source(path: Path) -> str:
    try:
        return str(path.relative_to(CEX_ROOT))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------

def _extract_jsonl(path: Path) -> Iterator[Tuple[str, str]]:
    """Yield (session, text) pairs from a JSONL file."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            yield ("", line)
            continue
        if not isinstance(obj, dict):
            yield ("", json.dumps(obj))
            continue
        session = str(obj.get("session_id") or obj.get("session") or "")
        parts: List[str] = []
        for field in ("content", "text", "message"):
            val = obj.get(field)
            if isinstance(val, str) and val.strip():
                parts.append(val)
        if not parts:
            payload = obj.get("payload")
            if isinstance(payload, dict):
                parts.append(json.dumps(payload))
            else:
                parts.append(json.dumps(obj))
        yield (session, " ".join(parts))


def _extract_file(path: Path) -> Iterator[Tuple[str, str]]:
    """Yield (session, text) pairs from any supported file."""
    suffix = path.suffix.lower()
    if suffix == ".jsonl":
        yield from _extract_jsonl(path)
        return
    if suffix == ".json":
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
            obj = json.loads(raw)
            session = ""
            if isinstance(obj, dict):
                session = str(obj.get("session_id") or obj.get("session") or "")
                content = (obj.get("content") or obj.get("text") or
                           obj.get("message") or json.dumps(obj))
            else:
                content = json.dumps(obj)
            yield (session, str(content))
        except (OSError, json.JSONDecodeError):
            pass
        return
    # plain text / log / md
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    stem = path.stem
    session = stem if (stem.startswith("sess_") or "session" in stem.lower()) else ""
    yield (session, text)


# ---------------------------------------------------------------------------
# Low-level index helpers
# ---------------------------------------------------------------------------

def _insert_doc(conn: sqlite3.Connection, session: str, source: str,
                chunk_no: int, content: str, ts: str) -> None:
    cur = conn.execute(
        "INSERT INTO docs(session, source, chunk_no, content, ts) VALUES(?,?,?,?,?)",
        (session, source, chunk_no, content, ts)
    )
    doc_id = cur.lastrowid
    try:
        conn.execute(
            "INSERT INTO docs_fts(rowid, content, session, source) VALUES(?,?,?,?)",
            (doc_id, content, session, source)
        )
    except sqlite3.OperationalError:
        pass


def _delete_docs_for_source(conn: sqlite3.Connection, source: str) -> None:
    rows = conn.execute(
        "SELECT doc_id, content, session, source FROM docs WHERE source=?",
        (source,)
    ).fetchall()
    for r in rows:
        try:
            conn.execute(
                "INSERT INTO docs_fts(docs_fts, rowid, content, session, source)"
                " VALUES('delete',?,?,?,?)",
                (r["doc_id"], r["content"], r["session"], r["source"])
            )
        except sqlite3.OperationalError:
            pass
    conn.execute("DELETE FROM docs WHERE source=?", (source,))


def _delete_docs_for_session(conn: sqlite3.Connection, session: str) -> None:
    rows = conn.execute(
        "SELECT doc_id, content, session, source FROM docs WHERE session=?",
        (session,)
    ).fetchall()
    for r in rows:
        try:
            conn.execute(
                "INSERT INTO docs_fts(docs_fts, rowid, content, session, source)"
                " VALUES('delete',?,?,?,?)",
                (r["doc_id"], r["content"], r["session"], r["source"])
            )
        except sqlite3.OperationalError:
            pass
    conn.execute("DELETE FROM docs WHERE session=?", (session,))


def _index_path(conn: sqlite3.Connection, path: Path,
                session_filter: Optional[str]) -> int:
    """Index a single file; returns chunk count."""
    source = _rel_source(path)
    ts = _now_iso()
    count = 0
    for session, text in _extract_file(path):
        if session_filter and session and session != session_filter:
            continue
        for i, chunk in enumerate(_chunk(text)):
            _insert_doc(conn, session, source, i, chunk, ts)
            count += 1
    return count


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_index(args: argparse.Namespace,
              db_path: Optional[Path] = None) -> None:
    session = (getattr(args, "session", "") or "").strip()
    conn = _open_db(db_path)

    if session:
        _delete_docs_for_session(conn, session)

    sources: List[Path] = []
    if TRACES_DIR.is_dir():
        for p in TRACES_DIR.rglob("*"):
            if p.is_file() and p.suffix.lower() in _INDEXABLE_SUFFIXES:
                sources.append(p)
    if HOOK_LOG.is_file():
        sources.append(HOOK_LOG)
    if HANDOFFS_DIR.is_dir():
        for p in HANDOFFS_DIR.glob("*.md"):
            sources.append(p)

    total = 0
    for path in sources:
        total += _index_path(conn, path, session_filter=session or None)

    conn.commit()
    conn.close()
    label = ("session '" + session + "'") if session else "all sources"
    print("[OK] Indexed " + str(total) + " chunks from " +
          str(len(sources)) + " files (" + label + ").")


def _fts_query(conn: sqlite3.Connection, query: str,
               top_k: int) -> List[Dict]:
    try:
        rows = conn.execute("""
            SELECT d.doc_id, d.session, d.source, d.chunk_no,
                   d.content, d.ts, docs_fts.rank AS bm25
            FROM docs_fts
            JOIN docs d ON docs_fts.rowid = d.doc_id
            WHERE docs_fts MATCH ?
            ORDER BY bm25
            LIMIT ?
        """, (query, top_k)).fetchall()
    except sqlite3.OperationalError as exc:
        print("[WARN] FTS5 error: " + str(exc), file=sys.stderr)
        return []
    return [dict(r) for r in rows]


def _heuristic_summarize(hits: List[Dict],
                         token_budget: int = DEFAULT_TOKEN_BUDGET) -> str:
    if not hits:
        return "No results to summarize."
    parts: List[str] = []
    used = 0
    for hit in hits:
        content = hit["content"].replace("\n", " ")
        sentences = [s.strip() for s in content.split(". ") if s.strip()]
        snippet = ". ".join(sentences[:2]) if sentences else content[:200]
        t = _tokens(snippet)
        if used + t > token_budget:
            break
        src = hit.get("source", "")
        parts.append("[" + src + "] " + snippet)
        used += t
    return "\n\n".join(parts)


def _llm_summarize(hits: List[Dict], query: str,
                   token_budget: int) -> str:
    try:
        from cex_sdk.models.chat import chat
        context = "\n---\n".join(
            "[" + h.get("source", "") + "] " + h["content"][:300]
            for h in hits[:5]
        )
        _prompt = (
            "Search results for query: " + query +
            "\n\n" + context +
            "\n\nSummarize the above in 1-2 paragraphs."
        )
        try:
            from _tools.cex_model_resolver import resolve_model_for_tool
            _model = resolve_model_for_tool("cex_fts5_search", "light")["model"]
        except Exception:
            _model = "claude-haiku-4-5-20251001"
        return chat(_prompt, model=_model, max_tokens=min(token_budget, 400))
    except Exception as exc:
        return "LLM summarize failed: " + str(exc)


def cmd_query(args: argparse.Namespace,
              db_path: Optional[Path] = None) -> None:
    conn = _open_db(db_path)
    top_k = getattr(args, "top_k", DEFAULT_TOP_K) or DEFAULT_TOP_K
    budget = getattr(args, "token_budget", DEFAULT_TOKEN_BUDGET) or DEFAULT_TOKEN_BUDGET
    do_summarize = getattr(args, "summarize", False)

    hits = _fts_query(conn, args.query, top_k=top_k)
    conn.close()

    if not hits:
        print("No results found for: " + args.query)
        return

    if do_summarize:
        llm_env = os.environ.get("CEX_SEARCH_LLM", "").strip()
        if llm_env:
            print(_llm_summarize(hits, args.query, budget))
        else:
            print(_heuristic_summarize(hits, budget))
        return

    used = 0
    for hit in hits:
        snippet = hit["content"][:200]
        t = _tokens(snippet)
        if used + t > budget:
            break
        src = hit.get("source", "?")
        score = round(hit.get("bm25") or 0.0, 3)
        print("[" + src + " bm25=" + str(score) + "] " + snippet)
        print()
        used += t


def cmd_stats(_args: argparse.Namespace,
              db_path: Optional[Path] = None) -> None:
    conn = _open_db(db_path)
    total = conn.execute("SELECT COUNT(*) FROM docs").fetchone()[0]
    sessions = conn.execute(
        "SELECT COUNT(DISTINCT session) FROM docs WHERE session != ''"
    ).fetchone()[0]
    sources = conn.execute(
        "SELECT COUNT(DISTINCT source) FROM docs"
    ).fetchone()[0]
    conn.close()
    print("FTS5 index stats:")
    print("  total chunks : " + str(total))
    print("  sessions     : " + str(sessions))
    print("  source files : " + str(sources))


# ---------------------------------------------------------------------------
# Public API (used by cex_user_model.py search)
# ---------------------------------------------------------------------------

def search(query: str, top_k: int = DEFAULT_TOP_K,
           db_path: Optional[Path] = None) -> List[Dict]:
    """Return top-K BM25-ranked hits for query."""
    conn = _open_db(db_path)
    hits = _fts_query(conn, query, top_k=top_k)
    conn.close()
    return hits


def index_text(session: str, source: str, content: str,
               db_path: Optional[Path] = None) -> int:
    """Index arbitrary text under a session/source label. Returns chunk count."""
    conn = _open_db(db_path)
    ts = _now_iso()
    count = 0
    for i, chunk in enumerate(_chunk(content)):
        _insert_doc(conn, session, source, i, chunk, ts)
        count += 1
    conn.commit()
    conn.close()
    return count


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cex_fts5_search",
        description="FTS5 session search + optional LLM summarization (HERMES W4.4)"
    )
    sub = p.add_subparsers(dest="command", required=True)

    pi = sub.add_parser("index", help="(Re)index session traces into FTS5")
    pi.add_argument("--session", default="",
                    help="Session ID to re-index; omit to index all sources")

    pq = sub.add_parser("query", help="BM25-ranked full-text search")
    pq.add_argument("--query", required=True, help="FTS5 query string")
    pq.add_argument("--summarize", action="store_true",
                    help="Condense hits to 1-2 paragraphs (heuristic or LLM)")
    pq.add_argument("--top-k", type=int, default=DEFAULT_TOP_K,
                    dest="top_k", help="Max hits (default 5)")
    pq.add_argument("--token-budget", type=int, default=DEFAULT_TOKEN_BUDGET,
                    dest="token_budget", help="Max output tokens (default 500)")

    sub.add_parser("stats", help="Show FTS5 index statistics")
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    dispatch = {
        "index": cmd_index,
        "query": cmd_query,
        "stats": cmd_stats,
    }
    fn = dispatch.get(args.command)
    if fn:
        fn(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
