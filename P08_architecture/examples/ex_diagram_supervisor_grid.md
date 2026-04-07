---
id: p08_diag_agent_group_grid
kind: diagram
pillar: P08
description: "Architecture diagram of orchestrator agent_group grid dispatch"
format: ascii
scope: orchestration
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [diagram, architecture, grid, agent_group, orchestration]
---

# Diagram: Agent_group Grid Dispatch

## Overview
orchestrator orchestrates up to 6 parallel agent_groups via PowerShell spawn scripts.

## Architecture
```
                    USER INPUT
                        |
                    [orchestrator]
                   (pi runtime)
                   /    |    \
          [HANDOFF] [HANDOFF] [HANDOFF]
              |         |         |
    +---------+---------+---------+---------+
    |  spawn_grid.ps1 (up to 6 slots)      |
    |  MoveWindow positioning (640x520 ea)  |
    +---------+---------+---------+---------+
         |         |         |
    [builder_agent]  [research_agent]   [marketing_agent]
    (opus)    (sonnet)   (sonnet)
    boot/     boot/      boot/
    edison    shaka      lily
    .cmd      .cmd       .cmd
         |         |         |
    [COMMIT]  [COMMIT]  [COMMIT]
         |         |         |
    [SIGNAL]  [SIGNAL]  [SIGNAL]
         \         |         /
          spawn_monitor.ps1
                |
           [orchestrator]
          (collect + push)
```

## Key Properties
- Max 6 slots for short tasks (<15min), 3 for long (>30min)
- Each agent_group: own CMD window, own Claude session, own MCP config
- Continuous mode: slot completes -> next batch auto-dispatched
- Isolation: agent_groups share git repo but never edit same files
