---
id: p04_vision_gpt4v
kind: vision_tool
8f: F5_call
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "GPT-4V Image Analyzer"
input_types:
  - base64
  - url
capabilities:
  - image_description
  - ocr
  - object_detection
output_format: json
providers:
  - openai_vision
quality: 9.0
tags: [vision_tool, gpt4v, ocr, image_analysis]
tldr: "GPT-4V vision tool for image description, OCR, and object detection via OpenAI API"
description: "Analyzes images using GPT-4V to extract text, describe content, and detect objects"
max_resolution: "2048x2048"
supported_formats: [png, jpg, jpeg, webp, gif]
confidence_threshold: 0.8
batch_support: false
max_bytes_per_image: 20971520
domain: "tool integration"
title: "Vision Tool Gpt4V"
density_score: 0.9
related:
  - bld_examples_vision_tool
  - p04_vision_tool_NAME
  - p01_kc_vision_tool
  - p03_sp_vision_tool_builder
  - bld_schema_vision_tool
  - vision-tool-builder
  - bld_instruction_vision_tool
  - bld_schema_model_registry
  - bld_collaboration_vision_tool
  - bld_output_template_vision_tool
---

# GPT-4V Image Analyzer

## Overview
Analyzes images using OpenAI's GPT-4V model to extract structured information. Used by agents that need to understand screenshots, product photos, or document scans.

## Input Types
### base64
Base64-encoded image string. Max 20MB after decoding. Preferred for programmatic use.

### url
Public HTTPS URL pointing to an image. Must be accessible without authentication.

## Capabilities
### image_description
Generates natural language description of image contents.
Confidence range: 0.85-0.99. Results filtered at confidence_threshold.
Output: `{"description": "string", "confidence": float}`

### ocr
Extracts visible text from images including screenshots, photos of documents.
Output: `{"text": "string", "regions": [{"bbox": [x,y,w,h], "text": "string"}]}`

### object_detection
Identifies and localizes objects within the image.
Output: `{"objects": [{"label": "string", "bbox": [x,y,w,h], "confidence": float}]}`

## Output Format
JSON envelope: `{"capability": "string", "results": {...}, "model": "gpt-4-vision-preview"}`

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `vision tool`
- **Artifact ID**: `p04_vision_gpt4v`
- **Tags**: [vision_tool, gpt4v, ocr, image_analysis]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `vision tool` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: vision_tool
pillar: P04
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_vision_tool]] | downstream | 0.45 |
| [[p04_vision_tool_NAME]] | sibling | 0.35 |
| [[p01_kc_vision_tool]] | upstream | 0.34 |
| [[p03_sp_vision_tool_builder]] | related | 0.34 |
| [[bld_schema_vision_tool]] | downstream | 0.31 |
| [[vision-tool-builder]] | related | 0.28 |
| [[bld_instruction_vision_tool]] | upstream | 0.28 |
| [[bld_schema_model_registry]] | downstream | 0.27 |
| [[bld_collaboration_vision_tool]] | downstream | 0.27 |
| [[bld_output_template_vision_tool]] | downstream | 0.27 |
