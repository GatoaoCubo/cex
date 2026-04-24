---
id: p04_fn_search_web
kind: function_def
8f: F6_produce
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: search_web
description: "Search the web and return ranked results with titles, URLs, and snippets"
parameters:
  type: object
  properties:
    query:
      type: string
      description: "The search query string"
    max_results:
      type: number
      description: "Maximum number of results to return"
    search_type:
      type: string
      description: "Type of search to perform"
      enum: [general, news, images, academic]
  required: [query]
returns:
  type: array
  description: "Array of search result objects with title, url, snippet, and score"
provider_compat: [openai, anthropic, gemini, bedrock]
strict: false
domain: web-search
quality: 9.1
tags: [function_def, search, web, tool_use]
tldr: "OpenAI-compatible function def for web search with query, max_results, and search_type params"
examples:
  - input: {"query": "best practices for RAG pipelines"}
    output: "[{title: '...', url: '...', snippet: '...', score: 0.95}]"
error_types: [rate_limit_exceeded, invalid_query, timeout]
title: "Function Def Search Web"
density_score: 0.9
related:
  - bld_examples_function_def
  - p04_search_tavily
  - p01_kc_academic_rag_patterns
  - bld_knowledge_card_agentic_rag
  - ex_knowledge_card_rag_fundamentals
  - bld_collaboration_search_tool
  - bld_output_template_search_tool
  - bld_examples_search_tool
  - bld_tools_agentic_rag
  - bld_output_template_function_def
---

# Web Search Function Definition

## Overview
Defines a callable function for LLM tool_use that performs web searches and returns structured results. An LLM calls this function when it needs real-time information not available in its training data.

## Parameters
### query
Type: string | Required: yes | Default: none
The user's search query. Supports natural language and quoted exact-match phrases. Max 400 characters.

### max_results
Type: number | Required: no | Default: 5
Number of results to return, between 1 and 20. Higher values increase latency and token usage.

### search_type
Type: string | Required: no | Default: general
Enum: [general, news, images, academic]
Controls which index to search. `news` limits to last 7 days. `academic` prioritizes scholarly sources.

## Returns
Type: array of objects
Structure: Each object contains `title` (string), `url` (string), `snippet` (string, max 200 chars), `score` (float 0-1).
Example:
```json
[
  {"title": "RAG Best Practices 2026", "url": "https://example.com/rag", "snippet": "Retrieval-augmented generation...", "score": 0.95}
]
```

## Examples
### Example 1: General web search
Input:
```json
{"query": "best practices for RAG pipelines", "max_results": 3}
```
Output:
```json
[
  {"title": "Building Production RAG", "url": "https://example.com/rag-prod", "snippet": "Key patterns for reliable RAG: chunk sizing, hybrid retrieval, reranking...", "score": 0.97},
  {"title": "RAG Pipeline Design", "url": "https://example.com/rag-design", "snippet": "A comprehensive guide to designing retrieval-augmented generation...", "score": 0.92},
  {"title": "Evaluating RAG Systems", "url": "https://example.com/rag-eval", "snippet": "Metrics and frameworks for measuring RAG quality and relevance...", "score": 0.88}
]
```

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `function def`
- **Artifact ID**: `p04_fn_search_web`
- **Tags**: [function_def, search, web, tool_use]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `function def` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_function_def]] | downstream | 0.47 |
| [[p04_search_tavily]] | related | 0.32 |
| [[p01_kc_academic_rag_patterns]] | upstream | 0.28 |
| [[bld_knowledge_card_agentic_rag]] | upstream | 0.27 |
| [[ex_knowledge_card_rag_fundamentals]] | upstream | 0.26 |
| [[bld_collaboration_search_tool]] | downstream | 0.26 |
| [[bld_output_template_search_tool]] | downstream | 0.26 |
| [[bld_examples_search_tool]] | downstream | 0.25 |
| [[bld_tools_agentic_rag]] | related | 0.25 |
| [[bld_output_template_function_def]] | downstream | 0.25 |
