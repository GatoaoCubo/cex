---
id: p04_fn_cf_slides_generate
kind: function_def
8f: F6_produce
pillar: P04
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: generate_slides
description: "Generate a slide presentation from Markdown using Marp. Call when the Content Factory needs PPTX, PDF, or HTML slides from structured Markdown content with speaker notes and visual themes."
parameters:
  type: object
  properties:
    input_path:
      type: string
      description: "Path to Marp-formatted Markdown file (uses triple-dash slide separators)"
    output_path:
      type: string
      description: "Destination path for the generated slides"
    format:
      type: string
      description: "Output format"
      enum: [pptx, pdf, html]
    theme:
      type: string
      description: "Marp theme name or path to custom CSS theme"
    width:
      type: integer
      description: "Slide width in pixels"
    height:
      type: integer
      description: "Slide height in pixels"
    paginate:
      type: boolean
      description: "Show page numbers on slides"
  required: [input_path, output_path, format]
returns:
  type: object
  description: "Slide generation result"
  properties:
    output_path:
      type: string
      description: "Path to the generated file"
    slide_count:
      type: integer
      description: "Number of slides generated"
    file_size_bytes:
      type: integer
      description: "Output file size"
    format:
      type: string
      description: "Output format produced"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content_factory
quality: 9.0
tags: [function_def, marp, slides, presentation, pptx, content_factory]
tldr: "LLM-callable function to generate PPTX/PDF/HTML slides from Marp Markdown via CLI"
examples:
  - input: {"input_path": "slides/module3.md", "output_path": "output/module3.pptx", "format": "pptx", "theme": "brand-dark"}
    output: {"output_path": "output/module3.pptx", "slide_count": 15, "file_size_bytes": 1048576, "format": "pptx"}
error_types: [input_not_found, marp_not_installed, invalid_markdown, theme_not_found]
density_score: 0.99
related:
  - p01_kc_marp_cli
  - p04_fn_cf_pdf_generate
  - p04_fn_cf_canva_export
  - p05_fmt_content_adapter
  - bld_schema_research_pipeline
  - bld_schema_validation_schema
  - bld_schema_pitch_deck
  - bld_schema_input_schema
  - p06_schema_env_contract
  - bld_schema_reranker_config
---

# Slides Generator Function (Marp)

## Overview
Generates slide presentations from Marp-formatted Markdown. The LLM calls this when the Content Factory pipeline has structured slide content (from `p03_pt_cf_slide_deck` template) and needs it compiled into deliverable PPTX, PDF, or HTML format. Marp handles theming, pagination, and speaker notes.

## Parameters

### input_path
Type: string | Required: yes
Path to a Marp-compatible Markdown file. Must use `---` as slide separators and `<!-- -->` for speaker notes.

### output_path
Type: string | Required: yes
Destination for generated file. Extension should match format.

### format
Type: string (enum) | Required: yes
- `pptx`: Editable PowerPoint — best for client delivery
- `pdf`: Fixed layout — best for distribution and printing
- `html`: Interactive — best for web embedding and live presentations

### theme
Type: string | Required: no | Default: default
Marp built-in theme (`default`, `gaia`, `uncover`) or path to custom CSS.

### width / height
Type: integer | Required: no | Default: 1280x720
Slide dimensions in pixels. Common: 1280x720 (16:9), 1920x1080 (HD), 960x720 (4:3).

### paginate
Type: boolean | Required: no | Default: true
Show slide numbers. Disable for title slides and social content.

## Returns
Type: object with `output_path`, `slide_count`, `file_size_bytes`, `format`.

## CLI Command
```bash
marp --theme {theme} --{format} --allow-local-files -o {output_path} {input_path}
```

## Examples

### Example 1: Course module slides to PPTX
```json
{"input_path": "slides/ai_agents_m3.md", "output_path": "output/ai_agents_m3.pptx", "format": "pptx", "theme": "themes/brand-dark.css", "paginate": true}
```

### Example 2: Pitch deck to PDF
```json
{"input_path": "slides/pitch_series_a.md", "output_path": "output/pitch.pdf", "format": "pdf", "theme": "gaia", "width": 1920, "height": 1080}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_marp_cli]] | upstream | 0.49 |
| [[p04_fn_cf_pdf_generate]] | sibling | 0.30 |
| [[p04_fn_cf_canva_export]] | sibling | 0.29 |
| [[p05_fmt_content_adapter]] | downstream | 0.26 |
| [[bld_schema_research_pipeline]] | downstream | 0.25 |
| [[bld_schema_validation_schema]] | downstream | 0.24 |
| [[bld_schema_pitch_deck]] | downstream | 0.23 |
| [[bld_schema_input_schema]] | downstream | 0.23 |
| [[p06_schema_env_contract]] | downstream | 0.22 |
| [[bld_schema_reranker_config]] | downstream | 0.22 |
