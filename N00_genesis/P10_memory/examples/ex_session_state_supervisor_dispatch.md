---
id: p10_ss_agent_group_dispatch
kind: session_state
8f: F8_collaborate
pillar: P10
description: "Ephemeral session state tracking active agent_group dispatches"
scope: stella_session
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [session-state, dispatch, tracking, ephemeral]
updated: "2026-04-07"
domain: "memory"
title: "Session State Supervisor Dispatch"
density_score: 0.92
tldr: "Defines session state for session state supervisor dispatch, with validation gates and integration points."
related:
  - p12_sig_agent_group_complete
  - dispatch-rule-builder
  - p06_vs_signal_completion
  - p01_kc_session_state
  - session-state-builder
  - bld_memory_session_state
  - signal-builder
  - p03_up_dispatch_agent_group
  - agent-card-builder
  - bld_collaboration_session_state
---

# Session State: Agent_group Dispatch Tracking

## Schema
```yaml
session_id: "stella_2026-03-24T20:00"
active_dispatches:
  - agent_group: edison
    task: "P04 examples from real artifacts"
    started: "2026-03-24T19:45:00Z"
    status: running
    pid: 14624
  - agent_group: shaka
    task: "Market research pet toys"
    started: "2026-03-24T19:50:00Z"
    status: complete
    signal: ".claude/signals/shaka_complete_9.0.json"
waves_completed: 1
total_dispatches: 5
last_monitor_check: "2026-03-24T20:02:00Z"
```

## Lifecycle
1. Created: on first dispatch in session
2. Updated: on each spawn, signal, or monitor check
3. Destroyed: on session end (ephemeral, not persisted to disk)

## Usage
orchestrator uses this to track which agent_groups are active, avoid double-dispatch, and determine when a wave is complete for collection.

## Properties

| Property | Value |
|----------|-------|
| Kind | `session_state` |
| Pillar | P10 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_sig_agent_group_complete]] | downstream | 0.34 |
| [[dispatch-rule-builder]] | downstream | 0.31 |
| [[p06_vs_signal_completion]] | upstream | 0.31 |
| [[p01_kc_session_state]] | related | 0.28 |
| [[session-state-builder]] | related | 0.27 |
| [[bld_memory_session_state]] | related | 0.26 |
| [[signal-builder]] | downstream | 0.26 |
| [[p03_up_dispatch_agent_group]] | upstream | 0.26 |
| [[agent-card-builder]] | upstream | 0.26 |
| [[bld_collaboration_session_state]] | related | 0.25 |
