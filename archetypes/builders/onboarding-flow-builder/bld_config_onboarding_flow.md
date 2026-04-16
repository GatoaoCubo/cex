---
kind: config
id: bld_config_onboarding_flow
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for onboarding_flow production
quality: 8.6
title: "Config Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, config]
tldr: "Naming, paths, limits for onboarding_flow production"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

p05_of_{{name}}.md
Pillar: P05

## Naming Convention
Pattern: p05_of_{{name}}.md
Examples: p05_of_user_onboarding.md, p05_of_payment_setup.md

## Paths
/opt/cex/flows/p05/{{name}}
Example: /opt/cex/flows/p05/user_onboarding

## Limits
max_bytes: 5120
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
