---
kind: output_template
id: bld_output_template_prompt_template
pillar: P00
quality: 9.0
title: "Output Template Prompt Template"
version: "1.0.0"
author: n03_builder
tags: [prompt_template, builder, examples]
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
domain: "prompt template construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: PRODUCE
---
id: p03_pt_`{{topic_slug}}`
kind: prompt_template
pillar: P03
title: "`{{title}}`"
version: "`{{version}}`"
created: "`{{created}}`"
updated: "`{{updated}}`"
author: "`{{author}}`"
variables:
  - name: "`{{var_name_1}}`"
    type: "`{{var_type_1}}`"
    required: `{{var_required_1}}`
    default: "`{{var_default_1}}`"
    description: "`{{var_description_1}}`"
  - name: "`{{var_name_2}}`"
    type: "`{{var_type_2}}`"
    required: `{{var_required_2}}`
    default: "`{{var_default_2}}`"
    description: "`{{var_description_2}}`"
variable_syntax: "`{{variable_syntax}}`"
composable: `{{composable}}`
domain: "`{{domain}}`"
quality: `{{quality}}`
tags: [`{{tags}}`]
tldr: "`{{tldr}}`"
keywords: [`{{keywords}}`]
density_score: `{{density_score}}`
---

# `{{title}}`
## Purpose
`{{purpose_paragraph}}`
## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `{{var_name_1}}` | {{var_type_1}} | {{var_required_1}} | {{var_default_1}} | `{{var_description_1}}` |
| `{{var_name_2}}` | {{var_type_2}} | {{var_required_2}} | {{var_default_2}} | `{{var_description_2}}` |
## Template Body
```
{{template_body}}
```
## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | `{{h01_status}}` | `{{h01_notes}}` |
| H02 required fields | `{{h02_status}}` | `{{h02_notes}}` |
| H03 no undeclared vars | `{{h03_status}}` | `{{h03_notes}}` |
| H04 no unused vars | `{{h04_status}}` | `{{h04_notes}}` |
| H05 size <= 8192 bytes | `{{h05_status}}` | `{{h05_notes}}` |
| H06 valid syntax tier | `{{h06_status}}` | `{{h06_notes}}` |
| H07 var fields complete | `{{h07_status}}` | `{{h07_notes}}` |
| H08 body non-empty | `{{h08_status}}` | `{{h08_notes}}` |
## Examples
### Filled Example
**Variables:**
```yaml
{{example_variables}}
```
**Rendered Output:**
```
{{example_rendered_output}}
```
