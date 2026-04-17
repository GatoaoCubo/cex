---
kind: output_template
id: bld_output_template_state_machine
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a state_machine artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: null
title: "Output Template State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, output_template]
tldr: "Fill-in template for state_machine: states table, transitions with guards/actions, guard definitions, action definitions."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Output Template: state_machine

```yaml
id: p12_sm_{{entity_slug}}
kind: state_machine
pillar: P12
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
entity: "{{EntityName}}"
initial_state: "{{INITIAL_STATE}}"
final_states: ["{{FINAL_STATE_1}}", "{{FINAL_STATE_2_optional}}"]
states_count: {{integer}}
transitions_count: {{integer}}
quality: null
tags: [state_machine, {{entity_slug}}, {{domain_tag}}]
tldr: "{{entity}} lifecycle FSM: {{states_count}} states, {{transitions_count}} transitions. {{brief_lifecycle_summary}}."
```

## States

| State | Type | Description |
|-------|------|-------------|
| {{STATE_1}} | initial | {{description}} |
| {{STATE_2}} | intermediate | {{description}} |
| {{STATE_N}} | final | {{description}} |

## Transitions

| from_state | event | to_state | guard | action |
|------------|-------|----------|-------|--------|
| {{FROM}} | {{EVENT}} | {{TO}} | {{guard_name()||"-"}} | {{action_name()||"-"}} |

## Guards

| Guard | Expression | Notes |
|-------|-----------|-------|
| {{guardName()}} | {{boolean_expression}} | {{when_it_is_true}} |

## Actions

| Action | Trigger | Effect |
|--------|---------|--------|
| {{actionName()}} | {{from_state}} -> {{to_state}} | {{what_happens}} |
