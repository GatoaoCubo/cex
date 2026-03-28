---
kind: instruction
id: bld_instruction_connector
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for connector
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a connector

## Phase 1: RESEARCH
1. Identify the external service to integrate and its domain (payment, CRM, messaging, etc.)
2. Determine protocol: rest, websocket, grpc, or mqtt
3. Map bidirectional endpoints: list inbound endpoints (service pushes to us) and outbound endpoints (we push to service) separately
4. Determine auth strategy: none, api_key, oauth, bearer, or hmac
5. Assess data transform requirements: field name differences, type conversions, format translations between external schema and local schema
6. Define health check mechanism: endpoint polling, heartbeat, or event-based liveness
7. Check for existing connector artifacts to avoid duplicates
8. Confirm service slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Service Configuration section: service name, protocol, auth strategy, base_url
5. Write Endpoints section: for each endpoint list direction (inbound/outbound), path or topic, and data transform reference
6. Write Data Transforms section: mapping rules, field conversions, format translations for both directions
7. Write Health Check section: endpoint or mechanism, check interval, expected response
8. Write Retry and Rate Limiting section: per-direction policies with max retries and backoff
9. Write Logging section: what to log per direction, sensitivity filtering rules
10. Verify body <= 1024 bytes
11. Verify id matches `^p04_cn_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_cn_`
4. Confirm kind == connector
5. Confirm protocol is specified (rest, websocket, grpc, or mqtt)
6. Confirm both inbound and outbound endpoints are present
7. Confirm health check is defined with interval and expected response
8. HARD gates: frontmatter valid, id pattern matches, protocol specified, both directions present, health check defined
9. SOFT gates: data transform rules are concrete (not vague), score against QUALITY_GATES.md
10. Cross-check: bidirectional flow (not unidirectional client)? Not using MCP protocol (mcp_server)? Transform rules describe actual field mappings (not abstract)?
11. Revise if score < 8.0 before outputting
