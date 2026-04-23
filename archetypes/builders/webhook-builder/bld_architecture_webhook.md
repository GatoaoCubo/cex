---
kind: architecture
id: bld_architecture_webhook
pillar: P04
llm_function: CONSTRAIN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [architecture, webhook, P04, components, boundary, event-driven]
tldr: "Webhook runtime components, data flow (inbound and outbound), and boundary with api_client/notifier/mcp_server."
density_score: 1.0
title: Architecture ISO - webhook
related:
  - webhook-builder
  - p01_kc_webhook
  - bld_knowledge_card_webhook
  - p03_sp_webhook_builder
  - bld_collaboration_webhook
  - bld_output_template_webhook
  - bld_instruction_webhook
  - bld_memory_webhook
  - p11_qg_webhook
  - p04_webhook_NAME
---
# Architecture: webhook

## Runtime Components

```
INBOUND FLOW:
  event_source
    -> [HTTP POST] -> endpoint (URL)
    -> signature_verifier (HMAC-SHA256 on raw_body)
    -> payload_parser (JSON decode after verify)
    -> event_router (dispatch by event_type)
    -> [handler_A | handler_B | handler_C]
    -> [2xx response within timeout_ms]
    -> idempotency_store (mark event_id as processed)

OUTBOUND FLOW:
  internal_event
    -> event_router (maps internal event to external webhook)
    -> payload_builder (construct JSON per target schema)
    -> signature_builder (sign payload with secret)
    -> retry_engine (HTTP POST with backoff)
    -> [2xx from target] OR [dead_letter after max_attempts]
```

## Component Responsibilities

| Component | Responsibility |
|-----------|---------------|
| endpoint | Receives HTTP POST, validates content-type |
| signature_verifier | HMAC-SHA256(secret, raw_body) vs header — reject if mismatch |
| payload_parser | JSON decode only after signature verified |
| event_router | Dispatches to correct handler by event_type string |
| idempotency_store | Cache of processed event IDs (TTL = retry_window + buffer) |
| retry_engine | Exponential backoff, tracks attempt count, emits to dead_letter |
| dead_letter | Persistent log of failed deliveries for manual replay |

## Boundary: What IS a webhook

- HTTP POST triggered by an external or internal event
- Stateless — no persistent connection between events
- Direction is always defined: inbound XOR outbound
- Event type identifies what happened, not what to do
- Payload carries event data, not instructions

## Boundary: What is NOT a webhook

| Pattern | Correct kind | Why different |
|---------|-------------|---------------|
| `GET /orders?id=123` | api_client | Request-response, caller-initiated |
| Send email on signup | notifier | Push delivery to end-user channel |
| MCP tool server | mcp_server | Protocol server, persistent session |
| Background job runner | daemon | Persistent process, not HTTP event |
| REST API endpoint | api_client | Synchronous, not event-driven |

## Scalability Notes

- Webhook receivers should respond 2xx immediately and process async
- High-volume providers (Stripe, GitHub) can burst — queue inbound events
- Signature verification is cheap (< 1ms) — never skip for throughput
- Idempotency store TTL: max(provider_retry_window) + 24h buffer

## Security Surface

- Secret rotation: support dual-secret window during rotation
- Replay attacks: timestamp in signature (Stripe t=, Slack ts=) — reject if > 5min old
- SSRF via outbound webhooks: validate target URL against allowlist
- Payload size limits: reject > 10MB before verification

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[webhook-builder]] | related | 0.53 |
| [[p01_kc_webhook]] | upstream | 0.51 |
| [[bld_knowledge_card_webhook]] | downstream | 0.51 |
| [[p03_sp_webhook_builder]] | related | 0.49 |
| [[bld_collaboration_webhook]] | related | 0.48 |
| [[bld_output_template_webhook]] | related | 0.39 |
| [[bld_instruction_webhook]] | upstream | 0.39 |
| [[bld_memory_webhook]] | downstream | 0.35 |
| [[p11_qg_webhook]] | downstream | 0.34 |
| [[p04_webhook_NAME]] | related | 0.34 |
