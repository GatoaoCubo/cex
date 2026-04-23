---
kind: memory_config
id: bld_memory_personality
pillar: P10
llm_function: INJECT
purpose: Memory hooks for personality artifacts -- what to persist and retrieve
quality: 8.8
title: "Memory: personality-builder"
version: "1.0.0"
author: n03_builder
tags: [personality, builder, memory, P10, hermes_origin, hot_swap]
tldr: "personality memory: active personality id in session_state, personality history in episodic_memory, preferences in user_model."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - p01_kc_mental_model
  - bld_architecture_session_state
  - memory-scope-builder
  - bld_architecture_memory_scope
  - p03_sp_memory_scope_builder
  - p01_kc_memory_scope
  - session-state-builder
  - p03_sp_session_state_builder
  - bld_collaboration_session_state
  - p01_kc_session_state
---

# Memory: personality-builder

## What to Persist

| Data | Kind | Location | TTL |
|------|------|----------|-----|
| Active personality id | session_state | P10 session_state.active_personality | session scope |
| Personality switch history | episodic_memory | P10 episodic store | 90d |
| User's preferred personality | user_model | P10 user_model.preferences collection | null (forever) |
| Personality definition | personality | P02 personality store | permanent |

## F3 INJECT Pattern

When an agent activates a personality, F3 INJECT pulls:
1. `p02_per_{{name}}.md` -- the personality spec itself
2. `session_state.active_personality` -- current active persona (for context continuity)
3. `user_model.preferences` -- user's preferred styles (optional, for personalization layer)

## Memory Scope

```
personality artifact        (P02) -- the DEFINITION (permanent, versioned)
session_state              (P10) -- tracks WHICH personality is active right now (ephemeral)
episodic_memory            (P10) -- records WHEN switches happened (90d TTL)
user_model.preferences     (P10) -- learns user's PREFERRED personality over time (durable)
```

## F8 COLLABORATE Signals

After producing a personality artifact:
```python
from _tools.signal_writer import write_signal
write_signal('n03', 'complete', score, mission='personality_built', kind='personality', name='{{name}}')
```

After hot-swap at runtime:
```python
# Update session_state with active personality
session_state['active_personality'] = 'per_{{name}}'
# Log switch to episodic_memory
episodic_store.append({'event': 'personality_swap', 'to': 'per_{{name}}', 'timestamp': now})
```

## Do NOT Persist
- Raw conversation content in personality artifacts
- User-specific preferences inside personality definition (use user_model instead)
- Capability overrides (personality is voice only -- no memory of capabilities)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_mental_model]] | upstream | 0.24 |
| [[bld_architecture_session_state]] | upstream | 0.24 |
| [[memory-scope-builder]] | upstream | 0.21 |
| [[bld_architecture_memory_scope]] | upstream | 0.20 |
| [[p03_sp_memory_scope_builder]] | upstream | 0.20 |
| [[p01_kc_memory_scope]] | upstream | 0.19 |
| [[session-state-builder]] | related | 0.17 |
| [[p03_sp_session_state_builder]] | upstream | 0.16 |
| [[bld_collaboration_session_state]] | related | 0.15 |
| [[p01_kc_session_state]] | related | 0.15 |
