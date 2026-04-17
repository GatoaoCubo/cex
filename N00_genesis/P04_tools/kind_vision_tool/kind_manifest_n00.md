---
id: n00_vision_tool_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Vision Tool -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, vision_tool, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A vision_tool provides agents with image analysis, OCR (optical character recognition), and screenshot interpretation capabilities by routing images to vision-capable LLMs or specialized vision APIs. It handles image preprocessing, resolution normalization, and structured output extraction from visual content. The output is a tool that converts image inputs into structured text observations agents can reason over.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `vision_tool` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| capabilities | list | yes | Supported operations: ocr, classification, description, structured_extract |
| provider | string | yes | Backend: claude_vision, gpt4v, google_vision, tesseract |
| output_format | string | yes | text, json, or markdown |
| max_image_size_kb | integer | no | Maximum input image size before downsampling |

## When to use
- When an agent needs to read text from screenshots, PDFs, or scanned documents
- When computer_use requires an image interpretation layer to understand UI state
- When N01 Intelligence processes competitor screenshots or product images for analysis

## Builder
`archetypes/builders/vision_tool-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind vision_tool --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: vt_claude_screenshot_reader
kind: vision_tool
pillar: P04
nucleus: n05
title: "Claude Screenshot Reader"
version: 1.0
quality: null
---
capabilities: [ocr, description, structured_extract]
provider: claude_vision
output_format: json
max_image_size_kb: 5120
```

## Related kinds
- `computer_use` (P04) -- higher-level tool that uses vision_tool to interpret screen state
- `browser_tool` (P04) -- browser automation that captures screenshots for vision_tool analysis
- `multi_modal_config` (P04) -- configuration that specifies image encoding rules for vision_tool
- `multimodal_prompt` (P03) -- prompt template that structures vision_tool output for LLM reasoning
