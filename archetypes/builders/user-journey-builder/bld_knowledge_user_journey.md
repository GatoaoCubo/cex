---
kind: knowledge_card
id: bld_knowledge_card_user_journey
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for user_journey production
quality: 9.2
title: "Knowledge Card User Journey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [user_journey, builder, knowledge_card]
tldr: "Domain knowledge for user_journey production"
domain: "user_journey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_user_journey
  - p03_sp_user_journey_builder
  - user-journey-builder
  - bld_instruction_user_journey
  - kc_user_journey
  - p10_mem_user_journey_builder
  - p05_qg_user_journey
  - p01_kc_marketing_best_practices
  - bld_examples_user_journey
  - bld_collaboration_user_journey
---

## Domain Overview
User journey mapping documents the end-to-end experience of a customer across all touchpoints from first awareness to post-purchase advocacy. Two foundational frameworks structure journey analysis: AIDA (Awareness, Interest, Desire, Action) -- a funnel model for conversion paths -- and AARRR Pirate Metrics (Acquisition, Activation, Retention, Revenue, Referral) for product/growth teams. Nielsen Norman Group (NNg) defines the gold standard for journey map artifacts: stages, touchpoints, emotional arcs, pain points, and opportunities. Unlike system workflows or onboarding flows, journey maps are human-centered and cross-channel, capturing both digital and offline interactions.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| AIDA Framework | Awareness, Interest, Desire, Action -- classic conversion funnel | Lewis (1898), updated by Hall (1924) |
| AARRR Pirate Metrics | Acquisition, Activation, Retention, Revenue, Referral -- growth framework | Dave McClure (2007), 500 Startups |
| Customer Journey Map (CJM) | Visual artifact: stages, touchpoints, emotions, pain points, opportunities | NNg (Nielsen Norman Group) |
| Service Blueprint | Back-stage view showing processes supporting each touchpoint | Shostack (1984), NNg |
| Touchpoint | Any interaction between user and brand (digital, physical, human) | Forrester Touchpoint Matrix |
| Moment of Truth | Critical touchpoint that decisively shapes perception (FMOT/SMOT/ZMOT) | Procter & Gamble; Google ZMOT (2011) |
| Emotional Arc | Mapping user sentiment (positive/negative) across journey stages | NNg Journey Mapping Guide |
| Drop-off Rate | % of users who abandon at a given funnel stage | Standard analytics metric |
| NPS (Net Promoter Score) | Measures advocacy: "How likely to recommend?" (0-10 scale) | Reichheld (2003), Bain & Company |
| Jobs-to-be-Done (JTBD) | What job is the customer hiring this product to do? | Christensen et al. (2015) |

## AIDA vs. AARRR Comparison

| Framework | Perspective | Stages | Best For |
|-----------|------------|--------|---------|
| AIDA | Marketing/advertising | Awareness -> Interest -> Desire -> Action | Top-of-funnel conversion |
| AARRR | Product/growth | Acquisition -> Activation -> Retention -> Revenue -> Referral | Full product lifecycle |
| NNg CJM | UX research | Discovery -> Research -> Purchase -> Use -> Loyalty | Human-centered design |
| McKinsey CDJ | Consumer behavior | Consider -> Evaluate -> Buy -> Experience -> Advocate -> Bond | Brand loyalty |

## Journey Stage Mapping

| Stage | AIDA | AARRR | Key Metric | Touchpoints |
|-------|------|-------|-----------|------------|
| Discovery | Awareness | Acquisition | Reach, impressions | Ads, SEO, social |
| Consideration | Interest + Desire | Activation | Trial rate, sign-ups | Product demos, reviews |
| Conversion | Action | Revenue | Conversion rate, ARPU | Checkout, pricing page |
| Retention | -- | Retention | D30/D90 retention | Onboarding, support |
| Advocacy | -- | Referral | NPS, referral rate | Community, NPS surveys |

## Industry Standards
- AIDA framework (Lewis 1898) -- marketing funnel standard
- AARRR Pirate Metrics (McClure 2007) -- SaaS/startup growth standard
- NNg Journey Mapping -- UX practitioner gold standard
- Service Blueprint (Shostack 1984, NNg updated) -- operational journey mapping
- Google ZMOT (2011) -- Zero Moment of Truth for discovery stage
- Forrester Customer Experience framework -- enterprise CX measurement

## Common Patterns
1. Start with AARRR to identify which stage has the highest drop-off rate.
2. Use AIDA lens for top-of-funnel journey stages (awareness, interest).
3. Map emotional arc at each stage -- users with positive emotion convert 3x more.
4. Identify Moments of Truth (ZMOT, FMOT, SMOT) and design around them.
5. Run usability tests at conversion stage to uncover hidden friction points.
6. Close the loop: advocacy stage feeds back into acquisition (referral loops).

## Pitfalls
- Confusing journey maps with system workflows: journey maps show user perspective, not system logic.
- Omitting emotional arc: functional steps without emotion data produce useless maps.
- Creating maps without real user data -- assumptions skew the journey.
- Stopping at conversion: retention and advocacy stages drive LTV, not acquisition alone.
- Building channel-specific maps that miss cross-channel friction (e.g., mobile-to-desktop handoff).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_user_journey]] | downstream | 0.45 |
| [[p03_sp_user_journey_builder]] | downstream | 0.44 |
| [[user-journey-builder]] | downstream | 0.43 |
| [[bld_instruction_user_journey]] | downstream | 0.40 |
| [[kc_user_journey]] | sibling | 0.37 |
| [[p10_mem_user_journey_builder]] | downstream | 0.32 |
| [[p05_qg_user_journey]] | downstream | 0.30 |
| [[p01_kc_marketing_best_practices]] | sibling | 0.28 |
| [[bld_examples_user_journey]] | downstream | 0.25 |
| [[bld_collaboration_user_journey]] | downstream | 0.24 |
