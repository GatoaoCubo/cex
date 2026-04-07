---
id: p01_kc_function_def
kind: knowledge_card
type: kind
pillar: P01
title: "Function Def — Deep Knowledge for function_def"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: function_def
quality: 9.1
tags: [function_def, P04, CALL, kind-kc, tool-use]
tldr: "JSON Schema definition of a callable function that an LLM invokes via tool_use — the universal tool interface across OpenAI, Anthropic, and all major frameworks"
when_to_use: "Building, reviewing, or reasoning about function_def artifacts"
keywords: [function, tool, json-schema, tool-use, callable]
feeds_kinds: [function_def]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Function Def

## Spec
```yaml
kind: function_def
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_fn_{{name}}.md + .json
core: true
```

## What It Is
A function_def is the JSON Schema declaration of a callable function that an LLM requests via tool_use. It contains name, description, and a parameters schema (JSON Schema draft-07). It is the schema layer — it declares what the LLM can call. It is NOT an mcp_server (which is a full protocol server exposing multiple tools with protocol handshake), NOT an api_client (which is the runtime implementation that makes the actual HTTP call after the LLM invokes the function).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | BaseTool, StructuredTool, @tool decorator | Pydantic args_schema compiles to JSON Schema |
| LlamaIndex | FunctionTool, QueryEngineTool | fn_schema auto-generated from signature |
| CrewAI | Tool(name, description, func) | Simpler schema; less strict than OpenAI |
| DSPy | dspy.Tool, Signature fields | Typed via Python type hints |
| Haystack | ComponentBase with @component | Component IO schema; not tool_use native |
| OpenAI | tools[].function in ChatCompletion | Canonical JSON Schema tool definition |
| Anthropic | tools[].input_schema in tool_use | JSON Schema; name + description + schema |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| strict | bool | false | True = LLM must match schema exactly |
| required_fields | list | [] | More required = less hallucination risk |
| description_quality | str | concise | Longer = better LLM routing accuracy |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Single-action tool | One clear capability | search_web(query: str) -> results |
| Enum-constrained param | Fixed option set | action: Literal["get","post","delete"] |
| Nested schema | Complex structured input | filters: {type, value, operator} |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Vague description | LLM misroutes or skips tool entirely | Add concrete usage examples in description |
| Too many parameters | LLM omits optional fields silently | Split into focused single-purpose sub-tools |
| No required array | LLM sends empty or partial calls | Always define required field list explicitly |

## Integration Graph
```
[LLM prompt + tool_choice] --> [function_def schema] --> [tool_call request]
                                       |                         |
                           [JSON Schema validation]       [api_client / handler]
```

## Decision Tree
- IF need full protocol with resources + tools THEN use mcp_server
- IF need runtime HTTP client implementation THEN use api_client
- IF function set is large and versioned THEN use mcp_server over bare function_defs
- DEFAULT: function_def for any single LLM-callable function declaration

## Quality Criteria
- GOOD: name, description, parameters schema, required list all present
- GREAT: strict mode, enum constraints, example in description, handler unit-tested
- FAIL: missing required array, generic parameter names (arg1, data), no description
