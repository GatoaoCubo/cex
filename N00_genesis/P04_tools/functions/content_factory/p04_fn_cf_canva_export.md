---
id: p04_fn_cf_canva_export
kind: function_def
pillar: P04
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: canva_export_design
description: "Export a Canva design to a downloadable file. Call after canva_create_design to produce PDF, PPTX, PNG, or MP4 output. Requires design_id and format."
parameters:
  type: object
  properties:
    design_id:
      type: string
      description: "Canva design ID returned by canva_create_design"
    format:
      type: string
      description: "Export file format"
      enum: [pdf, pptx, png, jpg, mp4, gif, svg]
    quality:
      type: string
      description: "Export quality level"
      enum: [draft, standard, high]
    pages:
      type: array
      items:
        type: integer
      description: "Specific page indices to export (0-based). Omit to export all pages."
    width:
      type: integer
      description: "Output width in pixels (for image/video formats)"
    lossless:
      type: boolean
      description: "Use lossless compression for PNG exports"
  required: [design_id, format]
returns:
  type: object
  description: "Export job result with download URL"
  properties:
    export_id:
      type: string
      description: "Export job ID for status tracking"
    status:
      type: string
      description: "Export status — pending, processing, completed, failed"
    download_url:
      type: string
      description: "Temporary URL to download the exported file (valid 24h)"
    file_size_bytes:
      type: integer
      description: "Size of the exported file"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content_factory
quality: 9.0
tags: [function_def, canva, export, pdf, pptx, content_factory]
tldr: "LLM-callable function to export Canva designs as PDF, PPTX, PNG, MP4 files"
examples:
  - input: {"design_id": "DAGxyz789", "format": "pdf", "quality": "high"}
    output: {"export_id": "EXP_001", "status": "completed", "download_url": "https://export.canva.com/...", "file_size_bytes": 2451200}
error_types: [design_not_found, export_in_progress, unsupported_format, auth_expired]
density_score: 0.91
related:
  - p01_kc_canva_connect_api
  - p04_fn_cf_canva_create
  - p04_fn_cf_slides_generate
  - bld_schema_research_pipeline
  - spec_content_factory_v1
  - bld_output_template_function_def
  - p03_ch_content_pipeline
  - bld_schema_validation_schema
  - bld_schema_social_publisher
  - p06_schema_env_contract
---

# Canva Export Design Function

## Overview
Exports a Canva design to a downloadable file format. The LLM calls this after creating or editing a design to produce deliverable output — PDF handouts, PPTX presentations, PNG social graphics, or MP4 videos. Export is asynchronous; poll status until completed.

## Parameters

### design_id
Type: string | Required: yes
The Canva design ID returned by `canva_create_design`. Must reference an existing design.

### format
Type: string (enum) | Required: yes
One of: pdf, pptx, png, jpg, mp4, gif, svg. Choose based on deliverable type: pdf for documents, pptx for editable slides, png for social, mp4 for video.

### quality
Type: string (enum) | Required: no | Default: standard
Export quality: draft (fast, lower res), standard (balanced), high (print-ready, slower).

### pages
Type: array of integers | Required: no
Zero-based page indices. Omit to export all. Use for multi-page designs when only specific slides are needed.

### width
Type: integer | Required: no
Custom output width in pixels. Maintains aspect ratio. Use for platform-specific image sizes.

### lossless
Type: boolean | Required: no | Default: false
Lossless PNG compression. Increases file size but preserves quality for print.

## Returns
Type: object with `export_id`, `status`, `download_url` (valid 24h), `file_size_bytes`.

## Examples

### Example 1: Export presentation as PPTX
```json
{"design_id": "DAG_m3deck", "format": "pptx", "quality": "high"}
```
→ `{"export_id": "EXP_deck01", "status": "completed", "download_url": "https://export.canva.com/deck01.pptx", "file_size_bytes": 5242880}`

### Example 2: Export specific slides as PNG
```json
{"design_id": "DAG_m3deck", "format": "png", "pages": [0, 5, 11], "width": 1200}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_canva_connect_api]] | upstream | 0.34 |
| [[p04_fn_cf_canva_create]] | sibling | 0.31 |
| [[p04_fn_cf_slides_generate]] | sibling | 0.28 |
| [[bld_schema_research_pipeline]] | downstream | 0.22 |
| [[spec_content_factory_v1]] | downstream | 0.21 |
| [[bld_output_template_function_def]] | downstream | 0.21 |
| [[p03_ch_content_pipeline]] | upstream | 0.21 |
| [[bld_schema_validation_schema]] | downstream | 0.20 |
| [[bld_schema_social_publisher]] | downstream | 0.20 |
| [[p06_schema_env_contract]] | downstream | 0.19 |
