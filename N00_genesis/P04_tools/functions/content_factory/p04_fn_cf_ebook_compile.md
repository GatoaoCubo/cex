---
id: p04_fn_cf_ebook_compile
kind: function_def
8f: F6_produce
pillar: P04
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: compile_ebook
description: "Compile an ebook from Markdown chapters using Pandoc. Call when the Content Factory has generated all chapter files and needs them merged into a single EPUB or PDF with cover, TOC, and metadata."
parameters:
  type: object
  properties:
    chapters:
      type: array
      items:
        type: string
      description: "Ordered list of chapter file paths (.md). Compiled in order."
    output_path:
      type: string
      description: "Destination path for the compiled ebook"
    format:
      type: string
      description: "Output ebook format"
      enum: [epub, pdf, html]
    metadata:
      type: object
      description: "Book metadata"
      properties:
        title:
          type: string
        subtitle:
          type: string
        author:
          type: string
        publisher:
          type: string
        language:
          type: string
        date:
          type: string
        rights:
          type: string
      required: [title, author]
    cover_image:
      type: string
      description: "Path to cover image file (JPG or PNG)"
    stylesheet:
      type: string
      description: "Path to CSS stylesheet for EPUB/HTML styling"
    toc:
      type: boolean
      description: "Generate table of contents"
    toc_depth:
      type: integer
      description: "TOC heading depth (1-3)"
  required: [chapters, output_path, format, metadata]
returns:
  type: object
  description: "Ebook compilation result"
  properties:
    output_path:
      type: string
      description: "Path to the compiled ebook"
    page_count:
      type: integer
      description: "Estimated page count (PDF only)"
    chapter_count:
      type: integer
      description: "Number of chapters compiled"
    file_size_bytes:
      type: integer
      description: "Output file size"
    word_count:
      type: integer
      description: "Total word count across all chapters"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content_factory
quality: 9.0
tags: [function_def, pandoc, ebook, epub, pdf, compile, content_factory]
tldr: "LLM-callable function to compile Markdown chapters into EPUB/PDF ebook via Pandoc"
examples:
  - input: {"chapters": ["ch01.md", "ch02.md", "ch03.md"], "output_path": "output/book.epub", "format": "epub", "metadata": {"title": "RAG Guide", "author": "DataCraft"}, "cover_image": "covers/rag_cover.jpg", "toc": true}
    output: {"output_path": "output/book.epub", "chapter_count": 3, "file_size_bytes": 524288, "word_count": 15000}
error_types: [chapter_not_found, pandoc_not_installed, invalid_metadata, cover_not_found, compilation_error]
density_score: 0.99
related:
  - p01_kc_pandoc_pipeline
  - p04_fn_cf_pdf_generate
  - bld_schema_validation_schema
  - bld_schema_integration_guide
  - bld_schema_research_pipeline
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_input_schema
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
---

# eBook Compiler Function (Pandoc)

## Overview
Compiles multiple Markdown chapter files into a single ebook using Pandoc. The LLM calls this as the final step in the Content Factory ebook pipeline — after all chapters have been generated via `p03_pt_cf_ebook_chapter`. Handles cover art, table of contents, metadata, and styling.

## Parameters

### chapters
Type: array of strings | Required: yes
Ordered list of chapter file paths. Each must be a valid Markdown file. Compiled in array order.

### output_path
Type: string | Required: yes
Destination for the compiled ebook.

### format
Type: string (enum) | Required: yes
- `epub`: Standard ebook format — Kindle, Apple Books, Kobo
- `pdf`: Print-ready via LaTeX backend — handouts, physical printing
- `html`: Single-page web version — online reading

### metadata
Type: object | Required: yes
Book metadata. `title` and `author` required. Embedded in EPUB metadata and PDF title page.

### cover_image
Type: string | Required: no
Path to cover image (JPG or PNG). Recommended 1600x2400px for EPUB stores.

### stylesheet
Type: string | Required: no
CSS file for EPUB/HTML styling. Controls typography, margins, colors.

### toc / toc_depth
Type: boolean / integer | Required: no | Default: true / 2
Table of contents generation. Depth 1 = chapter titles only, 2 = + sections, 3 = + subsections.

## Returns
Type: object with `output_path`, `page_count`, `chapter_count`, `file_size_bytes`, `word_count`.

## CLI Command (generated)
```bash
pandoc ch01.md ch02.md ch03.md \
  --metadata title="RAG Guide" --metadata author="DataCraft" \
  --epub-cover-image=covers/rag_cover.jpg \
  --css=styles/ebook.css \
  --toc --toc-depth=2 \
  -o output/book.epub
```

## Examples

### Example 1: Full EPUB with cover and styling
```json
{
  "chapters": ["chapters/ch01_intro.md", "chapters/ch02_embeddings.md", "chapters/ch03_retrieval.md", "chapters/ch04_vectors.md", "chapters/ch05_production.md"],
  "output_path": "output/rag_guide.epub",
  "format": "epub",
  "metadata": {"title": "Building RAG Systems", "subtitle": "A Practical Guide", "author": "DataCraft", "language": "en-US", "date": "2026"},
  "cover_image": "covers/rag_cover.jpg",
  "stylesheet": "styles/ebook.css",
  "toc": true,
  "toc_depth": 2
}
```

### Example 2: PDF for print
```json
{
  "chapters": ["chapters/ch01.md", "chapters/ch02.md"],
  "output_path": "output/preview.pdf",
  "format": "pdf",
  "metadata": {"title": "Preview Chapters", "author": "DataCraft"},
  "toc": false
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_pandoc_pipeline]] | upstream | 0.42 |
| [[p04_fn_cf_pdf_generate]] | sibling | 0.37 |
| [[bld_schema_validation_schema]] | downstream | 0.22 |
| [[bld_schema_integration_guide]] | downstream | 0.22 |
| [[bld_schema_research_pipeline]] | downstream | 0.21 |
| [[bld_schema_quickstart_guide]] | downstream | 0.21 |
| [[bld_schema_reranker_config]] | downstream | 0.21 |
| [[bld_schema_input_schema]] | downstream | 0.21 |
| [[bld_schema_dataset_card]] | downstream | 0.21 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.21 |
