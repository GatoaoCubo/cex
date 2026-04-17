---
id: n00_interactive_demo_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Interactive Demo -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, interactive_demo, p05, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Interactive demo produces a scripted guided-tour artifact for product demonstrations, covering the step-by-step flow a sales engineer or product specialist follows to showcase core value. Each step includes the UI element to highlight, the narration script, the expected user reaction, and the objection response. Designed for both live demos and self-serve sandbox environments.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `interactive_demo` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Product + use case + "Demo Script" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| demo_duration_min | int | yes | Target demo length in minutes |
| audience_segment | string | yes | Technical / Executive / End-user |
| demo_steps | list | yes | Ordered steps with element, script, reaction |
| aha_moment | string | yes | The single highest-value moment in the demo |
| objection_responses | list | no | Common objections with scripted responses |

## When to use
- Training sales engineers on a standard demo flow
- Creating a self-serve sandbox tour for PLG (product-led growth) activation
- Building a conference or trade show demo script

## Builder
`archetypes/builders/interactive_demo-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind interactive_demo --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing + N06 commercial co-produce demo scripts
- `{{SIN_LENS}}` -- Creative Lust: make the aha moment undeniable
- `{{TARGET_AUDIENCE}}` -- specific buyer persona (CTO, ops lead, end user)
- `{{DOMAIN_CONTEXT}}` -- product feature set, primary use case, competitive context

## Example (minimal)
```yaml
---
id: interactive_demo_cex_cto_tour
kind: interactive_demo
pillar: P05
nucleus: n02
title: "CEX Platform -- CTO Demo Script"
version: 1.0
quality: null
---
demo_duration_min: 20
audience_segment: Technical
aha_moment: "8F pipeline produces production artifact from 5-word input"
```

## Related kinds
- `product_tour` (P05) -- in-app guided tour (no sales engineer); demo is live/semi-live
- `onboarding_flow` (P05) -- activation sequence after demo converts to signup
- `pitch_deck` (P05) -- slides that accompany the demo for executive audiences
