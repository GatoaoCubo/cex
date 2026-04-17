---
kind: config
id: bld_config_judge_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for judge_config production
quality: 8.6
title: "Config Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, config]
tldr: "Naming, paths, limits for judge_config production"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p07_jc_{{name}}.md`
Examples: `p07_jc_initial.md`, `p07_jc_final.md`

## Paths
Artifacts: `/mnt/artifacts/p07/{{name}}/`
Judge config: `/mnt/configs/judge/p07_jc_{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
