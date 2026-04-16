---
kind: collaboration
id: bld_collaboration_thinking_config
pillar: P12
llm_function: COLLABORATE
purpose: How thinking_config-builder works in crews with other builders
quality: 8.9
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

This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.
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
Does NOT define reasoning techniques (handled by reasoning_strategy builder) or input token
limits (handled by context_window_config builder) or task effort profiles (handled by
effort_profile builder).

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | thinking_config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
