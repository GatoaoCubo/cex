---
kind: output_template
id: bld_output_template_validation_schema
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for validation_schema production
pattern: derives from SCHEMA.md — no extra fields
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
- **on_failure**: {{reject/warn/auto_fix}}
- **strict**: {{true/false}} — {{explanation}}
- **coercion**: {{true/false}} — {{explanation}}
- **error_template**: "{{field}} failed: {{reason}}"
- **remediation**: {{how_to_fix_common_failures}}
## Integration
- **Pipeline position**: after LLM generation, before acceptance
- **Applied by**: {{system_component}}
- **Input**: raw LLM output ({{format}})
- **Output**: validated artifact or error report
## References
- {{reference_1}}
- {{reference_2}}
```
