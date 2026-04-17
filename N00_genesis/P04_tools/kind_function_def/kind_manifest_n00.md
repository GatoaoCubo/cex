---
id: n00_function_def_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Function Def -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, function_def, p04, n00, archetype, template]
density_score: 0.97
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A function_def is an LLM-callable function definition using JSON Schema that exposes a capability as a tool the model can invoke during generation. It specifies the function name, description, parameter schema, and return format so the LLM knows exactly when and how to call it. The output is a tool specification compatible with OpenAI function calling, Anthropic tool use, and MCP tool protocols.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `function_def` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| function_name | string | yes | Exact function name the LLM uses in tool_use blocks |
| description | string | yes | Natural language description of what the function does |
| parameters | object | yes | JSON Schema object describing input parameters |
| return_schema | object | no | JSON Schema describing the expected return value |

## When to use
- When wrapping any capability (API, CLI, database) as an LLM-callable tool
- When building the toolkit for a nucleus and each capability needs a typed function_def
- When registering tools with an MCP server that exposes them to Claude or other LLMs

## Builder
`archetypes/builders/function_def-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind function_def --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: fd_search_web
kind: function_def
pillar: P04
nucleus: n01
title: "Web Search Function"
version: 1.0
quality: null
---
function_name: search_web
description: "Search the web for current information on a topic. Returns top 5 results."
parameters:
  type: object
  properties:
    query:
      type: string
      description: "The search query"
    max_results:
      type: integer
      description: "Number of results to return (1-10)"
  required: [query]
```

## Related kinds
- `toolkit` (P04) -- collection that bundles multiple function_defs for an agent
- `mcp_server` (P04) -- server that registers function_defs as MCP-compatible tools
- `api_client` (P04) -- the implementation that function_def wraps as an LLM-callable interface
- `action_paradigm` (P04) -- execution loop that invokes function_defs in the action space
