---
kind: config
id: bld_config_handoff
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
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
quality: 9.1
title: "Config Handoff"
version: "1.0.0"
author: n03_builder
tags: [handoff, builder, examples]
tldr: "Golden and anti-examples for handoff construction, demonstrating ideal structure and common pitfalls."
domain: "handoff construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_handoff
  - handoff-builder
  - p01_kc_handoff
  - bld_config_handoff_protocol
  - bld_schema_handoff
  - bld_instruction_handoff
  - bld_collaboration_handoff_protocol
  - bld_config_dag
  - bld_config_signal
  - handoff-protocol-builder
---
# Config: handoff Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_ho_{task}.md` | `p12_ho_wave19_builders.md` |
| Builder directory | kebab-case | `handoff-builder/` |
| Frontmatter fields | snake_case | `quality_target`, `scope_fence` |
| Autonomy values | lowercase enum | `full`, `supervised`, `assisted` |
| Agent_group values | lowercase slug | `edison`, `atlas`, `shaka` |
Rule: use `.md` (YAML frontmatter + markdown body) for handoff artifacts.
## File Paths
1. Primary output: `.claude/handoffs/p12_ho_{task}.md`
2. Compiled output: `P12_orchestration/compiled/p12_ho_{task}.md`
3. Human reference: `P12_orchestration/examples/p12_ho_{task}.md`
## Size Limits
1. Preferred handoff size: <= 3072 bytes
2. Absolute max: 4096 bytes
3. Tasks should be concise and specific
## Content Restrictions
1. Each task step must be one specific action (no compound steps)
2. Scope fence must list both SOMENTE and NAO TOQUE
3. Commit section must have exact git add and commit commands
4. Signal section must reference a concrete completion mechanism
## Boundary Restrictions
1. No prompt persona or response format constraints (belongs in action_prompt)
2. No status events or quality scores (belongs in signal)
3. No keyword routing tables (belongs in dispatch_rule)
4. No step graphs with error handling (belongs in workflow)
5. No dependency graph structure (belongs in dag)
6. No multi-agent coordination protocol (belongs in crew)

## Metadata

```yaml
id: bld_config_handoff
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-handoff.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | handoff construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_handoff]] | upstream | 0.43 |
| [[handoff-builder]] | downstream | 0.40 |
| [[p01_kc_handoff]] | downstream | 0.39 |
| [[bld_config_handoff_protocol]] | sibling | 0.39 |
| [[bld_schema_handoff]] | upstream | 0.38 |
| [[bld_instruction_handoff]] | upstream | 0.37 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.36 |
| [[bld_config_dag]] | sibling | 0.35 |
| [[bld_config_signal]] | sibling | 0.35 |
| [[handoff-protocol-builder]] | upstream | 0.35 |
