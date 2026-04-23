---
kind: output_template
id: bld_output_synthetic_data_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a synthetic_data_config
pattern: every field here exists in SCHEMA -- template derives, never invents
quality: null
title: "Synthetic Data Config Builder - Output ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, output]
tldr: "Output template for synthetic data config artifacts."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_synthetic_data_config
---

# Output Template: synthetic_data_config

```yaml
id: p01_sdc_{{config_slug}}
kind: synthetic_data_config
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
generation_method: "{{self_instruct_or_evol_instruct_or_other}}"
source_model: "{{teacher_model_id}}"
seed_count: {{integer}}
output_format: "{{jsonl_or_alpaca_or_sharegpt}}"
target_samples: {{integer}}
domain: "{{domain_value}}"
quality: null
tags: [synthetic-data, {{method_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Generation Method
`{{method_description_with_parameters}}`

## Seed Examples
`{{seed_count_format_and_diversity_requirements}}`

## Quality Filters
`{{perplexity_dedup_length_toxicity_thresholds}}`

## Decontamination
`{{eval_set_overlap_removal_rules}}`

## Output Format
`{{schema_field_names_validation}}`

## Cost Estimate
`{{estimated_api_cost_or_compute_time}}`
