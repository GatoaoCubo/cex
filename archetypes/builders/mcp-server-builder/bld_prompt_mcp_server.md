---
id: p03_ins_mcp_server
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: MCP Server Builder Execution Protocol
target: mcp-server-builder agent
phases_count: 4
prerequisites:
  - Server name and primary domain are identified (search, scrape, deploy, filesystem, etc.)
  - Transport type is determinable from the deployment context (local vs remote)
  - At least one tool or resource the server exposes is known
validation_method: checklist
domain: mcp_server
quality: 9.1
tags: [instruction, mcp-server, P04, tools, transport, infrastructure]
idempotent: true
atomic: false
rollback: "Discard generated artifact; no server infrastructure is created or modified"
dependencies: []
logging: true
tldr: Define an MCP server artifact specifying transport type, tools with JSON-Schema parameters, resources with URI templates, and auth strategy.
density_score: 0.90
llm_function: REASON
related:
  - bld_knowledge_card_mcp_server
  - mcp-server-builder
  - p03_sp_mcp_server_builder
  - bld_schema_mcp_server
  - p11_qg_mcp_server
  - bld_memory_mcp_server
  - bld_collaboration_mcp_server
  - bld_config_mcp_server
  - p01_kc_mcp_server
  - n01_atom_02_mcp_protocol
---
## Context
The mcp-server-builder produces `mcp_server` artifacts (P04) — specification documents for Model Context Protocol servers that expose tools and resources for LLM agents to consume. An mcp_server artifact is a definition, not running code; it specifies what a server exposes and how clients connect to it.
MCP servers differ from connectors (bidirectional integrations), clients (API consumers), skills (reusable capability sequences), and daemons (background processes without MCP protocol).
**Inputs:**
- `$server_name (required) - string - "Human-readable server name (e.g. 'firecrawl', 'filesystem', 'railway-deploy')"`
- `$server_slug (required) - string - "snake_case, lowercase, no hyphens — used in id field (e.g. 'firecrawl', 'fs_local')"`
- `$transport (required) - string - "One of: stdio, sse, http"`
- `$tools (required) - list[string] - "Exact tool names the server exposes (e.g. ['search', 'scrape', 'extract'])"`
- `$resources (optional) - list[string] - "URI templates for resources (e.g. ['file://{path}', 'db://{table}/{id}'])"`
- `$auth_strategy (optional) - string - "Auth method: none (stdio), api_key, oauth, jwt — derived from transport if omitted"`
**Output:** A single `mcp_server` artifact, body <= 2048 bytes, with complete frontmatter and 4 required body sections: Overview, Tools, Resources, Transport and Auth.
**Boundary check before proceeding:**
- Bidirectional integration with a third-party service → route to connector-builder
- Reusable multi-step capability sequence → route to skill-builder
- Background process without MCP protocol → document as daemon, not mcp_server
- Server exposing tools via MCP protocol → proceed
## Phases
### Phase 1: Research
**Action:** Gather all parameters needed to fully specify the server.
1. Confirm server `slug`: snake_case, lowercase, no hyphens, unique within P04.
2. Confirm `transport` selection:
   - `stdio` — local process, spawned by client, no network required, auth = none
   - `sse` — remote server-sent events, persistent connection, requires auth
   - `http` — remote HTTP endpoint, stateless request/response, requires auth
3. List every **tool** the server exposes with its exact name (not categories — specific names).
4. For each tool, identify: description, parameters (name + type + required/optional), return type.
5. List every **resource URI template** (e.g. `file://{path}`, `mem://{key}`).
6. For each resource, identify: content-type and description.
7. Determine `auth_strategy`:
   - `stdio` → always `none`
   - `sse` or `http` → one of: `api_key`, `oauth`, `jwt`
8. Identify `rate_limit` (requests per minute) and `health_check` endpoint (if applicable).
9. Check for existing mcp_server artifacts covering the same server to avoid duplicates.
10. Verify slug generates valid id: `p04_mcp_{slug}` must match `^p04_mcp_[a-z][a-z0-9_]+$`.
**Verification:** Every tool has a name, description, and at least one parameter or explicit "no parameters". Transport and auth are consistent.
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections within the 2048-byte body limit.
1. Read `SCHEMA.md` — source of truth for all required fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Fill frontmatter: all required fields (`quality: null` — never self-score).
4. Set `transport`: one of `stdio`, `sse`, `http`.
5. Set `tools_provided`: list of exact tool names — must exactly match tool names in `## Tools`.
6. Set `resources_provided`: list of URI templates — must exactly match templates in `## Resources`.
7. Write `## Overview` — 1-2 sentences: what the server does and who consumes it.
8. Write `## Tools` — for each tool:
   ```
   ### {tool_name}
   {description}
   Parameters: {name: type (required|optional), ...}
   Returns: {return_type}
   ```
9. Write `## Resources` — for each URI template:
   ```
   ### {uri_template}
   Content-Type: {type}
   {description}
   ```
   If no resources: write `## Resources\nNone.`
10. Write `## Transport and Auth` — connection details, auth config, rate limit, health check.
Byte budget pseudocode:
```
body_bytes = len(encode_utf8(body_content))
# if body_bytes > 2048: compress descriptions, remove redundant prose
```
**Verification:** `tools_provided` list in frontmatter exactly matches tool names in `## Tools` body section (zero drift). Body <= 2048 bytes.
### Phase 3: Validate
**Action:** Run all HARD gates from `QUALITY_GATES.md`. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches `^p04_mcp_[a-z][a-z0-9_]+$` |
| H03 | `kind` is literal string `mcp_server` |
| H04 | `quality` is `null` |
| H05 | `transport` is one of: stdio, sse, http |
| H06 | `tools_provided` list exactly matches tool names in `## Tools` section |
| H07 | `resources_provided` matches URI templates in `## Resources` section |
| H08 | All 4 required body sections present |
| H09 | Body <= 2048 bytes |
Score SOFT gates from `QUALITY_GATES.md`. If soft score < 8.0, revise in the same pass.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_mcp_server]] | downstream | 0.51 |
| [[mcp-server-builder]] | downstream | 0.50 |
| [[p03_sp_mcp_server_builder]] | related | 0.50 |
| [[bld_schema_mcp_server]] | downstream | 0.50 |
| [[p11_qg_mcp_server]] | downstream | 0.49 |
| [[bld_memory_mcp_server]] | downstream | 0.48 |
| [[bld_collaboration_mcp_server]] | downstream | 0.48 |
| [[bld_config_mcp_server]] | downstream | 0.46 |
| [[p01_kc_mcp_server]] | upstream | 0.43 |
| [[n01_atom_02_mcp_protocol]] | upstream | 0.43 |
