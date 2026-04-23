---
kind: quality_gate
id: p11_qg_streaming_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of streaming_config artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: "Gate: streaming_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, streaming-config, SSE, WebSocket, chunked, P11]
tldr: "Gates for streaming_config: validates protocol enum, buffer positivity, heartbeat presence, lifecycle completeness."
domain: "streaming_config -- SSE, WebSocket, and chunked HTTP transport specifications"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_examples_streaming_config
  - bld_schema_streaming_config
  - p03_sp_streaming_config_builder
  - bld_architecture_streaming_config
  - bld_instruction_streaming_config
  - bld_output_template_streaming_config
  - streaming-config-builder
  - bld_config_streaming_config
  - p11_qg_chunk_strategy
  - bld_knowledge_card_streaming_config
---

## Quality Gate

# Gate: streaming_config

## Definition

| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All artifacts where `kind: streaming_config` |

## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.

| ID | Check | Failure message |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p05_sc_[a-z][a-z0-9_]+$` | "ID fails streaming_config namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"streaming_config"` | "Kind is not 'streaming_config'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, protocol, version, created, author, tags, tldr | "Missing required field(s)" |
| H07 | `protocol` is one of: sse, websocket, chunked, auto | "Protocol is not a valid enum value" |
| H08 | `buffer_bytes` is a positive integer (> 0) when present | "buffer_bytes must be a positive integer" |
| H09 | `heartbeat_interval_ms` is present when protocol is sse or websocket | "heartbeat_interval_ms required for SSE and WebSocket" |
| H10 | Body contains all 4 required sections: Overview, Protocol Settings, Flow Control, Lifecycle | "Missing required body section(s)" |

## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.

| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Protocol rationale | 1.0 | Explains why this protocol was chosen over alternatives |
| Buffer sizing justification | 1.0 | buffer_bytes choice is explained relative to expected data rate |
| Backpressure completeness | 1.0 | backpressure_strategy present with overflow rationale |
| Heartbeat tuning | 1.0 | heartbeat_interval_ms below known proxy timeout thresholds |
| Flush interval correctness | 1.0 | flush_interval_ms <= 50ms for token streams; documented rationale |
| Lifecycle completeness | 1.0 | timeout_ms, reconnect_delay_ms, shutdown strategy all present |
| Boundary clarity | 0.5 | Explicitly not output_template, formatter, or trace_config |
| Consumer/producer identification | 1.0 | Overview names the producer system and consumer system |
| Protocol settings completeness | 1.0 | All protocol-specific parameters filled (content_type, encoding, etc.) |
| Documentation quality | 0.5 | tldr names protocol and key tuning values |

Weight sum: 1.0+1.0+1.0+1.0+1.0+1.0+0.5+1.0+1.0+0.5 = 9.5 (normalized to 100%)

## Actions

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0 | REJECT | Return to author with failure report |

## Bypass

| Field | Value |
|-------|-------|
| conditions | New transport integration where full parameter set is not yet known |
| approver | Engineering lead approval required (written); protocol and buffer fields never bypassed |

## Examples

# Examples: streaming-config-builder

## Golden Example 1 -- SSE for LLM Token Delivery

INPUT: "Configure SSE streaming for LLM token delivery"

OUTPUT:
```yaml
id: p05_sc_llm_token_sse
kind: streaming_config
pillar: P05
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
protocol: sse
buffer_bytes: 4096
heartbeat_interval_ms: 15000
reconnect_delay_ms: 1000
max_reconnect_attempts: -1
max_connections: 200
backpressure_strategy: drop
timeout_ms: 60000
flush_interval_ms: 50
quality: null
tags: [streaming_config, sse, llm, token-delivery]
tldr: "SSE stream for LLM tokens: 4KB buffer, 50ms flush, 15s heartbeat, drop on overflow"
description: "SSE config for streaming LLM inference tokens from FastAPI to browser client"
```

## Overview
SSE transport for real-time LLM token delivery from inference server to browser.
Producer: FastAPI inference endpoint. Consumer: browser EventSource API.

## Protocol Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| protocol | sse | Unidirectional; browser auto-reconnects |
| content_type | text/event-stream | Required MIME for SSE |
| encoding | utf-8 | Text tokens |
| event_id | enabled | Allows reconnect resume from last token |
| event_type | token | Named event; client filters by type |

## Flow Control

| Parameter | Value | Notes |
|-----------|-------|-------|
| buffer_bytes | 4096 | 4KB -- fits ~1000 tokens before flush |
| flush_interval_ms | 50 | 20 flushes/sec -- smooth UX |
| backpressure_strategy | drop | Slow client drops tokens; LLM keeps generating |
| max_connections | 200 | Limit concurrent inferences |

## Lifecycle

| Parameter | Value | Notes |
|-----------|-------|-------|
| heartbeat_interval_ms | 15000 | Comment event every 15s prevents proxy timeout |
| timeout_ms | 60000 | 60s idle terminates stream |
| reconnect_delay_ms | 1000 | 1s before EventSource reconnects |
| max_reconnect_attempts | -1 | Infinite -- client retries until done |
| shutdown | graceful | Send [DONE] sentinel before closing |

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p05_sc_ pattern (H02 pass)
- kind: streaming_config (H04 pass)
- protocol: sse (valid enum, H06 pass)
- buffer_bytes: 4096 positive integer (H07 pass)
- heartbeat_interval_ms present for SSE (H08 pass)
- 4 body sections present (H09 pass)
- No credentials in artifact (H10 pass)
- tldr <= 160 chars (S01 pass)
- tags includes "streaming_config" (S02 pass)

## Golden Example 2 -- WebSocket for Chat

INPUT: "Configure WebSocket streaming for bidirectional chat"

OUTPUT (frontmatter only for brevity):
```yaml
id: p05_sc_chat_websocket
kind: streaming_config
pillar: P05
protocol: websocket
buffer_bytes: 8192
heartbeat_interval_ms: 30000
max_connections: 500
backpressure_strategy: block
timeout_ms: 300000
quality: null
tags: [streaming_config, websocket, chat]
tldr: "WebSocket chat stream: 8KB buffer, 30s ping, block on overflow, 5min idle timeout"
```

Key differences from SSE: block backpressure (messages must not drop in chat),
larger buffer (binary frames), longer timeout (chat sessions persist).

## Anti-Example

INPUT: "create streaming config"

BAD OUTPUT:
```yaml
id: streaming-config-1
kind: stream
protocol: http
buffer: big
quality: 8.5
tags: [config]
```

FAILURES:
1. id: "streaming-config-1" uses hyphens and no `p05_sc_` prefix -- H02 FAIL
2. kind: "stream" not "streaming_config" -- H04 FAIL
3. protocol: "http" not a valid enum (sse|websocket|chunked|auto) -- H06 FAIL
4. buffer: "big" is not a positive integer -- H07 FAIL
5. quality: 8.5 (not null) -- H05 FAIL
6. Missing required fields: pillar, version, created, updated, author, tldr -- H06 FAIL
7. tags: only 1 item, missing "streaming_config" -- S02 FAIL
8. Body missing all 4 required sections -- H09 FAIL
9. No heartbeat_interval_ms defined -- H08 FAIL
10. No backpressure_strategy defined -- H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
