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
