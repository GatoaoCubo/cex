---
kind: output_template
id: bld_output_template_optimizer
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for optimizer production
pattern: derives from SCHEMA.md — no extra fields, no instructions
quality: 9.1
title: "Output Template Optimizer"
version: "1.0.0"
author: n03_builder
tags: [optimizer, builder, examples]
tldr: "Golden and anti-examples for optimizer construction, demonstrating ideal structure and common pitfalls."
domain: "optimizer construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_optimizer
  - bld_examples_optimizer
  - bld_schema_optimizer
  - p03_sp_optimizer_builder
  - p11_qg_optimizer
  - bld_memory_optimizer
  - optimizer-builder
  - bld_knowledge_card_optimizer
  - bld_config_optimizer
  - bld_architecture_optimizer
---

# Output Template: optimizer
```yaml
id: p11_opt_{{target_slug}}
kind: optimizer
pillar: P11
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{process_domain}}"
quality: null
tags: [optimizer, {{domain}}, {{frequency}}]
tldr: "{{one_sentence_what_is_optimized_and_how}}"
density_score: {{0.80_to_1.00}}
target: "{{process_being_optimized}}"
metric:
  name: "{{metric_name}}"
  unit: "{{unit_of_measurement}}"
  direction: "{{minimize_or_maximize}}"
action:
  type: "{{tune_prune_scale_replace_restructure}}"
  description: "{{what_action_is_taken}}"
  automated: {{true_or_false}}
threshold:
  trigger: {{float_when_action_fires}}
  target: {{float_desired_state}}
  critical: {{float_emergency_level}}
frequency: "{{continuous_hourly_daily_weekly_monthly}}"
baseline:
  value: {{float_starting_value}}
  measured_at: "{{YYYY-MM-DD}}"
  conditions: "{{context_when_baseline_was_measured}}"
improvement:
  current: {{float_current_value}}
  target: {{float_goal_value}}
  history:
    - date: "{{YYYY-MM-DD}}"
      value: {{float}}
cost:
  compute: {{float_cpu_or_memory_overhead}}
  time: {{float_seconds_per_optimization_cycle}}
  risk: "{{low_medium_high_description}}"
risk:
  level: "{{low_medium_high}}"
  mitigation: "{{how_risk_is_mitigated}}"
monitoring:
  dashboard: "{{dashboard_name_or_url}}"
  alerts:
    - "{{alert_condition_1}}"
    - "{{alert_condition_2}}"
  reporting: "{{reporting_cadence_and_format}}"
## Target Process
{{scope_of_what_is_optimized}}
{{boundaries_what_is_in_scope_and_out}}
## Metrics
| Metric | Unit | Direction | Trigger | Target | Critical |
|--------|------|-----------|---------|--------|----------|
| {{primary_metric}} | {{unit}} | {{minimize_maximize}} | {{trigger}} | {{target}} | {{critical}} |
### Secondary Metrics
| Metric | Unit | Purpose |
|--------|------|---------|
| {{secondary_1}} | {{unit}} | {{why_tracked}} |
| {{secondary_2}} | {{unit}} | {{why_tracked}} |
## Actions
| Trigger Condition | Action Type | Description | Automated |
|-------------------|-------------|-------------|-----------|
| {{condition_1}} | {{type}} | {{what_happens}} | {{yes_no}} |
| {{condition_2}} | {{type}} | {{what_happens}} | {{yes_no}} |
### Rollback
{{rollback_procedure_if_action_causes_regression}}
## Risk Assessment
| Risk | Level | Mitigation |
|------|-------|-----------|
| {{risk_1}} | {{low_medium_high}} | {{mitigation}} |
| {{risk_2}} | {{low_medium_high}} | {{mitigation}} |
Cost: compute={{compute_overhead}}, time={{time_per_cycle}}s
## Monitoring
- Dashboard: {{dashboard}}
- Alerts: {{alert_list}}
- Reporting: {{cadence_and_format}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_optimizer]] | upstream | 0.44 |
| [[bld_examples_optimizer]] | downstream | 0.42 |
| [[bld_schema_optimizer]] | downstream | 0.36 |
| [[p03_sp_optimizer_builder]] | upstream | 0.35 |
| [[p11_qg_optimizer]] | downstream | 0.31 |
| [[bld_memory_optimizer]] | downstream | 0.31 |
| [[optimizer-builder]] | downstream | 0.29 |
| [[bld_knowledge_card_optimizer]] | upstream | 0.28 |
| [[bld_config_optimizer]] | downstream | 0.27 |
| [[bld_architecture_optimizer]] | downstream | 0.27 |
