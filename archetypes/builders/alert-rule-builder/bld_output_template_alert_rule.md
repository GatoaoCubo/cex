---
id: bld_tpl_alert_rule
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 5.4
tags: [alert_rule, template, output]
title: "Output Template: alert_rule"
density_score: 1.0
updated: "2026-04-17"
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
