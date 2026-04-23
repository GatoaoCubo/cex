---
kind: collaboration
id: bld_collaboration_reasoning_strategy
pillar: P12
llm_function: COLLABORATE
purpose: How reasoning_strategy-builder works in crews with other builders
quality: 8.9
title: "Collaboration Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, collaboration]
tldr: "How reasoning_strategy-builder works in crews with other builders"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_search_strategy
  - p03_sp_reasoning_strategy_builder
  - reasoning-strategy-builder
  - bld_tools_reasoning_strategy
  - p01_kc_prompt_engineering_best_practices
  - bld_output_template_reasoning_strategy
  - bld_instruction_reasoning_strategy
  - bld_collaboration_reward_model
  - bld_collaboration_product_tour
  - bld_config_reasoning_strategy
---

## Crew Role  

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
Designs structured reasoning approaches to solve complex problems, ensuring alignment with team objectives and technical constraints.  

## Receives From  
| Builder              | What                  | Format          |  
|----------------------|-----------------------|-----------------|  
| Problem_Definition_Builder | Problem scope & constraints | Structured document |  
| Knowledge_Base_Builder     | Relevant data sources   | Dataset schema  |  
| Feedback_Collector         | Prior strategy outcomes | Feedback report |  

## Produces For  
| Builder              | What                  | Format          |  
|----------------------|-----------------------|-----------------|  
| Solution_Architect   | Strategy implementation plan | Technical spec |  
| Evaluation_Framework_Builder | Metrics for success | Assessment config |  
| Documentation_Builder | Strategy rationale    | Technical doc   |  

## Boundary  
Does NOT handle prompt engineering (prompt_technique) or resource allocation (thinking_config). Prompt engineering is managed by Prompt_Engineer; resource allocation by Resource_Allocator.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_search_strategy]] | sibling | 0.28 |
| [[p03_sp_reasoning_strategy_builder]] | upstream | 0.27 |
| [[reasoning-strategy-builder]] | upstream | 0.27 |
| [[bld_tools_reasoning_strategy]] | upstream | 0.27 |
| [[p01_kc_prompt_engineering_best_practices]] | upstream | 0.26 |
| [[bld_output_template_reasoning_strategy]] | upstream | 0.25 |
| [[bld_instruction_reasoning_strategy]] | upstream | 0.25 |
| [[bld_collaboration_reward_model]] | sibling | 0.25 |
| [[bld_collaboration_product_tour]] | sibling | 0.23 |
| [[bld_config_reasoning_strategy]] | upstream | 0.23 |
