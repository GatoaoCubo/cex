---
kind: schema
id: bld_schema_webhook
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for webhook
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [schema, webhook, P04, P06, constraint]
quality: 9.1
title: "Schema Webhook"
tldr: "Golden and anti-examples for webhook construction, demonstrating ideal structure and common pitfalls."
domain: "webhook construction"
density_score: 0.90
related:
  - bld_schema_handoff_protocol
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_client
  - bld_schema_chunk_strategy
  - bld_schema_constraint_spec
  - bld_schema_smoke_eval
  - bld_schema_unit_eval
  - bld_schema_prompt_version
---
# Schema: webhook

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | YES | - | Must match `p04_webhook_{event_slug}` |
| kind | literal "webhook" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable webhook name |
| direction | enum: inbound, outbound | YES | - | Receive or send events |
| event_type | string | YES | - | Primary event (e.g., "payment.completed") |
| event_types | list[string] | REC | - | All event types handled |
| payload_schema | object (JSON Schema) | YES | - | Expected/produced payload |
| signature_method | enum: hmac_sha256, hmac_sha1, rsa_sha256, none | REC | hmac_sha256 | Verification method |
| signature_header | string | REC | - | Header with signature (e.g., "X-Hub-Signature-256") |
| retry_policy | object {max_attempts, backoff} | REC | - | Retry configuration |
| idempotency_key | string | REC | - | Field used for dedup |
| timeout_ms | int | REC | 30000 | Response timeout |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "webhook" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the webhook does |

## ID Pattern

Regex: `^p04_webhook_[a-z][a-z0-9_]+$`
Examples: `p04_webhook_payment_completed`, `p04_webhook_push`, `p04_webhook_message_received`

## Body Structure

1. `## Overview` — direction, events handled, use case context
2. `## Events` — each event type: trigger condition, payload example
3. `## Verification` — signature method, header name, secret management
4. `## Retry & Delivery` — retry policy, timeout, idempotency, failure handling

## Constraints

- max_bytes: 1024 (body only — compact webhook spec)
- naming: `p04_webhook_{event_slug}.md` (single file per webhook)
- machine_format: json (compiled artifact)
- id must equal filename stem exactly
- quality: null always — never self-score
- NO implementation code in body
- NO server/daemon lifecycle — webhooks are stateless endpoints

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_handoff_protocol]] | sibling | 0.67 |
| [[bld_schema_retriever_config]] | sibling | 0.66 |
| [[bld_schema_output_validator]] | sibling | 0.65 |
| [[bld_schema_memory_scope]] | sibling | 0.65 |
| [[bld_schema_client]] | sibling | 0.64 |
| [[bld_schema_chunk_strategy]] | sibling | 0.64 |
| [[bld_schema_constraint_spec]] | sibling | 0.63 |
| [[bld_schema_smoke_eval]] | sibling | 0.63 |
| [[bld_schema_unit_eval]] | sibling | 0.62 |
| [[bld_schema_prompt_version]] | sibling | 0.62 |
