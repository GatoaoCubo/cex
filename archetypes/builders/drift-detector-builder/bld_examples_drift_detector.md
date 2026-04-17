---
kind: examples
id: bld_examples_drift_detector
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of drift_detector artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 8.6
title: "Examples Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, examples]
tldr: "Golden and anti-examples for drift_detector construction."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Examples: drift-detector-builder

## Golden Example
INPUT: "Create drift detector for CEX nucleus output quality distribution"
OUTPUT:
```yaml
id: p11_dd_nucleus_output_quality
kind: drift_detector
pillar: P11
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
detection_method: ks
threshold:
  warning: 0.05
  critical: 0.10
drift_type: behavioral
features_monitored:
  - "quality_score"
  - "density_score"
  - "gate_pass_rate"
window_config:
  reference: "Rolling 30-day average quality scores from N01-N06 artifacts"
  production: "Last 7 days of scored artifacts"
alert_rule:
  destination: signal_file
  frequency: daily
  suppression_window: "4h after alert"
platform: "custom"
enabled: true
sampling_rate: 1.0
quality: null
tags: [drift_detector, behavioral, nucleus_output, P11]
tldr: "Daily KS drift monitor on nucleus quality/density/gate_pass_rate; warning at 0.05, critical at 0.10."
```
## Overview
Monitors behavioral drift in CEX nucleus output quality metrics. Detects when quality_score, density_score, or gate_pass_rate distributions shift from the 30-day rolling baseline.

## Detection Method
Method: KS (Kolmogorov-Smirnov) -- nonparametric, no distributional assumptions, works on small samples.
Parameters: two-sample KS statistic; p-value threshold 0.05 warning, 0.10 critical.
Rationale: Quality scores are continuous; KS is preferred over PSI when baseline is not fixed.

## Thresholds
| Level | Value | Interpretation | Action |
|-------|-------|---------------|--------|
| Warning | 0.05 | Mild distribution shift | Alert + investigate recent commits |
| Critical | 0.10 | Significant shift | Alert + trigger quality audit |

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p11_dd_` (H02 pass)
- kind: drift_detector (H04 pass)
- detection_method: ks (H06 pass)
- threshold with both levels (H07 pass)
- features_monitored: 3 named dimensions (H08 pass)
- window_config declared (H09 pass)
- alert_rule with suppression (H10 pass)

## Anti-Example
INPUT: "Monitor my model for problems"
BAD OUTPUT:
```yaml
id: model-monitor
kind: monitor
detection: statistical
threshold: low
features: all
alert: yes
quality: 8.0
```
FAILURES:
1. id: "model-monitor" has hyphen, no `p11_dd_` prefix -> H02 FAIL
2. kind: "monitor" not "drift_detector" -> H04 FAIL
3. quality: 8.0 (not null) -> H05 FAIL
4. detection_method: "statistical" not in enum -> H06 FAIL
5. threshold: "low" is not a numeric value -> H07 FAIL
6. features_monitored: "all" is not a specific list -> H08 FAIL
7. No window_config -> H09 FAIL
8. alert_rule has no destination or frequency -> H10 FAIL
