---
id: p03_brand_discovery_interview
kind: prompt_template
pillar: P03
title: "Brand Discovery Interview — 3-Phase Progressive Depth"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-discovery
quality: null
tags: [prompt, brand, discovery, interview, n06]
tldr: "12-15 question progressive interview in 3 phases: Essence (who), Audience (for whom), Expression (how). Extracts brand DNA for brand book generation."
density_score: 0.94
---

# Brand Discovery Interview

## Purpose
Extract brand DNA through progressive questioning. Output feeds into Brand Book Generator.

## Phase 1 — ESSENCE (Who are you?) — Questions 1-5

### Q1: Origin
"What problem made you start this? Tell me the moment you decided to build {{BRAND_NAME}}."
> Extracts: BRAND_STORY, BRAND_MISSION

### Q2: Transformation Promise
"If your ideal customer uses your product for 90 days, what changes in their life? Be specific — before vs. after."
> Extracts: BRAND_TRANSFORMATION (From X to Y through Z)

### Q3: Core Values
"Name 3-5 non-negotiable principles. What would you NEVER compromise, even for revenue?"
> Extracts: BRAND_VALUES

### Q4: Vision
"It's 2030. Your brand succeeded beyond expectations. What does the world look like?"
> Extracts: BRAND_VISION

### Q5: Anti-Identity
"What does your brand REFUSE to be? What competitor behavior disgusts you?"
> Extracts: BRAND_ARCHETYPE_SHADOW, BRAND_VOICE_DONT

## Phase 2 — AUDIENCE (For whom?) — Questions 6-9

### Q6: Ideal Customer Profile
"Describe your best customer. Not demographics — describe their daily frustrations and secret aspirations."
> Extracts: BRAND_ICP, BRAND_ICP_FEARS, BRAND_ICP_ASPIRATIONS

### Q7: Customer Language
"What exact words does your customer use to describe their problem? Copy their language."
> Extracts: voice calibration, funnel copy seeds

### Q8: Competitive Landscape
"Who else solves this problem? Why do some customers choose them instead of you?"
> Extracts: BRAND_COMPETITORS, BRAND_DIFFERENTIATOR

### Q9: Category Ownership
"Complete: 'We are the only _____ that _____.' If you can't fill this, we need to work on positioning."
> Extracts: BRAND_CATEGORY, BRAND_UVP

## Phase 3 — EXPRESSION (How do you show up?) — Questions 10-15

### Q10: Voice
"If your brand were a person at a dinner party, how would they talk? Formal or casual? Funny or serious? Warm or analytical?"
> Extracts: BRAND_VOICE_TONE, 5D scores (formality, enthusiasm, humor, warmth, authority)

### Q11: Archetype Resonance
"Which of these best describes your brand's personality? (Present 12 Jungian archetype cards with descriptions)"
> Extracts: BRAND_ARCHETYPE

### Q12: Visual Instinct
"Show me 3 brands whose LOOK you admire (not their product — their aesthetic). What draws you to them?"
> Extracts: BRAND_STYLE, BRAND_COLORS direction

### Q13: Content Pillars
"What 3-5 topics could your brand talk about EVERY day without running out of things to say?"
> Extracts: BRAND_CONTENT_PILLARS

### Q14: Revenue Model
"How do you want to make money? One-time sale, subscription, marketplace, courses, or hybrid?"
> Extracts: BRAND_PRICING_MODEL, BRAND_TIERS

### Q15: Platform & Market
"Where are your customers? Brazil, global, or both? Portuguese or English? Hotmart or Stripe?"
> Extracts: BRAND_LANGUAGE, BRAND_CURRENCY, BRAND_PAYMENT_PROVIDERS, BRAND_ICP_LOCATION

## Extraction Rules

1. After all phases complete, synthesize into Brand Book using `brand_book_generator.md`
2. Never skip Phase 1 — essence must be clear before audience or expression
3. If answers are vague, probe deeper: "Can you give me a specific example?"
4. Record exact customer language (Q7) — this feeds directly into funnel copy
5. Archetype selection (Q11) must be validated against answers from Q1-Q10 for coherence
