---
id: p10_bi_bm25_knowledge
kind: knowledge_index
8f: F3_inject
pillar: P10
title: "BM25 Knowledge Index — Sparse Retrieval Baseline"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-retrieval
quality: 9.1
tags: [knowledge-index, bm25, sparse-retrieval, tf-idf, baseline]
tldr: "BM25 sparse index over 2184 CEX artifacts — term frequency baseline for retrieval, benchmarking against future dense indexes."
density_score: 0.92
related:
  - p01_gl_rag
  - bld_collaboration_knowledge_index
  - n04_rag_pipeline_memory
  - p03_sp_knowledge_index_builder
  - knowledge-index-builder
  - p01_kc_knowledge_index
  - p10_lr_knowledge-index-builder
  - p06_arch_rag_pipeline
  - bld_examples_knowledge_index
  - bld_knowledge_card_knowledge_index
---

# BM25 Knowledge Index

## Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Algorithm | BM25 (Okapi) | Industry-standard sparse retrieval |
| k1 | 1.5 | Default term saturation — balanced for mixed doc lengths |
| b | 0.75 | Default length normalization — penalizes very long docs |
| Corpus size | 2,184 artifacts | All `.md` with valid frontmatter |
| Vocabulary | ~12,000 terms | After stop-word removal + lowercasing |
| Tokenizer | Whitespace + punctuation split | Simple, language-agnostic |
| Stop words | English standard (NLTK) + CEX-specific (`---`, `yaml`, `md`) | Reduce noise |

## Index Scope

| Source | Artifact Count | Content |
|--------|------:|---------|
| `P01_knowledge/library/kind/` | 123 | Kind KCs — backbone |
| `N{01-07}_*/` (all subdirs) | ~400 | Nucleus artifacts — agents, prompts, schemas |
| `archetypes/builders/` | 1,625 | Builder ISOs (13 × 125) |
| `_docs/specs/` | ~30 | Specification documents |
| `compiled/*.yaml` | N/A | Excluded — redundant with source `.md` |

## CEX Implementation

The current implementation lives in `cex_retriever.py`:
- Builds TF-IDF matrix (scikit-learn `TfidfVectorizer`)
- Stores sparse matrix in memory (no persistence yet)
- Query: vectorize → cosine similarity → top-K
- Rebuild: triggered manually via `--rebuild` flag

## Performance Baseline

| Metric | Value | Context |
|--------|-------|---------|
| Index build time | ~3s | 2184 docs, 12K vocab, single-threaded |
| Query latency | <50ms | Top-10 retrieval |
| Memory footprint | ~15MB | Sparse matrix in RAM |
| Recall@5 (estimated) | ~0.65 | Keyword-heavy queries only |
| Recall@10 (estimated) | ~0.78 | Broader net catches more |

## Planned Upgrades

| Upgrade | Kind | Impact |
|---------|------|--------|
| Persistent index (pickle) | `knowledge_index` | Skip rebuild on restart |
| Dense counterpart (pgvector) | `vector_store` | Semantic retrieval |
| Hybrid fusion (RRF) | `retriever_config` | Best of sparse + dense |
| Incremental updates | Tool enhancement | No full rebuild on single KC add |

## Related

- `cex_retriever.py` — current TF-IDF implementation
- `rag_pipeline_architecture.md` — end-to-end pipeline context
- `p01_gl_rag.md` — RAG glossary entry

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_gl_rag]] | upstream | 0.32 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.29 |
| [[n04_rag_pipeline_memory]] | related | 0.29 |
| [[p03_sp_knowledge_index_builder]] | upstream | 0.28 |
| [[knowledge-index-builder]] | related | 0.27 |
| [[p01_kc_knowledge_index]] | related | 0.27 |
| [[p10_lr_knowledge-index-builder]] | related | 0.26 |
| [[p06_arch_rag_pipeline]] | upstream | 0.26 |
| [[bld_examples_knowledge_index]] | upstream | 0.25 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.25 |
