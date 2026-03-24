---
id: p04_conn_whatsapp_bridge
name: whatsapp_bridge
description: "Bidirectional WhatsApp connector via whatsapp-web.js — REST send + webhook receive on port 3847"
protocol: REST+WebSocket
direction: bidirectional
auth: session
port: 3847
lp: P04
type: connector
version: 3.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: messaging
quality: 9.0
tags: [connector, whatsapp, bridge, rest, webhook, messaging]
---

# WhatsApp Bridge — Bidirectional Messaging Connector

## Purpose
Node.js connector providing bidirectional WhatsApp messaging via whatsapp-web.js with LocalAuth. Exposes REST API for sending and webhook push for receiving. Handles text, audio, images, video, documents, vcard, and stickers.

## Architecture
- **Runtime**: Node.js with `whatsapp-web.js` + `LocalAuth`
- **Auth**: QR code pairing (first run), session persistence after
- **Port**: 3847 (configurable)
- **Send**: REST API with rate limiting (20 msgs/min sliding window)
- **Receive**: Webhook push (POST to configurable URL, 3x retry)

## Endpoints

### GET /health
Returns uptime, messages processed, reconnect count, memory usage, last error.

### POST /send
Send text/media message to a WhatsApp number.

## Features
- Origin tracking (self/external, API-sent filtered)
- Reconnect with exponential backoff (5s -> 5min cap)
- Rate limiting on send (20 msgs/min sliding window)
- Graceful shutdown (SIGTERM/SIGINT -> close client + server)
- Multimedia: audio, text, image, video, document, vcard, sticker

## Integration
Paired with `wa_monitor.py` daemon which polls the bridge every 5s, detects new messages, transcribes audio via Groq, and writes signal files for CODEXA wake-on-message.
