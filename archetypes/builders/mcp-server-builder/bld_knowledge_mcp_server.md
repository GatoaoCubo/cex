---
kind: knowledge_card
id: bld_knowledge_card_mcp_server
pillar: P04
llm_function: INJECT
purpose: Domain knowledge for mcp_server production — atomic searchable facts
sources: mcp-server-builder MANIFEST.md + SCHEMA.md v1.0.0
quality: 9.1
title: "Knowledge Card Mcp Server"
version: "1.0.0"
author: n03_builder
tags: [mcp_server, builder, examples]
tldr: "Golden and anti-examples for mcp server construction, demonstrating ideal structure and common pitfalls."
domain: "mcp server construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_mcp_server
  - bld_memory_mcp_server
  - p03_sp_mcp_server_builder
  - mcp-server-builder
  - p11_qg_mcp_server
  - p01_kc_mcp_server
  - bld_config_mcp_server
  - bld_collaboration_mcp_server
  - bld_schema_mcp_server
  - bld_examples_mcp_server
---

# Domain Knowledge: mcp_server
## Executive Summary
MCP servers are protocol-compliant providers that expose tools and resources to LLM agents via the Model Context Protocol (JSON-RPC 2.0). Each server declares a transport (stdio/SSE/HTTP), tools with JSON-Schema parameters, and resources with URI templates. They differ from connectors (bidirectional integrations), clients (API consumers), plugins (lifecycle-based extensions), and skills (LLM-level capabilities) by implementing the standardized MCP protocol for agent-to-tool communication.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools/infrastructure) |
| Kind | `mcp_server` (exact literal) |
| ID pattern | `p04_mcp_{slug}` |
| Protocol | JSON-RPC 2.0 over stdio, SSE, or HTTP |
| Quality gates | HARD + SOFT (per QUALITY_GATES.md) |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Key fields | transport, tools_provided, resources_provided, auth |
## Patterns
| Pattern | Application |
|---------|-------------|
| Transport selection | stdio = local subprocess; SSE = remote streaming; HTTP = high-throughput remote |
| Tool schema | JSON-Schema object: name (snake_case), description (1 sentence), inputSchema |
| Resource URIs | file://, db://, api://, mem:// — resources are READ-ONLY snapshots |
| Auth by transport | stdio = none (process trust); SSE/HTTP = api_key or OAuth |
| Tools vs resources | Tools = ACTIONS (side effects); Resources = READ-ONLY snapshots |
| Minimal tool surface | Expose only necessary tools; fewer tools = better agent routing |
### Transport Decision Table
| Condition | Transport | Auth |
|-----------|-----------|------|
| Local filesystem/CLI wrapper | stdio | none |
| Cloud API with streaming | SSE | api_key |
| High-throughput remote service | HTTP (streamable) | api_key or OAuth |
| Shared team infrastructure | SSE or HTTP | OAuth |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| stdio with auth headers | stdio is local process; auth adds complexity with no benefit |
| Resource that modifies state | Resources are READ-ONLY; use tools for mutations |
| Tool without inputSchema | Agent cannot discover parameters; blind invocation |
| Mixed transport in one server | One server = one transport; use separate servers |
| Vague tool description | Agent routing fails; description must state what + when |
| No error response spec | JSON-RPC 2.0 requires error codes; omission breaks protocol |
## Application
1. Choose transport based on deployment: stdio (local), SSE (remote stream), HTTP (remote batch)
2. Define `tools_provided`: each with name, description, and JSON-Schema inputSchema
3. Define `resources_provided`: each with URI template and content type
4. Set auth strategy matching transport (none for stdio, api_key/OAuth for remote)
5. Specify error codes following JSON-RPC 2.0 convention
6. Document startup command and environment requirements
7. Validate: body <= 4096 bytes, density >= 0.80, all HARD + SOFT gates
## References
- mcp-server-builder SCHEMA.md v1.0.0
- MCP Specification: modelcontextprotocol.io
- JSON-RPC 2.0 Specification: jsonrpc.org/specification
- Anthropic MCP documentation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_mcp_server]] | upstream | 0.61 |
| [[bld_memory_mcp_server]] | downstream | 0.60 |
| [[p03_sp_mcp_server_builder]] | upstream | 0.55 |
| [[mcp-server-builder]] | related | 0.53 |
| [[p11_qg_mcp_server]] | downstream | 0.50 |
| [[p01_kc_mcp_server]] | sibling | 0.50 |
| [[bld_config_mcp_server]] | downstream | 0.50 |
| [[bld_collaboration_mcp_server]] | related | 0.42 |
| [[bld_schema_mcp_server]] | downstream | 0.41 |
| [[bld_examples_mcp_server]] | downstream | 0.40 |
