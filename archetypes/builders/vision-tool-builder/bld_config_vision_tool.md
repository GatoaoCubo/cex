---
kind: config
id: bld_config_vision_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Vision Tool"
version: "1.0.0"
author: n03_builder
tags: [vision_tool, builder, examples]
tldr: "Golden and anti-examples for vision tool construction, demonstrating ideal structure and common pitfalls."
domain: "vision tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_vision_tool
  - p03_sp_vision_tool_builder
  - bld_instruction_vision_tool
  - bld_config_memory_scope
  - bld_config_cli_tool
  - bld_output_template_vision_tool
  - bld_examples_vision_tool
  - bld_schema_vision_tool
  - bld_config_output_validator
  - bld_config_prompt_version
---
# Config: vision_tool Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_vision_{capability_slug}.md` | `p04_vision_document_ocr.md` |
| Builder directory | kebab-case | `vision-tool-builder/` |
| Frontmatter fields | snake_case | `input_types`, `output_format`, `confidence_threshold` |
| Capability slug | snake_case, lowercase, no hyphens | `document_ocr`, `scene_classifier`, `face_detector` |
| Capability names | snake_case, noun or noun_verb | `text_extraction`, `object_detection`, `layout_detection` |
| Provider names | snake_case, lowercase | `openai_vision`, `google_vision`, `tesseract`, `doctr` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_vision_{capability_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_vision_{capability_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Output Format Enum
| Value | When to use |
|-------|-------------|
| json | Structured extraction (OCR blocks, detected objects, classification labels) |
| text | Narrative scene description, caption generation |
| table | Tabular data extraction (spreadsheets, forms, structured documents) |
## Input Type Enum
| Value | Encoding | Max Size | Notes |
|-------|----------|----------|-------|
| base64 | UTF-8 base64 string | 10MB decoded | Optional data URI prefix |
| url | HTTP/HTTPS URL string | Provider limit | Must be publicly accessible |
| file_path | Absolute or relative path | Disk limit | Local filesystem only |
| buffer | In-memory bytes object | 20MB | For pipeline integrations |
| screenshot | Captured frame buffer | 5MB | From screen capture tools |
## Capability Name Conventions
| Category | Canonical Names |
|----------|----------------|
| Text | text_extraction, layout_detection, table_extraction, handwriting_recognition |
| Objects | object_detection, logo_detection, product_recognition |
| Scene | scene_description, landmark_detection, safe_search |
| Classification | image_classification, sentiment_analysis, topic_classification |
| People | face_detection, emotion_recognition, age_estimation |
| Documents | document_parsing, form_extraction, barcode_detection |
## Provider Name Registry
`openai_vision` | `anthropic_claude` | `google_vision` | `azure_computer_vision` | `tesseract` | `doctr`
Rule: use canonical provider names from registry — costm names must document full endpoint.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_vision_tool]] | upstream | 0.35 |
| [[p03_sp_vision_tool_builder]] | upstream | 0.34 |
| [[bld_instruction_vision_tool]] | upstream | 0.30 |
| [[bld_config_memory_scope]] | sibling | 0.30 |
| [[bld_config_cli_tool]] | sibling | 0.30 |
| [[bld_output_template_vision_tool]] | upstream | 0.29 |
| [[bld_examples_vision_tool]] | upstream | 0.29 |
| [[bld_schema_vision_tool]] | upstream | 0.28 |
| [[bld_config_output_validator]] | sibling | 0.28 |
| [[bld_config_prompt_version]] | sibling | 0.28 |
