---
quality: 7.8
quality: 7.4
id: bld_output_template_slo_definition
kind: knowledge_card
pillar: P05
title: "Output Template: slo_definition"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
tags: [output_template, slo_definition, P09]
llm_function: PRODUCE
tldr: "Canonical output template for slo_definition artifacts."
density_score: null
related:
  - bld_knowledge_card_enterprise_sla
  - bld_output_template_enterprise_sla
  - bld_collaboration_rate_limit_config
  - p11_qg_enterprise_sla
---

# Output Template: slo_definition

## Frontmatter Template
```yaml
---
id: p09_slo_{{name_slug}}
kind: slo_definition
pillar: P09
version: 1.0.0
service_name: "{{service_name}}"
sli_type: {{sli_type}}
target_percent: {{target_percent}}
window_days: {{window_days}}
error_budget_minutes: {{error_budget_minutes}}
error_budget_policy: {{error_budget_policy}}
owner: "{{owner}}"
domain: "{{domain}}"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
quality: null
tags: [slo_definition, {{domain}}, {{sli_type}}]
tldr: "{{service_name}} {{sli_type}} SLO: {{target_percent}}% over {{window_days}}d rolling window"
---
```

## Body Template
```markdown
# {{service_name}} SLO

## SLI Definition
- **Type**: {{sli_type}}
- **Metric**: `{{sli_metric_query}}`
- **Denominator**: {{denominator_description}}
- **Measurement**: {{measurement_method}}

## Target
- **Target**: {{target_percent}}% over {{window_days}}-day rolling window
- **Error Budget**: {{error_budget_minutes}} minutes

## Error Budget
| Period | Allowed Downtime | Burn Rate Trigger |
|--------|-----------------|-------------------|
| 1h fast burn | {{budget_1h_minutes}}m | {{burn_rate_14x}}x |
| 6h slow burn | {{budget_6h_minutes}}m | {{burn_rate_6x}}x |

## Alerting Policy
- **Page on**: burn rate >= {{fast_burn_threshold}} over 1h
- **Ticket on**: burn rate >= {{slow_burn_threshold}} over 6h
- **Budget exhaustion**: {{error_budget_policy}}
- **Owner**: {{owner}}
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
| [[bld_knowledge_card_enterprise_sla]] | sibling | 0.23 |
| [[bld_output_template_enterprise_sla]] | related | 0.19 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.16 |
| [[p11_qg_enterprise_sla]] | downstream | 0.16 |
