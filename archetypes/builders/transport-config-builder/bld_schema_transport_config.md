---
kind: schema
id: bld_schema_transport_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for transport_config
quality: 9.1
title: "Schema Transport Config"
version: "1.1.0"
author: n04_hybrid_review2
tags: [transport_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for transport_config"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_rl_algorithm
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_thinking_config
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | - | Matches `^p09_tc_[a-z0-9_]+$` |
| kind | string | yes | "transport_config" | CEX kind |
| pillar | string | yes | "P09" | Pillar classification |
| title | string | yes | - | Configuration title |
| version | string | yes | "1.0.0" | Semantic versioning |
| created | date | yes | - | ISO 8601 creation date |
| updated | date | yes | - | ISO 8601 last update |
| author | string | yes | - | Author or nucleus ID |
| domain | string | yes | - | Operational domain |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Lowercase alphanumeric tags |
| tldr | string | yes | - | One-line summary |
| transport_type | enum | yes | - | See transport_type enum below |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| protocol | string | Specific protocol version (e.g., "rfc6455", "grpc-over-http2") |
| description | string | Detailed purpose and context |
| notes | string | Additional context, tradeoffs |

## Transport Type Enum
```
transport_type: webrtc | websocket | sse | grpc_streaming | quic | tcp | udp | http2
```

## ID Pattern
```
^p09_tc_[a-z0-9_]+$
```

Examples: `p09_tc_webrtc_media`, `p09_tc_ws_events`, `p09_tc_grpc_inference`

## Body Structure
1. **Transport Type Declaration**
   State `transport_type` and primary `protocol` reference.

2. **Protocol-Specific Parameters**
   All mandatory fields for the declared `transport_type` (see system_prompt for per-protocol mandatory fields).

3. **Security Configuration**
   TLS/DTLS version, certificate paths (for server configs), DTLS role (for WebRTC).

4. **Resilience Parameters**
   Keepalive, heartbeat, ping/pong intervals, reconnection/retry policy with backoff.

5. **QoS and Performance**
   DSCP marking, message size limits, flow control windows, congestion control algorithm.

6. **Notes**
   Deployment context, NAT topology assumptions, known limitations.

## Constraints
- `quality` MUST be null (never "draft", "review", or a numeric score)
- `transport_type` MUST be from the enum above
- All required fields must be present and non-empty
- ID MUST match naming pattern
- WebRTC configs MUST include at least one TURN server entry
- All encrypted transports MUST specify TLS version >= 1.2
- Max file size: 4096 bytes (configs can be verbose; expanded from 2048)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.62 |
| [[bld_schema_usage_report]] | sibling | 0.62 |
| [[bld_schema_search_strategy]] | sibling | 0.61 |
| [[bld_schema_benchmark_suite]] | sibling | 0.61 |
| [[bld_schema_integration_guide]] | sibling | 0.60 |
| [[bld_schema_sandbox_config]] | sibling | 0.60 |
| [[bld_schema_rl_algorithm]] | sibling | 0.60 |
| [[bld_schema_pitch_deck]] | sibling | 0.59 |
| [[bld_schema_quickstart_guide]] | sibling | 0.59 |
| [[bld_schema_thinking_config]] | sibling | 0.59 |
