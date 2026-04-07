---
id: p04_document_loader_NAME
kind: document_loader
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
