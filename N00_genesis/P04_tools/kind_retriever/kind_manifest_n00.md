---
id: n00_retriever_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Retriever -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, retriever, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A retriever performs vector, keyword, or hybrid search over a local knowledge store as the core component of RAG (Retrieval-Augmented Generation) pipelines. It takes a query, computes similarity against indexed embeddings, and returns ranked chunks with relevance scores. The output is the F3 INJECT layer's primary tool: the retriever finds the most relevant knowledge and injects it into the LLM context before generation.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `retriever` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| retrieval_method | string | yes | vector, keyword, hybrid, or rerank |
| index_path | string | yes | Path to the vector index or knowledge store |
| top_k | integer | yes | Number of results to return per query |
| score_threshold | float | no | Minimum relevance score to include in results |

## When to use
- When the F3 INJECT step needs to pull relevant context from the local knowledge library
- When building a RAG pipeline that requires dynamic knowledge injection based on query similarity
- When cex_retriever.py is the backing implementation and needs a typed configuration artifact

## Builder
`archetypes/builders/retriever-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind retriever --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ret_cex_tfidf_local
kind: retriever
pillar: P04
nucleus: n04
title: "CEX TF-IDF Local Retriever"
version: 1.0
quality: null
---
retrieval_method: hybrid
index_path: ".cex/index/knowledge_index.json"
top_k: 10
score_threshold: 0.4
```

## Related kinds
- `document_loader` (P04) -- loader that ingests documents before the retriever indexes them
- `embedding_config` (P01) -- embedding configuration that determines retriever similarity space
- `knowledge_index` (P10) -- the index artifact that the retriever queries
- `research_pipeline` (P04) -- pipeline that uses retriever in its RETRIEVE stage
