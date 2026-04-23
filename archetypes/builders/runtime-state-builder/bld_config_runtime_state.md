---
kind: config
id: bld_config_runtime_state
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for runtime_state production
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
title: "Config Runtime State"
version: "1.0.0"
author: n03_builder
tags: [runtime_state, builder, examples]
tldr: "Golden and anti-examples for runtime state construction, demonstrating ideal structure and common pitfalls."
domain: "runtime state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_runtime_state
  - bld_config_session_state
  - bld_collaboration_runtime_state
  - p11_qg_runtime_state
  - runtime-state-builder
  - bld_schema_runtime_state
  - bld_config_mental_model
  - bld_config_quality_gate
  - bld_config_knowledge_index
  - bld_config_retriever_config
---
# Config: runtime_state Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p10_rs_{agent_slug}.md | p10_rs_researcher.md |
| Builder dir | kebab-case | runtime-state-builder/ |
| Fields | snake_case | routing_mode, update_frequency |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P10_memory/examples/p10_rs_{agent_slug}.md
2. Compiled: cex/P10_memory/compiled/p10_rs_{agent_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Density: >= 0.80
## Persistence Modes
| Mode | Lifetime | Use case |
|------|----------|----------|
| session | Reset on session end | Ephemeral routing preferences |
| cross_session | Survives across sessions | Accumulated routing intelligence |
## Routing Mode Reference
| Mode | Mechanism | Best for |
|------|-----------|----------|
| keyword | Exact keyword matching | Simple, deterministic routing |
| semantic | Embedding similarity | Fuzzy, meaning-based routing |
| hybrid | Keyword + semantic combined | Balanced accuracy + recall |
| rule_based | Explicit if-then rules | Complex multi-condition routing |

## Metadata

```yaml
id: bld_config_runtime_state
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-runtime-state.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_runtime_state]] | upstream | 0.29 |
| [[bld_config_session_state]] | sibling | 0.29 |
| [[bld_collaboration_runtime_state]] | downstream | 0.29 |
| [[p11_qg_runtime_state]] | downstream | 0.28 |
| [[runtime-state-builder]] | downstream | 0.28 |
| [[bld_schema_runtime_state]] | upstream | 0.27 |
| [[bld_config_mental_model]] | sibling | 0.26 |
| [[bld_config_quality_gate]] | sibling | 0.26 |
| [[bld_config_knowledge_index]] | sibling | 0.26 |
| [[bld_config_retriever_config]] | sibling | 0.25 |
