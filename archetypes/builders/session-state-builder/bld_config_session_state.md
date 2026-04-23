---
kind: config
id: bld_config_session_state
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
title: "Config Session State"
version: "1.0.0"
author: n03_builder
tags: [session_state, builder, examples]
tldr: "Golden and anti-examples for session state construction, demonstrating ideal structure and common pitfalls."
domain: "session state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_session_state
  - bld_config_signal
  - bld_knowledge_card_session_state
  - session-state-builder
  - bld_examples_session_state
  - bld_schema_session_state
  - p03_sp_session_state_builder
  - bld_memory_session_state
  - p01_kc_session_state
  - bld_config_retriever_config
---
# Config: session_state Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p10_ss_{session}.yaml` | `p10_ss_edison_wave19_build.yaml` |
| Builder directory | kebab-case | `session-state-builder/` |
| Frontmatter fields | snake_case | `session_id`, `started_at` |
| Status values | lowercase enum | `active`, `paused`, `completed`, `aborted` |
| Agent values | lowercase slug | `edison`, `atlas`, `codex` |
Rule: use `.yaml` extension only for this builder.
## File Paths
1. Output: `cex/P10_memory/compiled/p10_ss_{session}.yaml`
2. Human reference: `cex/P10_memory/examples/p10_ss_{session}.md`
## Size Limits
1. Preferred snapshot size: <= 2048 bytes
2. Absolute max: 3072 bytes
3. Optional fields should remain sparse and compact
## Payload Restrictions
1. Required fields must appear exactly as defined in SCHEMA.md
2. Omit optional null/unknown fields instead of writing placeholders
3. `ended_at` and `duration_seconds` only meaningful for completed/aborted sessions
4. `checkpoints` should be concise: label + timestamp only
5. `errors` entries must have both `code` and `message`
## Boundary Restrictions
1. No persistent state: routing decisions, accumulated scores belong in runtime_state
2. No learning patterns: accumulated outcomes belong in learning_record
3. No search configuration: index settings belong in knowledge_index
4. No immutable rules: fundamental axioms belong in axiom

## Metadata

```yaml
id: bld_config_session_state
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-session-state.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | session state construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_session_state]] | upstream | 0.41 |
| [[bld_config_signal]] | sibling | 0.38 |
| [[bld_knowledge_card_session_state]] | upstream | 0.38 |
| [[session-state-builder]] | downstream | 0.37 |
| [[bld_examples_session_state]] | upstream | 0.36 |
| [[bld_schema_session_state]] | upstream | 0.35 |
| [[p03_sp_session_state_builder]] | upstream | 0.35 |
| [[bld_memory_session_state]] | downstream | 0.34 |
| [[p01_kc_session_state]] | downstream | 0.32 |
| [[bld_config_retriever_config]] | sibling | 0.32 |
