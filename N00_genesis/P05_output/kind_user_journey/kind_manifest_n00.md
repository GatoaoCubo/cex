---
id: n00_user_journey_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "User Journey -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, user_journey, p05, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
User journey produces an end-to-end funnel map from awareness to conversion and retention, documenting every touchpoint, user emotion, friction point, and enabling artifact at each stage. It is the canonical top-level artifact for product and marketing strategy, serving as the source of truth from which more specific output artifacts (landing pages, onboarding flows, product tours) are derived.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `user_journey` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Persona name + "User Journey" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| persona | string | yes | User persona name and archetype |
| stages | list | yes | Journey stages (awareness/consideration/decision/retention) |
| touchpoints | list | yes | Interaction points at each stage with channel and content |
| emotion_curve | list | yes | Emotional state (positive/neutral/negative) at each stage |
| friction_points | list | yes | Drop-off risks and their mitigation artifacts |

## When to use
- Designing or auditing the full acquisition and retention funnel for a product
- Identifying gaps in the content and artifact coverage for a specific persona
- Aligning marketing, product, and commercial teams on the canonical customer path

## Builder
`archetypes/builders/user_journey-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind user_journey --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing + N06 commercial co-own journey mapping
- `{{SIN_LENS}}` -- Strategic Greed: optimize every stage for conversion and LTV
- `{{TARGET_AUDIENCE}}` -- internal teams (product, marketing, commercial) using journey as strategy doc
- `{{DOMAIN_CONTEXT}}` -- persona definition, channel mix, current funnel conversion data

## Example (minimal)
```yaml
---
id: user_journey_cex_developer
kind: user_journey
pillar: P05
nucleus: n02
title: "Developer Persona -- CEX User Journey"
version: 1.0
quality: null
---
persona: "Senior developer evaluating AI orchestration platforms"
stages: [awareness, consideration, trial, activation, retention]
emotion_curve: [neutral, curious, excited, satisfied, loyal]
```

## Related kinds
- `onboarding_flow` (P05) -- details the activation stage of the user journey
- `landing_page` (P05) -- primary artifact at the awareness/acquisition stage
- `cohort_analysis` (P07) -- measures retention stage outcomes from the journey
