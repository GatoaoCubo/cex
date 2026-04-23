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
related:
  - thinking-config-builder
  - p03_sp_thinking_config_builder
  - bld_collaboration_action_paradigm
  - bld_config_thinking_config
  - bld_memory_thinking_config
  - bld_instruction_thinking_config
  - p11_qg_thinking_config
  - bld_collaboration_effort_profile
  - bld_collaboration_prompt_technique
  - bld_examples_thinking_config
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[thinking-config-builder]] | upstream | 0.47 |
| [[p03_sp_thinking_config_builder]] | upstream | 0.42 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.40 |
| [[bld_config_thinking_config]] | upstream | 0.39 |
| [[bld_memory_thinking_config]] | upstream | 0.35 |
| [[bld_instruction_thinking_config]] | upstream | 0.34 |
| [[p11_qg_thinking_config]] | upstream | 0.34 |
| [[bld_collaboration_effort_profile]] | sibling | 0.33 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.33 |
| [[bld_examples_thinking_config]] | upstream | 0.33 |
