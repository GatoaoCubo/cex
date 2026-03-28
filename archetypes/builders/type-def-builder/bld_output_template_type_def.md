---
id: type-def-builder-output-template
kind: output_template
pillar: P05
llm_function: PRODUCE
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [output-template, type-def, P05, template]
---

## Template
```yaml
id: p06_td_{{type_slug}}
kind: type_def
pillar: P06
layer: spec
version: {{version}}
created: "{{created_date}}"
updated: "{{updated_date}}"
author: {{author}}
type_name: {{TypeName}}
base_type: {{base_type}}
domain: {{domain}}
nullable: {{nullable}}
quality: null
tags: {{tags_list}}
tldr: "{{one_sentence_description}}"
## Definition
{{prose_description_of_what_this_type_represents}}
## Constraints
{{constraint_key_1}}: {{constraint_value_1}}
{{constraint_key_2}}: {{constraint_value_2}}
## Composition
mode: {{composition_mode}}
members:
  - {{member_type_1}}
  - {{member_type_2}}
## Inheritance
extends: {{parent_type_def_id}}
## Generics
parameters:
  - name: {{type_param_name}}
    bound: {{type_param_bound}}
## Serialization
format: {{serialization_format}}
encoding: {{encoding}}
wire_type: {{wire_type}}
## Examples
- value: {{example_value_1}}
  note: "{{example_note_1}}"
- value: {{example_value_2}}
  note: "{{example_note_2}}"
## Keywords
{{keyword_1}}, {{keyword_2}}, {{keyword_3}}
```
