---
kind: config
id: bld_config_govtech_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for govtech_vertical production
quality: 8.6
title: "Config Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, config]
tldr: "Naming, paths, limits for govtech_vertical production"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p01_gv_<vertical_name>.md` (e.g., `p01_gv_cybersecurity.md`, `p01_gv_transport.md`)

## Paths
Artifacts: `/cex/artifacts/p01/gv/<vertical_name>/`
Shared: `/cex/shared/p01/gv/`

## Limits
max_bytes: 6144
max_turns: 5
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
