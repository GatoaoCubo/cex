---
kind: config
id: bld_config_contributor_guide
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for contributor_guide production
quality: 8.6
title: "Config Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, config]
tldr: "Naming, paths, limits for contributor_guide production"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---
## Naming Convention
Files: kebab-case (e.g., `contributor-guide-builder.md`). Directories: PascalCase (e.g., `Src`). Classes: PascalCase. Variables: snake_case.
## Paths
Artifacts stored in: `/repo/src/p05`, `/repo/docs/p05`, `/repo/tests/p05`.

## Limits
max_bytes: 6144. max_turns: 5. effort_level: medium.

## Hooks
pre_build: null. post_build: null. on_error: null. on_quality_fail: null.