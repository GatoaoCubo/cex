---
kind: output_template
id: bld_output_template_schedule
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a schedule artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_this_schedule_triggers_1_to_2_sentences}}
{{frequency_and_primary_use_case}}
## Trigger
- Expression: `{{cron_expression}}` — {{cron_plain_english_explanation}}
- Timezone: {{timezone}}
- Enabled: {{true|false}}
- Trigger type: {{cron|interval|event|manual|one_shot}}
## Workflow
- Workflow: `{{workflow_ref}}`
- Expected duration: {{duration_estimate}}
- Dependencies: {{upstream_data_or_services_required}}
## Policy
- Catch-up: {{true|false}} — {{catch_up_rationale}}
- Max concurrent: {{integer}} — {{concurrency_rationale}}
- Jitter: {{jitter_value}} — {{jitter_rationale}}
- On failure: {{retry|alert|skip}} — {{failure_handling_description}}
