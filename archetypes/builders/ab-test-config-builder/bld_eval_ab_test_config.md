---
kind: quality_gate
id: p11_qg_ab_test_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for ab_test_config
quality: 9.1
title: "Quality Gate Ab Test Config"
version: "1.0.0"
author: n03_builder
tags: [ab_test_config, builder, quality_gate]
tldr: "Artifact-level quality gate: validates ab_test_config YAML structure, hypothesis completeness, and statistical plan integrity (not runtime experiment metrics)."
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_examples_ab_test_config
  - bld_schema_ab_test_config
  - p11_qg_experiment_config
  - p11_qg_audit_log
  - p05_qg_github_issue_template
  - p07_qg_cohort_analysis
  - p09_qg_marketplace_app_manifest
  - p11_qg_feature_flag
  - p11_qg_function_def
  - p11_qg_ai_rmf_profile
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| schema_fields_present | 100% | == | frontmatter |
| variant_traffic_sum | 100 | == | variants list |
| score_minimum | 8.0 | >= | artifact |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Missing or malformed YAML |
| H02 | ID matches `^p11_abt_[a-z][a-z0-9_]+\.yaml$` | ID does not conform |
| H03 | `kind` field == `ab_test_config` | kind is wrong or missing |
| H04 | `hypothesis` present, non-empty, contains "if"+"then" structure | Hypothesis missing or malformed |
| H05 | `variants` list has >= 2 entries AND exactly one `is_control: true` | <2 variants or missing/multiple control |
| H06 | `variants[].traffic_pct` integers summing to 100 | Non-integer or sum != 100 |
| H07 | `primary_metric` object with `{name, type, direction, aggregation}` | Missing required keys |
| H08 | `guardrail_metrics` list present (may be empty only if decision_record justifies) | Field absent |
| H09 | `minimum_detectable_effect` present AND `sample_size_per_variant` present | Power plan incomplete |
| H10 | `statistical_method` in {frequentist_fixed, frequentist_sequential, bayesian} | Invalid or missing method |
| H11 | `quality: null` in frontmatter | Self-scored (must be null) |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Hypothesis clarity | 0.15 | 1.0: if/then/because + mechanism; 0.5: if/then only; 0.0: outcome-only |
| D2 | OEC specificity | 0.12 | 1.0: name+type+direction+aggregation; 0.5: name+direction; 0.0: name only |
| D3 | Guardrail coverage | 0.12 | 1.0: 2-3 guardrails covering retention+performance+revenue; 0.5: 1 guardrail; 0.0: none |
| D4 | Power analysis rigor | 0.13 | 1.0: alpha+power+baseline+MDE+n shown; 0.5: some; 0.0: none |
| D5 | Variant exclusivity | 0.10 | 1.0: mutual_exclusion_group set; 0.5: disjoint but unlabeled; 0.0: overlap risk |
| D6 | Randomization integrity | 0.08 | 1.0: unit+seed+sticky hash documented; 0.5: unit only; 0.0: unspecified |
| D7 | Stopping-rule discipline | 0.10 | 1.0: sequential method OR fixed horizon + peek policy; 0.0: ad-hoc stop |
| D8 | Analysis pre-registration | 0.10 | 1.0: subgroups+SRM+novelty window declared; 0.5: partial; 0.0: absent |
| D9 | Interoperability | 0.05 | 1.0: field names match Optimizely/Statsig/GrowthBook; 0.0: custom jargon |
| D10 | Reversibility | 0.05 | 1.0: kill-switch + rollout ramp; 0.0: all-or-nothing |

Weights sum = 1.00.

## Actions
| Score | Action |
|---|---|
| >= 9.5 | GOLDEN: approve for publication |
| >= 8.0 | PUBLISH: deploy to experimentation platform |
| >= 7.0 | REVIEW: return to author with scored rubric |
| < 7.0 | REJECT: rebuild -- power analysis or hypothesis missing |

## Bypass
| condition | approver | audit trail |
|---|---|---|
| Emergency rollback experiment | Head of Product + Data Science | Documented in incident log |
| Holdout / marketing test exempt from full OEC | Head of Data Science | Decision record required |

## Examples

## Golden Example
```yaml
kind: ab_test_config
title: "Homepage CTA Optimization"
description: "A/B test to evaluate impact of CTA button color and headline text on conversion rate"
experiment_name: "HomepageCTAExperiment"
tool: "Google Optimize"
variables:
  - name: primary_button_color
    variants: ["#FF4B5C", "#3498DB", "#2ECC71"]
  - name: hero_headline
    variants: ["Upgrade Now", "Get Started Today", "Join Thousands"]
audience:
  - segment: "US users"
  - segment: "Mobile Safari users"
metrics:
  - conversion_rate
  - click_through_rate
schedule:
  start: "2023-11-01"
  end: "2023-12-15"
```

## Anti-Example 1: Confusing with feature flag
```yaml
kind: feature_flag
title: "Toggle for new button color"
description: "Enable/disable blue button on checkout page"
flag_name: "checkout_button_color"
state: "off"
```
## Why it fails
This is a feature flag configuration, not an A/B test. It lacks experiment variables, audience segmentation, and metrics tracking required for conversion optimization experiments.

## Anti-Example 2: Missing critical fields
```yaml
kind: ab_test_config
title: "CTA Experiment"
description: "Test different CTA texts"
variables:
  - name: call_to_action
    variants: ["Sign Up", "Register Now"]
```
## Why it fails
Incomplete configuration missing essential fields: experiment name, tool integration, audience definition, metrics tracking, and schedule. Cannot be implemented or measured as a valid A/B test.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
