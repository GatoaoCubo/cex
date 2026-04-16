---
kind: config
id: bld_config_rbac_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for rbac_policy production
quality: 8.6
title: "Config Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, config]
tldr: "Naming, paths, limits for rbac_policy production"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p09_rbac_<name>.yaml`
Examples: `p09_rbac_admin.yaml`, `p09_rbac_guest.yaml`

## Paths
`/opt/cex/policies/rbac/{{name}}.yaml`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
