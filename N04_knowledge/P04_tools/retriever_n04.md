---
id: p04_ret_n04_knowledge
kind: retriever
8f: F3_inject
pillar: P04
nucleus: n04
title: "Retriever -- N04 Dense + Sparse Fusion Configuration"
version: "1.0.0"
quality: 9.1
tags: [retriever, n04, dense_retrieval, sparse_retrieval, hybrid, RRF, P04]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "N04 retriever configuration: primary=pgvector dense+BM25 sparse, fusion=RRF(k=60), reranker=cross-encoder, fallback chain to ChromaDB then TF-IDF. All tunable parameters and their current values."
density_score: null
related:
  - bld_knowledge_card_retriever_config
  - bld_examples_retriever_config
  - p10_bi_bm25_knowledge
  - p01_rc_hybrid_rag
  - p09_kc_retriever_domain
  - bld_architecture_retriever
  - p01_kc_retriever
  - bld_examples_retriever
  - p06_arch_rag_pipeline
  - bld_instruction_retriever
---

# Retriever: N04 Dense + Sparse Fusion Configuration

## Retriever Identity

| Property | Value |
|----------|-------|
| Primary strategy | Hybrid (dense + sparse) |
| Dense backend | pgvector (cosine similarity) |
| Sparse backend | BM25 / TF-IDF (cex_retriever.py) |
| Fusion algorithm | Reciprocal Rank Fusion (RRF, k=60) |
| Reranker | cross-encoder (optional, enabled by default) |
| Embedding model | text-embedding-3-small (1536 dim) |
| Fallback chain | pgvector -> ChromaDB -> TF-IDF -> grep |

---

## Dense Retriever Config

```yaml
dense_retriever:
  backend: pgvector
  connection:
    host: "${SUPABASE_URL}"
    key: "${SUPABASE_KEY}"
    table: "knowledge_documents"
  embedding:
    model: "text-embedding-3-small"
    dimensions: 1536
    encoding_format: "float"
  search:
    metric: "cosine"
    top_k_candidates: 20          # retrieve 20 before rerank
    score_threshold: 0.65
    ef_search: 64                 # HNSW search parameter
  namespaces:
    - "cex_artifacts"
    - "external_docs"
    - "session_memory"
```

---

## Sparse Retriever Config

```yaml
sparse_retriever:
  backend: bm25
  index_path: ".cex/cache/bm25_index.pkl"
  corpus_path: "N04_knowledge/"
  vocabulary_size: 12000          # current TF-IDF vocab
  k1: 1.5                        # BM25 term frequency saturation
  b: 0.75                        # BM25 length normalization
  top_k_candidates: 20
  fallback_to_grep: true         # if index stale or missing
```

---

## Fusion Config (RRF)

```yaml
fusion:
  algorithm: "reciprocal_rank_fusion"
  k: 60                          # RRF k parameter (constant, 60 is standard)
  weights:
    dense: 1.0
    sparse: 1.0
  normalize_scores: true         # normalize to 0-1 before fusion
  merge_top_k: 20               # merge top-20 from each retriever
  output_top_k: 10              # return top-10 after fusion
```

**Why RRF?**: No tuning required, handles different score scales from dense/sparse,
consistently outperforms weighted linear combination on knowledge retrieval.
(Cormack et al. 2009)

---

## Reranker Config

```yaml
reranker:
  enabled: true                  # enable by default
  model: "cross-encoder/ms-marco-MiniLM-L-6-v2"
  batch_size: 8
  max_length: 512
  threshold: null                # use top_k, not threshold after rerank
  candidates_to_rerank: 20       # rerank top-20 from fusion
  output_top_k: 10              # return top-10 after reranking
  fallback_on_error: true        # if reranker fails, return RRF results
```

---

## Fallback Chain

```
Level 1: pgvector (primary)
  |-- available if SUPABASE_URL and SUPABASE_KEY set
  |-- latency: 180ms (dense), 220ms (hybrid)
  |
  | FAIL -> Level 2
  v
Level 2: ChromaDB (local persistent)
  |-- available if chroma service running on localhost:8000
  |-- latency: 120ms (dense), 160ms (hybrid)
  |
  | FAIL -> Level 3
  v
Level 3: cex_retriever.py TF-IDF (embedded, zero dependency)
  |-- always available (pure Python, no external service)
  |-- 2184 documents indexed
  |-- latency: 45ms (sparse only, no dense)
  |-- note: no reranking at this level
  |
  | FAIL -> Level 4
  v
Level 4: grep-based keyword search
  |-- pure OS-level, no Python dependencies
  |-- bash: grep -r --include="*.md" "{query}" ./N04_knowledge/
  |-- latency: 5-20ms
  |-- no scoring, just presence detection
```

---

## Tuning Reference

| Parameter | Current | Range | Effect |
|-----------|---------|-------|--------|
| `score_threshold` | 0.65 | 0.40-0.90 | Lower = more recall, more noise |
| `top_k_candidates` | 20 | 5-100 | Higher = better recall pre-rerank |
| `rrf_k` | 60 | 10-200 | Higher = less rank compression |
| `ef_search` (HNSW) | 64 | 16-512 | Higher = better recall, slower |
| `bm25_k1` | 1.5 | 0.5-3.0 | Lower = less TF saturation |
| `bm25_b` | 0.75 | 0-1.0 | Lower = less length normalization |

---

## Performance Targets

| Metric | Target | Alert Threshold |
|--------|--------|----------------|
| MRR@10 | >= 0.83 | < 0.75 |
| NDCG@10 | >= 0.80 | < 0.72 |
| p95 latency | < 500ms | > 1000ms |
| Corpus coverage | 100% | < 95% |

See `memory_benchmark_n04.md` for current measured values.

---

## Integration

| Artifact | Role |
|---------|------|
| `search_tool_n04.md` | Consumes this retriever config |
| `api_reference_rag_apis.md` | pgvector + Pinecone API specs |
| `embedding_config_knowledge.md` | Embedding model config |
| `retriever_config_knowledge.md` | Dense retriever config (P01 KC) |
| `memory_benchmark_n04.md` | Regression baselines |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_retriever_config]] | upstream | 0.36 |
| [[bld_examples_retriever_config]] | downstream | 0.36 |
| [[p10_bi_bm25_knowledge]] | downstream | 0.35 |
| [[p01_rc_hybrid_rag]] | upstream | 0.32 |
| [[p09_kc_retriever_domain]] | downstream | 0.30 |
| [[bld_architecture_retriever]] | downstream | 0.28 |
| [[p01_kc_retriever]] | upstream | 0.28 |
| [[bld_examples_retriever]] | downstream | 0.27 |
| [[p06_arch_rag_pipeline]] | downstream | 0.26 |
| [[bld_instruction_retriever]] | upstream | 0.25 |
