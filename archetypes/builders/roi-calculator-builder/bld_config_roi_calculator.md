---
kind: config
id: bld_config_roi_calculator
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for roi_calculator production
quality: 8.6
title: "Config Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, config]
tldr: "Naming, paths, limits for roi_calculator production"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p11_roi_{{name}}.yaml`
Examples: `p11_roi_projectA.yaml`, `p11_roi_q4_2023.yaml`

## Paths
Artifacts: `/artifacts/roi/p11/{{name}}/output.yaml`
Logs: `/artifacts/roi/p11/{{name}}/logs/`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
