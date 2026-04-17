---
id: p04_vision_tool_NAME
kind: vision_tool
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
