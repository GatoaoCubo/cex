---
id: bld_architecture_canary_config
kind: knowledge_card
pillar: P08
title: "Architecture: canary_config Relationships"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
quality: null
tags: [architecture, canary_config, P09]
llm_function: CONSTRAIN
tldr: "How canary_config relates to deployment_manifest, slo_definition, feature_flag, and ab_test_config."
density_score: null
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
