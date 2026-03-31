---
kind: output_template
id: bld_output_template_hook_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a hook_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: hook_config
```yaml
id: p04_hookconf_{{slug}}
kind: hook_config
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}"
target_builder: "{{target_builder}}"
phases: [{{phases_list}}]
quality: null
tags: [hook_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}"
priority_mode: "{{priority_mode}}"
error_strategy: "{{error_strategy}}"
```
## Overview
{{overview_content}}
## Hooks
{{hooks_table_content}}
## Lifecycle
{{lifecycle_content}}
## Integration
{{integration_content}}
