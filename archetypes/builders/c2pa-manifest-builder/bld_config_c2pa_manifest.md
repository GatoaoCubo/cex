---
kind: config
id: bld_config_c2pa_manifest
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for c2pa_manifest production
quality: 8.6
title: "Config C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, config, C2PA, JUMBF, p10]
tldr: "Naming, paths, limits for c2pa_manifest production"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_vc_credential
  - bld_config_search_strategy
  - bld_config_workflow_run_crate
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_partner_listing
  - bld_config_planning_strategy
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_pricing_page
---

## Naming Convention
Pattern: `p10_cm_{{name}}.md`
Examples: `p10_cm_firefly_banner_2026.md`, `p10_cm_campaign_video_q2.md`

## Paths
Artifacts stored in: `P10_memory/manifests/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 4

## Hooks
pre_build: validate_mime_type
post_build: compile_to_yaml
on_error: null
on_quality_fail: rebuild_with_assertion_fix

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_vc_credential]] | sibling | 0.69 |
| [[bld_config_search_strategy]] | sibling | 0.68 |
| [[bld_config_workflow_run_crate]] | sibling | 0.68 |
| [[bld_config_sales_playbook]] | sibling | 0.67 |
| [[bld_config_transport_config]] | sibling | 0.65 |
| [[bld_config_partner_listing]] | sibling | 0.64 |
| [[bld_config_planning_strategy]] | sibling | 0.64 |
| [[bld_config_visual_workflow]] | sibling | 0.64 |
| [[bld_config_prompt_technique]] | sibling | 0.63 |
| [[bld_config_pricing_page]] | sibling | 0.62 |
