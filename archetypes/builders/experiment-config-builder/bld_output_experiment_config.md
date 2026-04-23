---
kind: output_template
id: bld_output_template_experiment_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an experiment_config artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.1
title: "Output Template Experiment Config"
version: "1.0.0"
author: n03_builder
tags: [experiment_config, builder, output_template, P09]
tldr: "Fill-in template for experiment_config artifacts: frontmatter + 6 required body sections."
domain: "experiment config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_experiment_config
  - p11_qg_experiment_config
  - bld_schema_experiment_config
  - bld_instruction_experiment_config
  - bld_config_experiment_config
  - bld_output_template_quality_gate
  - bld_knowledge_card_experiment_config
  - bld_architecture_experiment_config
  - p01_kc_experiment_config
  - p03_sp_experiment_config_builder
---

# Output Template: experiment_config
```yaml
id: p09_ec_{{name_slug}}
kind: experiment_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
hypothesis: "{{falsifiable_hypothesis_max_200ch}}"
variants:
  - control
  - {{treatment_1}}
  - {{treatment_2_if_any}}
primary_metric: "{{single_kpi_name}}"
guardrail_metrics:
  - {{guardrail_metric_1}}
  - {{guardrail_metric_2}}
traffic_split:
  control: {{pct_integer}}
  {{treatment_1}}: {{pct_integer}}
status: {{draft|running|paused|concluded}}
significance_threshold: {{0.05}}
min_detectable_effect: "{{e.g. +2pct relative}}"
sample_size_target: {{N_per_variant}}
duration_days: {{N}}
segment: "{{all|power_users|new_users|custom_segment}}"
quality: null
tags: [experiment_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Overview
`{{what_is_being_tested_and_why_1_to_2_sentences}}`
`{{what_decision_this_experiment_enables}}`
## Variants
| Variant | Type | Description | Key Changes |
|---------|------|-------------|-------------|
| control | control | `{{baseline_description}}` | Baseline -- no changes |
| `{{treatment_1}}` | treatment | {{treatment_description}} | `{{parameter_changes}}` |
| `{{treatment_2_if_any}}` | treatment | {{treatment_description}} | `{{parameter_changes}}` |
## Traffic Split
| Variant | Allocation | Segment |
|---------|-----------|---------|
| control | `{{pct}}`% | `{{segment}}` |
| `{{treatment_1}}` | {{pct}}% | `{{segment}}` |
Allocation total: 100%. `{{hold_out_rule_if_any}}`
## Metrics
### Primary Metric
| Metric | Direction | Winning Threshold |
|--------|-----------|-------------------|
| `{{primary_metric}}` | {{higher_is_better|lower_is_better}} | {{e.g. +3pct vs control}} |
### Guardrail Metrics
| Metric | Acceptable Limit | Action if Breached |
|--------|-----------------|-------------------|
| `{{guardrail_1}}` | {{e.g. p99_latency <= 500ms}} | `{{pause_experiment}}` |
| `{{guardrail_2}}` | {{e.g. error_rate < 1pct}} | `{{pause_experiment}}` |
## Statistical Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| Significance threshold | {{0.05}} | alpha = {{5pct}} |
| Min detectable effect | {{+2pct relative}} | `{{baseline_rate}}` |
| Sample size (per variant) | `{{N}}` | `{{power_calculation_method}}` |
| Duration | `{{N}}` days | `{{estimated_daily_samples}}` samples/day |
## Lifecycle
| Field | Value |
|-------|-------|
| Status | {{draft|running|paused|concluded}} |
| Created | {{YYYY-MM-DD}} |
| Launch target | {{YYYY-MM-DD}} |
| Conclusion criteria | `{{statistical_significance_AND_min_runtime}}` |
| Decision owner | `{{team_or_role}}` |
## References
- `{{reference_1}}`
- `{{reference_2}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_experiment_config]] | downstream | 0.53 |
| [[p11_qg_experiment_config]] | downstream | 0.43 |
| [[bld_schema_experiment_config]] | downstream | 0.43 |
| [[bld_instruction_experiment_config]] | upstream | 0.39 |
| [[bld_config_experiment_config]] | downstream | 0.38 |
| [[bld_output_template_quality_gate]] | sibling | 0.33 |
| [[bld_knowledge_card_experiment_config]] | upstream | 0.33 |
| [[bld_architecture_experiment_config]] | downstream | 0.32 |
| [[p01_kc_experiment_config]] | downstream | 0.29 |
| [[p03_sp_experiment_config_builder]] | upstream | 0.28 |
