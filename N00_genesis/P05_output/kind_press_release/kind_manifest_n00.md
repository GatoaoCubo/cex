---
id: n00_press_release_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Press Release -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, press_release, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_press_release
  - bld_schema_pitch_deck
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_app_directory_entry
  - bld_schema_multimodal_prompt
  - bld_schema_customer_segment
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Press release produces an AP-style news announcement with headline, dateline, lead paragraph, body quotes, boilerplate, and media contact block. It follows wire distribution conventions (PR Newswire, Business Wire, GlobeNewswire) to maximize pickup probability. The artifact is designed to be publishable without editing by a journalist covering the relevant beat.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `press_release` |
| pillar | string | yes | Always `P05` |
| title | string | yes | AP-style headline (< 100 chars, active voice) |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| dateline | string | yes | City, State, Date -- FOR IMMEDIATE RELEASE |
| news_type | enum | yes | product_launch / funding / partnership / award / milestone |
| lead_paragraph | string | yes | Who/what/when/where/why in first 50 words |
| executive_quote | string | yes | Attributed quote from CEO or relevant executive |
| boilerplate | string | yes | Standard "About [Company]" paragraph |
| media_contact | object | yes | Name, email, phone for press inquiries |

## When to use
- Announcing a product launch, funding round, major partnership, or company milestone
- Distributing news via wire services for broad media pickup
- Providing journalists with ready-to-publish factual content

## Builder
`archetypes/builders/press_release-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind press_release --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing produces; N06 commercial approves business facts
- `{{SIN_LENS}}` -- Creative Lust: irresistible headline that demands to be clicked
- `{{TARGET_AUDIENCE}}` -- journalists and editors covering the relevant tech/business beat
- `{{DOMAIN_CONTEXT}}` -- news event type, key facts, executive names, embargo status

## Example (minimal)
```yaml
---
id: press_release_cex_launch_2026
kind: press_release
pillar: P05
nucleus: n02
title: "CEX Launches Enterprise AI Brain with 257 Typed Knowledge Kinds"
version: 1.0
quality: null
---
news_type: product_launch
dateline: "SAO PAULO, April 17, 2026 -- FOR IMMEDIATE RELEASE"
```

## Related kinds
- `analyst_briefing` (P05) -- often coordinated with press release for analyst coverage
- `app_directory_entry` (P05) -- directory submission often timed with launch PR
- `case_study` (P05) -- customer evidence that can be quoted in press releases

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_press_release]] | downstream | 0.56 |
| [[bld_schema_pitch_deck]] | downstream | 0.48 |
| [[bld_schema_usage_report]] | downstream | 0.47 |
| [[bld_schema_integration_guide]] | downstream | 0.47 |
| [[bld_schema_dataset_card]] | downstream | 0.47 |
| [[bld_schema_reranker_config]] | downstream | 0.47 |
| [[bld_schema_app_directory_entry]] | downstream | 0.46 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.46 |
| [[bld_schema_customer_segment]] | downstream | 0.45 |
| [[bld_schema_search_strategy]] | downstream | 0.45 |
