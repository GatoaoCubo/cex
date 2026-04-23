---
kind: output_template
id: bld_output_template_boot_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a boot_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Boot Config"
version: "1.0.0"
author: n03_builder
tags: [boot_config, builder, examples]
tldr: "Golden and anti-examples for boot config construction, demonstrating ideal structure and common pitfalls."
domain: "boot config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_boot_config
  - bld_examples_boot_config
  - p11_qg_boot_config
  - p03_sp_boot_config_builder
  - bld_knowledge_card_boot_config
  - bld_instruction_boot_config
  - bld_output_template_agent_card
  - boot-config-builder
  - bld_output_template_embedding_config
  - p10_lr_boot-config-builder
---

# Output Template: boot_config
```yaml
id: p02_boot_{{provider_slug}}
kind: boot_config
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
provider: "{{provider_name}}"
identity:
  name: "{{agent_display_name}}"
  role: "{{primary_role}}"
  agent_group: "{{agent_group_or_agnostic}}"
constraints:
  max_tokens: {{integer}}
  context_window: {{integer}}
  timeout_seconds: {{integer}}
  max_retries: {{integer}}
  temperature: {{float}}
tools: [{{tool_1}}, {{tool_2}}, {{tool_3}}]
model: "{{model_identifier}}"
temperature: {{0.0-2.0}}
flags: [{{flag_1}}, {{flag_2}}]
mcp_config:
  {{mcp_name}}: {{mcp_transport}}
permissions:
  read: [{{read_scope}}]
  write: [{{write_scope}}]
  execute: [{{exec_scope}}]
system_prompt_ref: "{{system_prompt_artifact_id_or_null}}"
domain: "{{config_domain}}"
quality: null
tags: [boot-config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Provider Overview
`{{provider_name}}` runtime for `{{agent_role}}` agents.
`{{one_sentence_runtime_characteristics}}`
## Identity Block
Name: `{{agent_display_name}}`
Role: `{{primary_role}}`
Agent_group: `{{agent_group_name}}`
## Constraints
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| max_tokens | `{{value}}` | `{{why}}` |
| context_window | `{{value}}` | `{{why}}` |
| timeout_seconds | `{{value}}` | `{{why}}` |
| max_retries | `{{value}}` | `{{why}}` |
## Tools Configuration
| Tool | Type | Purpose |
|------|------|---------|
| `{{tool_1}}` | {{mcp|cli|api}} | `{{purpose_1}}` |
| `{{tool_2}}` | {{mcp|cli|api}} | `{{purpose_2}}` |
## Flags
| Flag | Purpose |
|------|---------|
| `{{flag_1}}` | `{{purpose_1}}` |
| `{{flag_2}}` | `{{purpose_2}}` |
## References
- Provider docs: `{{provider_doc_url}}`
- Related config: `{{related_boot_config_or_none}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_boot_config]] | downstream | 0.42 |
| [[bld_examples_boot_config]] | downstream | 0.41 |
| [[p11_qg_boot_config]] | downstream | 0.37 |
| [[p03_sp_boot_config_builder]] | upstream | 0.33 |
| [[bld_knowledge_card_boot_config]] | upstream | 0.32 |
| [[bld_instruction_boot_config]] | upstream | 0.31 |
| [[bld_output_template_agent_card]] | sibling | 0.29 |
| [[boot-config-builder]] | upstream | 0.28 |
| [[bld_output_template_embedding_config]] | sibling | 0.28 |
| [[p10_lr_boot-config-builder]] | downstream | 0.24 |
