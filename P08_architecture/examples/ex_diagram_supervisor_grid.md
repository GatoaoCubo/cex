---
id: p08_diag_agent_node_grid
kind: diagram
pillar: P08
description: "Architecture diagram of orchestrator agent_node grid dispatch"
format: ascii
scope: orchestration
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [diagram, architecture, grid, agent_node, orchestration]
---

# Diagram: Satellite Grid Dispatch

## Overview
orchestrator orchestrates up to 6 parallel agent_nodes via PowerShell spawn scripts.

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
- Each agent_node: own CMD window, own Claude session, own MCP config
- Continuous mode: slot completes -> next batch auto-dispatched
- Isolation: agent_nodes share git repo but never edit same files
