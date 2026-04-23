---
id: p01_kc_anthropic_api_patterns
kind: knowledge_card
type: domain
pillar: P01
title: 'Anthropic API Patterns: Tool Use, Computer Use, Prompt Caching, Server Tools'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: anthropic_api
origin: src_provider_taxonomy
quality: 9.1
tags:
- anthropic
- tool-use
- computer-use
- prompt-caching
- server-tools
- knowledge
tldr: Anthropic Claude API patterns covering tool use (client/server tools, strict mode), computer use (actions + zoom), prompt
  caching (ephemeral TTL), and the agentic loop.
when_to_use: When building with Claude API, implementing tool use, optimizing with prompt caching, or setting up computer
  use automation.
keywords:
- anthropic
- tool_use
- computer_use
- prompt_caching
- server_tools
- agentic_loop
long_tails:
- anthropic tool use strict mode schema enforcement
- claude prompt caching cache_control ephemeral ttl pricing
axioms:
- Anthropic tool definitions use input_schema (JSON Schema); tool_choice controls selection with auto/any/tool/none
feeds_kinds:
- function_def
- mcp_server
- system_prompt
- prompt_template
- computer_use
- input_schema
linked_artifacts:
  adw: null
  agent: null
  hop: null
density_score: 0.92
related:
  - p01_kc_terminology_anthropic_canonical
  - p01_kc_terminology_openai_canonical
  - p01_kc_terminology_rosetta_stone
  - bld_tools_prompt_cache
  - p01_kc_openai_api_patterns
  - p01_kc_function_def
  - bld_collaboration_search_tool
  - bld_examples_knowledge_card
  - p01_kc_terminology_google_mcp_canonical
  - prompt-cache-builder
---

# KC-Domain: Anthropic API Patterns

## Quick Reference
```yaml
topic: Anthropic Claude API (docs.anthropic.com)
scope: Tool use, computer use, prompt caching, server tools
owner: builder_agent
criticality: high
```

## Tool Use

| Term | Role | Key Detail |
|------|------|------------|
| `tool` | Definition | `{name, description, input_schema}` in `tools` array |
| `tool_use` | Response block | Claude invokes tool: `{id, name, input}` |
| `tool_result` | Request block | Developer returns result: `{tool_use_id, content}` |
| `tool_choice` | Selection | `auto` (model decides) / `any` (must use) / `tool` (specific) / `none` |
| `strict: true` | Schema enforcement | Guarantees tool call matches input_schema exactly |
| `stop_reason: "tool_use"` | Signal | Generation stopped for pending tool call |

**Two categories**:
- **Client tools**: Execute in developer's app (user-defined + Anthropic-schema like bash, text_editor)
- **Server tools**: Execute on Anthropic infra (web_search, web_fetch, code_execution, tool_search)

### Server Tools (Built-in)
| Tool | Type String | Purpose |
|------|-------------|---------|
| Web Search | `web_search_20260209` | Search the web |
| Web Fetch | `web_fetch` | Fetch web content |
| Code Execution | `code_execution` | Run code on Anthropic servers |
| Tool Search | `tool_search` | Search available tools |

**Agentic Loop**: Claude returns `tool_use` -> developer executes -> sends `tool_result` -> Claude continues -> repeat until `stop_reason != "tool_use"`.

## Computer Use

| Term | Role | Key Detail |
|------|------|------------|
| `computer_20251124` | Latest tool | Beta header: `computer-use-2025-11-24`; supports Opus 4.6, Sonnet 4.6, Opus 4.5 |
| `computer_20250124` | Previous tool | Beta header: `computer-use-2025-01-24`; supports Claude 4 + Sonnet 3.7 |
| `text_editor_20250728` | Editor tool | Standard name: `str_replace_based_edit_tool` |
| `bash_20250124` | Shell tool | Command execution |

**Actions** (latest version): `screenshot`, `left_click`, `right_click`, `middle_click`, `double_click`, `triple_click`, `type`, `key`, `mouse_move`, `left_click_drag`, `scroll`, `hold_key`, `wait`, `left_mouse_down`, `left_mouse_up`, `zoom` (requires `enable_zoom: true`).

**Required params**: `display_width_px`, `display_height_px`.

## Prompt Caching

| Term | Role | Key Detail |
|------|------|------------|
| `cache_control` | Request object | `{"type": "ephemeral"}` or `{"type": "ephemeral", "ttl": "1h"}` |
| `ttl: "5m"` | Default TTL | 1.25x base price for cache creation |
| `ttl: "1h"` | Extended TTL | 2x base price for cache creation |
| `cache_read_input_tokens` | Usage | Tokens from cache: 0.1x base price (90% savings) |
| `cache_creation_input_tokens` | Usage | Tokens written to cache |
| Cache breakpoint | Concept | Max 4 per request; marks `cache_control` positions |

**Pricing math**: Cache miss = 1.25-2x write cost. Cache hit = 0.1x read cost. Break-even at 2-3 hits for 5m TTL, 4-5 hits for 1h TTL.

## Cross-Provider Alignment

| Concept | Anthropic | OpenAI Equivalent |
|---------|-----------|-------------------|
| Tool def | `tool` with `input_schema` | `tool` wrapping `function` with `parameters` |
| Invocation | `tool_use` block | `tool_calls` array |
| Result | `tool_result` with `tool_use_id` | tool role message with `tool_call_id` |
| Selection | `auto/any/tool/none` | `auto/none/required/function` |
| Parallel | Multiple `tool_use` blocks | `parallel_tool_calls: true` |
| Caching | Explicit `cache_control` | Automatic KV cache (no control) |
| Web search | `web_search_20260209` server tool | No native equivalent |
| Code exec | `code_execution` server tool | `code_interpreter` |

## Golden Rules
- Always handle `stop_reason: "tool_use"` in the agentic loop -- missing this breaks the cycle
- Prompt caching: place stable content (system prompt, tool defs) before cache breakpoints
- Computer use requires beta header -- requests without it get 400 errors
- `strict: true` is opt-in (unlike OpenAI where it's also opt-in but more commonly used)
- Server tools return results directly; client tools require developer-side execution

## Flow
```text
[Define tools + cache_control] -> [Send request] -> [Check stop_reason] -> [Execute tool_use] -> [Return tool_result] -> [Loop until done]
```

## References
- Origin: src_provider_taxonomy.md (Provider Official Taxonomy)
- Tool Use: /docs/en/agents-and-tools/tool-use
- Strict Tool Use: /docs/en/agents-and-tools/tool-use/strict-tool-use
- Computer Use: /docs/en/build-with-claude/computer-use
- Prompt Caching: /docs/en/build-with-claude/prompt-caching

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_terminology_anthropic_canonical]] | sibling | 0.51 |
| [[p01_kc_terminology_openai_canonical]] | sibling | 0.33 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.31 |
| [[bld_tools_prompt_cache]] | downstream | 0.30 |
| [[p01_kc_openai_api_patterns]] | sibling | 0.29 |
| [[p01_kc_function_def]] | sibling | 0.27 |
| [[bld_collaboration_search_tool]] | downstream | 0.27 |
| [[bld_examples_knowledge_card]] | downstream | 0.26 |
| [[p01_kc_terminology_google_mcp_canonical]] | sibling | 0.25 |
| [[prompt-cache-builder]] | downstream | 0.25 |
