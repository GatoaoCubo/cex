#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX SQLite Indexer -- scans all .md/.yaml, parses frontmatter + wikilinks, stores in .cex/index.db"""

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import parse_frontmatter as _shared_parse_frontmatter

ROOT = Path(__file__).resolve().parent.parent
DB_DIR = ROOT / ".cex"
DB_PATH = DB_DIR / "index.db"

SKIP_DIRS = {".git", ".obsidian", "__pycache__", "node_modules", ".cex"}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
BODY_KEYWORDS_RE = re.compile(r"^keywords:\s*\[([^\]]+)\]", re.MULTILINE)


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from --- delimited block (delegates to cex_shared)."""
    return _shared_parse_frontmatter(text) or {}


def extract_wikilinks(text: str) -> list[str]:
    """Extract all [[target]] wikilinks from text."""
    return WIKILINK_RE.findall(text)


def compute_density(text: str) -> float:
    """Approximate information density: non-whitespace ratio."""
    if not text:
        return 0.0
    stripped = text.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
    return round(len(stripped) / len(text), 3) if len(text) > 0 else 0.0


def init_db(conn: sqlite3.Connection) -> None:
    """Create tables if they don't exist."""
    conn.executescript("""
        DROP TABLE IF EXISTS files;
        DROP TABLE IF EXISTS edges;

        CREATE TABLE files (
            path          TEXT PRIMARY KEY,
            id            TEXT,
            type          TEXT,
            pillar        TEXT,
            quality       REAL,
            size_bytes    INTEGER,
            density       REAL,
            keywords_json TEXT,
            axioms_json   TEXT,
            domain        TEXT,
            kind          TEXT,
            created       TEXT,
            modified      TEXT
        );

        CREATE TABLE edges (
            source_path   TEXT,
            target_id     TEXT,
            link_type     TEXT DEFAULT 'wikilink',
            FOREIGN KEY (source_path) REFERENCES files(path)
        );

        CREATE INDEX idx_files_type ON files(type);
        CREATE INDEX idx_files_pillar ON files(pillar);
        CREATE INDEX idx_files_quality ON files(quality);
        CREATE INDEX idx_files_kind ON files(kind);
        CREATE INDEX idx_edges_source ON edges(source_path);
        CREATE INDEX idx_edges_target ON edges(target_id);
    """)


def scan_files(root: Path) -> list[Path]:
    """Recursively find all .md and .yaml files, skipping excluded dirs."""
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(".md") or f.endswith(".yaml") or f.endswith(".yml"):
                results.append(Path(dirpath) / f)
    return results


def index_file(filepath: Path, root: Path) -> tuple[dict[str, Any], list[tuple[str, str, str]]]:
    """Parse a single file, return (file_row, edge_rows)."""
    rel = filepath.relative_to(root).as_posix()
    stat = filepath.stat()
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        text = ""

    fm = parse_frontmatter(text)
    density = compute_density(text)
    wikilinks = extract_wikilinks(text)

    # Normalize frontmatter fields
    keywords = fm.get("keywords", [])
    if isinstance(keywords, str):
        keywords = [k.strip() for k in keywords.split(",")]
    # A2: fallback -- extract keywords from body ## Routing section if frontmatter empty
    if not keywords and "bld_model" in rel:
        body_match = BODY_KEYWORDS_RE.search(text)
        if body_match:
            keywords = [k.strip() for k in body_match.group(1).split(",")]
    axioms = fm.get("axioms", [])
    if isinstance(axioms, str):
        axioms = [a.strip() for a in axioms.split(",")]

    quality = fm.get("quality")
    if quality is not None:
        try:
            quality = float(quality)
        except (ValueError, TypeError):
            quality = None

    # Normalize kind field (can be list in some templates)
    raw_kind = fm.get("kind", "")
    if isinstance(raw_kind, list):
        raw_kind = ", ".join(str(k) for k in raw_kind)

    file_row = {
        "path": rel,
        "id": fm.get("id", filepath.stem),
        "type": fm.get("type", raw_kind),
        "pillar": fm.get("pillar", fm.get("lp", "")),
        "quality": quality,
        "size_bytes": stat.st_size,
        "density": density,
        "keywords_json": json.dumps(keywords) if keywords else "[]",
        "axioms_json": json.dumps(axioms) if axioms else "[]",
        "domain": fm.get("domain", ""),
        "kind": raw_kind,
        "created": time.strftime("%Y-%m-%d", time.localtime(stat.st_ctime)),
        "modified": time.strftime("%Y-%m-%d", time.localtime(stat.st_mtime)),
    }

    edge_rows = [(rel, target, "wikilink") for target in wikilinks]
    return file_row, edge_rows


def rebuild(verbose: bool = False) -> None:
    """Full rebuild of the index."""
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    init_db(conn)

    files = scan_files(ROOT)
    total_edges = 0
    t0 = time.time()

    for fp in files:
        try:
            row, edges = index_file(fp, ROOT)
            conn.execute(
                "INSERT INTO files VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    row["path"],
                    row["id"],
                    row["type"],
                    row["pillar"],
                    row["quality"],
                    row["size_bytes"],
                    row["density"],
                    row["keywords_json"],
                    row["axioms_json"],
                    row["domain"],
                    row["kind"],
                    row["created"],
                    row["modified"],
                ),
            )
            if edges:
                conn.executemany("INSERT INTO edges VALUES (?,?,?)", edges)
                total_edges += len(edges)
        except Exception as e:
            if verbose:
                print(f"  WARN: {fp}: {e}", file=sys.stderr)

    conn.commit()
    elapsed = time.time() - t0

    print(f"Indexed {len(files)} files, {total_edges} edges in {elapsed:.1f}s")
    print(f"Database: {DB_PATH} ({DB_PATH.stat().st_size / 1024:.0f} KB)")
    conn.close()


def show_stats() -> None:
    """Print index statistics."""
    conn = sqlite3.connect(str(DB_PATH))
    total = conn.execute("SELECT COUNT(*) FROM files").fetchone()[0]
    edges = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    with_quality = conn.execute("SELECT COUNT(*) FROM files WHERE quality IS NOT NULL").fetchone()[
        0
    ]
    avg_quality = conn.execute(
        "SELECT AVG(quality) FROM files WHERE quality IS NOT NULL"
    ).fetchone()[0]
    avg_density = conn.execute("SELECT AVG(density) FROM files").fetchone()[0]

    print("\n=== CEX Index Stats ===")
    print(f"Total files:    {total}")
    print(f"Total edges:    {edges}")
    print(f"With quality:   {with_quality}")
    if avg_quality:
        print(f"Avg quality:    {avg_quality:.2f}")
    print(f"Avg density:    {avg_density:.3f}")

    # Top types
    print("\n--- Types (top 15) ---")
    for row in conn.execute(
        "SELECT type, COUNT(*) as c FROM files WHERE type != '' GROUP BY type ORDER BY c DESC LIMIT 15"
    ):
        print(f"  {row[0]:40s} {row[1]:>5d}")

    # Top pillars
    print("\n--- Pillars ---")
    for row in conn.execute(
        "SELECT pillar, COUNT(*) as c FROM files WHERE pillar != '' GROUP BY pillar ORDER BY pillar"
    ):
        print(f"  {row[0]:20s} {row[1]:>5d}")

    # Top link targets
    print("\n--- Most linked targets (top 10) ---")
    for row in conn.execute(
        "SELECT target_id, COUNT(*) as c FROM edges GROUP BY target_id ORDER BY c DESC LIMIT 10"
    ):
        print(f"  {row[0]:50s} {row[1]:>5d}")

    conn.close()


def query(expression: str) -> None:
    """Run a simple field=value query against the files table."""
    conn = sqlite3.connect(str(DB_PATH))
    # Parse simple expressions: field=value, field>value, field<value
    m = re.match(r"(\w+)\s*(=|>|<|>=|<=|!=|LIKE)\s*(.+)", expression, re.IGNORECASE)
    if not m:
        print(f"Invalid query: {expression}")
        print("Format: field=value, field>value, field LIKE %pattern%")
        return

    field, op, value = m.group(1), m.group(2), m.group(3).strip().strip("'\"")

    # Validate field
    valid_fields = {
        "path",
        "id",
        "type",
        "pillar",
        "quality",
        "size_bytes",
        "density",
        "keywords_json",
        "axioms_json",
        "domain",
        "kind",
        "created",
        "modified",
    }
    if field not in valid_fields:
        print(f"Unknown field: {field}. Valid: {', '.join(sorted(valid_fields))}")
        return

    sql = f"SELECT path, id, type, pillar, quality, density FROM files WHERE {field} {op} ?"
    try:
        rows = conn.execute(sql, (value,)).fetchall()
    except sqlite3.OperationalError as e:
        print(f"Query error: {e}")
        return

    print(f"\n{len(rows)} results for: {field} {op} {value}\n")
    for r in rows:
        q = f"q={r[4]:.1f}" if r[4] else "q=--"
        print(f"  {r[0]:60s} id={r[1]:30s} type={r[2]:20s} {q}  d={r[5]:.2f}")
    conn.close()


def orphans() -> None:
    """Find files with no incoming wikilinks."""
    conn = sqlite3.connect(str(DB_PATH))
    rows = conn.execute("""
        SELECT f.path, f.id, f.type
        FROM files f
        LEFT JOIN edges e ON f.id = e.target_id
        WHERE e.target_id IS NULL
        ORDER BY f.path
    """).fetchall()

    print(f"\n{len(rows)} orphan files (no incoming links):\n")
    for r in rows:
        print(f"  {r[0]:60s} id={r[1]:30s} type={r[2]}")
    conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="CEX SQLite Indexer")
    parser.add_argument("--query", "-q", help="Query: field=value (e.g. type=knowledge_card)")
    parser.add_argument("--orphans", action="store_true", help="Show files with no incoming links")
    parser.add_argument("--stats", "-s", action="store_true", help="Show index statistics")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    if args.query:
        if not DB_PATH.exists():
            print("No index found. Run without arguments to build first.")
            sys.exit(1)
        query(args.query)
    elif args.orphans:
        if not DB_PATH.exists():
            print("No index found. Run without arguments to build first.")
            sys.exit(1)
        orphans()
    elif args.stats:
        if not DB_PATH.exists():
            print("No index found. Run without arguments to build first.")
            sys.exit(1)
        show_stats()
    else:
        print("Rebuilding CEX index...")
        rebuild(verbose=args.verbose)
        show_stats()


if __name__ == "__main__":
    main()
