---
kind: config
id: bld_config_webhook
pillar: P04
llm_function: CONSTRAIN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: EDISON
quality: null
tags: [config, webhook, P04, naming, constraints, enums]
tldr: "Runtime config: naming convention, size limit, direction enum, signature enum, event naming patterns per provider."
---
# Config: webhook

## Naming Convention

```
filename : p04_webhook_{event_slug}.md
id       : p04_webhook_{event_slug}
```

### Event Slug Rules

- Lowercase only
- Underscores for separators (no hyphens, no dots)
- Reflects the primary event_type
- Max 40 characters

### Slug Derivation Examples

| event_type | slug | id |
|-----------|------|----|
| payment_intent.succeeded | payment_completed | p04_webhook_payment_completed |
| push | push | p04_webhook_push |
| message.received | message_received | p04_webhook_message_received |
| customer.subscription.deleted | subscription_deleted | p04_webhook_subscription_deleted |
| inbound_email | inbound_email | p04_webhook_inbound_email |

## Size Constraint

```
max_bytes : 1024  (body only, frontmatter excluded)
```

Measure with: `len(body.encode("utf-8"))`
If over limit: compress Overview (1 sentence), inline minimal payload examples.

## Direction Enum

```yaml
direction:
  - inbound   # external system calls your endpoint
  - outbound  # your system calls external endpoint
```

No aliases accepted: "receive", "send", "incoming", "outgoing" all fail H06.

## Signature Method Enum

```yaml
signature_method:
  - hmac_sha256   # recommended default
  - hmac_sha1     # legacy (Twilio)
  - rsa_sha256    # SendGrid
  - none          # only for internal/trusted-network outbound
```

`none` on an inbound webhook always fails S11 (security gate).

## Provider Event Naming Patterns

| Provider | Pattern | Examples |
|----------|---------|---------|
| Stripe | `object.action` | `payment_intent.succeeded`, `customer.created` |
| GitHub | `event_name` | `push`, `pull_request`, `issues` |
| Slack | `event_type` | `message`, `app_mention`, `reaction_added` |
| Twilio | `EventType` | `com.twilio.messaging.inbound-message` |
| SendGrid | `event` | `delivered`, `open`, `bounce`, `click` |
| Custom | `domain.action` | `order.fulfilled`, `user.signup` |

## Retry Policy Defaults

```yaml
retry_policy:
  max_attempts: 3       # minimum acceptable
  backoff: exponential
  backoff_base_ms: 1000
```

Provider-managed (Stripe, GitHub): set max_attempts to match provider window.
Self-managed outbound: 3-5 attempts, cap at 5min total wait.

## Timeout Defaults

```yaml
timeout_ms: 30000   # 30s — standard for most providers
```

Stripe: 30s. GitHub: 10s. Slack: 3s (Events API). Use provider minimum when known.

## Tags Requirement

Must include at minimum:
- `"webhook"` (kind tag)
- event slug or domain (e.g., `"payment_completed"`, `"stripe"`)
- `"P04"` (pillar tag)
