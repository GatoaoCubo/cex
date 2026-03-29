---
kind: output_template
id: bld_output_template_enum_def
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an enum_def artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: enum_def
```yaml
id: p06_enum_{{enum_slug}}
kind: enum_def
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_enum_name}}"
values:
  - {{VALUE_1}}
  - {{VALUE_2}}
  - {{VALUE_3}}
default: "{{default_value_or_omit}}"
extensible: {{true|false}}
deprecated:
  - {{deprecated_value_or_omit_section}}
quality: null
tags: [enum_def, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_the_enum_represents_max_200ch}}"
descriptions:
  {{VALUE_1}}: "{{meaning_and_when_to_use}}"
  {{VALUE_2}}: "{{meaning_and_when_to_use}}"
  {{VALUE_3}}: "{{meaning_and_when_to_use}}"
representations:
  json_schema: '{"enum": [{{quoted_values_csv}}]}'
  pydantic: "{{PydanticEnumClassName}}"
  zod: 'z.enum([{{quoted_values_csv}}])'
  graphql: "enum {{GraphQLEnumName}} { {{VALUES_SPACE_SEPARATED}} }"
  typescript: 'type {{TypeName}} = {{quoted_values_pipe_separated}};'
```
## Overview
{{what_the_enum_represents_1_to_2_sentences}}
{{who_uses_it_and_primary_domain_context}}
## Values
### {{VALUE_1}}
{{description_of_this_value_and_when_to_use_it}}
### {{VALUE_2}}
{{description_of_this_value_and_when_to_use_it}}
### {{VALUE_3}}
{{description_of_this_value_and_when_to_use_it}}
## Usage
JSON Schema: `{"enum": [{{quoted_values_csv}}]}`
Pydantic: `class {{PydanticEnumClassName}}(str, Enum): {{VALUE_1}} = "{{VALUE_1}}"`
Zod: `z.enum([{{quoted_values_csv}}])`
GraphQL: `enum {{GraphQLEnumName}} { {{VALUES_SPACE_SEPARATED}} }`
TypeScript: `type {{TypeName}} = {{quoted_values_pipe_separated}};`
## Constraints
Default: {{default_value_or_"none"}}
Extensible: {{yes — new values may be added in future versions | no — set is closed}}
Deprecated: {{deprecated_value_list_with_reason_or_"none"}}
