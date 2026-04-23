---
kind: output_template
id: bld_output_template_checkpoint
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a checkpoint artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Checkpoint"
version: "1.0.0"
author: n03_builder
tags: [checkpoint, builder, examples]
tldr: "Golden and anti-examples for checkpoint construction, demonstrating ideal structure and common pitfalls."
domain: "checkpoint construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_checkpoint_builder
  - bld_instruction_checkpoint
  - p11_qg_checkpoint
  - bld_examples_checkpoint
  - bld_schema_checkpoint
  - bld_architecture_checkpoint
  - bld_collaboration_checkpoint
  - checkpoint-builder
  - bld_knowledge_card_checkpoint
  - p10_lr_checkpoint_builder
---

# Output Template: checkpoint
```yaml
id: p12_ck_{{workflow_slug}}_{{step_slug}}
kind: checkpoint
pillar: P12
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_checkpoint_name}}"
workflow_ref: "{{workflow_artifact_id}}"
step: "{{step_name_in_workflow}}"
quality: null
tags: [checkpoint, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_this_checkpoint_captures_max_200ch}}"
state:
  {{key_1}}: {{type}} # {{size_hint}}
  {{key_2}}: {{type}} # {{size_hint}}
resumable: {{true|false}}
ttl: "{{24h|7d|30d|none}}"
parent_checkpoint: "{{p12_ck_previous_id|null}}"
retry_count: {{integer}}
error: {{null|"error_message_string"}}
```
## Overview
`{{what_workflow_state_this_checkpoint_captures_1_to_2_sentences}}`
`{{which_workflow_and_step_plus_why_this_point_matters}}`
## State
| Key | Type | Size | Description |
|-----|------|------|-------------|
| `{{key_1}}` | {{type}} | {{bytes_or_count}} | `{{what_this_value_represents}}` |
| `{{key_2}}` | {{type}} | {{bytes_or_count}} | `{{what_this_value_represents}}` |
Serialization format: {{yaml|json}}
Total state budget: `{{N}}` bytes (max 2048)
## Resume
Prerequisites:
- `{{prerequisite_1}}` (e.g., external service available, auth token valid)
- `{{prerequisite_2}}`
Resume steps:
1. Load checkpoint by id: `{{p12_ck_slug}}`
2. Restore state keys: `{{key_list}}`
3. Re-enter workflow at step: `{{step_name}}`
4. Validate state integrity: `{{validation_check}}`
Idempotent: {{yes|no}} — `{{reason}}`
## Lifecycle
TTL: `{{value}}` — `{{why_this_duration}}`
Cleanup: {{auto_delete|archive|manual}} after TTL expiry
Archival: `{{path_or_policy}}`
Chain: `{{parent_checkpoint}}` -> this -> `{{next_checkpoint_if_known}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_checkpoint_builder]] | upstream | 0.51 |
| [[bld_instruction_checkpoint]] | upstream | 0.48 |
| [[p11_qg_checkpoint]] | downstream | 0.48 |
| [[bld_examples_checkpoint]] | downstream | 0.48 |
| [[bld_schema_checkpoint]] | downstream | 0.47 |
| [[bld_architecture_checkpoint]] | downstream | 0.46 |
| [[bld_collaboration_checkpoint]] | downstream | 0.45 |
| [[checkpoint-builder]] | downstream | 0.45 |
| [[bld_knowledge_card_checkpoint]] | upstream | 0.44 |
| [[p10_lr_checkpoint_builder]] | downstream | 0.40 |
