---
id: p01_kc_vision_tool
kind: knowledge_card
type: kind
pillar: P01
title: "Vision Tool — Deep Knowledge for vision_tool"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: vision_tool
quality: 9.1
tags: [vision_tool, P04, CALL, kind-kc, vision, OCR]
tldr: "Processes visual input (images, screenshots, PDFs as images) and returns structured data — OCR text, object labels, layout analysis, and multimodal understanding"
when_to_use: "Building, reviewing, or reasoning about vision_tool artifacts"
keywords: [vision, OCR, image, screenshot, multimodal]
feeds_kinds: [vision_tool]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - p04_vision_tool_NAME
  - kc_multimodal_prompt
  - vision-tool-builder
  - p04_vision_gpt4v
  - p01_kc_multi_modal_config
  - p03_sp_vision_tool_builder
  - bld_architecture_vision_tool
  - bld_collaboration_vision_tool
  - bld_examples_vision_tool
  - bld_instruction_vision_tool
---

# Vision Tool

## Spec
```yaml
kind: vision_tool
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_vision_{{capability}}.md + .yaml
core: false
```

## What It Is
A vision_tool processes visual input (images, screenshots, PDFs rendered as images, charts) and returns structured data: OCR text, object labels, bounding box coordinates, layout structure, captions, or full multimodal analysis. It wraps a vision model API (GPT-4o, Claude 3/4, Gemini Vision) or a specialized library (Tesseract, AWS Textract). It is NOT a browser_tool (which interacts with web pages via DOM) nor a computer_use tool (which controls the OS screen at pixel level).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | HumanMessage with image_url content | Multimodal via vision-capable LLM |
| LlamaIndex | ImageNode, MultiModalVectorStoreIndex | Image indexing and multimodal retrieval |
| CrewAI | VisionTool (crewai-tools) | GPT-4V-based image analysis |
| DSPy | dspy.Predict with image input field | Multimodal signature support |
| Haystack | MultiModalRetriever | Image + text pipeline components |
| OpenAI | vision in gpt-4o, gpt-4-turbo | image_url in messages; detail: high/low/auto |
| Anthropic | vision in claude-3/4 family | Base64 or URL in content blocks |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| capabilities | list | [caption] | More = richer output; more tokens |
| detail | str | auto | high = precise text/tables; low = fast+cheap |
| output_format | str | json | json = structured; text = narrative |
| max_image_size_mb | float | 5.0 | Larger = richer detail; higher latency |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| OCR extraction | PDFs, scanned documents, invoices | Extract invoice fields from JPEG scan |
| Screenshot analysis | UI state validation, QA | Describe page state from PNG screenshot |
| Chart interpretation | Dashboard monitoring, reporting | Parse bar chart values from PNG export |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| High detail always | 2-4x token cost on every call | Use auto; only high for fine text/tables |
| Raw image without resize | Token overflow on large images | Resize to 2048px max before sending |
| vision_tool for DOM interaction | Wrong abstraction layer | Use browser_tool for any DOM actions |

## Integration Graph
```
[image_input / screenshot_bytes] --> [vision_tool] --> [structured: OCR/labels/JSON]
                                          |                       |
                                 [model, detail, format]   [agent reasoning / storage]
```

## Decision Tree
- IF need DOM interaction (click, scroll, fill) THEN use browser_tool
- IF need OS-level screen control (mouse, keyboard) THEN use computer_use
- IF input is PDF document for chunking THEN use document_loader with PDF support
- DEFAULT: vision_tool for any image-to-structured-data extraction task

## Quality Criteria
- GOOD: capability declared, output_format typed, image size validated before send
- GREAT: detail routing (auto/high/low), structured JSON output, fallback on parse failure
- FAIL: always high detail regardless of content, no image size limit, untyped text output

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_vision_tool_NAME]] | downstream | 0.40 |
| [[kc_multimodal_prompt]] | sibling | 0.40 |
| [[vision-tool-builder]] | downstream | 0.39 |
| [[p04_vision_gpt4v]] | downstream | 0.39 |
| [[p01_kc_multi_modal_config]] | sibling | 0.38 |
| [[p03_sp_vision_tool_builder]] | downstream | 0.37 |
| [[bld_architecture_vision_tool]] | downstream | 0.36 |
| [[bld_collaboration_vision_tool]] | downstream | 0.36 |
| [[bld_examples_vision_tool]] | downstream | 0.35 |
| [[bld_instruction_vision_tool]] | downstream | 0.34 |
