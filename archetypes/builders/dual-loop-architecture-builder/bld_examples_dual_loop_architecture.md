---
kind: examples
id: bld_examples_dual_loop_architecture
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of dual_loop_architecture artifacts
quality: 8.9
title: "Examples Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, examples]
tldr: "Golden and anti-examples of dual_loop_architecture artifacts"
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.
```yaml
title: Autonomous Vehicle Control System
kind: dual_loop_architecture
description: >-
  Outer loop handles route planning; inner loop manages real-time steering/throttle.
  Feedback ensures alignment between high-level goals and low-level execution.
outer_loop:
  - name: Path Planner
    inputs: [destination, map, traffic data]
    outputs: [desired trajectory]
inner_loop:
  - name: Vehicle Controller
    inputs: [trajectory, sensor data]
    outputs: [steering, throttle, brake]
feedback:
  - from: Vehicle Controller
    to: Path Planner
    metric: deviation from trajectory
```

## Anti-Example 1: Linear Workflow Misinterpretation
```yaml
title: Misinterpreted Workflow
kind: dual_loop_architecture
description: >-
  "Outer loop" processes data sequentially, then passes to "inner loop" for final output.
outer_loop:
  - name: Data Processor
    inputs: [raw data]
    outputs: [processed data]
inner_loop:
  - name: Finalizer
    inputs: [processed data]
    outputs: [result]
```
## Why it fails
Lacks bidirectional feedback and real-time adjustment. Treats loops as sequential stages, violating dual-loop control's core principle of continuous interaction between high-level planning and low-level execution.

## Anti-Example 2: Merged Loop Architecture
```yaml
title: Monolithic Controller
kind: dual_loop_architecture
description: >-
  Single agent handles both planning and execution without clear separation.
agent:
  - name: Unified Controller
    inputs: [goals, sensor data]
    outputs: [actions]
```
## Why it fails
Blurs separation between strategic planning (outer loop) and tactical execution (inner loop). Loses modularity and fails to enable independent optimization of each control layer, making system adaptation and debugging difficult.
