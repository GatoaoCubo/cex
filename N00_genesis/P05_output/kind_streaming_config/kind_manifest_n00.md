---
id: n00_streaming_config_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Streaming Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, streaming_config, p05, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Streaming config produces a configuration artifact for real-time output delivery via Server-Sent Events (SSE), WebSocket, or chunked HTTP transfer encoding. It specifies buffer sizes, heartbeat intervals, reconnection policies, event type schemas, and client-side error handling. Used when LLM output must be displayed progressively rather than awaited to completion.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `streaming_config` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Service name + "Streaming Config" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| protocol | enum | yes | sse / websocket / chunked_http |
| buffer_size_bytes | int | yes | Chunk buffer size in bytes |
| heartbeat_interval_ms | int | no | Keepalive ping interval in milliseconds |
| reconnect_policy | object | yes | max_retries, backoff_ms, jitter |
| event_types | list | yes | Named event types with payload schemas |
| error_handling | object | yes | on_timeout, on_disconnect, on_error actions |

## When to use
- Building a chat interface that streams LLM tokens to the browser in real time
- Implementing a pipeline step that pushes progress events to a monitoring dashboard
- Configuring a backend service to deliver streaming completions via the Anthropic API

## Builder
`archetypes/builders/streaming_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind streaming_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements streaming infrastructure
- `{{SIN_LENS}}` -- Gating Wrath: zero dropped events, deterministic reconnection
- `{{TARGET_AUDIENCE}}` -- frontend engineers and backend service consumers
- `{{DOMAIN_CONTEXT}}` -- LLM provider API, client framework, latency requirements

## Example (minimal)
```yaml
---
id: streaming_config_cex_chat_api
kind: streaming_config
pillar: P05
nucleus: n05
title: "CEX Chat API -- SSE Streaming Config"
version: 1.0
quality: null
---
protocol: sse
buffer_size_bytes: 1024
heartbeat_interval_ms: 15000
event_types:
  - {name: token, schema: {text: string}}
  - {name: done, schema: {finish_reason: string}}
```

## Related kinds
- `api_reference` (P06) -- documents the streaming endpoints backing this config
- `trace_config` (P07) -- observability config that instruments streaming event flow
- `response_format` (P05) -- defines the content shape of each streamed chunk
