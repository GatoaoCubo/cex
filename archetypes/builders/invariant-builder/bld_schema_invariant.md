---
id: bld_schema_invariant
kind: schema
pillar: P08
parent: invariant-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder_agent
tags: [schema, invariant-builder, source-of-truth, P08]
quality: 9.1
title: "Schema Invariant"
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
density_score: 0.90
llm_function: CONSTRAIN
---
# invariant-builder — SCHEMA
SOURCE OF TRUTH. OUTPUT_TEMPLATE.md derives from this. CONFIG.md restricts this. Zero drift permitted.
## Required Fields (15)
| Field | Type | Required | Default | Gate | Notes |
|-------|------|----------|---------|------|-------|
| id | string | YES | — | H02, H03 | Pattern: `p08_law_{number}`. MUST equal filename stem. |
| kind | literal "invariant" | YES | — | H04 | Exact string "invariant". Never "rule", "mandate", "policy". |
| pillar | literal "P08" | YES | — | H06 | Exact string "P08". |
| version | semver X.Y.Z | YES | "1.0.0" | H06 | Quoted string. Increment on revision. |
| created | date YYYY-MM-DD | YES | — | H06 | Quoted string. ISO 8601 format. |
| updated | date YYYY-MM-DD | YES | — | H06 | Quoted string. Update on every revision. |
| author | string | YES | — | H06 | Agent_group ID or human name that produced this. |
| domain | string | YES | — | H06 | Governance domain (e.g., "quality", "operations", "security"). |
| quality | null | YES | null | H05 | MUST be literal null. NEVER a number. Self-scoring prohibited. |
| tags | list[string], len >= 3 | YES | — | H07 | Must include "invariant" and pillar tag. |
| tldr | string, <= 160 chars | YES | — | S01 | Dense one-line summary. No filler. |
| number | positive integer | YES | — | H08 | Unique across all P08 laws. Sequential. |
| statement | string, imperative | YES | — | H09 | One sentence. MUST use MUST/SHALL/NEVER/ALWAYS. |
| rationale | string | YES | — | S02 | WHY this law exists. Must not restate statement. |
| enforcement | string | YES | — | S03 | Names the detection mechanism explicitly. |
## Extended Fields (4)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| scope | enum [system, agent_group, domain] | RECOMMENDED | Applicability boundary. Default: system. |
| exceptions | list[string] | RECOMMENDED | Conditions where law does not apply. Empty list `[]` = no exceptions. |
| priority | integer 1-10 | RECOMMENDED | Conflict resolution. 10 = highest. Used when laws conflict. |
| keywords | list[string], len >= 2 | RECOMMENDED | Brain search terms. S10 gate. |
## ID Pattern
```
^p08_law_[0-9]+$
```
Examples of valid IDs: `p08_law_1`, `p08_law_12`, `p08_law_100`
Examples of invalid IDs: `p08_law_01`, `law_5`, `p08_rule_5`, `P08_law_5`
Rule: `id` MUST equal filename stem. File `p08_law_5.md` MUST have `id: p08_law_5`.
## Required Body Sections (8)
All 8 sections MUST be present. Section headers are exact strings:
| # | Section Header | Minimum Content |
|---|---------------|----------------|
| 1 | `## Statement` | Full imperative form of the invariant |
| 2 | `## Rationale` | Why this law exists with concrete justification |
| 3 | `## Enforcement` | Mechanism, detection method, consequence |
| 4 | `## Exceptions` | Conditions where law does not apply, or "None" |
| 5 | `## Examples` | >= 2 correct applications |
| 6 | `## Violations` | >= 2 breach scenarios with consequences |
| 7 | `## History` | Establishment date and reason, revisions |
| 8 | `## References` | >= 1 governance source |
## Constraints
| Constraint | Value |
|-----------|-------|
| max_bytes (body) | 3072 |
| density_min | 0.80 |
| naming | `p08_law_{number}.md` |
| statement mood | imperative (MUST/SHALL/NEVER/ALWAYS) |
| number | positive integer, unique, sequential |
| enforcement | must name detection mechanism |
| exceptions | explicit list or "None" — never omit |
| scope | one of: system, agent_group, domain |
| priority | integer 1-10 |
| quality | always null |
## Drift Prevention
Every field in SCHEMA.md MUST appear in OUTPUT_TEMPLATE.md.
Every `{{var}}` in OUTPUT_TEMPLATE.md MUST map to a field in SCHEMA.md.
CONFIG.md MAY restrict values but MUST NOT add new fields.
