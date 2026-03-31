---
kind: output_template
id: bld_output_template_effort_profile
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an effort_profile artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: effort_profile
```yaml
id: p09_effort_{{slug}}
kind: effort_profile
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}"
model: "{{model}}"
thinking_level: "{{thinking_level}}"
target_builder: "{{target_builder}}"
quality: null
tags: [effort_profile, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}"
cost_tier: "{{cost_tier}}"
fallback_model: "{{fallback_model}}"
max_tokens: {{max_tokens}}
temperature: {{temperature}}
```
## Overview
{{overview_content}}
## Configuration
{{configuration_content}}
## Levels
{{levels_content}}
## Integration
{{integration_content}}
