---
id: p01_kc_cex_function_call
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function CALL — Tool Invocation Beyond Text Generation"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, call, tools, mcp, function-calling, plugin]
tldr: "CALL invokes external tools (APIs, MCPs, CLIs) via 8 types — expands LLM beyond text"
when_to_use: "Understand how LLMs use tools and the boundary between CALL (instrument) and COLLABORATE (agent)"
keywords: [call, tools, mcp, function-calling, plugin, skill, connector]
long_tails:
  - "What is the difference between CALL and COLLABORATE in CEX"
  - "What are the 8 tool types in the CEX taxonomy"
axioms:
  - "ALWAYS use REASON before CALL in complex chains"
  - "NEVER confuse CALL (passive tool) with COLLABORATE (active agent)"
linked_artifacts:
  primary: p01_kc_cex_function_reason
  related: [p01_kc_cex_function_become, p01_kc_cex_function_inject]
density_score: null
data_source: "https://arxiv.org/abs/2307.16789"
related:
  - p01_kc_cex_lp04_tools
  - p01_kc_mcp_server
  - p01_kc_lp04_tools
  - mcp-server-builder
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_llm_function_concept
  - bld_memory_mcp_server
  - bld_collaboration_mcp_server
  - p01_kc_cex_function_produce
  - db-connector-builder
---

## Summary

CALL invokes external tools to expand LLM capabilities beyond text generation. The LLM selects the tool, formats arguments (function calling), executes, and receives the result in context. With 8 types (10% of CEX), it covers from atomic functions (function_tool) to bidirectional MCP servers. Critical boundary: CALL uses passive instruments without identity; COLLABORATE converses with active agents with goals and memory.

## Spec

| Type | LP | Complexity | Function | Detail |
|------|-----|-----------|----------|--------|
| function_tool | P04 | Low | Atomic function | Typed schema, direct invocation |
| cli_tool | P04 | Low | CLI command | Single invocation without wrapper |
| connector | P04 | Medium | API client | SDK wrapper, retry, auth |
| plugin | P04 | Medium | Modular extension | Adds capability without altering core |
| component | P04 | Medium | Pipeline unit | Typed I/O, composable (Haystack) |
| scraper | P04 | Medium | Web extractor | HTML/JSON parsing, anti-bot |
| skill | P04 | High | Reusable recipe | Steps, quality gate, examples |
| mcp_server | P04 | High | MCP protocol | Bidirectional, stateful, stdio/sse |

Complexity hierarchy: function_tool < cli_tool < connector < skill < MCP.
function_tool is the minimal form: JSON schema + pure function.
MCP is the maximal form: bidirectional protocol with persistent state.
Critical boundary: CALL (passive tool, no identity) vs
COLLABORATE (active agent, with goals, memory, persona).
LangChain separates Tool from Agent. CrewAI confirms Tool vs Agent.

## Code

<!-- lang: python | purpose: MCP tool invocation -->
```python
# function_tool: forma mais simples de CALL
@function_tool
def get_price(product_id: str) -> float:
    return db.query(f"SELECT price FROM products WHERE id=?", product_id)

# mcp_server: protocolo bidirecional com estado
mcp = MCPServer("brain", transport="stdio")
result = mcp.call("brain_query", {"query": "agent for research"})
# tool (passivo, sem goals) != agent (ativo, com identidade)
```

## Patterns

| Trigger | Action |
|---------|--------|
| Simple atomic operation | function_tool with typed schema |
| Capability exists as CLI | cli_tool without wrapper |
| Integration with external service | connector as API client |
| Extension without modifying entity | modular plugin |
| Pipeline with standard interface | component with typed I/O |
| Standardized and reusable capability | skill with steps and quality gate |
| Bidirectional access with state | mcp_server (MCP protocol) |

## Anti-Patterns

- Agent with 20+ tools without specialists (split them)
- CALL without prior REASON (action without planning)
- Confusing tool (passive) with agent (active, with goals)
- MCP for simple stateless operation (use function_tool)
- Skill without quality gate (not validatable)
- Connector without retry/timeout (silent failure)

## References

- source: https://arxiv.org/abs/2307.16789
- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_function_reason
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp04_tools]] | sibling | 0.34 |
| [[p01_kc_mcp_server]] | sibling | 0.30 |
| [[p01_kc_lp04_tools]] | sibling | 0.29 |
| [[mcp-server-builder]] | downstream | 0.28 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.27 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.26 |
| [[bld_memory_mcp_server]] | downstream | 0.25 |
| [[bld_collaboration_mcp_server]] | downstream | 0.25 |
| [[p01_kc_cex_function_produce]] | sibling | 0.21 |
| [[db-connector-builder]] | downstream | 0.20 |
