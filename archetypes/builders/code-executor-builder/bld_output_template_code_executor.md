---
kind: output_template
id: bld_output_template_code_executor
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a code_executor artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Code Executor"
version: "1.0.0"
author: n03_builder
tags: [code_executor, builder, examples]
tldr: "Golden and anti-examples for code executor construction, demonstrating ideal structure and common pitfalls."
domain: "code executor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: code_executor
```yaml
id: p04_exec_{{runtime_slug}}
kind: code_executor
pillar: P04

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

name: "{{human_readable_executor_name}}"
runtime: {{python|node|bash|r|julia|go|multi}}
sandbox_type: {{docker|e2b|wasm|vm|process}}
languages:

  - "{{language_1}} {{version_constraint}}"
  - "{{language_2}} {{version_constraint}}"
timeout: {{seconds_integer}}
resource_limits:

  cpu: "{{cpu_limit}}"
  memory: "{{memory_limit}}"
  disk: "{{disk_limit}}"
network_access: {{true|false}}

file_io: {{true|false}}
persistent_session: {{true|false}}
quality: null
tags: [code_executor, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
description: "{{what_executor_does_max_200ch}}"
```
## Overview
`{{what_this_executor_provides_1_to_2_sentences}}`
`{{primary_use_case_and_who_uses_it}}`
## Sandbox
Isolation: `{{sandbox_type}}` — `{{security_boundary_description}}`
Escape prevention: `{{how_code_is_prevented_from_escaping_sandbox}}`
Session: `{{ephemeral_or_persistent}}` — `{{state_handling}}`
## Languages
### `{{language_1}}`
Version: `{{version_constraint}}`
Libraries: `{{pre_installed_libraries_if_any}}`
### `{{language_2}}`
Version: `{{version_constraint}}`
Libraries: `{{pre_installed_libraries_if_any}}`
## Limits
1. Timeout: `{{timeout_seconds}}`s per invocation
2. CPU: `{{cpu_limit}}`
3. Memory: `{{memory_limit}}`
4. Disk: `{{disk_limit}}`
5. Network: {{allowed|blocked}} — `{{network_policy_detail}}`
6. File I/O: {{read-write|read-only|none}} — `{{file_access_scope}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | code executor construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
