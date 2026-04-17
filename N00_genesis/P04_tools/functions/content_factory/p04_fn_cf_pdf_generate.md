---
id: p04_fn_cf_pdf_generate
kind: function_def
pillar: P04
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: generate_pdf
description: "Generate a styled PDF from Markdown or HTML input using Typst, Pandoc, or WeasyPrint. Call when the Content Factory needs formatted PDF output — handouts, worksheets, reports, or printable materials."
parameters:
  type: object
  properties:
    input_path:
      type: string
      description: "Path to the source file (.md, .html, or .typ)"
    engine:
      type: string
      description: "PDF generation engine"
      enum: [typst, pandoc, weasyprint]
    output_path:
      type: string
      description: "Destination path for the generated PDF"
    template:
      type: string
      description: "Path to style template (Typst .typ, Pandoc .latex, WeasyPrint .css)"
    variables:
      type: object
      description: "Key-value pairs injected into the template (title, author, date, etc.)"
      additionalProperties:
        type: string
    page_size:
      type: string
      description: "Paper size"
      enum: [a4, letter, a5, custom]
    toc:
      type: boolean
      description: "Include table of contents"
  required: [input_path, engine, output_path]
returns:
  type: object
  description: "PDF generation result"
  properties:
    output_path:
      type: string
      description: "Path to the generated PDF file"
    page_count:
      type: integer
      description: "Number of pages in the output"
    file_size_bytes:
      type: integer
      description: "Size of the generated PDF"
    engine_used:
      type: string
      description: "Which engine produced the PDF"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content_factory
quality: 9.0
tags: [function_def, pdf, typst, pandoc, generate, content_factory]
tldr: "LLM-callable function to generate styled PDFs from Markdown/HTML via Typst, Pandoc, or WeasyPrint"
examples:
  - input: {"input_path": "chapter_04.md", "engine": "typst", "output_path": "output/chapter_04.pdf", "template": "templates/book.typ"}
    output: {"output_path": "output/chapter_04.pdf", "page_count": 12, "file_size_bytes": 245760, "engine_used": "typst"}
error_types: [input_not_found, template_not_found, engine_not_installed, compilation_error]
density_score: 0.98
---

# PDF Generator Function

## Overview
Generates a styled PDF from Markdown, HTML, or Typst source files. The LLM calls this when the Content Factory pipeline needs printable output — ebook chapters, worksheets, handouts, or reports. Supports three engines with different strengths: Typst (fast, modern), Pandoc (flexible, LaTeX), WeasyPrint (CSS-styled HTML).

## Parameters

### input_path
Type: string | Required: yes
Path to the source file. Supported: `.md` (Markdown), `.html`, `.typ` (Typst). Relative to working directory.

### engine
Type: string (enum) | Required: yes
- `typst`: Fast compilation, modern syntax, best for structured documents
- `pandoc`: Maximum format flexibility, LaTeX backend, best for academic/complex layouts
- `weasyprint`: CSS-styled HTML to PDF, best for web-like designs

### output_path
Type: string | Required: yes
Destination path for the PDF. Parent directory must exist.

### template
Type: string | Required: no
Path to a style template. Engine-specific: `.typ` for Typst, `.latex` for Pandoc, `.css` for WeasyPrint.

### variables
Type: object | Required: no
Template variables injected at compile time. Common: `title`, `author`, `date`, `brand_name`.

### page_size
Type: string (enum) | Required: no | Default: a4
Paper size. `custom` requires width/height in the template.

### toc
Type: boolean | Required: no | Default: false
Generate table of contents from document headers.

## Returns
Type: object with `output_path`, `page_count`, `file_size_bytes`, `engine_used`.

## Examples

### Example 1: eBook chapter via Typst
```json
{"input_path": "chapters/ch04_vectors.md", "engine": "typst", "output_path": "output/ch04.pdf", "template": "templates/ebook.typ", "variables": {"title": "Storing Embeddings", "author": "DataCraft"}, "toc": true}
```

### Example 2: Worksheet via WeasyPrint
```json
{"input_path": "worksheets/docker_basics.html", "engine": "weasyprint", "output_path": "output/worksheet.pdf", "template": "templates/worksheet.css", "page_size": "a4"}
```
