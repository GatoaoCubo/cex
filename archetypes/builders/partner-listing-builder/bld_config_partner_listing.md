---
kind: config
id: bld_config_partner_listing
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for partner_listing production
quality: 8.6
title: "Config Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, config]
tldr: "Naming, paths, limits for partner_listing production"
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p05_pl_{{name}}.md`
Examples: `p05_pl_partnerA.md`, `p05_pl_sponsorX.md`

## Paths
Artifacts stored in: `/artifacts/p05/partner_listings/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
