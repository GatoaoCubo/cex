---
id: p04_webhook_NAME
kind: webhook
pillar: P04
version: 1.0.0
title: "Template - Webhook"
tags: [template, webhook, callback, http, integration]
tldr: "Defines an HTTP webhook endpoint or callback URL. Configures method, headers, payload schema, retry policy, and signature verification."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
related:
  - webhook-builder
  - p03_sp_webhook_builder
  - bld_output_template_webhook
  - p12_ho_builder_nucleus
  - bld_architecture_webhook
  - bld_knowledge_card_webhook
  - bld_knowledge_card_client
  - p11_qg_webhook
  - bld_config_signal
  - p11_qg_client
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
1. **Endpoint unreachable**: Queue payload, retry with backoff
2. **Auth failed (401)**: Log error, do NOT retry
3. **Payload too large**: Truncate to 64KB
4. **Timeout**: Retry once, then log as failed delivery

## Quality Gate
1. [ ] URL is HTTPS (security)
2. [ ] Authentication configured
3. [ ] Retry policy defined
4. [ ] Payload schema documented

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `webhook` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[webhook-builder]] | related | 0.29 |
| [[p03_sp_webhook_builder]] | related | 0.24 |
| [[bld_output_template_webhook]] | related | 0.24 |
| [[p12_ho_builder_nucleus]] | downstream | 0.24 |
| [[bld_architecture_webhook]] | related | 0.23 |
| [[bld_knowledge_card_webhook]] | downstream | 0.23 |
| [[bld_knowledge_card_client]] | upstream | 0.22 |
| [[p11_qg_webhook]] | downstream | 0.22 |
| [[bld_config_signal]] | downstream | 0.22 |
| [[p11_qg_client]] | downstream | 0.22 |
