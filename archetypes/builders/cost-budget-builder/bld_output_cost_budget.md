---
kind: output_template
id: bld_output_template_cost_budget
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a cost_budget artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.0
title: "Output Template Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, output_template, P09]
tldr: "Fill-in template for cost_budget artifacts: frontmatter + 4 required body sections."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_cost_budget
  - bld_instruction_cost_budget
  - bld_schema_cost_budget
  - p03_sp_cost_budget_builder
  - p11_qg_cost_budget
  - p10_lr_cost_budget_builder
  - bld_architecture_cost_budget
  - bld_knowledge_card_cost_budget
  - bld_config_cost_budget
  - cost-budget-builder
---

# Output Template: cost_budget
```yaml
id: p09_cb_{{name_slug}}
kind: cost_budget
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{global_or_provider_or_model}}"
providers:
  - {{provider_1}}
  - {{provider_2}}
quality: null
tags: [cost_budget, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_budget_covers_max_200ch}}"
currency: {{USD|token_units}}
reset_policy: {{daily|weekly|monthly|rolling_7d|rolling_30d|none}}
alert_enabled: {{true|false}}
total_budget: {{number_or_null}}
overage_action: {{block|warn|log}}
```
## Overview
`{{what_scope_why_these_limits_1_to_2_sentences}}`
`{{who_enforces_these_limits}}`
## Budget Catalog
| Provider | Model | Token Limit | USD Limit | Alert % | Reset | Overage Action |
|----------|-------|-------------|-----------|---------|-------|----------------|
| `{{provider_1}}` | {{model_or_star}} | {{tokens_or_null}} | {{usd_or_null}} | {{warn_pct}}% | `{{reset_policy}}` | {{block|warn|log}} |
| `{{provider_2}}` | {{model_or_star}} | {{tokens_or_null}} | {{usd_or_null}} | {{warn_pct}}% | `{{reset_policy}}` | {{block|warn|log}} |
## Alert Policy
| Threshold | Level | Channel | Action |
|-----------|-------|---------|--------|
| `{{warn_pct}}`% | warn | {{log|email|webhook|pagerduty}} | `{{action_description}}` |
| 100% | block | `{{channel}}` | `{{action_description}}` |
Escalation: `{{who_is_notified_and_how}}`
## Overage Rules
- Breach behavior: `{{what_happens_on_limit_hit}}`
- Grace period: `{{grace_period_or_none}}`
- Increase request: `{{how_to_request_higher_limit}}`
## References
- `{{reference_1}}`
- `{{reference_2}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_cost_budget]] | downstream | 0.55 |
| [[bld_instruction_cost_budget]] | upstream | 0.47 |
| [[bld_schema_cost_budget]] | downstream | 0.46 |
| [[p03_sp_cost_budget_builder]] | upstream | 0.45 |
| [[p11_qg_cost_budget]] | downstream | 0.39 |
| [[p10_lr_cost_budget_builder]] | downstream | 0.34 |
| [[bld_architecture_cost_budget]] | downstream | 0.34 |
| [[bld_knowledge_card_cost_budget]] | upstream | 0.34 |
| [[bld_config_cost_budget]] | downstream | 0.33 |
| [[cost-budget-builder]] | downstream | 0.32 |
