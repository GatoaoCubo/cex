---
kind: output_template
id: bld_output_template_schedule
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a schedule artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Schedule"
version: "1.0.0"
author: n03_builder
tags: [schedule, builder, examples]
tldr: "Golden and anti-examples for schedule construction, demonstrating ideal structure and common pitfalls."
domain: "schedule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - schedule-builder
  - bld_schema_schedule
  - bld_instruction_schedule
  - p03_sp_schedule_builder
  - bld_examples_schedule
  - p11_qg_schedule
  - bld_architecture_schedule
  - p01_kc_schedule
  - bld_knowledge_card_schedule
  - p10_lr_schedule_builder
---

# Output Template: schedule
```yaml
id: p12_sc_{{schedule_slug}}
kind: schedule
pillar: P12

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

name: "{{human_readable_schedule_name}}"
trigger_type: {{cron|interval|event|manual|one_shot}}
cron: "{{cron_expression}}"
workflow_ref: "{{workflow_id}}"

quality: null
tags: [schedule, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
timezone: "{{America/Sao_Paulo|UTC}}"

enabled: {{true|false}}
start_date: "{{YYYY-MM-DD}}"
end_date: {{null|"YYYY-MM-DD"}}
max_concurrent: {{integer}}

catch_up: {{true|false}}
jitter: "{{0-30s|none}}"
description: "{{what_this_schedule_triggers_max_200ch}}"
```
## Overview
`{{what_this_schedule_triggers_1_to_2_sentences}}`
`{{frequency_and_primary_use_case}}`
## Trigger
1. Expression: `{{cron_expression}}` — `{{cron_plain_english_explanation}}`
2. Timezone: `{{timezone}}`
3. Enabled: {{true|false}}
4. Trigger type: {{cron|interval|event|manual|one_shot}}
## Workflow
1. Workflow: `{{workflow_ref}}`
2. Expected duration: `{{duration_estimate}}`
3. Dependencies: `{{upstream_data_or_services_required}}`
## Policy
1. Catch-up: {{true|false}} — `{{catch_up_rationale}}`
2. Max concurrent: `{{integer}}` — `{{concurrency_rationale}}`
3. Jitter: `{{jitter_value}}` — `{{jitter_rationale}}`
4. On failure: {{retry|alert|skip}} — `{{failure_handling_description}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | schedule construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[schedule-builder]] | downstream | 0.48 |
| [[bld_schema_schedule]] | downstream | 0.47 |
| [[bld_instruction_schedule]] | upstream | 0.47 |
| [[p03_sp_schedule_builder]] | upstream | 0.47 |
| [[bld_examples_schedule]] | downstream | 0.46 |
| [[p11_qg_schedule]] | downstream | 0.44 |
| [[bld_architecture_schedule]] | downstream | 0.44 |
| [[p01_kc_schedule]] | downstream | 0.42 |
| [[bld_knowledge_card_schedule]] | upstream | 0.39 |
| [[p10_lr_schedule_builder]] | downstream | 0.33 |
