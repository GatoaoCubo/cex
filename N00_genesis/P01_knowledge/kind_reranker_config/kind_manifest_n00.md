---
id: n00_reranker_config_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Reranker Config -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, reranker_config, p01, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Reranker Config specifies the model and strategy for re-ranking retrieved documents before passing them to an LLM for generation. A reranker applies a cross-encoder or LLM-based scoring pass to improve precision of the top-k retrieved chunks. This config governs which reranker model to use, its scoring threshold, and how many candidates to rerank.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `reranker_config` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Config name and model |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| model | string | yes | Reranker model identifier |
| provider | enum | yes | cohere\|cross-encoder\|colbert\|llm |
| top_n | int | yes | Number of documents to return after reranking |
| candidate_pool | int | yes | Number of candidates retrieved before reranking |
| score_threshold | float | no | Minimum relevance score to include |

## When to use
- When vector search precision is insufficient for high-stakes queries
- When building a two-stage retrieval pipeline (recall + precision)
- When optimizing RAG quality without increasing LLM token cost

## Builder
`archetypes/builders/reranker_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind reranker_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- engineers optimizing retrieval precision
- `{{DOMAIN_CONTEXT}}` -- query type and retrieval quality requirements

## Example (minimal)
```yaml
---
id: reranker_config_cohere_v3
kind: reranker_config
pillar: P01
nucleus: n04
title: "Cohere Rerank v3"
version: 1.0
quality: null
---
model: rerank-english-v3.0
provider: cohere
top_n: 5
candidate_pool: 20
score_threshold: 0.4
```

## Related kinds
- `retriever_config` (P01) -- first-stage retrieval this reranker refines
- `embedding_config` (P01) -- embedding pipeline producing candidates
- `agentic_rag` (P01) -- agent pattern that uses reranking
