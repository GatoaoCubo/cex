---
kind: config
id: bld_config_reranker_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for reranker_config production
quality: 8.6
title: "Config Reranker Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [reranker_config, builder, config]
tldr: "Naming, paths, limits for reranker_config production"
domain: "reranker_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_data_residency
  - bld_config_ab_test_config
  - bld_config_graph_rag_config
  - bld_config_transport_config
  - bld_config_sandbox_spec
  - bld_config_playground_config
  - bld_config_usage_quota
  - bld_config_sso_config
  - bld_config_sandbox_config
  - bld_config_rl_algorithm
---

## Naming Convention
Pattern: `p01_rr_<project_name>.yaml`
Examples:
- `p01_rr_search.yaml`
- `p01_rr_recommend.yaml`

## Paths
Artifacts stored in: `/mnt/cex/artifacts/p01/rerankers/{{name}}.yaml`

## Limits
-

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_data_residency]] | sibling | 0.35 |
| [[bld_config_ab_test_config]] | sibling | 0.35 |
| [[bld_config_graph_rag_config]] | sibling | 0.32 |
| [[bld_config_transport_config]] | sibling | 0.31 |
| [[bld_config_sandbox_spec]] | sibling | 0.30 |
| [[bld_config_playground_config]] | sibling | 0.30 |
| [[bld_config_usage_quota]] | sibling | 0.28 |
| [[bld_config_sso_config]] | sibling | 0.28 |
| [[bld_config_sandbox_config]] | sibling | 0.28 |
| [[bld_config_rl_algorithm]] | sibling | 0.27 |
