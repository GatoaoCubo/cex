---
id: p08_diag_satellite_grid
kind: diagram
pillar: P08
description: "Architecture diagram of STELLA satellite grid dispatch"
format: ascii
scope: orchestration
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [diagram, architecture, grid, satellite, orchestration]
---

# Diagram: Satellite Grid Dispatch

## Overview
STELLA orchestrates up to 6 parallel satellites via PowerShell spawn scripts.

## Architecture
```
                    USER INPUT
                        |
                    [STELLA]
                   (pi runtime)
                   /    |    \
          [HANDOFF] [HANDOFF] [HANDOFF]
              |         |         |
    +---------+---------+---------+---------+
    |  spawn_grid.ps1 (up to 6 slots)      |
    |  MoveWindow positioning (640x520 ea)  |
    +---------+---------+---------+---------+
         |         |         |
    [EDISON]  [SHAKA]   [LILY]
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
           [STELLA]
          (collect + push)
```

## Key Properties
- Max 6 slots for short tasks (<15min), 3 for long (>30min)
- Each satellite: own CMD window, own Claude session, own MCP config
- Continuous mode: slot completes -> next batch auto-dispatched
- Isolation: satellites share git repo but never edit same files
