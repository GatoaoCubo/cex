---
id: n00_document_loader_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Document Loader -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, document_loader, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A document_loader ingests files in various formats (PDF, HTML, CSV, DOCX, Markdown) and converts them into structured text chunks suitable for embedding or direct LLM consumption. It handles format detection, encoding normalization, table extraction, and metadata preservation. The output is a parsed document with chunk boundaries, source metadata, and clean text ready for the F3 INJECT step of the 8F pipeline.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `document_loader` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| supported_formats | list | yes | File types: pdf, html, csv, docx, md, txt, xlsx |
| chunking_strategy | string | yes | fixed_size, semantic, paragraph, or page |
| chunk_size_tokens | integer | yes | Target chunk size in tokens |
| metadata_fields | list | no | Preserved metadata: source_url, page_number, section |

## When to use
- When ingesting external documents into a RAG pipeline as knowledge sources
- When N04 Knowledge needs to process uploaded files before indexing
- When the research_pipeline RETRIEVE stage pulls documents from local or remote storage

## Builder
`archetypes/builders/document_loader-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind document_loader --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: dl_pdf_semantic_chunker
kind: document_loader
pillar: P04
nucleus: n04
title: "PDF Semantic Chunker"
version: 1.0
quality: null
---
supported_formats: [pdf, html, md]
chunking_strategy: semantic
chunk_size_tokens: 512
metadata_fields: [source_path, page_number, section_title]
```

## Related kinds
- `retriever` (P04) -- vector retriever that indexes document_loader output
- `chunk_strategy` (P01) -- knowledge card defining chunking methodology
- `embedding_config` (P01) -- embedding configuration applied to loaded document chunks
- `research_pipeline` (P04) -- pipeline that uses document_loader in its RETRIEVE stage
