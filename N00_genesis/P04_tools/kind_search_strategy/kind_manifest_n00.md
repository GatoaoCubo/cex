---
id: n00_search_strategy_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Search Strategy -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, search_strategy, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A search_strategy defines the inference-time compute allocation strategy for search operations, specifying how to balance recall vs. precision, when to use dense vs. sparse retrieval, and how to allocate query budget across multiple search passes. It governs the multi-pass search behavior in research_pipelines and RAG systems. The output is a reusable search protocol that optimizes retrieval quality within compute constraints.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `search_strategy` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| retrieval_mode | string | yes | dense, sparse, hybrid, or rerank |
| query_expansion | boolean | yes | Whether to expand query with synonyms or HyDE |
| max_passes | integer | yes | Maximum search iterations before returning results |
| precision_target | float | no | Target precision score (0.0-1.0) |

## When to use
- When configuring how a retriever or research_pipeline allocates its search budget
- When building a multi-pass RAG system that needs an explicit retrieval strategy
- When N01 Intelligence needs to optimize between broad recall and precise citation retrieval

## Builder
`archetypes/builders/search_strategy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind search_strategy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ss_hybrid_high_recall
kind: search_strategy
pillar: P04
nucleus: n01
title: "Hybrid High-Recall Search Strategy"
version: 1.0
quality: null
---
retrieval_mode: hybrid
query_expansion: true
max_passes: 3
precision_target: 0.8
```

## Related kinds
- `retriever` (P04) -- retriever that applies this search_strategy for its query logic
- `search_tool` (P04) -- web search tool that uses search_strategy for query formulation
- `research_pipeline` (P04) -- pipeline that configures search_strategy at the PLAN stage
- `chunk_strategy` (P01) -- chunking strategy that determines what the search_strategy retrieves
