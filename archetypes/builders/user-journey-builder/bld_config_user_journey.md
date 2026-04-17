---
kind: config
id: bld_config_user_journey
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for user_journey production
quality: 8.6
title: "Config User Journey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [user_journey, builder, config]
tldr: "Naming, paths, limits for user_journey production"
domain: "user_journey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p05_uj_{{name}}.md`
Examples: `p05_uj_onboarding.md`, `p05_uj_checkout.md`

## Paths
Artifacts: `/cex/artifacts/p05/user_journeys/{{name}}.md`
Templates: `/cex/templates/p05/user_journey-builder/`

## Limits
max_bytes: 5120
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
