---
kind: schema
id: bld_schema_response_format
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for response_format
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: 2.0.0
quality: 9.1
title: "Schema Response Format"
author: n03_builder
tags: [response_format, builder, examples]
tldr: "Golden and anti-examples for response format construction, demonstrating ideal structure and common pitfalls."
domain: "response format construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: response_format
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P05` |
| Type | literal `response_format` |
| Machine format | `yaml` (frontmatter yaml + md body) |
| Naming | `p05_rf_{format_slug}.yaml` |
| Max bytes | 4096 |
## Required Fields (12)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string, matches `^p05_rf_[a-z][a-z0-9_]+$` | YES | — | id == filename stem |
| kind | literal "response_format" | YES | — | Type discriminator |
| pillar | literal "P05" | YES | — | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update date |
| author | string | YES | — | Producer identity |
| format_type | enum: json, yaml, markdown, text, structured | YES | — | Output format; compliance: JSON 95% > YAML 90% > tables 88% > lists 85% > prose 70% |
| domain | string | YES | — | Domain this format covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "response-format" |
| tldr | string <= 160ch | YES | — | Dense summary |
## Recommended Fields (4)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| target_kind | string | REC | Artifact kind that uses this format |
| example_output | string | REC | Concrete example of expected output |
| variable_syntax | enum: mustache, bracket | REC | tier1=`{{MUSTACHE}}` for primary, tier2=[BRACKET] for secondary |
| sections | list[string] | REC | Ordered output section names |
## ID Pattern
```
^p05_rf_[a-z][a-z0-9_]+$
```
Rule: id MUST equal filename stem.
## Variable Syntax
| Tier | Syntax | Use |
|------|--------|-----|
| Primary (required vars) | `{{VARIABLE_NAME}}` | Mustache — always typed in variables table |
| Secondary (optional vars) | `[VARIABLE_NAME]` | Bracket — clearly marked optional |
Every variable MUST have type + example in the variables table. Untyped variables are forbidden.
## Body Structure (4 sections)
1. `## Format Specification` — what output structure this defines, format_type, compliance notes
2. `## Variables Table` — all variables with name, type, constraints, required/optional, example
3. `## Template Body` — the actual template with placeholders showing expected shape
4. `## Example Output` — complete filled example demonstrating correct output
## Compliance Note
Format preference hierarchy (by LLM compliance rate):
`JSON (95%) > YAML (90%) > Markdown tables (88%) > Numbered lists (85%) > Prose (70%)`
Choose format_type based on consumer: machine = json, config = yaml, human = markdown.
## Constraints
| Constraint | Value |
|-----------|-------|
| max_bytes | 4096 (body only) |
| naming | p05_rf_{format_slug}.yaml |
| id == filename stem | enforced |
| format_type | one of: json, yaml, markdown, text, structured |
| quality | ALWAYS null |
| sections | 4-7 per format (consolidate if >7) |
| variables | every variable typed + exampled |
