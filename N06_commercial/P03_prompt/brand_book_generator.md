---
id: p03_brand_book_generator
kind: prompt_template
pillar: P03
title: "Brand Book Generator — 32-Block Structure"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-book
quality: 9.0
updated: 2026-04-07
tags: [prompt, brand, brand-book, generator, n06]
tldr: "Transforms Brand Discovery answers into 32-block Brand Book covering identity, positioning, voice, visual, narrative, guidelines, and validation. Uses output_brand_book.md template."
density_score: 0.93
axioms:
  - "ALWAYS generate all 32 blocks — partial brand books create downstream inconsistency."
  - "NEVER generate without completed discovery interview — incomplete inputs = diluted output."
linked_artifacts:
  primary: n06_output_brand_book
  related: [p01_kc_brand_book_patterns, p03_brand_config_extractor, p01_kc_brand_archetypes]
---

# Brand Book Generator

## Input
Brand Discovery Interview answers (all 12-15 questions completed).

## Output
32-block Brand Book in markdown format following `output_brand_book.md` template.

## Generation Instructions

### Section 1 — IDENTITY (Blocks 1-5)
From Discovery Q1-Q5:
- **Block 1 Names**: Primary name + 2 variations (short, domain-safe, hashtag-safe)
- **Block 2 Taglines**: 3 options, 40-60 chars each, pick winner
- **Block 3 Archetype**: Primary (from Q11) + secondary influence + shadow (from Q5)
- **Block 4 Traits**: 5 personality traits derived from archetype + Q10 voice answers
- **Block 5 Essence**: 1 phrase that captures brand DNA — if you can only say ONE thing

### Section 2 — POSITIONING (Blocks 6-10)
From Discovery Q6-Q9:
- **Block 6 UVP**: Headline + subheadline + 3 proof points (from Q9)
- **Block 7 Segment**: Demographics + psychographics + behavioral (from Q6)
- **Block 8 Differentiation**: What only YOU do + competitive matrix (from Q8)
- **Block 9 Promise**: Transformation arc — From X to Y through Z (from Q2)
- **Block 10 Ries & Trout**: Category ownership statement (from Q9)

### Section 3 — VOICE (Blocks 11-15)
From Discovery Q10-Q11:
- **Block 11 5D Scale**: Formality, Enthusiasm, Humor, Warmth, Authority (each 1-5)
- **Block 12 Language Style**: Sentence structure, vocabulary level, jargon policy
- **Block 13 Do's**: 5 voice behaviors to ALWAYS follow
- **Block 14 Don'ts**: 5 voice behaviors to NEVER do
- **Block 15 Example Phrases**: 10 on-brand phrases for common scenarios

### Section 4 — VISUAL (Blocks 16-19)
From Discovery Q12:
- **Block 16 Palette**: Primary, secondary, accent + HEX + RGB + color psychology rationale
- **Block 17 Typography**: Heading, body, mono fonts + pairing rationale + size scale
- **Block 18 Mood Board**: 9 concepts (3x3 grid) — keywords + reference aesthetic
- **Block 19 Visual Guidelines**: Logo usage, photography style, icon style, dark mode

### Section 5 — NARRATIVE (Blocks 20-24)
From Discovery Q1-Q4:
- **Block 20 Origin Story**: 500+ chars, founder/problem/eureka/mission arc
- **Block 21 Mission**: 100-150 chars, present tense, action-oriented
- **Block 22 Vision**: 100-150 chars, future tense, aspirational
- **Block 23 Values**: 5 values with 1-sentence explanation each
- **Block 24 Manifesto**: 300+ chars, we-believe statements, rallying cry

### Section 6 — GUIDELINES (Blocks 25-28)
Synthesized from all phases:
- **Block 25 Extended Do's**: 8 detailed brand behavior rules with examples
- **Block 26 Extended Don'ts**: 8 detailed brand prohibitions with examples
- **Block 27 Compliance**: Relevant regulations (ANVISA, INMETRO, CONAR, CDC for BR)
- **Block 28 Checklist**: 10-point brand consistency checklist for any content

### Section 7 — VALIDATION (Blocks 29-32)
Quality assurance:
- **Block 29 Consistency Score**: Rate archetype alignment across all blocks (target >= 0.85)
- **Block 30 Uniqueness Score**: Rate differentiation from competitors (target >= 8.0)
- **Block 31 Competitor Audit**: Side-by-side voice/visual comparison with top 3 competitors
- **Block 32 Integration Notes**: How this brand book maps to brand_config.yaml variables

## Rules
1. Every block must reference Discovery answers — no invented content
2. Zero hardcoded values — all brand-specific content uses {{BRAND_*}} syntax
3. Consistency score < 0.85 → revise archetype selection or voice calibration
4. All 18 required blocks must be complete; 14 optional blocks recommended
