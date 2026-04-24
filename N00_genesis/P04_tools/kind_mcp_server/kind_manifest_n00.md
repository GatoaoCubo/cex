---
id: n00_mcp_server_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "MCP Server -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, mcp_server, p04, n00, archetype, template]
density_score: 0.98
related:
  - bld_schema_mcp_server
  - bld_collaboration_mcp_server
  - mcp-server-builder
  - p01_kc_mcp_server
  - p03_ins_mcp_server
  - bld_memory_mcp_server
  - bld_architecture_mcp_server
  - p11_qg_mcp_server
  - bld_examples_mcp_server
  - n01_atom_02_mcp_protocol
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An mcp_server is a Model Context Protocol server that exposes tools and resources to LLM clients, enabling any compliant model to call capabilities defined in the server without bespoke integration. It implements the MCP transport (stdio or HTTP+SSE), tool registration, resource serving, and authentication. The output is a deployable MCP server that Claude, GPT, and other MCP-compatible clients can connect to via .mcp.json configuration.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `mcp_server` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| transport | string | yes | stdio or http_sse |
| tools | list | yes | List of tool names exposed by this server |
| resources | list | no | List of resource URIs exposed by this server |
| auth_scheme | string | no | none, api_key, or oauth2 |

## When to use
- When building a CEX capability that must be accessible to multiple LLM clients via MCP
- When packaging nucleus tools (search, memory, compile) for cross-runtime agent access
- When deploying a shared tool server for the CEX grid that all nuclei can call

## Builder
`archetypes/builders/mcp_server-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind mcp_server --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: mcp_cex_knowledge_server
kind: mcp_server
pillar: P04
nucleus: n04
title: "CEX Knowledge MCP Server"
version: 1.0
quality: null
---
transport: stdio
tools: [search_knowledge, get_kind_info, list_builders]
resources: ["cex://kinds_meta", "cex://pillar_schemas"]
auth_scheme: none
```

## Related kinds
- `function_def` (P04) -- tool definitions registered with this mcp_server
- `mcp_app_extension` (P04) -- higher-level app wrapper that uses mcp_server as transport
- `toolkit` (P04) -- tool collection that the mcp_server exposes as a bundle
- `agent_name_service_record` (P04) -- ANS record pointing to this mcp_server endpoint

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_mcp_server]] | downstream | 0.51 |
| [[bld_collaboration_mcp_server]] | related | 0.47 |
| [[mcp-server-builder]] | related | 0.46 |
| [[p01_kc_mcp_server]] | sibling | 0.46 |
| [[p03_ins_mcp_server]] | upstream | 0.45 |
| [[bld_memory_mcp_server]] | downstream | 0.41 |
| [[bld_architecture_mcp_server]] | downstream | 0.41 |
| [[p11_qg_mcp_server]] | downstream | 0.38 |
| [[bld_examples_mcp_server]] | downstream | 0.38 |
| [[n01_atom_02_mcp_protocol]] | sibling | 0.37 |
