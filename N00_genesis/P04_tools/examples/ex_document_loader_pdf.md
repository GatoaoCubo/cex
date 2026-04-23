---
id: p04_loader_pdf
kind: document_loader
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "PDF Document Loader"
formats_supported:
  - application/pdf
chunk_strategy: recursive
output_format: langchain_doc
chunk_size: 512
overlap: 50
encoding: utf-8
quality: 9.1
tags: [document_loader, pdf, RAG, chunking, P04]
tldr: "PDF loader with recursive chunking at 512 tokens for RAG pipelines using PyMuPDF parser"
description: "Ingests PDF files, extracts text with layout awareness, and produces chunked Documents"
metadata_fields:
  - source
  - page_number
  - total_pages
domain: "tool integration"
title: "Document Loader Pdf"
density_score: 0.93
related:
  - bld_examples_document_loader
  - document_loader-builder
  - p01_kc_document_loader
  - bld_output_template_document_loader
  - p03_sp_document_loader_builder
  - bld_architecture_document_loader
  - bld_knowledge_card_document_loader
  - p04_comp_text_splitter
  - p04_document_loader_NAME
  - bld_instruction_document_loader
---

# PDF Document Loader

## Overview
Ingests PDF files and converts them into chunked LangChain Documents for RAG indexing. Handles single and multi-page PDFs with layout-aware text extraction. Stage 1 of the RAG pipeline: raw file to chunked Documents.

## Formats
| Format | MIME Type | Parser | Limitations |
|--------|-----------|--------|-------------|
| PDF | application/pdf | PyMuPDF (fitz) | Scanned PDFs need OCR fallback |

## Chunking
- Strategy: recursive (RecursiveCharacterTextSplitter)
- Chunk size: 512 tokens
- Overlap: 50 tokens
- Boundary rule: never split mid-sentence; falls back to paragraph then newline
- Splitter: LangChain RecursiveCharacterTextSplitter

## Metadata
| Field | Type | Source | Notes |
|-------|------|--------|-------|
| source | string | file path or URL | Required — provenance for every chunk |
| page_number | int | PDF page index | 1-based page number |
| total_pages | int | PDF metadata | Total document pages |

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `document loader`
- **Artifact ID**: `p04_loader_pdf`
- **Tags**: [document_loader, pdf, RAG, chunking, P04]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `document loader` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: document_loader
pillar: P04
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_document_loader]] | related | 0.49 |
| [[document_loader-builder]] | related | 0.40 |
| [[p01_kc_document_loader]] | upstream | 0.38 |
| [[bld_output_template_document_loader]] | related | 0.38 |
| [[p03_sp_document_loader_builder]] | related | 0.37 |
| [[bld_architecture_document_loader]] | related | 0.30 |
| [[bld_knowledge_card_document_loader]] | related | 0.29 |
| [[p04_comp_text_splitter]] | related | 0.28 |
| [[p04_document_loader_NAME]] | sibling | 0.27 |
| [[bld_instruction_document_loader]] | related | 0.27 |
