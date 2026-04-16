---
kind: schema
id: bld_schema_expansion_play
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for expansion_play
quality: 9.2
title: "Schema Expansion Play"
version: "1.0.0"
author: wave6_n06
tags: [expansion_play, builder, schema, upsell, NRR, land-and-expand]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for expansion_play"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field            | Type   | Required | Default | Notes                                        |
|------------------|--------|----------|---------|----------------------------------------------|
| id               | string | yes      |         | Pattern: p03_ep_{{name}}.md                  |
| kind             | string | yes      |         | Must be "expansion_play"                     |
| pillar           | string | yes      |         | Must be "P03"                                |
| title            | string | yes      |         |                                              |
| version          | string | yes      |         |                                              |
| created          | date   | yes      |         | ISO 8601                                     |
| updated          | date   | yes      |         | ISO 8601                                     |
| author           | string | yes      |         |                                              |
| domain           | string | yes      |         | e.g., "SaaS expansion -- enterprise segment" |
| quality          | null   | yes      | null    | Never self-score; peer review assigns        |
| tags             | array  | yes      |         | Must include: expansion, NRR or upsell       |
| tldr             | string | yes      |         |                                              |
| account_segment  | string | yes      |         | SMB / MM / ENT                               |
| expansion_type   | string | yes      |         | seat_upsell / tier_upgrade / cross_sell / usage_ramp |
| trigger_type     | string | yes      |         | usage_threshold / feature_adoption / QBR_signal |
| NRR_target       | string | yes      |         | e.g., ">120%" -- numeric target required     |

### Recommended
| Field              | Type   | Notes                                      |
|--------------------|--------|--------------------------------------------|
| current_ARR        | string | Current account ARR                        |
| expansion_ARR      | string | Expected expansion ARR from this play      |
| seat_utilization   | string | Current seats used vs. licensed            |
| health_score       | number | Gainsight/CS health score (0-100)          |
| qbr_date           | date   | Next scheduled QBR date                    |

## ID Pattern
^p03_ep_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Expansion Trigger** -- quantified usage/adoption signal that activates the play
2. **Account Map** -- economic buyer, champion, blocker, procurement contact
3. **Expansion Motion** -- seat upsell / tier upgrade / cross-sell SKU / usage ramp
4. **NRR Model** -- expansion ARR, contraction risk, net NRR contribution
5. **AE/CSM Talk Track** -- hook, value statement, business case, ask, next step
6. **QBR Structure** -- value delivered slide, expansion opportunity slide, success metrics
7. **Objection Handling** -- budget, timing, competing priorities responses

## Constraints
- All required fields must be present and valid.
- id must match regex pattern exactly.
- expansion_type must be one of: seat_upsell, tier_upgrade, cross_sell, usage_ramp.
- trigger_type must be one of: usage_threshold, feature_adoption, QBR_signal, health_score_spike.
- NRR_target must be a numeric percentage string (e.g., ">120%", "115%").
- Talk track must contain minimum: hook, value statement, ask, and next step sections.
