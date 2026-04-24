---
id: p04_document_loader_NAME
kind: document_loader
8f: F5_call
pillar: P04
version: 1.0.0
title: "Template — Document Loader"
tags: [template, document, loader, parser, extraction]
tldr: "Configures document ingestion: parsing format, text extraction, metadata extraction, and chunking handoff. Supports PDF, HTML, markdown, CSV, and DOCX."
quality: 9.0
domain: "tool integration"
density_score: 0.86
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
related:
  - p01_kc_document_loader
  - document_loader-builder
  - bld_knowledge_card_document_loader
  - bld_architecture_document_loader
  - bld_instruction_document_loader
  - bld_examples_document_loader
  - p04_loader_pdf
  - tpl_response_format
  - p11_qg_document_loader
  - p03_sp_document_loader_builder
---

# Document Loader: [NAME]

## Purpose
[WHAT documents and WHY — ingesting knowledge base, processing uploads, indexing corpus]

## Supported Formats

| Format | Parser | Metadata Extracted |
|--------|--------|--------------------|
| PDF | [pymupdf \| pdfplumber] | title, author, pages, creation_date |
| HTML | [beautifulsoup \| trafilatura] | title, headings, links, og_tags |
| Markdown | [markdown-it \| native] | frontmatter (YAML), headings |
| CSV/TSV | [pandas \| csv] | column names, row count |
| DOCX | [python-docx] | title, author, styles |

## Configuration
```yaml
format: [pdf | html | markdown | csv | docx | auto-detect]
encoding: [utf-8 | auto]
max_file_size_mb: [10 | 50 | 100]
extract_images: [true | false]
extract_tables: [true | false]
strip_headers_footers: [true | false]
```

## Processing Pipeline
```
File → Detect(format) → Parse(text + structure) → Extract(metadata) → Clean → Chunk
```
1. **Detect**: MIME type or extension-based format detection
2. **Parse**: Extract raw text preserving structure (headings, lists, tables)
3. **Extract**: Pull metadata from document properties + content
4. **Clean**: Remove boilerplate, normalize whitespace, fix encoding
5. **Chunk**: Hand off to chunk_strategy for splitting

## Output Schema
```yaml
document:
  source: "[file_path or URL]"
  format: "[detected_format]"
  text: "[extracted_text]"
  metadata:
    title: "[extracted]"
    pages: [N]
    word_count: [N]
  chunks: [] # Populated by chunk_strategy
```

## Error Handling
- **Corrupt file**: Log error, skip, continue with next
- **Encoding issues**: Try utf-8 → latin-1 → cp1252 → skip
- **Password-protected PDF**: Skip + flag for manual review
- **File too large**: Reject with clear error message

## Quality Gate
- [ ] At least 2 formats supported
- [ ] Max file size defined
- [ ] Error handling for corrupt/encoding/oversized files
- [ ] Output includes metadata (not just raw text)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_document_loader]] | upstream | 0.30 |
| [[document_loader-builder]] | related | 0.29 |
| [[bld_knowledge_card_document_loader]] | related | 0.29 |
| [[bld_architecture_document_loader]] | related | 0.29 |
| [[bld_instruction_document_loader]] | related | 0.27 |
| [[bld_examples_document_loader]] | related | 0.23 |
| [[p04_loader_pdf]] | sibling | 0.23 |
| [[tpl_response_format]] | downstream | 0.23 |
| [[p11_qg_document_loader]] | downstream | 0.21 |
| [[p03_sp_document_loader_builder]] | related | 0.21 |
