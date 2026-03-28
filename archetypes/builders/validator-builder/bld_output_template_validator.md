---
kind: output_template
id: bld_output_template_validator
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a validator
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{plain_language_description_of_what_is_checked}}
## Conditions
| # | Field | Operator | Value | Target |
|---|-------|----------|-------|--------|
| 1 | {{field}} | {{op}} | {{val}} | {{target}} |
| 2 | {{field}} | {{op}} | {{val}} | {{target}} |
## Error Handling
- **Message**: {{error_message}}
- **Severity**: {{severity}}
- **Auto-fix**: {{yes_no_and_how}}
- **Remediation**: {{steps_to_fix_manually}}
## Bypass Policy
- **Conditions**: {{when_bypass_is_allowed}}
- **Approver**: {{who_can_approve}}
- **Audit**: always logged
## References
- {{reference_1}}
- {{reference_2}}
