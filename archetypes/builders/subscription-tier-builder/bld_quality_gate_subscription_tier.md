---
kind: quality_gate
id: p11_qg_subscription_tier
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for subscription_tier
quality: 9.1
title: "Quality Gate Subscription Tier"
version: "1.0.0"
author: n03_builder
tags: [subscription_tier, builder, quality_gate]
tldr: "Artifact-level quality gate: validates subscription_tier YAML structure, Stripe/Chargebee field compliance, and pricing integrity (not runtime billing metrics)."
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| schema_fields_present | 100% | == | frontmatter |
| price_integrity | valid | == | price object |
| score_minimum | 8.0 | >= | artifact |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Missing or malformed YAML |
| H02 | ID matches `^p11_st_[a-z][a-z0-9_]+\.yaml$` | ID does not conform |
| H03 | `kind` field == `subscription_tier` | kind is wrong or missing |
| H04 | `tier_name` present and NOT in {bronze, silver, gold, platinum, diamond} | Medal-metaphor naming |
| H05 | `monetization_unit` in {flat, per_seat, per_usage, hybrid} | Invalid or missing |
| H06 | `price.unit_amount` is integer >= 0 (smallest currency unit, cents) | Decimal or negative |
| H07 | `price.currency` is ISO 4217 3-letter code | Invalid currency |
| H08 | `price.interval` in {day, week, month, year} AND `interval_count` is positive int | Non-canonical interval |
| H09 | `feature_matrix` non-empty AND every row has `{feature, included}` minimum | Empty or malformed |
| H10 | `grandfathering_policy` present when `deprecation.status in {legacy, sunset}` | Missing grandfathering on deprecated tier |
| H11 | `quality: null` in frontmatter | Self-scored (must be null) |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Audience specificity | 0.12 | 1.0: JTBD + segment + size; 0.5: segment only; 0.0: "general" |
| D2 | Pricing canonicality | 0.12 | 1.0: Stripe-shaped price object + tax_behavior; 0.5: Stripe-ish; 0.0: freeform |
| D3 | Feature matrix clarity | 0.12 | 1.0: rows with quota+addon_price; 0.5: included-only; 0.0: prose list |
| D4 | Monetization unit fit | 0.10 | 1.0: unit matches product (per_seat for collab, per_usage for API); 0.0: mismatch |
| D5 | Tier differentiation | 0.10 | 1.0: each tier adds 2+ differentiated capabilities; 0.5: 1; 0.0: overlap |
| D6 | Trial & conversion design | 0.08 | 1.0: trial_policy + auto_convert + proration; 0.5: partial; 0.0: absent |
| D7 | Grandfathering discipline | 0.08 | 1.0: price_lock + feature_freeze + migration offer; 0.0: ignored |
| D8 | Expansion MRR hooks | 0.10 | 1.0: upgrade_to + add_ons + seat expansion priced; 0.5: upgrade path only; 0.0: none |
| D9 | Annual/monthly discount economics | 0.08 | 1.0: 15-25% annual discount justified; 0.5: discount no rationale; 0.0: no annual option |
| D10 | Deprecation planning | 0.10 | 1.0: sunset_date + successor_tier documented; 0.0: tier designed without lifecycle |

Weights sum = 1.00.

## Actions
| Score | Action |
|---|---|
| >= 9.5 | GOLDEN: publish to billing system |
| >= 8.0 | PUBLISH: push to Stripe/Chargebee |
| >= 7.0 | REVIEW: return to pricing/product lead |
| < 7.0 | REJECT: rebuild -- price canonicality or feature matrix incomplete |

## Bypass
| condition | approver | audit trail |
|---|---|---|
| Custom enterprise contract (non-standard terms) | CRO + CFO | Contract + decision record |
| Regulated-market pricing exception | Head of Legal | Compliance memo attached |
