---
kind: config
id: bld_config_healthcare_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for healthcare_vertical production
quality: 8.6
title: "Config Healthcare Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [healthcare_vertical, builder, config]
tldr: "Naming, paths, limits for healthcare_vertical production"
domain: "healthcare_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p01_hv_{{name}}.md`
Examples:
- `p01_hv_example.md`
- `p01_hv_patient_portal.md`

## Paths
Artifacts stored in: `/cex/verticals/P01/{{name}}/artifacts/`

## Limits
max_bytes: 6144
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
