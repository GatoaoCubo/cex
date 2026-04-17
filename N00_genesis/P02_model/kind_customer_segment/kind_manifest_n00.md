---
id: n00_customer_segment_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Customer Segment -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, customer_segment, p02, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Customer Segment defines an Ideal Customer Profile (ICP) or buyer persona with demographic, firmographic, psychographic, and behavioral attributes. It constrains how agents generate content, pricing, and messaging to resonate with a specific audience. Used by N06 commercial and N02 marketing nuclei to ground outputs in real buyer context.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `customer_segment` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Segment name and label |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| segment_type | enum | yes | ICP\|persona\|account\|cohort |
| industry | string | yes | Primary industry vertical |
| company_size | string | no | Employee range (e.g., 50-500) |
| buyer_role | string | yes | Job title or function of decision maker |
| pain_points | list | yes | Top 3-5 pain points |
| desired_outcomes | list | yes | What success looks like for this segment |
| willingness_to_pay | enum | no | low\|medium\|high |

## When to use
- When defining who a product or service targets
- When grounding N06 pricing or N02 copy generation with ICP context
- When segmenting a market for campaign targeting

## Builder
`archetypes/builders/customer_segment-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind customer_segment --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N06 or N02)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- marketing and sales teams
- `{{DOMAIN_CONTEXT}}` -- product category and market

## Example (minimal)
```yaml
---
id: customer_segment_enterprise_cto
kind: customer_segment
pillar: P02
nucleus: n06
title: "Enterprise CTO Segment"
version: 1.0
quality: null
---
segment_type: ICP
industry: Technology
company_size: "500-5000"
buyer_role: CTO / VP Engineering
pain_points: [AI cost unpredictability, vendor lock-in, quality inconsistency]
desired_outcomes: [sovereign AI infrastructure, predictable costs, quality governance]
willingness_to_pay: high
```

## Related kinds
- `discovery_questions` (P01) -- qualification questions for this segment
- `competitive_matrix` (P01) -- competitive context this segment faces
- `nucleus_def` (P02) -- nucleus that serves this segment
