---
kind: config
id: bld_config_usage_quota
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for usage_quota production
quality: 8.6
title: "Config Usage Quota"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_quota, builder, config]
tldr: "Naming, paths, limits for usage_quota production"
domain: "usage_quota construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: p09_uq_{{name}}.yaml
Examples:
- p09_uq_example.yaml
- p09_uq_another.yaml

## Paths
/artifacts/usage_quotas/{{name}}.yaml

## Limits
max_bytes: 3072
max_turns: 0
effort_level: high

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
