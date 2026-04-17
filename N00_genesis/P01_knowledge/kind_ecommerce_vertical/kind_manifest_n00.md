---
id: n00_ecommerce_vertical_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "eCommerce Vertical -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, ecommerce_vertical, p01, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
eCommerce Vertical is an industry vertical knowledge artifact that packages domain-specific terminology, KPIs, buyer personas, regulatory context, and technology stack patterns for the eCommerce sector. It is injected into nucleus prompts when operating in retail/eCommerce contexts, enabling domain-aware generation without repeated re-explanation.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `ecommerce_vertical` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Vertical name and scope |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| sub_verticals | list | no | D2C, marketplace, B2B commerce, etc. |
| key_kpis | list | yes | Conversion rate, AOV, CAC, LTV, churn |
| regulatory | list | no | GDPR, PCI-DSS, consumer protection laws |
| tech_stack | list | no | Common platforms: Shopify, Magento, VTEX |
| buyer_personas | list | yes | Primary buyer archetypes |

## When to use
- When generating content, analysis, or agents for eCommerce clients
- When configuring nucleus prompts with retail domain grounding
- When conducting competitive analysis in the eCommerce space

## Builder
`archetypes/builders/ecommerce_vertical-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind ecommerce_vertical --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N01, N02, or N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- eCommerce operators or digital agencies
- `{{DOMAIN_CONTEXT}}` -- specific sub-vertical and geography

## Example (minimal)
```yaml
---
id: ecommerce_vertical_d2c_brazil
kind: ecommerce_vertical
pillar: P01
nucleus: n01
title: "D2C eCommerce Brazil"
version: 1.0
quality: null
---
sub_verticals: [D2C, marketplace]
key_kpis: [conversion_rate, AOV, CAC, LTV]
regulatory: [LGPD, CDC]
tech_stack: [VTEX, Shopify, Magento]
buyer_personas: [fashion_consumer, electronics_buyer]
```

## Related kinds
- `context_doc` (P01) -- broader domain context for eCommerce
- `customer_segment` (P02) -- ICP definitions within eCommerce
- `knowledge_card` (P01) -- atomic facts about the vertical
- `fintech_vertical` (P01) -- adjacent vertical for payment context
