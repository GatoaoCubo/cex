---
kind: config
id: bld_config_api_reference
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for api_reference production
quality: 8.6
title: "Config Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, config]
tldr: "Naming, paths, limits for api_reference production"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p06_ar_<name>.md` (e.g., `p06_ar_userapi.md`, `p06_ar_payment.md`)

## Paths
`/artifacts/api_refs/p06/<name>.md`

## Limits
max_bytes: 8192 | max_turns: 20 | effort level: 3

## Hooks
pre_build: null | post_build: null | on_error: null | on_quality_fail: null
