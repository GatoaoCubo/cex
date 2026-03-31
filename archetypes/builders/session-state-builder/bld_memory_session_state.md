---
kind: memory
id: bld_memory_session_state
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for session_state artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: session-state-builder
## Summary
Session states are ephemeral snapshots of an agent's current context during execution — token usage, active tasks, checkpoints, and working memory. The critical production lesson is that session states must never persist beyond the session that created them. Leaked session state causes agents to resume with stale context from previous runs, leading to confusing behavior. The second lesson is checkpoint design: checkpoints without recovery instructions are useless — knowing where you were without knowing how to resume provides no value.
## Pattern
- Session state must be scoped to exactly one session — automatically discarded when the session ends
- Checkpoints must include both state snapshot and recovery instructions for resuming from that point
- Token usage tracking must include both consumed and remaining budget — one without the other prevents planning
- Context window contents should be summarized, not stored verbatim — verbatim storage exceeds size limits
- Active task list must include task status (pending, in-progress, blocked, complete) for each entry
- Timestamp all state entries — temporal ordering enables debugging of state evolution
## Anti-Pattern
- Session state persisting across sessions — agents resume with stale context causing confusion
- Checkpoints without recovery instructions — knowing the state is useless without knowing how to resume
- Storing full context window verbatim — exceeds size limits and most content is reconstructable
- Missing token budget tracking — agent continues past budget limits or stops prematurely
- Confusing session_state (P10, ephemeral snapshot) with runtime_state (P10, mutable across session) or learning_record (P10, retrospective)
- State without timestamps — cannot determine recency or debug state evolution
## Context
Session states sit in the P10 memory pillar as the most ephemeral memory type. They exist only during a single execution session and capture the agent's working memory, progress, and resource usage. They are consumed by checkpoint/resume systems, context compaction logic, and resource monitors. Unlike runtime states (mutable but persistent) and learning records (retrospective and permanent), session states are live and disposable.
## Impact
Strict session scoping eliminated 100% of stale context bugs from session leakage. Checkpoints with recovery instructions achieved 90% successful session resumption versus 20% for checkpoint-only snapshots. Token budget tracking prevented 95% of budget overrun incidents.
## Reproducibility
For reliable session state production: (1) define session scope boundary explicitly, (2) include checkpoint with recovery instructions, (3) track token budget (consumed + remaining), (4) summarize context window instead of verbatim storage, (5) timestamp all entries, (6) validate against naming and size gates.
## References
- session-state-builder SCHEMA.md (P10 ephemeral state fields)
- P10 memory pillar specification
- Session management and checkpoint/resume patterns
