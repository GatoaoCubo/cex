---
kind: output_template
id: bld_output_template_interface
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an interface
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Interface"
version: "1.0.0"
author: n03_builder
tags: [interface, builder, examples]
tldr: "Golden and anti-examples for interface construction, demonstrating ideal structure and common pitfalls."
domain: "interface construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: interface
```yaml
id: p06_iface_{{contract_slug}}
kind: interface
pillar: P06

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

contract: "{{human_readable_contract_name}}"
provider: "{{provider_agent_or_system}}"
consumer: "{{consumer_agent_or_system}}"
methods:

  - name: "{{method_name}}"
    input: {{input_type_or_object}}
    output: {{output_type_or_object}}
    description: "{{what_this_method_does}}"

backward_compatible: {{true|false}}
deprecation:
  deprecated_methods: [{{method_names_or_empty}}]
  sunset_date: "{{YYYY-MM-DD_or_null}}"

  migration: "{{migration_notes_or_null}}"
mock:
  enabled: {{true|false}}
  example_payloads:

    - method: "{{method_name}}"
      input: {{example_input}}
      output: {{example_output}}
domain: "{{integration_domain}}"

quality: null
tags: [interface, {{provider_tag}}, {{consumer_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
```
## Contract Definition
`{{what_this_interface_enables_between_provider_and_consumer}}`
## Methods
| # | Name | Input | Output | Description |
|---|------|-------|--------|-------------|
| 1 | `{{method}}` | {{input}} | {{output}} | `{{desc}}` |
| 2 | `{{method}}` | {{input}} | {{output}} | `{{desc}}` |
## Versioning
1. **Version**: `{{current_version}}`
2. **Backward compatible**: `{{yes_no}}`
3. **Changes from previous**: `{{changelog_or_initial}}`
4. **Migration notes**: `{{migration_or_none}}`
## Mock Specification
```json
{
  "method": "{{method_name}}",
  "input": {{example_input_json}},

  "output": {{example_output_json}}
}
```
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | interface construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
