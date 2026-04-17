---
kind: output_template
id: bld_output_template_drift_detector
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a drift_detector artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 7.8
title: "Output Template Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, output_template]
tldr: "Fill {{vars}} to produce a drift_detector artifact with method, thresholds, windows, and alert rule."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Output Template: drift_detector
```yaml
id: p11_dd_{{detector_slug}}
kind: drift_detector
pillar: P11
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
detection_method: {{psi|ks|chi_square|js_divergence|embedding_distance|custom}}
threshold:
  warning: {{float_lower}}
  critical: {{float_higher}}
drift_type: {{data|concept|prediction|behavioral}}
features_monitored:
  - "{{feature_or_dimension_1}}"
  - "{{feature_or_dimension_2}}"
window_config:
  reference: "{{baseline_description}}"
  production: "{{production_window_description}}"
alert_rule:
  destination: {{webhook|log|signal_file}}
  frequency: "{{hourly|daily|per_batch}}"
  suppression_window: "{{e.g._1h_after_alert}}"
platform: "{{Evidently|Arize|Whylogs|custom}}"
enabled: true
sampling_rate: {{0.0_to_1.0}}
quality: null
tags: [drift_detector, {{drift_type_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Overview
`{{what_this_detector_monitors_and_why_1_to_2_sentences}}`
`{{when_it_fires_and_what_action_follows}}`

## Detection Method
Method: `{{statistical_test}}`
Parameters: `{{test_specific_parameters}}`
Rationale: `{{why_this_test_for_this_feature_type}}`

## Window Config
| Window | Specification | Refresh |
|--------|--------------|---------|
| Reference | {{baseline_description}} | {{how_often_refreshed}} |
| Production | {{production_window}} | {{streaming_or_batch}} |

## Thresholds
| Level | Value | Interpretation | Action |
|-------|-------|---------------|--------|
| Warning | {{float}} | {{what_this_score_means}} | {{alert_and_investigate}} |
| Critical | {{float}} | {{what_this_score_means}} | {{alert_and_retrain}} |

## Alert Rule
Destination: `{{destination}}`
Frequency: `{{frequency}}`
Suppression: `{{suppression_policy}}`
Payload: `{{what_data_is_sent_in_alert}}`
