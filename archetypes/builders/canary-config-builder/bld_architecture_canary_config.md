---
quality: 8.2
quality: 7.8
id: bld_architecture_canary_config
kind: knowledge_card
pillar: P08
title: "Architecture: canary_config Relationships"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
tags: [architecture, canary_config, P09]
llm_function: CONSTRAIN
tldr: "How canary_config relates to deployment_manifest, slo_definition, feature_flag, and ab_test_config."
density_score: null
related:
  - bld_architecture_trace_config
  - p01_kc_experiment_config
  - p11_qg_experiment_config
  - ab-test-config-builder
  - experiment-config-builder
  - p03_sp_optimizer_builder
  - p11_qg_trace_config
  - bld_architecture_feature_flag
  - p02_agent_deploy_ops
  - p01_kc_cicd_llm_pipeline
---

# Architecture: canary_config

## Relationship Graph
```
[deployment_manifest] --> [canary_config] --> [slo_definition] (rollback trigger)
                               |
                               +--> [signal: canary_promoted | canary_rolled_back]
                               |
                               +--> [trace_config] (metric data source)
```

## Kind Boundaries
| Kind | Relationship | Boundary |
|------|-------------|---------|
| deployment_manifest | UPSTREAM | deployment_manifest defines artifacts; canary_config defines traffic split strategy |
| slo_definition | ROLLBACK SIGNAL | slo_definition breach triggers canary_config rollback |
| feature_flag | SIBLING | feature_flag is boolean toggle; canary_config is graduated traffic split |
| ab_test_config | SIBLING | ab_test_config uses statistical analysis; canary_config uses metric thresholds |
| trace_config | DOWNSTREAM | trace_config feeds metric data used by canary analysis |

## Progressive Delivery Stack
```
deployment_manifest  (what to deploy)
      |
canary_config        (how to roll out traffic)
      |
slo_definition       (success criteria)
      |
trace_config         (observability data)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_trace_config]] | related | 0.23 |
| [[p01_kc_experiment_config]] | sibling | 0.20 |
| [[p11_qg_experiment_config]] | downstream | 0.19 |
| [[ab-test-config-builder]] | downstream | 0.18 |
| [[experiment-config-builder]] | downstream | 0.17 |
| [[p03_sp_optimizer_builder]] | upstream | 0.17 |
| [[p11_qg_trace_config]] | downstream | 0.17 |
| [[bld_architecture_feature_flag]] | related | 0.17 |
| [[p02_agent_deploy_ops]] | upstream | 0.16 |
| [[p01_kc_cicd_llm_pipeline]] | sibling | 0.16 |
