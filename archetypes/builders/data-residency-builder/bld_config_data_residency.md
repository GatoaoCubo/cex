---
kind: config
id: bld_config_data_residency
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for data_residency production
quality: 8.6
title: "Config Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, config]
tldr: "Naming, paths, limits for data_residency production"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p09_dr_<project_name>.yaml`
Examples: `p09_dr_customer_data.yaml`, `p09_dr_inventory.yaml`

## Paths
Artifacts stored in:
`/artifacts/pillar/P09/{{name}}/build`
`/artifacts/pillar/P09/{{name}}/output`

## Limits
max_bytes: 3072
max_turns: 50
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
