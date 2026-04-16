---
kind: config
id: bld_config_integration_guide
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for integration_guide production
quality: 8.6
title: "Config Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, config]
tldr: "Naming, paths, limits for integration_guide production"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

p05_ig_integration_guide.md
## Naming Convention
Pattern: `p05_ig_<name>.md`
Examples: `p05_ig_integration_guide.md`, `p05_ig_api_v2.md`

## Paths
Artifacts stored in: `/artifacts/p05/ig/{{name}}/`
Subdirectories: `docs/`, `logs/`, `metadata/`

## Limits
max_bytes: 8192
max_turns: 20
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
