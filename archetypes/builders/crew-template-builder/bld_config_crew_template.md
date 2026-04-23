---
kind: config
id: bld_config_crew_template
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for crew_template production
quality: 8.7
title: "Config Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, config, composable, crewai]
tldr: "Naming, paths, limits for crew_template production"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
related:
  - bld_config_transport_config
  - bld_config_search_strategy
  - bld_config_usage_quota
  - bld_config_sales_playbook
  - bld_config_ab_test_config
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_vc_credential
---

## Naming Convention
Pattern: `p12_ct_{{crew_name}}.md`
Examples: `p12_ct_research_brief.md`, `p12_ct_brand_launch.md`, `p12_ct_incident_triage.md`

## Paths
Artifacts stored in: `P12_orchestration/crews/{{crew_name}}.md`
Compiled YAML: `P12_orchestration/crews/compiled/{{crew_name}}.yaml`
Index entry: `.cex/indices/crews.json`

## Limits
max_bytes: 4096
max_turns: 4
effort_level: 3
max_roles_per_crew: 8
max_depth_hierarchical: 3

## Hooks
pre_build: validate_role_refs_exist
post_build: compile_to_yaml
on_error: null
on_quality_fail: rebuild_with_peer_review

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_transport_config]] | sibling | 0.45 |
| [[bld_config_search_strategy]] | sibling | 0.42 |
| [[bld_config_usage_quota]] | sibling | 0.41 |
| [[bld_config_sales_playbook]] | sibling | 0.41 |
| [[bld_config_ab_test_config]] | sibling | 0.41 |
| [[bld_config_visual_workflow]] | sibling | 0.40 |
| [[bld_config_prompt_technique]] | sibling | 0.40 |
| [[bld_config_planning_strategy]] | sibling | 0.40 |
| [[bld_config_partner_listing]] | sibling | 0.40 |
| [[bld_config_vc_credential]] | sibling | 0.40 |
