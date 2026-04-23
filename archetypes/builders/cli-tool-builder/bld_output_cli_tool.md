---
kind: output_template
id: bld_output_template_cli_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a cli_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Cli Tool"
version: "1.0.0"
author: n03_builder
tags: [cli_tool, builder, examples]
tldr: "Golden and anti-examples for cli tool construction, demonstrating ideal structure and common pitfalls."
domain: "cli tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_cli_tool
  - bld_schema_cli_tool
  - cli-tool-builder
  - p03_sp_cli_tool_builder
  - p10_lr_cli_tool_builder
  - bld_instruction_cli_tool
  - bld_output_template_input_schema
  - p11_qg_cli_tool
  - bld_output_template_function_def
  - bld_knowledge_card_cli_tool
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
`{{what_the_tool_does_1_to_2_sentences}}`
`{{who_runs_it_and_primary_use_case}}`
## Commands
### `{{command_name_1}}`
`{{binary}} {{command}} {{args}} [{{flags}}]`
`{{command_description}}`
Flags:

- `--`{{flag_1}} ({{type}}, {{default}}): `{{flag_description}}`
Args:
- `{{arg_1}}` ({{type}}, {{required|optional}}): `{{arg_description}}`
Returns: `{{output_description}}`
### `{{command_name_2}}`
`{{binary}} {{command}} [{{flags}}]`
`{{command_description}}`
Flags:

- `--`{{flag_1}} ({{type}}): `{{flag_description}}`
Returns: `{{output_description}}`
## Output
1. stdout: `{{primary_output_format_and_structure}}`
2. stderr: `{{error_and_progress_output}}`
3. Exit codes: `{{code_to_meaning_summary}}`
## Configuration
Config file: `{{config_file_path_and_format}}`
Env vars: `{{env_var_list_with_purpose}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | cli tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_cli_tool]] | downstream | 0.45 |
| [[bld_schema_cli_tool]] | downstream | 0.38 |
| [[cli-tool-builder]] | upstream | 0.36 |
| [[p03_sp_cli_tool_builder]] | upstream | 0.36 |
| [[p10_lr_cli_tool_builder]] | downstream | 0.32 |
| [[bld_instruction_cli_tool]] | upstream | 0.31 |
| [[bld_output_template_input_schema]] | sibling | 0.31 |
| [[p11_qg_cli_tool]] | downstream | 0.30 |
| [[bld_output_template_function_def]] | sibling | 0.29 |
| [[bld_knowledge_card_cli_tool]] | upstream | 0.28 |
