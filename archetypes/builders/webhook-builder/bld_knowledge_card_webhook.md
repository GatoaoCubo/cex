---
id: bld_knowledge_card_webhook
kind: knowledge_card
pillar: P06
llm_function: INJECT
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: webhook
quality: 9.1
tags: [knowledge_card, webhook, HMAC, signature, retry, idempotency, stripe, github, slack]
tldr: "Domain knowledge: webhook patterns, HMAC-SHA256 verification, retry/backoff, idempotency, provider specifics (Stripe/GitHub/Slack/Twilio)."
density_score: 1.0
title: Knowledge Card ISO - webhook
---
# Knowledge Card: webhook
## Core Concept
A webhook is an HTTP POST callback triggered by an event. Direction:
- **Inbound**: external system calls YOUR endpoint when event occurs
- **Outbound**: YOUR system calls external endpoint when YOUR event occurs
Webhooks are stateless — they do not maintain connections between events.
## Provider Patterns
| Provider | Signature Header | Method | Event Header |
|----------|-----------------|--------|--------------|
| Stripe | `Stripe-Signature` | HMAC-SHA256 (t= + v1=) | - |
| GitHub | `X-Hub-Signature-256` | HMAC-SHA256 | `X-GitHub-Event` |
| Slack | `X-Slack-Signature` | HMAC-SHA256 (v0=) | - |
| Twilio | `X-Twilio-Signature` | HMAC-SHA1 | - |
| SendGrid | `X-Twilio-Email-Event-Webhook-Signature` | ECDSA-SHA256 | - |
| Custom | configurable | HMAC-SHA256 recommended | configurable |
## HMAC-SHA256 Verification Pattern
```
signature = HMAC-SHA256(secret_key, raw_request_body)
provided  = extract from signature_header (strip prefix: "sha256=", "v1=", "v0=")
valid     = constant_time_compare(signature, provided)
```
CRITICAL: verify raw_body BEFORE JSON decode. Parsing before verification allows payload manipulation attacks.
## Retry & Backoff
Standard exponential backoff: `wait = base_ms * (2 ^ attempt_number)`
Example (base=1000ms): 1s, 2s, 4s, 8s, 16s — cap at 5 attempts for most cases.
Stripe retries up to 3 days. GitHub retries for ~72h. Design receivers to be fast (respond 2xx in <3s) and idempotent.
## Idempotency
Always identify the dedup key — usually a unique event ID in the payload:
- Stripe: `data.object.id` or top-level `id`
- GitHub: `X-GitHub-Delivery` header (UUID per delivery)
- Slack: `event.event_id`
- Custom: `event_id`, `request_id`, or `idempotency_key`
Store processed IDs in a short-lived cache (TTL = retry window + buffer).
## Dead-Letter Pattern
After max_attempts exhausted: log full payload + error, emit to dead-letter queue or table, alert on-call if queue depth > threshold, ensure manual replay path exists.
## Patterns (use these)
- Respond 2xx immediately, process async — prevents timeout-triggered retries
- Verify signature first, parse second — security invariant
- Store raw payload before processing — enables replay
- Use event_type routing table — one endpoint, many handlers
- Version your payload schema — breaking changes need migration window
## Anti-Patterns (avoid)
- Unsigned inbound webhooks — payload spoofing risk
- Synchronous heavy processing in handler — causes timeout + infinite retries
- Ignoring duplicate delivery — idempotency is not optional
- Hardcoded secrets — use env vars or secret manager
- HTTP (not HTTPS) for outbound — plaintext payload exposure
## Boundary Clarity
| Pattern | Builder |
|---------|---------|
| Event-driven HTTP push | webhook-builder (this) |
| Synchronous request-response | api-client-builder |
| Push notification (email/SMS/Slack msg) | notifier-builder |
| MCP protocol server | mcp-server-builder |
| Persistent background process | daemon-builder |
