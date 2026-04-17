---
id: kc_marketing_vocabulary
kind: knowledge_card
pillar: P01
nucleus: n02
title: "N02 Marketing Controlled Vocabulary -- Canonical Terms"
version: 1.0.0
quality: null
tags: [knowledge_card, controlled_vocabulary, marketing_terms, ubiquitous_language, P01, n02_marketing]
domain: marketing
type: controlled_vocabulary
status: active
---

# N02 Marketing Controlled Vocabulary

## Purpose

This is N02's language model. Every artifact N02 generates uses THESE terms --
not synonyms, not creative alternatives, not industry jargon from competing frameworks.
Vocabulary drift is how smart systems accumulate confusion. This KC prevents it.

Load at F2b SPEAK before any artifact generation.

---

## Canonical Terms

| Term | Definition | N02 Application Context | Anti-pattern |
|------|-----------|------------------------|-------------|
| `conversion_rate_optimization` (CRO) | Systematic process of increasing the percentage of users who take desired actions | Applied at BOFU stage; governs CTA testing, landing page copy, friction removal | "conversion hacking", "optimize for sales" |
| `click_through_rate` (CTR) | Ratio of users clicking a link to total users seeing it (clicks / impressions) | Primary MOFU metric; measured per asset per platform in cohort_analysis | "engagement rate" (different), "click rate" |
| `cost_per_acquisition` (CPA) | Total cost divided by number of acquisitions (signups, purchases, demos booked) | BOFU efficiency metric; used in ab_test_config to evaluate paid variants | "cost per lead" (upstream), "cost per sale" (downstream -- distinct) |
| `A_B_testing` (split testing) | Controlled experiment comparing two variants to determine which performs better | Governed by ab_test_config_n02.md; requires statistical significance before winner declaration | "multivariate testing" (different -- tests multiple variables simultaneously) |
| `funnel_stage` | Position in the buyer's journey: TOFU (awareness), MOFU (consideration), BOFU (decision) | Drives hook_type, CTA style, urgency level in action_prompt_n02_copy.md | "stage of the funnel", "buyer stage", "pipeline stage" |
| `TOFU_MOFU_BOFU` | Top/Middle/Bottom of Funnel -- three-stage demand generation model | Content ratio target: 60:30:10 default (see user_journey_n02.md) | "top of the funnel content", "awareness-stage" (use TOFU) |
| `brand_voice` | Consistent personality and tone expressed through all brand communications | One of six modes (bold/conversational/professional/playful/authoritative/empathetic); set in campaign brief | "brand personality", "tone of voice" (acceptable synonym but use brand_voice in artifacts) |
| `content_pillar` | Core topic category around which a brand builds its content strategy | 3-5 pillars per brand; each campaign should map to one primary pillar | "content bucket", "topic cluster" (SEO context -- different), "content category" |
| `editorial_calendar` | Planned schedule of content publication across platforms and formats | Derived from workflow_campaign_pipeline.md (F4 PLAN output); maps asset to date, platform, format | "content calendar" (acceptable but use editorial_calendar in artifacts), "posting schedule" |
| `performance_creative` | Ad creative optimized specifically for measurable performance outcomes (CVR, CPA) | Distinct from brand creative; requires CTA, urgency, and direct response structure | "paid social ad", "performance ad", "direct response creative" |
| `retargeting` | Serving ads to users who have previously interacted with brand content or website | Attribution window governed in campaign brief (default 30 days); requires behavioral_cohort tracking | "remarketing" (Google's term -- same concept, use retargeting), "re-engagement" |
| `lookalike_audience` | Audience modeled to resemble a seed audience based on behavioral similarity | Configured in AudienceSpec.lookalike_source; improves TOFU reach efficiency | "similar audience" (Meta's UI label -- use lookalike_audience in artifacts) |
| `social_proof` | Evidence that others have validated a decision (testimonials, reviews, user counts) | Hook type in action_prompt_n02_copy.md; most effective for MOFU consideration content | "testimonials" (subset), "reviews" (subset), "word of mouth" (offline equivalent) |
| `urgency_scarcity` | Persuasion mechanism using time pressure (deadline) or limited availability (scarcity) | Urgency trigger field in campaign brief; validated by content_filter_n02.md for authenticity | "FOMO" (colloquial), "fear of missing out" (colloquial -- map to urgency_trigger) |
| `ICP` (Ideal Customer Profile) | Detailed description of the hypothetical perfect customer for a product or service | Defined per segment in customer_segment_n02.md; drives hook_type and tone selection | "target audience" (broader), "buyer persona" (individual-level, ICP is company-level) |
| `jobs_to_be_done` (JTBD) | Framework describing the functional and emotional tasks a customer hires a product to accomplish | Used in AudienceSpec.pain_points field; drives pain-hook copy generation | "user needs", "pain points" (narrower -- pain_points are the symptom; JTBD is the cause) |
| `message_market_fit` | Degree to which a specific message resonates with a specific market segment | Measured via CTR + engagement_rate correlation to segment; optimized by self_improvement_loop | "product-market fit" (different -- PMF is the product; MMF is the message) |
| `hook_framework` | Structured approach to opening a piece of content to capture attention immediately | Five types in N02: pain, curiosity, authority, social_proof, data; assigned per funnel_stage | "intro", "opening line", "attention grabber" (use hook in artifacts) |
| `value_proposition_canvas` | Framework aligning customer profile (pains, gains, jobs) with value map (pain relievers, gain creators) | Used in SEG definitions and MOFU copy strategy; ensures message-market fit | "value prop" (shorthand OK in conversation, use full term in artifacts) |
| `brand_architecture` | Structural organization of a brand's portfolio (monolithic, endorsed, pluralistic) | Governs how product/feature naming appears in copy; affects brand_voice consistency | "brand hierarchy", "brand structure" |
| `tone_of_voice_matrix` | Structured mapping of how brand voice shifts across channels, audiences, and contexts | Implemented in validation_schema_content_spec.md (tone_rule_matrix); governs L1 filtering | "voice guidelines", "tone guide" |

---

## Cross-Nucleus Shared Terms (DO NOT REDEFINE)

These terms are defined in N00_genesis and must not be redefined here:

| Term | Source | N02 Usage Note |
|------|--------|---------------|
| `kind` | N00_genesis | Artifact type -- e.g. action_prompt, workflow, ab_test_config |
| `pillar` | N00_genesis | P01-P12 domain grouping for all artifacts |
| `quality_gate` | N00_genesis | F7 GOVERN validation; N02 uses validation_schema_content_spec.md as gate |
| `8F pipeline` | N00_genesis | F1-F8 (+ F9-F12 for campaign lifecycle) |
| `signal` | N00_genesis | F8 COLLABORATE completion notification to n07 |

---

## Domain-Specific Extensions (N02-Introduced Terms)

| New Term | Definition | Maps to Industry Standard |
|----------|-----------|--------------------------|
| `campaign_lifecycle` | Extended 8F pipeline for campaigns: F1-F8 (build) + F9-F12 (measure + evolve) | marketing_funnel + attribution_model + CRO loop |
| `copy_density` | Ratio of high-information words to total words in a copy asset | readability_score (Flesch-Kincaid) + information_density |
| `hook_to_body_ratio` | Proportion of copy effort allocated to hook vs. body vs. CTA | attention_allocation_model |
| `segment_message_fit_score` | Quantified alignment between a copy asset and a target ICP segment | message_market_fit (quantified) |
| `creative_fatigue` | Degradation of ad performance from repeated exposure to same creative | frequency_capping + creative_refresh_cadence |
| `content_calendar_cadence` | Platform-specific publishing rhythm (posts per day/week) | publishing_schedule + frequency |

---

## Rulebook (Promoted from self_improvement_loop)

This section is populated by `self_improvement_loop_n02.md` when hypotheses are promoted.
Initially empty; grows autonomously as campaigns are deployed and measured.

```yaml
promoted_rules:
  # format: {rule_id, statement, confidence, promoted_from_hyp, promoted_at}
  # example:
  # - rule_id: RULE_001
  #   statement: "Pain hooks on LinkedIn outperform curiosity hooks for SEG_02 by 23% CTR"
  #   confidence: 0.96
  #   promoted_from_hyp: hyp_20260501_001
  #   promoted_at: 2026-05-15
```
