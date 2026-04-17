---
kind: architecture
id: bld_architecture_drift_detector
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of drift_detector -- inventory, dependencies, and architectural position
quality: 8.3
title: "Architecture Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, architecture]
tldr: "drift_detector sits in P11 Feedback as the runtime distribution monitor between deployed model and alerting/retraining systems."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| detection_method | Statistical test applied to detect shift | drift_detector | required |
| threshold | Warning/critical numeric bounds | drift_detector | required |
| features_monitored | Input/output dimensions under observation | drift_detector | required |
| alert_rule | Where and how to route drift signals | drift_detector | required |
| window_config | Reference baseline + production window | drift_detector | required |
| reference_distribution | Statistical baseline (training data or historical window) | P10 memory | producer |
| production_stream | Live model inputs/outputs being compared | P04 tools | producer |
| benchmark | Point-in-time evaluation -- distinct from continuous monitoring | P07 | sibling |
| regression_check | Code behavior regression -- distinct from data distribution shift | P11 | sibling |
| retraining_trigger | Downstream action when drift exceeds critical threshold | P12 | consumer |
| preference_dataset | Training data whose distribution this monitor tracks | P11 | sibling |

## Dependency Graph
```
reference_distribution  --provides-->  window_config.reference
production_stream       --provides-->  window_config.production
detection_method        --applied_to-> (reference vs production comparison)
threshold               --governs-->   drift score interpretation
features_monitored      --scopes-->    which dimensions are compared
alert_rule              --triggered_by--> threshold crossing
drift_detector          --feeds-->     retraining_trigger (when critical)
drift_detector          --feeds-->     alerting system
```

## Boundary Table
| drift_detector IS | drift_detector IS NOT |
|-------------------|-----------------------|
| Continuous distribution shift monitor | Point-in-time score (that is benchmark) |
| Statistical comparison of reference vs live | Code test assertion (that is regression_check) |
| Runtime operational concern | Artifact quality gate (that is quality_gate) |
| Detects data/concept/prediction/behavioral drift | Detects model weight corruption (that is diff task) |
| Configuration spec for monitoring platform | Full monitoring dashboard implementation |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| signal | detection_method, threshold | Define what constitutes drift |
| data | features_monitored, window_config | Scope what is compared |
| runtime | reference_distribution, production_stream | Supply data for comparison |
| action | alert_rule, retraining_trigger | Respond to detected drift |
| governance | enabled, sampling_rate | Control monitoring overhead |
