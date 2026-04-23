---
kind: memory
id: bld_memory_messaging_gateway
pillar: P10
llm_function: INJECT
purpose: P10 memory hooks for messaging_gateway builder -- what to remember across sessions
quality: 8.6
title: "Memory Hooks: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, memory, p10, hermes_origin]
tldr: "Memory hooks: track active platforms, security posture decisions, DP5 stub status, and Honcho wiring per deployment."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.89
related:
  - p01_kc_memory_persistence
  - bld_architecture_entity_memory
  - bld_collaboration_entity_memory
  - entity-memory-builder
  - p01_kc_memory_scope
  - p10_rs_conversation
  - p03_sp_entity_memory_builder
  - p01_kc_entity_memory
  - bld_collaboration_memory_scope
  - session-state-builder
---

# Memory Hooks: messaging_gateway Builder

## What to Remember Across Sessions
When a messaging_gateway artifact is produced, record these facts in session memory:

### Deployment-Level Facts
| Fact | Memory Kind | Why |
|------|-------------|-----|
| active_platforms at build time | entity_memory | Avoid redundant re-configuration |
| security.allowed_user_ids decisions | entity_memory | User-specific access policy |
| command_approval_list decisions | entity_memory | Privileged command surface |
| voice_memo_transcription toggle | entity_memory | stt_provider dependency tracking |
| Primary gateway id (p04_mg_X) | entity_memory | Cross-reference in handoffs |

### Builder-Level Facts
| Fact | Memory Kind | Why |
|------|-------------|-----|
| GDP decisions (DP5 confirmed) | learning_record | Never re-ask this decision |
| Platform transport choices | learning_record | Reuse in future gateway builds |
| Deployment context (dev vs prod) | entity_memory | Security posture calibration |

## Integration with P10
The messaging_gateway spec is stateless between turns. All durable state lives in P10:

```
messaging_gateway artifact
  |
  +-> user_model (P10, user-model-builder)
  |     peer_id, collections, dialectic loop config
  |
  +-> session_state (P10, session-state-builder)
        ephemeral conversation snapshot per turn
```

The gateway ARTIFACT does not store user data. It only specifies the interface.
Actual user memory belongs to `user_model`. Actual session state belongs to `session_state`.

## Memory Anti-Patterns (NEVER store in messaging_gateway)
- Bot tokens or platform credentials -> these go in .cex/config/
- User messages or conversation history -> these go in session_state (P10)
- Derived user facts -> these go in user_model (P10) Collections
- Active platform connection state -> this is runtime, not spec

## Compaction Trigger
If a session produces multiple messaging_gateway builds (multi-platform deployment),
compact into one entity_memory record:
```
entity: p10_em_gateway_deployment_{workspace}
attributes:
  active_platforms: [telegram, discord]
  security_posture: production (dm_pairing + allowlist)
  voice_enabled: false
  hermes_version: DP5_stub
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_persistence]] | upstream | 0.39 |
| [[bld_architecture_entity_memory]] | upstream | 0.37 |
| [[bld_collaboration_entity_memory]] | downstream | 0.37 |
| [[entity-memory-builder]] | related | 0.32 |
| [[p01_kc_memory_scope]] | upstream | 0.32 |
| [[p10_rs_conversation]] | related | 0.31 |
| [[p03_sp_entity_memory_builder]] | related | 0.30 |
| [[p01_kc_entity_memory]] | related | 0.30 |
| [[bld_collaboration_memory_scope]] | downstream | 0.29 |
| [[session-state-builder]] | related | 0.29 |
