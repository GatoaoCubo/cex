---
id: p04_vision_tool_NAME
kind: vision_tool
pillar: P04
version: 1.0.0
title: "Template - Vision Tool"
tags: [template, vision, image, ocr, analysis]
tldr: "Configures a vision tool for image analysis, OCR, or screenshot interpretation. Defines model, resolution, cost limits, and output format."
quality: null
---

# Vision Tool: [NAME]

## Purpose
Enables agents to analyze images: screenshots, documents, diagrams, photos.

## Configuration
```yaml
provider: [openai | anthropic | google]
model: [gpt-4o | claude-sonnet-4-20250514 | gemini-pro-vision]
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
- **Image too large**: Resize to max_resolution before sending
- **Unsupported format**: Convert to PNG/JPEG
- **Model timeout**: Retry with lower resolution
- **Cost exceeded**: Reject + alert

## Quality Gate
- [ ] Provider and model specified
- [ ] Resolution setting defined (low saves 60% cost)
- [ ] Output format matches downstream consumer
- [ ] Cost limit per image set
