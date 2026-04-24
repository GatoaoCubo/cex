---
id: p01_kc_forking
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Forking and Branching — Parallel Agent Execution"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
quality: 9.0
tags: [forking, branching, parallel, fan-out, spawn]
tldr: "Fork execution into parallel branches, each agent handles a subset, fan-in to collect results. Git branching model applied to agent work."
when_to_use: "Designing parallel execution strategies for multi-agent systems"
keywords: [forking, branching, parallel, fan-out, fan-in, spawn]
density_score: 0.91
updated: "2026-04-07"
related:
  - p01_kc_coordination
  - spec_infinite_bootstrap_loop
  - p01_kc_anti_isolated_sessions
  - kc_workflow_run_crate
  - p01_kc_distillation_pipeline
  - p03_pt_orchestration_task_dispatch
  - kc_n07_orchestrator
  - spec_claude_native_hardening
  - continuous_batching_report
  - p12_wp_map_reduce
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

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_coordination]] | sibling | 0.29 |
| [[spec_infinite_bootstrap_loop]] | related | 0.26 |
| [[p01_kc_anti_isolated_sessions]] | sibling | 0.26 |
| [[kc_workflow_run_crate]] | related | 0.24 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.23 |
| [[p03_pt_orchestration_task_dispatch]] | downstream | 0.22 |
| [[kc_n07_orchestrator]] | sibling | 0.21 |
| [[spec_claude_native_hardening]] | related | 0.20 |
| [[continuous_batching_report]] | related | 0.19 |
| [[p12_wp_map_reduce]] | downstream | 0.19 |
