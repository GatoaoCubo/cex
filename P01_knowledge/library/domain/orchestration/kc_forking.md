---
id: p01_kc_forking
kind: knowledge_card
type: domain
pillar: P01
title: "Forking and Branching — Parallel Agent Execution"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
quality: 8.7
tags: [forking, branching, parallel, fan-out, spawn]
tldr: "Fork execution into parallel branches, each agent handles a subset, fan-in to collect results. Git branching model applied to agent work."
when_to_use: "Designing parallel execution strategies for multi-agent systems"
keywords: [forking, branching, parallel, fan-out, fan-in, spawn]
density_score: 0.91
---

# Forking and Branching

## The Pattern
```
PLAN (sequential)
  → FORK: dispatch N agents in parallel
    → Agent A: task 1
    → Agent B: task 2
    → Agent C: task 3
  → FAN-IN: collect all results
→ CONSOLIDATE (sequential)
```

## Fork Strategies

| Strategy | When | Risk |
|----------|------|------|
| Independent | Tasks share no state | None (ideal) |
| Shared-read | Tasks read same config/brand | Low (read-only) |
| Merge-later | Tasks may overlap, reconcile after | Medium (conflicts) |
| Pipeline fork | Tasks form sub-pipelines | Dependency complexity |

## CEX Implementation
- `_spawn/spawn_grid.ps1` = fork up to 6 nuclei
- Each nucleus = separate window/process
- Shared filesystem = coordination layer
- Signals = fan-in mechanism
- `/consolidate` = post-fork reconciliation
- Wave-based dispatch = controlled forking (W1 done → fork W2)
