---
kind: collaboration
id: bld_collaboration_dual_loop_architecture
pillar: P12
llm_function: COLLABORATE
purpose: How dual_loop_architecture-builder works in crews with other builders
quality: 8.9
title: "Collaboration Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, collaboration]
tldr: "How dual_loop_architecture-builder works in crews with other builders"
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_knowledge_card_dual_loop_architecture
  - dual-loop-architecture-builder
  - p03_sp_dual_loop_architecture_builder
  - kc_dual_loop_architecture
  - p10_lr_dual_loop_architecture_builder
  - bld_instruction_dual_loop_architecture
  - p08_qg_dual_loop_architecture
  - bld_examples_dual_loop_architecture
  - bld_tools_dual_loop_architecture
  - bld_architecture_dual_loop_architecture
---

## Crew Role  

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.
Coordinates dual-loop control systems by maintaining real-time feedback (inner loop) and strategic adaptation (outer loop), ensuring alignment between operational execution and long-term goals.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Inner Loop    | Sensor data           | JSON        |  
| Outer Loop    | Strategic parameters  | YAML        |  
| Monitor       | Performance metrics   | Custom      |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Inner Loop    | Control adjustments   | JSON        |  
| Outer Loop    | Status summaries      | YAML        |  
| Logger        | System diagnostics    | Custom      |  

## Boundary  
Does NOT handle external stakeholder communication (handled by dedicated interface agents) or resource allocation (managed by orchestration layer). Focuses strictly on loop synchronization and control logic.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_dual_loop_architecture]] | upstream | 0.70 |
| [[dual-loop-architecture-builder]] | upstream | 0.67 |
| [[p03_sp_dual_loop_architecture_builder]] | upstream | 0.64 |
| [[kc_dual_loop_architecture]] | upstream | 0.62 |
| [[p10_lr_dual_loop_architecture_builder]] | upstream | 0.58 |
| [[bld_instruction_dual_loop_architecture]] | upstream | 0.55 |
| [[p08_qg_dual_loop_architecture]] | upstream | 0.51 |
| [[bld_examples_dual_loop_architecture]] | upstream | 0.47 |
| [[bld_tools_dual_loop_architecture]] | upstream | 0.47 |
| [[bld_architecture_dual_loop_architecture]] | upstream | 0.43 |
