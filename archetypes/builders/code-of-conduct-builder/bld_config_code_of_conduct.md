---
kind: config
id: bld_config_code_of_conduct
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for code_of_conduct production
quality: 8.6
title: "Config Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, config]
tldr: "Naming, paths, limits for code_of_conduct production"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Naming Convention
Pattern: `p05_coc_{{name}}.md`
Examples: `p05_coc_myproject.md`, `p05_coc_openwidget.md`, `p05_coc_foundation.md`

## Paths
Artifacts stored in: `P05_output/community/{{name}}/CODE_OF_CONDUCT.md`
Builder ISOs stored in: `archetypes/builders/code-of-conduct-builder/`

## Limits
max_bytes: 4096
max_turns: 4
effort_level: 2

## Hooks
pre_build: null
post_build: python _tools/cex_compile.py {path}
on_error: log to .cex/runtime/signals/
on_quality_fail: retry F6 PRODUCE once, then escalate to N07
