---
kind: memory
id: bld_memory_webhook
pillar: P06
llm_function: INJECT
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [memory, webhook, P06, learning, patterns, anti-patterns]
tldr: "Learned patterns from webhook artifact production: security invariants, delivery guarantees, idempotency discipline."
memory_scope: project
observation_types: [user, feedback, project, reference]
density_score: 0.98
title: Memory ISO - webhook
related:
  - webhook-builder
  - p03_sp_webhook_builder
  - p01_kc_webhook
  - bld_collaboration_webhook
  - bld_knowledge_card_webhook
  - bld_examples_webhook
  - bld_instruction_webhook
  - bld_architecture_webhook
  - bld_schema_webhook
  - p11_qg_webhook
---
# Memory: webhook-builder
## Critical Invariants (learned from failures)
### INV-01: Verify before parse
**Pattern**: Signature verification must happen on raw_body before JSON decode.
**Why it matters**: If you parse JSON first, an attacker can send a valid-looking payload with a forged structure. The verification window is the raw bytes, not the parsed object.
**Learned from**: Multiple inbound webhook security reviews where handlers called `json.loads(body)` before `verify_signature(body, header)`.
### INV-02: Idempotency is not optional
**Pattern**: Every inbound webhook must identify and store an idempotency key.
**Why it matters**: Providers retry on timeout or 5xx. Without dedup, the same payment.completed can trigger double fulfillment, double email, double charge.
**Learned from**: Stripe retry storms during 5xx outages — 48h of retries, each causing duplicate order creation.
### INV-03: Outbound without retry is fire-and-forget (unacceptable)
**Pattern**: All outbound webhooks must define retry_policy with max_attempts > 0.
**Why it matters**: Target systems go down, network blips happen, TLS handshakes fail. Without retry, events are silently lost.
**Learned from**: Order fulfillment webhooks to logistics partners — 0.3% drop rate without retry caused ~1200 lost shipment events per month at scale.
### INV-04: Respond fast, process async
**Pattern**: Webhook receiver should return 2xx within timeout_ms, queue processing.
**Why it matters**: Slow handlers trigger provider retries. GitHub times out at 10s. Slack at 3s. Synchronous DB writes inside handler = retry storm.
**Learned from**: Slack Events API handler doing synchronous Postgres inserts — exceeded 3s, received 50+ duplicate events per original event.
## Scoring Patterns
| Condition | Typical soft_score |
|-----------|-------------------|
| Full provider artifact (Stripe/GitHub) with all REC fields | 8.5-9.5 |
| Custom webhook with all required + signature + retry | 7.5-8.5 |
| Missing signature_method on inbound | 4.0-5.0 (S11 fails) |
| Missing retry_policy on outbound | 5.0-6.0 (S04 fails) |
| No idempotency_key | 6.0-7.0 (S05 fails) |
## Disambiguation Log
Requests that required clarification before production:
| Ambiguous request | Question asked | Resolution |
|------------------|----------------|------------|
| "webhook for orders" | Inbound (receive) or outbound (send)? | Clarify system role |
| "GitHub webhook" | Which events? push only or all? | List required events |
| "payment webhook" | Provider? Stripe, PayPal, costm? | Determines signature method |
| "notification webhook" | Is this notifier or webhook? | Check if end-user receives it |
## Known Provider Quirks
- **Stripe**: timestamp in signature (`t=` prefix) — must validate timestamp within 300s
- **GitHub**: sends `X-GitHub-Event` header separately from payload — use for routing
- **Slack**: URL verification challenge on first registration — respond with challenge value
- **Twilio**: signs with account SID + auth token — not a simple shared secret
- **SendGrid**: ECDSA-SHA256 (not HMAC) — requires public key from SendGrid dashboard

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[webhook-builder]] | upstream | 0.51 |
| [[p03_sp_webhook_builder]] | upstream | 0.48 |
| [[p01_kc_webhook]] | upstream | 0.44 |
| [[bld_collaboration_webhook]] | upstream | 0.43 |
| [[bld_knowledge_card_webhook]] | related | 0.43 |
| [[bld_examples_webhook]] | upstream | 0.40 |
| [[bld_instruction_webhook]] | upstream | 0.39 |
| [[bld_architecture_webhook]] | upstream | 0.38 |
| [[bld_schema_webhook]] | related | 0.35 |
| [[p11_qg_webhook]] | downstream | 0.34 |
