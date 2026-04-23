---
kind: output_template
id: bld_output_template_validation_schema
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for validation_schema production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.1
title: "Output Template Validation Schema"
version: "1.0.0"
author: n03_builder
tags: [validation_schema, builder, examples]
tldr: "Golden and anti-examples for validation schema construction, demonstrating ideal structure and common pitfalls."
domain: "validation schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_validation_schema
  - p06_vs_frontmatter
  - bld_schema_validation_schema
  - bld_output_template_input_schema
  - bld_output_template_golden_test
  - bld_output_template_response_format
  - p11_qg_validation_schema
  - bld_collaboration_validation_schema
  - validation-schema-builder
  - p03_ins_validation_schema
---

# Output Template: validation_schema
```yaml
id: p06_vs_{{scope_slug}}
kind: validation_schema
pillar: P06

title: "Validation Schema: {{schema_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"

author: "{{who_produced}}"
target_kind: "{{artifact_kind_validated}}"
format: "{{json_or_yaml}}"
fields_count: {{integer_gte_1}}

on_failure: "{{reject_or_warn_or_auto_fix}}"
strict: {{true_or_false}}
domain: "{{domain_value}}"
quality: null

tags: [validation-schema, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
coercion: {{true_or_false}}
error_template: "{{field}} failed: {{reason}}"

density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{target_kind_builder}}"
  related: [{{related_artifact_refs}}]
## Schema Overview
{{what_this_validates_and_why}}
## Fields
| Field | Type | Required | Constraints | Error message |
|-------|------|----------|-------------|---------------|
| {{field_1}} | {{type}} | {{yes/no}} | {{constraints}} | {{error_msg}} |
| {{field_2}} | {{type}} | {{yes/no}} | {{constraints}} | {{error_msg}} |
| {{field_3}} | {{type}} | {{yes/no}} | {{constraints}} | {{error_msg}} |
## Failure Handling
1. **on_failure**: {{reject/warn/auto_fix}}
2. **strict**: {{true/false}} — {{explanation}}
3. **coercion**: {{true/false}} — {{explanation}}
4. **error_template**: "{{field}} failed: {{reason}}"
5. **remediation**: {{how_to_fix_common_failures}}
## Integration
1. **Pipeline position**: after LLM generation, before acceptance
2. **Applied by**: {{system_component}}
3. **Input**: raw LLM output ({{format}})
4. **Output**: validated artifact or error report
## References
1. {{reference_1}}
2. {{reference_2}}
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | validation schema construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_validation_schema]] | downstream | 0.49 |
| [[p06_vs_frontmatter]] | downstream | 0.44 |
| [[bld_schema_validation_schema]] | downstream | 0.40 |
| [[bld_output_template_input_schema]] | sibling | 0.39 |
| [[bld_output_template_golden_test]] | sibling | 0.37 |
| [[bld_output_template_response_format]] | sibling | 0.35 |
| [[p11_qg_validation_schema]] | downstream | 0.32 |
| [[bld_collaboration_validation_schema]] | downstream | 0.32 |
| [[validation-schema-builder]] | downstream | 0.31 |
| [[p03_ins_validation_schema]] | upstream | 0.30 |
