---
kind: knowledge_card
id: bld_knowledge_card_vector_store
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for vector_store production — atomic searchable facts
sources: vector-store-builder SCHEMA + MANIFEST, backend docs, HNSW paper
quality: 9.1
title: "Knowledge Card Vector Store"
version: "1.0.0"
author: n03_builder
tags: [vector_store, builder, examples]
tldr: "Golden and anti-examples for vector store construction, demonstrating ideal structure and common pitfalls."
domain: "vector store construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_memory_vector_store
  - p03_sp_vector_store_builder
  - p03_ins_vector_store
  - bld_config_vector_store
  - p11_qg_vector_store
  - p01_kc_vector_store
  - bld_examples_vector_store
  - bld_schema_vector_store
  - vector-store-builder
  - bld_output_template_vector_store
---

# Domain Knowledge: vector_store
## Executive Summary
Vectordb backend configs are storage infrastructure artifacts for RAG pipelines — they encode the connection and indexing spec for a vector database. Each config captures backend type, connection details, collection name, dimension contract (matching upstream embedder), distance metric (aligned with normalization), index type and HNSW parameters, metadata filtering, persistence behavior, and namespace strategy. The dimension count is a hard contract from the embedder: mismatches corrupt similarity or crash index creation. These configs differ from embedder_provider (which produces vectors), model_provider (which routes LLM calls), and retriever (which orchestrates search queries).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge infrastructure) |
| Kind | `vector_store` (exact literal) |
| ID pattern | `p01_vdb_{backend}` |
| Required frontmatter | 22+ fields |
| Quality gates | 10 HARD + 12 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.85 |
| Quality field | always `null` |
| Domain field | always `vector_storage` |
| Index types | hnsw, ivf, flat, ivf_pq, costm |
| Distance metrics | cosine, l2, dot_product, inner_product |
| Backend enum | pinecone, pgvector, chroma, faiss, qdrant, weaviate, milvus, other |
## Patterns
| Pattern | Application |
|---------|-------------|
| Dimension contract | Exact integer from upstream embedder_provider; MUST match |
| Distance metric alignment | cosine for L2-normalized, l2 for raw, dot_product for magnitude-aware |
| Start local, scale cloud | FAISS/Chroma for dev -> Pinecone/Qdrant for production |
| HNSW defaults | M=16, ef_construction=200, ef_search=100 — safe for <1M vectors |
| Scale-based index selection | flat (<10K), HNSW (10K-1M), IVF-PQ (>1M, memory-constrained) |
| Collection per domain | cex_knowledge, cex_marketing — metadata filtering for cross-domain |
| Persistence explicitness | FAISS = manual save/load; Chroma = auto; Pinecone = cloud-managed |
| Reindex on model change | Switching embedder requires full reindex — no partial migration |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Dimensions != embedder output | Index creation fails or similarity scores become meaningless |
| cosine on unnormalized vectors | Magnitudes ignored, ranking distorted |
| FAISS without save_index | All vectors lost on process exit — in-memory only by default |
| HNSW for < 1K vectors | Overhead without benefit — flat search is faster and exact |
| Mixing embedding models in one collection | Different vector spaces produce garbage similarity |
| ef_search < 50 | Recall drops below 90% — queries miss relevant documents |
| No namespace strategy | Multi-domain data leaks between queries |
| No reindex plan | Schema or embedder change silently degrades recall without full rebuild |
## Application
1. Set `id: p01_vdb_{backend}` — must equal filename stem
2. Populate all required frontmatter fields; set `quality: null`
3. Set `dimensions` from upstream embedder_provider (exact match required)
4. Set `distance_metric` aligned with embedding normalization
5. Set `index_type` and HNSW params based on expected scale
6. Write `## Backend Matrix` with Value + Source URL per row
7. Write `## Index Configuration` with HNSW params and scale guidance
8. Write `## Lifecycle Operations` with create, reindex, backup, restore
9. Validate: body <= 4096 bytes, all configs sourced, 10 HARD + 12 SOFT gates
## References
- HNSW paper: Malkov & Yashunin, "Efficient and robust approximate nearest neighbor using Hierarchical Navigable Small World graphs" (2018)
- Pinecone: https://docs.pinecone.io/
- Chroma: https://docs.trychroma.com/
- FAISS: https://github.com/facebookresearch/faiss/wiki
- pgvector: https://github.com/pgvector/pgvector
- Qdrant: https://qdrant.tech/documentation/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_vector_store]] | downstream | 0.68 |
| [[p03_sp_vector_store_builder]] | downstream | 0.57 |
| [[p03_ins_vector_store]] | downstream | 0.57 |
| [[bld_config_vector_store]] | downstream | 0.52 |
| [[p11_qg_vector_store]] | downstream | 0.50 |
| [[p01_kc_vector_store]] | sibling | 0.49 |
| [[bld_examples_vector_store]] | downstream | 0.48 |
| [[bld_schema_vector_store]] | downstream | 0.43 |
| [[vector-store-builder]] | downstream | 0.40 |
| [[bld_output_template_vector_store]] | downstream | 0.39 |
