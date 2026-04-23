---
id: n00_reward_model_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Reward Model -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, reward_model, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_reward_model
  - bld_schema_reward_signal
  - bld_schema_rl_algorithm
  - bld_knowledge_card_reward_model
  - bld_tools_reward_model
  - bld_collaboration_reward_signal
  - reward-model-builder
  - bld_schema_reranker_config
  - p10_lr_reward_model_builder
  - bld_schema_benchmark_suite
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Reward model defines the configuration for a process or outcome reward model used in reinforcement learning from human feedback (RLHF), AI feedback (RLAIF), or agent trajectory optimization. It specifies whether the model scores intermediate steps (process reward) or final outcomes (outcome reward), the training dataset, scoring criteria, and integration with the agent training pipeline.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `reward_model` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Domain + "Reward Model" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| reward_type | enum | yes | process / outcome / hybrid |
| base_model | string | yes | Foundation model fine-tuned for reward scoring |
| training_dataset_id | string | yes | Labeled preference dataset used for training |
| scoring_granularity | enum | yes | token / step / trajectory / response |
| feedback_source | enum | yes | human / llm / automated_heuristic |

## When to use
- Training or configuring a reward model for RLHF fine-tuning of a nucleus
- Implementing automated preference learning without human annotators
- Building a process reward model for multi-step agent trajectory optimization

## Builder
`archetypes/builders/reward_model-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind reward_model --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence + N03 engineering design reward models
- `{{SIN_LENS}}` -- Analytical Envy: precise preference signal, no reward hacking
- `{{TARGET_AUDIENCE}}` -- ML engineers training or fine-tuning agent models
- `{{DOMAIN_CONTEXT}}` -- task domain, feedback source, training compute budget

## Example (minimal)
```yaml
---
id: reward_model_cex_8f_process
kind: reward_model
pillar: P07
nucleus: n01
title: "CEX 8F Process Reward Model"
version: 1.0
quality: null
---
reward_type: process
base_model: claude-haiku-4-6
scoring_granularity: step
feedback_source: llm
training_dataset_id: eval_dataset_cex_8f_preference_pairs
```

## Related kinds
- `trajectory_eval` (P07) -- evaluates agent trajectories that the reward model scores
- `eval_dataset` (P07) -- preference pairs used to train the reward model
- `llm_judge` (P07) -- LLM-as-judge that can serve as the feedback source

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reward_model]] | upstream | 0.46 |
| [[bld_schema_reward_signal]] | downstream | 0.43 |
| [[bld_schema_rl_algorithm]] | upstream | 0.42 |
| [[bld_knowledge_card_reward_model]] | sibling | 0.42 |
| [[bld_tools_reward_model]] | upstream | 0.41 |
| [[bld_collaboration_reward_signal]] | downstream | 0.40 |
| [[reward-model-builder]] | related | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
| [[p10_lr_reward_model_builder]] | downstream | 0.37 |
| [[bld_schema_benchmark_suite]] | upstream | 0.37 |
