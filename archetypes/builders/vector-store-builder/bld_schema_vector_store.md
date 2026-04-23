---
kind: schema
id: bld_schema_vector_store
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for vector_store — SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Vector Store"
version: "1.0.0"
author: n03_builder
tags: [vector_store, builder, examples]
tldr: "Golden and anti-examples for vector store construction, demonstrating ideal structure and common pitfalls."
domain: "vector store construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_embedder_provider
  - bld_schema_model_provider
  - bld_schema_memory_scope
  - bld_schema_model_card
  - bld_schema_integration_guide
  - bld_schema_retriever
  - bld_schema_embedding_config
  - bld_schema_sandbox_spec
  - bld_schema_reranker_config
  - bld_schema_retriever_config
---

# Schema: vector_store
## Frontmatter Fields
| Field | Type | Required | Default | Source |
|-------|------|----------|---------|--------|
| id | string (p01_vdb_{backend}) | YES | — | CEX naming |
| kind | literal "vector_store" | YES | — | CEX |
| pillar | literal "P01" | YES | — | CEX |
| version | semver string | YES | "1.0.0" | CEX |
| created | date YYYY-MM-DD | YES | — | CEX |
| updated | date YYYY-MM-DD | YES | — | CEX |
| author | string | YES | — | CEX |
| backend | enum (see below) | YES | — | CEX |
| connection | object (see Connection) | YES | — | Backend docs |
| collection | string | YES | — | CEX convention |
| dimensions | integer > 0 | YES | — | Upstream embedder |
| distance_metric | enum (cosine/l2/dot_product/inner_product) | YES | cosine | Math |
| index_type | enum (hnsw/ivf/flat/ivf_pq/costm) | YES | hnsw | Backend docs |
| hnsw | object or null (see HNSW Params) | REC | null | Backend docs |
| max_vectors | integer or null | REC | null | Backend docs |
| metadata_filtering | boolean | REC | true | Backend docs |
| metadata_schema | object or null | REC | null | CEX convention |
| persistence | enum (auto/manual/external) | YES | — | Backend behavior |
| namespace_strategy | string | REC | — | CEX convention |
| cloud_region | string or null | REC | null | Cloud provider |
| pricing | object or null | REC | null | Cloud provider |
| domain | literal "vector_storage" | YES | — | CEX |
| quality | null | YES | null | CEX (never self-score) |
| tags | list[string], len >= 3 | YES | — | CEX |
| tldr | string < 160ch | YES | — | CEX |
| keywords | list[string] | REC | — | CEX |
| linked_artifacts | object | REC | — | CEX |
| data_source | URL string | YES | — | CEX |
## Backend Enum
Valid: pinecone, pgvector, chroma, faiss, qdrant, weaviate, milvus, other
## Connection Object
```yaml
connection:
  host: "localhost"         # or cloud endpoint
  port: 8000               # backend-specific default
  api_key_env: "PINECONE_API_KEY"  # env var name or null for local
  tls: true                # encryption in transit
  database: null            # pgvector: PostgreSQL database name
```
Rule: api_key_env is env var NAME, never the key itself. Null for local backends.
## HNSW Parameters
```yaml
hnsw:
  M: 16                    # max connections per node (4-64)
  ef_construction: 200     # build-time search width (100-500)
  ef_search: 100           # query-time search width (50-500)
```
Rule: higher M and ef = better recall, more memory, slower operations. Document tradeoff.
## Distance Metric Alignment
| Embedding Normalization | Correct Metric | Why |
|------------------------|----------------|-----|
| L2-normalized (unit vectors) | cosine | Cosine = 1 - dot_product for unit vectors |
| Raw (unnormalized) | l2 (euclidean) | Magnitude matters, cosine loses information |
| Raw + magnitude-aware | dot_product | Preserves magnitude as relevance signal |
## Body Structure (required sections)
1. `## Boundary` — vector_store IS / IS NOT
2. `## Backend Matrix` — table with Parameter + Value + Source columns
3. `## Index Configuration` — HNSW/IVF params with recall/speed tradeoffs
4. `## Namespace Strategy` — collection naming and domain isolation
5. `## Lifecycle Operations` — create, reindex, backup, restore
6. `## Anti-Patterns` — >= 4 common mistakes
7. `## References` — >= 1 official URL
## Constraints
- max_bytes: 4096 (body only, excl frontmatter)
- naming: p01_vdb_{backend}.yaml
- id == filename stem
- every Backend Matrix row MUST have Source URL (never `-`)
- dimensions MUST match upstream embedder_provider
- distance_metric MUST align with embedding normalization

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_embedder_provider]] | sibling | 0.61 |
| [[bld_schema_model_provider]] | sibling | 0.60 |
| [[bld_schema_memory_scope]] | sibling | 0.53 |
| [[bld_schema_model_card]] | sibling | 0.50 |
| [[bld_schema_integration_guide]] | sibling | 0.50 |
| [[bld_schema_retriever]] | sibling | 0.50 |
| [[bld_schema_embedding_config]] | sibling | 0.49 |
| [[bld_schema_sandbox_spec]] | sibling | 0.48 |
| [[bld_schema_reranker_config]] | sibling | 0.48 |
| [[bld_schema_retriever_config]] | sibling | 0.48 |
