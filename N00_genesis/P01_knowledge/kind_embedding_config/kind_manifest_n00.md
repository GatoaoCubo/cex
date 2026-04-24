---
id: n00_embedding_config_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Embedding Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, embedding_config, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_graph_rag_config
  - bld_schema_embedding_config
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_thinking_config
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Embedding Config specifies the full configuration for an embedding pipeline: provider selection, batch size, normalization, and caching behavior. It governs how raw text is transformed into vector representations for storage in a vector_store. One embedding_config ties together an embedder_provider with operational parameters for production use.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `embedding_config` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Config name and environment |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider_ref | string | yes | Reference to embedder_provider artifact |
| batch_size | int | yes | Number of texts embedded per API call |
| normalize | bool | yes | Whether to L2-normalize output vectors |
| cache_embeddings | bool | yes | Whether to cache computed embeddings |
| cache_ttl_hours | int | no | Cache time-to-live in hours |

## When to use
- When deploying a new RAG pipeline requiring consistent embedding behavior
- When changing embedding providers and needing a governed migration path
- When tuning batch size or caching for throughput optimization

## Builder
`archetypes/builders/embedding_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind embedding_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- ML engineers, RAG pipeline operators
- `{{DOMAIN_CONTEXT}}` -- production environment and scale requirements

## Example (minimal)
```yaml
---
id: embedding_config_prod_nomic
kind: embedding_config
pillar: P01
nucleus: n04
title: "Production Nomic Embedding Config"
version: 1.0
quality: null
---
provider_ref: embedder_provider_ollama_nomic
batch_size: 32
normalize: true
cache_embeddings: true
cache_ttl_hours: 24
```

## Related kinds
- `embedder_provider` (P01) -- the provider this config references
- `chunk_strategy` (P01) -- upstream chunking before embedding
- `vector_store` (P01) -- downstream storage of computed embeddings
- `retriever_config` (P01) -- uses same vectors for similarity search

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_dataset_card]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.42 |
| [[bld_schema_graph_rag_config]] | downstream | 0.42 |
| [[bld_schema_embedding_config]] | downstream | 0.42 |
| [[bld_schema_integration_guide]] | downstream | 0.41 |
| [[bld_schema_sandbox_spec]] | downstream | 0.40 |
| [[bld_schema_usage_report]] | downstream | 0.40 |
| [[bld_schema_search_strategy]] | downstream | 0.39 |
| [[bld_schema_thinking_config]] | downstream | 0.39 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.39 |
