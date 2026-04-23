---
kind: config
id: bld_config_retriever
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [config, retriever, P06, naming, constraints, RAG]
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
title: Config ISO - retriever
related:
  - p09_kc_retriever_domain
  - bld_instruction_retriever
  - p03_sp_retriever_builder
  - bld_output_template_retriever
  - retriever-builder
  - bld_schema_retriever
  - bld_examples_retriever
  - bld_collaboration_retriever
  - bld_architecture_retriever
  - bld_config_vector_store
---
# Config: retriever Production Rules

## Naming Convention

| Rule | Pattern | Examples |
|------|---------|---------|
| File name | `p04_retr_{store_slug}.md` | `p04_retr_chroma.md`, `p04_retr_pinecone_hybrid.md` |
| id field | `p04_retr_{store_slug}` | Must equal filename stem exactly |
| store_slug | snake_case, lowercase, no hyphens | `faiss_local`, `qdrant_sparse`, `weaviate_bm25` |
| Disambiguation | append use case slug if multiple retrievers use same store | `p04_retr_chroma_docs`, `p04_retr_chroma_code` |

## File Paths

| Asset | Path |
|-------|------|
| Artifact output | `records/pool/p04_retr_{store_slug}.md` |
| Builder files | `archetypes/builders/retriever-builder/bld_*.md` |
| Schema | `archetypes/builders/retriever-builder/bld_schema_retriever.md` |
| Template | `archetypes/builders/retriever-builder/bld_output_template_retriever.md` |
| Quality gate | `archetypes/builders/retriever-builder/bld_quality_gate_retriever.md` |

## Size Limits

| Metric | Limit | Enforcement |
|--------|-------|-------------|
| Body bytes (sections only) | <= 2048 | HARD gate H10 |
| Frontmatter | not counted in 2048 | excluded |
| density_score | >= 0.80 | SOFT gate S10 |
| tldr length | <= 160 characters | schema constraint |
| description length | <= 200 characters | schema constraint |

## store_type Enum

| Value | Backend | Hosting |
|-------|---------|---------|
| chroma | ChromaDB | local (in-memory or persistent) / Chroma Cloud |
| pinecone | Pinecone | managed cloud (serverless or pod) |
| faiss | FAISS | local CPU/GPU (no built-in persistence) |
| qdrant | Qdrant | local Docker / Qdrant Cloud |
| weaviate | Weaviate | local Docker / Weaviate Cloud |
| milvus | Milvus / Zilliz | local Docker / Zilliz Cloud |
| elasticsearch | Elasticsearch | local / Elastic Cloud (kNN + BM25) |
| costm | other or proprietary | document explicitly |

## similarity_metric Enum

| Value | Use When |
|-------|----------|
| cosine | Default for text; embeddings not guaranteed normalized |
| dot_product | Embeddings natively normalized (Cohere embed-v3, some ST models) |
| euclidean | Image / spatial embeddings; NOT recommended for high-dim text |
| manhattan | Sparse embeddings only |

## search_type Enum

| Value | Strategy | Best For |
|-------|----------|----------|
| vector | Dense ANN only | Semantic queries, concept search |
| keyword | BM25/TF-IDF only | Exact term match, code search |
| hybrid | Vector + keyword fusion | Most production RAG (recommended default) |

## top_k Guidelines

| Scenario | Recommended top_k |
|----------|------------------|
| No reranking, direct to LLM | 3-10 |
| With reranking (first pass) | 20-50 |
| Evaluation / BEIR benchmarking | 100 |
| Minimum acceptable | 1 (only for strict precision tasks) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_kc_retriever_domain]] | downstream | 0.42 |
| [[bld_instruction_retriever]] | upstream | 0.38 |
| [[p03_sp_retriever_builder]] | upstream | 0.37 |
| [[bld_output_template_retriever]] | upstream | 0.36 |
| [[retriever-builder]] | upstream | 0.34 |
| [[bld_schema_retriever]] | related | 0.34 |
| [[bld_examples_retriever]] | downstream | 0.32 |
| [[bld_collaboration_retriever]] | downstream | 0.30 |
| [[bld_architecture_retriever]] | downstream | 0.29 |
| [[bld_config_vector_store]] | sibling | 0.28 |
