---
kind: output_template
id: bld_output_template_white_label_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for white_label_config production
quality: 8.8
title: "Output Template White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, output_template]
tldr: "Template with vars for white_label_config production"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_white_label_config
  - p04_fn_cf_slides_generate
  - bld_output_template_playground_config
  - bld_schema_sdk_example
  - bld_output_template_judge_config
---

```yaml
---
id: {{id}} <!-- Pattern: ^p09_wl_[a-z][a-z0-9_]+.yaml$ -->
name: {{name}} <!-- Human-readable label for the white label -->
description: {{description}} <!-- Brief purpose of this configuration -->
config:
  theme: {{theme}} <!-- UI/UX theme (e.g., "dark", "light") -->
  language: {{language}} <!-- Default language code (e.g., "en", "es") -->
quality: null <!-- Must remain null -->
```

| Parameter   | Example Value | Description                  |
|-------------|---------------|------------------------------|
| theme       | dark          | UI theme for the platform    |
| language    | en            | Default language             |
| max_users   | 1000          | Maximum concurrent users     |

```yaml
# Example config block
config:
  theme: dark
  language: en
  max_users: 1000
  features:
    - trading
    - wallet
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_white_label_config]] | downstream | 0.21 |
| [[p04_fn_cf_slides_generate]] | upstream | 0.18 |
| [[bld_output_template_playground_config]] | sibling | 0.17 |
| [[bld_schema_sdk_example]] | downstream | 0.16 |
| [[bld_output_template_judge_config]] | sibling | 0.15 |
