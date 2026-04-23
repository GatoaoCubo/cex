---
kind: output_template
id: bld_output_template_scoring_rubric
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for scoring_rubric production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Scoring Rubric"
version: "1.0.0"
author: n03_builder
tags: [scoring_rubric, builder, examples]
tldr: "Golden and anti-examples for scoring rubric construction, demonstrating ideal structure and common pitfalls."
domain: "scoring rubric construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_quality_gate
  - bld_examples_scoring_rubric
  - bld_schema_scoring_rubric
  - bld_output_template_golden_test
  - p03_sp_scoring_rubric_builder
  - bld_architecture_scoring_rubric
  - bld_config_scoring_rubric
  - p01_kc_scoring_rubric
  - bld_memory_scoring_rubric
  - bld_knowledge_card_scoring_rubric
---

# Output Template: scoring_rubric
```yaml
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_quality_gate]] | sibling | 0.43 |
| [[bld_examples_scoring_rubric]] | downstream | 0.35 |
| [[bld_schema_scoring_rubric]] | downstream | 0.35 |
| [[bld_output_template_golden_test]] | sibling | 0.31 |
| [[p03_sp_scoring_rubric_builder]] | upstream | 0.29 |
| [[bld_architecture_scoring_rubric]] | downstream | 0.28 |
| [[bld_config_scoring_rubric]] | downstream | 0.28 |
| [[p01_kc_scoring_rubric]] | downstream | 0.28 |
| [[bld_memory_scoring_rubric]] | downstream | 0.27 |
| [[bld_knowledge_card_scoring_rubric]] | upstream | 0.26 |
