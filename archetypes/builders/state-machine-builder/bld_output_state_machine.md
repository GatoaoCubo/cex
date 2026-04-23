---
quality: 8.2
quality: 7.8
kind: output_template
id: bld_output_template_state_machine
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a state_machine artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
title: "Output Template State Machine"
version: "1.0.0"
author: n03_builder
tags: [state_machine, builder, output_template]
tldr: "Fill-in template for state_machine: states table, transitions with guards/actions, guard definitions, action definitions."
domain: "state machine construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p03_ins_lifecycle_rule
  - bld_output_template_input_schema
  - bld_output_template_entity_memory
  - bld_output_template_lifecycle_rule
  - p11_qg_lifecycle_rule
  - bld_schema_lifecycle_rule
  - bld_output_template_visual_workflow
  - bld_output_template_webhook
  - bld_output_template_embedding_config
  - bld_output_template_schedule
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_lifecycle_rule]] | upstream | 0.24 |
| [[bld_output_template_input_schema]] | sibling | 0.23 |
| [[bld_output_template_entity_memory]] | sibling | 0.22 |
| [[bld_output_template_lifecycle_rule]] | sibling | 0.21 |
| [[p11_qg_lifecycle_rule]] | downstream | 0.21 |
| [[bld_schema_lifecycle_rule]] | downstream | 0.21 |
| [[bld_output_template_visual_workflow]] | sibling | 0.21 |
| [[bld_output_template_webhook]] | sibling | 0.21 |
| [[bld_output_template_embedding_config]] | sibling | 0.20 |
| [[bld_output_template_schedule]] | sibling | 0.19 |
