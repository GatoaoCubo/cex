---
kind: examples
id: bld_examples_input_schema
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of input_schema artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Input Schema"
version: "1.0.0"
author: n03_builder
tags: [input_schema, builder, examples]
tldr: "Golden and anti-examples for input schema construction, demonstrating ideal structure and common pitfalls."
domain: "input schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: input-schema-builder
## Golden Example
INPUT: "Define o input schema para o brain_query — what precisa receber para searchr"
OUTPUT:
```yaml
id: p06_is_brain_query
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
scope: "brain_query search operation"
fields:
  - name: "query"
    type: "string"
    required: true
    default: null
    description: "Natural language search query"
    error_message: "query is required — provide a search string"
  - name: "max_results"
    type: "integer"
    required: false
    default: 10
    description: "Maximum number of results to return"
    error_message: null
  - name: "filters"
    type: "object"
    required: false
    default: null
    description: "Optional filters: {pillar, kind, domain, min_quality}"
    error_message: null
coercion:
  - from: "string"
    to: "integer"
    rule: "Parse max_results from string if numeric"
examples:
  - {query: "agent for research", max_results: 5}
  - {query: "P06 validators", filters: {pillar: "P06", kind: "validator"}}
domain: "brain-search"
quality: 8.9
tags: [input-schema, brain-query, search, P10]
tldr: "Input contract for brain_query: requires query string, optional max_results and filters."
density_score: 0.90
```
## Contract Definition
brain_query receives search requests from any agent/agent_group. Callers provide a natural
language query string, optional result limit, and optional filters by pillar/kind/domain.
## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | query | string | YES | - | Natural language search query |
| 2 | max_results | integer | NO | 10 | Max results to return |
| 3 | filters | object | NO | null | Filter by pillar, kind, domain, min_quality |
## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | integer | Parse max_results from string if numeric |
## Examples
```json
{"query": "agent for research", "max_results": 5}
```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_is_ pattern (H02 pass)
- kind: input_schema (H04 pass)
- 13+ required fields present (H06 pass)
- fields has 3 entries with name/type/required (H07 pass)
- optional fields have defaults (H08 pass)
- scope is descriptive (S05 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "input-schema" (S02 pass)
- YAML parses cleanly (H01 pass)
## Anti-Example
INPUT: "Input para brain query"
BAD OUTPUT:
```yaml
id: brain_input
kind: schema
pillar: Schema
scope: brain
fields: "query string and results count"
quality: 8.0
tags: input
```
Takes a query and returns results.
FAILURES:
1. id: no `p06_is_` prefix -> H02 FAIL
2. kind: "schema" not "input_schema" -> H04 FAIL
3. pillar: "Schema" not "P06" -> H03 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. fields: string instead of list[object] -> H07 FAIL
6. scope: "brain" not descriptive -> S05 FAIL
7. tags: string not list, len < 3 -> S02 FAIL
8. body: filler prose ("Takes a query and returns results") -> S07 FAIL
9. no examples section -> S08 FAIL
10. no coercion section -> S06 FAIL
