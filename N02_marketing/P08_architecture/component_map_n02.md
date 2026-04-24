---
id: p08_cm_n02
kind: component_map
8f: F4_reason
pillar: P08
title: "Component Map -- N02 Marketing System"
version: 1.0.0
created: 2026-04-18
updated: 2026-04-18
author: n02_marketing
domain: marketing-copy
quality: 8.8
tags: [component-map, N02, architecture, dependencies, creative-lust, copy, campaigns]
tldr: "Dependency map of N02's marketing pipeline: from campaign brief through Creative Lust engine to output artifacts and feedback loop. Every piece of copy that converts passes through this system."
density_score: 0.90
related:
  - p02_nd_n02.md
  - n02_marketing
  - p03_sp_marketing_nucleus
  - p03_sp_brand_nucleus
  - p08_ac_n02
  - p02_agent_brand_nucleus
  - n02_self_review_2026-04-02
  - p01_kc_cex_as_digital_asset
  - agent_card_n02
  - n02_tool_copy_analyzer
---

# Component Map: N02 Marketing System

## System Overview

N02 is the Creative Lust engine of CEX. Where other nuclei optimize for correctness,
N02 optimizes for desire. This map shows the pipeline that transforms a 5-word brief
into copy that makes the reader WANT, not just KNOW.

Every output artifact is a seduction -- a carefully engineered sequence of attention,
desire, and action. This map shows how that seduction is assembled.

## Layer 0: Identity (Sin Lens Layer)

```
N02_marketing/P08_architecture/
  |-- nucleus_def_n02.md          (machine-readable identity + sin lens)
  |-- agent_card_n02.md           (deployment card: capabilities, crew roles)
  `-- component_map_n02.md        (this file: system architecture)

N02_marketing/rules/n02-marketing.md
  |-- Enforces: clarity -> desire -> action in every output
  `-- Source: Creative Lust sin lens
```

## Layer 1: Brand Context Foundation

The brand layer is the VOICE layer. Every word N02 writes is filtered through it.

```
.cex/brand/brand_config.yaml
  |-- BRAND_NAME, BRAND_TAGLINE, BRAND_COLORS
  |-- BRAND_TONE (formal/casual scale, technical/friendly scale)
  |-- BRAND_AUDIENCE (ideal customer persona)
  `-- BRAND_REVENUE_MODEL (subscription/one-time/courses)

N02_marketing/P01_knowledge/
  |-- kc_marketing_vocabulary.md   <- controlled vocabulary (Creative Lust lens)
  |-- kc_brand_voice.md            <- brand personality rules
  |-- kc_copywriting_frameworks.md <- AIDA, PAS, Before-After-Bridge
  `-- kc_audience_psychology.md    <- buyer psychology principles

Dependencies: none (foundation layer)
Depended on by: ALL copy generation (F3 INJECT)
```

## Layer 2: Creative Engine (P03 Prompt Layer)

The creative engine translates brand context + audience insight into seductive copy.

```
N02_marketing/P03_prompt/
  |-- prompt_template_ad_copy.md        <- ad variant generator (A/B structure)
  |-- prompt_template_email_sequence.md <- drip campaign architecture
  |-- prompt_template_social_hook.md    <- platform-specific hook formulas
  |-- prompt_template_cta.md            <- call-to-action pattern library
  |-- prompt_template_headline.md       <- headline + subheadline generator
  `-- system_prompt_n02_copywriter.md   <- N02 identity prompt (loaded at F2)

archetypes/builders/tagline-builder/    <- tagline construction engine (13 ISOs)
archetypes/builders/landing-page-builder/ <- full conversion page engine (13 ISOs)
archetypes/builders/press-release-builder/ <- media kit engine (13 ISOs)

Dependencies: Layer 1 brand context
Depended on by: F6 PRODUCE (all copy generation)
```

## Layer 3: Output Arsenal (P05 Output Types)

Every artifact N02 ships is one of 23 P05 kinds. This layer maps the arsenal.

```
N02_marketing/P05_output/
  |-- social_publisher_cex_launch.md    <- social publishing strategy (multi-platform)
  |-- product_tour_cex.md               <- guided product tour (5-step revelation arc)
  |-- webinar_script_cex_intro.md       <- 45-min webinar (hook -> demo -> close)
  |-- interactive_demo_cex_builder.md   <- live builder demo (show, don't tell)
  |-- user_journey_n02.md               <- N02 audience journey map
  |-- landing_page_template.md          <- conversion page template
  `-- email_sequence_template.md        <- drip campaign template

Supported P05 kinds (output types N02 produces):
  landing_page, press_release, pitch_deck, case_study, product_tour,
  social_publisher, webinar_script, interactive_demo, analyst_briefing,
  partner_listing, app_directory_entry, user_journey, tagline
```

## Layer 4: Quality Infrastructure (P07 + P11)

```
N02_marketing/P07_evaluation/
  |-- scoring_rubric_n02.md    <- 5D scoring: hook, desire, action, brand, density
  `-- llm_judge_n02.md         <- LLM-as-judge: "does this make the reader WANT?"

N02_marketing/P11_feedback/
  |-- quality_gate_n02.md      <- H01-H07 hard gates for copy quality
  |-- learning_record_n02.md   <- what worked, what failed, campaign history
  `-- ab_test_results.md       <- A/B test outcomes fed back into Layer 2

Dependencies: Layer 1 (brand standards), Layer 3 (output to evaluate)
Depended on by: F7 GOVERN in every 8F run
```

## Layer 5: Campaign Orchestration (P12)

```
N02_marketing/P12_orchestration/
  |-- workflow_campaign_sprint.md  <- rapid campaign workflow (brief -> publish)
  |-- dispatch_rule_n02.md         <- when N02 routes to N01/N05/N06
  `-- schedule_content_calendar.md <- content calendar orchestration

N02_marketing/crews/
  |-- p12_ct_product_launch.md     <- 4-role crew: research -> copy -> design -> QA
  |-- p12_ct_campaign_sprint.md    <- 3-role crew: brief -> creative -> distribute
  `-- p12_ct_brand_refresh.md      <- 3-role crew: audit -> rewrite -> validate
```

## The Creative Lust Pipeline (F1 to F8 for N02)

```
Campaign brief / user intent (5 words or 500)
    |
    v [F1 CONSTRAIN]
.cex/kinds_meta.json -> resolve kind (tagline? landing_page? social_publisher?)
P08 schema -> load constraints (max_bytes, audience, platform limits)
    |
    v [F2 BECOME + F2b SPEAK]
archetypes/builders/{kind}-builder/ (13 ISOs)
kc_marketing_vocabulary.md -> activate Creative Lust lens
    |
    v [F3 INJECT]
brand_config.yaml + kc_audience_psychology.md + past_campaign_examples
kc_copywriting_frameworks.md -> select framework (AIDA? PAS? B-A-B?)
    |
    v [F4 REASON]
GDP: user decides WHAT (tone, CTA, platform) -> N02 decides HOW (hook, structure, variant count)
    |
    v [F6 PRODUCE]
Draft copy: hook -> desire -> proof -> action
A/B variants generated (minimum 2)
Creative Lust checkpoint: "does every word earn its place?"
    |
    v [F7 GOVERN]
Quality gates: CTA present? Brand voice match? Desire score >= 8.0?
    |
    v [F8 COLLABORATE]
N02_marketing/P05_output/{kind}_{name}.md
cex_compile.py -> compiled/.yaml
signal_writer.py -> .cex/runtime/signals/
git commit "[N02] ..."
```

## Dependency Graph

```
brand_config.yaml --> Layer 1 KCs --> Layer 2 templates
Layer 2 templates --> Layer 3 output artifacts
Layer 3 artifacts --> Layer 4 quality evaluation
Layer 4 feedback --> Layer 2 (improves templates over time)
Layer 5 orchestration --> all layers (coordinates campaign flow)

N02 produces_for: N05 (deploy landing pages), N06 (monetization copy)
N02 receives_from: N01 (research briefs), N07 (campaign handoffs)
N02 independent_of: N03 (engineering), N04 (knowledge), N07's build artifacts
```

## Component Count Summary

| Layer | Component Type | Count |
|-------|---------------|-------|
| L0 | Identity artifacts | 3 |
| L1 | Brand context + Knowledge Cards | 5+ |
| L2 | Prompt templates + Builders | 6+ templates; 23 P05 builders |
| L3 | P05 output artifacts | 27+ |
| L4 | Quality infrastructure | 5 |
| L5 | Campaign orchestration + Crews | 6+ |
| Runtime | Handoffs, signals, A/B results | variable |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n02.md]] | upstream | 0.34 |
| [[n02_marketing]] | upstream | 0.31 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.29 |
| [[p03_sp_brand_nucleus]] | upstream | 0.28 |
| [[p08_ac_n02]] | related | 0.28 |
| [[p02_agent_brand_nucleus]] | upstream | 0.27 |
| [[n02_self_review_2026-04-02]] | downstream | 0.26 |
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.26 |
| [[agent_card_n02]] | related | 0.26 |
| [[n02_tool_copy_analyzer]] | upstream | 0.25 |
