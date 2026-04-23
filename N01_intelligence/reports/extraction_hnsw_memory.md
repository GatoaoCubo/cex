---
quality: 8.3
quality: 8.0
id: extraction_hnsw_memory
kind: knowledge_card
pillar: P01
nucleus: N01
title: "R1 Extraction: HNSW Vector Memory -- ruflo AgentDB + RuVector"
version: 1.0
tags: [extraction, hnsw, vector_memory, retrieval, ruflo, cex_retriever]
created: 2026-04-19
domain: competitive-intelligence
source: ruvnet/ruflo (SPARC 3.0 agent runtime)
related:
  - p01_kc_supabase_vectors
  - p01_embedding_config_supabase
  - p01_kc_supabase_pgvector_rag_setup
  - bld_memory_vector_store
  - p03_sp_vector_store_builder
  - bld_knowledge_card_vector_store
  - port_plan_external_repos
  - p01_kc_vector_store
  - extraction_trust_tiers
  - bld_examples_vector_store
density_score: 1.0
updated: "2026-04-22"
---

# R1 Extraction: HNSW Vector Memory

> **Pattern**: Replace TF-IDF `cex_retriever.py` L2 with HNSW semantic layer.
> ruflo ships two distinct HNSW implementations; CEX should adopt the lighter one first.

## Competitive Baseline

| System | Retrieval Method | Latency | Scale | Memory |
|--------|-----------------|---------|-------|--------|
| CEX (current) | TF-IDF, 2184 docs, 12K vocab | ~5-50ms | <10K docs | Low |
| ruflo AgentDB | HNSW + sql.js (SQLite WASM) | <100us | <1M vectors | 4-32x reducible |
| ruflo RuVector | HNSW + PostgreSQL pgvector | <1ms | Unlimited | PG-managed |

**Gap**: CEX TF-IDF has no semantic recall. Two documents with different words but same meaning score zero similarity. HNSW closes this gap without replacing TF-IDF (stack, not swap).

## Two HNSW Implementations Found in ruflo

### Implementation 1 -- AgentDB (SQLite, recommended for reference)

**Package**: `agentic-flow` (npm), uses `sql.js` (WASM SQLite, cross-platform, no native compilation)

**Source files**:
- `_external/ruflo/v3/@claude-flow/cli/.claude/skills/agentdb-vector-search/SKILL.md`
- `_external/ruflo/v3/@claude-flow/cli/src/commands/embeddings.ts`

**Core API** (TypeScript excerpt):
```typescript
import { createAgentDBAdapter, computeEmbedding } from 'agentic-flow/reasoningbank';

const adapter = await createAgentDBAdapter({
  dbPath: '.agentdb/vectors.db',
  enableLearning: false,
  enableReasoning: true,
  quantizationType: 'binary',   // 32x memory reduction
  cacheSize: 1000,
});

const embedding = await computeEmbedding(text);  // 384-dim MiniLM
const results = await adapter.retrieveWithReasoning(queryEmbedding, {
  domain: 'cex-artifacts',
  k: 10,
  useMMR: true,           // Maximal Marginal Relevance -- diverse results
  synthesizeContext: true,
});
```

**Quantization options** (critical for RAM-constrained environments):
| Mode | Memory Reduction | When to Use |
|------|-----------------|-------------|
| `binary` | 32x | >1K artifacts, RAM constrained |
| `scalar` | 4x | Balanced default |
| `product` | 8-16x | Large-scale production |

### Implementation 2 -- RuVector (PostgreSQL, scale)

**Source file**: `_external/ruflo/v3/@claude-flow/cli/src/commands/ruvector/init.ts`

**Actual SQL from init.ts (lines 304-424)**:
```sql
-- Vector storage table
CREATE TABLE IF NOT EXISTS {schema}.embeddings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  key VARCHAR(512) NOT NULL,
  namespace VARCHAR(128) NOT NULL DEFAULT 'default',
  content TEXT,
  embedding vector(384),
  metadata JSONB DEFAULT '{}',
  UNIQUE(key, namespace)
);

-- HNSW index -- THE critical config
CREATE INDEX IF NOT EXISTS idx_embeddings_vector_hnsw
ON {schema}.embeddings
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```

**HNSW params**:
- `m = 16` -- connections per node (higher = better recall, more RAM)
- `ef_construction = 64` -- build-time quality (standard community default)
- Extension fallback: tries `ruvector` first, falls back to `pgvector`
- Alt index: IVFFlat with `lists = 100` for append-heavy workloads

**Additional tables created**:
- `attention_patterns` (query/key/value embeddings for attention mechanism)
- `gnn_edges` (graph neural network adjacency)
- `hyperbolic_embeddings` (Poincare ball model, curvature=-1.0)

## Performance Benchmark (from ruflo AgentDB SKILL.md)

| Operation | TF-IDF baseline | HNSW AgentDB | Speedup |
|-----------|----------------|--------------|---------|
| Pattern search (10K) | ~15ms | 100us | 150x |
| Batch insert (100 vectors) | ~1s | 2ms | 500x |
| Large-scale query (1M) | ~100s | 8ms | 12,500x |

## CEX Integration Plan

**Decision**: Do NOT use AgentDB (npm/JS). CEX is Python-first.
**Use `hnswlib`** (Python, Apache-2.0): same algorithm, native Python, no JS bridge.

### New file: `_tools/cex_retriever_hnsw.py`

```python
import hnswlib
import numpy as np
from sentence_transformers import SentenceTransformer

class HNSWRetriever:
    """L2 semantic retriever -- runs after TF-IDF L1 fast path."""

    MODEL = "all-MiniLM-L6-v2"   # 384-dim, matches ruflo AgentDB default
    DIM = 384
    INDEX_PATH = ".cex/cache/hnsw_index.bin"

    # HNSW params from ruflo RuVector init.ts
    M = 16
    EF_CONSTRUCTION = 64
    EF_SEARCH = 32  # standard: 2*k

    def __init__(self):
        self.model = SentenceTransformer(self.MODEL)
        self.index = hnswlib.Index(space='cosine', dim=self.DIM)

    def build(self, docs: list, ids: list):
        self.index.init_index(
            max_elements=len(docs),
            ef_construction=self.EF_CONSTRUCTION,
            M=self.M
        )
        vecs = self.model.encode(docs, batch_size=32, show_progress_bar=True)
        self.index.add_items(vecs, ids)
        self.index.save_index(self.INDEX_PATH)

    def query(self, query: str, k: int = 10) -> list:
        qvec = self.model.encode([query])[0]
        labels, distances = self.index.knn_query(qvec, k=k)
        return list(zip(labels[0].tolist(), distances[0].tolist()))
```

### Modify: `_tools/cex_retriever.py` (hybrid wrapper, ~10 lines added)

```python
def hybrid_retrieve(query: str, k: int = 10):
    # L1: TF-IDF fast path (existing)
    tfidf_results = existing_tfidf_search(query, k=k*2)
    # L2: HNSW semantic rerank
    if hnsw_index_exists():
        hnsw_results = hnsw_retriever.query(query, k=k)
        return merge_and_rerank(tfidf_results, hnsw_results, k=k)
    return tfidf_results[:k]
```

### Hook integration (session-start, `_tools/cex_hooks_native.py`)

```bash
python _tools/cex_retriever_hnsw.py --rebuild-if-stale
# Stale = any artifact newer than index mtime
```

## Estimated Effort

| Task | LoC | Complexity | Time |
|------|-----|------------|------|
| `cex_retriever_hnsw.py` | ~100 | Low | 2h |
| Hook integration | ~20 | Low | 30min |
| Index rebuild on artifact change | ~30 | Low | 1h |
| Benchmark vs TF-IDF | ~50 | Low | 1h |
| **Total** | **~200** | **Low** | **~5h** |

## Files to Modify

| File | Change |
|------|--------|
| `_tools/cex_retriever.py` | Add `hybrid_retrieve()` wrapper |
| `_tools/cex_retriever_hnsw.py` | NEW -- HNSW index builder + query |
| `requirements.txt` | Add `hnswlib>=0.8`, `sentence-transformers>=2.7` |
| `_tools/cex_hooks_native.py` | session-start: rebuild stale HNSW index |
| `.cex/cache/` | Storage: `hnsw_index.bin`, `hnsw_doc_map.json` |

## Source References

- AgentDB API: `_external/ruflo/v3/@claude-flow/cli/.claude/skills/agentdb-vector-search/SKILL.md`
- RuVector DDL: `_external/ruflo/v3/@claude-flow/cli/src/commands/ruvector/init.ts` lines 304-462
- HNSW params: `WITH (m = 16, ef_construction = 64)` at line 408
- Benchmark numbers: SKILL.md lines 200-208
- Port plan: `_docs/specs/port_plan_external_repos.md` pattern R1

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_vectors]] | sibling | 0.34 |
| [[p01_embedding_config_supabase]] | related | 0.34 |
| [[p01_kc_supabase_pgvector_rag_setup]] | sibling | 0.33 |
| [[bld_memory_vector_store]] | downstream | 0.29 |
| [[p03_sp_vector_store_builder]] | downstream | 0.29 |
| [[bld_knowledge_card_vector_store]] | sibling | 0.26 |
| [[port_plan_external_repos]] | related | 0.26 |
| [[p01_kc_vector_store]] | sibling | 0.25 |
| [[extraction_trust_tiers]] | sibling | 0.25 |
| [[bld_examples_vector_store]] | downstream | 0.24 |
