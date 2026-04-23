---
kind: output_template
id: bld_output_template_dataset_card
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for dataset_card production
quality: 8.7
title: "Output Template Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, output_template]
tldr: "Template with vars for dataset_card production"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_dataset_card
  - p01_kc_dataset_card
  - bld_schema_dataset_card
  - bld_output_template_thinking_config
  - bld_examples_workflow_node
  - dataset-card-builder
  - p10_lr_dataset_card_builder
  - bld_output_template_integration_guide
  - p06_is_creation_data
  - bld_output_template_input_schema
---

```yaml
name: {{name}}
version: {{version}}
description: {{description}}
date: {{date}}
author: {{author}}
license: {{license}}
tags: {{tags}}
```

# Dataset Card: {{name}}
## Overview
{{overview_summary}}

## Data Collection
{{collection_methodology_and_sources}}

## Data Processing
{{preprocessing_and_cleaning_steps}}

## Intended Use
{{use_cases_and_applications}}

## Limitations & Biases
{{limitations_and_potential_biases}}

## Metadata
- **Pillar**: P01
- **Template Type**: dataset_card
- **Naming Convention**: p01_dc_{{name}}.md

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_dataset_card]] | downstream | 0.27 |
| [[p01_kc_dataset_card]] | upstream | 0.24 |
| [[bld_schema_dataset_card]] | downstream | 0.21 |
| [[bld_output_template_thinking_config]] | sibling | 0.20 |
| [[bld_examples_workflow_node]] | downstream | 0.20 |
| [[dataset-card-builder]] | upstream | 0.19 |
| [[p10_lr_dataset_card_builder]] | downstream | 0.19 |
| [[bld_output_template_integration_guide]] | sibling | 0.19 |
| [[p06_is_creation_data]] | downstream | 0.18 |
| [[bld_output_template_input_schema]] | sibling | 0.18 |
