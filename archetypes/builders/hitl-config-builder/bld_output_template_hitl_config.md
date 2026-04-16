---
kind: output_template
id: bld_output_template_hitl_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a hitl_config artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.0
title: "Output Template Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, output_template, P11]
tldr: "Fill-in template for hitl_config: frontmatter + 5 body sections covering trigger, escalation, approval, timeout, fallback."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Output Template: hitl_config
```yaml
id: p11_hitl_{{name}}
kind: hitl_config
pillar: P11
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
workflow: "{{workflow_or_scope_name}}"
review_trigger: "{{evaluable_condition_e.g._confidence_lt_0.8}}"
escalation_chain:
  - "{{L1_role}}"
  - "{{L2_role}}"
approval_flow: "{{binary|edit|score}}"
timeout_seconds: {{integer_e.g._3600}}
fallback_action: "{{reject|accept_with_flag|retry}}"
quality: null
tags: [hitl_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_workflow_and_why_human_review_max_200ch}}"
max_queue_depth: {{integer_e.g._100}}
notification_channel: "{{email|slack|webhook}}"
priority_rules:
  - "{{condition_1_e.g._domain_eq_medical_then_priority_critical}}"
feedback_loop: "{{how_review_decisions_feed_model_training_or_omit}}"
```
## Overview
`{{what_workflow_is_being_reviewed_1_to_2_sentences}}`
`{{why_human_judgment_is_required_cannot_be_fully_automated}}`
`{{who_or_what_system_consumes_the_approved_output}}`
## Review Trigger
`{{precise_condition_description}}`
| Trigger | Condition | Data Source | Notes |
|---------|-----------|-------------|-------|
| `{{trigger_name}}` | {{evaluable_expression}} | {{where_value_comes_from}} | `{{notes}}` |
## Escalation Chain
| Level | Role | SLA (min) | Channel | Escalates When |
|-------|------|-----------|---------|---------------|
| L1 | `{{reviewer_role}}` | {{minutes}} | {{email_slack_webhook}} | `{{condition_to_escalate}}` |
| L2 | `{{reviewer_role}}` | {{minutes}} | {{channel}} | `{{condition_to_escalate}}` |
## Approval Flow
Flow type: **{{binary|edit|score}}**
| Action | Meaning | Downstream Effect |
|--------|---------|-------------------|
| `{{accept}}` | {{what_reviewer_confirms}} | `{{output_is_released_to_pipeline}}` |
| `{{reject}}` | {{what_reviewer_rejects}} | `{{output_is_discarded_or_flagged}}` |
## Timeout and Fallback
Timeout: **`{{timeout_seconds}}`s** (applies to each escalation level).
Fallback: **{{reject|accept_with_flag|retry}}** -- `{{justification_for_this_choice}}`.
## References
- `{{reference_1}}`
- `{{reference_2}}`
