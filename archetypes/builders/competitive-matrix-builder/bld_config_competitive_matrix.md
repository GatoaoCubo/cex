---
kind: config
id: bld_config_competitive_matrix
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for competitive_matrix production
quality: 8.6
title: "Config Competitive Matrix"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, config]
tldr: "Naming, paths, limits for competitive_matrix production"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention (competitive matrix artifacts)
Pattern: p01_cm_{{name}}.md (e.g., p01_cm_market_analysis.md) for competitive matrix outputs

## Paths
/artifacts/p01/cm/{{name}}.md

## Limits
max_bytes: 5120
max_turns: 3
effort_level: high

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
