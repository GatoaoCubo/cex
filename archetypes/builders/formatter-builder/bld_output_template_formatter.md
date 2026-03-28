---
kind: output_template
id: bld_output_template_formatter
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a formatter artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: formatter
```yaml
id: p05_fmt_{{formatter_slug}}
kind: formatter
pillar: P05
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target_format: "{{json|yaml|markdown|html|csv|text|xml|table}}"
input_type: "{{structured_data|raw_text|typed_object|mixed}}"
rule_count: {{integer_matching_table}}
domain: "{{formatter_domain}}"
quality: null
tags: [formatter, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
template_engine: "{{mustache|jinja2|handlebars|string_format|custom|none}}"
pretty_print: {{true|false}}
escaping: "{{html|url|json|xml|shell|none}}"
encoding: "{{utf8|ascii|latin1}}"
locale: "{{locale_code_or_null}}"
streaming: {{true|false}}
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
density_score: {{0.80_to_1.00}}
```
## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| {{rule_name_1}} | {{input_field_1}} | {{transform_1}} | {{pattern_1}} | {{options_1}} |
| {{rule_name_2}} | {{input_field_2}} | {{transform_2}} | {{pattern_2}} | {{options_2}} |
## Input Specification
Type: {{input_type}}
Structure: {{description_of_expected_input}}
Example:
```{{input_format}}
{{sample_input}}
```
## Output Specification
Format: {{target_format}}
Example:
```{{target_format}}
{{sample_output}}
```
## Template
Engine: {{template_engine}}
```{{template_syntax}}
{{formatting_template}}
```
## Edge Cases
- Null values: {{null_handling}}
- Empty strings: {{empty_handling}}
- Special characters: {{special_char_handling}}
- Overflow: {{overflow_handling}}
## References
- {{reference_1}}
- {{reference_2}}
