---
kind: config
id: bld_config_customer_segment
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for customer_segment production
quality: 8.6
title: "Config Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, config]
tldr: "Naming, paths, limits for customer_segment production"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p02_cs_{{name}}`
Examples: `p02_cs_high_value`, `p02_cs_churn_risk`

## Paths
Artifacts: `/data/segments/p02/{{name}}/artifacts`
Logs: `/logs/p02/{{name}}`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
