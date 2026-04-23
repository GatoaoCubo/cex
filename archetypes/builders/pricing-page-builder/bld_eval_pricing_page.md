---
kind: quality_gate
id: p05_qg_pricing_page
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for pricing_page
quality: 9.0
title: "Quality Gate Pricing Page"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pricing_page, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for pricing_page"
domain: "pricing_page construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_pricing_page
  - p05_qg_user_journey
  - p05_qg_integration_guide
  - p05_qg_product_tour
  - bld_instruction_pricing_page
  - p07_qg_eval_metric
  - kc_subscription_tier
  - p11_qg_usage_report
  - p03_qg_prompt_technique
  - p02_qg_customer_segment
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| metric | threshold | operator | scope |
|---|---|---|---|
| Tier comparison clarity | 3+ | >= | Pricing tiers |
| Conversion copy effectiveness | 80% | >= | Call-to-action buttons |
| Currency symbol consistency | 100% | == | All price displays |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax |
| H02 | ID matches pattern ^p05_pp_[a-z][a-z0-9_]+.md$ | Invalid schema ID |
| H03 | kind field matches 'pricing_page' | Incorrect kind value |
| H04 | At least 3 pricing tiers | <3 tiers defined |
| H05 | Conversion copy includes CTA verbs | Missing "Buy", "Sign up", etc. |
| H06 | No missing currency symbols | Missing $, €, or ₽ |
| H07 | Tier comparison table present | Table missing or incomplete |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Tier clarity | 0.15 | 1-5 (less clear to very clear) |
| D02 | Conversion copy | 0.20 | 1-5 (weak to compelling) |
| D03 | Visual hierarchy | 0.10 | 1-5 (poor to excellent) |
| D04 | Currency accuracy | 0.10 | 1-5 (errors to perfect) |
| D05 | Comparison completeness | 0.15 | 1-5 (sparse to comprehensive) |
| D06 | CTA prominence | 0.10 | 1-5 (hidden to obvious) |
| D07 | Mobile usability | 0.20 | 1-5 (broken to seamless) |

## Actions
(Table: Score | Action)
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-publish with celebration |
| PUBLISH | >=8.0 | Publish immediately |
| REVIEW | >=7.0 | Require stakeholder review |
| REJECT | <7.0 | Reject and request major fixes |

## Bypass
(Table: conditions, approver, audit trail)
| conditions | approver | audit trail |
|---|---|---|
| Emergency launch | CTO | Slack notification + email |

## Examples

## Golden Example
---
title: "Pricing - ClickUp"
description: "Compare plans to find the right fit for your team"
---
# Pricing

**Choose the plan that fits your workflow**

| Feature              | Basic ($12/user/month) | Pro ($29/user/month) | Enterprise (Custom) |
|----------------------|------------------------|----------------------|---------------------|
| Task Management      | [YES]                     | [YES]                   | [YES]                  |
| Integrations         | 10                     | 50                   | Unlimited           |
| Storage              | 5GB                    | 20GB                 | Unlimited           |
| Priority Support     | Email                  | 24/7 Chat            | Dedicated Account   |
| Team Members         | 1                      | 10                   | Unlimited           |

**Why upgrade?**
Pro plan users report 40% faster project completion. Enterprise customers get custom workflows and API access.
--> [Start free trial](#) or [Contact sales](#)

## Anti-Example 1: Missing clear CTAs
---
# Pricing

**Our plans**

| Feature              | Starter | Growth | Enterprise |
|----------------------|---------|--------|------------|
| Users                | 1       | 5      | 50+        |
| Storage              | 10GB    | 50GB   | Unlimited  |
| Support              | Email   | Chat   | Phone      |

*Choose the right plan for your needs*

## Why it fails
No clear call-to-action buttons or links. Users can't easily convert without knowing where to click.

## Anti-Example 2: Vague value propositions
---
# Pricing

**Our plans**

| Feature              | Basic | Pro | Premium |
|----------------------|-------|-----|---------|
| Feature A            | Yes   | Yes | Yes     |
| Feature B            | No    | Yes | Yes     |
| Feature C            | No    | No  | Yes     |
| Price                | $9    | $29 | $99     |

*Find the plan that matches your needs*

## Why it fails
Features are named generically ("Feature A") without explaining their value. Users can't understand what differentiates tiers.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
