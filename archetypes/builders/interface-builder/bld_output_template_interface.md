---
kind: output_template
id: bld_output_template_interface
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an interface
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_this_interface_enables_between_provider_and_consumer}}
## Methods
| # | Name | Input | Output | Description |
|---|------|-------|--------|-------------|
| 1 | {{method}} | {{input}} | {{output}} | {{desc}} |
| 2 | {{method}} | {{input}} | {{output}} | {{desc}} |
## Versioning
- **Version**: {{current_version}}
- **Backward compatible**: {{yes_no}}
- **Changes from previous**: {{changelog_or_initial}}
- **Migration notes**: {{migration_or_none}}
## Mock Specification
```json
{
  "method": "{{method_name}}",
  "input": {{example_input_json}},
  "output": {{example_output_json}}
}
```
## References
- {{reference_1}}
- {{reference_2}}
