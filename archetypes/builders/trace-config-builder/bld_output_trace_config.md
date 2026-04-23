---
kind: output_template
id: bld_output_template_trace_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a trace_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Trace Config"
version: "1.0.0"
author: n03_builder
tags: [trace_config, builder, examples]
tldr: "Golden and anti-examples for trace config construction, demonstrating ideal structure and common pitfalls."
domain: "trace config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_trace_config
  - bld_schema_trace_config
  - p11_qg_trace_config
  - p07_tc_opentelemetry
  - bld_config_trace_config
  - bld_knowledge_card_trace_config
  - p03_sp_trace_config_builder
  - p01_kc_trace_config
  - p10_lr_trace_config_builder
  - bld_architecture_trace_config
---

# Output Template: trace_config
```yaml
id: p07_tc_{{name}}
kind: trace_config
pillar: P07
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
enabled: {{true|false}}
sample_rate: {{0.0_to_1.0}}
export_format: {{otlp|langsmith|console|json_file}}
export_path: "{{endpoint_url_or_filesystem_path}}"
capture_prompts: {{true|false}}
capture_responses: {{true|false}}
span_attributes:
  - cex.nucleus
  - cex.kind
  - cex.8f.function
  - {{costm_attribute_1}}
  - {{costm_attribute_2}}
retention_days: {{positive_integer}}
quality: null
tags: [trace_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_config_covers_max_200ch}}"
scope: "{{agent_or_system_scope}}"
environment: {{development|staging|production|evaluation}}
error_classification:
  transient: "{{transient_error_types}}"
  permanent: "{{permanent_error_types}}"
```
## Tracing Specification
`{{enabled_state_and_sample_rate_rationale}}`
Export via `{{export_format}}` to `{{export_path}}`.
`{{why_this_configuration_fits_the_environment}}`
## Capture Rules
| Category | Captured | Rationale |
|----------|----------|-----------|
| `{{category_1}}` | {{YES|NO}} | `{{rationale}}` |
| `{{category_2}}` | {{YES|NO}} | `{{rationale}}` |
| `{{category_3}}` | {{YES|NO}} | `{{rationale}}` |
## Span Attributes
| Span | Attributes | 8F Mapping |
|------|-----------|-----------|
| `cex.pipeline` | `{{root_attributes}}` | Root span |
| `cex.8f.`{{function}} | `{{function_attributes}}` | {{F1-F8}} |
| `cex.llm.call` | `{{llm_attributes}}` | LLM invocation |
## Retention Policy
| Tier | Days | Storage | Cleanup |
|------|------|---------|---------|
| Hot | `{{days}}` | {{storage_type}} | `{{cleanup_strategy}}` |
| Warm | `{{days}}` | {{storage_type}} | `{{cleanup_strategy}}` |
| Cold | `{{days}}` | {{storage_type}} | `{{cleanup_strategy}}` |
## Privacy Controls
`{{pii_redaction_rules}}`
`{{prompt_capture_policy}}`
## References
- `{{reference_1}}`
- `{{reference_2}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_trace_config]] | downstream | 0.53 |
| [[bld_schema_trace_config]] | downstream | 0.44 |
| [[p11_qg_trace_config]] | downstream | 0.40 |
| [[p07_tc_opentelemetry]] | downstream | 0.34 |
| [[bld_config_trace_config]] | downstream | 0.33 |
| [[bld_knowledge_card_trace_config]] | upstream | 0.33 |
| [[p03_sp_trace_config_builder]] | upstream | 0.33 |
| [[p01_kc_trace_config]] | downstream | 0.28 |
| [[p10_lr_trace_config_builder]] | downstream | 0.28 |
| [[bld_architecture_trace_config]] | downstream | 0.28 |
