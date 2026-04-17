---
id: schema_prompt_template_builder
kind: type_def
pillar: P06
llm_function: CONSTRAIN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [schema, prompt-template, P03, source-of-truth]
quality: 9.1
title: "Schema Prompt Template"
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
density_score: 0.90
---

# Schema — prompt-template-builder
> SOURCE OF TRUTH. All fields in this file MUST appear in OUTPUT_TEMPLATE.md. Zero drift permitted.
## ID Pattern
```
^p03_pt_[a-z][a-z0-9_]+$
```
Examples: `p03_pt_knowledge_card`, `p03_pt_research_synthesis`, `p03_pt_code_review`
## Frontmatter Fields
| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| id | string | YES | — | Unique identifier. Must match ID pattern above |
| kind | enum | YES | — | Fixed value: `prompt_template` |
| pillar | enum | YES | — | Fixed value: `P03` |
| title | string | YES | — | Human-readable name of the template |
| version | string | YES | `"1.0.0"` | Semver string |
| created | string | YES | — | ISO date: YYYY-MM-DD |
| updated | string | YES | — | ISO date: YYYY-MM-DD, updated on every change |
| author | string | YES | — | Agent_group or human author ID |
| variables | list[object] | YES | — | List of variable definitions (see Variable Object below) |
| variable_syntax | enum | YES | `"mustache"` | `"mustache"` or `"bracket"` |
| composable | boolean | YES | `false` | True if template is designed for embedding in larger templates |
| domain | string | YES | — | Semantic domain: research, marketing, knowledge, code, etc. |
| quality | float or null | YES | `null` | Gate score 0.0-1.0; null until first validation |
| tags | list[string] | YES | `[]` | Searchability tags |
| tldr | string | YES | — | One-sentence summary for discovery |
| keywords | list[string] | REC | `[]` | Search keywords distinct from tags |
| density_score | float | REC | `null` | Content density 0.0-1.0; null until measured |
## Variable Object
Each item in the `variables` list MUST contain:
| Field | Type | Required | Description |
|---|---|---|---|
| name | string | YES | Variable name matching the slot in the template body |
| type | enum | YES | `string`, `list`, `integer`, `boolean`, `object` |
| required | boolean | YES | Whether the variable must be supplied at render time |
| default | any or null | YES | Default value; null for required variables |
| description | string | YES | One sentence describing the variable's purpose |
## Body Structure
Every `prompt_template` artifact MUST contain these 5 sections in order:
1. `## Purpose` — one paragraph describing what the template produces and its reuse scope
2. `## Variables Table` — markdown table listing all variables with all 5 object fields
3. `## Template Body` — the parameterized prompt text in a fenced code block
4. `## Quality Gates` — table showing H01-H08 gate status for this artifact
5. `## Examples` — at least one filled example with variable values and rendered output
## Constraints
| Constraint | Rule |
|---|---|
| max_bytes | 8192 bytes per file |
| variable_syntax | `mustache` is tier-1 ({{var}}); `bracket` is tier-2 (`[VAR]`) — use bracket only when Mustache conflicts with target system |
| body completeness | Every `{{var}}` in the body MUST be declared in `variables`. Every declared variable MUST appear in the body at least once. |
| id uniqueness | No two prompt_template artifacts may share the same id |
| kind lock | The `kind` field MUST be `prompt_template` — never overridden |
| quality null | `quality: null` is valid for draft artifacts; must be a float before pool submission |
## Enum Values
### variable_syntax
- `mustache` — `{{variable}}` syntax (Mustache, Handlebars, Anthropic-compatible)
- `bracket` — `[VARIABLE]` syntax (fallback for systems where `{{}}` is reserved)
### variable.type
- `string` — plain text
- `list` — array of items
- `integer` — whole number
- `boolean` — true/false
- `object` — structured key-value data
