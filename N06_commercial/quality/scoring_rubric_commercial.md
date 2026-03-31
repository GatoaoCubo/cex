---
id: p07_sr_commercial_evaluation
kind: scoring_rubric
pillar: P07
title: Rubric — Commercial Output Evaluation
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n06_commercial
framework: Commercial Output Evaluation
target_kinds: [pricing_strategy, course_outline, funnel_copy, upsell_sequence, revenue_model]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: semi-automated
domain: commercial-monetization
quality: 8.9
tags: [scoring-rubric, commercial, N06, pricing, funnels, conversion]
tldr: 5-dimension rubric for N06 output — Offer Clarity (25%), Pricing Logic (25%), Funnel Coherence (20%), Copy Persuasion (20%), Revenue Potential (10%).
density_score: 0.92
---

## Framework Overview

This rubric evaluates N06 commercial artifacts across five dimensions specific to revenue-generating output.
The framework is calibrated to the infoprodutos/digital products market (primary CEX commercial domain).

## Dimensions

| Dimension | Weight | Scale | What it Measures |
|-----------|--------|-------|-----------------|
| D1: Offer Clarity | 25% | 0-10 | Is the product, audience, price, and transformation unmistakably clear? |
| D2: Pricing Logic | 25% | 0-10 | Is the price justified with value rationale, tiers, and revenue model? |
| D3: Funnel Coherence | 20% | 0-10 | Does each funnel stage connect logically with the right artifact and CTA? |
| D4: Copy Persuasion | 20% | 0-10 | Does the copy use proven structure (hook, agitate, reveal, proof, CTA)? |
| D5: Revenue Potential | 10% | 0-10 | Does the artifact generate real revenue? Is the model sustainable and scalable? |

## Dimension Criteria

### D1: Offer Clarity (25%)
| Score | Description |
|-------|-------------|
| 10 | Audience named precisely, transformation stated as measurable outcome, offer components listed explicitly |
| 8-9 | Clear audience + transformation, minor missing specifics (e.g., platform not named) |
| 6-7 | General audience and transformation, some specificity gaps |
| 4-5 | Vague audience ("business owners"), vague transformation ("improve results") |
| 0-3 | No defined audience or transformation. Generic placeholder content. |

### D2: Pricing Logic (25%)
| Score | Description |
|-------|-------------|
| 10 | 3-tier table + value rationale + revenue model (units × price × conversion) + psychological anchoring |
| 8-9 | Tiers present, rationale documented, revenue model with minor gaps |
| 6-7 | Tiers present but no rationale or revenue model |
| 4-5 | Single flat price, no tiers, no justification |
| 0-3 | No pricing at all, or price range without commitment |

### D3: Funnel Coherence (20%)
| Score | Description |
|-------|-------------|
| 10 | All stages (TOFU/MOFU/BOFU) defined, conversion benchmarks per stage, artifact per stage, natural progression |
| 8-9 | Full funnel map, benchmarks present, minor stage gaps |
| 6-7 | 2 of 3 stages defined, missing benchmarks |
| 4-5 | Only one stage addressed, no stage-to-stage connection |
| 0-3 | No funnel structure. Disconnected fragments. |

### D4: Copy Persuasion (20%)
| Score | Description |
|-------|-------------|
| 10 | Hook calls out exact avatar, agitates specific pain, reveals unique mechanism, proof present, CTA with urgency |
| 8-9 | Strong hook + structure, minor proof or urgency gap |
| 6-7 | Some structure present but hook is generic or proof is missing |
| 4-5 | Flat copy, no hook-agitate-reveal structure, generic CTA |
| 0-3 | No persuasive copy structure. "Buy now" level. |

### D5: Revenue Potential (10%)
| Score | Description |
|-------|-------------|
| 10 | Scalable model, upsell path defined, LTV > 2x AOV, projected ROAS >= 3x |
| 8-9 | Clear revenue path, upsell defined, reasonable LTV projections |
| 6-7 | Revenue model present but no upsell or LTV path |
| 4-5 | One-time sale only, no recurring or upsell revenue path |
| 0-3 | No revenue model. No path beyond initial transaction. |

## Scoring Formula

```
final_score = (D1 × 0.25) + (D2 × 0.25) + (D3 × 0.20) + (D4 × 0.20) + (D5 × 0.10)
```

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Mark as reference example. Add to calibration set. |
| PUBLISH | >= 8.0 | Deliver to user. Proceed to F8. |
| REVIEW | 7.0-7.9 | Return with D-gate feedback. Revise specific dimension. |
| REJECT | < 7.0 | Return to F4 REASON. Rebuild from plan. |

## Calibration Examples

| Level | Score | Profile |
|-------|-------|---------|
| GOLDEN | 9.7 | "Curso Precificação para Designers": full 3-tier, transformation arc, VSL, upsell sequence, R$99k revenue projection validated |
| PUBLISH | 8.3 | Course outline + pricing tiers, transformation arc defined, missing upsell sequence details |
| REVIEW | 7.2 | Pricing tiers present but no revenue model; copy has hook but no proof section |
| REJECT | 5.8 | Generic course outline, single flat price, no funnel, no audience specificity |

## Automation

| Dimension | Status | Method |
|-----------|--------|--------|
| D1 Offer Clarity | semi-automated | Check for audience keywords + transformation language |
| D2 Pricing Logic | semi-automated | Detect tier table + revenue calculation pattern |
| D3 Funnel Coherence | manual | Stage review by N06 agent |
| D4 Copy Persuasion | semi-automated | Hook/CTA structure pattern match |
| D5 Revenue Potential | manual | LTV/ROAS projection review |
