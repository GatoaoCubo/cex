---
kind: config
id: bld_config_trajectory_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for trajectory_eval production
quality: null
title: "Config Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, config]
tldr: "Naming, paths, limits for trajectory_eval production"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention  
Pattern: `p07_te_<name>`  
Examples: `p07_te_eval_01`, `p07_te_test_case`  

## Paths  
Artifacts: `/mnt/cex/trajectories/p07/te/<name>/artifacts`  
Logs: `/mnt/cex/trajectories/p07/te/<name>/logs`  

## Limits  
max_bytes: 5120  
max_turns: 10  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
