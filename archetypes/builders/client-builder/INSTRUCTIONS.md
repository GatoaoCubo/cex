---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for client
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a client

## Phase 1: RESEARCH
1. Identify the external API to consume and its primary domain (payment, search, deploy, etc.)
2. Map every endpoint the client uses: HTTP method, path, query params, and return types
3. Determine auth strategy: none, api_key, oauth, jwt, or basic
4. Define rate limits (requests per second/minute) and retry policy (max retries, backoff)
5. Identify pagination pattern: cursor, offset, page-number, or none
6. Determine serialization format: json, xml, or protobuf
7. Check for existing client artifacts to avoid duplicates
8. Confirm API slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Base Configuration section: base_url, auth strategy, required headers
5. Write Endpoints section: for each endpoint, list method, path, params, return type, and error codes
6. Write Rate Limiting section: request limits per time window, backoff strategy
7. Write Retry Policy section: max retries, backoff formula, list of idempotent methods
8. Write Pagination section: pattern name (cursor/offset/page) with field names
9. Write Error Handling section: HTTP status code mapping to client behavior
10. Verify body <= 1024 bytes
11. Verify id matches `^p04_cl_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_cl_`
4. Confirm kind == client
5. Confirm base_url is defined
6. Confirm auth strategy is specified
7. Confirm at least 1 endpoint is mapped with method, path, and return type
8. HARD gates: frontmatter valid, id pattern matches, base_url defined, auth specified, endpoint present
9. SOFT gates: score against QUALITY_GATES.md
10. Cross-check: unidirectional only (consumes, does not receive)? Not bidirectional (connector)? Not an MCP protocol provider (mcp_server)? Not HTML extraction (scraper)?
11. Revise if score < 8.0 before outputting
