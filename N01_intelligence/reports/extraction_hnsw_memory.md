---
id: extraction_hnsw_memory
kind: knowledge_card
pillar: P01
nucleus: N01
domain: retrieval
title: "Extraction: HNSW Vector Memory (R1 -- ruflo)"
version: 1.0
quality: 8.2
tags: [extraction, hnsw, vector_memory, retrieval, ruflo, port_plan]
created: 2026-04-17
source: C:/Users/CEX/Documents/GitHub/_external/ruflo/
source_files:
  - v3/@claude-flow/memory/benchmarks/hnsw-indexing.bench.ts
  - v3/@claude-flow/memory/src/agentdb-backend.ts
  - CLAUDE.md (intelligence pipeline section)
port_priority: P0_HIGH
---

# Extraction: HNSW Vector Memory (R1 -- ruflo)

> Source: `ruvnet/ruflo` | Priority: P0 HIGH | Effort: Medium | Blocking: No (side install)

## 1. What ruflo implements

Ruflo's `@claude-flow/memory` package wraps AgentDB with HNSW (Hierarchical Navigable Small World)
indexing for semantic recall at scale. The HNSW layer sits between the caller and a SQLite
backend, providing O(log n) approximate nearest-neighbor search instead of O(n) brute-force.

Claimed speedup: **150x--12,500x** vs brute-force vector search (from ruflo CLAUDE.md).

## 2. Exact HNSW parameters (source of truth)

### Production config (`agentdb-backend.ts` DEFAULT_CONFIG)

| Parameter | Value | Description |
|-----------|-------|-------------|
| `vectorDimension` | 1536 | OpenAI embedding dims (overridable to 384 for all-MiniLM) |
| `hnswM` | 16 | Max bidirectional connections per node per layer |
| `hnswEfConstruction` | 200 | Dynamic candidate list size during index build |
| `hnswEfSearch` | 100 | Dynamic candidate list size during query |
| `maxEntries` | 1,000,000 | Max vectors in index |
| `forceWasm` | false | Prefer native hnswlib-node; fall back to WASM |
| `vectorBackend` | 'auto' | Resolves: ruvector > hnswlib > WASM |
| `cacheEnabled` | true | Cache layer on top of HNSW |

### Benchmark config (`hnsw-indexing.bench.ts`)

```typescript
const DEFAULT_HNSW_CONFIG = {
  dimensions: 384,         // all-MiniLM-L6-v2 size
  maxElements: 100000,
  M: 16,
  efConstruction: 200,
  mL: 1 / Math.log(16),   // = 0.2789 -- level generation param
};
```

### Distance metric

Cosine distance (1 - dot product on L2-normalized vectors):

```typescript
private distance(a: Float32Array, b: Float32Array): number {
  let dot = 0;
  for (let i = 0; i < a.length; i++) dot += a[i] * b[i];
  return 1 - dot;  // cosine distance on pre-normalized vectors
}
```

## 3. Algorithm structure (from benchmark implementation)

```
INSERT(vector, id):
  1. randomLevel = floor(-ln(uniform()) * mL)  -- probabilistic level assignment
  2. Greedy descent from max_level to randomLevel+1
  3. For each level l from min(randomLevel, maxLevel) down to 0:
     a. searchLayer(vector, entry, l, efConstruction) -> candidates
     b. Select top-M neighbors (heuristic)
     c. Connect bidirectionally (prune to M if over-limit)
  4. Update entry point if new max_level

SEARCH(query, k, ef=50):
  1. Greedy descent from max_level to 1 (ef=1 fast path)
  2. Full searchLayer at level 0 with ef=max(ef, k)
  3. Return top-k from results
```

## 4. Benchmark targets (from bench file)

| Operation | Target | Notes |
|-----------|--------|-------|
| Single insert | <10ms | Per-bench assertion |
| Batch insert 100 | ~varies | Per-vector overhead |
| Search k=10 on 1000 vectors | <5ms | ef=50 |
| Vector removal | <5ms | Marks tombstone + unlinks |
| Optimal M formula | M = 2 * log2(dims) | For 384 dims: M=17 |

## 5. Optimization strategies (from bench file)

| Strategy | Expected improvement | Implementation |
|----------|---------------------|----------------|
| Optimal M selection | 10-30% | M = round(2 * log2(dimensions)) |
| Parallel construction | 2-4x | Worker threads, merge partial indices |
| Incremental updates | 20-50% | Batch threshold 100, flush on overflow |
| Memory-mapped storage | 30-50% memory, 10-20% speed | mmap-io for large indices |

## 6. CEX integration plan

### Target: `_tools/cex_retriever.py` -- add L2 HNSW semantic layer

**Current architecture:**

```
cex_retriever.py --> TF-IDF (sklearn) --> .cex/retriever_index.json
```

**Proposed 2-layer architecture:**

```
cex_retriever.py --> L1: TF-IDF fast path (token match, existing)
                 --> L2: HNSW semantic path (embedding similarity, new)
                 --> Merge: L1 boosts exact-term hits, L2 elevates semantic neighbors
```

### New file: `_tools/cex_retriever_hnsw.py`

```python
# Pseudo-implementation
class HNSWRetriever:
    CONFIG = {
        "dimensions": 384,         # all-MiniLM-L6-v2
        "max_elements": 50000,     # CEX artifact ceiling
        "M": 17,                   # optimal for 384 dims: 2*log2(384)=17
        "ef_construction": 200,
        "ef_search": 50,
        "space": "cosine",
    }

    def build(self, artifacts: list[dict]) -> None:
        """Embed all artifacts, insert into HNSW index."""
        import hnswlib
        index = hnswlib.Index(space='cosine', dim=self.CONFIG["dimensions"])
        index.init_index(
            max_elements=self.CONFIG["max_elements"],
            M=self.CONFIG["M"],
            ef_construction=self.CONFIG["ef_construction"],
        )
        embeddings = self._embed_batch([a["text"] for a in artifacts])
        index.add_items(embeddings, range(len(artifacts)))
        index.set_ef(self.CONFIG["ef_search"])
        self._save(index)

    def query(self, text: str, top_k: int = 10) -> list[dict]:
        """Return top-k semantically similar artifacts."""
        index = self._load()
        query_embed = self._embed(text)
        labels, distances = index.knn_query(query_embed, k=top_k)
        return self._format_results(labels[0], distances[0])
```

### Dependency installation

```bash
pip install hnswlib sentence-transformers
# OR (ruflo approach: WASM fallback if no native):
# pip install hnswlib  # native C++ extension
# pip install usearch  # alternative pure WASM
```

### Integration point in cex_retriever.py

- **Lines to modify**: `build_index()`, `search()`, `main()`
- **New flag**: `--semantic` to activate HNSW layer (off by default -- no-op install)
- **Index file**: `.cex/retriever_hnsw.bin` (hnswlib binary format)
- **Embedding cache**: `.cex/embeddings_cache.json` (avoid re-embedding on query)

## 7. Comparison: CEX TF-IDF vs HNSW

| Dimension | CEX TF-IDF (current) | HNSW (proposed L2) |
|-----------|---------------------|---------------------|
| Algorithm | Token frequency | Approximate nearest neighbor |
| Recall quality | High for exact terms | High for semantic similarity |
| Speed | O(n) at query time | O(log n) at query time |
| Build time | ~5s for 2184 docs | ~30s first build (embedding) |
| Query time | ~50ms | ~2ms after index load |
| Semantic matching | No ("chunking" won't find "segmentation") | Yes |
| Cold start | Fast (TF-IDF from JSON) | Slow (embedding model load ~1s) |
| Disk footprint | ~5MB JSON | ~20MB bin + ~150MB model |
| **Verdict** | Good baseline | Best for F3 INJECT quality |

## 8. Estimated effort

| Task | Complexity | Lines |
|------|-----------|-------|
| `cex_retriever_hnsw.py` (new) | Medium | ~200 |
| Modify `cex_retriever.py` for 2-layer merge | Low | ~50 |
| Embedding model integration | Low | ~30 |
| Tests + bench | Low | ~100 |
| **Total** | **Medium** | **~380** |

## 9. Risks

| Risk | Mitigation |
|------|-----------|
| hnswlib native build fails on Windows | Add WASM fallback (hnswlib-wasm or usearch) |
| Embedding model 150MB download | Cache model; skip HNSW if no network/slow start |
| Embedding drift over time | Include model name + version in index metadata |
| Semantic hallucination (unrelated "neighbors") | Threshold: ignore results with distance > 0.5 |
