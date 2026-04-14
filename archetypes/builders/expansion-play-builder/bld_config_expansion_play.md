---
kind: config
id: bld_config_expansion_play
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for expansion_play production
quality: null
title: "Config Expansion Play"
version: "1.0.0"
author: wave6_n06
tags: [expansion_play, builder, config, upsell, NRR]
tldr: "Naming, paths, limits for expansion_play production"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p03_ep_{{name}}.md`
Examples: `p03_ep_acme_seat_upsell_q2.md`, `p03_ep_globex_tier_upgrade_q3.md`
Name segment: lowercase, snake_case, include account abbreviation + expansion_type + quarter

## Paths
Artifacts stored in: `N06_commercial/expansion_plays/{{segment}}/{{name}}.md`
Segment subdirs: `enterprise/`, `mid_market/`, `smb/`

## Limits
max_bytes: 5120
max_turns: 6
effort_level: 4

## Hooks
pre_build: load Gainsight health score + usage signal data
post_build: create Salesforce Expansion Opportunity record
on_error: flag to RevOps for manual review
on_quality_fail: return to CSM/AE for trigger quantification

## Runtime Parameters
| Parameter          | Value          | Notes                                    |
|--------------------|----------------|------------------------------------------|
| min_stakeholders   | 2              | Economic buyer + champion required       |
| nrr_floor          | "100%"         | Below 100% = contraction, not expansion  |
| trigger_window_min | 7              | Min days for trigger window (avoid noise)|
| qbr_required_ent   | true           | Enterprise segment requires QBR prep     |
| auto_alert_threshold| 80            | Seat utilization % to fire alert         |
