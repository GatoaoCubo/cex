---
kind: config
id: bld_config_churn_prevention_playbook
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for churn_prevention_playbook production
quality: 8.6
title: "Config Churn Prevention Playbook"
version: "1.0.0"
author: n05_wave6
tags: [churn_prevention_playbook, builder, config]
tldr: "Naming, paths, limits for churn_prevention_playbook production"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p03_cpp_{{name}}.md`
Examples: `p03_cpp_enterprise_red_zone.md`, `p03_cpp_smb_winback_90d.md`

## Paths
Artifacts stored in: `P03_prompt/playbooks/churn/`

## Limits
max_bytes: 6144
max_turns: 6
effort_level: 4

## Hooks
pre_build: load health_score_model from Gainsight config
post_build: compile + signal N06 with win-back offer parameters
on_error: log to `.cex/runtime/signals/churn_error.json`
on_quality_fail: rebuild -- enforce save script objection handlers
