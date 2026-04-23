---
kind: output_template
id: bld_output_template_session_state
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a session_state
pattern: every field here exists in SCHEMA.md; template derives, never invents
quality: 9.0
title: "Output Template Session State"
version: "1.0.0"
author: n03_builder
tags: [session_state, builder, examples]
tldr: "Golden and anti-examples for session state construction, demonstrating ideal structure and common pitfalls."
domain: "session state construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_dag
  - bld_config_session_state
  - p03_ins_session_state_builder
  - bld_knowledge_card_session_state
  - bld_schema_session_state
  - bld_examples_session_state
  - session-state-builder
  - bld_output_template_action_prompt
  - bld_output_template_signal
  - p03_sp_session_state_builder
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
agent: "{{agent_or_agent_group}}"
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
1. Required fields (id through tldr) form the minimum valid snapshot
2. Optional fields capture richer execution context when available
3. Omit absent optional fields instead of writing placeholder values
4. Keep the snapshot ephemeral: no accumulated history, no persistent routing

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | session state construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_dag]] | sibling | 0.41 |
| [[bld_config_session_state]] | downstream | 0.40 |
| [[p03_ins_session_state_builder]] | upstream | 0.39 |
| [[bld_knowledge_card_session_state]] | upstream | 0.38 |
| [[bld_schema_session_state]] | downstream | 0.34 |
| [[bld_examples_session_state]] | downstream | 0.31 |
| [[session-state-builder]] | downstream | 0.29 |
| [[bld_output_template_action_prompt]] | sibling | 0.29 |
| [[bld_output_template_signal]] | sibling | 0.27 |
| [[p03_sp_session_state_builder]] | upstream | 0.26 |
