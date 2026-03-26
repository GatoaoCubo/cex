---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a parser artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: parser

```yaml
---
id: p05_parser_{{parser_slug}}
kind: parser
pillar: P05
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
input_format: "{{text|json|html|xml|yaml|csv|log|mixed}}"
output_format: "{{json|yaml|csv|markdown|typed_object}}"
extraction_count: {{integer_matching_table}}
domain: "{{parser_domain}}"
quality: null
tags: [parser, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
error_strategy: "{{skip|default|fail|retry}}"
streaming: {{true|false}}
chunking: {{true|false}}
chunk_size: {{integer_bytes_or_null}}
normalization: [{{normalize_step_1}}, {{normalize_step_2}}]
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
density_score: {{0.80_to_1.00}}
---
```

## Extraction Rules

| Name | Target | Method | Pattern | Required | Default |
|------|--------|--------|---------|----------|---------|
| {{rule_name_1}} | {{target_field_1}} | {{method_1}} | {{pattern_1}} | {{true|false}} | {{default_or_dash}} |
| {{rule_name_2}} | {{target_field_2}} | {{method_2}} | {{pattern_2}} | {{true|false}} | {{default_or_dash}} |

## Input Specification
Format: {{input_format}}
Structure: {{description_of_expected_input}}
Example:
```{{input_format}}
{{sample_input}}
```

## Output Specification
Format: {{output_format}}
Schema:
```{{output_format}}
{{output_schema_with_types}}
```
Example:
```{{output_format}}
{{sample_output}}
```

## Error Handling
Strategy: {{error_strategy}}
- On extraction failure: {{failure_behavior}}
- On malformed input: {{malformed_behavior}}
- On partial match: {{partial_behavior}}
Fallback extraction: {{fallback_method_or_none}}

## Normalization
Pipeline (applied in order after extraction):
1. {{normalize_step_1}}: {{description}}
2. {{normalize_step_2}}: {{description}}

## References
- {{reference_1}}
- {{reference_2}}
