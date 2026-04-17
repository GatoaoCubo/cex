---
id: n00_chunk_strategy_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Chunk Strategy -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, chunk_strategy, p01, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Chunk Strategy defines how source documents are segmented into retrievable units for vector search and RAG pipelines. It specifies the splitting algorithm, chunk size, overlap, and metadata preservation rules. A well-defined chunk strategy directly determines retrieval precision and recall quality.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `chunk_strategy` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Human-readable strategy name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| method | enum | yes | fixed\|recursive\|semantic\|sentence\|token -- splitting algorithm |
| chunk_size | int | yes | Target chunk size in tokens or characters |
| chunk_overlap | int | yes | Overlap between consecutive chunks |
| preserve_metadata | bool | yes | Whether to carry source metadata into chunks |
| separator | string | no | Custom separator for fixed splitting |

## When to use
- When configuring a new RAG pipeline with a document corpus
- When retrieval quality is poor and re-chunking may improve recall
- When source documents have unique structure (code, tables, legal text)

## Builder
`archetypes/builders/chunk_strategy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind chunk_strategy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- engineers configuring the retrieval pipeline
- `{{DOMAIN_CONTEXT}}` -- document type and corpus characteristics

## Example (minimal)
```yaml
---
id: chunk_strategy_markdown_recursive
kind: chunk_strategy
pillar: P01
nucleus: n04
title: "Markdown Recursive Chunker"
version: 1.0
quality: null
---
method: recursive
chunk_size: 512
chunk_overlap: 64
preserve_metadata: true
separator: "\n\n"
```

## Related kinds
- `embedding_config` (P01) -- embedding model applied after chunking
- `retriever_config` (P01) -- uses chunk outputs for similarity search
- `rag_source` (P01) -- the source being chunked
- `vector_store` (P01) -- destination for chunked embeddings
