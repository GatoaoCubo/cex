---
kind: output_template
id: bld_output_template_learning_record
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a learning_record
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
agent_node: "{{agent_node_name_or_null}}"
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
{{dense_overview_2_3_sentences}}
## Pattern
- {{concrete_step_that_worked_1}}
- {{concrete_step_that_worked_2}}
- {{concrete_step_that_worked_3}}
## Anti-Pattern
- {{specific_failure_1}}
- {{specific_failure_2}}
## Context
- Environment: {{runtime_environment}}
- Satellite: {{agent_node_involved}}
- Timing: {{when_it_happened}}
- Constraints: {{relevant_constraints}}
## Impact
- {{measurable_outcome_1}}
- {{measurable_outcome_2}}
## Reproducibility
- Conditions: {{what_must_be_true_to_repeat}}
- Confidence: {{HIGH_MEDIUM_LOW}}
- Caveats: {{edge_cases_or_limitations}}
## References
- {{reference_1}}
- {{reference_2}}
