---
kind: output_template
id: bld_output_template_regression_check
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a regression_check artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
tool: {{braintrust|promptfoo|langsmith|deepeval|custom}}
comparison_mode: {{relative|absolute}}
fail_action: {{block|warn|log}}
notify: [{{owner_or_channel_1}}, {{owner_or_channel_2}}]
cadence: {{on_pr|on_deploy|daily|on_demand}}
scope: "{{which_prompt_model_or_pipeline}}"
```
## Overview
{{what_system_this_check_governs_1_to_2_sentences}}
{{who_owns_it_and_when_it_runs}}
## Baseline
**baseline_ref**: `{{experiment_id_or_version_tag}}`
{{what_this_baseline_represents}}
{{when_it_was_captured_and_conditions}}
**Update policy**: {{when_to_rotate_baseline}}
## Metrics
### {{metric_name_1}}
- **Definition**: {{what_this_metric_measures}}
- **Method**: {{how_it_is_measured_in_tool}}
- **Threshold**: {{threshold_value}} {{percent|absolute}} ({{higher|lower}} is better)
- **Direction**: {{increase|decrease}} signals regression
### {{metric_name_2}}
- **Definition**: {{what_this_metric_measures}}
- **Method**: {{how_it_is_measured_in_tool}}
- **Threshold**: {{threshold_value}} {{percent|absolute}} ({{higher|lower}} is better)
- **Direction**: {{increase|decrease}} signals regression
## Failure Protocol
- **fail_action**: {{block|warn|log}}
- **Notify**: {{who_gets_notified}}
- **Remediation**: {{steps_to_investigate_and_fix}}
- **Escalation**: {{if_not_resolved_in_X_time}}
