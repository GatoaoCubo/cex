---
kind: output_template
id: bld_output_template_runtime_state
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for runtime_state production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Runtime State"
version: "1.0.0"
author: n03_builder
tags: [runtime_state, builder, examples]
tldr: "Golden and anti-examples for runtime state construction, demonstrating ideal structure and common pitfalls."
domain: "runtime state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: runtime_state
```yaml
id: p10_rs_{{agent_slug}}
kind: runtime_state
pillar: P10
title: "Runtime State: {{agent_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
agent: "{{agent_name}}"
persistence: "{{session_or_cross_session}}"
domain: "{{domain_value}}"
quality: null
tags: [runtime-state, {{agent}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
routing_mode: "{{keyword_or_semantic_or_hybrid_or_rule_based}}"
priority_count: {{number}}
update_frequency: "{{per_task_or_per_session_or_on_trigger}}"
fallback_agent: "{{who_handles_failure}}"
density_score: {{0.80_to_1.00}}
constraint_count: {{number}}
linked_artifacts:
  primary: "{{related_mental_model_or_agent}}"
  related: [{{related_refs}}]
## Agent Context
{{which_agent_and_domain_context}}
## Routing Rules
| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| {{rule_1}} | {{when_triggered}} | {{what_happens}} | {{threshold}} |
| {{rule_2}} | {{when_triggered}} | {{what_happens}} | {{threshold}} |
## Decision Tree
```text
`{{input_condition}}`
  ├── `{{branch_1}}` -> `{{outcome_1}}`
  ├── `{{branch_2}}` -> `{{outcome_2}}`
  └── `{{fallback}}` -> `{{default_outcome}}`
```
## Priorities
1. {{highest_priority}} — {{rationale}}
2. {{second_priority}} — {{rationale}}
3. {{third_priority}} — {{rationale}}
## Heuristics
| Heuristic | When | Confidence |
|-----------|------|------------|
| {{rule_of_thumb_1}} | {{ambiguous_situation}} | {{confidence_level}} |
| {{rule_of_thumb_2}} | {{ambiguous_situation}} | {{confidence_level}} |
## Constraints
1. {{limit_1}}
2. {{limit_2}}
3. {{limit_3}}
## State Transitions
| Trigger | From | To | Condition |
|---------|------|----|-----------|
| {{event_1}} | {{state_a}} | {{state_b}} | {{when}} |
| {{event_2}} | {{state_b}} | {{state_c}} | {{when}} |
```
