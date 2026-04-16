#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Vector Store -- L2 semantic retriever using numpy cosine similarity.

Design: hnswlib was the target but doesn't build on Python 3.14.
This implements a numpy-based cosine similarity fallback that works
identically for CEX's scale (~2000 artifacts, ~128-384 dim embeddings).

Architecture:
  L1 retriever: cex_retriever.py (TF-IDF, keyword-based)
  L2 retriever: cex_vector_store.py (this file, semantic embeddings)

The vector store uses a simple .npz file for persistence. Embeddings
are generated via Ollama's /api/embed endpoint (local, $0).

Usage (import):
    from cex_vector_store import VectorStore
    vs = VectorStore()
    vs.add("doc_id", embedding_vector, metadata={"kind": "knowledge_card"})
    results = vs.search(query_vector, top_k=5)

Usage (CLI):
    python _tools/cex_vector_store.py index          # build index from artifacts
    python _tools/cex_vector_store.py search "query"  # search with embedding
    python _tools/cex_vector_store.py stats           # index stats
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy required. pip install numpy", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = ROOT / ".cex" / "cache" / "vectors"
INDEX_FILE = INDEX_DIR / "vector_index.npz"
META_FILE = INDEX_DIR / "vector_meta.json"

OLLAMA_BASE = "http://localhost:11434"
EMBED_MODEL = "qwen3:14b"  # Ollama model for embeddings


class VectorStore:
    """In-memory vector store with numpy cosine similarity."""

    def __init__(self, index_path=None, meta_path=None):
        self.index_path = Path(index_path or INDEX_FILE)
        self.meta_path = Path(meta_path or META_FILE)
        self.vectors = None  # np.ndarray (N, D) or None
        self.ids = []        # list of doc IDs
        self.metadata = {}   # doc_id -> metadata dict
        self._load()

    def _load(self):
        """Load index from disk if available."""
        if self.index_path.exists() and self.meta_path.exists():
            try:
                data = np.load(str(self.index_path))
                self.vectors = data["vectors"]
                meta = json.loads(self.meta_path.read_text(encoding="utf-8"))
                self.ids = meta.get("ids", [])
                self.metadata = meta.get("metadata", {})
            except Exception:
                self.vectors = None
                self.ids = []
                self.metadata = {}

    def _save(self):
        """Persist index to disk."""
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        if self.vectors is not None and len(self.ids) > 0:
            np.savez_compressed(str(self.index_path), vectors=self.vectors)
            meta = {"ids": self.ids, "metadata": self.metadata,
                    "updated": time.time(), "count": len(self.ids)}
            self.meta_path.write_text(
                json.dumps(meta, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

    def add(self, doc_id: str, vector: Any, metadata: dict[str, Any] | None = None) -> None:
        """Add a document vector to the store.

        Args:
            doc_id: Unique identifier for the document.
            vector: List or numpy array of floats (embedding).
            metadata: Optional dict of metadata.
        """
        vec = np.array(vector, dtype=np.float32).reshape(1, -1)

        # Normalize for cosine similarity
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm

        if self.vectors is None:
            self.vectors = vec
        else:
            # Check dimension match
            if vec.shape[1] != self.vectors.shape[1]:
                raise ValueError(
                    "Dimension mismatch: index has %d, got %d" % (
                        self.vectors.shape[1], vec.shape[1])
                )
            # Check for duplicate ID -- replace if exists
            if doc_id in self.ids:
                idx = self.ids.index(doc_id)
                self.vectors[idx] = vec[0]
            else:
                self.vectors = np.vstack([self.vectors, vec])
                self.ids.append(doc_id)

        if metadata:
            self.metadata[doc_id] = metadata

    def search(
        self,
        query_vector: Any,
        top_k: int = 5,
        threshold: float = 0.0,
    ) -> list[tuple[str, float, dict[str, Any]]]:
        """Search for most similar vectors.

        Args:
            query_vector: Query embedding (list or numpy array).
            top_k: Number of results to return.
            threshold: Minimum cosine similarity (0-1).

        Returns:
            List of (doc_id, similarity, metadata) tuples, sorted by similarity desc.
        """
        if self.vectors is None or len(self.ids) == 0:
            return []

        qvec = np.array(query_vector, dtype=np.float32).reshape(1, -1)
        norm = np.linalg.norm(qvec)
        if norm > 0:
            qvec = qvec / norm

        # Cosine similarity (vectors are pre-normalized)
        similarities = (self.vectors @ qvec.T).flatten()

        # Get top-k indices
        if top_k >= len(self.ids):
            top_indices = np.argsort(similarities)[::-1]
        else:
            top_indices = np.argpartition(similarities, -top_k)[-top_k:]
            top_indices = top_indices[np.argsort(similarities[top_indices])[::-1]]

        results = []
        for idx in top_indices:
            sim = float(similarities[idx])
            if sim < threshold:
                continue
            doc_id = self.ids[idx]
            meta = self.metadata.get(doc_id, {})
            results.append((doc_id, sim, meta))

        return results

    def remove(self, doc_id: str) -> bool:
        """Remove a document from the store."""
        if doc_id not in self.ids:
            return False
        idx = self.ids.index(doc_id)
        self.vectors = np.delete(self.vectors, idx, axis=0)
        self.ids.pop(idx)
        self.metadata.pop(doc_id, None)
        if len(self.ids) == 0:
            self.vectors = None
        return True

    def save(self) -> None:
        """Explicit save (also called by CLI commands)."""
        self._save()

    def count(self) -> int:
        """Number of vectors in store."""
        return len(self.ids)

    def dimensions(self) -> int:
        """Embedding dimensions."""
        if self.vectors is not None:
            return self.vectors.shape[1]
        return 0


# ================================================================
# Ollama Embedding Helper
# ================================================================

def get_embedding(
    text: str,
    model: str = EMBED_MODEL,
    base_url: str = OLLAMA_BASE,
) -> list[float] | None:
    """Get embedding vector from Ollama /api/embed endpoint.

    Args:
        text: Text to embed.
        model: Ollama model name.
        base_url: Ollama API base URL.

    Returns:
        List of floats (embedding vector) or None on error.
    """
    import urllib.request
    import urllib.error

    url = "%s/api/embed" % base_url
    payload = json.dumps({"model": model, "input": text}).encode("utf-8")
    req = urllib.request.Request(
        url, data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            embeddings = data.get("embeddings", [])
            if embeddings and len(embeddings) > 0:
                return embeddings[0]
    except (urllib.error.URLError, OSError, json.JSONDecodeError):
        pass

    return None


# ================================================================
# CLI
# ================================================================

def _collect_artifacts():
    """Find all .md artifacts with frontmatter in nucleus directories."""
    import re
    artifacts = []
    for d in sorted(os.listdir(str(ROOT))):
        if not d.startswith("N0") or not os.path.isdir(str(ROOT / d)):
            continue
        for md in sorted(Path(ROOT / d).rglob("*.md")):
            if any(part.startswith(".") for part in md.parts):
                continue
            try:
                text = md.read_text(encoding="utf-8")
                if text.startswith("---\n"):
                    fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
                    if fm_match:
                        fm = fm_match.group(1)
                        kind_m = re.search(r"kind:\s*(\S+)", fm)
                        kind = kind_m.group(1).strip().strip("'\"") if kind_m else "unknown"
                        # Use first 500 chars of body as text for embedding
                        body = text[fm_match.end():][:500]
                        artifacts.append({
                            "id": str(md.relative_to(ROOT)),
                            "kind": kind,
                            "text": "%s %s" % (kind, body.strip()),
                            "path": str(md),
                        })
            except (OSError, UnicodeDecodeError):
                continue
    return artifacts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX Vector Store -- L2 semantic retriever (numpy cosine)"
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("stats", help="Show index statistics")
    sub.add_parser("index", help="Build/rebuild index from artifacts")

    search_p = sub.add_parser("search", help="Search by text query")
    search_p.add_argument("query", help="Search query text")
    search_p.add_argument("--top-k", type=int, default=5)
    search_p.add_argument("--threshold", type=float, default=0.3)

    args = parser.parse_args()
    vs = VectorStore()

    if args.command == "stats":
        print("CEX Vector Store Stats")
        print("  Vectors:    %d" % vs.count())
        print("  Dimensions: %d" % vs.dimensions())
        print("  Index file: %s" % vs.index_path)
        if vs.meta_path.exists():
            meta = json.loads(vs.meta_path.read_text(encoding="utf-8"))
            if meta.get("updated"):
                import datetime
                print("  Updated:    %s" % datetime.datetime.fromtimestamp(
                    meta["updated"]).isoformat())

    elif args.command == "index":
        artifacts = _collect_artifacts()
        print("Found %d artifacts to index" % len(artifacts))

        indexed = 0
        failed = 0
        for i, art in enumerate(artifacts):
            emb = get_embedding(art["text"])
            if emb:
                vs.add(art["id"], emb, metadata={
                    "kind": art["kind"], "path": art["path"]
                })
                indexed += 1
            else:
                failed += 1

            if (i + 1) % 50 == 0:
                print("  Progress: %d/%d (indexed=%d, failed=%d)" % (
                    i + 1, len(artifacts), indexed, failed))

        vs.save()
        print("Done. Indexed: %d  Failed: %d  Total: %d" % (
            indexed, failed, vs.count()))

    elif args.command == "search":
        if vs.count() == 0:
            print("Index is empty. Run: python _tools/cex_vector_store.py index")
            sys.exit(1)

        emb = get_embedding(args.query)
        if not emb:
            print("Failed to get embedding for query. Is Ollama running?",
                  file=sys.stderr)
            sys.exit(1)

        results = vs.search(emb, top_k=args.top_k, threshold=args.threshold)
        if not results:
            print("No results above threshold %.2f" % args.threshold)
        else:
            print("%-5s | %-20s | Path" % ("Score", "Kind"))
            print("-" * 70)
            for doc_id, sim, meta in results:
                print("%.3f | %-20s | %s" % (
                    sim, meta.get("kind", "?")[:20], doc_id))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
