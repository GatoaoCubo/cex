---
kind: instruction
id: bld_instruction_rl_algorithm
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for rl_algorithm
quality: 8.9
title: "Instruction Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, instruction]
tldr: "Step-by-step production process for rl_algorithm"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Define problem domain, reward structure, and environment dynamics.  
2. Review RL literature for suitable algorithm (e.g., DQN, PPO, SAC).  
3. Select benchmark environments (e.g., OpenAI Gym, MuJoCo).  
4. Analyze hyperparameter sensitivity and exploration-exploitation tradeoffs.  
5. Identify baseline performance metrics (e.g., cumulative reward, convergence speed).  
6. Document research gaps and algorithmic modifications required.  

## Phase 2: COMPOSE  
1. Implement environment interface per SCHEMA.md (observation/action spaces).  
2. Define RL agent class with policy, value function, and training loop.  
3. Code reward shaping and discount factor (γ) per domain requirements.  
4. Integrate experience replay buffer and noise injection (if applicable).  
5. Write optimizer configuration (learning rates, batch sizes) from OUTPUT_TEMPLATE.md.  
6. Add logging hooks for training metrics (episodes, losses, rewards).  
7. Implement early stopping and checkpointing mechanisms.  
8. Write unit tests for policy update and environment interaction.  
9. Finalize code structure with version control and dependency management.  

## Phase 3: VALIDATE  
[ ] ✅ Unit tests pass for all core functions (policy, loss, update).  
[ ] ✅ Training converges to baseline metrics in benchmark environments.  
[ ] ✅ Hyperparameter sweeps show stable performance across seeds.  
[ ] ✅ Algorithm adheres to SCHEMA.md and OUTPUT_TEMPLATE.md formats.  
[ ] ✅ Documentation covers usage, limitations, and tuning guidelines.
