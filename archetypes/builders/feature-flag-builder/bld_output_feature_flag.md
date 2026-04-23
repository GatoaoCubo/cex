---
kind: output_template
id: bld_output_template_feature_flag
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a feature_flag artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Feature Flag"
version: "1.0.0"
author: n03_builder
tags: [feature_flag, builder, examples]
tldr: "Golden and anti-examples for feature flag construction, demonstrating ideal structure and common pitfalls."
domain: "feature flag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_runtime_rule
  - bld_output_template_golden_test
  - bld_output_template_input_schema
  - bld_output_template_output_validator
  - bld_schema_feature_flag
  - bld_output_template_embedding_config
  - bld_output_template_hook_config
  - bld_examples_feature_flag
  - bld_output_template_skill
  - bld_output_template_path_config
---

# Output Template: feature_flag
```yaml
id: p09_ff_{{feature_slug}}
kind: feature_flag
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
flag_name: "{{human_readable_flag_name}}"
default_state: {{on|off}}
category: {{release|experiment|ops|permission}}
rollout_percentage: {{0_to_100}}
quality: null
tags: [feature_flag, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_flag_controls_max_200ch}}"
owner: "{{responsible_team_or_person}}"
expires: "{{YYYY-MM-DD_or_null}}"
targeting: "{{targeting_strategy_summary}}"
```
## Flag Specification
`{{feature_description_and_current_state}}`
`{{kill_switch_behavior_if_ops}}`
## Rollout Strategy
`{{rollout_stages_with_percentages_and_timeline}}`
## Lifecycle
`{{lifecycle_stages_create_test_ramp_full_retire}}`
## References
- `{{reference_1}}`
```

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
| Domain | feature flag construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_runtime_rule]] | sibling | 0.42 |
| [[bld_output_template_golden_test]] | sibling | 0.40 |
| [[bld_output_template_input_schema]] | sibling | 0.39 |
| [[bld_output_template_output_validator]] | sibling | 0.38 |
| [[bld_schema_feature_flag]] | downstream | 0.38 |
| [[bld_output_template_embedding_config]] | sibling | 0.38 |
| [[bld_output_template_hook_config]] | sibling | 0.37 |
| [[bld_examples_feature_flag]] | downstream | 0.36 |
| [[bld_output_template_skill]] | sibling | 0.35 |
| [[bld_output_template_path_config]] | sibling | 0.35 |
