---
id: p11_qg_function_def
kind: quality_gate
pillar: P11
title: "Gate: function_def"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "JSON Schema function definitions callable by LLMs via tool_use/function_calling"
quality: 9.0
tags: [quality-gate, function-def, P04, json-schema, tool-calling, parameters]
tldr: "Pass/fail gate for function_def artifacts: valid JSON Schema parameters, LLM-facing description, return type, and provider compatibility."
density_score: 0.90
llm_function: GOVERN
---
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
