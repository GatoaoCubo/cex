---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for scoring_rubric production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: scoring_rubric

```yaml
---
id: p07_sr_{{framework_slug}}
kind: scoring_rubric
pillar: P07
title: "Rubric: {{framework_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
framework: "{{framework_name}}"
target_kinds: [{{kind_1}}, {{kind_2}}]
dimensions_count: {{integer_gte_3}}
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "{{manual_or_semi_or_automated}}"
domain: "{{domain_value}}"
quality: null
tags: [scoring-rubric, {{framework}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
calibration_set: [{{golden_test_ref_1}}, {{golden_test_ref_2}}]
inter_rater_agreement: {{0.0_to_1.0}}
appeals_process: "{{how_to_contest_a_score}}"
linked_artifacts:
  primary: "{{target_kind_builder_or_schema}}"
  related: [{{related_artifact_refs}}]
---

## Framework Overview
{{what_it_measures_and_why}}

## Dimensions
| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| {{dim_1}} | {{pct}}% | 0-10 | {{concrete_criteria}} | {{high_example}} | {{mid_example}} |
| {{dim_2}} | {{pct}}% | 0-10 | {{concrete_criteria}} | {{high_example}} | {{mid_example}} |
| {{dim_3}} | {{pct}}% | 0-10 | {{concrete_criteria}} | {{high_example}} | {{mid_example}} |

## Thresholds
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | {{golden_action}} |
| PUBLISH | >= 8.0 | {{publish_action}} |
| REVIEW | >= 7.0 | {{review_action}} |
| REJECT | < 7.0 | {{reject_action}} |

## Calibration
{{examples_at_each_tier_with_rationale}}

## Automation
| Dimension | Status | Tool |
|-----------|--------|------|
| {{dim_1}} | {{manual_or_semi_or_automated}} | {{tool_ref}} |
| {{dim_2}} | {{manual_or_semi_or_automated}} | {{tool_ref}} |

## References
- {{reference_1}}
- {{reference_2}}
```
