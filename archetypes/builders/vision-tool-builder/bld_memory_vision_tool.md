---
id: p10_lr_vision_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: edison
observation: "Vision tools without declared confidence_threshold returned noisy low-confidence detections that corrupted 3 of 5 downstream data pipelines. Tools with explicit confidence_threshold (0.8+) and supported_formats declarations composed correctly in every integration reviewed."
pattern: "Declare confidence_threshold explicitly. List supported_formats — providers differ significantly. Mirror capabilities list in frontmatter to body section names. Keep body under 2048 bytes. Always declare providers."
evidence: "5 document pipelines: 3 failed with noise from unfiltered confidence; 0 failures after threshold was declared. Provider list omission caused 4 runtime surprises where callers sent unsupported formats."
confidence: 0.8
outcome: SUCCESS
domain: vision_tool
tags: [vision-tool, confidence-threshold, providers, supported-formats, ocr, image-analysis]
tldr: "Confidence threshold is load-bearing for data quality. Supported_formats prevents runtime surprises. Mirror capabilities in frontmatter to body. Stay under 2048 bytes."
impact_score: 8.0
decay_rate: 0.04
agent_node: edison
keywords: [vision tool, confidence threshold, supported formats, providers, capabilities, ocr, object detection]
---

## Summary
Vision tools are consumed by data pipelines where low-confidence detections are indistinguishable from correct results unless filtered at the spec level. The two most common causes of vision tool integration failure are: (1) undeclared confidence_threshold producing noisy output, and (2) missing supported_formats causing callers to send incompatible image types.
The difference between a vision tool that composes well and one that silently corrupts data comes down to three decisions made at spec time: confidence threshold, supported formats, and provider declaration. All three are invisible during happy-path use and catastrophic on failure.
## Pattern
**Declare confidence threshold, supported formats, and providers at spec time.**
Confidence threshold schema:
- 0.9+: high precision, may miss detections — use for legal/financial document OCR
- 0.8: balanced default — recommended for most production tools
- 0.7: higher recall, more noise — use only when completeness > precision
- 0.5: low threshold — only for exploratory/research tools, never production
Supported formats rules:
- Tesseract: png, jpg, jpeg, bmp, tiff (no PDF native — requires conversion)
- DocTR: png, jpg, jpeg, pdf, tiff
- OpenAI Vision: png, jpg, jpeg, webp, gif (no TIFF, no PDF)
- Google Vision: png, jpg, jpeg, gif, bmp, webp, tiff, pdf, ico
- Azure Computer Vision: png, jpg, jpeg, gif, bmp, webp, tiff
- Anthropic Claude: png, jpg, jpeg, webp, gif (no TIFF, no PDF)
Capabilities list:
- Write capabilities list in frontmatter first (forces scope decision before prose)
- Each frontmatter capability name must exactly match a `## Capabilities > {name}` section in body
- Each capability entry in body must include: input format, output schema, confidence range
Body budget (2048 bytes max): Overview (150) + Input Types (400) + Capabilities (1000) + Output Format (400) = ~1950.
## Anti-Pattern
- Omitting confidence_threshold entirely (caller receives all detections regardless of quality; data noise)
- Provider list empty or set to "any" (runtime provider selection is not a spec concern)
- Using unsupported image formats with specific providers (Tesseract + PDF = silent failure)
- Capabilities list in frontmatter not matching body section names (spec drift)
- Conflating vision_tool with computer_use (vision reads; computer_use acts)
- Including API keys or credentials in spec (spec is a public contract document)
- Setting quality to non-null value (self-scoring corrupts pool quality metrics)
## Context
Body limit 2048B. Budget: Overview (150) + Input Types (400) + Capabilities (1000) + Output (400). Link to provider docs, don't duplicate.
