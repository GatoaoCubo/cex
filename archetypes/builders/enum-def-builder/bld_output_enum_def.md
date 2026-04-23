---
kind: output_template
id: bld_output_template_enum_def
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an enum_def artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Enum Def"
version: "1.0.0"
author: n03_builder
tags: [enum_def, builder, examples]
tldr: "Golden and anti-examples for enum def construction, demonstrating ideal structure and common pitfalls."
domain: "enum def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p06_enum_def
  - enum-def-builder
  - bld_knowledge_card_enum_def
  - bld_schema_enum_def
  - bld_output_template_function_def
  - bld_instruction_enum_def
  - p03_sp_enum_def_builder
  - bld_collaboration_enum_def
  - bld_output_template_runtime_rule
  - bld_tools_enum_def
---

# Output Template: enum_def
```yaml
id: p06_enum_{{enum_slug}}
kind: enum_def
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_enum_name}}"
values:
  - {{VALUE_1}}
  - {{VALUE_2}}
  - {{VALUE_3}}
default: "{{default_value_or_omit}}"
extensible: {{true|false}}
deprecated:
  - {{deprecated_value_or_omit_section}}
quality: null
tags: [enum_def, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_the_enum_represents_max_200ch}}"
descriptions:
  {{VALUE_1}}: "{{meaning_and_when_to_use}}"
  {{VALUE_2}}: "{{meaning_and_when_to_use}}"
  {{VALUE_3}}: "{{meaning_and_when_to_use}}"
representations:
  json_schema: '{"enum": [{{quoted_values_csv}}]}'
  pydantic: "{{PydanticEnumClassName}}"
  zod: 'z.enum([{{quoted_values_csv}}])'
  graphql: "enum {{GraphQLEnumName}} { {{VALUES_SPACE_SEPARATED}} }"
  typescript: 'type {{TypeName}} = {{quoted_values_pipe_separated}};'
```
## Overview
`{{what_the_enum_represents_1_to_2_sentences}}`
`{{who_uses_it_and_primary_domain_context}}`
## Values
### `{{VALUE_1}}`
`{{description_of_this_value_and_when_to_use_it}}`
### `{{VALUE_2}}`
`{{description_of_this_value_and_when_to_use_it}}`
### `{{VALUE_3}}`
`{{description_of_this_value_and_when_to_use_it}}`
## Usage
JSON Schema: `{"enum": [{{quoted_values_csv}}]}`
Pydantic: `class {{PydanticEnumClassName}}(str, Enum): {{VALUE_1}} = "{{VALUE_1}}"`
Zod: `z.enum([{{quoted_values_csv}}])`
GraphQL: `enum {{GraphQLEnumName}} { {{VALUES_SPACE_SEPARATED}} }`
TypeScript: `type {{TypeName}} = {{quoted_values_pipe_separated}};`
## Constraints
Default: {{default_value_or_"none"}}
Extensible: {{yes — new values may be added in future versions | no — set is closed}}
Deprecated: {{deprecated_value_list_with_reason_or_"none"}}

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
| Domain | enum def construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_enum_def]] | downstream | 0.46 |
| [[enum-def-builder]] | downstream | 0.43 |
| [[bld_knowledge_card_enum_def]] | upstream | 0.42 |
| [[bld_schema_enum_def]] | downstream | 0.40 |
| [[bld_output_template_function_def]] | sibling | 0.40 |
| [[bld_instruction_enum_def]] | upstream | 0.37 |
| [[p03_sp_enum_def_builder]] | downstream | 0.37 |
| [[bld_collaboration_enum_def]] | downstream | 0.36 |
| [[bld_output_template_runtime_rule]] | sibling | 0.35 |
| [[bld_tools_enum_def]] | upstream | 0.33 |
