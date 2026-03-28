---
kind: examples
id: bld_examples_function_def
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of function_def artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: function-def-builder
## Golden Example
INPUT: "Create function definition for web search that LLMs can call"
OUTPUT:
```yaml
id: p04_fn_search_web
kind: function_def
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "EDISON"
name: "search_web"
description: "Search the web for current information. Call when the user asks about recent events, needs factual data you lack, or requests information that may have changed since your training cutoff."
parameters:
  type: object
  properties:
    query:
      type: string
      description: "Search query — use natural language, be specific"
    max_results:
      type: integer
      description: "Maximum results to return"
      default: 5
    language:
      type: string
      description: "Language code for results"
      enum: ["en", "pt", "es", "fr", "de"]
      default: "en"
  required: ["query"]
returns:
  type: array
  items:
    type: object
    properties:
      title: {type: string}
      url: {type: string}
      snippet: {type: string}
  description: "Array of search results with title, URL, and snippet"
provider_compat: [openai, anthropic, gemini, bedrock]
strict: false
quality: null
tags: [function_def, search, web, P04]
tldr: "Web search function: query + max_results + language params, returns ranked results array"
examples:
  - input: {query: "latest Claude model release date", max_results: 3}
    output: [{title: "Anthropic launches...", url: "https://...", snippet: "..."}]
error_types: [rate_limit, invalid_query, provider_unavailable]
```
## Overview
Searches the web for current information using a search provider.
Call when user asks about recent events, needs facts beyond training data, or requests time-sensitive information.
## Parameters
### query
Type: string | Required: yes | Default: none
The search query in natural language. Be specific — "Claude 4 release date" not "Claude info".
### max_results
Type: integer | Required: no | Default: 5
Maximum number of results to return. Range 1-20.
### language
Type: string | Required: no | Default: "en"
Language code for results. Enum: en, pt, es, fr, de.
## Returns
Type: array of objects
Each result: {title: string, url: string, snippet: string}
Ordered by relevance. Empty array if no results found.
## Examples
### Example 1: Basic search
Input: `{"query": "Claude 4 release date", "max_results": 3}`
Output: `[{"title": "Anthropic launches Claude 4", "url": "...", "snippet": "Released March 2026..."}]`
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_fn_ pattern (H02 pass)
- kind: function_def (H04 pass)
- parameters is valid JSON Schema with type: object (H06 pass)
- returns has type and structure (H07 pass)
- description is LLM-facing — explains WHEN to call (S01 pass)
- All required frontmatter present (H06 pass)
- Examples with concrete input/output (S06 pass)
- Provider-agnostic core schema (S04 pass)
## Anti-Example
INPUT: "Create function for searching"
BAD OUTPUT:
```yaml
id: search
kind: tool
name: Search
description: Searches things
parameters:
  query: string
quality: 8.5
tags: [search]
```
FAILURES:
1. id: "search" has no `p04_fn_` prefix -> H02 FAIL
2. kind: "tool" not "function_def" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. parameters not valid JSON Schema (missing type: object, properties) -> H06 FAIL
5. Missing fields: returns, version, created, pillar, tldr -> H06 FAIL
6. description: "Searches things" — vague, LLM cannot decide when to call -> S01 FAIL
7. tags: only 1 item, missing "function_def" -> S02 FAIL
8. No body sections (Overview, Parameters, Returns, Examples) -> H07 FAIL
9. No examples with input/output -> S06 FAIL
