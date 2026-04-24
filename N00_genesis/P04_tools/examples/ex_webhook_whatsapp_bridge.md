---
id: p04_webhook_whatsapp_bridge
kind: webhook
8f: F5_call
name: whatsapp_bridge
protocol: REST
direction: bidirectional
auth: session
pillar: P04
version: 3.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [connector, whatsapp, bridge, messaging]
updated: "2026-04-07"
domain: "tool integration"
title: "Webhook Whatsapp Bridge"
density_score: 0.92
tldr: "Defines webhook for webhook whatsapp bridge, with validation gates and integration points."
related:
  - webhook-builder
  - p04_webhook_NAME
  - db-connector-builder
  - tpl_validation_schema
  - p11_qg_connector
  - bld_knowledge_card_connector
  - p01_kc_webhook
  - skill
  - bld_collaboration_webhook
  - research_then_build
---

# Connector: whatsapp_bridge

## Service Contract
1. Service: WhatsApp via whatsapp-web.js (Node.js, port 3847)
2. Mode: bidirectional (REST send + webhook receive)
3. Auth: QR code first run, LocalAuth session persistence after

## Data Mapping
| External Field | Internal Field | Rule |
|----------------|----------------|------|
| msg.body | text | UTF-8, max 4096 chars |
| msg.hasMedia | audio_path | Download OGG to data/ |
| msg.from | sender_id | number@c.us or group@g.us |

## Failure Handling
1. Retry: 3 attempts, exponential backoff
2. Fallback: Queue if disconnected, flush on reconnect
3. Rate limit: 20 msgs/min sliding window

## Metadata

```yaml
id: p04_webhook_whatsapp_bridge
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p04-webhook-whatsapp-bridge.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `webhook` |
| Pillar | P04 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[webhook-builder]] | related | 0.24 |
| [[p04_webhook_NAME]] | sibling | 0.23 |
| [[db-connector-builder]] | related | 0.23 |
| [[tpl_validation_schema]] | downstream | 0.23 |
| [[p11_qg_connector]] | downstream | 0.20 |
| [[bld_knowledge_card_connector]] | upstream | 0.20 |
| [[p01_kc_webhook]] | upstream | 0.20 |
| [[skill]] | downstream | 0.19 |
| [[bld_collaboration_webhook]] | related | 0.19 |
| [[research_then_build]] | downstream | 0.19 |
