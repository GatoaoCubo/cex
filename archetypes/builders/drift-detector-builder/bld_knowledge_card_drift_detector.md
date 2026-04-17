---
kind: knowledge_card
id: bld_knowledge_card_drift_detector
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for drift_detector production
sources: Evidently AI docs, Arize Phoenix, Whylogs, "Failing Loudly" (Rabanser et al. 2019), PSI reference
quality: null
title: "Knowledge Card Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, knowledge_card]
tldr: "Drift detectors apply statistical tests to compare reference vs live distributions, firing alerts when divergence exceeds calibrated thresholds."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Domain Knowledge: drift_detector

## Executive Summary
Distribution drift detection compares a reference distribution (training data or historical baseline) to a production distribution (current model inputs/outputs) using statistical tests. When the test score exceeds a threshold, the detector fires an alert. Drift can affect inputs (data drift), labels/outputs (concept drift), predicted probabilities (prediction drift), or agent behavior patterns (behavioral drift).

## Statistical Test Selection
| Feature Type | Recommended Test | Threshold Range | Notes |
|-------------|-----------------|-----------------|-------|
| Continuous numerical | KS (Kolmogorov-Smirnov) | p-value > 0.05 = no drift | Two-sample, nonparametric |
| Numerical with baseline | PSI (Population Stability Index) | 0.1 warning, 0.2 critical | Classic credit risk metric |
| Categorical / discrete | Chi-square or JS divergence | chi2 p > 0.05; JS < 0.1 | JS is bounded [0,1] |
| Text embeddings | Cosine distance or MMD | domain-specific calibration | Semantic drift detection |
| LLM output quality | Distribution of quality scores | >= 10% shift = warning | Behavioral drift |

## Window Strategies
| Strategy | Reference Window | Production Window | Use Case |
|----------|----------------|-------------------|----------|
| Fixed baseline | Training data stats (frozen) | Rolling last N days | Stable concept deployment |
| Rolling reference | Last 30/90 days | Last 7 days | Non-stationary environments |
| Seasonal | Same period last year | Current period | Seasonal domains |
| A/B comparison | Control model | Treatment model | Shadow deployment |

## PSI Reference
| PSI Score | Interpretation | Action |
|-----------|---------------|--------|
| < 0.10 | No significant change | Monitor only |
| 0.10 - 0.20 | Slight shift | Investigate |
| > 0.20 | Major shift | Retrain or alert |

## Platform Comparison
| Platform | Strengths | Integration |
|----------|-----------|-------------|
| Evidently AI | Rich reports, open source, batch + streaming | Python SDK, REST API |
| Arize Phoenix | LLM-native, embedding drift, tracing | OpenTelemetry, SDK |
| Whylogs | Lightweight, statistical profiles, columnar | Python, Java, Spark |
| Custom | Full control, no external dependency | Direct implementation |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No reference window | Cannot compute drift without baseline |
| Threshold = 0 | Every tiny statistical fluctuation fires alerts |
| Monitoring "all features" generically | Alert fatigue; important signals drown in noise |
| No suppression window | Alert storms on correlated drift |
| Conflating drift with regression | Different root causes, different fixes |
