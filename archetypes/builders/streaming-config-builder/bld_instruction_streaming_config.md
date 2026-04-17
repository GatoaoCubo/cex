---
kind: instruction
id: bld_instruction_streaming_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for streaming_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Streaming Config"
version: "1.0.0"
author: n03_builder
tags: [streaming_config, builder, instruction, P03]
tldr: "3-phase process: research transport needs, compose spec with buffer/heartbeat/backpressure, validate gates."
domain: "streaming config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Instructions: How to Produce a streaming_config

## Phase 1: RESEARCH

1. Identify the streaming use case: LLM token delivery, event broadcast, file download,
   bidirectional chat, live dashboard, or progressive rendering
2. Select the protocol:
   - SSE: unidirectional, HTTP/1.1, auto-reconnect, ideal for LLM token streams
   - WebSocket: bidirectional, upgraded TCP, ideal for interactive chat
   - Chunked: one-shot large response, no persistent connection
   - Auto: let server negotiate; document decision criteria
3. Determine data volume and velocity: tokens/sec, message rate, payload size per frame
4. Identify proxy and load balancer constraints: timeout limits, buffering behavior,
   whether they support long-lived connections (SSE/WS need 60s+ keepalive)
5. Determine backpressure requirements: can slow consumers drop events (drop), block
   producers (block), or buffer overflow (buffer with limit)?
6. Check existing streaming_configs via brain_query [IF MCP] -- do not duplicate a config
   that already covers this transport use case

## Phase 2: COMPOSE

1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` -- never self-score
4. Write **Overview** section: protocol, purpose, producer identity, consumer identity
5. Write **Protocol Settings** section: table with all protocol-specific parameters
   (event format for SSE, frame type for WebSocket, chunk size for chunked)
6. Write **Flow Control** section: buffer_bytes, flush_interval_ms, backpressure_strategy,
   max_connections, and overflow behavior
7. Write **Lifecycle** section: heartbeat_interval_ms, timeout_ms, reconnect_delay_ms,
   max_reconnect_attempts, graceful shutdown procedure
8. Confirm body <= 2048 bytes

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p05_sc_[a-z][a-z0-9_]+$`
4. Confirm `protocol` is one of: sse, websocket, chunked, auto
5. Confirm `buffer_bytes` is positive integer (not zero, not absent for SSE/WS)
6. Confirm `heartbeat_interval_ms` is present for SSE and WebSocket protocols
7. Confirm no actual credentials or endpoint secrets appear in the artifact
8. Confirm `quality` is null
9. Confirm body <= 2048 bytes
10. Cross-check: is this a transport configuration? If this defines response JSON shape,
    it belongs in `output_template`. If it defines data serialization, it belongs in
    `formatter`. If it defines observability, it belongs in `trace_config`.
11. If score < 8.0: revise in the same pass before outputting
