---
id: retriever_n01
kind: retriever
pillar: P04
nucleus: n01
title: "N01 Intelligence Corpus Retriever"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: null
tags: [retriever, rag, semantic_search, n01, knowledge_retrieval, corpus]
tldr: "Hybrid retriever for N01 knowledge corpus: BM25 (keyword) + dense embedding (semantic) with RRF fusion. Retrieves from N01_intelligence/ artifact store and .cex/cache/ compiled outputs."
density_score: 0.90
---

<!-- 8F: F1 constrain=P04/retriever F2 become=retriever-builder F3 inject=knowledge_index_intelligence+embedding_config_intelligence+rag_source_intelligence+search_strategy_n01 F4 reason=N01 Analytical Envy: before generating new research, retrieve what N01 already knows -- avoid redundancy, find contradictions F5 call=cex_compile F6 produce=retriever_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P04_tools/ -->

## Purpose

Analytical Envy drives N01 to ALWAYS compare new findings against existing knowledge.
Before any synthesis, N01 must query its own corpus to:
1. Avoid duplicating research already done
2. Identify contradictions (new data vs. old data = the interesting signal)
3. Build on existing intelligence (compound knowledge, not restart)

## Retrieval Architecture

| Component | Technology | Role |
|-----------|-----------|------|
| Sparse index | BM25 (rank_bm25) | keyword precision: exact terms, entity names |
| Dense index | sentence-transformers/all-MiniLM-L6-v2 | semantic similarity |
| Fusion | RRF (Reciprocal Rank Fusion) | combine sparse+dense scores |
| Store | local file index (`knowledge_index_intelligence.md`) | no external vector DB needed |
| Reranker | cross-encoder (ms-marco-MiniLM-L-6-v2) | top-10 rerank |

## Query Protocol

```
query(text: str, top_k: int = 10) -> list[RetrievedDoc]:
  1. bm25_results = bm25_index.search(text, top_k=20)
  2. dense_results = embedder.search(text, top_k=20)
  3. fused = rrf_fuse(bm25_results, dense_results, k=60)
  4. reranked = cross_encoder.rerank(fused[:20], top_k=top_k)
  5. return reranked
```

## Corpus Coverage

| Source | Format | Update Frequency |
|--------|--------|-----------------|
| `N01_intelligence/P01_knowledge/*.md` | knowledge_card | on every new KC |
| `N01_intelligence/compiled/*.yaml` | compiled artifacts | on every compile |
| `.cex/cache/*.json` | prompt cache | on session start |
| Research outputs in `.cex/runtime/` | session outputs | on session end |

## Retrieved Document Schema

| Field | Type | Description |
|-------|------|-------------|
| `doc_id` | string | artifact path (relative) |
| `title` | string | artifact title |
| `kind` | string | CEX kind |
| `content` | string | relevant excerpt |
| `bm25_score` | float | keyword relevance |
| `dense_score` | float | semantic similarity |
| `fused_rank` | int | final RRF rank |
| `rerank_score` | float | cross-encoder score |
| `last_updated` | ISO8601 | artifact modification date |

## Pre-Synthesis Check Protocol

Before any research task, N01 runs:

```
existing = retriever.query(task_goal, top_k=5)
if existing[0].rerank_score > 0.85:
    report("HIGH_OVERLAP: similar research found in corpus")
    decision = "extend" if existing is partial else "reuse"
else:
    proceed_with_new_research()
```

| Score | Action |
|-------|--------|
| > 0.85 | reuse or extend existing artifact |
| 0.60 - 0.85 | run targeted gaps, merge into existing |
| < 0.60 | full new research pipeline |

## Performance Targets

| Metric | Target | Alert |
|--------|--------|-------|
| Index build time (cold) | < 30s for 200 docs | > 60s |
| Query latency (warm) | < 500ms | > 2s |
| Recall@10 | > 0.80 | < 0.60 |
| Precision@5 | > 0.70 | < 0.50 |

## Comparison vs. Alternatives

| Approach | Precision | Speed | Corpus Type | N01 Fit |
|----------|-----------|-------|-------------|---------|
| BM25 only | high keyword | fast | large text | misses semantic |
| Dense only | high semantic | medium | embedding DB | misses exact terms |
| This (hybrid RRF) | best of both | medium | local files | optimal |
| Full vector DB (Pinecone) | high | fast | cloud required | overkill for N01 scale |

## Related Artifacts

| Artifact | Relationship |
|----------|-------------|
| `P10_memory/knowledge_index_n01.md` | index that this retriever queries |
| `P10_memory/embedding_config_intelligence.md` | embedding model config |
| `P04_tools/research_pipeline_n01.md` | calls this before synthesis |
| `P01_knowledge/*.md` | primary corpus being indexed |
