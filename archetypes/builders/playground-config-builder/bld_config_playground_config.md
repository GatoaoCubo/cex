---
kind: config
id: bld_config_playground_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for playground_config production
quality: 8.6
title: "Config Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, config]
tldr: "Naming, paths, limits for playground_config production"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p09_pg_{{name}}.yaml`
Examples:
- p09_pg_example.yaml
- p09_pg_test.yaml

## Paths
Artifacts: `/mnt/data/cex/playgrounds/p09/{{name}}`
Logs: `/mnt/data/cex/logs/p09/{{name}}`

## Limits
- max_bytes: 4096
- max_turns: 0
- effort_level: 0

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
