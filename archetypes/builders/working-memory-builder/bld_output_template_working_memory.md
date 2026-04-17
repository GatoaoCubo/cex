---
kind: output_template
id: bld_output_template_working_memory
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a working_memory artifact
quality: 7.5
title: "Output Template Working Memory"
version: "1.0.0"
author: n03_builder
tags: [working_memory, builder, output_template]
tldr: "Fill {{vars}} to produce a working_memory artifact with task binding, typed slots, and clear policy."
domain: "working memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Output Template: working_memory
```yaml
id: p10_wm_{{task_slug}}
kind: working_memory
pillar: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
task_id: "{{task_or_agent_id_this_memory_binds_to}}"
context_slots:
  {{slot_name_1}}: "{{type_string|int|float|bool|list|json}}"
  {{slot_name_2}}: "{{type}}"
  {{slot_name_3}}: "{{type}}"
capacity_limit:
  value: {{int}}
  unit: {{tokens|slots}}
expiry: "{{TTL_e.g._30min|on_task_complete|on_session_end}}"
clear_on_complete: {{clear|promote}}
promote_targets: [{{entity_memory|episodic_memory|learning_record}}]
nucleus: "{{n0x}}"
quality: null
tags: [working_memory, {{nucleus_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_task_this_serves_max_200ch}}"
```
## Overview
`{{what_task_this_working_memory_serves_1_to_2_sentences}}`
`{{why_working_memory_is_needed_for_this_task}}`

## Context Slots
| Slot Name | Type | Purpose | Example Value |
|-----------|------|---------|--------------|
| `{{slot_name_1}}` | {{type}} | {{what_this_slot_holds}} | `{{example}}` |
| `{{slot_name_2}}` | {{type}} | {{what_this_slot_holds}} | `{{example}}` |
| `{{slot_name_3}}` | {{type}} | {{what_this_slot_holds}} | `{{example}}` |

## Capacity and Expiry
Capacity: `{{value}} {{unit}}`
Expiry: `{{expiry_policy}}`
Rationale: `{{why_this_capacity_and_expiry_is_appropriate}}`

## Clear Policy
Policy: `{{clear|promote}}`
`{{what_happens_when_task_completes}}`
Promoted to: `{{target_memory_kind}}` (for slots: `{{which_slots}}`)
