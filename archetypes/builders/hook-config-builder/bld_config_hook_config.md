---
kind: config
id: bld_config_hook_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
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
title: "Config Hook Config"
version: "1.0.0"
author: n03_builder
tags: [hook_config, builder, examples]
tldr: "Golden and anti-examples for hook config construction, demonstrating ideal structure and common pitfalls."
domain: "hook config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
  - bld_config_chunk_strategy
  - bld_config_quality_gate
  - bld_config_effort_profile
  - bld_config_pattern
---
# Config: hook_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_hookconf_{slug}.md` | `p04_hookconf_agent_builder.md` |
| Builder directory | kebab-case | `hook-config-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `agent_builder` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
1. Output: `cex/P04_execution/examples/p04_hookconf_{slug}.md`
2. Compiled: `cex/P04_execution/compiled/p04_hookconf_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total (frontmatter + body): ~5120 bytes
3. Density: >= 0.8 (no filler)

## Metadata

```yaml
id: bld_config_hook_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-hook-config.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | hook config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.63 |
| [[bld_config_memory_scope]] | sibling | 0.57 |
| [[bld_config_prompt_version]] | sibling | 0.56 |
| [[bld_config_output_validator]] | sibling | 0.55 |
| [[bld_config_handoff_protocol]] | sibling | 0.53 |
| [[bld_config_constraint_spec]] | sibling | 0.52 |
| [[bld_config_chunk_strategy]] | sibling | 0.51 |
| [[bld_config_quality_gate]] | sibling | 0.49 |
| [[bld_config_effort_profile]] | sibling | 0.47 |
| [[bld_config_pattern]] | sibling | 0.39 |
