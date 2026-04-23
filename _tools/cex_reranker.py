#!/usr/bin/env python3
"""cex_reranker.py: Rerank candidate docs by BM25 + title match.

For N04 leverage: improve retriever results with lexical reranking.
Minimal BM25 without external deps.

Usage:
    python _tools/cex_reranker.py --query "query string" path1.md path2.md ...
    python _tools/cex_reranker.py --query "RAG chunking" --top-k 5
    python _tools/cex_reranker.py --query "RAG chunking" --top-k 5 --json
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def bm25_score(query_tokens: list[str], doc_tokens: list[str], avg_len: float,
               doc_freqs: dict, n_docs: int, k1: float = 1.5, b: float = 0.75) -> float:
    score = 0.0
    dl = len(doc_tokens)
    if dl == 0:
        return 0.0
    tf_map = {}
    for t in doc_tokens:
        tf_map[t] = tf_map.get(t, 0) + 1
    for q in query_tokens:
        if q not in tf_map:
            continue
        df = doc_freqs.get(q, 1)
        idf = math.log((n_docs - df + 0.5) / (df + 0.5) + 1)
        tf = tf_map[q]
        denom = tf + k1 * (1 - b + b * dl / avg_len)
        score += idf * tf * (k1 + 1) / denom
    return score


def rerank(query: str, doc_paths: list[Path], top_k: int = 10) -> list[tuple[float, Path]]:
    docs = []
    for p in doc_paths:
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        docs.append((p, tokenize(txt)))
    if not docs:
        return []

    avg_len = sum(len(d[1]) for d in docs) / len(docs)
    doc_freqs = {}
    for _, toks in docs:
        for t in set(toks):
            doc_freqs[t] = doc_freqs.get(t, 0) + 1

    q_toks = tokenize(query)
    scored = []
    for path, toks in docs:
        s = bm25_score(q_toks, toks, avg_len, doc_freqs, len(docs))
        # title boost: bonus if query terms appear in filename
        name = path.stem.lower()
        title_hits = sum(1 for q in q_toks if q in name)
        s += title_hits * 0.5
        scored.append((s, path))

    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:top_k]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--query", required=True)
    p.add_argument("paths", nargs="*", help="document paths; defaults to P01_knowledge/library/**/*.md")
    p.add_argument("--top-k", type=int, default=10)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    if args.paths:
        doc_paths = [Path(x) for x in args.paths]
    else:
        lib = ROOT / "N00_genesis" / "P01_knowledge" / "library"
        doc_paths = list(lib.rglob("*.md")) if lib.exists() else []

    if not doc_paths:
        print("ERROR: no documents found", file=sys.stderr)
        return 1

    results = rerank(args.query, doc_paths, args.top_k)
    if args.json:
        out = [{"score": round(s, 3), "path": p.relative_to(ROOT).as_posix()} for s, p in results]
        print(json.dumps(out, indent=2))
    else:
        for s, path in results:
            rel = path.relative_to(ROOT).as_posix() if ROOT in path.parents else path
            print(f"{s:7.3f}  {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
