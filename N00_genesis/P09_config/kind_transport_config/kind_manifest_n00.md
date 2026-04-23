---
id: n00_transport_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Transport Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, transport_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_transport_config
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_streaming_config
  - bld_schema_thinking_config
  - bld_schema_dataset_card
  - bld_schema_vad_config
  - bld_schema_benchmark_suite
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A transport_config defines the network transport layer for realtime communication between CEX agents, tools, and external services: protocol selection (WebSocket, WebRTC, gRPC, SSE), TLS settings, connection pooling, keepalive intervals, and reconnection strategies. It ensures reliable and secure data transmission for voice sessions, streaming outputs, and inter-nucleus signals.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `transport_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| protocol | enum | yes | websocket \| webrtc \| grpc \| sse \| http2 |
| tls_required | boolean | yes | Enforce TLS for all connections |
| tls_version | enum | no | tls12 \| tls13 (default tls13) |
| keepalive_interval_s | integer | no | Seconds between keepalive pings |
| connection_timeout_ms | integer | yes | Connection establishment timeout |
| max_reconnect_attempts | integer | no | Reconnection attempts before abort |
| reconnect_backoff_ms | integer | no | Base delay for reconnection backoff |
| max_message_size_bytes | integer | no | Maximum single message size |

## When to use
- Configuring the WebSocket layer for a realtime voice session
- Setting up gRPC transport for high-throughput inter-nucleus communication
- Defining SSE parameters for streaming LLM output to a browser client

## Builder
`archetypes/builders/transport_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind transport_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: transport_config_realtime_ws
kind: transport_config
pillar: P09
nucleus: n05
title: "Realtime WebSocket Transport"
version: 1.0
quality: null
---
protocol: websocket
tls_required: true
tls_version: tls13
keepalive_interval_s: 30
connection_timeout_ms: 5000
max_reconnect_attempts: 5
reconnect_backoff_ms: 1000
```

## Related kinds
- `realtime_session` (P09) -- session config that uses this transport layer
- `runtime_rule` (P09) -- timeout rules that apply to transport connections
- `secret_config` (P09) -- TLS certificates managed as secrets

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_transport_config]] | upstream | 0.41 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[bld_schema_integration_guide]] | upstream | 0.37 |
| [[bld_schema_sandbox_spec]] | upstream | 0.37 |
| [[bld_schema_streaming_config]] | upstream | 0.37 |
| [[bld_schema_thinking_config]] | upstream | 0.36 |
| [[bld_schema_dataset_card]] | upstream | 0.36 |
| [[bld_schema_vad_config]] | upstream | 0.36 |
| [[bld_schema_benchmark_suite]] | upstream | 0.35 |
