---
kind: output_template
id: bld_output_template_smoke_eval
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for smoke_eval production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Smoke Eval"
version: "1.0.0"
author: n03_builder
tags: [smoke_eval, builder, examples]
tldr: "Golden and anti-examples for smoke eval construction, demonstrating ideal structure and common pitfalls."
domain: "smoke eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_unit_eval
  - bld_output_template_e2e_eval
  - bld_output_template_golden_test
  - bld_knowledge_card_smoke_eval
  - bld_output_template_input_schema
  - bld_output_template_runtime_rule
  - bld_config_smoke_eval
  - bld_output_template_feature_flag
  - bld_output_template_embedding_config
  - bld_output_template_output_validator
---

# Output Template: smoke_eval
```yaml
id: p07_se_{{scope_slug}}
kind: smoke_eval
pillar: P07
title: "{{eval_title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_is_being_tested}}"
critical_path:
  - "{{step_1}}"
  - "{{step_2}}"
  - "{{step_3}}"
timeout: {{max_30_seconds}}
assertions:
  - check: "{{what_to_verify}}"
    expected: "{{expected_result}}"
    timeout_ms: {{milliseconds}}
fast_fail: true
prerequisites:
  - "{{prerequisite_1}}"
  - "{{prerequisite_2}}"
environment: "{{target_environment}}"
health_check: "{{health_endpoint_or_check}}"
frequency: "{{how_often}}"
alerting: "{{who_to_notify}}"
domain: "{{domain_value}}"
quality: null
tags: [smoke-eval, {{scope}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
## Critical Path
{{ordered_minimum_checks}}
## Assertions
{{fast_binary_checks_with_timeouts}}
## Prerequisites
{{what_must_exist_before_running}}
## On Failure
{{action_on_failure}}
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
| Domain | smoke eval construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_unit_eval]] | sibling | 0.47 |
| [[bld_output_template_e2e_eval]] | sibling | 0.44 |
| [[bld_output_template_golden_test]] | sibling | 0.39 |
| [[bld_knowledge_card_smoke_eval]] | downstream | 0.38 |
| [[bld_output_template_input_schema]] | sibling | 0.37 |
| [[bld_output_template_runtime_rule]] | sibling | 0.35 |
| [[bld_config_smoke_eval]] | downstream | 0.35 |
| [[bld_output_template_feature_flag]] | sibling | 0.35 |
| [[bld_output_template_embedding_config]] | sibling | 0.34 |
| [[bld_output_template_output_validator]] | sibling | 0.33 |
