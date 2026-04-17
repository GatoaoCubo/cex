---
id: n00_embedder_provider_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Embedder Provider -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, embedder_provider, p01, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Embedder Provider defines a text embedding service adapter for vector search pipelines. It specifies connection parameters, model identifiers, dimensionality, and pricing for a specific embedding provider (OpenAI, Cohere, Ollama, HuggingFace). Used by embedding_config to select and configure the correct provider at runtime.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `embedder_provider` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Provider name and model |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider | enum | yes | openai\|cohere\|ollama\|huggingface\|voyageai |
| model_id | string | yes | Embedding model identifier |
| dimensions | int | yes | Output vector dimensionality |
| max_tokens | int | yes | Maximum input token limit |
| cost_per_1k_tokens | float | no | USD cost per 1000 input tokens |
| local | bool | yes | Whether model runs locally |

## When to use
- When configuring a new embedding provider for a RAG pipeline
- When comparing providers for cost, quality, or latency trade-offs
- When switching embedding providers with minimal config change

## Builder
`archetypes/builders/embedder_provider-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind embedder_provider --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- engineers configuring retrieval infrastructure
- `{{DOMAIN_CONTEXT}}` -- deployment environment (cloud vs. local)

## Example (minimal)
```yaml
---
id: embedder_provider_ollama_nomic
kind: embedder_provider
pillar: P01
nucleus: n04
title: "Ollama nomic-embed-text"
version: 1.0
quality: null
---
provider: ollama
model_id: nomic-embed-text
dimensions: 768
max_tokens: 8192
local: true
cost_per_1k_tokens: 0.0
```

## Related kinds
- `embedding_config` (P01) -- applies this provider in a pipeline
- `vector_store` (P01) -- stores embeddings produced by this provider
- `model_provider` (P02) -- LLM provider (distinct from embedding provider)
