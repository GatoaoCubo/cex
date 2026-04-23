---
id: kc_pricing_page
kind: knowledge_card
pillar: P01
title: "KC: Pricing Page"
version: 1.1.0
created: "2026-04-07"
updated: "2026-04-22"
author: knowledge-card-builder
domain: monetization
quality: 8.8
tags: [pricing-page, monetization, saas, conversion, subscription, ui]
tldr: "Pricing page converts via anchor tier, CTA hierarchy, feature matrix, and FAQ. Builds on subscription_tier; max 4 tiers."
when_to_use: "Building a pricing_page artifact: tier layout, anchor, CTA copy, feature matrix, FAQ, and social proof."
keywords: [pricing-page, tier, anchor, CTA, feature-matrix]
long_tails:
  - "how to structure a SaaS pricing page with 3 tiers"
  - "pricing page with free trial CTA and annual toggle"
axioms:
  - "ALWAYS include an anchor tier (middle tier highlighted) to guide decisions"
  - "NEVER list more than 4 tiers -- cognitive overload kills conversion"
  - "ALWAYS pair each tier with a primary CTA that matches the tier goal"
  - "NEVER hide pricing -- friction-free price visibility increases qualified leads"
linked_artifacts:
  primary: pricing-page-builder
  related: [kc_subscription_tier, kc_landing_page, kc_ai_saas_monetization]
density_score: 0.88
data_source: "https://www.priceintelligently.com/blog/saas-pricing-page"
---
# Knowledge Card: pricing_page

## Quick Reference
```yaml
topic: pricing_page
scope: SaaS/infoproduct monetization UI (P05 + P11)
owner: N06_commercial + N02_marketing
criticality: high
builder: pricing-page-builder
```

## Definition
A **pricing_page** is a standalone conversion page presenting subscription tiers
with anchoring, feature matrix, FAQ, and CTA hierarchy for visitor self-selection.

## Key Concepts
- **Anchor tier**: middle tier styled as "Most Popular"; shifts purchases up
- **Feature matrix**: rows=features, cols=tiers; checkmarks show differentiation
- **Annual toggle**: monthly/annual switch with discount badge (e.g. "Save 20%")
- **CTA hierarchy**: primary (highlighted tier) > secondary (other tiers)
- **Trust signals**: logos, testimonials, "no credit card required" badge
- **FAQ section**: minimum 5 objections (cancel anytime, refund, security, upgrade)

## Strategy Phases
1. **Define tiers**: 3 (Free/Pro/Business) or 4 max; map to buyer personas
2. **Set anchor**: middle tier price makes top tier feel reasonable (Weber law)
3. **Build matrix**: cols=tiers, rows=features ordered high->low value
4. **CTA copy**: Free="Get Started Free", Pro="Start Trial", Biz="Contact Sales"
5. **Social proof**: 2-3 logos + 1 testimonial per tier use case
6. **FAQ**: 5 objections (cancel policy, refund, security, upgrade, downgrade)

## Golden Rules
- ANCHOR: highlight 1 tier only (border + badge); highlighting 2+ kills effect
- MATRIX: limit feature rows to 8-10; more = visual noise, not value
- TOGGLE: show annual price by default; monthly toggle reduces conversion 12-18%
- CTA: all primary CTAs above the fold; secondary CTAs repeat at page bottom
- TRUST: "no credit card required" near Free CTA doubles free-tier signup rate

## Flow
```text
[Landing] -> [Toggle annual/monthly] -> [3 tier cards + anchor badge]
[Scroll]  -> [Feature matrix] -> [Social proof] -> [FAQ] -> [Bottom CTA]
```

## Comparativo
| Element | Free | Pro (anchor) | Business |
|---------|------|--------------|----------|
| CTA | "Get Started Free" | "Start Free Trial" | "Contact Sales" |
| Badge | -- | "Most Popular" | -- |
| Price | $0/mo | $X/mo annual | Custom |
| Features shown | 3-4 | 7-8 | All + custom |
| Trust | "No CC needed" | Testimonial | Logo wall |

## Anti-Patterns
- **4+ highlighted tiers**: anchoring fails; visitor paralysis, page exits up
- **Features listed as bullet prose**: matrix table converts 2x better
- **Monthly price default**: annual default + toggle increases LTV conversion
- **Missing FAQ**: 28% of SaaS visitors cite "unclear cancellation" as drop reason
- **Enterprise "call us" without form**: removes low-friction entry for SMB

## Integration Points
| Artifact | Role |
|----------|------|
| `subscription_tier` (P11) | Tier definitions injected into pricing_page |
| `landing_page` (P05) | Pricing section or standalone embed |
| `content_monetization` (P11) | Sets tier prices and feature limits |
| `competitive_matrix` (P01) | Informs tier positioning vs. competitors |
| `brand_config.yaml` (P09) | Design tokens: colors, fonts, CTA styles |

## References
- https://www.priceintelligently.com/blog/saas-pricing-page
- https://unbounce.com/landing-page-articles/saas-pricing-page-examples/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_subscription_tier]] | sibling | 0.72 |
| [[kc_landing_page]] | upstream | 0.61 |
| [[kc_ai_saas_monetization]] | sibling | 0.55 |
| [[pricing-page-builder]] | downstream | 0.53 |
| [[bld_examples_pricing_page]] | downstream | 0.47 |
| [[bld_instruction_pricing_page]] | downstream | 0.44 |
| [[p08_pat_pricing_framework]] | sibling | 0.38 |
| [[n06_api_access_pricing]] | downstream | 0.35 |
| [[n06_funnel_cex_product]] | downstream | 0.31 |
| [[bld_knowledge_card_pricing_page]] | sibling | 0.28 |
