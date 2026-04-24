---
id: p12_crew_agent_group_grid
kind: crew
8f: F8_collaborate
pillar: P12
description: "Multi-agent_group crew configuration for parallel task execution via spawn_grid"
version: 1.0.0
created: 2026-03-25
author: orchestrator
quality: 9.1
tags: [crew, multi-agent, grid, parallel, orchestration]
updated: "2026-04-07"
domain: "orchestration"
title: "Workflow Supervisor Grid"
density_score: 0.92
tldr: "Defines crew for workflow supervisor grid, with validation gates and integration points."
related:
  - p12_spawn_grid_continuous
  - bld_collaboration_agent_card
  - p12_wf_stella_dispatch
  - bld_collaboration_spawn_config
  - tpl_validation_schema
  - agent-card-builder
  - p12_sig_agent_group_complete
  - skill
  - p08_diag_agent_group_grid
  - p01_kc_spawn_config
---

# Crew: Agent_group Grid

## Purpose
Defines how N agent_groups collaborate on a mission. The crew is NOT the agents — it is the PROTOCOL that coordinates them.

## Configuration
```yaml
crew:
  name: "GENESIS"
  coordinator: orchestrator
  protocol: parallel_grid
  
  members:
    - agent_group: research_agent
      role: researcher
      model: sonnet
      tasks_from: ".claude/handoffs/GENESIS_batch_*_shaka.md"
    - agent_group: builder_agent
      role: builder
      model: opus
      tasks_from: ".claude/handoffs/GENESIS_batch_*_edison.md"
    - agent_group: knowledge_agent
      role: knowledge
      model: sonnet
      tasks_from: ".claude/handoffs/GENESIS_batch_*_pytha.md"

  coordination:
    max_parallel: 6
    mode: continuous  # static | continuous
    shared_state: git_repo  # all read/write same repo
    conflict_resolution: file_isolation  # each agent_group edits different files
    
  lifecycle:
    spawn: "spawn_grid.ps1 -mission GENESIS -mode continuous"
    monitor: "spawn_monitor.ps1 (30s poll)"
    completion: "all signals received"
    cleanup: "spawn_stop.ps1 + archive handoffs"

  termination:
    condition: all_signals_complete
    timeout: 60m
    on_stuck: escalate_to_stella
```

## The crew is a fractal of 12 LPs
A crew instantiates ALL 12 LPs at the group level:
P01=shared pool, P02=N agent_groups, P03=mission goal, P04=shared MCPs,
P06=file isolation contract, P07=quality gates, P09=grid config,
P10=shared git state, P11=monitor watchdog, P12=signal protocol.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `crew` |
| Pillar | P12 |
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
| [[p12_spawn_grid_continuous]] | related | 0.31 |
| [[bld_collaboration_agent_card]] | upstream | 0.30 |
| [[p12_wf_stella_dispatch]] | related | 0.29 |
| [[bld_collaboration_spawn_config]] | related | 0.29 |
| [[tpl_validation_schema]] | upstream | 0.28 |
| [[agent-card-builder]] | upstream | 0.27 |
| [[p12_sig_agent_group_complete]] | related | 0.27 |
| [[skill]] | upstream | 0.27 |
| [[p08_diag_agent_group_grid]] | upstream | 0.27 |
| [[p01_kc_spawn_config]] | related | 0.26 |
