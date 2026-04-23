---
kind: config
id: bld_config_ai_rmf_profile
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for ai_rmf_profile production
quality: 8.6
title: "Config AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, config, NIST, AI-RMF]
tldr: "Naming, paths, limits for ai_rmf_profile production"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_gpai_technical_doc
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_safety_hazard_taxonomy
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_visual_workflow
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p11_rmf_{{profile}}.md`
Examples: `p11_rmf_customer_support_llm_v1.md`, `p11_rmf_fraud_detection_system.md`

## Paths
Artifacts stored in: `P11_governance/ai_rmf_profiles/`

## Limits
max_bytes: 5120
max_turns: 7
effort_level: 4

## Hooks
pre_build: validate_nist_action_ids
post_build: compile + signal_n07
on_error: null
on_quality_fail: retry_with_gap_analysis

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_gpai_technical_doc]] | sibling | 0.68 |
| [[bld_config_search_strategy]] | sibling | 0.66 |
| [[bld_config_transport_config]] | sibling | 0.66 |
| [[bld_config_sales_playbook]] | sibling | 0.64 |
| [[bld_config_safety_hazard_taxonomy]] | sibling | 0.64 |
| [[bld_config_planning_strategy]] | sibling | 0.62 |
| [[bld_config_partner_listing]] | sibling | 0.62 |
| [[bld_config_diff_strategy]] | sibling | 0.62 |
| [[bld_config_visual_workflow]] | sibling | 0.61 |
| [[bld_config_agent_computer_interface]] | sibling | 0.61 |
