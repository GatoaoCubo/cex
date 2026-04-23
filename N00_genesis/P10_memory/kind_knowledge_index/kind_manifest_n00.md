---
id: n00_knowledge_index_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Knowledge Index -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, knowledge_index, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_knowledge_index
  - knowledge-index-builder
  - bld_schema_reranker_config
  - bld_schema_graph_rag_config
  - bld_collaboration_knowledge_index
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_thinking_config
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A knowledge_index configures the search index (BM25, FAISS, or hybrid) over the CEX knowledge corpus, enabling fast retrieval of relevant artifacts during F3 INJECT. It defines the index type, embedding model, corpus scope, and retrieval parameters that make knowledge searchable at inference time.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `knowledge_index` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| index_type | enum | yes | bm25 \| faiss \| hybrid |
| embedding_model | string | no | Model ID for dense embeddings (FAISS/hybrid only) |
| corpus_paths | array | yes | Glob patterns identifying documents to index |
| top_k | integer | yes | Default number of results to return |
| refresh_schedule | string | no | Cron expression for index rebuild |
| vocab_size | integer | no | BM25 vocabulary size (default 12000) |

## When to use
- When bootstrapping the CEX retriever (`cex_retriever.py`) for a new corpus
- When expanding the indexed corpus to include new pillars or nuclei
- When tuning retrieval quality (precision vs. recall tradeoffs)

## Builder
`archetypes/builders/knowledge_index-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind knowledge_index --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ki_cex_main_corpus
kind: knowledge_index
pillar: P10
nucleus: n04
title: "Example Knowledge Index"
version: 1.0
quality: null
---
# CEX Main Corpus Index
index_type: hybrid
corpus_paths: ["P01_knowledge/**/*.md", "archetypes/**/*.md"]
top_k: 10
vocab_size: 12000
```

## Related kinds
- `embedding_config` (P01) -- defines the embedding model parameters used by FAISS
- `rag_source` (P01) -- documents that feed into this index
- `chunk_strategy` (P01) -- chunking rules applied before indexing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_knowledge_index]] | upstream | 0.51 |
| [[knowledge-index-builder]] | related | 0.46 |
| [[bld_schema_reranker_config]] | upstream | 0.43 |
| [[bld_schema_graph_rag_config]] | upstream | 0.42 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.41 |
| [[bld_schema_dataset_card]] | upstream | 0.41 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.40 |
| [[bld_schema_usage_report]] | upstream | 0.40 |
| [[bld_schema_integration_guide]] | upstream | 0.40 |
| [[bld_schema_thinking_config]] | upstream | 0.40 |
