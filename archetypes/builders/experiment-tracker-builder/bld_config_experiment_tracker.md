---
kind: config
id: bld_config_experiment_tracker
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for experiment_tracker production
quality: 8.6
title: "Config Experiment Tracker"
version: "1.0.0"
author: wave1_builder_gen
tags: [experiment_tracker, builder, config]
tldr: "Naming, paths, limits for experiment_tracker production"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention
Pattern: p07_et_{{name}}.md
Examples: p07_et_baseline.md, p07_et_v1_test.md

## Paths
Artifacts: ./outputs/p07/experiments/

## Limits
max_bytes: 4096
max_turns: 15
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
