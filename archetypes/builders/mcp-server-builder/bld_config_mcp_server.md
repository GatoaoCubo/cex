---
kind: config
id: bld_config_mcp_server
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: mcp_server Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_mcp_{server_slug}.md` + `.yaml` | `p04_mcp_document_search.md` |
| Builder directory | kebab-case | `mcp-server-builder/` |
| Frontmatter fields | snake_case | `tools_provided`, `resources_provided` |
| Server slug | snake_case, lowercase, no hyphens | `brain_search`, `file_system` |
| Tool names | snake_case, verb_noun pattern | `search_documents`, `read_file` |
| Resource URIs | `scheme://{path_template}` | `file://{path}`, `db://{table}/{id}` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `cex/P04_tools/examples/p04_mcp_{server_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_mcp_{server_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes (stricter than most P04 kinds)
- Total (frontmatter + body): ~3000 bytes
- Density: >= 0.80 (no filler)

## Transport Enum

| Value | Where runs | Auth pairing |
|-------|-----------|--------------|
| stdio | Local subprocess | none only |
| sse | Remote HTTP (server-sent events) | api_key or oauth |
| http | Remote HTTP (streamable) | api_key or bearer |

## Auth Enum

| Value | When to use |
|-------|-------------|
| none | stdio transport only — process-level trust |
| api_key | SSE/HTTP — static key in Authorization header |
| oauth | SSE/HTTP — OAuth 2.0 flow for user-delegated access |
| bearer | HTTP — JWT or token in Authorization: Bearer header |

## Body Requirements
- Overview: 1-2 sentences; name the consumer agent type
- Tools: each tool needs name, description, parameters, return type
- Resources: each resource needs URI template, content-type, description
- Transport & Auth: connection command/endpoint + auth config
- tools_provided list MUST match tool names in ## Tools (zero drift)
- resources_provided MUST match URI templates in ## Resources (zero drift)
