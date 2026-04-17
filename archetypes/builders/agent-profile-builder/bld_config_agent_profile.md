---
kind: config
id: bld_config_agent_profile
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for agent_profile production
quality: 8.6
title: "Config Agent Profile"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_profile, builder, config]
tldr: "Naming, paths, limits for agent_profile production"
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention
Pattern: `p02_ap_{{name}}.md`
Examples: `p02_ap_john.md`, `p02_ap_sarah.md`

## Paths
Artifacts stored in: `/artifacts/p02/profiles/`
Example path: `/artifacts/p02/profiles/john.md`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
