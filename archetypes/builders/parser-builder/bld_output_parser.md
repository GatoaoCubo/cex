---
kind: output_template
id: bld_output_template_parser
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a parser artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Parser"
version: "1.0.0"
author: n03_builder
tags: [parser, builder, examples]
tldr: "Golden and anti-examples for parser construction, demonstrating ideal structure and common pitfalls."
domain: "parser construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_parser
  - p03_ins_parser
  - bld_examples_parser
  - p11_qg_parser
  - parser-builder
  - bld_output_template_input_schema
  - bld_output_template_formatter
  - p03_sp_parser_builder
  - bld_architecture_parser
  - bld_knowledge_card_parser
---

# Output Template: parser
```yaml
id: p05_parser_{{parser_slug}}
kind: parser
pillar: P05

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

input_format: "{{text|json|html|xml|yaml|csv|log|mixed}}"
output_format: "{{json|yaml|csv|markdown|typed_object}}"
extraction_count: {{integer_matching_table}}
domain: "{{parser_domain}}"

quality: null
tags: [parser, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
error_strategy: "{{skip|default|fail|retry}}"

streaming: {{true|false}}
chunking: {{true|false}}
chunk_size: {{integer_bytes_or_null}}
normalization: [{{normalize_step_1}}, {{normalize_step_2}}]

keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
density_score: {{0.80_to_1.00}}
```
## Extraction Rules
| Name | Target | Method | Pattern | Required | Default |
|------|--------|--------|---------|----------|---------|
| `{{rule_name_1}}` | {{target_field_1}} | {{method_1}} | {{pattern_1}} | {{true|false}} | `{{default_or_dash}}` |
| `{{rule_name_2}}` | {{target_field_2}} | {{method_2}} | {{pattern_2}} | {{true|false}} | `{{default_or_dash}}` |
## Input Specification
Format: `{{input_format}}`
Structure: `{{description_of_expected_input}}`
Example:
``{{input_format}}`
{{sample_input}}
```
## Output Specification
Format: `{{output_format}}`
Schema:
``{{output_format}}`
{{output_schema_with_types}}
```
Example:
``{{output_format}}`
{{sample_output}}
```
## Error Handling
Strategy: `{{error_strategy}}`
1. On extraction failure: `{{failure_behavior}}`
2. On malformed input: `{{malformed_behavior}}`
3. On partial match: `{{partial_behavior}}`
Fallback extraction: `{{fallback_method_or_none}}`
## Normalization
Pipeline (applied in order after extraction):
1. `{{normalize_step_1}}`: `{{description}}`
2. `{{normalize_step_2}}`: `{{description}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | parser construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_parser]] | downstream | 0.48 |
| [[p03_ins_parser]] | upstream | 0.45 |
| [[bld_examples_parser]] | downstream | 0.40 |
| [[p11_qg_parser]] | downstream | 0.39 |
| [[parser-builder]] | related | 0.37 |
| [[bld_output_template_input_schema]] | sibling | 0.35 |
| [[bld_output_template_formatter]] | sibling | 0.35 |
| [[p03_sp_parser_builder]] | upstream | 0.34 |
| [[bld_architecture_parser]] | downstream | 0.33 |
| [[bld_knowledge_card_parser]] | upstream | 0.30 |
