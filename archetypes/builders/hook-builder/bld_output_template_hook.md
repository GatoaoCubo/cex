---
kind: output_template
id: bld_output_template_hook
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a hook artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Hook"
version: "1.0.0"
author: n03_builder
tags: [hook, builder, examples]
tldr: "Golden and anti-examples for hook construction, demonstrating ideal structure and common pitfalls."
domain: "hook construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: hook
```yaml
id: p04_hook_{{hook_slug}}
kind: hook
pillar: P04

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

trigger_event: "{{pre_tool_use|post_tool_use|session_start|session_end|user_prompt_submit|stop|subagent_stop|pre_compact|permission_request|notification|costm}}"
script_path: "{{path_to_script}}"
execution: "{{pre|post|both}}"
blocking: {{true|false}}

domain: "{{hook_domain}}"
quality: null
tags: [hook, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"

timeout: {{integer_ms}}
conditions: [{{condition_1}}, {{condition_2}}]
async: {{true|false}}
error_handling: "{{ignore|log|fail|retry}}"

logging: {{true|false}}
environment: [{{env_var_1}}, {{env_var_2}}]
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
density_score: {{0.80_to_1.00}}
```
## Trigger Configuration
Event: `{{trigger_event}}`
Execution: `{{execution}}` (`{{pre_post_description}}`)
Conditions:
1. `{{condition_description_1}}`
2. `{{condition_description_2}}`
## Script
Path: `{{script_path}}`
Language: `{{script_language}}`
Arguments: `{{script_args_or_none}}`
``{{script_language}}`
{{script_content_or_description}}
```
## Input/Output
Input (from event):
1. `{{input_field_1}}`: `{{input_description_1}}`
2. `{{input_field_2}}`: `{{input_description_2}}`
Output (to caller):
- `{{output_field_1}}`: `{{output_description_1}}`
## Error Handling
Strategy: `{{error_handling}}`
1. On script failure: `{{failure_behavior}}`
2. On timeout: `{{timeout_behavior}}`
3. On missing script: `{{missing_behavior}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | hook construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
