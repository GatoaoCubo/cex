---
kind: output_template
id: bld_output_template_plugin
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a plugin artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Plugin"
version: "1.0.0"
author: n03_builder
tags: [plugin, builder, examples]
tldr: "Golden and anti-examples for plugin construction, demonstrating ideal structure and common pitfalls."
domain: "plugin construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: plugin

This ISO defines a plugin contract: the extension surface a host uses to load, register, and invoke external capability.
```yaml
id: p04_plug_{{plugin_slug}}
kind: plugin
pillar: P04

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

interface: "{{interface_contract_name}}"
lifecycle: [on_load, on_unload, {{additional_lifecycle_events}}]
enabled: {{true|false}}
api_surface_count: {{integer_matching_table}}

dependencies: [{{dep_1}}, {{dep_2}}]
domain: "{{plugin_domain}}"
quality: null
tags: [plugin, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
isolation: "{{sandboxed|shared|privileged}}"
hot_reload: {{true|false}}
config_schema:

  {{config_field_1}}:
    type: "{{string|integer|boolean|list|object}}"
    default: {{default_value}}
    required: {{true|false}}

    description: "{{field_description}}"
version_constraints: "{{semver_range}}"
priority: {{integer_loading_order}}
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]

density_score: {{0.80_to_1.00}}
```
## Interface Contract
Implements: `{{interface_contract_name}}`
Contract: `{{contract_description}}`
Required methods:
1. `{{required_method_1}}`: `{{method_description_1}}`
2. `{{required_method_2}}`: `{{method_description_2}}`
## API Surface
| Method | Input | Output | Description | Idempotent |
|--------|-------|--------|-------------|------------|
| `{{method_1}}` | {{input_1}} | {{output_1}} | `{{desc_1}}` | {{true|false}} |
| `{{method_2}}` | {{input_2}} | {{output_2}} | `{{desc_2}}` | {{true|false}} |
## Configuration
```yaml
{{config_field_1}}: {{default_value_1}}  # {{description_1}}
{{config_field_2}}: {{default_value_2}}  # {{description_2}}
```
## Lifecycle Hooks
1. **on_load**: `{{on_load_behavior}}`
2. **on_enable**: `{{on_enable_behavior}}`
3. **on_disable**: `{{on_disable_behavior}}`
4. **on_unload**: `{{on_unload_behavior}}`
## Dependencies
1. `{{dependency_1}}`: {{why_needed_1}} (`{{version_constraint_1}}`)
2. `{{dependency_2}}`: {{why_needed_2}} (`{{version_constraint_2}}`)
## Testing
1. Unit: `{{unit_test_strategy}}`
2. Integration: `{{integration_test_strategy}}`
3. Mock: `{{mock_strategy}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | plugin construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
