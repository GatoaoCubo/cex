---
kind: config
id: bld_config_fintech_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for fintech_vertical production
quality: 8.6
title: "Config Fintech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [fintech_vertical, builder, config]
tldr: "Naming, paths, limits for fintech_vertical production"
domain: "fintech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p01_fv_{{name}}.md`
Examples: `p01_fv_payment_gateway.md`, `p01_fv_fraud_detection.md`

## Paths
Artifacts: `/artifacts/verticals/p01_fv_{{name}}`
Configs: `/configs/p01`
Logs: `/logs/p01_fv_{{name}}`

## Limits
max_bytes: 6144
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
