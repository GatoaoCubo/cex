---
kind: output_template
id: bld_output_template_reward_signal
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a reward_signal artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_this_reward_signal_measures_1_to_2_sentences}}
{{who_uses_it_and_primary_improvement_loop}}
## Signal Design
- Type: {{signal_type}} — {{why_this_type_fits_the_domain}}
- Scale: {{scale}} — {{what_high_and_low_values_mean}}
- Model: {{model}} — {{why_this_model_produces_reliable_reward}}
- Computation: {{how_score_is_computed_step_by_step}}
- Frequency: {{frequency}} — {{when_evaluation_runs}}
- Aggregation: {{aggregation}} — {{how_multi_score_windows_combine}}
## Criteria
| Dimension | Weight | Low Score | High Score |
|-----------|--------|-----------|------------|
| {{dim_1}} | {{w1}} | {{low_example_1}} | {{high_example_1}} |
| {{dim_2}} | {{w2}} | {{low_example_2}} | {{high_example_2}} |
| {{dim_3}} | {{w3}} | {{low_example_3}} | {{high_example_3}} |
Baseline: {{baseline}} — {{what_happens_when_score_falls_below}}
## Application
- Loop: {{rlhf|dpo|filtering|monitoring}} — {{how_signal_feeds_improvement}}
- Consumer: {{who_reads_this_signal_and_what_action_they_take}}
- Cadence: {{how_often_scores_are_collected_and_applied}}
