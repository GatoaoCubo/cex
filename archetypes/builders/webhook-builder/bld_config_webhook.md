---
kind: config
id: bld_config_webhook
pillar: P04
llm_function: CONSTRAIN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [config, webhook, P04, naming, constraints, enums]
tldr: "Runtime config: naming convention, size limit, direction enum, signature enum, event naming patterns per provider."
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
density_score: 1.0
title: Config ISO - webhook
related:
  - bld_examples_webhook
  - bld_instruction_webhook
  - webhook-builder
  - bld_knowledge_card_webhook
  - bld_output_template_webhook
  - p11_qg_webhook
  - p03_sp_webhook_builder
  - p01_kc_webhook
  - bld_memory_webhook
  - bld_collaboration_webhook
---
# Config: webhook
## Naming Convention
```
filename : p04_webhook_{event_slug}.md
id       : p04_webhook_{event_slug}
```
### Event Slug Rules
- Lowercase only, underscores for separators (no hyphens, no dots)
- Reflects the primary event_type, max 40 characters
### Slug Derivation Examples
| event_type | slug | id |
|-----------|------|----|
| payment_intent.succeeded | payment_completed | p04_webhook_payment_completed |
| push | push | p04_webhook_push |
| message.received | message_received | p04_webhook_message_received |
| costmer.subscription.deleted | subscription_deleted | p04_webhook_subscription_deleted |
| inbound_email | inbound_email | p04_webhook_inbound_email |
## Size Constraint
```
max_bytes : 1024  (body only, frontmatter excluded)
```
Measure with: `len(body.encode("utf-8"))`. If over: compress Overview (1 sentence), inline minimal payload.
## Direction Enum
```yaml
direction:
  - inbound   # external system calls your endpoint
  - outbound  # your system calls external endpoint
```
No aliases: "receive", "send", "incoming", "outgoing" all fail H06.
## Signature Method Enum
```yaml
signature_method:
  - hmac_sha256   # recommended default
  - hmac_sha1     # legacy (Twilio)
  - rsa_sha256    # SendGrid
  - none          # only for internal/trusted-network outbound
```
`none` on inbound always fails S11 (security gate).
## Provider Event Naming Patterns
| Provider | Pattern | Examples |
|----------|---------|---------|
| Stripe | `object.action` | `payment_intent.succeeded`, `costmer.created` |
| GitHub | `event_name` | `push`, `pull_request`, `issues` |
| Slack | `event_type` | `message`, `app_mention`, `reaction_added` |
| Twilio | `EventType` | `com.twilio.messaging.inbound-message` |
| SendGrid | `event` | `delivered`, `open`, `bounce`, `click` |
| Custom | `domain.action` | `order.fulfilled`, `user.signup` |
## Retry Policy Defaults
```yaml
retry_policy:
  max_attempts: 3
  backoff: exponential
  backoff_base_ms: 1000
```
Provider-managed (Stripe, GitHub): match provider window. Self-managed: 3-5 attempts, 5min cap.
## Timeout Defaults
```yaml
timeout_ms: 30000   # 30s standard
```
Stripe: 30s. GitHub: 10s. Slack: 3s (Events API). Use provider minimum when known.
## Tags Requirement
Must include: `"webhook"` (kind), event slug or domain (e.g., `"stripe"`), `"P04"` (pillar).
## Payload Schema
JSON Schema (type:object, required+properties). Include: event_id, event_type, data payload. `idempotency_key` mandatory for inbound (Stripe: `data.object.id`, GitHub: `delivery.id`).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_webhook]] | related | 0.46 |
| [[bld_instruction_webhook]] | upstream | 0.44 |
| [[webhook-builder]] | related | 0.38 |
| [[bld_knowledge_card_webhook]] | downstream | 0.37 |
| [[bld_output_template_webhook]] | related | 0.35 |
| [[p11_qg_webhook]] | downstream | 0.35 |
| [[p03_sp_webhook_builder]] | related | 0.33 |
| [[p01_kc_webhook]] | upstream | 0.32 |
| [[bld_memory_webhook]] | downstream | 0.32 |
| [[bld_collaboration_webhook]] | related | 0.32 |
