---
kind: config
id: bld_config_audit_log
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for audit_log production
quality: 8.6
title: "Config Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, config]
tldr: "Naming, paths, limits for audit_log production"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p11_al_{{name}}.yaml`
Examples: `p11_al_user123.yaml`, `p11_al_system456.yaml`

## Paths
Artifacts: `/opt/cex/audit_logs/{{name}}/`
Backup: `/backup/cex/audit_logs/{{name}}/`

## Limits
max_bytes: 3072
max_turns: 100
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
