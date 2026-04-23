---
quality: 8.4
quality: 8.0
kind: memory
id: bld_memory_terminal_backend
pillar: P10
llm_function: INJECT
purpose: Memory hooks for terminal_backend builder
title: "Memory Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, memory]
tldr: "Memory hooks: persist active backend selection, cost alerts, session outcomes for routing decisions"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.88
related:
  - bld_architecture_entity_memory
  - bld_collaboration_session_backend
  - session-backend-builder
  - bld_architecture_session_backend
  - bld_collaboration_entity_memory
  - p03_sp_session_backend_builder
  - p01_kc_memory_persistence
  - p01_kc_session_backend
  - bld_tools_session_backend
  - p11_qg_entity_memory
---

## What to Persist

| Event | Memory Type | KC to Update |
|-------|------------|-------------|
| Backend switched | entity_memory | Record active backend per nucleus |
| Cost threshold exceeded | entity_memory | Flag backend as high-cost for routing |
| Session timeout hit | learning_record | Log timeout_seconds was too short |
| Auth failure | entity_memory | Mark backend as auth-broken, alert N05 |
| Hibernation trigger | entity_memory | Record idle duration that triggered hibernation |

## Memory Hooks

### On Successful Session
```
entity_memory: {nucleus}_active_backend = {backend_type}
learning_record: session completed, backend={backend_type}, duration_seconds={actual}
```

### On Cost Alert
```
entity_memory: {backend_type}_cost_flagged = true
signal: write_signal('n05', 'cost_alert', backend={backend_type}, usd_per_hour={estimate})
```

### On Auth Failure
```
entity_memory: {backend_type}_auth_status = 'broken'
signal: write_signal('n05', 'auth_failure', backend={backend_type}, secret_ref={ref})
```

## Routing Influence
N07 reads `entity_memory` before dispatching to prefer:
1. Backends with `auth_status != 'broken'`
2. Backends where cost < `cost_alert_threshold_usd_per_hour`
3. Backends matching the task's compute profile (GPU -> modal, HPC -> singularity)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_entity_memory]] | upstream | 0.35 |
| [[bld_collaboration_session_backend]] | downstream | 0.32 |
| [[session-backend-builder]] | upstream | 0.28 |
| [[bld_architecture_session_backend]] | upstream | 0.27 |
| [[bld_collaboration_entity_memory]] | downstream | 0.26 |
| [[p03_sp_session_backend_builder]] | upstream | 0.26 |
| [[p01_kc_memory_persistence]] | upstream | 0.25 |
| [[p01_kc_session_backend]] | related | 0.25 |
| [[bld_tools_session_backend]] | upstream | 0.25 |
| [[p11_qg_entity_memory]] | downstream | 0.25 |
