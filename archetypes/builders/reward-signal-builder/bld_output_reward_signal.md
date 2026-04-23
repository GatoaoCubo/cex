---
kind: output_template
id: bld_output_template_reward_signal
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a reward_signal artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Reward Signal"
version: "1.0.0"
author: n03_builder
tags: [reward_signal, builder, examples]
tldr: "Golden and anti-examples for reward signal construction, demonstrating ideal structure and common pitfalls."
domain: "reward signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_reward_signal
  - p03_sp_reward_signal_builder
  - bld_instruction_reward_signal
  - p11_qg_reward_signal
  - bld_schema_reward_signal
  - bld_examples_reward_signal
  - reward-signal-builder
  - bld_config_reward_signal
  - bld_knowledge_card_reward_signal
  - bld_output_template_llm_judge
---

# Output Template: reward_signal
```yaml
id: p11_rs_{{signal_slug}}
kind: reward_signal
pillar: P11

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

name: "{{human_readable_signal_name}}"
signal_type: {{scalar|preference|critique|comparative|implicit}}
scale: "{{0-1|0-10|binary|-1_to_1|costm_range}}"
model: "{{model_id_or_human}}"

quality: null
tags: [reward_signal, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
criteria:

  - "{{dimension_1}}"
  - "{{dimension_2}}"
  - "{{dimension_3}}"
frequency: {{per_turn|per_task|per_session|on_demand}}

aggregation: {{mean|weighted_mean|min|max|last}}
baseline: {{float_within_scale_range}}
description: "{{what_signal_measures_max_200ch}}"
```
## Overview
`{{what_this_reward_signal_measures_1_to_2_sentences}}`
`{{who_uses_it_and_primary_improvement_loop}}`
## Signal Design
1. Type: `{{signal_type}}` — `{{why_this_type_fits_the_domain}}`
2. Scale: `{{scale}}` — `{{what_high_and_low_values_mean}}`
3. Model: `{{model}}` — `{{why_this_model_produces_reliable_reward}}`
4. Computation: `{{how_score_is_computed_step_by_step}}`
5. Frequency: `{{frequency}}` — `{{when_evaluation_runs}}`
6. Aggregation: `{{aggregation}}` — `{{how_multi_score_windows_combine}}`
## Criteria
| Dimension | Weight | Low Score | High Score |
|-----------|--------|-----------|------------|
| `{{dim_1}}` | {{w1}} | {{low_example_1}} | `{{high_example_1}}` |
| `{{dim_2}}` | {{w2}} | {{low_example_2}} | `{{high_example_2}}` |
| `{{dim_3}}` | {{w3}} | {{low_example_3}} | `{{high_example_3}}` |
Baseline: `{{baseline}}` — `{{what_happens_when_score_falls_below}}`
## Application
1. Loop: {{rlhf|dpo|filtering|monitoring}} — `{{how_signal_feeds_improvement}}`
2. Consumer: `{{who_reads_this_signal_and_what_action_they_take}}`
3. Cadence: `{{how_often_scores_are_collected_and_applied}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | reward signal construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_reward_signal]] | downstream | 0.50 |
| [[p03_sp_reward_signal_builder]] | downstream | 0.49 |
| [[bld_instruction_reward_signal]] | upstream | 0.48 |
| [[p11_qg_reward_signal]] | downstream | 0.47 |
| [[bld_schema_reward_signal]] | downstream | 0.44 |
| [[bld_examples_reward_signal]] | downstream | 0.42 |
| [[reward-signal-builder]] | downstream | 0.38 |
| [[bld_config_reward_signal]] | downstream | 0.36 |
| [[bld_knowledge_card_reward_signal]] | upstream | 0.36 |
| [[bld_output_template_llm_judge]] | sibling | 0.30 |
