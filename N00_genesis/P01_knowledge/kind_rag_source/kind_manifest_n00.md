---
id: n00_rag_source_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "RAG Source -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, rag_source, p01, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
RAG Source defines an external indexable source for retrieval augmented generation pipelines. It specifies the source location, format, access credentials pattern, refresh frequency, and pre-processing requirements. Each RAG source is ingested, chunked, and embedded according to its associated chunk_strategy and embedding_config.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `rag_source` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Source name and type |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| source_type | enum | yes | file\|url\|api\|database\|confluence\|notion |
| location | string | yes | Path, URL, or connection string pattern |
| format | enum | yes | pdf\|markdown\|html\|json\|csv\|docx |
| refresh_frequency | enum | yes | never\|daily\|weekly\|on_change |
| chunk_strategy_ref | string | yes | Reference to chunk_strategy artifact |
| auth_required | bool | yes | Whether access requires credentials |

## When to use
- When onboarding a new data source into a RAG pipeline
- When configuring knowledge ingestion from external systems
- When defining the corpus for a nucleus's retrieval context

## Builder
`archetypes/builders/rag_source-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind rag_source --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- engineers building RAG pipelines
- `{{DOMAIN_CONTEXT}}` -- knowledge domain of the source

## Example (minimal)
```yaml
---
id: rag_source_cex_repo_markdown
kind: rag_source
pillar: P01
nucleus: n04
title: "CEX Repo Markdown Files"
version: 1.0
quality: null
---
source_type: file
location: "C:/Users/CEX/Documents/GitHub/cex/**/*.md"
format: markdown
refresh_frequency: on_change
chunk_strategy_ref: chunk_strategy_markdown_recursive
auth_required: false
```

## Related kinds
- `chunk_strategy` (P01) -- how this source is segmented
- `embedding_config` (P01) -- how chunks are embedded
- `vector_store` (P01) -- where embeddings are stored
- `retriever_config` (P01) -- how this source is queried
