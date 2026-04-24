---
id: p04_vision_tool_NAME
kind: vision_tool
8f: F5_call
pillar: P04
version: 1.0.0
title: "Template - Vision Tool"
tags: [template, vision, image, ocr, analysis]
tldr: "Configures a vision tool for image analysis, OCR, or screenshot interpretation. Defines model, resolution, cost limits, and output format."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
related:
  - p01_kc_vision_tool
  - p04_vision_gpt4v
  - p01_kc_multi_modal_config
  - bld_instruction_vision_tool
  - bld_knowledge_card_multi_modal_config
  - vision-tool-builder
  - p01_kc_universal_llm
  - bld_examples_model_provider
  - bld_collaboration_vision_tool
  - bld_config_model_provider
---

# Vision Tool: [NAME]

## Purpose
Enables agents to analyze images: screenshots, documents, diagrams, photos.

## Configuration
```yaml
provider: [openai | anthropic | google]
model: [gpt-4o | claude-sonnet-4-6 | gemini-pro-vision]
max_resolution: [low | auto | high]
max_images_per_request: [1 | 5 | 20]
output_format: [text | json | markdown]
max_tokens_response: [500 | 1000 | 4000]
```

## Capabilities

| Capability | Model | Accuracy | Notes |
|---|---|---|---|
| OCR (text extraction) | gpt-4o | 95%+ | Best for documents |
| Diagram analysis | claude-sonnet | 90% | Understands flowcharts |
| Photo description | gemini-pro | 85% | Good for natural images |
| Screenshot UI | claude-sonnet | 92% | Best for computer use |

## Error Handling
1. **Image too large**: Resize to max_resolution before sending
2. **Unsupported format**: Convert to PNG/JPEG
3. **Model timeout**: Retry with lower resolution
4. **Cost exceeded**: Reject + alert

## Quality Gate
1. [ ] Provider and model specified
2. [ ] Resolution setting defined (low saves 60% cost)
3. [ ] Output format matches downstream consumer
4. [ ] Cost limit per image set

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `vision_tool` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_vision_tool]] | upstream | 0.33 |
| [[p04_vision_gpt4v]] | sibling | 0.32 |
| [[p01_kc_multi_modal_config]] | related | 0.29 |
| [[bld_instruction_vision_tool]] | upstream | 0.27 |
| [[bld_knowledge_card_multi_modal_config]] | upstream | 0.26 |
| [[vision-tool-builder]] | related | 0.25 |
| [[p01_kc_universal_llm]] | upstream | 0.25 |
| [[bld_examples_model_provider]] | downstream | 0.24 |
| [[bld_collaboration_vision_tool]] | downstream | 0.24 |
| [[bld_config_model_provider]] | downstream | 0.24 |
