---
kind: output_template
id: bld_output_template_path_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a path_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Path Config"
version: "1.0.0"
author: n03_builder
tags: [path_config, builder, examples]
tldr: "Golden and anti-examples for path config construction, demonstrating ideal structure and common pitfalls."
domain: "path config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_path_config
  - p03_ins_path_config
  - bld_examples_path_config
  - bld_output_template_input_schema
  - path-config-builder
  - bld_output_template_function_def
  - bld_output_template_runtime_rule
  - p03_sp_path_config_builder
  - bld_memory_path_config
  - bld_output_template_feature_flag
---

# Output Template: path_config
```yaml
id: p09_path_{{scope_slug}}
kind: path_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{global_or_agent_group_or_service}}"
paths:
  - {{path_name_1}}
  - {{path_name_2}}
  - {{path_name_3}}
platform: {{windows|unix|all}}
quality: null
tags: [path_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_paths_cover_max_200ch}}"
base_dir: "{{base_directory_path}}"
dir_count: {{N}}
file_count: {{N}}
```
## Overview
`{{what_scope_and_purpose_1_to_2_sentences}}`
`{{who_consumes_these_paths}}`
## Path Catalog
| Path | Type | Platform | Default | Required | Notes |
|------|------|----------|---------|----------|-------|
| `{{path_name_1}}` | {{dir|file}} | {{windows|unix|all}} | {{default_path}} | {{yes|no}} | `{{notes}}` |
| `{{path_name_2}}` | {{type}} | {{platform}} | {{default}} | {{yes|no}} | `{{notes}}` |
| `{{path_name_3}}` | {{type}} | {{platform}} | {{default}} | {{yes|no}} | `{{notes}}` |
## Directory Hierarchy
```text
{{base_dir}}/
  {{subdir_1}}/
  {{subdir_2}}/
    {{nested_dir}}/
  {{subdir_3}}/
```
## Platform Notes
`{{platform_specific_differences_and_resolution_rules}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

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
| Domain | path config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_path_config]] | downstream | 0.51 |
| [[p03_ins_path_config]] | upstream | 0.40 |
| [[bld_examples_path_config]] | downstream | 0.39 |
| [[bld_output_template_input_schema]] | sibling | 0.39 |
| [[path-config-builder]] | downstream | 0.34 |
| [[bld_output_template_function_def]] | sibling | 0.33 |
| [[bld_output_template_runtime_rule]] | sibling | 0.33 |
| [[p03_sp_path_config_builder]] | upstream | 0.33 |
| [[bld_memory_path_config]] | downstream | 0.32 |
| [[bld_output_template_feature_flag]] | sibling | 0.32 |
