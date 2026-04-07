---
id: p12_crew_agent_group_grid
kind: crew
pillar: P12
description: "Multi-agent_group crew configuration for parallel task execution via spawn_grid"
version: 1.0.0
created: 2026-03-25
author: orchestrator
quality: 9.0
tags: [crew, multi-agent, grid, parallel, orchestration]
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
