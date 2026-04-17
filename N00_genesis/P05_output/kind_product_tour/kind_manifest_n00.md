---
id: n00_product_tour_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Product Tour -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, product_tour, p05, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Product tour produces an in-app guided walkthrough specification that introduces new users to core features through contextual tooltips, spotlights, and progressive disclosure steps. Unlike an interactive demo (which is sales-engineer-led), a product tour is self-serve and triggered automatically on first login or feature discovery. It is the primary PLG activation mechanism.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `product_tour` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Feature name + "Tour" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| trigger | enum | yes | first_login / feature_discovery / manual |
| steps | list | yes | Tour steps with element_selector, content, action |
| skip_allowed | bool | yes | Whether user can exit the tour |
| completion_action | string | yes | What happens after final step (CTA, confetti, etc.) |
| tour_library | string | no | Implementation library (Shepherd.js, Intro.js, Intercom) |

## When to use
- Onboarding new users to a complex feature without human intervention
- Introducing a new feature to existing users on first visit
- Building a PLG activation loop where tour completion is a key activation event

## Builder
`archetypes/builders/product_tour-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind product_tour --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing writes copy; N05 operations implements triggers
- `{{SIN_LENS}}` -- Creative Lust: delight at every step, zero friction
- `{{TARGET_AUDIENCE}}` -- new user persona on first interaction with the feature
- `{{DOMAIN_CONTEXT}}` -- feature complexity, UI framework, activation definition

## Example (minimal)
```yaml
---
id: product_tour_cex_build_command
kind: product_tour
pillar: P05
nucleus: n02
title: "CEX /build Command Tour"
version: 1.0
quality: null
---
trigger: first_login
skip_allowed: true
completion_action: "Show confetti + CTA: Build your first artifact"
```

## Related kinds
- `onboarding_flow` (P05) -- sequences multiple tours into a structured activation path
- `interactive_demo` (P05) -- sales-engineer-led; product tour is self-serve
- `user_journey` (P05) -- full funnel map; product tour is the activation step
