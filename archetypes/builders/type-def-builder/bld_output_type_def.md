---
id: bld_output_template_type_def
kind: output_template
pillar: P05
llm_function: PRODUCE
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [output-template, type-def, P05, template]
quality: 9.0
title: "Output Template Type Def"
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
density_score: 0.90
related:
  - bld_output_template_input_schema
  - bld_output_template_runtime_rule
  - bld_knowledge_card_type_def
  - bld_output_template_golden_test
  - bld_output_template_skill
  - bld_output_template_feature_flag
  - bld_output_template_embedding_config
  - bld_output_template_function_def
  - bld_output_template_output_validator
  - p11_qg_type_def
---

## Template
```yaml
id: p06_td_{{type_slug}}
kind: type_def
pillar: P06
layer: spec
version: {{version}}
created: "{{created_date}}"
updated: "{{updated_date}}"
author: {{author}}
type_name: {{TypeName}}
base_type: {{base_type}}
domain: {{domain}}
nullable: {{nullable}}
quality: null
tags: {{tags_list}}
tldr: "{{one_sentence_description}}"
## Definition
{{prose_description_of_what_this_type_represents}}
## Constraints
{{constraint_key_1}}: {{constraint_value_1}}
{{constraint_key_2}}: {{constraint_value_2}}
## Composition
mode: {{composition_mode}}
members:
  - {{member_type_1}}
  - {{member_type_2}}
## Inheritance
extends: {{parent_type_def_id}}
## Generics
parameters:
  - name: {{type_param_name}}
    bound: {{type_param_bound}}
## Serialization
format: {{serialization_format}}
encoding: {{encoding}}
wire_type: {{wire_type}}
## Examples
- value: {{example_value_1}}
  note: "{{example_note_1}}"
- value: {{example_value_2}}
  note: "{{example_note_2}}"
## Keywords
{{keyword_1}}, {{keyword_2}}, {{keyword_3}}
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
| Domain | type def construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_input_schema]] | sibling | 0.34 |
| [[bld_output_template_runtime_rule]] | sibling | 0.31 |
| [[bld_knowledge_card_type_def]] | upstream | 0.31 |
| [[bld_output_template_golden_test]] | sibling | 0.30 |
| [[bld_output_template_skill]] | sibling | 0.30 |
| [[bld_output_template_feature_flag]] | sibling | 0.30 |
| [[bld_output_template_embedding_config]] | sibling | 0.30 |
| [[bld_output_template_function_def]] | sibling | 0.30 |
| [[bld_output_template_output_validator]] | sibling | 0.29 |
| [[p11_qg_type_def]] | downstream | 0.29 |
