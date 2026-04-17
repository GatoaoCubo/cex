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
updated: "2026-04-07"
domain: "architecture"
title: "Diagram Supervisor Grid"
density_score: 0.92
tldr: "Defines diagram for diagram supervisor grid, with validation gates and integration points."
---

# Diagram: Agent_group Grid Dispatch

## Overview
orchestrator orchestrates up to 6 parallel agent_groups via PowerShell spawn scripts.

## Architecture
```
                    USER INPUT
                        |
                    [orchestrator]
                   (Claude Code runtime)
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
1. Max 6 slots for short tasks (<15min), 3 for long (>30min)
2. Each agent_group: own CMD window, own Claude session, own MCP config
3. Continuous mode: slot completes -> next batch auto-dispatched
4. Isolation: agent_groups share git repo but never edit same files

## Properties

| Property | Value |
|----------|-------|
| Kind | `diagram` |
| Pillar | P08 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
