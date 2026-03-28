---
kind: output_template
id: bld_output_template_vision_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a vision_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_the_tool_does_1_to_2_sentences}}
{{who_uses_it_and_primary_use_case}}
## Input Types
### {{input_type_1}}
{{format_description_encoding_and_size_limit}}
### {{input_type_2}}
{{format_description_encoding_and_size_limit}}
## Capabilities
### {{capability_name_1}}
{{what_the_capability_detects_or_extracts}}
Confidence range: {{min}}-{{max}}. Results filtered at confidence_threshold.
Output: `{{json_schema_or_field_description}}`
### {{capability_name_2}}
{{what_the_capability_detects_or_extracts}}
Output: `{{json_schema_or_field_description}}`
## Output Format
{{primary_format_description_with_envelope_schema}}
`{capability: string, {{processing_field}}: {{type}}, results: {…capability_schema}}`
