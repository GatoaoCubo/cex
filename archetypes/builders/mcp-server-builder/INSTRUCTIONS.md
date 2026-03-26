---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for mcp_server
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a mcp_server

## Phase 1: RESEARCH
1. Identify the server name and primary domain (search, scrape, deploy, filesystem, etc.)
2. Determine transport type: stdio (local) or SSE/HTTP (remote)
3. List every tool the server exposes (concrete names, not categories)
4. List every resource URI template the server exposes
5. Determine auth strategy based on transport (none for stdio, api_key/oauth for remote)
6. Check for existing mcp_server artifacts via brain_query [IF MCP] (avoid duplicates)
7. Identify rate_limit and health_check requirements (if any)
8. Confirm server slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set transport to one of: stdio, sse, http
5. Write tools_provided list with exact tool names matching ## Tools body section
6. Write resources_provided list with URI templates matching ## Resources body section
7. Write ## Overview: 1-2 sentences on what server does and who consumes it
8. Write ## Tools: for each tool, define name, description, parameters, return type
9. Write ## Resources: for each URI template, define content-type and description
10. Write ## Transport & Auth: connection details and auth config
11. Verify body <= 2048 bytes
12. Verify id matches `^p04_mcp_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm tools_provided list matches tool names in ## Tools section (zero drift)
4. Confirm resources_provided list matches URI templates in ## Resources section
5. Confirm quality == null
6. Confirm body has all 4 required sections
7. Confirm body <= 2048 bytes
8. Score SOFT gates against QUALITY_GATES.md
9. Revise if score < 8.0 before outputting
