---
id: p04_webhook_whatsapp_bridge
kind: webhook
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
---

# Connector: whatsapp_bridge

## Service Contract
- Service: WhatsApp via whatsapp-web.js (Node.js, port 3847)
- Mode: bidirectional (REST send + webhook receive)
- Auth: QR code first run, LocalAuth session persistence after

## Data Mapping
| External Field | Internal Field | Rule |
|----------------|----------------|------|
| msg.body | text | UTF-8, max 4096 chars |
| msg.hasMedia | audio_path | Download OGG to data/ |
| msg.from | sender_id | number@c.us or group@g.us |

## Failure Handling
- Retry: 3 attempts, exponential backoff
- Fallback: Queue if disconnected, flush on reconnect
- Rate limit: 20 msgs/min sliding window
