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
