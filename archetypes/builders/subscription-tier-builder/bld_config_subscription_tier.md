---
kind: config
id: bld_config_subscription_tier
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for subscription_tier production
quality: 8.6
title: "Config Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, config]
tldr: "Naming, paths, limits for subscription_tier production"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p11_st_{{name}}.yaml`
Examples: `p11_st_bronze.yaml`, `p11_st_premium.yaml`

## Paths
Artifacts: `/artifacts/subscription_tiers/p11_st_{{name}}.yaml`
Logs: `/logs/build/p11_st_{{name}}`

## Limits
max_bytes: 3072
max_turns: 150
effort_level: high

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
