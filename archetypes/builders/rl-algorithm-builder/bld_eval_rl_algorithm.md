---
kind: quality_gate
id: p02_qg_rl_algorithm
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for rl_algorithm
quality: 9.1
title: "Quality Gate Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for rl_algorithm"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_rl_algorithm
  - rl-algorithm-builder
  - bld_instruction_rl_algorithm
  - bld_knowledge_card_rl_algorithm
  - bld_output_template_rl_algorithm
  - bld_examples_reward_model
  - p03_sp_rl_algorithm_builder
  - bld_tools_reward_model
  - p10_lr_rl_algorithm_builder
  - p07_qg_benchmark_suite
---

## Quality Gate

## Definition
| metric               | threshold         | operator | scope          |
|----------------------|-------------------|----------|----------------|
| Training loss        | <= 0.1            | <=       | All episodes   |
| Reward convergence   | >= 95%            | >=       | Final 10%      |
| Training duration    | <= 72h            | <=       | Per experiment |

## HARD Gates
| ID   | Check                  | Fail Condition                          |
|------|------------------------|-----------------------------------------|
| H01  | YAML valid             | Invalid YAML syntax                     |
| H02  | ID matches pattern     | ID does not match `^p02_rla_[a-zA-Z0-9_]+$` |
| H03  | Kind matches           | Kind != `rl_algorithm`                 |
| H04  | Parameters complete    | Missing required algorithm parameters  |
| H05  | Hyperparameters valid  | Hyperparameters outside defined ranges |
| H06  | Training duration      | Training time exceeds 72h              |
| H07  | Reward threshold       | Final reward < 95% of target           |

## SOFT Scoring
| Dim | Dimension         | Weight | Scoring Guide                          |
|-----|-------------------|--------|----------------------------------------|
| D01 | Code quality      | 0.15   | 100%: clean, 75%: minor issues         |
| D02 | Documentation     | 0.10   | 100%: complete, 50%: partial           |
| D03 | Training perf     | 0.15   | 100%: meets loss/reward targets        |
| D04 | Hyperparam tuning | 0.10   | 100%: optimal, 50%: suboptimal         |
| D05 | Convergence       | 0.10   | 100%: stable, 50%: fluctuating         |
| D06 | Reward design     | 0.15   | 100%: aligned with objective           |
| D07 | Scalability       | 0.10   | 100%: handles 10k+ episodes            |
| D08 | Reproducibility   | 0.15   | 100%: same results on 3 runs           |

## Actions
| Score     | Action                          |
|-----------|---------------------------------|
| GOLDEN    | >=9.5: Auto-publish             |
| PUBLISH   | >=8.0: Manual review required   |
| REVIEW    | >=7.0: Detailed review required |
| REJECT    | <7.0: Reject, fix and resubmit  |

## Bypass
| conditions                          | approver         | audit trail                          |
|------------------------------------|------------------|--------------------------------------|
| Emergency fix for production issue | Senior engineer  | Log bypass reason and approver name  |
| Experimental phase with risk approval | Manager         | Document experimental scope and risks |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
