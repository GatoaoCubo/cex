---
kind: output_template
id: bld_output_template_vision_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a vision_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Vision Tool"
version: "1.0.0"
author: n03_builder
tags: [vision_tool, builder, examples]
tldr: "Golden and anti-examples for vision tool construction, demonstrating ideal structure and common pitfalls."
domain: "vision tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_vision_tool
  - bld_schema_vision_tool
  - p03_sp_vision_tool_builder
  - bld_instruction_vision_tool
  - bld_output_template_input_schema
  - p11_qg_vision_tool
  - bld_output_template_output_validator
  - bld_output_template_feature_flag
  - bld_output_template_golden_test
  - bld_output_template_runtime_rule
---

# Output Template: vision_tool
```yaml
id: p04_vision_{{capability_slug}}
kind: vision_tool
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_tool_name}}"
input_types:
  - {{base64|url|file_path|buffer|screenshot}}
  - {{base64|url|file_path|buffer|screenshot}}
capabilities:
  - {{capability_name_1}}
  - {{capability_name_2}}
output_format: {{json|text|table}}
providers:
  - {{openai_vision|anthropic_claude|google_vision|azure_computer_vision|tesseract|doctr}}
quality: null
tags: [vision_tool, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_tool_does_max_200ch}}"
max_resolution: "{{WxH_or_omit}}"
supported_formats: [{{png|jpg|jpeg|webp|gif|bmp|tiff|pdf}}]
confidence_threshold: {{0.0_to_1.0_default_0.8}}
batch_support: {{true|false}}
max_bytes_per_image: {{bytes_integer_or_omit}}
```
## Overview
`{{what_the_tool_does_1_to_2_sentences}}`
`{{who_uses_it_and_primary_use_case}}`
## Input Types
### `{{input_type_1}}`
`{{format_description_encoding_and_size_limit}}`
### `{{input_type_2}}`
`{{format_description_encoding_and_size_limit}}`
## Capabilities
### `{{capability_name_1}}`
`{{what_the_capability_detects_or_extracts}}`
Confidence range: `{{min}}`-`{{max}}`. Results filtered at confidence_threshold.
Output: `{{json_schema_or_field_description}}`
### `{{capability_name_2}}`
`{{what_the_capability_detects_or_extracts}}`
Output: `{{json_schema_or_field_description}}`
## Output Format
`{{primary_format_description_with_envelope_schema}}`
`{capability: string, {{processing_field}}: {{type}}, results: {…capability_schema}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | vision tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_vision_tool]] | downstream | 0.40 |
| [[bld_schema_vision_tool]] | downstream | 0.39 |
| [[p03_sp_vision_tool_builder]] | upstream | 0.38 |
| [[bld_instruction_vision_tool]] | upstream | 0.38 |
| [[bld_output_template_input_schema]] | sibling | 0.37 |
| [[p11_qg_vision_tool]] | downstream | 0.34 |
| [[bld_output_template_output_validator]] | sibling | 0.33 |
| [[bld_output_template_feature_flag]] | sibling | 0.33 |
| [[bld_output_template_golden_test]] | sibling | 0.33 |
| [[bld_output_template_runtime_rule]] | sibling | 0.32 |
