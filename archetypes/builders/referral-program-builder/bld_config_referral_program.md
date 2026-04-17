---
kind: config
id: bld_config_referral_program
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for referral_program production
quality: 8.6
title: "Config Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, config]
tldr: "Naming, paths, limits for referral_program production"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p11_rp_{{name}}.yaml`
Examples: `p11_rp_referral_program.yaml`, `p11_rp_loyalty.yaml`

## Paths
`/artifacts/referral_programs/p11_rp_{{name}}.yaml`
`/src/pillars/P11/configs/referral_programs/`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
