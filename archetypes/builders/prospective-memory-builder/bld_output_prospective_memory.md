---
quality: 8.6
quality: 8.0
kind: output_template
id: bld_output_template_prospective_memory
pillar: P05
llm_function: PRODUCE
purpose: Template for prospective_memory artifact production
title: "Output Template Prospective Memory"
version: "1.0.0"
author: n03_builder
tags: [prospective_memory, builder, output_template]
tldr: "Fill template to produce prospective_memory with owner, reminders, execution_mechanism."
domain: "prospective memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_output_template_schedule
  - bld_output_template_action_prompt
  - bld_output_template_entity_memory
  - bld_output_template_action_paradigm
  - bld_output_template_visual_workflow
  - bld_schema_dispatch_rule
  - p01_kc_dispatch_rule
  - bld_output_template_feature_flag
  - bld_output_template_optimizer
  - bld_output_template_checkpoint
---

# Output Template: prospective_memory
```yaml
id: p10_pm_{{agent_slug}}
kind: prospective_memory
pillar: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
owner: "{{agent_or_nucleus_id}}"
execution_mechanism: {{schedule_signal|polling|wake_notification}}
completion_policy: {{mark_done|re_schedule}}
reminders:
  - id: "{{reminder_id_1}}"
    trigger_type: {{time|event|condition}}
    trigger_value: "{{datetime_or_signal_or_condition}}"
    action_payload: "{{what_the_agent_should_do}}"
    priority: {{int_1_is_highest}}
    expiry: "{{YYYY-MM-DD|null}}"
    completion_policy: {{mark_done|re_schedule}}
    recurrence: {{null|cron_expression}}
  - id: "{{reminder_id_2}}"
    trigger_type: {{time|event|condition}}
    trigger_value: "{{trigger_value_2}}"
    action_payload: "{{action_2}}"
    priority: {{int}}
    expiry: "{{YYYY-MM-DD|null}}"
    completion_policy: mark_done
quality: null
tags: [prospective_memory, {{owner_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Overview
`{{what_agent_this_serves}}`
`{{types_of_future_actions_and_when_they_fire}}`

## Reminders
| ID | Trigger Type | Trigger Value | Action | Priority | Expiry |
|----|-------------|--------------|--------|----------|--------|
| {{id_1}} | {{trigger_type}} | {{trigger_value}} | {{action}} | {{priority}} | {{expiry}} |
| {{id_2}} | {{trigger_type}} | {{trigger_value}} | {{action}} | {{priority}} | {{expiry}} |

## Execution
Mechanism: `{{execution_mechanism}}`
`{{how_reminders_are_checked_and_fired}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_schedule]] | sibling | 0.23 |
| [[bld_output_template_action_prompt]] | sibling | 0.19 |
| [[bld_output_template_entity_memory]] | sibling | 0.19 |
| [[bld_output_template_action_paradigm]] | sibling | 0.19 |
| [[bld_output_template_visual_workflow]] | sibling | 0.18 |
| [[bld_schema_dispatch_rule]] | downstream | 0.17 |
| [[p01_kc_dispatch_rule]] | downstream | 0.17 |
| [[bld_output_template_feature_flag]] | sibling | 0.17 |
| [[bld_output_template_optimizer]] | sibling | 0.17 |
| [[bld_output_template_checkpoint]] | sibling | 0.16 |
