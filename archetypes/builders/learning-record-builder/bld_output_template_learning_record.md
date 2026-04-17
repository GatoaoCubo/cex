---
kind: output_template
id: bld_output_template_learning_record
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a learning_record
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Learning Record"
version: "1.0.0"
author: n03_builder
tags: [learning_record, builder, examples]
tldr: "Golden and anti-examples for learning record construction, demonstrating ideal structure and common pitfalls."
domain: "learning record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: learning_record
```yaml
id: p10_lr_{{topic_slug}}
kind: learning_record
pillar: P10

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

domain: "{{domain}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"

topic: "{{what_was_learned}}"
outcome: {{SUCCESS_or_PARTIAL_or_FAILURE}}
score: {{0.0_to_10.0}}
context: "{{when_where_this_happened}}"

agent_group: "{{agent_group_name_or_null}}"
reproducibility: {{HIGH_or_MEDIUM_or_LOW}}
impact: "{{measurable_impact}}"
timestamp: "{{ISO_8601_datetime}}"

dependencies: [{{dep_1}}]
keywords: [{{kw_1}}, {{kw_2}}, {{kw_3}}]
linked_artifacts:
  primary: {{primary_or_null}}

  related: [{{related_1}}]
```
## Summary
`{{dense_overview_2_3_sentences}}`
## Pattern
1. `{{concrete_step_that_worked_1}}`
2. `{{concrete_step_that_worked_2}}`
3. `{{concrete_step_that_worked_3}}`
## Anti-Pattern
1. `{{specific_failure_1}}`
2. `{{specific_failure_2}}`
## Context
1. Environment: `{{runtime_environment}}`
2. Agent_group: `{{agent_group_involved}}`
3. Timing: `{{when_it_happened}}`
4. Constraints: `{{relevant_constraints}}`
## Impact
1. `{{measurable_outcome_1}}`
2. `{{measurable_outcome_2}}`
## Reproducibility
1. Conditions: `{{what_must_be_true_to_repeat}}`
2. Confidence: `{{HIGH_MEDIUM_LOW}}`
3. Caveats: `{{edge_cases_or_limitations}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | learning record construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
