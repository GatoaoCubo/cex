---
kind: output_template
id: bld_output_template_function_def
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a function_def artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Function Def"
version: "1.0.0"
author: n03_builder
tags: [function_def, builder, examples]
tldr: "Golden and anti-examples for function def construction, demonstrating ideal structure and common pitfalls."
domain: "function def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: function_def
```yaml
id: p04_fn_{{function_slug}}
kind: function_def
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{function_name_snake_case}}"
description: "{{what_function_does_max_200ch}}"
parameters:
  type: object
  properties:
    {{param_name_1}}:
      type: "{{string|number|boolean|array|object}}"
      description: "{{param_description}}"
    {{param_name_2}}:
      type: "{{string|number|boolean|array|object}}"
      description: "{{param_description}}"
      enum: [{{value_1}}, {{value_2}}]
  required: [{{param_name_1}}]
returns:
  type: "{{string|number|boolean|array|object}}"
  description: "{{return_description}}"
provider_compat: [openai, anthropic, gemini, bedrock]
strict: {{true|false}}
quality: null
tags: [function_def, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
examples:
  - input: {"{{param_name_1}}": "{{value}}"}
    output: "{{expected_result}}"
error_types: [{{error_1}}, {{error_2}}]
```

## Overview
`{{what_the_function_does_1_to_2_sentences}}`
`{{when_an_LLM_should_call_this_function}}`

## Parameters
### `{{param_name_1}}`
Type: `{{type}}` | Required: {{yes|no}} | Default: `{{default}}`
`{{detailed_description_with_constraints}}`

### `{{param_name_2}}`
Type: `{{type}}` | Required: {{yes|no}} | Default: `{{default}}`
`{{detailed_description_with_constraints}}`
Enum: `{{list_of_allowed_values_if_applicable}}`

## Returns
Type: `{{return_type}}`
Structure: `{{return_structure_description}}`
Example: `{{concrete_return_value}}`

## Examples
### Example 1: `{{scenario_name}}`
Input:
```json
{"{{param_name_1}}": "{{value}}", "{{param_name_2}}": "{{value}}"}
```
Output:
```json
{{expected_output}}
```

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
| Domain | function def construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
