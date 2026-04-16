---
kind: config
id: bld_config_sdk_example
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for sdk_example production
quality: 8.6
title: "Config Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, config]
tldr: "Naming, paths, limits for sdk_example production"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p04_sdk_{{name}}`
Examples: `p04_sdk_userauth`, `p04_sdk_payment`

## Paths
Artifacts stored in: `/artifacts/sdk/P04/{{name}}`
Example: `/artifacts/sdk/P04/userauth`

## Limits
- max_bytes: 5120
- max_turns: 10
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
