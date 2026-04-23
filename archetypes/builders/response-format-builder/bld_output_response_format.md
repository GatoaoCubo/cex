---
kind: output_template
id: bld_output_template_response_format
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for response_format production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.1
title: "Output Template Response Format"
version: "1.0.0"
author: n03_builder
tags: [response_format, builder, examples]
tldr: "Golden and anti-examples for response format construction, demonstrating ideal structure and common pitfalls."
domain: "response format construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_response_format
  - bld_output_template_validation_schema
  - response-format-builder
  - bld_output_template_golden_test
  - bld_schema_response_format
  - bld_output_template_action_prompt
  - bld_knowledge_card_response_format
  - bld_config_response_format
  - bld_output_template_input_schema
  - bld_architecture_response_format
---

# Output Template: response_format
```yaml
id: p05_rf_{{format_slug}}
kind: response_format
pillar: P05

title: "Response Format: {{format_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"

author: "{{who_produced}}"
target_kind: "{{artifact_kind_or_task}}"
format_type: "{{json_or_yaml_or_markdown_or_csv_or_plaintext}}"
injection_point: "{{system_prompt_or_user_message}}"

sections: [{{section_1}}, {{section_2}}, {{section_3}}]
sections_count: {{integer_gte_1}}
domain: "{{domain_value}}"
quality: null

tags: [response-format, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
example_output: "see body"
composable: {{true_or_false}}

density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{target_kind_builder}}"
  related: [{{related_artifact_refs}}]
## Format Overview
{{what_structure_this_defines_and_for_what_task}}
## Sections
| # | Section | Description | Required | Constraints |
|---|---------|-------------|----------|-------------|
| 1 | {{section_1}} | {{description}} | {{yes/no}} | {{constraints}} |
| 2 | {{section_2}} | {{description}} | {{yes/no}} | {{constraints}} |
| 3 | {{section_3}} | {{description}} | {{yes/no}} | {{constraints}} |
## Example Output
````{{format_type}}`
`{{complete_example_showing_expected_shape}}`
```
## Injection Instructions
1. **Point**: {{system_prompt_or_user_message}}
2. **Position**: {{where_in_the_prompt}}
3. **Template**: "Respond using the following format: {{format_description}}"
4. **Composable**: {{true/false}} — {{explanation}}
## References
1. {{reference_1}}
2. {{reference_2}}
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | response format construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_response_format]] | downstream | 0.47 |
| [[bld_output_template_validation_schema]] | sibling | 0.40 |
| [[response-format-builder]] | related | 0.38 |
| [[bld_output_template_golden_test]] | sibling | 0.37 |
| [[bld_schema_response_format]] | downstream | 0.36 |
| [[bld_output_template_action_prompt]] | sibling | 0.33 |
| [[bld_knowledge_card_response_format]] | related | 0.31 |
| [[bld_config_response_format]] | downstream | 0.31 |
| [[bld_output_template_input_schema]] | sibling | 0.31 |
| [[bld_architecture_response_format]] | downstream | 0.30 |
