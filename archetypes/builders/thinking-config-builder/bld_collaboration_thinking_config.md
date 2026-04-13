---
kind: collaboration
id: bld_collaboration_thinking_config
pillar: P12
llm_function: COLLABORATE
purpose: How thinking_config-builder works in crews with other builders
quality: null
title: "Collaboration Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, collaboration]
tldr: "How thinking_config-builder works in crews with other builders"
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Allocates and enforces thinking budget constraints (e.g., time, computational resources) for consistent reasoning execution.  

## Receives From  
| Builder       | What             | Format  |  
|---------------|------------------|---------|  
| Planner       | Budget parameters | JSON    |  
| Validator     | Constraint rules  | YAML    |  
| Monitor       | Resource limits   | CSV     |  

## Produces For  
| Builder       | What               | Format  |  
|---------------|--------------------|---------|  
| Executor      | Thinking config    | JSON    |  
| Reporter      | Budget report      | YAML    |  
| Allocator     | Allocation plan    | CSV     |  

## Boundary  
Does NOT define reasoning techniques (handled by `reasoning_strategy_builder`) or token limits (handled by `context_window_config_builder`).
