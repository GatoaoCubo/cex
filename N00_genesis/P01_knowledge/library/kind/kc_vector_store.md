---
id: p01_kc_vector_store
kind: knowledge_card
type: kind
pillar: P01
title: "VectorDB Backend -- Deep Knowledge for vector_store"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: vector_store
quality: 9.1
tags: [vector_store, p01, INJECT, kind-kc, knowledge, rag, vector]
tldr: "Configuration for vector database storage -- where embeddings live and how similarity search is performed"
when_to_use: "Choosing and configuring a vector store for semantic retrieval in CEX knowledge pipelines"
keywords: [vectordb, vector, database, pgvector, chroma, qdrant, faiss, similarity]
feeds_kinds: [vector_store]
density_score: null
related:
  - bld_memory_vector_store
  - bld_knowledge_card_vector_store
  - p03_ins_vector_store
  - p03_sp_vector_store_builder
  - vector-store-builder
  - bld_collaboration_vector_store
  - bld_config_vector_store
  - bld_examples_vector_store
  - bld_output_template_vector_store
  - p11_qg_vector_store
---

# VectorDB Backend

## Spec
```yaml
kind: vector_store
pillar: P01
llm_function: INJECT
max_bytes: 3072
naming: p01_vdb_{{backend}}.yaml
core: false
```

## Purpose

A vectordb backend config tells CEX where to store and query embedding vectors. This is the persistence layer for semantic search -- it takes vectors from the embedder provider and enables fast approximate nearest neighbor (ANN) lookup.

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| backend | Database technology | `pgvector`, `chroma`, `qdrant`, `faiss`, `sqlite-vss` |
| connection | Connection config | `postgresql://...` or `./data/chroma/` |
| collection | Namespace for vectors | `cex_knowledge` |
| dimensions | Expected vector dimensions | `1536` |
| distance_metric | Similarity function | `cosine`, `l2`, `inner_product` |
| index_type | ANN index algorithm | `hnsw`, `ivfflat`, `flat` |
| ef_construction | HNSW build parameter | `128` |
| ef_search | HNSW query parameter | `64` |

## Key Patterns

1. **Start local**: FAISS or Chroma for development (zero server), pgvector for production
2. **Namespace per domain**: Separate collections for KCs, memories, artifacts, and user content
3. **Hybrid search**: Combine vector similarity with metadata filters (pillar, kind, date)
4. **Reindex on schema change**: When embedding model changes, full reindex required

## Anti-Patterns

- Mixing vector dimensions in one collection (instant crash)
- No metadata filtering (semantic-only search returns false positives)
- FAISS without save/load (vectors lost on restart)
- Over-indexing: embedding every file including configs and logs

## CEX Integration

- `cex_retriever.py` currently uses TF-IDF (2184 docs, 12K vocab) -- vectordb is the upgrade path
- `cex_sdk/vectordb/` provides pluggable backend abstraction
- `cex_kc_index.py` maintains the knowledge card index (future: vector-backed)
- Embedder provider config feeds the vector dimensions for this backend

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_vector_store]] | downstream | 0.53 |
| [[bld_knowledge_card_vector_store]] | sibling | 0.52 |
| [[p03_ins_vector_store]] | downstream | 0.51 |
| [[p03_sp_vector_store_builder]] | downstream | 0.47 |
| [[vector-store-builder]] | downstream | 0.44 |
| [[bld_collaboration_vector_store]] | downstream | 0.44 |
| [[bld_config_vector_store]] | downstream | 0.43 |
| [[bld_examples_vector_store]] | downstream | 0.43 |
| [[bld_output_template_vector_store]] | downstream | 0.42 |
| [[p11_qg_vector_store]] | downstream | 0.39 |
