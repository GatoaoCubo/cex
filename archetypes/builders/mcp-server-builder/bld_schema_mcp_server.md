---
kind: schema
id: bld_schema_mcp_server
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for mcp_server
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Mcp Server"
version: "1.0.0"
author: n03_builder
tags: [mcp_server, builder, examples]
tldr: "Golden and anti-examples for mcp server construction, demonstrating ideal structure and common pitfalls."
domain: "mcp server construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_client
  - bld_schema_retriever_config
  - bld_schema_cli_tool
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_chunk_strategy
  - bld_schema_constraint_spec
  - bld_schema_action_prompt
  - bld_schema_prompt_version
---

# Schema: mcp_server
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_mcp_{server_slug}) | YES | - | Namespace compliance |
| kind | literal "mcp_server" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable server name |
| transport | enum: stdio, sse, http | YES | - | How clients connect |
| tools_provided | list[string], len >= 1 | YES | - | Exact tool names exposed |
| resources_provided | list[string] | YES | [] | URI templates exposed |
| auth | enum: none, api_key, oauth, bearer | REC | none | Auth strategy |
| description | string <= 200ch | REC | - | What the server does |
| health_check | string | REC | - | Endpoint or command |
| rate_limit | string | REC | - | Requests per unit time |
| versioning | string | REC | - | Version negotiation strategy |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "mcp_server" |
| tldr | string <= 160ch | YES | - | Dense summary |
## ID Pattern
Regex: `^p04_mcp_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the server does, use case, who consumes it
2. `## Tools` — each tool: name, description, parameters (JSON-Schema inline)
3. `## Resources` — each resource: URI template, description, content type
4. `## Transport & Auth` — transport config, auth method, connection details
## Constraints
- max_bytes: 2048 (body only — compact infrastructure spec)
- naming: p04_mcp_{server_slug}.md + .yaml (dual file)
- machine_format: json (compiled artifact)
- id == filename stem
- tools_provided list MUST match tool names defined in ## Tools section
- resources_provided list MUST match URI templates in ## Resources section
- quality: null always
- NO implementation code in body — spec only
- transport: stdio = local process; sse/http = remote server

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_client]] | sibling | 0.66 |
| [[bld_schema_retriever_config]] | sibling | 0.66 |
| [[bld_schema_cli_tool]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_handoff_protocol]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.63 |
| [[bld_schema_chunk_strategy]] | sibling | 0.63 |
| [[bld_schema_constraint_spec]] | sibling | 0.63 |
| [[bld_schema_action_prompt]] | sibling | 0.62 |
| [[bld_schema_prompt_version]] | sibling | 0.61 |
