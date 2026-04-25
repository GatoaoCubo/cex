---
id: n00_analyst_briefing_manifest
kind: knowledge_card
8f: F3_inject
pillar: P05
nucleus: n00
title: "Analyst Briefing -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, analyst_briefing, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_analyst_briefing
  - analyst-briefing-builder
  - p03_sp_analyst_briefing_builder
  - bld_knowledge_card_analyst_briefing
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - p05_qg_analyst_briefing
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Analyst briefing produces a structured deck artifact following Gartner/Forrester/IDC conventions. It delivers a concise, credibility-building narrative for industry analysts covering market positioning, differentiation, traction evidence, and roadmap signals. Output is designed for 30-60 minute briefing sessions with Tier 1 analysts.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `analyst_briefing` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Human-readable briefing title |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| analyst_firm | string | yes | Target firm (Gartner, Forrester, IDC, etc.) |
| analyst_name | string | no | Named analyst or coverage team |
| market_category | string | yes | Magic Quadrant / Wave category being addressed |
| briefing_date | date | no | Scheduled or planned briefing date |
| sections | list | yes | Ordered slide/section list with titles and content |

## When to use
- Scheduling a formal briefing with Gartner, Forrester, IDC, or boutique analyst firms
- Preparing a positioning narrative ahead of a Magic Quadrant / Wave evaluation cycle
- Responding to an analyst inquiry with structured evidence of capabilities and traction

## Builder
`archetypes/builders/analyst_briefing-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind analyst_briefing --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N02 marketing)
- `{{SIN_LENS}}` -- Creative Lust: seductive positioning narrative
- `{{TARGET_AUDIENCE}}` -- named analyst + firm covering the relevant market
- `{{DOMAIN_CONTEXT}}` -- product category, competitive landscape, traction metrics

## Example (minimal)
```yaml
---
id: analyst_briefing_cex_gartner_2026
kind: analyst_briefing
pillar: P05
nucleus: n02
title: "CEX Platform -- Gartner AI Orchestration Briefing 2026"
version: 1.0
quality: null
---
# Sections
- problem: Enterprise AI fragmentation -- 7 tools, 0 governance
- solution: CEX typed knowledge system -- 300 kinds, 8F pipeline
- traction: 3647 ISOs, 148 tools, 4 runtimes in production
```

## Related kinds
- `pitch_deck` (P05) -- investor-facing narrative; analyst briefing uses more technical evidence
- `case_study` (P05) -- provides the traction evidence that feeds into the briefing
- `press_release` (P05) -- often timed alongside analyst briefing for coordinated coverage

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_analyst_briefing]] | downstream | 0.50 |
| [[analyst-briefing-builder]] | related | 0.46 |
| [[p03_sp_analyst_briefing_builder]] | upstream | 0.44 |
| [[bld_knowledge_card_analyst_briefing]] | sibling | 0.41 |
| [[bld_schema_pitch_deck]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
| [[bld_schema_search_strategy]] | downstream | 0.38 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[p05_qg_analyst_briefing]] | downstream | 0.38 |
