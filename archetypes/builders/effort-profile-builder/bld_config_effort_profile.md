---
kind: config
id: bld_config_effort_profile
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
title: "Config Effort Profile"
version: "1.0.0"
author: n03_builder
tags: [effort_profile, builder, examples]
tldr: "Golden and anti-examples for effort profile construction, demonstrating ideal structure and common pitfalls."
domain: "effort profile construction"
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
  - bld_config_hook_config
  - bld_config_chunk_strategy
  - bld_config_quality_gate
  - bld_collaboration_effort_profile
---
# Config: effort_profile Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_effort_{slug}.md` | `p09_effort_n03_opus_high.md` |
| Builder directory | kebab-case | `effort-profile-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `n03_opus_high` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
1. Output: `cex/P09_config/examples/p09_effort_{slug}.md`
2. Compiled: `cex/P09_config/compiled/p09_effort_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total (frontmatter + body): ~5120 bytes
3. Density: >= 0.8 (no filler)

## Metadata

```yaml
id: bld_config_effort_profile
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-effort-profile.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
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
| [[bld_config_retriever_config]] | sibling | 0.60 |
| [[bld_config_memory_scope]] | sibling | 0.57 |
| [[bld_config_prompt_version]] | sibling | 0.56 |
| [[bld_config_output_validator]] | sibling | 0.55 |
| [[bld_config_handoff_protocol]] | sibling | 0.53 |
| [[bld_config_constraint_spec]] | sibling | 0.53 |
| [[bld_config_hook_config]] | sibling | 0.52 |
| [[bld_config_chunk_strategy]] | sibling | 0.51 |
| [[bld_config_quality_gate]] | sibling | 0.49 |
| [[bld_collaboration_effort_profile]] | downstream | 0.40 |
