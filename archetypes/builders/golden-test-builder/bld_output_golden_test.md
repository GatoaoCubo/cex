---
kind: output_template
id: bld_output_template_golden_test
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for golden_test production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Golden Test"
version: "1.0.0"
author: n03_builder
tags: [golden_test, builder, examples]
tldr: "Golden and anti-examples for golden test construction, demonstrating ideal structure and common pitfalls."
domain: "golden test construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_unit_eval
  - bld_output_template_input_schema
  - bld_output_template_embedding_config
  - bld_output_template_feature_flag
  - bld_output_template_e2e_eval
  - bld_output_template_validation_schema
  - bld_output_template_runtime_rule
  - golden-test-builder
  - bld_output_template_output_validator
  - bld_config_golden_test
---

# Output Template: golden_test
```yaml
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
## Input Scenario
{{verbatim_request_or_prompt}}
## Golden Output
{{complete_artifact_no_abbreviation}}
## Rationale
{{mapped_to_gate_ids_h01_s03_etc}}
## Evaluation Criteria
{{specific_checks_this_validates}}
## References
1. {{reference_1}}
2. {{reference_2}}
```

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | golden test construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_unit_eval]] | sibling | 0.42 |
| [[bld_output_template_input_schema]] | sibling | 0.41 |
| [[bld_output_template_embedding_config]] | sibling | 0.38 |
| [[bld_output_template_feature_flag]] | sibling | 0.38 |
| [[bld_output_template_e2e_eval]] | sibling | 0.37 |
| [[bld_output_template_validation_schema]] | sibling | 0.37 |
| [[bld_output_template_runtime_rule]] | sibling | 0.36 |
| [[golden-test-builder]] | downstream | 0.35 |
| [[bld_output_template_output_validator]] | sibling | 0.34 |
| [[bld_config_golden_test]] | downstream | 0.33 |
