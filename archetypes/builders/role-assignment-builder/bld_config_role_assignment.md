---
kind: config
id: bld_config_role_assignment
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for role_assignment production
quality: 8.7
title: "Config Role Assignment"
version: "1.0.0"
author: n03_wave8_builder
tags: [role_assignment, builder, config, composable, crewai]
tldr: "Naming, paths, limits for role_assignment production"
domain: "role_assignment construction"
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
Pattern: `p02_ra_{{role_name}}.md`
Examples: `p02_ra_domain_researcher.md`, `p02_ra_peer_reviewer.md`, `p02_ra_brief_editor.md`, `p02_ra_research_manager.md`

## Paths
Artifacts stored in: `P02_model/role_assignments/{{role_name}}.md`
Compiled YAML: `P02_model/role_assignments/compiled/{{role_name}}.yaml`
Index entry: `.cex/indices/roles.json`

## Limits
max_bytes: 3072
max_turns: 3
effort_level: 2
max_responsibilities: 5
max_tools_allowed: 12
backstory_max_chars: 300
goal_max_chars: 150

## Hooks
pre_build: resolve_agent_id_against_registry
post_build: compile_to_yaml
on_error: null
on_quality_fail: rebuild_with_peer_review

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_transport_config]] | sibling | 0.45 |
| [[bld_config_search_strategy]] | sibling | 0.43 |
| [[bld_config_usage_quota]] | sibling | 0.42 |
| [[bld_config_sales_playbook]] | sibling | 0.42 |
| [[bld_config_ab_test_config]] | sibling | 0.41 |
| [[bld_config_visual_workflow]] | sibling | 0.41 |
| [[bld_config_prompt_technique]] | sibling | 0.40 |
| [[bld_config_planning_strategy]] | sibling | 0.40 |
| [[bld_config_partner_listing]] | sibling | 0.40 |
| [[bld_config_vc_credential]] | sibling | 0.40 |
