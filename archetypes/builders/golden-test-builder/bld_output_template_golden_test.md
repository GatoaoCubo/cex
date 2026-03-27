---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for golden_test production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: golden_test

```yaml
---
id: p07_gt_{{case_slug}}
kind: golden_test
pillar: P07
title: "Golden: {{case_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target_kind: "{{artifact_kind_being_tested}}"
input: "{{request_prompt}}"
golden_output_ref: "{{path_or_inline}}"
quality_threshold: {{9.5_or_higher}}
rationale: "{{why_golden_with_gate_refs}}"
edge_case: {{true_or_false}}
reviewer: "{{who_approved}}"
approval_date: "{{YYYY-MM-DD}}"
domain: "{{domain_value}}"
quality: null
tags: [golden-test, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{target_kind_builder_or_schema}}"
  related: [{{related_artifact_refs}}]
---

## Input Scenario
{{verbatim_request_or_prompt}}

## Golden Output
{{complete_artifact_no_abbreviation}}

## Rationale
{{mapped_to_gate_ids_h01_s03_etc}}

## Evaluation Criteria
{{specific_checks_this_validates}}

## References
- {{reference_1}}
- {{reference_2}}
```
