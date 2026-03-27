---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for client
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a client

## Phase 1: RESEARCH
1. Identify the target API name and primary domain (payment, search, deploy, etc.)
2. Determine base_url for the API (e.g., https://api.stripe.com/v1)
3. List every endpoint the client consumes (concrete method + path pairs)
4. Determine auth strategy: none, api_key, oauth, or bearer
5. Identify rate_limit constraints (requests per unit time)
6. Determine retry policy (max retries, backoff strategy)
7. Check for existing client artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm API slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set auth to one of: none, api_key, oauth, bearer
5. Write endpoints list with exact endpoint names matching ## Endpoints body section
6. Write ## Overview: 1-2 sentences on what API and who consumes it
7. Write ## Endpoints: for each endpoint, define method, path, parameters, return type
8. Write ## Auth & Config: base_url, auth method, required headers
9. Write ## Error Handling: error codes, retry strategy, timeout behavior
10. Verify body <= 1024 bytes
11. Verify id matches `^p04_client_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm endpoints list matches endpoint names in ## Endpoints section (zero drift)
4. Confirm quality == null
5. Confirm body has all 4 required sections
6. Confirm body <= 1024 bytes
7. Score SOFT gates against QUALITY_GATES.md
8. Revise if score < 8.0 before outputting
