---
kind: collaboration
id: bld_collaboration_drift_detector
pillar: P12
llm_function: COLLABORATE
purpose: How drift-detector-builder works in crews with other builders
quality: 8.6
title: "Collaboration Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, collaboration]
tldr: "drift-detector-builder is the distribution shift monitor in MLOps and alignment crews."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Collaboration: drift-detector-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what statistical method, threshold, and alert rule should continuously monitor this model's input/output distribution?"
I do not evaluate point-in-time quality. I do not test code regressions. I do not curate training data.
I produce the runtime monitoring configuration that keeps a deployed model's behavior within expected bounds.

## Crew Compositions

### Crew: "MLOps Deployment"
```
  1. env-config-builder -> "deployment environment configuration"
  2. rate-limit-config-builder -> "API throttle configuration"
  3. drift-detector-builder -> "distribution shift monitor for deployed model"
  4. bugloop-builder -> "automated fix cycles triggered by alerts"
```

### Crew: "Alignment Monitoring"
```
  1. preference-dataset-builder -> "training preference pairs"
  2. benchmark-builder -> "pre/post training evaluation"
  3. drift-detector-builder -> "ongoing behavioral drift monitor post-deployment"
  4. learning-record-builder -> "record of drift incidents and root causes"
```

## Handoff Protocol

### I Receive
- seeds: model name, domain, features to monitor, existing baseline distribution stats
- optional: platform preference (Evidently, Arize, Whylogs)
- optional: alert routing destination (webhook URL, signal file path)

### I Produce
- drift_detector artifact (.md with YAML frontmatter)
- committed to: `N05_operations/P11_feedback/p11_dd_{scope}.md`

### I Signal
- signal: complete (with quality score)
- if quality < 8.0: retry with failures (common: missing window_config, string threshold)

## Builders I Depend On
| Builder | Why |
|---------|-----|
| benchmark-builder | Establishes baseline performance; reference window often derived from benchmark run |
| env-config-builder | Platform credentials and endpoint config for drift monitoring platform |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| bugloop-builder | Automated fix cycles triggered when drift_detector fires critical alert |
| learning-record-builder | Drift incidents recorded as learning events with root cause analysis |
| retraining-trigger-builder | Drift critical threshold triggers retraining pipeline dispatch |

## Conflict Resolution
| Scenario | Resolution |
|----------|-----------|
| Drift vs regression | drift_detector = distribution shift (statistical). regression_check = code behavior change (assertions). Different tools. |
| Drift vs benchmark | drift_detector = continuous runtime monitor. benchmark = point-in-time evaluation. Complementary, not competing. |
| Multiple features with different test types | Create separate detector artifacts per feature group, or use platform with per-feature method config. |
