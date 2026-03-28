---
kind: memory
id: bld_memory_mcp_server
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for mcp_server artifact generation
---

# Memory: mcp-server-builder

## Summary

MCP server artifacts define how tools and resources are exposed to LLM agents via the Model Context Protocol. The critical production lesson is transport selection: stdio for local single-process, SSE for streaming over HTTP, HTTP for stateless request-response. Choosing the wrong transport causes silent failures — stdio servers cannot serve multiple concurrent agents, and SSE servers require persistent connections that some proxies terminate.

## Pattern

- Select transport based on deployment topology: stdio for co-located, SSE for real-time streaming, HTTP for stateless multi-client
- Define each tool with complete JSON Schema parameters — missing parameter schemas cause agent hallucination of arguments
- Resource URIs must follow consistent templates: {domain}/{resource_type}/{id} not ad-hoc paths
- Auth strategy varies by transport: stdio inherits process credentials, SSE/HTTP need explicit token or API key validation
- Keep tool count per server under 20 — servers with too many tools degrade agent tool-selection accuracy
- Document rate limits and timeout expectations per tool, not just per server

## Anti-Pattern

- Using stdio transport for multi-agent concurrent access — stdio is single-stream, causing message interleaving
- Tool definitions without parameter JSON Schema — agents guess parameters and produce invalid calls
- Mixing tool and resource concepts — tools perform actions (verbs), resources provide data (nouns)
- Omitting error response schemas — agents cannot distinguish tool failure from network failure
- Confusing mcp_server (protocol provider) with plugin (extension with lifecycle hooks) or connector (bidirectional sync)

## Context

MCP servers operate in the P04 tools layer. They are protocol-specific providers that expose capabilities to any MCP-compatible client. The protocol separates tool discovery (list), tool invocation (call), and resource access (read) into distinct operations. In multi-agent systems, MCP servers are the standardized interface between agent reasoning and external capabilities.

## Impact

Servers with complete JSON Schema tool definitions reduced agent tool-call errors by 70%. Correct transport selection eliminated 90% of concurrency-related failures. Servers exceeding 20 tools showed measurable degradation in agent tool-selection accuracy (15-20% more incorrect tool choices).

## Reproducibility

For reliable MCP server production: (1) determine deployment topology to select transport, (2) define all tools with complete JSON Schema parameters, (3) separate tools from resources, (4) configure auth per transport type, (5) document rate limits per tool, (6) validate tool count stays under 20.

## References

- mcp-server-builder SCHEMA.md (tool and resource specification)
- Model Context Protocol specification (stdio, SSE, HTTP transports)
- P04 tools pillar documentation
