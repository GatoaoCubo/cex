---
kind: quality_gate
id: p11_qg_function_def
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of function_def artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: function_def"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, function-def, P04, json-schema, tool-calling, parameters]
tldr: "Pass/fail gate for function_def artifacts: valid JSON Schema parameters, LLM-facing description, return type, and provider compatibility."
domain: "JSON Schema function definitions callable by LLMs via tool_use/function_calling"
created: "2026-03-28"
updated: "2026-03-28"
density_score: 0.90
related:
  - bld_examples_function_def
  - bld_instruction_function_def
  - p03_sp_function_def_builder
  - p11_qg_search_tool
  - bld_output_template_function_def
  - p11_qg_chunk_strategy
  - p11_qg_vision_tool
  - p11_qg_retriever_config
  - p11_qg_constraint_spec
  - bld_schema_function_def
---

## Quality Gate

# Gate: function_def
## Definition
| Field | Value |
|---|---|
| metric | function_def artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: function_def` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_fn_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, spaces, or no p04_fn_ prefix |
| H03 | ID equals filename stem | `id: p04_fn_search` but file is `other_search.md` |
| H04 | Kind equals literal `function_def` | `kind: tool` or `kind: function` or any other value |
| H05 | Quality field is null | `quality: 7.5` or any non-null value |
| H06 | All required fields present | Missing `parameters`, `returns`, `description`, or `name` |
| H07 | Parameters is valid JSON Schema | parameters missing type: object, or invalid schema structure |
| H08 | Returns has type defined | Returns field missing or has no type specification |
| H09 | Description is non-empty and >= 20 chars | Empty or trivially short description |
| H10 | Body has required sections | Missing Overview, Parameters, Returns, or Examples section |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Description quality | 1.5 | LLM-facing, explains WHEN to call, specific enough to differentiate |
| Parameter documentation | 1.0 | Each param has type, required status, default, and description |
| Return type clarity | 1.0 | Return structure documented with type and example value |
| Example completeness | 1.0 | 2+ examples with concrete input/output pairs |
| Provider compatibility | 0.5 | Tested against target providers, compat list accurate |
| Enum usage | 0.5 | Finite option sets use enum constraints |
| Nesting depth | 0.5 | Parameters <= 2 levels deep |
| Error documentation | 0.5 | Error types listed with conditions |
| Naming convention | 0.5 | Function name is verb_noun, snake_case |
| Boundary clarity | 1.0 | Explicitly not an mcp_server, api_client, or code_executor |
| Domain specificity | 1.0 | Parameters and returns specific to the declared function purpose |
| Schema correctness | 1.0 | JSON Schema is valid, required array matches actual required params |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal test function used only during development |
| approver | Author self-certification with debug-only scope comment |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — test functions must be promoted or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates corrupt metrics) |

## Examples

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
author: "builder_agent"
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
quality: 8.8
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
