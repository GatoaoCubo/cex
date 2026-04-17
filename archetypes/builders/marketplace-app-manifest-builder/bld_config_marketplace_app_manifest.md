---
kind: config
id: bld_config_marketplace_app_manifest
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for marketplace_app_manifest production
quality: 8.6
title: "Config Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, config]
tldr: "Naming, paths, limits for marketplace_app_manifest production"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p09_mam_<app_name>.yaml`
Examples:
- `p09_mam_calendar.yaml`
- `p09_mam_notes.yaml`

## Paths
Artifacts stored in: `/mnt/cex/apps/marketplace/manifests/<app_name>/v<version>/manifest.yaml`

## Limits
max_bytes: 4096
max_turns: 20
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
