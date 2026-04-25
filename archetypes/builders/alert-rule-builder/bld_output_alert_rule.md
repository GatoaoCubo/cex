---
id: bld_tpl_alert_rule
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 7.5
tags: [alert_rule, template, output]
title: "Output Template: alert_rule"
author: builder
tldr: "Alert Rule prompt: output template, formatting rules, and structure"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p06_security_validation_schema
  - p11_qg_validator
  - extraction_gate_severity
  - bld_knowledge_card_guardrail
  - p03_ins_validator
  - bld_output_template_validator
  - bld_output_template_guardrail
  - p10_lr_guardrail_builder
  - bld_memory_validator
  - p03_sp_validator-builder
---
# Output Template: alert_rule
```markdown
---
id: ar_{{system_snake}}_{{metric_snake}}
kind: alert_rule
pillar: P09
title: "{{SystemName}} {{MetricName}} {{Condition}} Alert"
version: 1.0.0
quality: null
alert_name: {{PascalCaseAlertName}}
severity: {{critical|warning|info}}
for_duration: "{{ISO_duration}}"
metric_expression: "{{PromQL_or_logical_expression}}"
routing: "{{team_channel_or_policy}}"
tags: [{{system}}, {{metric}}, alert-rule]
---

# {{PascalCaseAlertName}}

## Condition
| Field | Value |
|-------|-------|
| metric | {{metric_name}} |
| expression | `{{metric_expression}}` |
| threshold | {{numeric_value}} {{unit}} |
| for_duration | {{ISO_duration}} |

## Severity & Routing
| Field | Value |
|-------|-------|
| severity | {{critical/warning/info}} |
| routing | {{target}} |
| on_call | {{team_or_person}} |

## Response
- **Automated**: {{auto_action or "none"}}
- **Runbook**: {{runbook_url or "TBD"}}
- **Remediation**: {{steps_or_link}}

## Labels (Prometheus)
```yaml
severity: {{severity}}
team: {{team}}
service: {{service}}
```

## Output Template Checklist

- Verify output format matches target kind schema
- Validate all frontmatter fields are present in template
- Cross-reference with eval gate for completeness
- Test template rendering with sample data before publishing

## Output Pattern

```yaml
# Output validation
format_match: true
frontmatter_complete: true
eval_gate_aligned: true
sample_rendered: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_security_validation_schema]] | downstream | 0.34 |
| [[p11_qg_validator]] | downstream | 0.32 |
| [[extraction_gate_severity]] | related | 0.29 |
| [[bld_knowledge_card_guardrail]] | upstream | 0.27 |
| [[p03_ins_validator]] | related | 0.27 |
| [[bld_output_template_validator]] | downstream | 0.26 |
| [[bld_output_template_guardrail]] | downstream | 0.25 |
| [[p10_lr_guardrail_builder]] | downstream | 0.25 |
| [[bld_memory_validator]] | downstream | 0.25 |
| [[p03_sp_validator-builder]] | related | 0.24 |
