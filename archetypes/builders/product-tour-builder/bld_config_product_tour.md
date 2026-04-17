---
kind: config
id: bld_config_product_tour
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for product_tour production
quality: 8.6
title: "Config Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, config]
tldr: "Naming, paths, limits for product_tour production"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: p05_pt_{{name}}.md
Examples: p05_pt_onboarding.md, p05_pt_feature_x.md

## Paths
/artifacts/p05/product_tours/{{name}}.md

## Limits
max_bytes: 5120
max_turns: 0
effort_level: 0

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
