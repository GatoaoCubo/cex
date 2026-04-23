---
kind: config
id: bld_config_sandbox_spec
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for sandbox_spec production
quality: 8.6
title: "Config Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, config]
tldr: "Naming, paths, limits for sandbox_spec production"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_sandbox_config
  - bld_config_playground_config
  - bld_config_ab_test_config
  - bld_config_data_residency
  - bld_config_transport_config
  - bld_config_graph_rag_config
  - bld_config_rl_algorithm
  - bld_config_usage_quota
  - bld_config_workflow_node
  - bld_config_sso_config
---

## Naming Convention
Pattern: `p09_sb_{{name}}.yaml`
Examples: `p09_sb_example.yaml`, `p09_sb_projectA.yaml`
Pillar-specific prefix: `p09_` for P09 projects

## Paths
Configs: `/mnt/cex/specs/p09/{{name}}/p09_sb_{{name}}.yaml`
Artifacts: `/mnt/cex/artifacts/p09/{{name}}/`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_sandbox_config]] | sibling | 0.57 |
| [[bld_config_playground_config]] | sibling | 0.55 |
| [[bld_config_ab_test_config]] | sibling | 0.55 |
| [[bld_config_data_residency]] | sibling | 0.52 |
| [[bld_config_transport_config]] | sibling | 0.51 |
| [[bld_config_graph_rag_config]] | sibling | 0.49 |
| [[bld_config_rl_algorithm]] | sibling | 0.49 |
| [[bld_config_usage_quota]] | sibling | 0.48 |
| [[bld_config_workflow_node]] | sibling | 0.48 |
| [[bld_config_sso_config]] | sibling | 0.48 |
