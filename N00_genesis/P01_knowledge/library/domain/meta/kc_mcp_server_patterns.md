---
id: p01_kc_mcp_server_patterns
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "MCP Server Patterns — Tool Integration Standard"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: meta
quality: 9.0
tags: [mcp, server, tool-integration, protocol, standard]
tldr: "Model Context Protocol: universal tool integration for LLMs. Server exposes tools/resources/prompts. Client (LLM) calls them. JSON-RPC over stdio."
when_to_use: "Adding external tool capabilities to any LLM agent"
keywords: [mcp, model-context-protocol, tool-server, json-rpc, stdio]
density_score: 0.93
related:
  - p01_kc_mcp_server
  - p01_kc_tool_use
  - self_audit_n05_20260408
  - p01_kc_mcp_protocol
  - bld_memory_mcp_server
  - mcp-server-builder
  - p04_tool_mcp_config
  - bld_collaboration_mcp_server
  - bld_tools_mcp_server
  - self_audit_newpc_n02
---

# MCP Server Patterns

## Core Architecture
```
LLM (client) ←→ MCP Server ←→ External Service
              JSON-RPC/stdio      API/DB/FS
```

## Three Primitives

| Primitive | What | Example |
|-----------|------|---------|
| **Tool** | Callable function | `search_web(query)`, `deploy(config)` |
| **Resource** | Readable data | `file://docs/`, `db://users` |
| **Prompt** | Reusable template | `brand_discovery_interview` |

## CEX MCP Configs

| Nucleus | Servers | Purpose |
|---------|---------|---------|
| N01 | gemini (native) | Research via Gemini |
| N02 | markitdown, puppeteer | Read docs, browser automation |
| N05 | postgres | Database operations |
| N06 | fetch, markitdown, stripe, hotmart | Web, docs, payments |

## Config Format (`.mcp-n0X.json`)
```json
{
  "mcpServers": {
    "server_name": {
      "command": "npx",
      "args": ["-y", "package-name"],
      "env": { "API_KEY": "${API_KEY}" }
    }
  }
}
```

## Best Practices
1. Environment variables for secrets (`${VAR}` not hardcoded)
2. One config per nucleus (scoped access)
3. Rate-limit tools with side effects
4. Describe tools clearly — LLM reads descriptions to decide usage

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_mcp_server]] | sibling | 0.36 |
| [[p01_kc_tool_use]] | sibling | 0.30 |
| [[self_audit_n05_20260408]] | sibling | 0.28 |
| [[p01_kc_mcp_protocol]] | sibling | 0.28 |
| [[bld_memory_mcp_server]] | downstream | 0.28 |
| [[mcp-server-builder]] | downstream | 0.28 |
| [[p04_tool_mcp_config]] | downstream | 0.27 |
| [[bld_collaboration_mcp_server]] | downstream | 0.27 |
| [[bld_tools_mcp_server]] | downstream | 0.26 |
| [[self_audit_newpc_n02]] | downstream | 0.26 |
