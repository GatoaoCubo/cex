---
kind: collaboration
id: bld_collaboration_rl_algorithm
pillar: P12
llm_function: COLLABORATE
purpose: How rl_algorithm-builder works in crews with other builders
quality: 8.9
title: "Collaboration Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, collaboration]
tldr: "How rl_algorithm-builder works in crews with other builders"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_reward_model
  - bld_tools_training_method
  - reward-model-builder
  - training-method-builder
  - p03_sp_training_method_builder
  - bld_knowledge_card_training_method
  - rl-algorithm-builder
  - bld_examples_rl_algorithm
  - bld_instruction_rl_algorithm
  - p03_sp_reward_model_builder
---

## Crew Role  
Designs and implements core reinforcement learning algorithms (e.g., policy gradient, Q-learning), ensuring compatibility with environment interfaces and training protocols.  

## Receives From  
| Builder          | What                  | Format      |  
|------------------|-----------------------|-------------|  
| Environment      | Observation/action specs | YAML        |  
| Reward_Model     | Reward function       | JSON        |  
| Training_Method  | Optimization strategy | Python module |  

## Produces For  
| Builder          | What                  | Format      |  
|------------------|-----------------------|-------------|  
| Training_Method  | Algorithm interface   | Python class |  
| Hyperparameter   | Configurable parameters | JSON        |  
| Evaluation       | Performance metrics   | CSV         |  

## Boundary  
Does NOT define training loops, hyperparameter schedules, or reward functions. Training_Method handles optimization, Reward_Model defines reward logic, and Environment provides interaction specs.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_reward_model]] | sibling | 0.36 |
| [[bld_tools_training_method]] | upstream | 0.34 |
| [[reward-model-builder]] | upstream | 0.34 |
| [[training-method-builder]] | upstream | 0.32 |
| [[p03_sp_training_method_builder]] | upstream | 0.31 |
| [[bld_knowledge_card_training_method]] | upstream | 0.31 |
| [[rl-algorithm-builder]] | upstream | 0.30 |
| [[bld_examples_rl_algorithm]] | upstream | 0.30 |
| [[bld_instruction_rl_algorithm]] | upstream | 0.29 |
| [[p03_sp_reward_model_builder]] | upstream | 0.29 |
