---
kind: config
id: bld_config_streaming_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 20
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Streaming Config"
version: "1.0.0"
author: n03_builder
tags: [streaming_config, builder, config, P09]
tldr: "Naming p05_sc_*, max 2048 bytes body, protocol enum enforced, heartbeat required for SSE/WS."
domain: "streaming config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_knowledge_card_streaming_config
  - p03_sp_streaming_config_builder
  - bld_instruction_streaming_config
  - bld_examples_streaming_config
  - bld_schema_streaming_config
  - streaming-config-builder
  - bld_config_handoff_protocol
  - bld_config_output_validator
  - p11_qg_streaming_config
  - bld_config_memory_scope
---

# Config: streaming_config Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p05_sc_{name}.yaml` | `p05_sc_llm_token_sse.yaml` |
| Builder directory | kebab-case | `streaming-config-builder/` |
| Frontmatter fields | snake_case | `buffer_bytes`, `heartbeat_interval_ms` |
| Name slug | snake_case, lowercase, no hyphens | `llm_token_sse`, `chat_websocket` |
| Protocol values | lowercase | `sse`, `websocket`, `chunked`, `auto` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
1. Output: `P05_output/examples/p05_sc_{name}.md`
2. Compiled: `P05_output/compiled/p05_sc_{name}.yaml`

## Size Limits (aligned with SCHEMA)
1. Body: max 2048 bytes
2. Total (frontmatter + body): ~3500 bytes
3. Density: >= 0.85 (no filler)

## Protocol Enum Enforcement

| Value | Transport | Use case |
|-------|-----------|----------|
| sse | HTTP/1.1 keep-alive, text/event-stream | LLM tokens, notifications, logs |
| websocket | TCP upgrade, RFC 6455 | Chat, live dashboards, bidirectional |
| chunked | HTTP/1.1 Transfer-Encoding: chunked | File download, large batch response |
| auto | Server negotiates | Adaptive, fallback-capable systems |

Any other value = HARD FAIL on H07.

## Heartbeat Requirement

| Protocol | heartbeat_interval_ms | Recommendation |
|----------|----------------------|----------------|
| sse | REQUIRED | 15000 (15s) for nginx/ALB |
| websocket | REQUIRED | 30000 (30s) standard ping/pong |
| chunked | OMIT | No persistent connection |
| auto | REQUIRED | Use SSE default (15000) |

## Backpressure Defaults by Use Case

| Use Case | Default strategy | Rationale |
|----------|-----------------|-----------|
| LLM token stream | drop | Tokens lost but generation continues |
| Chat / messaging | block | No message loss acceptable |
| Event broadcast | buffer | Brief spikes absorbed; OOM capped |
| File download | buffer | Receiver controls pace |

## Metadata

```yaml
id: bld_config_streaming_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_config_streaming_config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_streaming_config]] | upstream | 0.49 |
| [[p03_sp_streaming_config_builder]] | upstream | 0.43 |
| [[bld_instruction_streaming_config]] | upstream | 0.40 |
| [[bld_examples_streaming_config]] | upstream | 0.40 |
| [[bld_schema_streaming_config]] | upstream | 0.36 |
| [[streaming-config-builder]] | upstream | 0.35 |
| [[bld_config_handoff_protocol]] | sibling | 0.32 |
| [[bld_config_output_validator]] | sibling | 0.32 |
| [[p11_qg_streaming_config]] | downstream | 0.30 |
| [[bld_config_memory_scope]] | sibling | 0.30 |
