---
kind: output_template
id: bld_output_template_regression_check
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a regression_check artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Regression Check"
version: "1.0.0"
author: n03_builder
tags: [regression_check, builder, examples]
tldr: "Golden and anti-examples for regression check construction, demonstrating ideal structure and common pitfalls."
domain: "regression check construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: regression_check
```yaml
id: p07_rc_{{check_slug}}
kind: regression_check
pillar: P07

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

name: "{{human_readable_check_name}}"
baseline_ref: "{{experiment_id_or_version_tag}}"
threshold: {{numeric_value}}
metrics:

  - {{metric_name_1}}
  - {{metric_name_2}}
quality: null
tags: [regression_check, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
description: "{{what_this_check_compares_max_200ch}}"
tool: {{braintrust|promptfoo|langsmith|deepeval|costm}}
comparison_mode: {{relative|absolute}}

fail_action: {{block|warn|log}}
notify: [{{owner_or_channel_1}}, {{owner_or_channel_2}}]
cadence: {{on_pr|on_deploy|daily|on_demand}}
scope: "{{which_prompt_model_or_pipeline}}"
```
## Overview
`{{what_system_this_check_governs_1_to_2_sentences}}`
`{{who_owns_it_and_when_it_runs}}`
## Baseline
**baseline_ref**: `{{experiment_id_or_version_tag}}`
`{{what_this_baseline_represents}}`
`{{when_it_was_captured_and_conditions}}`

**Update policy**: `{{when_to_rotate_baseline}}`
## Metrics
### `{{metric_name_1}}`
1. **Definition**: `{{what_this_metric_measures}}`
2. **Method**: `{{how_it_is_measured_in_tool}}`
3. **Threshold**: `{{threshold_value}}` {{percent|absolute}} ({{higher|lower}} is better)
4. **Direction**: {{increase|decrease}} signals regression
### `{{metric_name_2}}`
1. **Definition**: `{{what_this_metric_measures}}`
2. **Method**: `{{how_it_is_measured_in_tool}}`
3. **Threshold**: `{{threshold_value}}` {{percent|absolute}} ({{higher|lower}} is better)
4. **Direction**: {{increase|decrease}} signals regression
## Failure Protocol
1. **fail_action**: {{block|warn|log}}
2. **Notify**: `{{who_gets_notified}}`
3. **Remediation**: `{{steps_to_investigate_and_fix}}`
4. **Escalation**: `{{if_not_resolved_in_X_time}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | regression check construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
