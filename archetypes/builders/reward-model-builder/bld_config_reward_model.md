---
kind: config
id: bld_config_reward_model
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for reward_model production
quality: 8.6
title: "Config Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, config]
tldr: "Naming, paths, limits for reward_model production"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention
p07_rwm_<model_name>_<timestamp> (e.g., p07_rwm_rlhf_v1_20231005)

## Paths
- Models: `/mnt/artifacts/p07/rwm/{{name}}/models/`
- Logs: `/mnt/artifacts/p07/rwm/{{name}}/logs/`
- Checkpoints: `/mnt/artifacts/p07/rwm/{{name}}/checkpoints/`

## Limits
- max_bytes: 5120
- max_turns: 20
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
