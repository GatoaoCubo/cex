---
kind: knowledge_card
id: bld_knowledge_card_function_def
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for function_def production — LLM function calling specification
sources: OpenAI function calling docs, Anthropic tool_use docs, JSON Schema spec
---

# Domain Knowledge: function_def
## Executive Summary
Function definitions are JSON Schema specifications that describe callable functions for LLMs. They are the universal interface between an LLM and external capabilities. Every major provider (OpenAI, Anthropic, Gemini, Bedrock) uses JSON Schema to describe function parameters, with minor variations in envelope format. The function_def artifact captures the provider-agnostic schema.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Schema format | JSON Schema (draft-07 compatible) |
| Parameter types | string, number, integer, boolean, array, object |
| Required field | Array of required property names |
| Description | LLM-facing — explains WHEN to call, not just what it does |
## Provider Mapping
| Provider | Envelope | Params Key | Description Key |
|----------|----------|-----------|----------------|
| OpenAI | functions[].function | parameters | description |
| Anthropic | tools[] | input_schema | description |
| Gemini | FunctionDeclaration | parameters (OpenAPI) | description |
| Bedrock | toolSpec | inputSchema.json | description |
## Patterns
- **Verb-noun naming**: `search_web`, `get_weather`, `create_ticket` — clear action + target
- **Flat parameters**: prefer flat objects over deep nesting — LLMs handle flat schemas better
- **Enum constraints**: use enum for finite option sets — reduces hallucination
- **Required vs optional**: mark truly needed params as required; provide defaults for optional

| Pattern | Example | When to use |
|---------|---------|-------------|
| Simple function | `get_weather(location)` | Single-purpose lookup |
| Multi-param | `search_web(query, max_results, lang)` | Configurable search |
| Nested object | `create_ticket(title, metadata: {priority, labels})` | Complex structured input |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No description | LLM cannot decide when to call the function |
| Vague description ("does stuff") | LLM picks wrong function or invents parameters |
| Deep nesting (>2 levels) | LLMs lose accuracy on deeply nested schemas |
| Missing required array | All params treated as optional, LLM omits critical fields |
| Provider-specific fields in core | Breaks portability across providers |
| Implementation in spec | This is an interface contract, not a code file |
## Application
1. Name the function: verb_noun, snake_case, clear action
2. Write description for the LLM: when should it call this? what problem does it solve?
3. Define parameters as JSON Schema: type, properties, required, descriptions
4. Specify return type and structure
5. Add 2+ examples with concrete input/output
6. Test: does the description alone tell the LLM when to use this?
## References
- JSON Schema: draft-07 specification
- OpenAI: function calling documentation
- Anthropic: tool use documentation
- Gemini: FunctionDeclaration API reference
- Bedrock: toolSpec API reference
