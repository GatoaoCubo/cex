#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Builder Discovery Query Tool -- find builders by keyword, domain, or natural language intent.

Usage:
    python _tools/cex_query.py "criar agente de vendas"
    python _tools/cex_query.py "monetizar curso hotmart" --top 3
    python _tools/cex_query.py "webhook hotmart" --json
    python _tools/cex_query.py --rebuild-cache
    python _tools/cex_query.py "criar agente" --suggest-crew
"""

import argparse
import json
import math
import re
import sqlite3
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / ".cex" / "index.db"

# ---------------------------------------------------------------------------
# Normalization & tokenization
# ---------------------------------------------------------------------------

# PT/EN stop words (common ones that add no search value)
STOP_WORDS = {
    "a", "o", "e", "de", "do", "da", "para", "com", "em", "um", "uma", "os", "as",
    "no", "na", "nos", "nas", "que", "se", "por", "mais", "como", "sobre", "este",
    "the", "a", "an", "and", "or", "o", "to", "in", "for", "with", "on", "is", "it",
    "this", "that", "from", "by", "at", "be", "as", "are", "was", "will", "has",
    "criar", "create", "build", "make", "novo", "new",
}

# Simple PT/EN suffix stripping (poor man's stemmer -- no external deps)
SUFFIXES = [
    "iza\u00e7\u00e3o", "iza\u00e7\u00e3o", "amento", "imento", "mente", "ador", "edor",
    "tion", "sion", "ment", "ness", "able", "ible", "ful", "less", "ing", "ous",
    "ando", "endo", "indo", "\u00e7\u00f5es", "\u00e7\u00e3o", "\u00f5es", "\u00e3o",
    "izar", "izar", "izar", "ar", "er", "ir",
    "ed", "ly", "er", "es", "al", "ive",
]


def normalize(text: str) -> str:
    """Lowercase, remove accents (simple), strip punctuation."""
    text = text.lower().strip()
    # Simple accent removal for PT
    for src, dst in [("\u00e1", "a"), ("\u00e0", "a"), ("\u00e3", "a"), ("\u00e2", "a"),
                     ("\u00e9", "e"), ("\u00ea", "e"), ("\u00ed", "i"), ("\u00f3", "o"),
                     ("\u00f4", "o"), ("\u00f5", "o"), ("\u00fa", "u"), ("\u00fc", "u"),
                     ("\u00e7", "c")]:
        text = text.replace(src, dst)
    # Replace hyphens/underscores with spaces for tokenization
    text = re.sub(r"[-_]", " ", text)
    # Remove non-alphanumeric except spaces
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return text


def stem(word: str) -> str:
    """Simple suffix stripping -- good enough for keyword matching."""
    if len(word) <= 4:
        return word
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)]
    return word


def tokenize(text: str) -> list[str]:
    """Normalize, split, remove stop words, stem."""
    words = normalize(text).split()
    tokens = []
    for w in words:
        if w not in STOP_WORDS and len(w) >= 2:
            tokens.append(stem(w))
    return tokens


# ---------------------------------------------------------------------------
# Index loading
# ---------------------------------------------------------------------------

def load_builders(conn: sqlite3.Connection) -> list[dict]:
    """Load all bld_model rows from the index."""
    rows = conn.execute(
        "SELECT id, kind, domain, keywords_json, pillar, path FROM files "
        "WHERE path LIKE '%bld_model%'"
    ).fetchall()
    builders = []
    for row in rows:
        kw_raw = row[3] or "[]"
        try:
            keywords = json.loads(kw_raw)
        except json.JSONDecodeError:
            keywords = []
        builders.append({
            "builder_id": row[0],
            "kind": row[1],
            "domain": row[2] or "",
            "keywords": [normalize(k) for k in keywords if isinstance(k, str)],
            "keywords_raw": keywords,
            "pillar": row[4] or "",
            "path": row[5],
        })
    return builders


# ---------------------------------------------------------------------------
# TF-IDF scoring
# ---------------------------------------------------------------------------

def build_idf(builders: list[dict]) -> dict[str, float]:
    """Build inverse document frequency from builder keywords."""
    doc_count = len(builders)
    if doc_count == 0:
        return {}
    df = Counter()
    for b in builders:
        # Unique stems per builder
        stems = set()
        for kw in b["keywords"]:
            for token in kw.split():
                stems.add(stem(token))
        # Also stem domain
        for token in normalize(b["domain"]).split():
            stems.add(stem(token))
        df.update(stems)
    return {term: math.log(doc_count / (1 + count)) for term, count in df.items()}


def score_builder(builder: dict, query_tokens: list[str], idf: dict[str, float]) -> float:
    """Score a builder against query tokens using weighted TF-IDF matching."""
    if not query_tokens:
        return 0.0

    # Collect all builder terms (stemmed)
    kw_stems = set()
    for kw in builder["keywords"]:
        for token in kw.split():
            kw_stems.add(stem(token))

    domain_stems = set()
    for token in normalize(builder["domain"]).split():
        domain_stems.add(stem(token))

    kind_stems = set()
    for token in normalize(builder.get("kind", "")).split():
        kind_stems.add(stem(token))

    score = 0.0
    matched_keywords = []

    for qt in query_tokens:
        term_idf = idf.get(qt, 1.0)

        # Keyword match (weight: 0.6)
        if qt in kw_stems:
            score += 0.6 * term_idf
            matched_keywords.append(qt)

        # Substring keyword match (weight: 0.3) -- handles partial matches
        elif any(qt in ks or ks in qt for ks in kw_stems if len(ks) >= 3):
            score += 0.3 * term_idf
            matched_keywords.append(f"~{qt}")

        # Domain match (weight: 0.3)
        if qt in domain_stems:
            score += 0.3 * term_idf

        # Kind match (weight: 0.1)
        if qt in kind_stems:
            score += 0.1 * term_idf

    # Normalize by query length to keep scores comparable
    if query_tokens:
        score /= len(query_tokens)

    return round(score, 4), matched_keywords


# ---------------------------------------------------------------------------
# Query function (importable)
# ---------------------------------------------------------------------------

def query_builders(query_text: str, top_k: int = 5, db_path: Path = DB_PATH) -> list[dict]:
    """Query builders by natural language. Returns list of {builder_id, kind, pillar, score, keywords_matched}."""
    if not db_path.exists():
        return []

    conn = sqlite3.connect(str(db_path))
    builders = load_builders(conn)
    conn.close()

    if not builders:
        return []

    query_tokens = tokenize(query_text)
    if not query_tokens:
        return []

    idf = build_idf(builders)

    results = []
    for b in builders:
        score, matched = score_builder(b, query_tokens, idf)
        if score > 0:
            results.append({
                "builder_id": b["builder_id"],
                "kind": b["domain"],
                "pillar": b["pillar"],
                "score": score,
                "keywords_matched": matched,
                "path": b["path"],
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]


# ---------------------------------------------------------------------------
# Suggest crew (bonus)
# ---------------------------------------------------------------------------

def suggest_crew(query_text: str, db_path: Path = DB_PATH) -> list[dict]:
    """Return suggested crew from bld_orchestration for top-matching builder."""
    results = query_builders(query_text, top_k=1, db_path=db_path)
    if not results:
        return []

    top = results[0]
    builder_dir = top["builder_id"]
    # Try to find orchestration file
    collab_pattern = f"archetypes/builders/{builder_dir}"
    conn = sqlite3.connect(str(db_path))
    rows = conn.execute(
        "SELECT path FROM files WHERE path LIKE ? AND path LIKE '%orchestration%'",
        (f"%{builder_dir}%",)
    ).fetchall()
    conn.close()

    if not rows:
        return [{"builder": top["builder_id"], "crew": "no orchestration file found"}]

    # Read the orchestration file
    collab_path = ROOT / rows[0][0]
    if collab_path.exists():
        try:
            text = collab_path.read_text(encoding="utf-8", errors="replace")
            return [{"builder": top["builder_id"], "orchestration": text[:500]}]
        except Exception:
            pass

    return [{"builder": top["builder_id"], "crew": "orchestration file unreadable"}]


# ---------------------------------------------------------------------------
# Rebuild cache (re-index)
# ---------------------------------------------------------------------------

def rebuild_cache():
    """Rebuild the index.db by calling cex_index.py."""
    index_script = ROOT / "_tools" / "cex_index.py"
    if index_script.exists():
        subprocess.run([sys.executable, str(index_script)], check=True)
    else:
        print("ERROR: _tools/cex_index.py not found", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CEX Builder Discovery -- find builders by keyword or natural language intent"
    )
    parser.add_argument("query", nargs="?", help="Natural language query (e.g. 'monetizar curso hotmart')")
    parser.add_argument("--top", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--rebuild-cache", action="store_true", help="Rebuild keyword index from manifests")
    parser.add_argument("--suggest-crew", action="store_true", help="Show recommended crew for top match")
    parser.add_argument("--intent", action="store_true", help="Use Motor 8F OBJECT_TO_KINDS as fallback")
    args = parser.parse_args()

    if args.rebuild_cache:
        rebuild_cache()
        return

    if not args.query:
        parser.print_help()
        sys.exit(1)

    if not DB_PATH.exists():
        print("No index.db found. Run: python _tools/cex_index.py", file=sys.stderr)
        sys.exit(1)

    # Main query
    results = query_builders(args.query, top_k=args.top)

    # Intent fallback: if few results, try Motor 8F OBJECT_TO_KINDS
    if args.intent and len(results) < 2:
        try:
            sys.path.insert(0, str(ROOT / "_tools"))
            from cex_8f_motor import OBJECT_TO_KINDS
            tokens = tokenize(args.query)
            for token in tokens:
                for obj_key, kinds_list in OBJECT_TO_KINDS.items():
                    if token in normalize(obj_key):
                        for kind, pillar, fn in kinds_list:
                            if not any(r["kind"] == kind for r in results):
                                results.append({
                                    "builder_id": f"{kind}-builder",
                                    "kind": kind,
                                    "pillar": pillar,
                                    "score": 0.1,
                                    "keywords_matched": [f"motor:{obj_key}"],
                                    "path": f"archetypes/builders/{kind}-builder/",
                                })
        except ImportError:
            pass

    if args.suggest_crew:
        crew = suggest_crew(args.query)
        if args.json:
            print(json.dumps(crew, indent=2, ensure_ascii=False))
        else:
            for c in crew:
                print(f"\n=== Suggested Crew for: {c.get('builder', 'unknown')} ===")
                if "orchestration" in c:
                    print(c["orchestration"])
                else:
                    print(c.get("crew", "none"))
        return

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    # Pretty print
    print(f"\n=== CEX Builder Discovery: \"{args.query}\" (top {args.top}) ===\n")
    if not results:
        print("  No matching builders found.")
        print("  Try: --intent flag for Motor 8F fallback, or --rebuild-cache to refresh index.")
        return

    for i, r in enumerate(results, 1):
        kw = ", ".join(r["keywords_matched"][:5])
        print(f"  {i}. {r['builder_id']}")
        print(f"     kind={r['kind']}  pillar={r['pillar']}  score={r['score']:.3f}")
        print(f"     matched: {kw}")
        print()


if __name__ == "__main__":
    main()
