---
kind: knowledge_card
id: bld_knowledge_card_session_state
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for session_state production — atomic searchable facts
sources: session-state-builder MANIFEST.md + SCHEMA.md, P10 schema
quality: 9.1
title: "Knowledge Card Session State"
version: "1.0.0"
author: n03_builder
tags: [session_state, builder, examples]
tldr: "Golden and anti-examples for session state construction, demonstrating ideal structure and common pitfalls."
domain: "session state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_session_state_builder
  - bld_memory_session_state
  - bld_architecture_session_state
  - bld_collaboration_session_state
  - bld_schema_session_state
  - p03_ins_session_state_builder
  - bld_config_session_state
  - p01_kc_session_state
  - session-state-builder
  - bld_memory_runtime_state
---

# Domain Knowledge: session_state
## Executive Summary
Session states are ephemeral snapshots of an agent's execution context — they capture what the agent is doing right now, how far along it is, and where recovery can resume. Each snapshot is a single-point observation (not a time series) consumed by monitors, recovery tools, and post-session extractors. They differ from runtime states (which persist across sessions and drive decisions), learning records (which accumulate experience over time), and axioms (which are immutable truths) by being strictly ephemeral observations lost when the session ends.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory) |
| Kind | `session_state` (exact literal) |
| ID pattern | `p10_ss_{session_slug}` |
| Naming | `p10_ss_{agent}_{task}.yaml` |
| Required frontmatter | session_id, agent, status, started_at + standard CEX fields |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Status values | active, paused, completed, aborted |
| Format | YAML (machine-parseable) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Minimum semantic contract | session_id + agent + status + started_at — always present |
| Status semantics | active (in progress), paused (recoverable), completed (normal end), aborted (abnormal) |
| Optional runtime metrics | active_tasks, context_window_used, tools_called, errors, checkpoints |
| Single-point snapshot | One observation, not a time series; no historical data |
| Graceful degradation | Must work when optional fields are absent |
| Machine-parseable format | YAML for programmatic consumption by monitors |
| Checkpoint for recovery | last_checkpoint enables resume after interruption |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Persistent state in session_state | Session state is ephemeral; use runtime_state for persistence |
| Time series data | Not a log; single snapshot per write |
| Missing session_id | Core identifier; cannot correlate with other session data |
| Missing status field | Consumers cannot determine agent lifecycle phase |
| Body > 3072 bytes | Exceeds max; session states must be compact |
| Routing decisions in session state | Routing belongs in runtime_state or mental_model |
| Optional fields without graceful fallback | Consumers break when optional fields absent |
## Application
1. Set session_id (unique execution context identifier)
2. Set agent (which agent is executing)
3. Set status: active, paused, completed, or aborted
4. Set started_at (ISO 8601 timestamp)
5. Add optional metrics as needed: tasks, context window, tools, errors
6. Add checkpoint data for recovery if applicable
7. Keep body compact (single snapshot); validate <= 3072 bytes
## References
- session-state-builder SCHEMA.md v1.0.0
- P10 memory pillar schema
- Finite state machine (status lifecycle)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_session_state_builder]] | downstream | 0.49 |
| [[bld_memory_session_state]] | downstream | 0.43 |
| [[bld_architecture_session_state]] | downstream | 0.42 |
| [[bld_collaboration_session_state]] | downstream | 0.40 |
| [[bld_schema_session_state]] | downstream | 0.39 |
| [[p03_ins_session_state_builder]] | downstream | 0.39 |
| [[bld_config_session_state]] | downstream | 0.39 |
| [[p01_kc_session_state]] | sibling | 0.39 |
| [[session-state-builder]] | downstream | 0.38 |
| [[bld_memory_runtime_state]] | downstream | 0.33 |
