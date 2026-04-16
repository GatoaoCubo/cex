---
kind: config
id: bld_config_quickstart_guide
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for quickstart_guide production
quality: 8.6
title: "Config Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, config]
tldr: "Naming, paths, limits for quickstart_guide production"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: p05_qs_{{name}}.md
Examples: p05_qs_quickstart.md, p05_qs_tutorial.md

## Paths
Artifacts stored in: /cex/quickstart/guides/p05_qs_{{name}}.md
Intermediate files: /cex/artifacts/quickstart/p05/

## Limits
max_bytes: 8192
max_turns: 5
effort_level: medium

## Hooks
pre_build -- null
post_build -- null
on_error -- null
on_quality_fail -- null
