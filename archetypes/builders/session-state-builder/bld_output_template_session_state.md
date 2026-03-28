---
kind: output_template
id: bld_output_template_session_state
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a session_state
pattern: every field here exists in SCHEMA.md; template derives, never invents
---

# Output Template: session_state
Naming pattern: `p10_ss_{session}.yaml`
Filename: `p10_ss_{{session_slug}}.yaml`
```yaml
id: p10_ss_{{session_slug}}
kind: session_state
lp: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
session_id: "{{unique_session_id}}"
agent: "{{agent_or_satellite}}"
status: "{{active|paused|completed|aborted}}"
started_at: "{{ISO_8601_timestamp}}"
domain: "{{domain_value}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
ended_at: "{{ISO_8601_or_omit}}"
duration_seconds: {{integer_or_omit}}
active_tasks: [{{task_labels_or_omit}}]
completed_tasks: [{{task_labels_or_omit}}]
context_window_used: {{integer_or_omit}}
context_window_max: {{integer_or_omit}}
tools_called: [{{tool_names_or_omit}}]
tool_call_count: {{integer_or_omit}}
errors:
  - code: "{{error_code_or_omit}}"
    message: "{{error_message_or_omit}}"
error_count: {{integer_or_omit}}
checkpoints:
  - label: "{{checkpoint_label_or_omit}}"
    timestamp: "{{ISO_8601_or_omit}}"
last_checkpoint: "{{label_or_omit}}"
keywords: [{{keyword_1}}, {{keyword_2}}]
linked_artifacts:
  primary: "{{primary_ref_or_omit}}"
  related: [{{related_refs_or_omit}}]
```
## Derivation Notes
- Required fields (id through tldr) form the minimum valid snapshot
- Optional fields capture richer execution context when available
- Omit absent optional fields instead of writing placeholder values
- Keep the snapshot ephemeral: no accumulated history, no persistent routing
