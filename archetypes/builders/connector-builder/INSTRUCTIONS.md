---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for connector
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a connector

## Phase 1: RESEARCH
1. Identify the target service name and integration domain (payment, CRM, messaging, etc.)
2. Determine protocol: rest, websocket, grpc, or mqtt
3. List every endpoint with direction annotation (inbound, outbound, or both)
4. Determine auth strategy: none, api_key, oauth, bearer, or hmac
5. Identify data mapping requirements between external schema and CEX schema
6. Determine health_check strategy (endpoint polling, heartbeat, event-based)
7. Check for existing connector artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm service slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set protocol to one of: rest, websocket, grpc, mqtt
5. Write endpoints list with names matching ## Endpoints body section
6. Write ## Overview: 1-2 sentences on service, integration pattern, data flow
7. Write ## Endpoints: for each, define direction, method/topic, path, data shape
8. Write ## Data Mapping: inbound and outbound transform rules, idempotency
9. Write ## Health & Errors: health check, error codes, retry, circuit breaker
10. Verify body <= 1024 bytes
11. Verify id matches `^p04_conn_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm endpoints list matches endpoint names in ## Endpoints section (zero drift)
4. Confirm quality == null
5. Confirm body has all 4 required sections
6. Confirm each endpoint has direction annotation (inbound/outbound)
7. Confirm body <= 1024 bytes
8. Score SOFT gates against QUALITY_GATES.md
9. Revise if score < 8.0 before outputting
