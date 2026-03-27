---
id: diagram-builder-schema
kind: schema
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — SCHEMA

SCHEMA.md is the SOURCE OF TRUTH. OUTPUT_TEMPLATE derives from it. CONFIG restricts it. No other file overrides SCHEMA.

## Required Fields (15)

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | YES | — | Pattern: `^p08_diag_[a-z][a-z0-9_]+$` — H02, H03 |
| kind | literal "diagram" | YES | — | Exact string — H04 |
| pillar | literal "P08" | YES | — | Exact string — H06 |
| version | semver X.Y.Z | YES | "1.0.0" | Quoted string |
| created | date YYYY-MM-DD | YES | — | Quoted string — H06 |
| updated | date YYYY-MM-DD | YES | — | Quoted string — H06 |
| author | string | YES | — | Who produced — H06 |
| domain | string | YES | — | Architecture domain (e.g. orchestration) |
| quality | null | YES | null | NEVER a number — H05 |
| tags | list[string], len >= 3 | YES | — | Searchability — H07 |
| tldr | string <= 160ch | YES | — | Dense summary — S01 |
| scope | string | YES | — | What is visualized — H08 |
| notation | enum [ascii, mermaid] | YES | — | Diagram format — H09 |
| zoom_level | enum [system, subsystem, component] | YES | — | Detail level — S02 |
| components | list[string], len >= 2 | YES | — | Visualized components — S03 |

## Extended Fields (4)

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| connections | list[string] | REC | Relationships between components |
| layers | list[string] | REC | Architecture layers shown |
| annotations | list[string] | REC | Design decision notes |
| keywords | list[string] | REC | Brain search terms, len >= 2 — S10 |

## ID Pattern

`^p08_diag_[a-z][a-z0-9_]+$`

Valid: `p08_diag_satellite_orchestration`, `p08_diag_brain_ingestion`
Invalid: `system_diagram`, `P08_diag_X`, `p08-diag-x`

## Body Structure (7 sections — all required for S07)

| Section | Content |
|---------|---------|
| `## Scope` | What system/subsystem is visualized and boundaries |
| `## Diagram` | Actual ASCII or Mermaid visual (not prose) |
| `## Legend` | Symbol and arrow type explanations |
| `## Components` | Table: Component / Role / Layer |
| `## Connections` | Table: From / To / Type / Data |
| `## Annotations` | Non-obvious design decisions |
| `## References` | Sources used |

## Constraints

| Constraint | Value |
|-----------|-------|
| max_bytes | 4096 |
| density_min | 0.80 |
| naming | `p08_diag_{scope_slug}.md` |
| notation | consistent — all ASCII or all Mermaid, no mixing |
| components | minimum 2 labeled |
| diagram | must contain actual visual characters |
| quality | always null |
