---
id: p01_kc_openai_api_patterns
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: 'OpenAI API Patterns: Function Calling, Structured Outputs, Assistants, Evals'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: openai_api
origin: src_provider_taxonomy
quality: 9.1
tags:
- openai
- function-calling
- structured-outputs
- assistants
- evals
- knowledge
tldr: OpenAI API patterns covering function calling (tool wrappers), structured outputs (json_schema enforcement), Assistants
  API (persistent threads/runs), and Evals framework.
when_to_use: When building with OpenAI APIs, comparing OpenAI vs Anthropic tool patterns, or implementing structured output
  guarantees.
keywords:
- openai
- function_calling
- structured_outputs
- assistants_api
- evals
long_tails:
- how does openai function calling compare to anthropic tool use
- openai structured outputs strict mode json schema
axioms:
- OpenAI wraps functions inside tool objects; Anthropic uses tool objects directly
feeds_kinds:
- function_def
- input_schema
- response_format
- system_prompt
- search_tool
- code_executor
- vision_tool
linked_artifacts:
  adw: null
  agent: null
  hop: null
density_score: 0.9
related:
  - p01_kc_terminology_openai_canonical
  - p01_kc_terminology_rosetta_stone
  - p01_kc_anthropic_api_patterns
  - bld_collaboration_function_def
  - p01_kc_function_def
  - p01_kc_terminology_anthropic_canonical
  - p01_kc_google_ai_patterns
  - bld_knowledge_card_function_def
  - atom_15_qwen_deepseek
  - function-def-builder
---

# KC-Domain: OpenAI API Patterns

## Quick Reference
```yaml
topic: OpenAI API (platform.openai.com)
scope: Function calling, structured outputs, Assistants API, Evals
owner: builder_agent
criticality: high
```

## Function Calling

| Term | Role | Key Detail |
|------|------|------------|
| `tool` | Request wrapper | `{"type": "function", "function": {name, description, parameters}}` |
| `tool_choice` | Selection control | `"auto"` / `"none"` / `"required"` / `{"type": "function", "function": {"name": "..."}}` |
| `tool_calls` | Response array | Each entry: `id`, `type`, `function` with `name` + `arguments` (JSON string) |
| `parallel_tool_calls` | Boolean param | Enables multiple simultaneous calls (default: true) |
| `strict` | Function field | Enforces strict JSON Schema adherence in tool calls |
| `tool_call_id` | Message field | Required in tool result messages to match invocation |

**Loop**: User -> model returns `tool_calls` -> developer executes -> sends tool role message with `tool_call_id` -> repeat.

## Structured Outputs

| Term | Role | Key Detail |
|------|------|------------|
| `response_format` | Request param | `{"type": "json_schema", "json_schema": {...}}` |
| `strict: true` | Schema field | Guarantees 100% schema compliance |
| `refusal` | Response field | Present when model refuses structured generation |
| `json_object` | Legacy format | Valid JSON but no schema enforcement |

**Rule**: `json_schema` + `strict: true` = deterministic schema conformance. Always prefer over `json_object`.

## Assistants API

| Term | Role | Key Detail |
|------|------|------------|
| `Assistant` | Persistent entity | Instructions + model + tools configured once |
| `Thread` | Conversation | Persists independently of runs; holds messages |
| `Run` | Execution | Stateful lifecycle: queued -> in_progress -> completed |
| `Run Step` | Sub-operation | Types: `message_creation`, `tool_calls` |
| `code_interpreter` | Built-in tool | Sandboxed Python execution |
| `file_search` | Built-in tool | Vector search over uploaded files via `vector_store` |
| `vector_store` | Storage | Embeddings for file_search |

**Pattern**: Create Assistant -> Create Thread -> Add Message -> Create Run -> Poll/Stream -> Get result.

## Evals Framework

| Term | Role | Key Detail |
|------|------|------------|
| `eval` | Resource | Evaluation config with data source + testing criteria |
| `testing_criteria` | Grader array | `string_check`, `text_similarity`, `model_graded_rubric`, `model_graded_factuality` |
| `run` | Execution | Eval execution against a dataset |

## Cross-Provider Alignment

| Concept | OpenAI | Anthropic Equivalent |
|---------|--------|---------------------|
| `tool` wrapper | `{"type": "function", ...}` | `tool` object directly |
| Selection | `tool_choice: "required"` | `tool_choice: {type: "any"}` |
| Result | tool role + `tool_call_id` | `tool_result` + `tool_use_id` |
| Structured | `response_format` + `json_schema` | No native equivalent (use tool output) |
| Threads | Server-side persistent | Client-side messages array |
| Code exec | `code_interpreter` | `code_execution` server tool |

## Golden Rules
- OpenAI `tool_calls[].function.arguments` is a JSON **string**, not object -- must parse
- `strict: true` works on both function calling AND structured outputs
- Assistants API is server-stateful (threads persist); Anthropic is client-stateful (messages array)
- `parallel_tool_calls` defaults true; disable for sequential-dependent operations

## Flow
```text
[Define tools] -> [Send request] -> [Parse tool_calls] -> [Execute functions] -> [Return results with tool_call_id]
```

## References
- Origin: src_provider_taxonomy.md (Provider Official Taxonomy)
- OpenAI Function Calling: /docs/guides/function-calling
- OpenAI Structured Outputs: /docs/guides/structured-outputs
- OpenAI Assistants: /docs/assistants/overview
- OpenAI Evals: /docs/guides/evals

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_terminology_openai_canonical]] | sibling | 0.58 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.34 |
| [[p01_kc_anthropic_api_patterns]] | sibling | 0.34 |
| [[bld_collaboration_function_def]] | downstream | 0.33 |
| [[p01_kc_function_def]] | sibling | 0.32 |
| [[p01_kc_terminology_anthropic_canonical]] | sibling | 0.30 |
| [[p01_kc_google_ai_patterns]] | sibling | 0.28 |
| [[bld_knowledge_card_function_def]] | sibling | 0.27 |
| [[atom_15_qwen_deepseek]] | sibling | 0.26 |
| [[function-def-builder]] | downstream | 0.26 |
