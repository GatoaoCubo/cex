---
kind: examples
id: bld_examples_trajectory_eval
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of trajectory_eval artifacts
quality: 8.9
title: "Examples Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, examples]
tldr: "Golden and anti-examples of trajectory_eval artifacts"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
cex_kind: trajectory_eval
title: "Trajectory Evaluation of RL Agent in Maze Navigation"
description: "Evaluation of a reinforcement learning agent's trajectory in a simulated maze environment using Stable Baselines3 and Gym."
tags: [reinforcement_learning, trajectory_analysis, gym]
---

**Methodology**:
- **Environment**: OpenAI Gym's `MiniGrid-Maze-10x10-v0`
- **Agent**: PPO algorithm implemented with Stable Baselines3 (version 2.0.0)
- **Evaluation Metrics**:
  - Path efficiency (shortest path vs. taken path)
  - Collision rate
  - Time to goal
- **Setup**: 100 episodes, 5 random seeds, 1000 steps per episode
- **Results**:
  - Average path efficiency: 85%
  - Collision rate: 2.3%
  - Time to goal: 120 steps (±15)
```

## Anti-Example 1: Confusing with Static Benchmark
```markdown
---
cex_kind: trajectory_eval
title: "Static Benchmark for Language Model"
description: "Evaluation of a language model on GLUE benchmark tasks."
tags: [nlp, benchmark]
---

**Methodology**:
- **Model**: Hugging Face's `bert-base-uncased`
- **Tasks**: MNLI, SST-2, QQP
- **Metrics**: Accuracy, F1 score
- **Results**:
  - MNLI: 87% accuracy
  - SST-2: 92% accuracy
```
## Why it fails
This example evaluates a static model on benchmark tasks, not agent trajectories. It lacks environment interaction, episode-based metrics, and trajectory-specific analysis.

## Anti-Example 2: Missing Environment Details
```markdown
---
cex_kind: trajectory_eval
title: "Unspecified Agent Evaluation"
description: "Evaluation of an unspecified agent in an unspecified environment."
tags: [unknown]
---

**Methodology**:
- **Agent**: [Not specified]
- **Environment**: [Not specified]
- **Metrics**:
  - "Success rate"
  - "Reward"
- **Results**:
  - "Success rate: 70%"
```
## Why it fails
The example lacks critical details about the environment, agent, and evaluation setup. Metrics like "success rate" are vague without context, making the evaluation non-reproducible and unverifiable.
