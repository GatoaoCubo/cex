---
id: n00_case_study_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Case Study -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, case_study, p05, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Case study produces a structured customer success narrative following the challenge/solution/outcome/quote pattern. It transforms raw customer data and interview notes into a publishable proof-of-value artifact for use in sales cycles, analyst briefings, and demand generation content. Credibility is built through quantified outcomes and authentic customer voice.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `case_study` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Customer name + outcome headline |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| customer_name | string | yes | Company name (or anonymized alias) |
| industry | string | yes | Customer industry vertical |
| challenge | string | yes | Business problem before the solution |
| solution | string | yes | How the product addressed the challenge |
| outcome | string | yes | Quantified results (%, $, time saved) |
| quote | string | no | Verbatim customer quote with attribution |
| use_permission | bool | yes | Customer approval to publish (true required before publish) |

## When to use
- Closing a sales cycle that needs proof from a peer company in the same industry
- Building a content library for analyst briefings (evidence section)
- Publishing post-launch success stories for demand generation

## Builder
`archetypes/builders/case_study-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind case_study --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing produces; N06 commercial sources the customers
- `{{SIN_LENS}}` -- Creative Lust: narrative arc that converts skeptics
- `{{TARGET_AUDIENCE}}` -- prospective buyers in the same industry vertical
- `{{DOMAIN_CONTEXT}}` -- industry, company size, use case, quantified outcomes

## Example (minimal)
```yaml
---
id: case_study_acme_fintech_2026
kind: case_study
pillar: P05
nucleus: n02
title: "Acme Corp -- 40% faster compliance reporting with CEX"
version: 1.0
quality: null
---
challenge: "Manual compliance reports took 3 weeks per quarter"
outcome: "Reduced to 9 days; 0 audit findings in first cycle"
```

## Related kinds
- `analyst_briefing` (P05) -- consumes case studies as traction evidence
- `pitch_deck` (P05) -- references case study outcomes in traction slides
- `landing_page` (P05) -- embeds case study excerpts as social proof
