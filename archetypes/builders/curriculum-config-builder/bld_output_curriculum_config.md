---
kind: output_template
id: bld_output_curriculum_config
pillar: P05
llm_function: PRODUCE
purpose: Template for producing a curriculum_config artifact
quality: null
title: "Curriculum Config Builder - Output ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, output]
tldr: "Output template for curriculum config artifacts."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_curriculum_config
---

# Output Template: curriculum_config

```yaml
id: p07_cc_{{config_slug}}
kind: curriculum_config
pillar: P07
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
strategy: "{{easy_to_hard_or_self_paced_or_mixing}}"
difficulty_metric: "{{perplexity_or_length_or_complexity}}"
num_phases: {{integer}}
warmup_fraction: {{float}}
data_sources: [{{source_list}}]
domain: "{{domain_value}}"
quality: null
tags: [curriculum, training, {{strategy_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Strategy
`{{selected_approach_with_rationale}}`

## Data Sources
`{{sources_sizes_mixing_ratios}}`

## Difficulty Progression
`{{metric_definition_and_schedule}}`

## Schedule
`{{warmup_phases_annealing}}`

## Checkpoints
`{{evaluation_points_and_competence_gates}}`
