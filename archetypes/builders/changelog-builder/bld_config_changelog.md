---
kind: config
id: bld_config_changelog
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for changelog production
quality: 8.6
title: "Config Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, config]
tldr: "Naming, paths, limits for changelog production"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p01_ch_{{name}}.md`
Examples:
- `p01_ch_release_v1.0.md`
- `p01_ch_hotfix_20231001.md`

## Paths
- Artifacts: `/artifacts/changelogs/p01/`
- Sources: `/src/pillars/p01/`

## Limits
- max_bytes: 5120
- max_turns: 10
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
