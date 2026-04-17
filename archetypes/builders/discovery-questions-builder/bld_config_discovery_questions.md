---
kind: config
id: bld_config_discovery_questions
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for discovery_questions production
quality: 8.6
title: "Config Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, config]
tldr: "Naming, paths, limits for discovery_questions production"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p01_dq_<name>.md` (e.g., `p01_dq_customer.md`, `p01_dq_product.md`)

## Paths
`/artifacts/p01/discovery_questions/{{name}}.md`
`/templates/p01/dq_template.md`

## Limits
- max_bytes: 4096
- max_turns: 5
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
