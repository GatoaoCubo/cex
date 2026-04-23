---
id: p01_kc_google_ai_patterns
kind: knowledge_card
type: domain
pillar: P01
title: 'Google Gemini API Patterns: Function Calling, Grounding, Tool Config'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: google_ai
origin: src_provider_taxonomy
quality: 9.1
tags:
- google
- gemini
- function-calling
- grounding
- google-search
- knowledge
tldr: Google Gemini API patterns covering FunctionDeclaration/FunctionCall/FunctionResponse cycle, tool_config modes (AUTO/ANY/NONE/VALIDATED),
  and google_search grounding with citation metadata.
when_to_use: When building with Gemini API, comparing Google vs Anthropic/OpenAI function calling, or implementing search
  grounding.
keywords:
- gemini
- function_calling
- grounding
- google_search
- tool_config
long_tails:
- gemini function calling mode auto any none validated
- google gemini grounding metadata search citations
axioms:
- Google uses FunctionDeclaration/FunctionCall/FunctionResponse naming; mode field replaces tool_choice
feeds_kinds:
- function_def
- input_schema
- code_executor
- search_tool
- system_prompt
- response_format
linked_artifacts:
  adw: null
  agent: null
  hop: null
density_score: 0.88
related:
  - p01_kc_terminology_rosetta_stone
  - p01_kc_terminology_google_mcp_canonical
  - p01_kc_openai_api_patterns
  - p01_kc_terminology_openai_canonical
  - p01_kc_anthropic_api_patterns
  - p01_kc_function_def
  - p01_kc_terminology_anthropic_canonical
  - bld_collaboration_search_tool
  - bld_knowledge_card_function_def
  - bld_collaboration_function_def
---

# KC-Domain: Google Gemini API Patterns

## Quick Reference
```yaml
topic: Google Gemini API (ai.google.dev)
scope: Function calling, grounding, tool configuration
owner: builder_agent
criticality: medium
```

## Function Calling

| Term | Role | Key Detail |
|------|------|------------|
| `FunctionDeclaration` | Definition | `{name, description, parameters}` with optional `enum`; parameters use JSON Schema |
| `Tool` | Container | Holds one or more `function_declarations`; passed in model config |
| `FunctionCall` | Response | Model's invocation: `{name, args, id}` |
| `FunctionResponse` | Request | Developer's result: `{name, response, id}` -- `id` must match FunctionCall.id |
| `tool_config` | Config wrapper | Contains `function_calling_config` |
| `function_calling_config` | Inner config | Sets `mode` + optional `allowed_function_names` |

### Modes

| Mode | Behavior |
|------|----------|
| `AUTO` | Default; model decides function call vs natural response |
| `ANY` | Must call a function; ensures schema adherence |
| `NONE` | No function calls allowed |
| `VALIDATED` | Preview; model chooses with validation |

**`allowed_function_names`**: Array restricting callable functions. Use with `ANY` or `VALIDATED` modes.

**Loop**: Send `FunctionDeclaration` in Tool -> model returns `FunctionCall` -> execute -> send `FunctionResponse` with matching `id` -> repeat.

## Grounding (Google Search)

| Term | Role | Key Detail |
|------|------|------------|
| `google_search` | Current tool | Grounding via Google Search for all current models |
| `google_search_retrieval` | Legacy tool | For older model versions |
| `grounding_metadata` | Response object | Contains search info + citations |

### Grounding Metadata Fields

| Field | Content |
|-------|---------|
| `groundingChunks` | Array of web sources: `{uri, title}` |
| `groundingSupports` | Links response text segments to `groundingChunks` citations |
| `webSearchQueries` | Array of search queries used (debugging) |
| `searchEntryPoint` | HTML/CSS for rendering required Search Suggestions UI |

**Rule**: When using grounding, you must render `searchEntryPoint` per Google's terms of service.

## Cross-Provider Alignment

| Concept | Google | Anthropic | OpenAI |
|---------|--------|-----------|--------|
| Tool def | `FunctionDeclaration` | `tool` | `tool` > `function` |
| Invocation | `FunctionCall` | `tool_use` block | `tool_calls` array |
| Result | `FunctionResponse` (id match) | `tool_result` (tool_use_id) | tool msg (tool_call_id) |
| Selection | `mode`: AUTO/ANY/NONE | `tool_choice`: auto/any/tool/none | `tool_choice`: auto/none/required |
| Web search | `google_search` grounding | `web_search_20260209` server tool | No native |
| Schema | JSON Schema in `parameters` | JSON Schema in `input_schema` | JSON Schema in `parameters` |

## Golden Rules
- Google uses PascalCase naming (FunctionDeclaration, FunctionCall) vs camelCase/snake_case elsewhere
- `id` field in FunctionCall/FunctionResponse must match -- mismatches cause silent failures
- `allowed_function_names` only works with `ANY` or `VALIDATED` modes, not `AUTO`
- Grounding requires rendering `searchEntryPoint` HTML (ToS requirement)
- No explicit prompt caching -- Google handles KV cache internally

## Flow
```text
[FunctionDeclaration in Tool] -> [Set tool_config mode] -> [Model returns FunctionCall] -> [Execute + FunctionResponse] -> [Repeat]
```

## References
- Origin: src_provider_taxonomy.md (Provider Official Taxonomy)
- Function Calling: /gemini-api/docs/function-calling
- Grounding: /gemini-api/docs/grounding

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.35 |
| [[p01_kc_terminology_google_mcp_canonical]] | sibling | 0.34 |
| [[p01_kc_openai_api_patterns]] | sibling | 0.34 |
| [[p01_kc_terminology_openai_canonical]] | sibling | 0.32 |
| [[p01_kc_anthropic_api_patterns]] | sibling | 0.31 |
| [[p01_kc_function_def]] | sibling | 0.28 |
| [[p01_kc_terminology_anthropic_canonical]] | sibling | 0.28 |
| [[bld_collaboration_search_tool]] | downstream | 0.27 |
| [[bld_knowledge_card_function_def]] | sibling | 0.27 |
| [[bld_collaboration_function_def]] | downstream | 0.26 |
