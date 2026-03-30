---
id: p10_ss_agent_node_dispatch
kind: session_state
pillar: P10
description: "Ephemeral session state tracking active agent_node dispatches"
scope: stella_session
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [session-state, dispatch, tracking, ephemeral]
---

# Session State: Satellite Dispatch Tracking

## Schema
```yaml
session_id: "stella_2026-03-24T20:00"
active_dispatches:
  - agent_node: edison
    task: "P04 examples from real artifacts"
    started: "2026-03-24T19:45:00Z"
    status: running
    pid: 14624
  - agent_node: shaka
    task: "Market research pet toys"
    started: "2026-03-24T19:50:00Z"
    status: complete
    signal: ".claude/signals/shaka_complete_9.0.json"
waves_completed: 1
total_dispatches: 5
last_monitor_check: "2026-03-24T20:02:00Z"
```

## Lifecycle
- Created: on first dispatch in session
- Updated: on each spawn, signal, or monitor check
- Destroyed: on session end (ephemeral, not persisted to disk)

## Usage
orchestrator uses this to track which agent_nodes are active, avoid double-dispatch, and determine when a wave is complete for collection.
