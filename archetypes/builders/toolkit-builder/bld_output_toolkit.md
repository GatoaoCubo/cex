---
kind: output_template
id: bld_output_template_toolkit
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a toolkit
pattern: every field here exists in the schema; template derives, never invents
quality: 9.1
title: "Output Template Toolkit"
version: "1.0.0"
author: n03_builder
tags: [toolkit, builder, examples]
tldr: "Golden and anti-examples for toolkit construction, demonstrating ideal structure and common pitfalls."
domain: "toolkit construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_toolkit
  - bld_schema_toolkit
  - p03_ins_toolkit_builder
  - bld_knowledge_card_toolkit
  - bld_config_toolkit
  - p03_sp_toolkit_builder
  - bld_tools_toolkit
  - p01_kc_toolkit
  - toolkit-builder
  - p11_qg_toolkit
---

# Output Template: toolkit
Naming pattern: `p04_tk_{name}.yaml`
Filename: `p04_tk_{{name}}.yaml`
```yaml
---
id: p04_tk_{{name}}
kind: toolkit
pillar: P04
quality: null
tags: [toolkit, {{category}}, P04]
---

name: "{{toolkit_name_snake_case}}"
category: "{{file_ops|git_ops|search|web|system|build|analysis}}"
requires_confirmation: {{true|false}}
scope: "{{nucleus|global|agent}}"
target_agent: "{{agent_or_nucleus_slug_or_omit}}"
mcp_server: "{{mcp_server_name_or_omit}}"
tools:
  - name: "{{tool_name_snake_case}}"
    description: "{{one_line_purpose_max_80_chars}}"
    confirmation: "{{auto|confirm|deny}}"
    mcp_endpoint: "{{/path/to/endpoint_or_omit}}"
    denied_for: [{{agent_slugs_or_omit}}]
    risk_level: "{{read|write|delete|dangerous_or_omit}}"
  - name: "{{tool_name_2}}"
    description: "{{one_line_purpose}}"
    confirmation: "{{auto|confirm|deny}}"
deny_list:
  - tool: "{{tool_name}}"
    denied_for: [{{agent_slugs}}]
    reason: "{{justification_for_denial_or_omit}}"
review_date: "{{ISO_8601_date_or_omit}}"
```
## Derivation Notes
1. The four top-level fields (name, tools, category, requires_confirmation) are required
2. Each tool MUST have name, description, and confirmation
3. `mcp_endpoint`, `denied_for`, `risk_level` are per-tool optional fields
4. `scope`, `target_agent`, `mcp_server`, `deny_list`, `review_date` are top-level optional
5. Omit absent optional fields instead of filling with placeholder strings
6. Read tools: confirmation = auto. Write tools: confirmation = confirm. Dangerous: deny.
7. Maximum 15 tools per toolkit — split by category if more are needed

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | toolkit construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_toolkit]] | downstream | 0.56 |
| [[bld_schema_toolkit]] | downstream | 0.54 |
| [[p03_ins_toolkit_builder]] | upstream | 0.54 |
| [[bld_knowledge_card_toolkit]] | upstream | 0.54 |
| [[bld_config_toolkit]] | downstream | 0.49 |
| [[p03_sp_toolkit_builder]] | upstream | 0.49 |
| [[bld_tools_toolkit]] | upstream | 0.42 |
| [[p01_kc_toolkit]] | upstream | 0.42 |
| [[toolkit-builder]] | upstream | 0.42 |
| [[p11_qg_toolkit]] | downstream | 0.39 |
