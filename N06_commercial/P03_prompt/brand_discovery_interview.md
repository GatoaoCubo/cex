---
id: p03_brand_discovery_interview
kind: prompt_template
pillar: P03
title: "Brand Discovery Interview — 3-Phase Progressive Depth"
version: 2.0.0
created: 2026-04-01
updated: 2026-04-01
author: n06_commercial
domain: brand-discovery
quality: 9.2
tags: [prompt, brand, discovery, interview, n06]
tldr: "15 questions in 3 phases: Essence (who), Audience (for whom), Expression (how). Structured extraction with JSON intermediate, validation checklists, and archetype scoring matrix. Absorbed from legacy marca prompts."
density_score: 0.96
related:
  - n06_kc_competitive_positioning
  - p03_sp_brand_nucleus
  - p03_sp_commercial_nucleus
  - spec_n06_brand_verticalization
  - n06_kc_icp_frameworks
  - p02_agent_commercial_nucleus
  - brand_bootstrap
  - p08_pat_brand_pipeline
  - p01_kc_cex_as_digital_asset
  - p08_ac_commercial_nucleus
---

# Brand Discovery Interview

## Purpose
Extract brand DNA through progressive questioning. Each phase produces structured
intermediate output. Final synthesis feeds Brand Book Generator.

**Pipeline**: Discovery Interview → Archetype Selection → Positioning → Brand Book

---

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

### Phase 1 Output (structured)

```json
{
  "discovery": {
    "core_benefit": "Primary value in 1-2 sentences [from Q1]",
    "audience_persona": {
      "demographics": "From Q2 context clues",
      "psychographics": "From Q3 values + Q5 anti-identity",
      "key_insight": "1-sentence golden insight"
    },
    "transformation_promise": "From [Q2 BEFORE] to [Q2 AFTER] through [Q1 mechanism]"
  },
  "confidence": 0.90
}
```

### Phase 1 Validation
- [ ] Core benefit is specific (not "helps people") and compelling
- [ ] Transformation promise follows From/To/Through format
- [ ] At least 3 values extracted
- [ ] Anti-identity identifies specific competitor behavior, not vague

---

## Phase 2 — AUDIENCE (For whom?) — Questions 6-9

### Q6: Ideal Customer Profile
"Describe your best customer. Not demographics — describe their daily frustrations and secret aspirations."
> Extracts: BRAND_ICP, BRAND_ICP_FEARS, BRAND_ICP_ASPIRATIONS

**Extraction rules (from legacy persona builder):**
```yaml
demographics:
  age_range: [from audience context]
  gender: [predominant or all]
  location: [Brazil focus for PT-BR]
  income_class: [from price_range: popular=C/D, premium=B/C, luxury=A/B]
psychographics:
  values: [3-5 core values from Q6]
  fears: [2-3 primary fears]
  aspirations: [2-3 desires]
  lifestyle: [1-2 sentence description]
behaviors:
  purchase_triggers: [what makes them buy]
  information_sources: [where they research]
  brand_affinities: [brands they already love]
```

### Q7: Customer Language
"What exact words does your customer use to describe their problem? Copy their language."
> Extracts: voice calibration seeds, funnel copy phrases

**Critical**: Record EXACT phrases. These feed directly into:
- Sales page headlines (TOFU)
- Email subject lines (MOFU)
- CTA buttons (BOFU)
- Testimonial prompts

### Q8: Competitive Landscape
"Who else solves this problem? Why do some customers choose them instead of you?"
> Extracts: BRAND_COMPETITORS, BRAND_DIFFERENTIATOR

**Competitive mapping (from legacy positioning prompt):**
```
1. List 3-5 direct competitors
2. Define 2 key positioning dimensions
3. Map each competitor on 2D grid
4. Identify whitespace (unoccupied quadrant)
```

### Q9: Category Ownership
"Complete: 'We are the only _____ that _____.' If you can't fill this, we need to work on positioning."
> Extracts: BRAND_CATEGORY, BRAND_UVP

**Positioning frameworks applied:**
```yaml
UVP formula: "Para [AUDIENCE] que [NEED], [BRAND] e [CATEGORY] que [DIFFERENTIATOR]"
Ries_Trout: "Para [TARGET], [BRAND] e o [CATEGORY] que [BENEFIT] porque [REASON]"
Differentiation: "We are the only [CATEGORY] that [UNIQUE]"
```

### Phase 2 Output (structured)

```json
{
  "audience": {
    "icp": "Full description [Q6]",
    "persona": {
      "demographics": "age, gender, location, income",
      "psychographics": "values, fears, aspirations",
      "language_phrases": ["exact phrase 1", "exact phrase 2", "exact phrase 3"]
    },
    "competitive_map": [
      {"competitor": "C1", "positioning": "how", "gap": "opportunity"},
      {"competitor": "C2", "positioning": "how", "gap": "opportunity"},
      {"competitor": "C3", "positioning": "how", "gap": "opportunity"}
    ],
    "uvp": "Full UVP statement [Q9]",
    "differentiation": "We are the only X that Y [Q9]"
  },
  "confidence": 0.88
}
```

### Phase 2 Validation
- [ ] ICP has all 3 components (demographics, psychographics, behavioral)
- [ ] At least 3 exact customer language phrases captured
- [ ] At least 3 competitors mapped with positioning + gap
- [ ] UVP follows formula and is specific (not generic)
- [ ] Differentiation statement is defensible (competitor cannot claim same)

---

## Phase 3 — EXPRESSION (How do you show up?) — Questions 10-15

### Q10: Voice
"If your brand were a person at a dinner party, how would they talk? Formal or casual? Funny or serious? Warm or analytical?"
> Extracts: BRAND_VOICE_TONE, 5D scores (formality, enthusiasm, humor, warmth, authority)

### Q11: Archetype Resonance
"Which of these best describes your brand's personality?"

**Present the 12 Jungian archetype cards:**

| Archetype | Desire | Voice | When to choose |
|-----------|--------|-------|----------------|
| Innocent | Happiness, simplicity | Warm, optimistic | Audience fears complexity |
| Explorer | Freedom, authenticity | Adventurous, bold | Audience feels trapped |
| Sage | Truth, understanding | Educational, clear | Audience seeks knowledge |
| Hero | Mastery, courage | Motivational, direct | Audience wants to prove worth |
| Rebel | Revolution, change | Provocative, bold | Audience resents status quo |
| Magician | Transformation | Visionary, inspiring | Audience wants breakthrough |
| Everyman | Belonging, connection | Friendly, accessible | Audience wants community |
| Lover | Intimacy, connection | Sensual, warm | Audience values experience |
| Jester | Joy, playfulness | Funny, irreverent | Audience values fun |
| Caregiver | Protection, nurture | Gentle, supportive | Audience needs safety |
| Creator | Innovation, expression | Creative, inspired | Audience values originality |
| Ruler | Control, order | Authoritative, confident | Audience respects power |

**Archetype selection criteria (from legacy archetype_selection prompt):**
1. **Audience alignment**: Which archetype resonates with target fears/desires?
2. **Category fit**: What archetypes work in this market segment?
3. **Differentiation**: What archetypes do competitors NOT use?
4. **Promise alignment**: Which supports the transformation arc?

**Effective pairs:**
- Hero + Caregiver: "Strength + Protection"
- Sage + Ruler: "Knowledge + Authority"
- Explorer + Creator: "Adventure + Innovation"
- Magician + Creator: "Transformation + Innovation"

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

### Phase 3 Output (structured)

```json
{
  "archetype": {
    "primary": {"name": "SAGE", "desire": "Truth", "voice": "Educational", "visual_direction": "Navy + gray"},
    "secondary": {"name": "MAGICIAN", "complement": "Adds transformation + vision"},
    "justification": "Why this combination for THIS brand [2-3 sentences]",
    "competitor_gap": "What competitors use and why this is different"
  },
  "positioning": {
    "uvp": "Full UVP statement",
    "differentiation_statement": "We are the only X that Y",
    "positioning_statement": "Full Ries and Trout statement"
  },
  "confidence": 0.92
}
```

### Phase 3 Validation
- [ ] Primary archetype aligns with audience desires from Phase 2
- [ ] Secondary archetype complements without conflicting
- [ ] Competitor archetype gap identified
- [ ] 5D voice scores are integers 1-5
- [ ] At least 3 content pillars defined
- [ ] Revenue model explicitly named

---

## Final Synthesis

After all 3 phases, produce:

1. **Structured JSON** combining all phase outputs (for machine processing)
2. **Brand Book** via `brand_book_generator.md` (for human reading)
3. **brand_config.yaml** via `brand_config_extractor.md` (for system propagation)

## Execution Rules

1. Never skip Phase 1 — essence must be clear before audience or expression
2. If answers are vague, probe deeper: "Can you give me a specific example?"
3. Record exact customer language (Q7) — feeds directly into funnel copy
4. Archetype selection (Q11) must be validated against Q1-Q10 answers for coherence
5. Each phase must pass its validation checklist before advancing
6. Output confidence scores: 0.90+ = proceed, 0.70-0.89 = probe deeper, < 0.70 = restart phase

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_kc_competitive_positioning]] | upstream | 0.34 |
| [[p03_sp_brand_nucleus]] | related | 0.31 |
| [[p03_sp_commercial_nucleus]] | related | 0.31 |
| [[spec_n06_brand_verticalization]] | downstream | 0.31 |
| [[n06_kc_icp_frameworks]] | upstream | 0.30 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.29 |
| [[brand_bootstrap]] | downstream | 0.28 |
| [[p08_pat_brand_pipeline]] | downstream | 0.25 |
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.25 |
| [[p08_ac_commercial_nucleus]] | downstream | 0.24 |
