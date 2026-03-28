---
kind: output_template
id: bld_output_template_feature_flag
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a feature_flag artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: feature_flag
```yaml
id: p09_ff_{{feature_slug}}
kind: feature_flag
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
flag_name: "{{human_readable_flag_name}}"
default_state: {{on|off}}
category: {{release|experiment|ops|permission}}
rollout_percentage: {{0_to_100}}
quality: null
tags: [feature_flag, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_flag_controls_max_200ch}}"
owner: "{{responsible_team_or_person}}"
expires: "{{YYYY-MM-DD_or_null}}"
targeting: "{{targeting_strategy_summary}}"
```
## Flag Specification
{{feature_description_and_current_state}}
{{kill_switch_behavior_if_ops}}
## Rollout Strategy
{{rollout_stages_with_percentages_and_timeline}}
## Lifecycle
{{lifecycle_stages_create_test_ramp_full_retire}}
## References
- {{reference_1}}
```
