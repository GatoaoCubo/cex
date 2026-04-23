---
id: p04_fn_cf_canva_create
kind: function_def
pillar: P04
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: canva_create_design
description: "Create a new design in Canva via API. Call when the Content Factory needs a presentation, social media graphic, document, or video canvas. Requires design_type and title; optionally accepts template_id for brand consistency."
parameters:
  type: object
  properties:
    design_type:
      type: string
      description: "Type of Canva design to create"
      enum: [presentation, social_media_post, document, video, whiteboard, logo, poster]
    title:
      type: string
      description: "Title of the design (appears in Canva dashboard)"
    template_id:
      type: string
      description: "Canva brand template ID for consistent styling. Get from list_brand_templates."
    width:
      type: integer
      description: "Custom canvas width in pixels (overrides design_type defaults)"
    height:
      type: integer
      description: "Custom canvas height in pixels (overrides design_type defaults)"
    brand_kit_id:
      type: string
      description: "Canva brand kit ID for colors, fonts, logos"
    content_data:
      type: object
      description: "Key-value pairs for template autofill (maps to template placeholders)"
      additionalProperties:
        type: string
  required: [design_type, title]
returns:
  type: object
  description: "Created design metadata"
  properties:
    design_id:
      type: string
      description: "Unique Canva design ID for subsequent operations"
    edit_url:
      type: string
      description: "URL to edit the design in Canva"
    thumbnail_url:
      type: string
      description: "URL of the design thumbnail"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content_factory
quality: 9.0
tags: [function_def, canva, design, create, content_factory]
tldr: "LLM-callable function to create Canva designs via API — presentations, social posts, documents, videos"
examples:
  - input: {"design_type": "presentation", "title": "Q1 Results", "template_id": "DAF_abc123"}
    output: {"design_id": "DAGxyz789", "edit_url": "https://canva.com/design/DAGxyz789/edit", "thumbnail_url": "https://canva.com/design/DAGxyz789/thumb"}
error_types: [invalid_template_id, quota_exceeded, invalid_dimensions, auth_expired]
density_score: 0.91
related:
  - p01_kc_canva_connect_api
  - bld_schema_model_registry
  - n06_schema_brand_config
  - bld_schema_research_pipeline
  - p04_fn_cf_canva_export
  - bld_schema_input_schema
  - bld_schema_api_reference
  - bld_schema_multimodal_prompt
  - bld_schema_social_publisher
  - p03_ch_content_pipeline
---

# Canva Create Design Function

## Overview
Creates a new design in Canva via the Connect API. The LLM calls this when the Content Factory pipeline needs a visual asset — presentation slides, social media graphics, documents, or video canvases. Supports brand templates for consistent styling and autofill for dynamic content injection.

## Parameters

### design_type
Type: string (enum) | Required: yes
One of: presentation, social_media_post, document, video, whiteboard, logo, poster.
Determines default canvas dimensions and Canva editor mode.

### title
Type: string | Required: yes
Display name in the Canva dashboard. Use descriptive names for organization.

### template_id
Type: string | Required: no
Brand template ID from `list_brand_templates`. When provided, the design starts from this template instead of blank.

### width / height
Type: integer | Required: no
Custom dimensions in pixels. Overrides design_type defaults. Use for non-standard aspect ratios.

### brand_kit_id
Type: string | Required: no
Applies brand colors, fonts, and logos automatically.

### content_data
Type: object | Required: no
Key-value pairs that map to template autofill placeholders. Keys must match template placeholder names.

## Returns
Type: object with `design_id` (string), `edit_url` (string), `thumbnail_url` (string).

## Examples

### Example 1: Create branded presentation
```json
{"design_type": "presentation", "title": "AI Agents Course - Module 3", "template_id": "DAF_brand_deck", "brand_kit_id": "BK_main"}
```
→ `{"design_id": "DAG_m3deck", "edit_url": "https://canva.com/design/DAG_m3deck/edit", "thumbnail_url": "..."}`

### Example 2: Create social post with autofill
```json
{"design_type": "social_media_post", "title": "Launch Post - LinkedIn", "template_id": "DAF_social_li", "content_data": {"headline": "New course live today", "subtext": "8 hours of hands-on AI", "cta": "Link in comments"}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_canva_connect_api]] | upstream | 0.32 |
| [[bld_schema_model_registry]] | downstream | 0.31 |
| [[n06_schema_brand_config]] | downstream | 0.30 |
| [[bld_schema_research_pipeline]] | downstream | 0.29 |
| [[p04_fn_cf_canva_export]] | sibling | 0.28 |
| [[bld_schema_input_schema]] | downstream | 0.28 |
| [[bld_schema_api_reference]] | downstream | 0.27 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.27 |
| [[bld_schema_social_publisher]] | downstream | 0.27 |
| [[p03_ch_content_pipeline]] | upstream | 0.26 |
