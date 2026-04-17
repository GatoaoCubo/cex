---
id: n00_rl_algorithm_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "RL Algorithm -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, rl_algorithm, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
RL Algorithm defines a reinforcement learning training algorithm specification for aligning or adapting LLMs. It documents the algorithm's mathematical formulation, hyperparameters, reward model requirements, and known trade-offs. Used when designing RLHF, DPO, ORPO, or PPO-based training pipelines for model alignment or specialized behavior.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `rl_algorithm` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Algorithm name and variant |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| algorithm_type | enum | yes | PPO\|DPO\|ORPO\|GRPO\|RLHF\|RLAIF |
| reward_model_required | bool | yes | Whether a separate reward model is needed |
| reference_model_required | bool | yes | Whether a reference (frozen) model is needed |
| key_hyperparameters | list | yes | Critical hyperparameters with ranges |
| memory_overhead | enum | yes | low\|medium\|high vs. SFT |
| stability | enum | yes | low\|medium\|high -- training stability |

## When to use
- When selecting an alignment algorithm for a fine-tuning project
- When documenting a training methodology for reproducibility
- When comparing RL algorithms for a specific alignment objective

## Builder
`archetypes/builders/rl_algorithm-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind rl_algorithm --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N03 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- ML researchers and alignment engineers
- `{{DOMAIN_CONTEXT}}` -- alignment objective and data availability

## Example (minimal)
```yaml
---
id: rl_algorithm_dpo_v1
kind: rl_algorithm
pillar: P02
nucleus: n03
title: "Direct Preference Optimization (DPO)"
version: 1.0
quality: null
---
algorithm_type: DPO
reward_model_required: false
reference_model_required: true
key_hyperparameters:
  - name: beta
    range: [0.01, 0.5]
    default: 0.1
memory_overhead: medium
stability: high
```

## Related kinds
- `finetune_config` (P02) -- training job using this algorithm
- `training_method` (P02) -- broader training approach this algorithm belongs to
- `model_architecture` (P02) -- model being trained with this algorithm
