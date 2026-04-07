---
id: p01_kc_mcp_protocol
kind: knowledge_card
type: domain
pillar: P01
title: 'MCP Protocol: Tools, Resources, Prompts, Transport, Capabilities'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: mcp_protocol
origin: src_provider_taxonomy
quality: 9.1
tags:
- mcp
- model-context-protocol
- tools
- resources
- prompts
- transport
- knowledge
tldr: Model Context Protocol (MCP) covering the 3-tier architecture (Host/Client/Server), server primitives (tools/resources/prompts),
  client primitives (sampling/elicitation/logging), JSON-RPC methods, and transport layers (stdio/Streamable HTTP).
when_to_use: When building MCP servers, integrating MCP clients, or understanding how MCP connects AI hosts to external context.
keywords:
- mcp
- model_context_protocol
- tools
- resources
- prompts
- transport
- json_rpc
long_tails:
- mcp server tool resource prompt primitives architecture
- mcp stdio vs streamable http transport capabilities negotiation
axioms:
- MCP is provider-agnostic -- any AI host can use MCP servers regardless of underlying model
feeds_kinds:
- mcp_server
- function_def
- knowledge_card
- prompt_template
- plugin
- hook
linked_artifacts:
  adw: null
  agent: null
  hop: null
density_score: 0.91
---

# KC-Domain: MCP Protocol

## Quick Reference
```yaml
topic: Model Context Protocol (modelcontextprotocol.io)
scope: Architecture, primitives, methods, transport
owner: builder_agent
criticality: high
```

## Architecture (3-Tier)

| Participant | Role | Examples |
|-------------|------|----------|
| `MCP Host` | AI application | Claude Desktop, VS Code, Claude Code |
| `MCP Client` | Connection manager | Dedicated 1:1 connection to one MCP Server |
| `MCP Server` | Context provider | Exposes tools, resources, prompts; local or remote |

**Relationship**: Host contains 1+ Clients. Each Client connects to exactly 1 Server. Host orchestrates across all Clients.

## Server Primitives

| Primitive | Purpose | Key Fields |
|-----------|---------|------------|
| `tool` | Executable function | `name`, `title`, `description`, `inputSchema` (JSON Schema) |
| `resource` | Data source | `name`, `description`, URI-addressable |
| `prompt` | Reusable template | `name`, `description`, parameterized |

**Tools** = actions (file ops, API calls, DB queries). **Resources** = data (file contents, DB records). **Prompts** = templates (system prompts, few-shot examples).

## Client Primitives

| Primitive | Purpose | Method |
|-----------|---------|--------|
| `sampling` | Server requests LLM completion from Host | `sampling/complete` |
| `elicitation` | Server requests user input | `elicitation/request` |
| `logging` | Server sends debug log messages | Log messages to client |

## JSON-RPC 2.0 Methods

### Lifecycle
| Method | Direction | Purpose |
|--------|-----------|---------|
| `initialize` | Client -> Server | Establish connection, negotiate capabilities |
| `notifications/initialized` | Client -> Server | Confirm readiness after initialize |

### Discovery & Execution
| Method | Direction | Purpose |
|--------|-----------|---------|
| `tools/list` | Client -> Server | List available tools |
| `tools/call` | Client -> Server | Invoke tool by name with arguments |
| `resources/list` | Client -> Server | List available resources |
| `resources/read` | Client -> Server | Read resource by URI |
| `prompts/list` | Client -> Server | List prompt templates |
| `prompts/get` | Client -> Server | Get specific prompt template |

### Client Methods (reverse direction)
| Method | Direction | Purpose |
|--------|-----------|---------|
| `sampling/complete` | Server -> Client | Request LLM completion |
| `elicitation/request` | Server -> Client | Request user input |

### Notifications
| Method | Direction | Purpose |
|--------|-----------|---------|
| `notifications/tools/list_changed` | Server -> Client | Tools changed (requires `listChanged: true` capability) |

## Transport Layers

| Transport | Mechanism | Best For |
|-----------|-----------|----------|
| `stdio` | stdin/stdout streams | Local processes; zero network overhead |
| `Streamable HTTP` | HTTP POST + optional SSE | Remote servers; supports OAuth |

## Capabilities Negotiation

During `initialize`, both sides declare supported features:
- **Server capabilities**: `tools` (+ `listChanged`), `resources`, `prompts`, `logging`
- **Client capabilities**: `sampling`, `elicitation`
- **Protocol version**: Date string (e.g., `"2025-06-18"`)

## Cross-Provider Alignment

| Concept | MCP | Anthropic | OpenAI | AWS |
|---------|-----|-----------|--------|-----|
| Tool def | `tool` (inputSchema) | `tool` (input_schema) | `tool` > `function` (parameters) | `action_group` (OpenAPI) |
| Data access | `resource` | No native | `file_search` + `vector_store` | `knowledge_base` |
| Templates | `prompt` | System prompt | Thread instructions | Agent instructions |
| Orchestration | Host orchestrates Clients | Client-side agentic loop | Server-side Run lifecycle | Server-side FM orchestration |
| Discovery | `tools/list`, `resources/list` | Defined in request | Defined in request | Defined in agent config |

## Golden Rules
- MCP is **provider-agnostic** -- works with Claude, GPT, Gemini, or any LLM
- Each MCP Client maintains exactly one Server connection (1:1)
- `tools/call` is the primary execution method; `resources/read` is the primary data method
- Always handle `notifications/tools/list_changed` for dynamic tool servers
- `stdio` for local = fast + simple; `Streamable HTTP` for remote = needs auth (OAuth supported)
- `inputSchema` uses standard JSON Schema -- same as Anthropic's `input_schema`
- Experimental: `Tasks` primitive for durable execution (deferred results + status tracking)

## Flow
```text
[Host spawns Client] -> [Client: initialize] -> [Server: capabilities] -> [Client: tools/list] -> [Host: select tool] -> [Client: tools/call] -> [Server: execute + return] -> [Host: present result]
```

## References
- Origin: src_provider_taxonomy.md (Provider Official Taxonomy)
- Architecture: modelcontextprotocol.io/docs/learn/architecture
- Protocol spec: modelcontextprotocol.io/specification
