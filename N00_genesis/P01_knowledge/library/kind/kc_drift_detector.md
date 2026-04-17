---
id: p01_kc_drift_detector
kind: knowledge_card
type: kind
pillar: P11
title: "Drift Detector -- Deep Knowledge for drift_detector"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: drift_detector
quality: null
tags: [drift_detector, P11, GOVERN, kind-kc, distribution-shift, monitoring, mlops]
tldr: "drift_detector applies statistical tests (KS, PSI, chi-square) to compare reference vs live distributions, firing alerts when divergence exceeds thresholds."
when_to_use: "Building, reviewing, or reasoning about drift_detector artifacts"
keywords: [drift_detector, distribution_shift, data_drift, concept_drift, ks_test, psi, evidently, arize]
feeds_kinds: [drift_detector]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
---

# Drift Detector

## Spec
```yaml
kind: drift_detector
pillar: P11
llm_function: GOVERN
max_bytes: 3072
naming: p11_dd_{scope}.md
core: true
```

## What It Is
A drift_detector applies statistical tests to compare a reference distribution (training data
or historical baseline) to a production distribution (current inputs/outputs), firing alerts
when divergence exceeds calibrated thresholds. Detects data drift, concept drift, prediction
drift, and behavioral drift.

## Drift Type Taxonomy
| Drift Type | What Changes | Detection Method |
|-----------|-------------|-----------------|
| Data drift | Input feature distribution | KS test, PSI, chi-square |
| Concept drift | Input-output relationship | Model performance metrics |
| Prediction drift | Output/label distribution | PSI on predictions |
| Behavioral drift | Agent action patterns | Distribution of action types |
| Embedding drift | Semantic distribution | Cosine distance, MMD |

## Statistical Test Reference
| Feature Type | Test | Threshold | Notes |
|-------------|------|-----------|-------|
| Continuous numerical | KS (Kolmogorov-Smirnov) | p-value > 0.05 = no drift | Nonparametric, two-sample |
| Numerical with baseline | PSI (Population Stability Index) | < 0.1 stable; 0.1-0.2 warning; > 0.2 critical | Classic credit risk metric |
| Categorical | Chi-square | p-value > 0.05 = no drift | Frequency comparison |
| Text embeddings | Cosine or MMD | Domain-calibrated | Semantic drift |
| LLM quality scores | Distribution shift | >= 10% shift = warning | Behavioral monitoring |

## Key Parameters
| Parameter | Type | Notes |
|-----------|------|-------|
| test_method | enum | ks, psi, chi_square, cosine, mmd |
| reference_window | string | training, last_30d, custom |
| production_window | string | last_7d, last_24h, custom |
| warning_threshold | float | Below this = no action |
| critical_threshold | float | Above this = alert/retrain |
| monitored_features | list[string] | Which features to test |
| alert_channel | string | Where to send alerts |

## Window Strategies
| Strategy | Reference | Production | Use Case |
|----------|-----------|------------|---------|
| Fixed baseline | Training data (frozen) | Rolling last N days | Stable concept |
| Rolling | Last 30/90 days | Last 7 days | Non-stationary |
| Seasonal | Same period last year | Current period | Seasonal domains |

## Patterns
| Pattern | When to Use | Config |
|---------|-------------|--------|
| Input feature monitoring | Data pipeline quality | KS on continuous; chi-sq on categorical |
| Output quality monitoring | LLM behavioral drift | PSI on quality score distribution |
| Embedding drift | Semantic topic shift | cosine distance on embedding centroids |
| Multi-feature | Full pipeline health | Array of detectors, one per feature |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Single threshold for all features | Feature sensitivities differ | Calibrate per feature type |
| No reference window | Cannot compute drift | Always define reference |
| Alerting on every drift | Alert fatigue | Tune thresholds with historical data |
| Ignoring concept drift | Model stales silently | Monitor prediction distribution too |

## Integration Graph
```
data_pipeline --> [drift_detector] --> alert (warning/critical)
                       |           --> scoring_rubric (retrain trigger)
                reference_dataset    --> quality_gate (deployment gate)
                production_stream    --> learning_record (drift history)
```

## Tools
| Tool | Purpose |
|------|---------|
| Evidently AI | Feature + model drift dashboards |
| Arize Phoenix | LLM-specific embedding + behavioral drift |
| Whylogs | Lightweight data profiling for drift |
| NannyML | Confidence-based concept drift (no labels needed) |
