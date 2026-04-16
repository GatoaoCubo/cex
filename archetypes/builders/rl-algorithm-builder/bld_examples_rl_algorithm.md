---
kind: examples
id: bld_examples_rl_algorithm
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of rl_algorithm artifacts
quality: 8.9
title: "Examples Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, examples]
tldr: "Golden and anti-examples of rl_algorithm artifacts"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
name: "PPO"
description: "Proximal Policy Optimization algorithm for model-free reinforcement learning"
version: "1.0"
author: "OpenAI"
keywords: ["policy gradient", "actor-critic", "on-policy"]
---

**Algorithm Components**:
- **Agent**: Uses parameterized policy π(a|s) and value function V(s)
- **Environment**: Continuous action space, episodic tasks
- **Policy Update**: Clipped surrogate objective with trust region constraint
- **Value Function**: Neural network approximator with TD error loss
- **Training Loop**:
  1. Collect trajectories with current policy
  2. Compute advantages via generalized advantage estimation
  3. Update policy and value function via stochastic gradient ascent
- **Hyperparameters**:
  - Clip range ε = 0.2
  - Generalized advantage estimation parameter λ = 0.95
  - Policy and value network learning rates
```

## Anti-Example 1: Conflating with Training Method
```markdown
---
name: "Experience Replay"
description: "Stochastic gradient descent with memory buffer"
version: "0.1"
author: "Unknown"
keywords: ["replay buffer", "off-policy"]
---

**Training Process**:
- Store transitions in a FIFO buffer
- Sample mini-batches randomly during training
- Update Q-network using Bellman equation
- Use target network for stability
```
## Why it fails
Experience replay is a training technique, not an RL algorithm. It lacks core algorithmic components like policy definition, value function formulation, and learning objective specification.

## Anti-Example 2: Confusing with Reward Model
```markdown
---
name: "Inverse Reward Design"
description: "Reward function inference from expert demonstrations"
version: "1.0"
author: "MIT"
keywords: ["reward shaping", "inverse reinforcement learning"]
---

**Reward Model**:
- Uses maximum entropy principle
- Learns potential function φ(s) from demonstrations
- Computes reward as Δφ(s)
- Regularizes with KL divergence to expert policy
```
## Why it fails
This defines a reward model (part of the environment), not an RL algorithm. It lacks agent policy definition, learning process, and algorithm-specific training procedure.
