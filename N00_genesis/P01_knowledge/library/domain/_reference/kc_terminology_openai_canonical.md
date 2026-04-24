---
id: p01_kc_terminology_openai_canonical
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "OpenAI Official Terminology: Canonical Vocabulary (2026)"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: N01_intelligence
domain: terminology
origin: src_provider_taxonomy
quality: 9.1
tags: [terminology, openai, canonical, agents-sdk, assistants, function-calling, structured-outputs, permanent]
tldr: "Complete canonical vocabulary from OpenAI's official docs. Every term is the EXACT name OpenAI uses. Covers Chat Completions, Assistants API, Agents SDK, Structured Outputs, Evals, and Responses API."
when_to_use: "When building CEX kinds for OpenAI features, comparing OpenAI vs Anthropic terminology, or validating naming in OpenAI-facing artifacts."
keywords: [openai, gpt, agents-sdk, assistants, function-calling, structured-outputs, evals, responses-api]
long_tails:
  - "openai official API term names function calling tool_calls structured outputs"
  - "what does openai call agents vs assistants vs swarm"
axioms:
  - "OpenAI has TWO agent systems: Assistants API (hosted) and Agents SDK (open-source). Terms differ."
  - "Responses API is the newest API surface — may supersede Chat Completions for agentic use"
feeds_kinds: [function_def, code_executor, search_tool, response_format, input_schema, system_prompt]
linked_artifacts:
  related:
    - P01_knowledge/library/domain/_reference/kc_openai_api_patterns.md
    - P01_knowledge/library/domain/_reference/kc_terminology_rosetta_stone.md
density_score: 0.92
related:
  - p01_kc_openai_api_patterns
  - p01_kc_terminology_anthropic_canonical
  - p01_kc_terminology_rosetta_stone
  - p01_kc_function_def
  - p01_kc_terminology_google_mcp_canonical
  - atom_03_openai_agents_sdk
  - bld_collaboration_function_def
  - p04_function_def_NAME
  - p01_kc_anthropic_api_patterns
  - bld_knowledge_card_function_def
---

# OpenAI Canonical Terminology

## Source
- **Primary**: platform.openai.com/docs (API Reference, Guides)
- **Agents SDK**: github.com/openai/openai-agents-python
- **Version**: API v2 (2025+), Agents SDK 0.1+

---

## API Surfaces (3 distinct systems)

| Official Name | Purpose | Status |
|---------------|---------|--------|
| **Chat Completions API** | Stateless chat/completion | Stable, primary |
| **Assistants API** | Stateful agents with threads | Stable, hosted |
| **Responses API** | Next-gen agentic API | Newer, converging |
| **Agents SDK** | Open-source agent framework | Python SDK |

> **Critical distinction**: Assistants API = hosted runtime (OpenAI manages state). Agents SDK = local framework (developer manages state). Terms differ between them.

## Chat Completions Terms

| Official Term | Category | Definition |
|---------------|----------|------------|
| **model** | Parameter | Model identifier (e.g., `gpt-4o`, `o3-mini`) |
| **messages** | Parameter | Array of message objects with `role` and `content` |
| **role** | Message field | `system`, `user`, `assistant`, `tool`, `developer` |
| **developer** | Role | New role replacing `system` in some contexts (Responses API) |
| **tools** | Parameter | Array of tool objects |
| **tool_calls** | Response field | Array of model tool invocations |
| **tool_choice** | Parameter | `auto`, `none`, `required`, or specific function |
| **parallel_tool_calls** | Parameter | Boolean enabling simultaneous tool calls |
| **response_format** | Parameter | Controls output structure |
| **max_tokens** / **max_completion_tokens** | Parameter | Response length limit |
| **temperature** | Parameter | Randomness (0–2) |
| **top_p** | Parameter | Nucleus sampling |
| **frequency_penalty** / **presence_penalty** | Parameter | Token repetition controls |
| **logprobs** | Parameter | Return token log probabilities |
| **stop** | Parameter | Stop sequences |
| **stream** | Parameter | Enable SSE streaming |
| **n** | Parameter | Number of completions |
| **seed** | Parameter | Deterministic sampling seed |

## Function Calling / Tool Use Terms

| Official Term | What It Is | Key Detail |
|---------------|-----------|------------|
| **tool** | Top-level object | `{type: "function", function: {name, description, parameters}}` |
| **function** | Nested object | Contains `name`, `description`, `parameters`, `strict` |
| **parameters** | Schema field | JSON Schema for function inputs (NOT `input_schema` — that's Anthropic) |
| **tool_calls** | Response array | Each entry: `{id, type: "function", function: {name, arguments}}` |
| **arguments** | String field | JSON string (NOT parsed object) — must JSON.parse() |
| **tool_call_id** | Message field | Required in tool-role message to match invocation |
| **tool_choice: "auto"** | Default | Model decides |
| **tool_choice: "required"** | Force | MUST call a tool (≠ Anthropic's `any`) |
| **tool_choice: "none"** | Disable | No tool use |
| **tool_choice: {type, function}** | Specific | Force specific function |
| **strict: true** | Function field | Enables Structured Outputs for tool calls |
| **finish_reason: "tool_calls"** | Response signal | Generation stopped for tool invocation |

> **Key difference vs Anthropic**: OpenAI wraps function inside tool object. Anthropic puts schema directly on tool.

## Structured Outputs Terms

| Official Term | What It Is |
|---------------|-----------|
| **Structured Outputs** | Feature name (capitalized, two words) |
| **response_format** | Parameter: `{type: "json_schema", json_schema: {...}}` |
| **json_schema** | Schema wrapper with `name`, `schema`, `strict` |
| **strict: true** | Guarantees 100% schema adherence |
| **refusal** | Response field when model refuses structured generation |
| **json_object** | Simpler mode: `{type: "json_object"}` (less strict) |

## Assistants API Terms

| Official Term | What It Is | Key Detail |
|---------------|-----------|------------|
| **Assistant** | Persistent agent | Has `instructions`, `tools`, `model`, `file_ids` |
| **Thread** | Conversation container | Persistent message history |
| **Run** | Execution instance | One assistant processing one thread |
| **Run Step** | Execution step | Individual action within a run |
| **Message** | Thread entry | User or assistant message with content |
| **File** | Upload | Attached to assistant or thread |
| **VectorStore** | Knowledge base | Stores embeddings for file_search |
| **file_search** | Built-in tool | RAG over uploaded files |
| **code_interpreter** | Built-in tool | Sandboxed Python execution |
| **function** | Custom tool | Developer-defined function |
| **required_action** | Run state | Indicates pending tool calls |
| **tool_outputs** | Submission | Developer submits tool results |
| **truncation_strategy** | Thread config | How to handle context overflow |

> **"code_interpreter"** is OpenAI's term. Anthropic says "code_execution". Google says "code_execution". CEX uses "code_executor".

## Agents SDK Terms

| Official Term | What It Is | Key Detail |
|---------------|-----------|------------|
| **Agent** | Core class | `Agent(name, instructions, tools, handoffs, guardrails)` |
| **handoff** | Delegation | `handoff()` function to transfer control between agents |
| **Guardrail** | Safety check | `InputGuardrail` / `OutputGuardrail` classes |
| **Runner** | Execution engine | `Runner.run(agent, input)` |
| **RunResult** | Output | Contains `output`, `final_agent`, `new_items` |
| **tool** | Decorator | `@function_tool` decorator for Python functions |
| **hosted_tool** | Built-in | `WebSearchTool`, `FileSearchTool`, `CodeInterpreterTool` |
| **tracing** | Observability | Built-in trace collection |
| **context** | State object | Passed to tools and guardrails |
| **output_type** | Schema | Pydantic model for structured agent output |

## Responses API Terms

| Official Term | What It Is |
|---------------|-----------|
| **Responses API** | Newer API surface (replaces some Chat Completions use cases) |
| **input** | Replaces `messages` in some contexts |
| **output** | Typed response items |
| **instructions** | Replaces `system` message |
| **tools** | Same semantics as Chat Completions |
| **web_search** | Built-in tool type |
| **file_search** | Built-in tool type |
| **code_interpreter** | Built-in tool type |
| **computer_use** | Built-in tool type (adopted from Anthropic) |

## Evals Terms

| Official Term | What It Is |
|---------------|-----------|
| **Eval** | Evaluation definition |
| **Run** | One evaluation execution |
| **CompletionResult** | Model output being evaluated |
| **Grader** | Scoring function (model, string, Python) |
| **TestingCriteria** | Pass/fail rules |

## Model Naming Convention

| Pattern | Example | Meaning |
|---------|---------|---------|
| `gpt-{generation}{variant}` | `gpt-4o` | Generation 4, optimized variant |
| `o{n}` / `o{n}-mini` | `o3-mini` | Reasoning models |
| Date suffix | `gpt-4o-2024-11-20` | Specific snapshot |
| `-latest` suffix | `gpt-4o-latest` | Newest snapshot alias |

## Terms OpenAI Does NOT Use

| ❌ Don't Say | ✅ OpenAI Says | Why |
|-------------|----------------|-----|
| tool_use (block type) | tool_calls (array) | Different response structure |
| input_schema | parameters | OpenAI's JSON Schema field name |
| extended thinking | reasoning (o-series) | Different model capability |
| computer use | computer_use (Responses API only) | Adopted but different context |
| content blocks | message content | OpenAI uses flat content, not block array |
| cache_control | automatic caching | No explicit cache control |
| ephemeral | N/A | Anthropic's cache concept |
| nucleus (N01-N07) | agent (Agents SDK) | CEX-specific term |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_openai_api_patterns]] | sibling | 0.51 |
| [[p01_kc_terminology_anthropic_canonical]] | sibling | 0.43 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.33 |
| [[p01_kc_function_def]] | sibling | 0.32 |
| [[p01_kc_terminology_google_mcp_canonical]] | sibling | 0.31 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.30 |
| [[bld_collaboration_function_def]] | downstream | 0.29 |
| [[p04_function_def_NAME]] | downstream | 0.29 |
| [[p01_kc_anthropic_api_patterns]] | sibling | 0.27 |
| [[bld_knowledge_card_function_def]] | sibling | 0.26 |
