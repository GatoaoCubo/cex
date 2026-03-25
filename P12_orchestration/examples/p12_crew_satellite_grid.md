---
id: p12_crew_satellite_grid
type: crew
lp: P12
description: "Multi-satellite crew configuration for parallel task execution via spawn_grid"
version: 1.0.0
created: 2026-03-25
author: stella
quality: 9.0
tags: [crew, multi-agent, grid, parallel, orchestration]
---

# Crew: Satellite Grid

## Purpose
Defines how N satellites collaborate on a mission. The crew is NOT the agents — it is the PROTOCOL that coordinates them.

## Configuration
```yaml
crew:
  name: "GENESIS"
  coordinator: STELLA
  protocol: parallel_grid
  
  members:
    - satellite: SHAKA
      role: researcher
      model: sonnet
      tasks_from: ".claude/handoffs/GENESIS_batch_*_shaka.md"
    - satellite: EDISON
      role: builder
      model: opus
      tasks_from: ".claude/handoffs/GENESIS_batch_*_edison.md"
    - satellite: PYTHA
      role: knowledge
      model: sonnet
      tasks_from: ".claude/handoffs/GENESIS_batch_*_pytha.md"

  coordination:
    max_parallel: 6
    mode: continuous  # static | continuous
    shared_state: git_repo  # all read/write same repo
    conflict_resolution: file_isolation  # each satellite edits different files
    
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
P01=shared pool, P02=N satellites, P03=mission goal, P04=shared MCPs,
P06=file isolation contract, P07=quality gates, P09=grid config,
P10=shared git state, P11=monitor watchdog, P12=signal protocol.
