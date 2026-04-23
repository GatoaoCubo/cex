---
id: p12_wf_commercial
kind: workflow
pillar: P12
title: "N06 Workflow — Brand Discovery + Revenue + Bridge"
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n06_commercial
domain: brand-identity-monetization
step_count: 10
quality: 9.1
updated: 2026-04-07
tags: [workflow, commercial, N06, brand, monetization, pipeline]
tldr: "3 workflows: BRAND (10-step discovery→propagation), MONETIZATION (7-step product→revenue), BRIDGE (5-step brand→monetization alignment). N06 runs FIRST on new instances."
density_score: 0.94
axioms:
  - "BRAND workflow ALWAYS completes before MONETIZATION workflow starts."
  - "BRIDGE workflow validates alignment — if brand→monetization gap > 0.15, re-run brand audit."
linked_artifacts:
  primary: p12_dr_commercial
  related: [p02_agent_commercial_nucleus, p07_qg_commercial, n06_schema_brand_audit]
related:
  - p02_agent_commercial_nucleus
  - p03_sp_commercial_nucleus
  - p07_sr_commercial
  - spec_n06_brand_verticalization
  - p02_mm_commercial_nucleus
  - p03_sp_brand_nucleus
  - p02_agent_brand_nucleus
  - p12_dr_commercial
  - agent_card_n06
  - p08_ac_brand_nucleus
---

# N06 Workflow — Brand + Monetization + Bridge

## Workflow 1: BRAND (10 Steps)

```
INTENT → DISCOVER → RESEARCH → ARCHETYPE → BOOK → EXTRACT → VALIDATE → PROPAGATE → AUDIT → SIGNAL
```

| Step | Action | Input | Output | Tool |
|------|--------|-------|--------|------|
| 1 | Receive brand intent | User request | Classified intent | cex_intent.py |
| 2 | Brand Discovery Interview | Intent | 12-15 answered questions | brand_discovery_interview.md |
| 3 | Market Research | Discovery answers | Competitive landscape | N01 handoff (fetch MCP) |
| 4 | Archetype Selection | Answers + research | 1 of 12 Jungian archetypes | kc_brand_archetypes.md |
| 5 | Brand Book Generation | All inputs | 32-block Brand Book | brand_book_generator.md |
| 6 | Config Extraction | Brand Book | brand_config.yaml | brand_config_extractor.md |
| 7 | Schema Validation | brand_config.yaml | Pass/fail + errors | brand_validate.py |
| 8 | Propagation | brand_config.yaml | brand_context.md per nucleus | brand_propagate.py |
| 9 | Brand Audit | All brand artifacts | Consistency score (>= 0.85) | brand_audit.py |
| 10 | Signal Complete | Audit results | n06_complete.json | signal_writer.py |

### Decision Points
- Step 7 FAIL → return to Step 5, revise Book
- Step 9 score < 0.85 → return to Step 4, re-evaluate archetype
- Step 9 score >= 0.95 → Gold standard, archive as exemplar

## Workflow 2: MONETIZATION (7 Steps)

```
PRODUCT → PRICING → TIERS → FUNNEL → COURSE → REVENUE → VALIDATE
```

| Step | Action | Input | Output | Tool |
|------|--------|-------|--------|------|
| 1 | Define product/service | Revenue intent | Product spec | — |
| 2 | Pricing Strategy | Product + ICP | Anchor + tier structure | pricing_calculator |
| 3 | Tier Design | Strategy | 2-4 tier cards + features | output_pricing_page.md |
| 4 | Funnel Design | Tiers + ICP | TOFU/MOFU/BOFU sequence | funnel_mapper |
| 5 | Course Structure (if applicable) | Product + transformation | Modules + lessons + arc | — |
| 6 | Revenue Modeling | Price × conversion × volume | MRR/LTV projections | revenue_forecaster |
| 7 | Quality Validation | All outputs | Score >= 8.0 | scoring_rubric_commercial.md |

### Decision Points
- Step 7 score < 8.0 → revise pricing rationale or funnel copy
- No brand_config.yaml → STOP, run Workflow 1 first

## Workflow 3: BRIDGE (5 Steps)

Connects brand identity to monetization artifacts:

```
BRAND_BOOK → EXTRACT_PRICING → ALIGN_FUNNEL → PRICE_BY_ARCHETYPE → DELIVER_ON_BRAND
```

| Step | Action | Input | Output |
|------|--------|-------|--------|
| 1 | Extract pricing context | Brand Book (positioning + ICP) | Value-based price anchors |
| 2 | Align funnel with voice | brand_config voice section | Funnel copy in brand tone |
| 3 | Price by archetype | Archetype + ICP income | Archetype-appropriate pricing |
| 4 | Brand-inject pricing page | Pricing page + brand_config | Fully branded HTML |
| 5 | Final validation | Branded revenue artifacts | Dual score (brand + revenue) |

### Archetype → Pricing Alignment

| Archetype | Pricing Style | Example |
|-----------|---------------|---------|
| Creator | Premium, innovation-premium | "Investment in your craft" |
| Hero | Achievement-based, challenge | "Level up your game" |
| Sage | Knowledge-value, authority | "Wisdom has no price" |
| Explorer | Freedom-pricing, flexibility | "Choose your adventure" |
| Rebel | Disruptive, anti-establishment | "Break free from overpriced X" |
| Caregiver | Accessible, payment plans | "We make it affordable" |
| Ruler | Premium, exclusive | "For those who lead" |
| Everyman | Value-for-money, no-frills | "Fair pricing, real results" |

## Pre-conditions

| Check | Required |
|-------|----------|
| brand_config.yaml exists | For Workflow 2 and 3 |
| brand_audit score >= 0.85 | For Workflow 3 |
| N01 research complete | For Workflow 1 step 3 |

## Post-conditions

| Artifact | Location |
|----------|----------|
| brand_config.yaml | .cex/brand/brand_config.yaml |
| Brand Book | N06_commercial/P05_output/ |
| Pricing artifacts | N06_commercial/P05_output/ |
| Propagation | N0X_*/config/brand_context.md |
| Signal | .cex/runtime/signals/n06_complete.json |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_commercial_nucleus]] | upstream | 0.56 |
| [[p03_sp_commercial_nucleus]] | upstream | 0.50 |
| [[p07_sr_commercial]] | upstream | 0.50 |
| [[spec_n06_brand_verticalization]] | upstream | 0.47 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.47 |
| [[p03_sp_brand_nucleus]] | upstream | 0.46 |
| [[p02_agent_brand_nucleus]] | upstream | 0.45 |
| [[p12_dr_commercial]] | related | 0.43 |
| [[agent_card_n06]] | upstream | 0.42 |
| [[p08_ac_brand_nucleus]] | upstream | 0.42 |
