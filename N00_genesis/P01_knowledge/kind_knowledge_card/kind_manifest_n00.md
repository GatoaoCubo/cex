---
id: n00_knowledge_card_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Knowledge Card -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, knowledge_card, p01, n00, archetype, template]
density_score: 1.0
related:
  - p06_is_knowledge_data_model
  - bld_collaboration_knowledge_card
  - bld_schema_reranker_config
  - bld_schema_dataset_card
  - p01_kc_qa_validation
  - bld_schema_search_strategy
  - bld_schema_integration_guide
  - bld_schema_action_paradigm
  - knowledge-card-builder
  - bld_schema_graph_rag_config
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Knowledge Card is the atomic, searchable fact unit of the CEX knowledge system. Each card captures one precise, dense piece of domain knowledge with density >= 0.85 (information per token). It is the most common artifact in CEX -- injected via F3 INJECT to ground every nucleus in verified domain knowledge before generation.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier (kc_{topic}) |
| kind | string | yes | Always `knowledge_card` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Human-readable topic name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| domain | string | yes | Knowledge domain (e.g., AI, pricing, ops) |
| density | float | yes | Information density score (target >= 0.85) |
| sources | list | no | Citation references supporting claims |
| tags | list | yes | Topic tags for retrieval |

## When to use
- When documenting a discovered fact, pattern, or domain insight
- When grounding a nucleus with verified knowledge before generation
- When building the searchable knowledge library (P01_knowledge/library/)

## Builder
`archetypes/builders/knowledge_card-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind knowledge_card --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04 most common)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- all nuclei via F3 INJECT
- `{{DOMAIN_CONTEXT}}` -- specific knowledge domain

## Example (minimal)
```yaml
---
id: kc_vector_search_fundamentals
kind: knowledge_card
pillar: P01
nucleus: n04
title: "Vector Search Fundamentals"
version: 1.0
quality: null
domain: AI / information retrieval
density: 0.88
tags: [vector-search, embeddings, ANN, RAG]
---
Vector search finds semantically similar documents by comparing dense vector
representations. Approximate Nearest Neighbor (ANN) algorithms (HNSW, IVF)
enable sub-linear search over billions of vectors. Key trade-off: recall vs.
latency controlled by ef_search (HNSW) or nprobe (IVF).
```

## Related kinds
- `citation` (P01) -- sources cited in knowledge cards
- `glossary_entry` (P01) -- term definitions within knowledge cards
- `context_doc` (P01) -- broader context built from multiple knowledge cards
- `few_shot_example` (P01) -- demonstrations that reference knowledge cards

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_is_knowledge_data_model]] | downstream | 0.37 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.36 |
| [[bld_schema_reranker_config]] | downstream | 0.35 |
| [[bld_schema_dataset_card]] | downstream | 0.34 |
| [[p01_kc_qa_validation]] | sibling | 0.34 |
| [[bld_schema_search_strategy]] | downstream | 0.34 |
| [[bld_schema_integration_guide]] | downstream | 0.33 |
| [[bld_schema_action_paradigm]] | downstream | 0.33 |
| [[knowledge-card-builder]] | downstream | 0.33 |
| [[bld_schema_graph_rag_config]] | downstream | 0.33 |
