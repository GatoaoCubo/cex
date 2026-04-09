---
id: p01_kc_mcp_server
kind: knowledge_card
type: kind
pillar: P01
title: "MCP Server — Deep Knowledge for mcp_server"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: mcp_server
quality: 9.1
tags: [mcp_server, P04, CALL, kind-kc, mcp]
tldr: "Model Context Protocol server exposing typed tools and resources over stdio/SSE — the standard plugin interface for Claude Code and any MCP-aware LLM runtime"
when_to_use: "Building, reviewing, or reasoning about mcp_server artifacts"
keywords: [mcp, server, tools, resources, protocol]
feeds_kinds: [mcp_server]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
aliases: ["tool server", "MCP plugin", "tool provider", "Model Context Protocol server", "MCP endpoint"]
user_says: ["create an MCP server", "servidor MCP", "expose tools to Claude", "give the AI access to my database", "build an MCP plugin"]
long_tails: ["I want to give Claude access to my database via MCP", "expose a set of tools over the Model Context Protocol", "build a tool server that Claude Code can connect to", "create an MCP server with stdio transport for local tools"]
cross_provider:
  langchain: "LangChain MCP Adapters (mcp-adapters)"
  llamaindex: "McpToolSpec"
  crewai: "MCPServerAdapter"
  dspy: "n/a (manual function_def wrapping)"
  openai: "n/a (uses function_def natively)"
  anthropic: "Native MCP client in Claude Code"
  haystack: "n/a (tool wrapping required)"
---

# MCP Server

## Spec
```yaml
kind: mcp_server
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_mcp_{{server}}.md + .yaml
core: true
```

## What It Is
An mcp_server is a process that speaks the Model Context Protocol (MCP), exposing a set of tools (callable functions) and resources (readable data) over stdio or SSE transport. The LLM client connects via MCP handshake, lists available tools, and calls them by name. It is NOT a connector (simple integration without protocol), NOT an MCP client (which consumes an mcp_server), NOT a bare function_def (JSON schema only, no protocol handshake).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | LangChain MCP Adapters (mcp-adapters) | Converts MCP tools to LC BaseTool |
| LlamaIndex | McpToolSpec | Wraps MCP server as LI FunctionTool |
| CrewAI | MCPServerAdapter | Exposes MCP tools as CrewAI Tool |
| DSPy | n/a (no native MCP support) | Manual function_def wrapping required |
| Haystack | n/a (no native MCP support) | Tool wrapping required |
| OpenAI | n/a (uses function_def natively) | No MCP support in ChatCompletion |
| Anthropic | Native MCP client in Claude Code | First-class; .mcp.json config file |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| transport | str | stdio | stdio = simple local; sse = networked |
| tools_provided | list[str] | [] | More tools = richer; harder to manage |
| resources_provided | list[str] | [] | Resources for context injection |
| strict_mcp_config | bool | false | True = only listed servers load |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Stdio local server | Dev, same-machine tools | brain_query MCP via stdio |
| SSE remote server | Multi-agent shared tools | Railway-hosted shared MCP |
| Per-agent_group config | Isolated tool sets | .mcp-atlas.json, .mcp-shaka.json |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| All tools in one server | LLM confused choosing between 30 tools | Split by domain (brain, db, browser) |
| No JSON Schema on tool params | LLM guesses wrong types and fails | Add JSON Schema to every tool |
| Global strict-mcp-config off | All servers load in every session | Use per-agent_group .mcp-{sat}.json configs |

## Integration Graph
```
[LLM client] --> [MCP handshake] --> [mcp_server] --> [tool_result / resource_content]
                                          |
                               [tools_provided, resources_provided, transport]
```

## Decision Tree
- IF single function, no protocol needed THEN use function_def
- IF simple HTTP client implementation THEN use api_client
- IF exposing domain-specific multi-tool suite THEN use mcp_server
- DEFAULT: mcp_server when Claude Code protocol interoperability is required

## Quality Criteria
- GOOD: transport configured, tools listed, each tool has JSON Schema
- GREAT: per-agent_group config, resources provided, version pinned, tested with MCP inspector
- FAIL: no schema on tools, wrong transport for environment, tools not grouped by domain
