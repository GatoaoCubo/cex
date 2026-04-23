---
kind: collaboration
id: bld_collaboration_streaming_config
pillar: P12
llm_function: COLLABORATE
purpose: How streaming-config-builder works in crews with other builders
pattern: each builder knows its ROLE, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Streaming Config"
version: "1.0.0"
author: n03_builder
tags: [streaming_config, builder, collaboration, P12]
tldr: "streaming-config-builder crews with agent-builder, api-client-builder, mcp-server-builder for real-time transport."
domain: "streaming config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_collaboration_mcp_server
  - bld_collaboration_retriever_config
  - bld_collaboration_env_config
  - bld_collaboration_trace_config
  - bld_collaboration_boot_config
  - bld_architecture_streaming_config
  - bld_collaboration_path_config
  - bld_collaboration_builder
  - bld_collaboration_handoff_protocol
  - bld_collaboration_client
---

# Collaboration: streaming-config-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should data stream from producer to consumer,
with what protocol and tuning?"
I do not define response data shapes. I do not define serialization formats.
I specify transport parameters so any server implementation delivers real-time data correctly.

## Crew Compositions

### Crew: "LLM Inference Streaming"
```
  1. agent-builder -> "agent definition and inference endpoint"
  2. streaming-config-builder -> "SSE transport spec for token delivery"
  3. output-template-builder -> "token wrapping and [DONE] sentinel format"
```

### Crew: "Real-Time API"
```
  1. api-client-builder -> "client consuming the stream"
  2. streaming-config-builder -> "WebSocket or SSE transport config"
  3. rate-limit-config-builder -> "connection count and burst limits"
  4. trace-config-builder -> "observability for stream health"
```

### Crew: "MCP Server with Streaming"
```
  1. mcp-server-builder -> "MCP server definition"
  2. streaming-config-builder -> "SSE transport for MCP protocol"
  3. env-config-builder -> "STREAM_AUTH_TOKEN and endpoint env vars"
```

## Handoff Protocol

### I Receive
- seeds: use case description, protocol preference (if any), expected data rate
- optional: proxy/LB constraints, consumer identity, max connection budget

### I Produce
- streaming_config artifact (.md + .yaml frontmatter)
- committed to: `P05_output/examples/p05_sc_{name}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- rate-limit-config-builder: reveals connection and rate constraints that bound max_connections
- env-config-builder: holds STREAM_AUTH_TOKEN and base URL env vars referenced by this config

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| agent-builder | Agent reads streaming_config for inference token delivery protocol |
| api-client-builder | Client uses timeout, reconnect, and protocol settings from this config |
| mcp-server-builder | MCP server reads SSE/WS transport config for its streaming interface |
| output-template-builder | Template wraps streamed content; needs to know protocol sentinel format |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_mcp_server]] | sibling | 0.40 |
| [[bld_collaboration_retriever_config]] | sibling | 0.39 |
| [[bld_collaboration_env_config]] | sibling | 0.39 |
| [[bld_collaboration_trace_config]] | sibling | 0.38 |
| [[bld_collaboration_boot_config]] | sibling | 0.37 |
| [[bld_architecture_streaming_config]] | upstream | 0.37 |
| [[bld_collaboration_path_config]] | sibling | 0.36 |
| [[bld_collaboration_builder]] | sibling | 0.35 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.35 |
| [[bld_collaboration_client]] | sibling | 0.34 |
