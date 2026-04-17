---
kind: config
id: bld_config_agents_md
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for agents_md production
quality: 8.6
title: "Config Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, config]
tldr: "Naming, paths, limits for agents_md production"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p02_am_{{name}}.md`
Examples: `p02_am_acme_api.md`, `p02_am_cex_core.md`

## Paths
Artifacts stored in: `/artifacts/p02/agents_md/{{name}}.md`

## Limits
max_bytes: 3072
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
