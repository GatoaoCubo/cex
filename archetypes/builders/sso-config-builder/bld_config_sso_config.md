---
kind: config
id: bld_config_sso_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for sso_config production
quality: 8.6
title: "Config Sso Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sso_config, builder, config]
tldr: "Naming, paths, limits for sso_config production"
domain: "sso_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_transport_config
  - bld_config_usage_quota
  - bld_config_ab_test_config
  - bld_config_visual_workflow
  - bld_config_data_residency
  - bld_config_prompt_technique
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_prosody_config
  - bld_config_sandbox_config
---

## Naming Convention
Pattern: `p09_sso_{{name}}.yaml`
Examples: `p09_sso_example.yaml`, `p09_sso_prod.yaml`

## Paths
Artifacts stored in: `/opt/cex/configs/p09/sso/{{name}}.yaml`

## Limits
max_bytes: 3072
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_transport_config]] | sibling | 0.60 |
| [[bld_config_usage_quota]] | sibling | 0.58 |
| [[bld_config_ab_test_config]] | sibling | 0.57 |
| [[bld_config_visual_workflow]] | sibling | 0.56 |
| [[bld_config_data_residency]] | sibling | 0.56 |
| [[bld_config_prompt_technique]] | sibling | 0.56 |
| [[bld_config_search_strategy]] | sibling | 0.56 |
| [[bld_config_sales_playbook]] | sibling | 0.54 |
| [[bld_config_prosody_config]] | sibling | 0.54 |
| [[bld_config_sandbox_config]] | sibling | 0.54 |
