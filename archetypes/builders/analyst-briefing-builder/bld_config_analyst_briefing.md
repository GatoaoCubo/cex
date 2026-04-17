---
kind: config
id: bld_config_analyst_briefing
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for analyst_briefing production
quality: 8.6
title: "Config Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, config]
tldr: "Naming, paths, limits for analyst_briefing production"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p05_ab_{{vendor_slug}}_{{analyst_firm}}_{{year}}.md`
Examples: `p05_ab_acme_gartner_2026.md`, `p05_ab_techco_forrester_2026.md`

## Paths
Artifacts stored in: `/artifacts/p05/analyst_briefings/{{vendor_slug}}/`

## Limits
max_bytes: 6144
max_turns: 6
effort_level: 4

## Hooks
pre_build: validate proof_point_count >= 3
post_build: run bld_quality_gate (HARD gates H01-H08)
on_error: log to ar_error_log.md
on_quality_fail: escalate to AR team lead
