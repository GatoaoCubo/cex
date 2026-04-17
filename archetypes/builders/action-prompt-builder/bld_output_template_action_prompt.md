---
kind: output_template
id: bld_output_template_action_prompt
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an action_prompt
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Action Prompt"
version: "1.0.0"
author: n03_builder
tags: [action_prompt, builder, examples]
tldr: "Golden and anti-examples for action prompt construction, demonstrating ideal structure and common pitfalls."
domain: "action prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: action_prompt
```yaml
id: p03_ap_{{task_slug}}
kind: action_prompt
pillar: P03

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

title: "{{human_readable_title}}"
action: "{{verb_phrase_describing_task}}"
input_required:
  - "{{input_item_1_with_type}}"

  - "{{input_item_2_with_type}}"
output_expected: "{{output_structure_description}}"
purpose: "{{why_this_prompt_exists}}"
steps_count: {{integer_or_omit}}

timeout: "{{max_time_or_null}}"
edge_cases:
  - "{{edge_case_1}}"
  - "{{edge_case_2}}"

constraints:
  - "{{constraint_1}}"
domain: "{{domain_value}}"
quality: null

tags: [action_prompt, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Context
`{{background_2_3_sentences}}`
Purpose: `{{purpose_restated_concisely}}`
## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| `{{input_1}}` | {{type}} | `{{format}}` | YES |
| `{{input_2}}` | {{type}} | `{{format}}` | {{YES/NO}} |
## Execution
1. `{{step_1_transform_input}}`
2. `{{step_2_process}}`
3. `{{step_3_produce_output}}`
## Output
Format: `{{output_format}}`
Structure:
``{{format}}`
{{output_structure_example}}
```
## Validation
1. `{{criterion_1_verifiable}}`
2. `{{criterion_2_verifiable}}`
3. Edge case handled: `{{edge_case_1_check}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | action prompt construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
