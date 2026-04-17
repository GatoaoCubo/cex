---
kind: config
id: bld_config_edtech_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for edtech_vertical production
quality: 8.6
title: "Config Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, config]
tldr: "Naming, paths, limits for edtech_vertical production"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: p01_etv_{{name}}.md
Examples: p01_etv_math.md, p01_etv_science.md

## Paths
/cex/verticals/p01_etv_{{name}}/artifacts/

## Limits
max_bytes: 6144
max_turns: 5
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
