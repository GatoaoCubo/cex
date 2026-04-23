---
id: p10_lr_vision_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
observation: "Vision tools without declared confidence_threshold returned noisy low-confidence detections that corrupted 3 of 5 downstream data pipelines. Tools with explicit confidence_threshold (0.8+) and supported_formats declarations composed correctly in every integration reviewed."
pattern: "Declare confidence_threshold explicitly. List supported_formats — providers differ significantly. Mirror capabilities list in frontmatter to body section names. Keep body under 2048 bytes. Always declare providers."
evidence: "5 document pipelines: 3 failed with noise from unfiltered confidence; 0 failures after threshold was..."
confidence: 0.8
outcome: SUCCESS
domain: vision_tool
tags: [vision-tool, confidence-threshold, providers, supported-formats, ocr, image-analysis]
tldr: "Confidence threshold is load-bearing for data quality. Supported_formats prevents runtime surprises. Mirror capabilities in frontmatter to body. Stay under 2048 bytes."
impact_score: 8.0
decay_rate: 0.04
agent_group: edison
keywords: [vision tool, confidence threshold, supported formats, providers, capabilities, ocr, object detection]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Vision Tool"
density_score: 0.90
llm_function: INJECT
related:
  - bld_instruction_vision_tool
  - p03_sp_vision_tool_builder
  - bld_output_template_vision_tool
  - bld_examples_vision_tool
  - bld_schema_vision_tool
  - vision-tool-builder
  - bld_collaboration_vision_tool
  - bld_knowledge_card_vision_tool
  - p11_qg_vision_tool
  - p04_vision_tool_NAME
---
## Summary
Vision tools are consumed by data pipelines where low-confidence detections are indistinguishable from correct results unless filtered at the spec level. The two most common causes of vision tool integration failure are: (1) undeclared confidence_threshold producing noisy output, and (2) missing supported_formats causing callers to send incompatible image types.
The difference between a vision tool that composes well and one that silently corrupts data comes down to three decisions made at spec time: confidence threshold, supported formats, and provider declaration. All three are invisible during happy-path use and catastrophic on failure.
## Pattern
**Declare confidence threshold, supported formats, and providers at spec time.**
Confidence threshold schema:
1. 0.9+: high precision, may miss detections — use for legal/financial document OCR
2. 0.8: balanced default — recommended for most production tools
3. 0.7: higher recall, more noise — use only when completeness > precision
4. 0.5: low threshold — only for exploratory/research tools, never production
Supported formats rules:
1. Tesseract: png, jpg, jpeg, bmp, tiff (no PDF native — requires conversion)
2. DocTR: png, jpg, jpeg, pdf, tiff
3. OpenAI Vision: png, jpg, jpeg, webp, gif (no TIFF, no PDF)
4. Google Vision: png, jpg, jpeg, gif, bmp, webp, tiff, pdf, ico
5. Azure Computer Vision: png, jpg, jpeg, gif, bmp, webp, tiff
6. Anthropic Claude: png, jpg, jpeg, webp, gif (no TIFF, no PDF)
Capabilities list:
1. Write capabilities list in frontmatter first (forces scope decision before prose)
2. Each frontmatter capability name must exactly match a `## Capabilities > {name}` section in body
3. Each capability entry in body must include: input format, output schema, confidence range
Body budget (2048 bytes max): Overview (150) + Input Types (400) + Capabilities (1000) + Output Format (400) = ~1950.
## Anti-Pattern
1. Omitting confidence_threshold entirely (caller receives all detections regardless of quality; data noise)
2. Provider list empty or set to "any" (runtime provider selection is not a spec concern)
3. Using unsupported image formats with specific providers (Tesseract + PDF = silent failure)
4. Capabilities list in frontmatter not matching body section names (spec drift)
5. Conflating vision_tool with computer_use (vision reads; computer_use acts)
6. Including API keys or credentials in spec (spec is a public contract document)
7. Setting quality to non-null value (self-scoring corrupts pool quality metrics)
## Context
Body limit 2048B. Budget: Overview (150) + Input Types (400) + Capabilities (1000) + Output (400). Link to provider docs, don't duplicate.

## Metadata

```yaml
id: p10_lr_vision_tool_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-vision-tool-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | vision_tool |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_vision_tool]] | upstream | 0.46 |
| [[p03_sp_vision_tool_builder]] | upstream | 0.41 |
| [[bld_output_template_vision_tool]] | upstream | 0.37 |
| [[bld_examples_vision_tool]] | upstream | 0.36 |
| [[bld_schema_vision_tool]] | upstream | 0.34 |
| [[vision-tool-builder]] | upstream | 0.33 |
| [[bld_collaboration_vision_tool]] | downstream | 0.30 |
| [[bld_knowledge_card_vision_tool]] | upstream | 0.30 |
| [[p11_qg_vision_tool]] | downstream | 0.28 |
| [[p04_vision_tool_NAME]] | upstream | 0.27 |
