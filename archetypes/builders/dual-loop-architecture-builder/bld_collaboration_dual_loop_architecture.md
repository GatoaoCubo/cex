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
