---
id: n00_content_monetization_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Content Monetization -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, content_monetization, p11, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A content_monetization artifact is a config-driven content monetization pipeline that defines how CEX-generated content is packaged, priced, and delivered to generate revenue. It specifies revenue streams, access tiers, paywall logic, affiliate structures, and conversion funnels, giving N06 a concrete blueprint for turning knowledge assets into income.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `content_monetization` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| revenue_model | enum | yes | subscription \| one_time \| freemium \| usage_based \| affiliate |
| content_assets | array | yes | List of content items being monetized with type and value |
| pricing_tiers | array | yes | Tier definitions with price, features, and access level |
| paywall_trigger | string | yes | Condition that activates the paywall |
| payment_provider | string | yes | Payment processor (stripe \| paddle \| lemonsqueezy) |
| conversion_funnel | array | no | Steps from free user to paying customer |

## When to use
- When packaging CEX-generated knowledge cards or courses for sale
- When designing SaaS monetization for a nucleus-powered product
- When building affiliate or referral revenue streams around content assets

## Builder
`archetypes/builders/content_monetization-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind content_monetization --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cm_cex_knowledge_course
kind: content_monetization
pillar: P11
nucleus: n06
title: "Example Content Monetization"
version: 1.0
quality: null
---
# Monetization: CEX Knowledge Course
revenue_model: freemium
payment_provider: stripe
paywall_trigger: "after 3 free modules"
pricing_tiers: [{tier: free, price: 0}, {tier: pro, price: 97}]
```

## Related kinds
- `subscription_tier` (P11) -- tier definition used in pricing_tiers
- `referral_program` (P11) -- referral revenue layer atop this monetization config
- `roi_calculator` (P11) -- ROI model for pricing decisions
