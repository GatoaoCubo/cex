---
kind: output_template
id: bld_output_template_rl_algorithm
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for rl_algorithm production
quality: 9.1
title: "Output Template Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, output_template]
tldr: "Template with vars for rl_algorithm production"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_rl_algorithm
  - bld_examples_rl_algorithm
  - bld_instruction_rl_algorithm
  - p03_sp_rl_algorithm_builder
  - p10_lr_rl_algorithm_builder
  - p02_qg_rl_algorithm
  - rl-algorithm-builder
  - bld_knowledge_card_rl_algorithm
  - kc_rl_algorithm
  - bld_architecture_rl_algorithm
---

```yaml
id: p02_rla_{{slug}}               # e.g. p02_rla_ppo_discrete
kind: rl_algorithm
pillar: P02
title: "{{Algorithm Name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{nucleus_or_team}}"
domain: "{{domain, e.g. robotics, dialogue, game playing}}"
quality: null                      # NEVER self-score
tags: [rl_algorithm, "{{algo_tag}}", "{{domain_tag}}"]
tldr: "{{One concrete sentence: algorithm type, key mechanism, convergence property}}"
algorithm_type: "{{DQN|PPO|SAC|A3C|DDPG|TD3|...}}"
hyperparameters:
  learning_rate: {{float}}         # e.g. 0.0003
  gamma: {{0.0-1.0}}              # discount factor
  batch_size: {{int}}             # e.g. 256
  {{other_params}}: {{values}}
```

## Overview
<!-- What problem this algorithm solves.
     Key mechanism (e.g., "proximal policy optimization clips the policy gradient").
     Theoretical guarantees (convergence, sample efficiency). -->

## Algorithm Components
<!-- Key modules in formal notation.
     Policy: pi(a|s; theta)
     Value function: V(s; phi)
     Exploration: epsilon-greedy, entropy bonus, etc. -->
| Component | Notation | Role |
|-----------|----------|------|
| Policy | pi(a\|s; theta) | Action selection |
| Value function | V(s; phi) | Baseline for variance reduction |
| `{{component}}` | {{notation}} | `{{role}}` |

## Training Process
1. Initialize: `{{initialization approach}}`
2. Sample: collect T timesteps of experience
3. Update: {{update rule, e.g., compute advantage, clip ratio, backprop}}
4. Evaluate: every `{{N}}` episodes, run `{{M}}` evaluation episodes
5. Convergence: `{{stopping criterion}}`

## Evaluation Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| Episode reward | >= `{{threshold}}` | Mean over last 100 episodes |
| Sample efficiency | `{{N}}` env steps | Time to reach target reward |
| `{{metric}}` | {{target}} | `{{method}}` |

## Use Cases
- APPLY when: `{{specific conditions where this algorithm excels}}`
- AVOID when: `{{conditions where alternatives outperform}}`

## Constraints
- Computational: {{GPU memory, parallelism requirements}}
- Environment: {{required interfaces, gym compatibility}}
- Reproducibility: fix random seeds `{{seed_list}}`, log all hyperparameters

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_rl_algorithm]] | downstream | 0.35 |
| [[bld_examples_rl_algorithm]] | downstream | 0.34 |
| [[bld_instruction_rl_algorithm]] | upstream | 0.31 |
| [[p03_sp_rl_algorithm_builder]] | upstream | 0.30 |
| [[p10_lr_rl_algorithm_builder]] | downstream | 0.29 |
| [[p02_qg_rl_algorithm]] | downstream | 0.29 |
| [[rl-algorithm-builder]] | upstream | 0.24 |
| [[bld_knowledge_card_rl_algorithm]] | upstream | 0.23 |
| [[kc_rl_algorithm]] | upstream | 0.22 |
| [[bld_architecture_rl_algorithm]] | downstream | 0.21 |
