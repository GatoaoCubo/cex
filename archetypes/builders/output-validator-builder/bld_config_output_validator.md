---
kind: config
id: bld_config_output_validator
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 25
disallowed_tools: [Write, BashTool]
fork_context: inline
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: restricted
quality: 9.0
title: "Config Output Validator"
version: "1.0.0"
author: n03_builder
tags: [output_validator, builder, examples]
tldr: "Golden and anti-examples for output validator construction, demonstrating ideal structure and common pitfalls."
domain: "output validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_prompt_version
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
  - bld_config_chunk_strategy
  - bld_config_hook_config
  - bld_config_quality_gate
  - bld_config_effort_profile
  - bld_collaboration_output_validator
---
# Config: output_validator Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p05_oval_{slug}.md` | `p05_oval_example.md` |
| Builder directory | kebab-case | `output-validator-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `example_config` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
1. Output: `cex/P05_output/examples/p05_oval_{slug}.md`
2. Compiled: `cex/P05_output/compiled/p05_oval_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 2048 bytes
2. Total (frontmatter + body): ~3048 bytes
3. Density: >= 0.85 (no filler)

## Metadata

```yaml
id: bld_config_output_validator
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-output-validator.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | output validator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.61 |
| [[bld_config_memory_scope]] | sibling | 0.58 |
| [[bld_config_prompt_version]] | sibling | 0.57 |
| [[bld_config_handoff_protocol]] | sibling | 0.54 |
| [[bld_config_constraint_spec]] | sibling | 0.53 |
| [[bld_config_chunk_strategy]] | sibling | 0.52 |
| [[bld_config_hook_config]] | sibling | 0.52 |
| [[bld_config_quality_gate]] | sibling | 0.48 |
| [[bld_config_effort_profile]] | sibling | 0.47 |
| [[bld_collaboration_output_validator]] | downstream | 0.39 |
