---
kind: output_template
id: bld_output_template_streaming_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a streaming_config artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.1
title: "Output Template Streaming Config"
version: "1.0.0"
author: n03_builder
tags: [streaming_config, builder, output_template, P05]
tldr: "Fill-in template for streaming_config: protocol, buffer, heartbeat, backpressure, lifecycle placeholders."
domain: "streaming config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_streaming_config
  - p03_sp_streaming_config_builder
  - bld_schema_streaming_config
  - p11_qg_streaming_config
  - bld_architecture_streaming_config
  - bld_instruction_streaming_config
  - bld_config_streaming_config
  - bld_knowledge_card_streaming_config
  - streaming-config-builder
  - bld_collaboration_streaming_config
---

# Output Template: streaming_config

```yaml
id: p05_sc_{{name}}
kind: streaming_config
pillar: P05
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
protocol: {{sse|websocket|chunked|auto}}
buffer_bytes: {{positive_integer}}
heartbeat_interval_ms: {{positive_integer_or_null_if_chunked}}
reconnect_delay_ms: {{positive_integer_for_sse_or_null}}
max_reconnect_attempts: {{integer_or_-1_for_infinite}}
max_connections: {{positive_integer}}
backpressure_strategy: {{drop|block|buffer}}
timeout_ms: {{positive_integer}}
flush_interval_ms: {{positive_integer_for_sse_or_null}}
quality: null
tags: [streaming_config, {{protocol_tag}}, {{use_case_tag}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_this_stream_does_max_200ch}}"
```

## Overview
`{{transport_protocol_and_why_1_sentence}}`
`{{producer_and_consumer_description}}`

## Protocol Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| protocol | {{sse|websocket|chunked}} | `{{rationale}}` |
| content_type | {{text/event-stream|application/octet-stream|text/plain}} | MIME for this protocol |
| encoding | {{utf-8|binary}} | Frame encoding |
| `{{protocol_param_1}}` | {{value}} | `{{notes}}` |
| `{{protocol_param_2}}` | {{value}} | `{{notes}}` |

## Flow Control

| Parameter | Value | Notes |
|-----------|-------|-------|
| buffer_bytes | `{{N}}` | Max bytes buffered before backpressure triggers |
| flush_interval_ms | `{{N}}` | How often buffered data is flushed to client |
| backpressure_strategy | {{drop|block|buffer}} | Overflow behavior |
| max_connections | `{{N}}` | Concurrent stream limit |

## Lifecycle

| Parameter | Value | Notes |
|-----------|-------|-------|
| heartbeat_interval_ms | `{{N}}` | Keepalive ping interval (prevents proxy timeout) |
| timeout_ms | `{{N}}` | Idle connection termination threshold |
| reconnect_delay_ms | `{{N}}` | Client reconnect backoff (SSE/WS) |
| max_reconnect_attempts | {{N or -1}} | -1 = infinite reconnect |
| shutdown | {{graceful|immediate}} | How stream closes on server stop |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_streaming_config]] | downstream | 0.56 |
| [[p03_sp_streaming_config_builder]] | upstream | 0.51 |
| [[bld_schema_streaming_config]] | downstream | 0.49 |
| [[p11_qg_streaming_config]] | downstream | 0.45 |
| [[bld_architecture_streaming_config]] | downstream | 0.44 |
| [[bld_instruction_streaming_config]] | upstream | 0.40 |
| [[bld_config_streaming_config]] | downstream | 0.35 |
| [[bld_knowledge_card_streaming_config]] | upstream | 0.34 |
| [[streaming-config-builder]] | related | 0.32 |
| [[bld_collaboration_streaming_config]] | downstream | 0.25 |
