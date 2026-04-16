---
kind: config
id: bld_config_expansion_play
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for expansion_play production
quality: 8.7
title: "Config Expansion Play"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [expansion_play, builder, config]
tldr: "Naming, paths, limits for expansion_play production"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

p03_ep_{{name}}.md
Pillar: P03

## Naming Convention
Pattern: `p03_ep_{{name}}.md`
Examples:
- p03_ep_initial.md
- p03_ep_v1.md

## Paths
Artifacts: `/artifacts/p03/ep/{{name}}`
Examples:
- `/artifacts/p03/ep/initial`
- `/artifacts/p03/ep/v1`

## Limits
max_bytes: 5120
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain
expansion_play configuration -- governs naming, paths, and runtime limits for expansion play artifacts.
Expansion plays are triggered by usage thresholds and cross-sell signals, targeting NRR >120%.
