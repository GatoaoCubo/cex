---
kind: config
id: bld_config_quality_gate
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for quality_gate production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Quality Gate"
version: "1.0.0"
author: n03_builder
tags: [quality_gate, builder, examples]
tldr: "Golden and anti-examples for quality gate construction, demonstrating ideal structure and common pitfalls."
domain: "quality gate construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_hook_config
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
  - bld_config_chunk_strategy
  - bld_config_effort_profile
  - bld_config_validation_schema
---
# Config: quality_gate Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_qg_{slug}.md | p11_qg_kc_publish.md |
| Builder dir | kebab-case | quality-gate-builder/ |
| Fields | snake_case | density_score |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P11_feedback/examples/p11_qg_{slug}.md
2. Compiled: cex/P11_feedback/compiled/p11_qg_{slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80

## Metadata

```yaml
id: bld_config_quality_gate
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-quality-gate.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | quality gate construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.51 |
| [[bld_config_memory_scope]] | sibling | 0.48 |
| [[bld_config_prompt_version]] | sibling | 0.46 |
| [[bld_config_output_validator]] | sibling | 0.45 |
| [[bld_config_hook_config]] | sibling | 0.44 |
| [[bld_config_handoff_protocol]] | sibling | 0.44 |
| [[bld_config_constraint_spec]] | sibling | 0.43 |
| [[bld_config_chunk_strategy]] | sibling | 0.42 |
| [[bld_config_effort_profile]] | sibling | 0.39 |
| [[bld_config_validation_schema]] | sibling | 0.37 |
