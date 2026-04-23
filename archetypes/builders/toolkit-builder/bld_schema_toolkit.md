---
kind: schema
id: bld_schema_toolkit
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for toolkit - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Toolkit"
version: "1.0.0"
author: n03_builder
tags: [toolkit, builder, examples]
tldr: "Golden and anti-examples for toolkit construction, demonstrating ideal structure and common pitfalls."
domain: "toolkit construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_toolkit_builder
  - bld_knowledge_card_toolkit
  - p03_sp_toolkit_builder
  - bld_config_toolkit
  - toolkit-builder
  - bld_output_template_toolkit
  - p11_qg_toolkit
  - bld_collaboration_toolkit
  - bld_architecture_toolkit
  - bld_memory_toolkit
---

# Schema: toolkit
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P04` |
| Type | literal `toolkit` |
| Machine format | `yaml` |
| Naming | `p04_tk_{name}.yaml` |
| Max bytes | 4096 |
## Required Top-Level Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| name | string, non-empty, snake_case | YES | - | toolkit identifier matching the domain |
| tools | list[tool_object], non-empty, 1-15 entries | YES | - | ordered list of tool definitions |
| category | enum (file_ops, git_ops, search, web, system, build, analysis) | YES | - | domain grouping for the toolkit |
| requires_confirmation | boolean | YES | - | global default: true if any write tool present |
## Tool Object Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| name | string, non-empty, snake_case | YES | - | tool identifier |
| description | string, non-empty, max 80 chars | YES | - | one-line purpose statement |
| confirmation | enum (auto, confirm, deny) | YES | - | permission tier for this tool |
| mcp_endpoint | string | NO | omitted | MCP server path if tool is remote |
| denied_for | list[string] | NO | omitted | agents/nuclei denied this tool |
| risk_level | enum (read, write, delete, dangerous) | NO | omitted | operation risk classification |
## Optional Top-Level Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| scope | enum (nucleus, global, agent) | NO | nucleus | permission scope level |
| target_agent | string | NO | omitted | specific agent this toolkit is for |
| version | string, semver | NO | 1.0.0 | toolkit version for compatibility tracking |
| deny_list | list[deny_object] | NO | omitted | global deny entries (supplement per-tool denied_for) |
| mcp_server | string | NO | omitted | default MCP server for all tools in this toolkit |
| review_date | string, ISO 8601 date | NO | omitted | next scheduled least-privilege review |
## Deny Object Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| tool | string, non-empty | YES | - | tool name being denied |
| denied_for | list[string], non-empty | YES | - | agents/nuclei denied |
| reason | string, non-empty | YES | - | justification for denial |
## Semantic Rules
1. One toolkit covers one domain (file_ops, git_ops, etc.) for one scope level
2. Maximum 15 tools per toolkit — complexity beyond 15 indicates domain split needed
3. Read-only tools default to `confirmation: auto` — no friction for safe operations
4. Write/modify tools MUST have `confirmation: confirm` — prevent unintended state changes
5. Destructive tools default to `confirmation: deny` unless explicitly justified
6. Deny lists override allow lists — a denied tool cannot be used regardless of other settings
7. Each tool appears in exactly one toolkit — no cross-toolkit duplication
8. Toolkits are versioned — changes require version bump and review
## Boundary Rules
`toolkit` IS:
- permission bundle for agent tool access
- confirmation tier assignments per tool
- deny list for explicit restrictions
- MCP endpoint mapping for remote execution
`toolkit` IS NOT:
- `tool_implementation`: no function code, no class definitions, no scripts
- `system_prompt`: no agent identity, no persona, no behavioral rules
- `workflow_primitive`: no step graphs, no conditions, no loops
- `dispatch_rule`: no routing policy, no keyword matching, no agent selection
## Canonical Minimal Example
```yaml
name: file_ops
category: file_ops
requires_confirmation: true
tools:
  - name: read_file
    description: Read file contents from disk
    confirmation: auto
  - name: write_file
    description: Write content to a file on disk
    confirmation: confirm
  - name: glob_search
    description: Search for files matching a glob pattern
    confirmation: auto
  - name: delete_file
    description: Delete a file from disk permanently
    confirmation: deny
    denied_for: [n01, n02, n04]
    risk_level: delete
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_toolkit_builder]] | upstream | 0.58 |
| [[bld_knowledge_card_toolkit]] | upstream | 0.55 |
| [[p03_sp_toolkit_builder]] | upstream | 0.54 |
| [[bld_config_toolkit]] | downstream | 0.50 |
| [[toolkit-builder]] | upstream | 0.49 |
| [[bld_output_template_toolkit]] | upstream | 0.48 |
| [[p11_qg_toolkit]] | downstream | 0.48 |
| [[bld_collaboration_toolkit]] | upstream | 0.46 |
| [[bld_architecture_toolkit]] | downstream | 0.45 |
| [[bld_memory_toolkit]] | downstream | 0.45 |
