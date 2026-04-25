---
id: n00_pitch_deck_manifest
kind: knowledge_card
8f: F3_inject
pillar: P05
nucleus: n00
title: "Pitch Deck -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, pitch_deck, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_multimodal_prompt
  - bld_schema_contributor_guide
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Pitch deck produces a structured sales or investor presentation with the canonical problem/solution/traction/team/ask narrative arc. It covers 10-12 slides with exact content specifications for each slide, talk track hints, and visual layout guidance. The artifact targets both investor fundraising decks and enterprise sales decks with configurable emphasis.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `pitch_deck` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Company name + deck type + year |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| deck_type | enum | yes | investor / enterprise_sales / partnership |
| slide_count | int | yes | Total number of slides |
| slides | list | yes | Ordered slide specs with title, content, notes |
| ask | string | yes | The specific ask (raise amount, deal size, action) |
| traction_metrics | list | yes | Key metrics proving market validation |

## When to use
- Preparing a fundraising deck for seed, Series A, or growth rounds
- Building an enterprise sales deck for strategic account pursuits
- Creating a partnership pitch for a strategic BD conversation

## Builder
`archetypes/builders/pitch_deck-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind pitch_deck --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N06 commercial structures the ask; N02 marketing crafts the narrative
- `{{SIN_LENS}}` -- Strategic Greed: every slide earns the next; no filler
- `{{TARGET_AUDIENCE}}` -- specific investor archetype or enterprise buyer persona
- `{{DOMAIN_CONTEXT}}` -- funding stage, deal size, competitive landscape, traction data

## Example (minimal)
```yaml
---
id: pitch_deck_cex_seed_2026
kind: pitch_deck
pillar: P05
nucleus: n06
title: "CEX Platform -- Seed Round Pitch Deck 2026"
version: 1.0
quality: null
---
deck_type: investor
slide_count: 11
ask: "$3M seed at $15M pre-money"
traction_metrics: [300 kinds, 3647 ISOs, 4 runtimes, 150 tools]
```

## Related kinds
- `case_study` (P05) -- social proof that feeds the traction slide
- `analyst_briefing` (P05) -- technical credibility that backs the market slide
- `pricing_page` (P05) -- revenue model detail that supports the business model slide

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_pitch_deck]] | downstream | 0.49 |
| [[bld_schema_integration_guide]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.42 |
| [[bld_schema_usage_report]] | downstream | 0.42 |
| [[bld_schema_quickstart_guide]] | downstream | 0.41 |
| [[bld_schema_dataset_card]] | downstream | 0.41 |
| [[bld_schema_search_strategy]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.40 |
| [[bld_schema_contributor_guide]] | downstream | 0.40 |
