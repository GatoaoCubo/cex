---
kind: config
id: bld_config_case_study
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for case_study production
quality: 8.6
title: "Config Case Study"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, config]
tldr: "Naming, paths, limits for case_study production"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

p05_cs_{{name}}.md
Pillar: P05
Max bytes: 6144

## Naming Convention
Pattern: `p05_cs_<study_name>.md`
Examples:
- `p05_cs_marketing.md`
- `p05_cs_technology.md`

## Paths
Artifacts stored in: `/opt/cex/artifacts/p05/{{name}}/`
Subdirectories: `docs/`, `data/`, `outputs/`

## Limits
- max_bytes: 6144
- max_turns: 5
- effort_level: medium

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
