---
kind: output_template
id: bld_output_template_input_schema
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an input_schema
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: input_schema
```yaml
id: p06_is_{{scope_slug}}
kind: input_schema
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_operation_or_agent_this_serves}}"
fields:
  - name: "{{field_name}}"
    type: "{{string|integer|float|boolean|list|object}}"
    required: {{true|false}}
    default: {{default_value_or_null}}
    description: "{{what_this_field_is}}"
    error_message: "{{message_if_missing_or_invalid}}"
  - name: "{{field_name_2}}"
    type: "{{type}}"
    required: {{true|false}}
    default: {{default_value_or_null}}
    description: "{{description}}"
    error_message: "{{error_message_or_null}}"
coercion:
  - from: "{{source_type}}"
    to: "{{target_type}}"
    rule: "{{how_to_convert}}"
examples:
  - {{example_valid_payload_1}}
domain: "{{schema_domain}}"
quality: null
tags: [input-schema, {{scope_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
```
## Contract Definition
{{what_operation_this_input_serves_and_who_provides_data}}
## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | {{name}} | {{type}} | {{Y/N}} | {{default}} | {{desc}} |
| 2 | {{name}} | {{type}} | {{Y/N}} | {{default}} | {{desc}} |
## Coercion Rules
| From | To | Rule |
|------|----|------|
| {{source}} | {{target}} | {{conversion}} |
## Examples
```json
{{valid_example_payload}}
```
## References
- {{reference_1}}
- {{reference_2}}
