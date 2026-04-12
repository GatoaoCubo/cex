---
id: extraction_hnsw_memory
kind: knowledge_card
pillar: P01_knowledge
title: "Extraction: HNSW Vector Memory from ruflo"
version: 1.0
quality: 8.9
tags: [extraction, hnsw, vector, retriever, ruflo, port]
created: 2026-04-12
author: n01_intelligence
domain: retrieval architecture
source: ruvnet/ruflo v3.5
tldr: "ruflo implements HNSW via agentdb + @ruvector/micro-hnsw-wasm with M=16, efConstruction=200, 1536-dim cosine. CEX can add HNSW as L2 layer behind existing TF-IDF."
---

# Extraction: HNSW Vector Memory (R1) from ruflo

## 1. Source Architecture

ruflo's memory system is a **hybrid backend**: SQLite for structured queries +
AgentDB/HNSW for semantic vector search. The routing strategy decides which
backend handles each query type.

### Process tree

```
HybridBackend (routing: auto | sqlite-first | agentdb-first)
  |
  +-- SQLite backend (exact, prefix, tag queries)
  +-- AgentDB backend (semantic, hybrid queries)
        |
        +-- HNSWIndex (pure TypeScript implementation)
        +-- @ruvector/micro-hnsw-wasm (WASM bridge, optional)
        +-- hnswlib-node (native fallback)
```

## 2. HNSW Index Parameters (exact values)

| Parameter | Default | Source file |
|-----------|---------|-------------|
| `dimensions` | 1536 | `v3/@claude-flow/memory/src/types.ts:246` |
| `M` (max connections/layer) | 16 | `v3/@claude-flow/memory/src/agentdb-backend.ts:78` |
| `efConstruction` | 200 | `v3/@claude-flow/memory/src/agentdb-backend.ts:79` |
| `efSearch` | 100 | `v3/@claude-flow/memory/src/agentdb-backend.ts:80` |
| `metric` | cosine | `v3/@claude-flow/memory/src/types.ts:44-48` |
| `maxElements` | 1000000 | `v3/@claude-flow/memory/src/agentdb-backend.ts:82` |
| `cacheEnabled` | true | `v3/@claude-flow/memory/src/agentdb-backend.ts:83` |

### Distance metrics supported

```
cosine (default) | euclidean | dot | manhattan
```

### Alternative dimensions

- 1536: OpenAI ada-002 (default)
- 384: MiniLM (mentioned in controller-registry.ts:113)

## 3. Data Structures

### HNSWNode (hnsw-index.ts:192-207)

```typescript
interface HNSWNode {
  id: string;
  vector: Float32Array;              // raw embedding
  normalizedVector: Float32Array | null;  // pre-normalized for O(1) cosine
  connections: Map<number, Set<string>>;  // per-layer adjacency list
  level: number;                     // top layer of this node
}
```

### SearchOptions (types.ts)

```typescript
interface SearchOptions {
  k: number;              // number of results
  ef?: number;            // search expansion factor (higher = more accurate, slower)
  threshold?: number;     // minimum similarity 0-1
  metric?: DistanceMetric;
  filters?: MemoryQuery;  // post-search filtering
}
```

### QueryType routing

```
semantic  -> HNSW index
exact     -> SQLite LIKE
prefix    -> SQLite LIKE prefix%
tag       -> SQLite tag join
hybrid    -> both backends, merge + deduplicate
```

## 4. Performance Characteristics

| Metric | Value | Source |
|--------|-------|--------|
| Speed vs brute-force | 150x-12,500x faster | CLAUDE.md benchmarks |
| Cache hit rate | 95%+ | hybrid-backend.ts |
| Batch insert size | 50 embeddings | agentdb-backend.ts:445-495 |
| Level multiplier | `1/log(M)` = 0.25 for M=16 | hnsw-index.ts |
| Storage precision | Float32 (32-bit per dimension) | types.ts |

### Key optimizations in ruflo

1. **Pre-normalized vectors**: eliminates sqrt in cosine similarity (O(1) vs O(n))
2. **Binary/scalar/product quantization**: optional compression for large indexes
3. **BinaryMinHeap + BinaryMaxHeap**: O(log n) candidate selection during search
4. **Dual-write mode**: both SQLite + AgentDB stay synchronized

## 5. CEX Integration Plan

### Current state: `_tools/cex_retriever.py`

CEX uses pure-Python TF-IDF with stdlib only (no numpy/sklearn):
- `build_tfidf()`: Counter-based DF, sparse dict vectors
- `cosine_similarity()`: dot product over common keys
- Vocab filter: words in 2+ docs but <90% of docs
- Index size: 2184 docs, 12K vocab terms
- Storage: JSON file at `.cex/retriever_index.json`

**Strengths** (keep): zero dependencies, fast cold start, good for keyword matching
**Weakness** (fix): no semantic understanding -- "agent orchestration" won't match "multi-model dispatch"

### Proposed: L2 HNSW layer

```
Query
  |
  +-- L1: TF-IDF (cex_retriever.py) -- fast, keyword-exact, 0 deps
  |     returns top-20 candidates in <50ms
  |
  +-- L2: HNSW (cex_retriever_hnsw.py) -- semantic, embedding-based
  |     returns top-20 candidates via vector similarity
  |
  +-- Merge: RRF (Reciprocal Rank Fusion) or weighted union
        returns top-k final results
```

### Implementation: `_tools/cex_retriever_hnsw.py`

**Option A: hnswlib (C++ via Python bindings)**
- Library: `pip install hnswlib` (mature, 5K+ GitHub stars)
- Pros: fast, battle-tested, pure C++ backend
- Cons: requires C++ build tools on Windows

**Option B: chromadb (batteries-included)**
- Library: `pip install chromadb`
- Pros: built-in HNSW + persistence + embedding functions
- Cons: heavy dependency (pulls in onnxruntime, etc.)

**Option C: Ollama local embeddings + hnswlib** (RECOMMENDED)
- Use Ollama (already running on RTX 5070 Ti) for embeddings
- Use hnswlib for index storage and search
- Zero cloud dependency, all local
- Model: `nomic-embed-text` (768 dims) or `mxbai-embed-large` (1024 dims)

### Recommended parameters for CEX

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| dimensions | 768 | nomic-embed-text on local Ollama |
| M | 16 | ruflo default, good balance for <100K docs |
| efConstruction | 200 | ruflo default, high quality index build |
| efSearch | 50 | CEX has ~2200 docs, lower ef is fine |
| metric | cosine | standard for text embeddings |
| maxElements | 50000 | 25x current corpus, room for growth |

### Files to create/modify

| File | Action | Lines est. |
|------|--------|-----------|
| `_tools/cex_retriever_hnsw.py` | CREATE | ~250 |
| `_tools/cex_retriever.py` | MODIFY -- add `--mode hybrid` flag | ~30 |
| `.cex/config/retriever_config.yaml` | CREATE -- HNSW params | ~20 |
| `requirements.txt` | MODIFY -- add `hnswlib` | 1 |

### Estimated effort

- **Complexity**: Medium (standalone module + integration glue)
- **Lines of code**: ~300 new + ~30 modified
- **Dependencies**: hnswlib (pip), Ollama API for embeddings
- **Risk**: Low -- side-by-side with TF-IDF, no breaking changes

## 6. Comparative Analysis

| Dimension | CEX TF-IDF (current) | ruflo HNSW | Proposed CEX L1+L2 |
|-----------|---------------------|------------|-------------------|
| Semantic understanding | None (keyword only) | Full (embedding-based) | Hybrid (best of both) |
| Cold start | <1s (JSON load) | ~5s (index build) | <1s L1, lazy-load L2 |
| Dependencies | Zero (stdlib) | agentdb + wasm | hnswlib + ollama |
| Memory footprint | ~2MB (sparse dicts) | ~50MB (1536d x 10K) | ~15MB (768d x 2.2K) |
| Query latency | <50ms | <5ms (after warm) | <60ms (both layers) |
| Accuracy at scale | Degrades >10K docs | Stable to 1M | Stable to 50K |

## 7. Key Code References in ruflo

| File (relative to ruflo/) | What it contains |
|---------------------------|-----------------|
| `v3/@claude-flow/memory/src/hnsw-index.ts` | Full HNSW implementation (BFS, heaps, layers) |
| `v3/@claude-flow/memory/src/types.ts` | HNSWConfig, SearchOptions, DistanceMetric types |
| `v3/@claude-flow/memory/src/agentdb-backend.ts` | Default config values, batch insert logic |
| `v3/@claude-flow/memory/src/hybrid-backend.ts` | Dual-backend routing (semantic/exact/hybrid) |
| `v3/@claude-flow/memory/src/agentdb-adapter.ts` | Embedding generation interface |
| `v3/@claude-flow/memory/benchmarks/hnsw-indexing.bench.ts` | Performance benchmarks |
| `v3/plugins/ruvector-upstream/src/bridges/hnsw.ts` | WASM bridge (fallback chain) |
