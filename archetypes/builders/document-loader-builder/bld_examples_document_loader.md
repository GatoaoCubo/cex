---
id: bld_examples_document_loader
kind: examples
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: GOVERN
quality: 9.1
tags: [examples, document_loader, ingestion, chunking, RAG, P04]
tldr: "Golden and anti-examples for document_loader artifacts with gate annotations."
density_score: 1.0
title: Examples ISO - document_loader
---
# Examples: document_loader-builder

## Golden Example
**INPUT**: "Create document loader for PDF ingestion with semantic chunking for legal document RAG"

**OUTPUT**:
```yaml
---
id: p04_loader_pdf_legal
kind: document_loader
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "PDF Legal Document Loader"
formats_supported:
  - application/pdf
chunk_strategy: semantic
output_format: langchain_doc
chunk_size: 512
overlap: 64
encoding: utf-8
quality: null
tags: [document_loader, pdf, legal, RAG, P04]
tldr: "Loads PDF legal documents, semanticslly chunks by topic boundary, preserves page/section metadata for citation."
metadata_fields: [source, page, section, author, created_date]
---

## Overview
Loads PDF files from legal corpora using pdfplumber for layout-aware text extraction.
Applies semantic chunking to split at topic boundaries rather than arbitrary character counts,
preserving citation fidelity. Stage 1 of legal RAG pipeline: feeds langchain_doc chunks to retriever.

## Formats
| Format | MIME Type | Parser | Limitations |
|--------|-----------|--------|-------------|
| PDF (text) | application/pdf | pdfplumber | Scanned PDFs need OCR pre-processing |

## Chunking
- Strategy: semantic (embedding-based topic boundary detection)
- Chunk size: 512 tokens
- Overlap: 64 tokens
- Boundary rule: never split mid-sentence; respect section headings as hard splits
- Splitter: LangChain SemanticChunker with text-embedding-3-small

## Metadata
| Field | Type | Source | Notes |
|-------|------|--------|-------|
| source | string | file path | Required provenance for every chunk |
| page | int | pdfplumber page index | 1-based page number |
| section | string | heading detection regex | Nearest preceding heading |
| author | string | PDF metadata dict | May be null for unsigned docs |
| created_date | string | PDF metadata dict | ISO 8601 if available |
```

**WHY THIS IS GOLDEN**:
- H01-H10: all HARD gates pass (valid YAML, correct id pattern, kind literal, quality null, all required fields, MIME types, valid enum values, body under 2048 bytes)
- Specific parser (pdfplumber) with limitation noted (scanned PDFs)
- Semantic strategy justified for legal domain
- overlap: 64 = 12.5% of 512 — within best-forctice range
- metadata includes source provenance + citation fields (page, section)
- output_format matches LangChain downstream
- Body: ~920 bytes — well under 2048 limit

---

## Anti-Example
**INPUT**: "Create document loader for files"

**BAD OUTPUT**:
```yaml
---
id: loader_files
kind: document_loader
version: 1.0
quality: 7.5
---

## Overview
Loads files and splits them into chunks.
```

**FAILURES**:
| Gate | Failure | Rule |
|---|---|---|
| H02 | id `loader_files` missing `p04_loader_` prefix | id must match `^p04_loader_[a-z][a-z0-9_]+$` |
| H05 | quality: 7.5 (self-scored) | quality must always be null |
| H06 | Missing formats_supported, chunk_strategy, output_format | All required fields must be present |
| H07 | formats_supported absent | Must be non-empty list of MIME types |
| H08 | chunk_strategy absent | Must be one of valid enum values |
| H09 | output_format absent | Must be one of valid enum values |
| SOFT | No format table, no chunking params, no metadata fields | Scores 0 on 6 of 11 soft dimensions |
