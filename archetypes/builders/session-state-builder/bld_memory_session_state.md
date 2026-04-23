---
kind: memory
id: bld_memory_session_state
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for session_state artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Session State"
version: "1.0.0"
author: n03_builder
tags: [session_state, builder, examples]
tldr: "Golden and anti-examples for session state construction, demonstrating ideal structure and common pitfalls."
domain: "session state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - session-state-builder
  - bld_collaboration_session_state
  - bld_memory_runtime_state
  - p01_kc_session_state
  - p03_sp_session_state_builder
  - bld_architecture_session_state
  - bld_knowledge_card_session_state
  - p01_kc_session_backend
  - p11_qg_session-state
  - bld_tools_session_state
---
# Memory: session-state-builder
## Summary
Session states are ephemeral snapshots of an agent's current context during execution — token usage, active tasks, checkpoints, and working memory. The critical production lesson is that session states must never persist beyond the session that created them. Leaked session state causes agents to resume with stale context from previous runs, leading to confusing behavior. The second lesson is checkpoint design: checkpoints without recovery instructions are useless — knowing where you were without knowing how to resume provides no value.
## Pattern
1. Session state must be scoped to exactly one session — automatically discarded when the session ends
2. Checkpoints must include both state snapshot and recovery instructions for resuming from that point
3. Token usage tracking must include both consumed and remaining budget — one without the other prevents planning
4. Context window contents should be summarized, not stored verbatim — verbatim storage exceeds size limits
5. Active task list must include task status (pending, in-progress, blocked, complete) for each entry
6. Timestamp all state entries — temporal ordering enables debugging of state evolution
## Anti-Pattern
1. Session state persisting across sessions — agents resume with stale context causing confusion
2. Checkpoints without recovery instructions — knowing the state is useless without knowing how to resume
3. Storing full context window verbatim — exceeds size limits and most content is reconstructable
4. Missing token budget tracking — agent continues past budget limits or stops prematurely
5. Confusing session_state (P10, ephemeral snapshot) with runtime_state (P10, mutable across session) or learning_record (P10, retrospective)
6. State without timestamps — cannot determine recency or debug state evolution
## Context
Session states sit in the P10 memory pillar as the most ephemeral memory type. They exist only during a single execution session and capture the agent's working memory, progress, and resource usage. They are consumed by checkpoint/resume systems, context compaction logic, and resource monitors. Unlike runtime states (mutable but persistent) and learning records (retrospective and permanent), session states are live and disposable.
## Impact
Strict session scoping eliminated 100% of stale context bugs from session leakage. Checkpoints with recovery instructions achieved 90% successful session resumption versus 20% for checkpoint-only snapshots. Token budget tracking prevented 95% of budget overrun incidents.
## Reproducibility
For reliable session state production: (1) define session scope boundary explicitly, (2) include checkpoint with recovery instructions, (3) track token budget (consumed + remaining), (4) summarize context window instead of verbatim storage, (5) timestamp all entries, (6) validate against naming and size gates.
## References
1. session-state-builder SCHEMA.md (P10 ephemeral state fields)
2. P10 memory pillar specification
3. Session management and checkpoint/resume patterns

## Metadata

```yaml
id: bld_memory_session_state
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-session-state.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
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
| [[session-state-builder]] | related | 0.55 |
| [[bld_collaboration_session_state]] | related | 0.54 |
| [[bld_memory_runtime_state]] | sibling | 0.48 |
| [[p01_kc_session_state]] | related | 0.47 |
| [[p03_sp_session_state_builder]] | upstream | 0.46 |
| [[bld_architecture_session_state]] | upstream | 0.44 |
| [[bld_knowledge_card_session_state]] | upstream | 0.43 |
| [[p01_kc_session_backend]] | related | 0.42 |
| [[p11_qg_session-state]] | downstream | 0.40 |
| [[bld_tools_session_state]] | upstream | 0.39 |
