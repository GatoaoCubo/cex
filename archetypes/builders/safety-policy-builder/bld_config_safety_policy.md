---
kind: config
id: bld_config_safety_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for safety_policy production
quality: 8.6
title: "Config Safety Policy"
version: "1.0.0"
author: wave1_builder_gen
tags: [safety_policy, builder, config]
tldr: "Naming, paths, limits for safety_policy production"
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention
Pattern: `p11_sp_{{name}}.md`
Examples: `p11_sp_data.md`, `p11_sp_network.md`

## Paths
Artifacts stored in: `/artifacts/p11/sp/{{name}}/`
Config file path: `/artifacts/p11/sp/{{name}}/safety_policy.md`

## Limits
max_bytes: 5120
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
