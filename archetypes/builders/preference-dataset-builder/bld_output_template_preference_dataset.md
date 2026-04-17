---
kind: output_template
id: bld_output_template_preference_dataset
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a preference_dataset artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: null
title: "Output Template Preference Dataset"
version: "1.0.0"
author: n03_builder
tags: [preference_dataset, builder, output_template]
tldr: "Fill {{vars}} to produce a preference_dataset artifact with training objective, pairs, and quality filters."
domain: "preference dataset construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Output Template: preference_dataset
```yaml
id: p11_pd_{{dataset_slug}}
kind: preference_dataset
pillar: P11
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
training_objective: {{rlhf|dpo|kto|constitutional|custom}}
preference_signal: "{{what_makes_chosen_better_than_rejected}}"
annotation_method: {{human|model_assisted|constitutional|hybrid}}
rater_count: {{int_per_pair}}
agreement_rate: {{float_0.0_to_1.0}}
domain: "{{task_domain}}"
language: "{{en|pt|etc}}"
total_pairs: {{int_target_or_actual}}
split_ratios:
  train: {{0.80}}
  eval: {{0.10}}
  test: {{0.10}}
source: "{{data_provenance}}"
quality: null
tags: [preference_dataset, {{domain_tag}}, {{objective_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Overview
`{{training_objective_and_domain_1_to_2_sentences}}`
`{{intended_use_and_scope}}`

## Annotation Protocol
`{{preference_criterion_definition}}`

| Chosen When | Rejected When |
|-------------|--------------|
| {{criterion_1_chosen}} | {{criterion_1_rejected}} |
| {{criterion_2_chosen}} | {{criterion_2_rejected}} |

Edge cases: `{{how_to_handle_ties_and_ambiguous_cases}}`

## Quality Filters
| Filter | Threshold | Action |
|--------|-----------|--------|
| agreement_rate | >= {{threshold}} | Exclude pairs below threshold |
| confidence | >= {{confidence_min}} | Flag low-confidence pairs for review |
| length_ratio | chosen/rejected != extreme ratio | Exclude length-biased pairs |
| {{custom_filter}} | {{custom_threshold}} | {{custom_action}} |

## Pairs
```yaml
pairs:
  - id: "{{pair_id_001}}"
    prompt: "{{instruction_or_conversation}}"
    chosen: "{{preferred_response}}"
    rejected: "{{dispreferred_response}}"
    metadata:
      rater_count: {{int}}
      agreement: {{float}}
      confidence: {{float}}
      tags: [{{tag_1}}, {{tag_2}}]
  - id: "{{pair_id_002}}"
    prompt: "{{instruction_or_conversation_2}}"
    chosen: "{{preferred_response_2}}"
    rejected: "{{dispreferred_response_2}}"
    metadata:
      rater_count: {{int}}
      agreement: {{float}}
      confidence: {{float}}
      tags: [{{tag_1}}]
```
