---
kind: config
id: bld_config_ecommerce_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for ecommerce_vertical production
quality: 8.6
title: "Config Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, config]
tldr: "Naming, paths, limits for ecommerce_vertical production"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p01_ev_{{name}}.md`
Examples:
- `p01_ev_homepage.md`
- `p01_ev_productpage.md`

## Paths
- Source: `/src/verticals/ecommerce/p01/`
- Artifacts: `/artifacts/ecommerce/p01/`

## Limits
- max_bytes: 6144
- max_turns: 5
- effort level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
