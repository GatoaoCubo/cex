---
id: n00_search_tool_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Search Tool -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, search_tool, p04, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A search_tool provides agents with web, semantic, or hybrid search capabilities through external providers (Tavily, Serper, Brave, Perplexity), returning ranked results with snippets and source URLs. It abstracts the provider API into a standardized tool interface with query normalization, result deduplication, and citation formatting. The output is a search capability that agents call during F5 CALL to retrieve current external information not in the local knowledge base.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `search_tool` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider | string | yes | Backend provider: tavily, serper, brave, perplexity, bing |
| search_type | string | yes | web, news, academic, or semantic |
| max_results | integer | yes | Number of results returned per query |
| include_raw_content | boolean | no | Whether to return full page content or just snippet |

## When to use
- When an agent needs current web information beyond its training data cutoff
- When N01 Intelligence performs competitive research requiring live web sources
- When the research_pipeline RETRIEVE stage needs external web data collection

## Builder
`archetypes/builders/search_tool-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind search_tool --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: st_tavily_web_search
kind: search_tool
pillar: P04
nucleus: n01
title: "Tavily Web Search Tool"
version: 1.0
quality: null
---
provider: tavily
search_type: web
max_results: 10
include_raw_content: false
```

## Related kinds
- `browser_tool` (P04) -- deeper alternative for dynamic pages that search_tool cannot access
- `search_strategy` (P04) -- strategy that governs how search_tool is called across passes
- `retriever` (P04) -- local knowledge retriever that complements search_tool for internal docs
- `research_pipeline` (P04) -- pipeline that orchestrates search_tool in the RETRIEVE stage
