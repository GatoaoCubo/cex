---
kind: output_template
id: bld_output_template_validator
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a validator
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Validator"
version: "1.0.0"
author: n03_builder
tags: [validator, builder, examples]
tldr: "Golden and anti-examples for validator construction, demonstrating ideal structure and common pitfalls."
domain: "validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: validator
```yaml
id: p06_val_{{rule_slug}}
kind: validator
pillar: P06

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

rule: "{{human_readable_rule_name}}"
conditions:
  - field: "{{field_name}}"
    operator: "{{operator}}"

    value: "{{expected_value}}"
    target: "{{frontmatter|body|filename}}"
error_message: "{{actionable_error_text}}"
severity: "{{error|warning|info}}"

auto_fix: {{true|false}}
pre_commit: {{true|false}}
threshold: {{number_or_null}}
bypass:

  conditions: ["{{bypass_condition}}"]
  approver: "{{approver_role}}"
  audit: true
logging: {{true|false}}

domain: "{{artifact_kind_this_validates}}"
quality: null
tags: [validator, {{domain_tag}}, {{rule_tag}}]
tldr: "{{dense_summary_max_160ch}}"

density_score: {{0.80_to_1.00}}
```
## Rule Definition
`{{plain_language_description_of_what_is_checked}}`
## Conditions
| # | Field | Operator | Value | Target |
|---|-------|----------|-------|--------|
| 1 | `{{field}}` | {{op}} | {{val}} | `{{target}}` |
| 2 | `{{field}}` | {{op}} | {{val}} | `{{target}}` |
## Error Handling
1. **Message**: `{{error_message}}`
2. **Severity**: `{{severity}}`
3. **Auto-fix**: `{{yes_no_and_how}}`
4. **Remediation**: `{{steps_to_fix_manually}}`
## Bypass Policy
1. **Conditions**: `{{when_bypass_is_allowed}}`
2. **Approver**: `{{who_can_approve}}`
3. **Audit**: always logged
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | validator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
