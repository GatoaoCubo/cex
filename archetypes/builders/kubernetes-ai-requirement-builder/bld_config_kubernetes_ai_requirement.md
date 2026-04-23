---
kind: config
id: bld_config_kubernetes_ai_requirement
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for kubernetes_ai_requirement production
quality: 8.6
title: "Config Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, config]
tldr: "Naming, paths, limits for kubernetes_ai_requirement production"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_data_residency
  - bld_config_diff_strategy
  - bld_config_visual_workflow
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p09_kar_{{name}}.md`
Examples: `p09_kar_llama3_70b_pretrain.md`, `p09_kar_vllm_disagg_inference.md`

## Paths
Artifacts stored in: `/artifacts/p09/kubernetes_ai_requirements/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 6
effort_level: 4

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.67 |
| [[bld_config_transport_config]] | sibling | 0.67 |
| [[bld_config_sales_playbook]] | sibling | 0.65 |
| [[bld_config_planning_strategy]] | sibling | 0.64 |
| [[bld_config_partner_listing]] | sibling | 0.63 |
| [[bld_config_data_residency]] | sibling | 0.63 |
| [[bld_config_diff_strategy]] | sibling | 0.62 |
| [[bld_config_visual_workflow]] | sibling | 0.62 |
| [[bld_config_pricing_page]] | sibling | 0.62 |
| [[bld_config_agent_computer_interface]] | sibling | 0.62 |
