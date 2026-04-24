---
id: p01_kc_tool_use
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Tool Use / Function Calling"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.1
tags: [tool-use, function-calling, mcp, api, agentic]
tldr: "LLMs call external tools via structured definitions. Universal: define schema → LLM decides → runtime executes → LLM synthesizes."
when_to_use: "When building agentic systems that interact with external APIs, databases, or tools"
keywords: [tool-use, function-calling, mcp, api-integration, agentic]
density_score: 0.93
updated: "2026-04-07"
related:
  - p01_kc_mcp_server_patterns
  - p01_kc_function_def
  - p01_kc_universal_llm
  - p01_kc_mcp_server
  - p01_kc_terminology_rosetta_stone
  - bld_memory_mcp_server
  - bld_knowledge_card_function_def
  - p03_sp_function_def_builder
  - p01_kc_anthropic_api_patterns
  - p11_qg_mcp_server
---

# Tool Use / Function Calling

## Universal Pattern
```
DEFINE → PRESENT → DECIDE → CALL → RETURN → SYNTHESIZE
```

## Provider Implementations

| Provider | Mechanism | Schema Format |
|----------|-----------|---------------|
| Claude | tool_use blocks | JSON Schema in tools array |
| GPT | function_calling | JSON Schema in functions array |
| Gemini | function_declarations | OpenAPI-style schema |
| Llama | tool_call tokens | JSON Schema (varies by host) |
| MCP | Model Context Protocol | Standardized tool/resource/prompt |

## MCP — The Universal Standard
Abstracts tool provision across providers:
- **Tools**: callable functions (search, calculate, deploy)
- **Resources**: readable data (files, databases, APIs)
- **Prompts**: reusable prompt templates

## Best Practices
1. Tool descriptions matter as much as code — LLM reads them to decide
2. Keep params <7 — reduces hallucinated parameters
3. Return structured JSON, not prose
4. Error messages should be actionable, not stack traces
5. Rate-limit tools with side effects

## CEX Integration
- `.mcp-n0X.json` configs per nucleus
- `_tools/*.py` callable via subprocess
- `cex_run.py` orchestrates tool chains

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_mcp_server_patterns]] | sibling | 0.32 |
| [[p01_kc_function_def]] | sibling | 0.32 |
| [[p01_kc_universal_llm]] | sibling | 0.30 |
| [[p01_kc_mcp_server]] | sibling | 0.29 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.27 |
| [[bld_memory_mcp_server]] | downstream | 0.26 |
| [[bld_knowledge_card_function_def]] | sibling | 0.25 |
| [[p03_sp_function_def_builder]] | downstream | 0.23 |
| [[p01_kc_anthropic_api_patterns]] | sibling | 0.21 |
| [[p11_qg_mcp_server]] | downstream | 0.21 |
