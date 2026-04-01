---
id: p04_webhook_NAME
kind: webhook
pillar: P04
version: 1.0.0
title: "Template - Webhook"
tags: [template, webhook, callback, http, integration]
tldr: "Defines an HTTP webhook endpoint or callback URL. Configures method, headers, payload schema, retry policy, and signature verification."
quality: 8.7
---

# Webhook: [NAME]

## Purpose
Connects CEX events to external systems via HTTP callbacks (Slack, GitHub, custom APIs).

## Configuration
```yaml
url: "[WEBHOOK_URL]"
method: [POST | PUT]
headers:
  Content-Type: application/json
  Authorization: "Bearer [TOKEN]"
timeout_ms: [5000 | 10000]
retry_count: [0 | 2 | 3]
retry_backoff_ms: [1000 | 2000]
```

## Capabilities

| Event | Payload | When |
|---|---|---|
| build_complete | {kind, id, quality, path} | After F8 |
| gate_failed | {kind, gates, issues} | F7 failure |
| signal_received | {nucleus, status, task} | On signal |
| doctor_alert | {pass, warn, fail} | Doctor finds issues |

## Error Handling
- **Endpoint unreachable**: Queue payload, retry with backoff
- **Auth failed (401)**: Log error, do NOT retry
- **Payload too large**: Truncate to 64KB
- **Timeout**: Retry once, then log as failed delivery

## Quality Gate
- [ ] URL is HTTPS (security)
- [ ] Authentication configured
- [ ] Retry policy defined
- [ ] Payload schema documented
