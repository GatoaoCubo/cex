---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for response_format production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: response_format

```yaml
---
id: p05_rf_{{format_slug}}
kind: response_format
pillar: P05
title: "Response Format: {{format_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target_kind: "{{artifact_kind_or_task}}"
format_type: "{{json_or_yaml_or_markdown_or_csv_or_plaintext}}"
injection_point: "{{system_prompt_or_user_message}}"
sections: [{{section_1}}, {{section_2}}, {{section_3}}]
sections_count: {{integer_gte_1}}
domain: "{{domain_value}}"
quality: null
tags: [response-format, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
example_output: "see body"
composable: {{true_or_false}}
density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{target_kind_builder}}"
  related: [{{related_artifact_refs}}]
---

## Format Overview
{{what_structure_this_defines_and_for_what_task}}

## Sections
| # | Section | Description | Required | Constraints |
|---|---------|-------------|----------|-------------|
| 1 | {{section_1}} | {{description}} | {{yes/no}} | {{constraints}} |
| 2 | {{section_2}} | {{description}} | {{yes/no}} | {{constraints}} |
| 3 | {{section_3}} | {{description}} | {{yes/no}} | {{constraints}} |

## Example Output
```{{format_type}}
{{complete_example_showing_expected_shape}}
```

## Injection Instructions
- **Point**: {{system_prompt_or_user_message}}
- **Position**: {{where_in_the_prompt}}
- **Template**: "Respond using the following format: {{format_description}}"
- **Composable**: {{true/false}} — {{explanation}}

## References
- {{reference_1}}
- {{reference_2}}
```
