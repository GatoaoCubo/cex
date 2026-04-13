---
id: n06_monetization_audit_2026_04_08
kind: context_doc
pillar: P01
title: "Monetization Portfolio Audit -- N06 Commercial Nucleus"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: monetization-audit
quality: 8.9
tags: [audit, monetization, portfolio, gaps, revenue-streams, N06]
tldr: "Full audit of 60 N06 artifacts. 12 revenue streams mapped: 9 defined, 3 gaps identified. Top gap: API Access Tiers (highest margin, most scalable, product already built). Second: Affiliate Program Structure. Third: Retention/Anti-Churn Program."
density_score: 0.96
---

# Monetization Portfolio Audit -- April 2026

> Audit scope: 60 artifacts in N06_commercial/
> Date: 2026-04-08 | Auditor: N06 Commercial Nucleus
> Mission: ROADMAP_NEXT Wave 1

---

## 1. Portfolio Inventory

### 1.1 Artifact Count by Subdirectory

| Directory | Count | Content |
|-----------|-------|---------|
| output/ | 17 | Business plans, pricing, strategies, audits, brand deliverables |
| knowledge/ | 11 | Brand KCs, competitive positioning, monetization models |
| architecture/ | 3 | Agent card, funnel pattern, pricing pattern |
| schemas/ | 5 | Brand config, brand book, brand voice, brand audit, content order |
| prompts/ | 6 | Brand discovery, audit, extraction, config, system prompt, template |
| orchestration/ | 4 | Dispatch rules, workflows (commercial + content monetization) |
| tools/ | 3 | Pricing experiment, funnel diagnostic, content monetization tool |
| agents/ | 3 | Agent def, axioms, mental model |
| memory/ | 3 | Brand decisions, commercial learning record, pricing optimization |
| feedback/ | 1 | Quality gate commercial |
| quality/ | 1 | Scoring rubric |
| root | 2 | README, agent_card_n06 |
| **TOTAL** | **60** | |

### 1.2 Revenue Streams Mapped

| # | Revenue Stream | Artifact(s) | Status | Est. Revenue (Y1) |
|---|---------------|-------------|--------|-------------------|
| 1 | **Course (Builder R$497)** | output_monetization_business_plan.md | DEFINED | R$120K-240K |
| 2 | **Course (Master R$997)** | output_monetization_business_plan.md | DEFINED | R$60K-180K |
| 3 | **SaaS Subscription (4 tiers)** | output_content_factory_business_model.md, content_factory_pricing.md | DEFINED | R$150K-480K |
| 4 | **Credit Packs (one-time)** | content_factory_pricing.md, knowledge_card_content_monetization.md | DEFINED | R$30K-120K |
| 5 | **Template Packs (R$97-497)** | strategy_claude_native.md | DEFINED | R$20K-50K |
| 6 | **Consulting/Setup (R$5-15K)** | output_monetization_business_plan.md, strategy_claude_native.md | DEFINED | R$25K-100K |
| 7 | **Enterprise Licensing (R$50-200K)** | strategy_claude_native.md | DEFINED | R$50K-200K |
| 8 | **White-Label (R$10K + 15%)** | strategy_claude_native.md | DEFINED | R$30K-100K |
| 9 | **Community (Insiders R$97/mo)** | strategy_claude_native.md | DEFINED | R$23K-58K |
| 10 | **API Access Tiers** | -- | **GAP** | R$100K-400K (est.) |
| 11 | **Affiliate Program** | Mentioned only (25% commission) | **GAP** | Revenue enabler (15-20% of course sales) |
| 12 | **Retention/Anti-Churn** | pattern_funnel_architecture.md (generic) | **GAP** | Revenue protector (saves 6-8% MRR) |

---

## 2. Gap Analysis

### GAP #1: API Access Tiers (HIGHEST PRIORITY)

**What's missing**: cex_sdk/ has 78 Python files (4,504 lines) -- the product exists. But there is zero pricing, zero access control, zero documentation for external developers who want to integrate CEX programmatically.

**Why it matters**:
- **Scalability**: API access is the most scalable revenue model. Zero marginal cost (runs on customer infra).
- **Market**: Agencies and SaaS companies want to embed CEX in their own products. Current model forces them to use CLI.
- **Existing demand**: The Factory tier (R$3,997/mo) already promises "API access" but no artifact defines what that means.
- **Compound effect**: API access + Content Factory = automated content at scale for agencies.

**Revenue potential**: R$100K-400K/year based on:
- 10-40 API customers at R$500-2,000/month
- Usage-based overage fees
- Enterprise API contracts (R$10K+/month)

**Action**: Build `api_access_pricing.md` (content_monetization) -- DONE in this wave.

### GAP #2: Affiliate Program Structure (MEDIUM PRIORITY)

**What's missing**: Multiple artifacts mention "25% affiliate commission" but no dedicated artifact defines:
- Affiliate tiers (standard vs premium)
- Commission structure per product type (course, SaaS, consulting)
- Marketing materials (swipe files, banners, landing page copy)
- Tracking and attribution rules (first-click, last-click, 30-day cookie)
- Payout schedule and minimum threshold
- Recruitment strategy and onboarding flow

**Why it matters**:
- Affiliates can drive 15-20% of course revenue with zero upfront cost
- Dev/consultant communities are ideal affiliate channels for CEX
- Without structure, affiliates don't know what to promote or how

**Revenue potential**: Revenue enabler -- if courses generate R$180K, affiliates add R$27-36K in attributed sales.

**Action**: Recommended for next wave. Kind: content_monetization, path: N06_commercial/output/affiliate_program.md.

### GAP #3: Retention/Anti-Churn Program (MEDIUM PRIORITY)

**What's missing**: The funnel_diagnostic_tool.md identifies churn as a metric and the business plan models 6-8% monthly churn. But no artifact defines:
- Win-back email sequences (7/14/30 day inactivity triggers)
- Usage-based loyalty discounts (>80% utilization = 10% renewal discount)
- Annual lock-in incentives (beyond the existing 20% annual discount)
- Churn prediction signals (credit balance dropping, login frequency declining)
- Exit interview/survey flow to capture churn reasons
- Pause option (freeze subscription at R$0 for 30 days instead of cancel)

**Why it matters**:
- At 6% monthly churn, you lose 52% of customers per year
- Reducing churn from 6% to 4% = 20% more retained MRR = R$50-100K additional revenue
- Retention is 5-7x cheaper than acquisition (AX pattern from funnel_architecture)

**Revenue potential**: Revenue protector -- saves R$50-100K/year in otherwise-churned MRR at scale.

**Action**: Recommended for next wave. Kind: content_monetization, path: N06_commercial/output/retention_program.md.

---

## 3. Portfolio Health Assessment

### 3.1 Strengths

| Strength | Evidence |
|----------|---------|
| **Course pricing well-modeled** | 3 scenarios (conserv/base/optimist), unit economics, pricing psychology |
| **Content Factory costed** | Per-format costs validated against real API pricing |
| **Multi-platform checkout** | Stripe + MercadoPago + Hotmart + Digistore24 covered in KC |
| **Brand system monetizable** | Brand config as entry point, brand propagation as value |
| **Competitive positioning clear** | 10+ competitors mapped with real pricing |

### 3.2 Weaknesses

| Weakness | Impact | Fix |
|----------|--------|-----|
| **No API pricing** | Blocks Factory tier differentiation | Build this wave (done) |
| **Affiliate program vaporware** | 15-20% potential revenue unrealized | Next wave |
| **No churn prevention** | 52% annual customer loss at 6% monthly | Next wave |
| **No partner/reseller program** | Enterprise channel undeveloped | H2 2026 |
| **No usage analytics as product** | Analytics data could be upsell | Future |

### 3.3 Coverage Matrix

| Revenue Lever | Covered? | Artifact Quality |
|--------------|---------|-----------------|
| Acquisition (new customers) | YES | Strong -- GTM plan, funnel, competitive positioning |
| Conversion (leads to paid) | YES | Strong -- pricing psychology, checkout flows |
| Expansion (upsell) | PARTIAL | Tiers exist, triggers documented, but no playbook |
| Retention (reduce churn) | WEAK | Generic funnel pattern only |
| Activation (first value) | PARTIAL | Onboarding mentioned in consulting, no standalone |
| Referral (viral growth) | WEAK | Affiliate mentioned but not structured |

---

## 4. Recommendations (Priority Order)

| # | Action | Effort | Revenue Impact | Timeline |
|---|--------|--------|---------------|----------|
| 1 | **API Access Tiers** (building now) | Medium | R$100-400K/yr | This wave |
| 2 | **Affiliate Program Structure** | Low | +15-20% of course revenue | Next wave |
| 3 | **Retention/Anti-Churn Program** | Medium | Save R$50-100K/yr | Next wave |
| 4 | Activation/Onboarding Playbook | Low | Improve trial-to-paid 10-15% | Month 2 |
| 5 | Partner/Reseller Channel | High | R$100K+ enterprise pipeline | H2 2026 |
| 6 | Usage Analytics as Upsell | Medium | R$50-100K/yr at scale | H2 2026 |

---

*Audit complete. 60 artifacts. 12 revenue streams. 3 gaps. 1 being closed this wave.*
*N06 Commercial Nucleus -- every gap is a revenue leak.*

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**
