---
id: p11_qg_webhook
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
target_kind: webhook
hard_gates: 10
soft_dims: 12
quality: 9.1
tags: [quality_gate, webhook, P11, validation]
tldr: "10 HARD gates (any failure = reject) + 12 SOFT dims (score 0-10, threshold 7.0)"
density_score: 1.0
title: Quality Gate ISO - webhook
---
# Gate: webhook

## HARD Gates (any failure = immediate reject)

| ID | Gate | Check |
|----|------|-------|
| H01 | YAML valid | Frontmatter parses without error |
| H02 | ID pattern | id matches `^p04_webhook_[a-z][a-z0-9_]+$` |
| H03 | Kind correct | kind == "webhook" |
| H04 | Quality null | quality == null (never self-scored) |
| H05 | Required fields | id, name, direction, event_type, payload_schema all present |
| H06 | Direction enum | direction is exactly "inbound" or "outbound" |
| H07 | Event type set | event_type is non-empty string |
| H08 | Payload schema | payload_schema is defined object, not empty `{}` |
| H09 | Size limit | body <= 1024 bytes (exclude frontmatter) |
| H10 | No lifecycle | Body contains no "server", "daemon", "listen forever", "start()" |

## SOFT Scoring (0-10 per dimension, threshold >= 7.0)

| Dim | Name | What earns full score |
|-----|------|-----------------------|
| S01 | Event coverage | All event_types listed with trigger conditions |
| S02 | Payload docs | Each event has payload_schema with field descriptions |
| S03 | Signature verification | Method + header + secret env var documented |
| S04 | Retry policy | max_attempts, backoff strategy, backoff_base_ms present |
| S05 | Idempotency | idempotency_key field identified in payload |
| S06 | Error handling | Dead-letter or failure fallback described |
| S07 | Timeout | timeout_ms explicitly set |
| S08 | Boundary clarity | Clearly NOT api_client / notifier / mcp_server |
| S09 | Domain specificity | Provider named (Stripe/GitHub/Slack/costm), not generic |
| S10 | Testability | Payload examples are valid JSON, realistic values |
| S11 | Security posture | Inbound: signature verified before parse; outbound: HTTPS only |
| S12 | Delivery guarantees | At-least-once or exactly-once semantics stated |

## Scoring Formula

```
soft_score = mean(S01..S12)
pass = all(H01..H10) AND soft_score >= 7.0
```

## Common Failures

- H06: direction = "receive" instead of "inbound" — use enum values only
- H08: payload_schema: {} — must define at minimum `type: object`
- H09: body too long — compress examples, remove prose padding
- S03: inbound webhook with signature_method: none — security gate will flag
- S04: outbound without retry_policy — fire-and-forget is unacceptable
- S11: signature verified after parsing — must verify raw_body before JSON decode
