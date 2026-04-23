---
kind: quality_gate
id: p11_qg_drift_detector
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of drift_detector artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 8.8
title: "Gate: drift_detector"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, drift-detector, P11, monitoring]
tldr: "Pass/fail gate for drift_detector: detection_method, numeric threshold, named features, window_config, alert_rule."
domain: "drift_detector -- statistical monitor for distribution shift in model inputs, outputs, or behavioral patterns"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p11_qg_chunk_strategy
  - p11_qg_retriever_config
  - p11_qg_memory_scope
  - p11_qg_constraint_spec
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_prompt_version
  - p11_qg_vision_tool
  - p11_qg_function_def
  - p11_qg_enum_def
---

## Quality Gate

# Gate: drift_detector

## Definition
| Field | Value |
|---|---|
| metric | drift_detector artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: drift_detector` |

## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p11_dd_[a-z][a-z0-9_]+$` | ID has hyphens, uppercase, or missing prefix |
| H03 | ID equals filename stem | id vs filename mismatch |
| H04 | Kind equals literal `drift_detector` | `kind: monitor` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | detection_method is declared enum value | Missing or "statistical" (not in enum) |
| H07 | threshold has at least one numeric value | `threshold: "low"` or missing |
| H08 | features_monitored is non-empty list | `features_monitored: []` or generic "all" |
| H09 | alert_rule declared with destination | No alert_rule or missing destination |
| H10 | Tags list >= 3 items and includes "drift_detector" | Too few tags or missing required tag |

## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Method-feature alignment | 1.5 | Statistical test appropriate for feature type (KS/PSI for continuous, chi-square/JS for categorical) |
| Threshold calibration | 1.5 | Both warning and critical levels declared with values grounded in domain knowledge |
| Window config completeness | 1.0 | reference_window and production_window both specified |
| Alert rule quality | 1.0 | Destination, frequency, and suppression_window all declared |
| Feature specificity | 1.0 | Named dimensions, not generic; each feature is a real model I/O dimension |
| Boundary clarity | 0.5 | Not regression_check (no code assertions), not benchmark (no eval metrics) |
| Platform declaration | 0.5 | Platform field set (Evidently, Arize, Whylogs, or custom) |
| tldr quality | 0.5 | <= 160 chars, includes method, feature, and threshold |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Reference detector spec |
| >= 8.0 | Publish | Deploy to monitoring platform |
| >= 7.0 | Review | Add window_config or calibrate thresholds |
| < 7.0 | Reject | Return with gate failures |

## Never Bypass
- H01 (unparseable YAML)
- H05 (self-scored artifacts)
- H07 (string threshold breaks numeric comparison in monitoring platform)

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
