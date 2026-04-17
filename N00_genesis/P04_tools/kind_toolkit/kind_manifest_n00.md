---
id: n00_toolkit_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Toolkit -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, toolkit, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A toolkit is a curated collection of callable tools with auto-generated JSON Schema that an agent receives as its complete tool environment. It bundles related function_defs, api_clients, and cli_tools into a named, versioned package that can be assigned to a nucleus at boot. The output is a tool bundle specification with automatic schema generation that ensures every tool the agent has access to is properly typed and documented.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `toolkit` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| tools | list | yes | List of tool IDs included in this toolkit |
| auto_schema | boolean | yes | Whether JSON Schema is auto-generated from tool definitions |
| nucleus_affinity | list | no | Which nuclei this toolkit is designed for |
| max_parallel_calls | integer | no | Maximum concurrent tool calls the agent may make |

## When to use
- When assigning a complete tool environment to a nucleus at boot
- When building the F5 CALL context for a nucleus by defining which tools it has access to
- When registering a toolkit with an MCP server so LLMs can discover available capabilities

## Builder
`archetypes/builders/toolkit-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind toolkit --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: tk_n01_intelligence_tools
kind: toolkit
pillar: P04
nucleus: n01
title: "N01 Intelligence Toolkit"
version: 1.0
quality: null
---
auto_schema: true
nucleus_affinity: [n01]
max_parallel_calls: 5
tools:
  - st_tavily_web_search
  - ret_cex_tfidf_local
  - dl_pdf_semantic_chunker
  - ct_git_ops
```

## Related kinds
- `function_def` (P04) -- individual tool definitions bundled in this toolkit
- `mcp_server` (P04) -- server that exposes the toolkit to LLM clients
- `capability_registry` (P08) -- registry that indexes all available toolkits
- `agent` (P02) -- agent definition that references the toolkit for its tool environment
