---
kind: output_template
id: bld_output_template_memory_scope
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a memory_scope artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Memory Scope"
version: "1.0.0"
author: n03_builder
tags: [memory_scope, builder, examples]
tldr: "Golden and anti-examples for memory scope construction, demonstrating ideal structure and common pitfalls."
domain: "memory scope construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_examples_memory_scope
  - bld_output_template_hook_config
  - p03_sp_memory_scope_builder
  - bld_schema_memory_scope
  - bld_output_template_input_schema
  - bld_output_template_output_validator
  - memory-scope-builder
  - bld_output_template_feature_flag
  - bld_architecture_memory_scope
---

# Output Template: memory_scope
```yaml
id: p02_memscope_{{slug}}
kind: memory_scope
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{name}}}}"
memory_types: "{{memory_types}}}}"
backend: "{{backend}}}}"
ttl: "{{ttl}}}}"
quality: null
tags: [memory_scope, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{description}}}}"
scope: "{{scope}}}}"
max_entries: "{{max_entries}}}}"
eviction_policy: "{{eviction_policy}}}}"
encryption: "{{encryption}}}}"
shared_with: "{{shared_with}}}}"
```
## Overview
`{{overview_content}}`
## Memory Types
`{{memory_types_content}}`
## Backend Config
`{{backend_config_content}}`
## Lifecycle
`{{lifecycle_content}}`

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
| Domain | memory scope construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | upstream | 0.41 |
| [[bld_examples_memory_scope]] | downstream | 0.39 |
| [[bld_output_template_hook_config]] | sibling | 0.38 |
| [[p03_sp_memory_scope_builder]] | upstream | 0.38 |
| [[bld_schema_memory_scope]] | downstream | 0.37 |
| [[bld_output_template_input_schema]] | sibling | 0.37 |
| [[bld_output_template_output_validator]] | sibling | 0.37 |
| [[memory-scope-builder]] | upstream | 0.37 |
| [[bld_output_template_feature_flag]] | sibling | 0.36 |
| [[bld_architecture_memory_scope]] | downstream | 0.36 |
