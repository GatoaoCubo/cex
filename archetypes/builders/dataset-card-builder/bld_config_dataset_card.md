---
kind: config
id: bld_config_dataset_card
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for dataset_card production
quality: null
title: "Config Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, config]
tldr: "Naming, paths, limits for dataset_card production"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention
Pattern: p01_dc_{{name}}.md
Examples: p01_dc_train.md, p01_dc_validation.md

## Paths
Artifacts: ./artifacts/p01/

## Limits
max_bytes: 5120
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
