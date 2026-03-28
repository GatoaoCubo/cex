---
kind: output_template
id: bld_output_template_cli_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a cli_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: cli_tool
```yaml
id: p04_cli_{{tool_slug}}
kind: cli_tool
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_tool_name}}"
commands:
  - {{command_name_1}}
  - {{command_name_2}}
output_format: {{text|json|table|yaml}}
exit_codes:
  0: "{{success_meaning}}"
  1: "{{error_meaning}}"
quality: null
tags: [cli_tool, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_tool_does_max_200ch}}"
config_file: "{{config_path_and_format}}"
verbose: {{true|false}}
interactive: {{true|false}}
env_vars: [{{VAR_1}}, {{VAR_2}}]
platforms: [{{linux|macos|windows}}]
```
## Overview
{{what_the_tool_does_1_to_2_sentences}}
{{who_runs_it_and_primary_use_case}}
## Commands
### {{command_name_1}}
`{{binary}} {{command}} {{args}} [{{flags}}]`
{{command_description}}
Flags:
- `--{{flag_1}}` ({{type}}, {{default}}): {{flag_description}}
Args:
- `{{arg_1}}` ({{type}}, {{required|optional}}): {{arg_description}}
Returns: {{output_description}}
### {{command_name_2}}
`{{binary}} {{command}} [{{flags}}]`
{{command_description}}
Flags:
- `--{{flag_1}}` ({{type}}): {{flag_description}}
Returns: {{output_description}}
## Output
- stdout: {{primary_output_format_and_structure}}
- stderr: {{error_and_progress_output}}
- Exit codes: {{code_to_meaning_summary}}
## Configuration
Config file: {{config_file_path_and_format}}
Env vars: {{env_var_list_with_purpose}}
