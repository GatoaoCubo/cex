#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Retriever -- TF-IDF semantic search over all CEX artifacts.

Indexes all .md artifacts, builds a TF-IDF matrix, and provides
similarity search for F3 INJECT knowledge injection.

Usage:
    python cex_retriever.py --build                    # Build/rebuild index
    python cex_retriever.py --query "RAG chunking"     # Find similar artifacts
    python cex_retriever.py --query "agent" --kind agent --top-k 3
    python cex_retriever.py --stats                    # Show index statistics
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import parse_frontmatter

CEX_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = CEX_ROOT / ".cex"
INDEX_PATH = INDEX_DIR / "retriever_index.json"

SKIP_DIRS = {".git", ".obsidian", "__pycache__", "node_modules", ".cex", "compiled"}


# ---------------------------------------------------------------------------
# Text Processing
# ---------------------------------------------------------------------------

# Common stopwords (EN + PT) for TF-IDF filtering
STOPWORDS = frozenset([
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "can", "could", "and", "or", "but", "if",
    "then", "else", "when", "where", "which", "that", "this", "these",
    "those", "it", "its", "in", "on", "at", "to", "for", "from", "by",
    "with", "of", "as", "not", "no",
    "o", "os", "um", "uma", "uns", "umas", "de", "do", "da", "dos", "das",
    "em", "no", "na", "nos", "nas", "para", "por", "com", "se", "que",
    "e", "ou", "nao", "eh", "como", "mais",
])

_WORD_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]{2,}")


def tokenize(text: str) -> list[str]:
    """Extract lowercase word tokens (3+ chars, no stopwords)."""
    words = _WORD_RE.findall(text.lower())
    return [w for w in words if w not in STOPWORDS]


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter from markdown."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            return text[end + 3:].strip()
    return text


# ---------------------------------------------------------------------------
# TF-IDF Implementation (pure stdlib -- no numpy/sklearn required)
# ---------------------------------------------------------------------------

import math
from collections import Counter


def build_tfidf(corpus: list[list[str]]) -> tuple[dict[str, int], list[dict[str, float]]]:
    """Build TF-IDF vectors from tokenized corpus.

    Returns:
        vocab: word -> index mapping
        vectors: list of {word: tfidf_score} dicts per document
    """
    n_docs = len(corpus)
    if n_docs == 0:
        return {}, []

    # Document frequency
    df: Counter = Counter()
    for doc_tokens in corpus:
        unique = set(doc_tokens)
        for word in unique:
            df[word] += 1

    # Vocabulary: only words appearing in 2+ docs but < 90% of docs
    max_df = int(n_docs * 0.9)
    vocab = {}
    for word, freq in sorted(df.items()):
        if 2 <= freq <= max_df:
            vocab[word] = len(vocab)

    # TF-IDF vectors
    vectors = []
    for doc_tokens in corpus:
        tf = Counter(doc_tokens)
        total = len(doc_tokens) or 1
        vec = {}
        for word, count in tf.items():
            if word in vocab:
                tf_val = count / total
                idf_val = math.log(n_docs / (1 + df[word]))
                score = tf_val * idf_val
                if score > 0.001:
                    vec[word] = round(score, 5)
        vectors.append(vec)

    return vocab, vectors


def cosine_similarity(vec_a: dict[str, float], vec_b: dict[str, float]) -> float:
    """Compute cosine similarity between two sparse TF-IDF vectors."""
    common = set(vec_a) & set(vec_b)
    if not common:
        return 0.0

    dot = sum(vec_a[w] * vec_b[w] for w in common)
    norm_a = math.sqrt(sum(v * v for v in vec_a.values()))
    norm_b = math.sqrt(sum(v * v for v in vec_b.values()))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


# ---------------------------------------------------------------------------
# Artifact Scanning
# ---------------------------------------------------------------------------


def scan_artifacts(root: Path) -> list[dict]:
    """Scan all .md artifacts with frontmatter, return metadata + text."""
    artifacts = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            if fname.startswith("README") or fname.startswith("_schema"):
                continue

            fpath = Path(dirpath) / fname
            try:
                text = fpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            fm = parse_frontmatter(text)
            if not fm or "kind" not in fm:
                continue

            rel = fpath.relative_to(root).as_posix()
            body = strip_frontmatter(text)

            artifacts.append({
                "path": rel,
                "id": fm.get("id", fpath.stem),
                "kind": fm.get("kind", ""),
                "pillar": fm.get("pillar", ""),
                "title": fm.get("title", fpath.stem),
                "tags": fm.get("tags", []),
                "tldr": fm.get("tldr", ""),
                "body_preview": body[:500],
                "tokens": tokenize(f"{fm.get('title', '')} {fm.get('tldr', '')} {body}"),
            })
    return artifacts


# ---------------------------------------------------------------------------
# Index Build & Load
# ---------------------------------------------------------------------------


def build_index(verbose: bool = False) -> dict:
    """Build TF-IDF index from all artifacts."""
    t0 = time.time()

    artifacts = scan_artifacts(CEX_ROOT)
    if verbose:
        print(f"  Scanned {len(artifacts)} artifacts")

    corpus = [a["tokens"] for a in artifacts]
    vocab, vectors = build_tfidf(corpus)

    if verbose:
        print(f"  Vocabulary: {len(vocab)} terms")

    # Build index structure (serializable)
    docs = []
    for art in artifacts:
        docs.append({
            "path": art["path"],
            "id": art["id"],
            "kind": art["kind"],
            "pillar": art["pillar"],
            "title": art["title"],
            "tags": art["tags"] if isinstance(art["tags"], list) else [],
            "tldr": art["tldr"],
            "body_preview": art["body_preview"],
        })

    index = {
        "version": "1.0.0",
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "n_docs": len(docs),
        "n_vocab": len(vocab),
        "docs": docs,
        "vocab": vocab,
        "vectors": vectors,
    }

    elapsed = time.time() - t0

    # Save
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")

    if verbose:
        size_kb = INDEX_PATH.stat().st_size / 1024
        print(f"  Index: {INDEX_PATH} ({size_kb:.0f} KB)")
        print(f"  Built in {elapsed:.1f}s")

    return index


def load_index() -> dict | None:
    """Load index from disk. Returns None if not found."""
    if not INDEX_PATH.exists():
        return None
    try:
        return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


# ---------------------------------------------------------------------------
# Search API
# ---------------------------------------------------------------------------


def find_similar(
    query: str,
    index: dict | None = None,
    kind: str | None = None,
    pillar: str | None = None,
    top_k: int = 5,
    min_score: float = 0.05,
) -> list[dict]:
    """Find artifacts most similar to query text.

    Args:
        query: Natural language query or artifact text
        index: Pre-loaded index (loads from disk if None)
        kind: Filter results to this kind only
        pillar: Filter results to this pillar only
        top_k: Maximum results to return
        min_score: Minimum cosine similarity threshold

    Returns:
        List of {path, id, kind, pillar, title, tldr, score} dicts
    """
    if index is None:
        index = load_index()
    if not index or not index.get("vectors"):
        return []

    # Tokenize query and build TF-IDF vector using index vocab
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    vocab = index["vocab"]
    n_docs = index["n_docs"]

    # Compute query TF-IDF using the index's IDF values
    tf = Counter(query_tokens)
    total = len(query_tokens)
    query_vec = {}
    for word, count in tf.items():
        if word in vocab:
            tf_val = count / total
            # Approximate IDF from vocabulary (word exists = appeared in corpus)
            idf_val = math.log(n_docs / (1 + n_docs * 0.1))  # conservative estimate
            query_vec[word] = tf_val * idf_val

    if not query_vec:
        # Fallback: use raw TF if no vocab overlap
        for word, count in tf.items():
            query_vec[word] = count / total

    # Score all documents
    scored = []
    for i, doc_vec in enumerate(index["vectors"]):
        if not doc_vec:
            continue

        doc = index["docs"][i]

        # Apply filters
        if kind and doc.get("kind") != kind:
            continue
        if pillar and doc.get("pillar") != pillar:
            continue

        score = cosine_similarity(query_vec, doc_vec)
        if score >= min_score:
            scored.append({
                "path": doc["path"],
                "id": doc["id"],
                "kind": doc["kind"],
                "pillar": doc["pillar"],
                "title": doc["title"],
                "tldr": doc.get("tldr", ""),
                "score": round(score, 4),
            })

    # Sort by score descending, return top_k
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]


def find_examples_for_kind(
    kind: str,
    intent: str = "",
    index: dict | None = None,
    top_k: int = 3,
) -> list[dict]:
    """Find the best example artifacts for a given kind + intent.

    Searches for artifacts whose kind matches AND whose content is
    semantically similar to the intent. Returns examples sorted by relevance.
    """
    if index is None:
        index = load_index()
    if not index:
        return []

    # Combine kind name + intent for richer query
    query = f"{kind} {intent}".strip()

    # First: find same-kind examples (strongest signal)
    same_kind = find_similar(query, index=index, kind=kind, top_k=top_k * 2, min_score=0.01)

    # Second: find cross-kind examples (weaker but sometimes useful)
    cross_kind = find_similar(query, index=index, top_k=top_k, min_score=0.10)

    # Merge: same-kind first (boosted), then cross-kind (if slots remain)
    seen = set()
    results = []
    for item in same_kind:
        if item["id"] not in seen:
            seen.add(item["id"])
            item["score"] = round(item["score"] * 1.5, 4)  # Boost same-kind
            results.append(item)

    for item in cross_kind:
        if item["id"] not in seen and len(results) < top_k:
            seen.add(item["id"])
            results.append(item)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def show_stats(index: dict):
    """Print index statistics."""
    print("\n=== CEX Retriever Index ===")
    print(f"  Version:    {index.get('version')}")
    print(f"  Built:      {index.get('built_at')}")
    print(f"  Documents:  {index.get('n_docs')}")
    print(f"  Vocabulary: {index.get('n_vocab')}")

    # Kind distribution
    kinds: Counter = Counter()
    pillars: Counter = Counter()
    for doc in index.get("docs", []):
        kinds[doc.get("kind", "?")] += 1
        pillars[doc.get("pillar", "?")] += 1

    print("\n--- Kinds (top 15) ---")
    for kind, count in kinds.most_common(15):
        print(f"    {kind:30s} {count:>4d}")

    print("\n--- Pillars ---")
    for pillar, count in sorted(pillars.items()):
        print(f"    {pillar:10s} {count:>4d}")


def main():
    parser = argparse.ArgumentParser(description="CEX Retriever -- TF-IDF semantic search")
    parser.add_argument("--build", action="store_true", help="Build/rebuild the index")
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--kind", "-k", help="Filter by kind")
    parser.add_argument("--pillar", "-p", help="Filter by pillar")
    parser.add_argument("--top-k", "-n", type=int, default=5, help="Maximum results")
    parser.add_argument("--min-score", "-s", type=float, default=0.05, help="Minimum similarity score")
    parser.add_argument("--stats", action="store_true", help="Show index statistics")
    parser.add_argument("--examples", "-e", help="Find examples for kind")
    parser.add_argument("--intent", "-i", help="Intent for example search")
    parser.add_argument("--output", "-o", help="Output format (json, table, markdown)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    if args.build:
        build_index(args.verbose)
        return

    if args.stats:
        index = load_index()
        if not index:
            print("No index found. Run --build first.")
            return
        show_stats(index)
        return

    if args.examples:
        index = load_index()
        if not index:
            print("No index found. Run --build first.")
            return
        examples = find_examples_for_kind(args.examples, intent=args.intent, index=index)
        if args.output == "json":
            print(json.dumps(examples, indent=2))
        elif args.output == "table":
            print("=== Examples ===")
            for e in examples:
                print(f"{e['title']} ({e['score']:.2f})")
        elif args.output == "markdown":
            print("### Examples")
            for e in examples:
                print(f"- **{e['title']}** ({e['score']:.2f})")
        else:
            print("=== Examples ===")
            for e in examples:
                print(f"{e['title']} ({e['score']:.2f})")
        return

    if args.query:
        index = load_index()
        if not index:
            print("No index found. Run --build first.")
            return
        results = find_similar(
            args.query,
            index=index,
            kind=args.kind,
            pillar=args.pillar,
            top_k=args.top_k,
            min_score=args.min_score,
        )
        if not results:
            print("No matching artifacts found.")
            return
        if args.output == "json":
            print(json.dumps(results, indent=2))
        elif args.output == "table":
            print("=== Search Results ===")
            for r in results:
                print(f"{r['title']} ({r['score']:.2f})")
        elif args.output == "markdown":
            print("### Search Results")
            for r in results:
                print(f"- **{r['title']}** ({r['score']:.2f})")
        else:
            print("=== Search Results ===")
            for r in results:
                print(f"{r['title']} ({r['score']:.2f})")
        return

    parser.print_help()
    return


if __name__ == "__main__":
    main()