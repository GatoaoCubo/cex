---
kind: knowledge_card
id: bld_knowledge_card_streaming_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for streaming_config production -- SSE, WebSocket, chunked HTTP
sources: W3C SSE Spec, RFC 6455 (WebSocket), RFC 7230 (Chunked Transfer), WHATWG EventSource
quality: 9.1
title: "Knowledge Card Streaming Config"
version: "1.0.0"
author: n03_builder
tags: [streaming_config, builder, knowledge_card, P01, SSE, WebSocket, chunked]
tldr: "Domain knowledge for streaming transports: protocol comparison, buffer math, heartbeat tuning, backpressure patterns."
domain: "streaming config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.91
related:
  - p03_sp_streaming_config_builder
  - bld_config_streaming_config
  - bld_instruction_streaming_config
  - p10_lr_streaming_config_builder
  - bld_examples_streaming_config
  - streaming-config-builder
  - p11_qg_streaming_config
  - bld_output_template_streaming_config
  - bld_schema_streaming_config
  - bld_collaboration_streaming_config
---

# Domain Knowledge: streaming_config

## Executive Summary
Streaming configs specify how data flows from a server producer to a client consumer in
real time. Three protocols cover all cases: SSE (unidirectional HTTP text stream),
WebSocket (bidirectional TCP-upgraded binary/text stream), and Chunked (one-shot large
HTTP body). The config specifies protocol, buffer size, heartbeat interval, backpressure
strategy, and connection lifecycle -- not the data shape or serialization format.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P05 (output) |
| llm_function | PRODUCE |
| Frontmatter fields | 15+ |
| Quality gates | 10 HARD + 10 SOFT |
| Naming | p05_sc_{name}.yaml |
| Max body bytes | 2048 |

## Protocol Comparison

| Protocol | Direction | Transport | Best For | Not For |
|----------|-----------|-----------|----------|---------|
| SSE | Server -> Client | HTTP/1.1 keep-alive | LLM tokens, notifications, logs | Bidirectional, binary |
| WebSocket | Bidirectional | TCP upgrade | Chat, live dashboards, gaming | Simple unidirectional output |
| Chunked | Server -> Client | HTTP/1.1 (one-shot) | File download, batch response | Real-time, persistent |
| Auto | Negotiated | Depends | Adaptive systems | Precise tuning required |

## Buffer Sizing Reference

| Use Case | Recommended buffer_bytes | Rationale |
|----------|--------------------------|-----------|
| LLM token delivery (SSE) | 4096 | ~1000 tokens; flush every 50ms |
| Chat message (WS) | 8192 | Full message fits before send |
| File chunked download | 65536 | 64KB for efficient TCP segments |
| Event broadcast (SSE) | 2048 | Small events, high frequency |

## Heartbeat Intervals

| Proxy/LB | Default timeout | Recommended heartbeat_interval_ms |
|----------|-----------------|-----------------------------------|
| nginx | 60s | 15000 (15s) |
| AWS ALB | 60s | 15000 (15s) |
| Cloudflare | 100s | 30000 (30s) |
| Fastly | 60s | 15000 (15s) |
| No proxy (direct) | none | 30000 (30s) for WS |

## Backpressure Strategy Selection

| Strategy | When to use | Risk if wrong choice |
|----------|-------------|---------------------|
| drop | LLM tokens, logs, metrics -- loss acceptable | Chat messages silently lost |
| block | Chat, transactions -- loss unacceptable | Server OOM if consumer never catches up |
| buffer | Event broadcasts -- brief bursts acceptable | OOM if sustained slow consumer |

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| No heartbeat_interval_ms for SSE/WS | Proxy terminates after 60s idle |
| buffer_bytes: 0 | Disables flow control; immediate backpressure on every write |
| WebSocket for unidirectional LLM output | Bidirectional complexity, no benefit |
| flush_interval_ms > 200 for tokens | Visible batching; poor streaming UX |
| Credentials in artifact | Secrets committed to git |

## References
- W3C SSE: https://html.spec.whatwg.org/multipage/server-sent-events.html
- RFC 6455: WebSocket Protocol
- RFC 7230 Section 4.1: Chunked Transfer Coding
- WHATWG EventSource API
- nginx proxy_read_timeout documentation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_streaming_config_builder]] | downstream | 0.58 |
| [[bld_config_streaming_config]] | downstream | 0.56 |
| [[bld_instruction_streaming_config]] | downstream | 0.50 |
| [[p10_lr_streaming_config_builder]] | downstream | 0.49 |
| [[bld_examples_streaming_config]] | downstream | 0.48 |
| [[streaming-config-builder]] | downstream | 0.45 |
| [[p11_qg_streaming_config]] | downstream | 0.34 |
| [[bld_output_template_streaming_config]] | downstream | 0.34 |
| [[bld_schema_streaming_config]] | downstream | 0.34 |
| [[bld_collaboration_streaming_config]] | downstream | 0.34 |
