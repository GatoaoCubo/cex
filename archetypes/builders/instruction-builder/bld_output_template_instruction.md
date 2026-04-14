---
kind: output_template
id: bld_output_template_instruction
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an instruction
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Instruction"
version: "1.0.0"
author: n03_builder
tags: [instruction, builder, examples]
tldr: "Golden and anti-examples for instruction construction, demonstrating ideal structure and common pitfalls."
domain: "instruction construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: instruction
```yaml
id: p03_ins_{{task_slug}}
kind: instruction
pillar: P03

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

title: "{{human_readable_title}}"
target: "{{who_executes}}"
steps_count: {{integer_matching_body}}
prerequisites:

  - "{{prerequisite_1}}"
  - "{{prerequisite_2}}"
validation_method: {{checklist|automated|manual|none}}
idempotent: {{true|false}}

atomic: {{true|false}}
rollback: "{{undo_procedure_or_null}}"
dependencies:
  - "{{dependency_1}}"

logging: {{true|false}}
domain: "{{domain_value}}"
quality: null
tags: [instruction, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Prerequisites
1. `{{prerequisite_1_verifiable_condition}}`
2. `{{prerequisite_2_verifiable_condition}}`
## Steps
1. `{{action_1}}` — `{{expected_outcome_1}}`
2. `{{action_2}}` — `{{expected_outcome_2}}`
3. `{{action_3}}` — `{{expected_outcome_3}}`
{{...one action per step, repeat for steps_count}}
## Validation
1. [ ] `{{check_1_verifiable}}`
2. [ ] `{{check_2_verifiable}}`
3. [ ] Final outcome: `{{expected_final_state}}`
## Rollback
`{{rollback_procedure_or_na_if_idempotent}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | instruction construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
