---
kind: architecture
id: bld_architecture_embedder_provider
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of embedder_provider — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Embedder Provider"
version: "1.0.0"
author: n03_builder
tags: [embedder_provider, builder, examples]
tldr: "Golden and anti-examples for embedder provider construction, demonstrating ideal structure and common pitfalls."
domain: "embedder provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_embedder_provider
  - bld_architecture_vector_store
  - p03_sp_embedder_provider_builder
  - embedder-provider-builder
  - p01_kc_embedder_provider
  - bld_architecture_model_provider
  - bld_collaboration_embedder_provider
  - p01_emb_openai_text_embedding_3_small
  - p11_qg_embedder_provider
  - bld_collaboration_embedding_config
---

# Architecture: embedder_provider in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 20+ field metadata header (id, kind, provider, model, dimensions, etc.) | embedder-provider-builder | active |
| provider_config | API endpoint, authentication, and rate limit settings | author | active |
| dimension_spec | Native dimensions, matryoshka support, reduction options | author | active |
| normalization_config | L2 normalization flag, distance metric recommendation | author | active |
| batch_config | Batch size limits, max tokens per request, truncation behavior | author | active |
| pricing_block | Cost per million tokens for embedding requests | author | active |
| benchmark_reference | MTEB scores for retrieval, clustering, classification tasks | author | active |
## Dependency Graph
```
provider_docs  --produces-->  embedder_provider  --consumed_by-->  vector_store
embedder_provider  --consumed_by-->  retriever     --referenced_by-> rag_pipeline
embedder_provider  --signals-->      dimension_contract
chunker_config     --constrains-->   embedder_provider (max_tokens)
```
| From | To | Type | Data |
|------|----|------|------|
| provider_docs (external) | embedder_provider | data_flow | official model specs, dimensions, pricing |
| embedder_provider | vector_store (P01) | consumes | dimension count for index creation |
| embedder_provider | retriever (P01) | data_flow | model ID and normalization for query embedding |
| embedder_provider | rag_pipeline | produces | configured embedding function for document ingestion |
| chunker_config (P01) | embedder_provider | dependency | chunk size must not exceed max_tokens |
| embedder_provider | cex_retriever.py | data_flow | embedding function for TF-IDF upgrade path |
## Boundary Table
| embedder_provider IS | embedder_provider IS NOT |
|----------------------|--------------------------|
| A connection spec for an embedding model API | A vector database configuration (vector_store P01) |
| Dimension and normalization contract for vectors | An LLM routing configuration (model_provider P02) |
| Batch size and rate limit constraints | A retrieval pipeline definition (retriever P01) |
| Provider-specific with API key environment variable | A chunking strategy (chunker_config P01) |
| Updated when provider releases new embedding models | A static document — must track model deprecations |
| Scoped to one embedding model from one provider | A comparison of multiple embedding models |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | provider_docs, MTEB benchmarks | Official documentation and benchmark results |
| Connection | provider_config, api_key_env | API endpoint and authentication |
| Contract | dimension_spec, normalization_config | Vector space agreement with downstream consumers |
| Limits | batch_config, max_tokens | Operational constraints for ingestion pipelines |
| Cost | pricing_block | Budget planning for embedding operations |
| Consumers | vector_store, retriever, rag_pipeline | Systems that embed documents and queries |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_embedder_provider]] | upstream | 0.53 |
| [[bld_architecture_vector_store]] | sibling | 0.51 |
| [[p03_sp_embedder_provider_builder]] | upstream | 0.44 |
| [[embedder-provider-builder]] | upstream | 0.44 |
| [[p01_kc_embedder_provider]] | upstream | 0.41 |
| [[bld_architecture_model_provider]] | sibling | 0.40 |
| [[bld_collaboration_embedder_provider]] | upstream | 0.40 |
| [[p01_emb_openai_text_embedding_3_small]] | upstream | 0.39 |
| [[p11_qg_embedder_provider]] | downstream | 0.37 |
| [[bld_collaboration_embedding_config]] | downstream | 0.34 |
