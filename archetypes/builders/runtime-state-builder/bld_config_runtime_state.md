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
- Output: cex/P10_memory/examples/p10_rs_{agent_slug}.md
- Compiled: cex/P10_memory/compiled/p10_rs_{agent_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Density: >= 0.80
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
