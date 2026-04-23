---
kind: output_template
id: bld_output_template_effort_profile
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an effort_profile artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Effort Profile"
version: "1.0.0"
author: n03_builder
tags: [effort_profile, builder, examples]
tldr: "Golden and anti-examples for effort profile construction, demonstrating ideal structure and common pitfalls."
domain: "effort profile construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_hook_config
  - bld_architecture_effort_profile
  - bld_output_template_output_validator
  - bld_output_template_constraint_spec
  - bld_output_template_input_schema
  - bld_output_template_feature_flag
  - bld_output_template_runtime_rule
  - bld_output_template_embedding_config
  - bld_output_template_retriever_config
  - bld_instruction_effort_profile
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
`{{overview_content}}`
## Configuration
`{{configuration_content}}`
## Levels
`{{levels_content}}`
## Integration
`{{integration_content}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | effort profile construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_hook_config]] | sibling | 0.44 |
| [[bld_architecture_effort_profile]] | downstream | 0.41 |
| [[bld_output_template_output_validator]] | sibling | 0.41 |
| [[bld_output_template_constraint_spec]] | sibling | 0.41 |
| [[bld_output_template_input_schema]] | sibling | 0.38 |
| [[bld_output_template_feature_flag]] | sibling | 0.38 |
| [[bld_output_template_runtime_rule]] | sibling | 0.37 |
| [[bld_output_template_embedding_config]] | sibling | 0.36 |
| [[bld_output_template_retriever_config]] | sibling | 0.36 |
| [[bld_instruction_effort_profile]] | upstream | 0.36 |
