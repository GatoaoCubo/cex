---
kind: config
id: bld_config_visual_workflow
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for visual_workflow production
quality: 8.6
title: "Config Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, config]
tldr: "Naming, paths, limits for visual_workflow production"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p12_vw_{{name}}.md`
Examples: `p12_vw_onboarding.md`, `p12_vw_data_processing.md`

## Paths
Artifacts stored in: `/opt/cex/p12/workflows/{{name}}.md`

## Limits
max_bytes: 5120
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
