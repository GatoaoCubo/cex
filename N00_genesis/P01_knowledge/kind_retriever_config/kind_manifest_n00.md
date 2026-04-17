---
id: n00_retriever_config_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Retriever Config -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, retriever_config, p01, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Retriever Config specifies the full retrieval configuration for a RAG pipeline: similarity metric, top-k results, hybrid search weights (dense + sparse), and reranker reference. It constrains how the retrieval layer selects candidates from a vector_store before passing them to an LLM. One retriever_config ties together vector search parameters with optional BM25 sparse retrieval.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `retriever_config` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Config name and retrieval strategy |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| vector_store_ref | string | yes | Reference to vector_store artifact |
| top_k | int | yes | Number of documents to retrieve |
| similarity_metric | enum | yes | cosine\|dot_product\|euclidean |
| hybrid | bool | yes | Whether to combine dense + sparse search |
| alpha | float | no | Dense weight in hybrid (0-1); 1=pure dense |
| reranker_ref | string | no | Optional reranker_config reference |

## When to use
- When configuring the retrieval layer of a new RAG pipeline
- When tuning recall/precision trade-offs for a specific use case
- When migrating from single-stage to hybrid or two-stage retrieval

## Builder
`archetypes/builders/retriever_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind retriever_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- engineers building or tuning RAG pipelines
- `{{DOMAIN_CONTEXT}}` -- query characteristics and corpus size

## Example (minimal)
```yaml
---
id: retriever_config_cex_hybrid
kind: retriever_config
pillar: P01
nucleus: n04
title: "CEX Hybrid Retriever"
version: 1.0
quality: null
---
vector_store_ref: vector_store_cex_chroma
top_k: 10
similarity_metric: cosine
hybrid: true
alpha: 0.7
reranker_ref: reranker_config_cohere_v3
```

## Related kinds
- `vector_store` (P01) -- backend being queried
- `reranker_config` (P01) -- optional precision refinement stage
- `embedding_config` (P01) -- must match embedding used at index time
- `agentic_rag` (P01) -- agent pattern built on this retriever
