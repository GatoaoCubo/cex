---
kind: collaboration
id: bld_collaboration_self_improvement_loop
pillar: P12
llm_function: COLLABORATE
purpose: How self_improvement_loop-builder works in crews with other builders
quality: 8.9
title: "Collaboration Self Improvement Loop"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [self_improvement_loop, builder, collaboration]
tldr: "How self_improvement_loop-builder works in crews with other builders"
domain: "self_improvement_loop construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Coordinates iterative refinement of processes, goals, and strategies through active feedback integration and adaptive planning.  

## Receives From  
| Builder       | What               | Format      |  
|---------------|--------------------|-------------|  
| Feedback_Collector | User performance data | Structured JSON |  
| Goal_Setter   | Target milestones   | Plain text  |  
| Analyzer      | Improvement insights | Markdown    |  
| Planner       | Actionable steps    | YAML        |  

## Produces For  
| Builder       | What                   | Format      |  
|---------------|------------------------|-------------|  
| Executor      | Updated task sequences | JSON        |  
| Reporter      | Progress summaries     | Markdown    |  
| Goal_Setter   | Revised objectives     | Plain text  |  
| Analyzer      | Next-phase hypotheses  | YAML        |  

## Boundary  
Does NOT handle bug-specific fixes (handled by `bugloop`), passive learning (handled by `learning_record`), or external system integrations (handled by `interface_builder`).
