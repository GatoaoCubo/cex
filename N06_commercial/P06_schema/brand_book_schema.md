---
id: n06_schema_brand_book
kind: constraint_spec
8f: F1_constrain
pillar: P06
title: "Brand Book Schema — 32-Block Validation"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-book-validation
quality: 9.1
updated: 2026-04-07
tags: [schema, brand, brand-book, validation, n06]
tldr: "Validates 32-block Brand Book output. 7 sections, 18 required blocks, 14 optional. Consistency >= 0.85, uniqueness >= 8.0."
density_score: 0.94
axioms:
  - "18 blocks are REQUIRED — missing required blocks = validation failure."
  - "Consistency score >= 0.85 AND uniqueness >= 8.0 — both must pass independently."
linked_artifacts:
  primary: n06_output_brand_book
  related: [p03_brand_book_generator, p01_kc_brand_book_patterns, n06_schema_brand_audit]
related:
  - p03_brand_book_generator
  - n06_output_brand_book
  - spec_n06_part2
  - p03_brand_config_extractor
  - p03_sp_brand_nucleus
  - p07_qg_commercial
  - p03_sp_commercial_nucleus
  - p11_qg_brand_artifacts
  - p07_sr_commercial
  - p02_agent_commercial_nucleus
---

# Brand Book Schema

## Structure: 7 Sections, 32 Blocks

### Section 1 — IDENTITY (Blocks 1-5)

| Block | Title | Required | Constraints |
|-------|-------|----------|-------------|
| 1 | Names | ✅ | 3 types: primary, short, hashtag-safe |
| 2 | Taglines | ✅ | 3 options, 40-60 chars each, winner marked |
| 3 | Archetype | ✅ | primary + secondary influence + shadow |
| 4 | Traits | ✅ | exactly 5 personality traits |
| 5 | Essence | ✅ | 1 phrase brand DNA capture |

### Section 2 — POSITIONING (Blocks 6-10)

| Block | Title | Required | Constraints |
|-------|-------|----------|-------------|
| 6 | UVP | ✅ | headline + subheadline + 3 proof points |
| 7 | Segment | ✅ | demographics + psychographics + behavioral |
| 8 | Differentiation | ✅ | "We are the only X that Y" + competitive matrix |
| 9 | Promise | ✅ | transformation arc: From X to Y through Z |
| 10 | Ries & Trout | ✅ | category ownership statement |

### Section 3 — VOICE (Blocks 11-15)

| Block | Title | Required | Constraints |
|-------|-------|----------|-------------|
| 11 | 5D Scale | ✅ | formality, enthusiasm, humor, warmth, authority (each 1-5) |
| 12 | Language Style | ❌ | sentence structure, vocabulary, jargon policy |
| 13 | Do's | ❌ | 5 voice behaviors to always follow |
| 14 | Don'ts | ❌ | 5 voice behaviors to never do |
| 15 | Example Phrases | ❌ | 10 on-brand phrases for common scenarios |

### Section 4 — VISUAL (Blocks 16-19)

| Block | Title | Required | Constraints |
|-------|-------|----------|-------------|
| 16 | Palette | ✅ | HEX + RGB + color psychology rationale |
| 17 | Typography | ❌ | heading + body + mono + pairing rationale |
| 18 | Mood Board | ❌ | 9 concepts (3×3 grid), keywords + reference |
| 19 | Visual Guidelines | ❌ | logo usage, photography, icon style, dark mode |

### Section 5 — NARRATIVE (Blocks 20-24)

| Block | Title | Required | Constraints |
|-------|-------|----------|-------------|
| 20 | Origin Story | ✅ | 500+ chars, founder/problem/eureka/mission arc |
| 21 | Mission | ✅ | 100-150 chars, present tense, action-oriented |
| 22 | Vision | ✅ | 100-150 chars, future tense, aspirational |
| 23 | Values | ✅ | 5 values with 1-sentence explanation each |
| 24 | Manifesto | ❌ | 300+ chars, we-believe statements, rallying cry |

### Section 6 — GUIDELINES (Blocks 25-28)

| Block | Title | Required | Constraints |
|-------|-------|----------|-------------|
| 25 | Extended Do's | ❌ | 8 detailed brand behavior rules + examples |
| 26 | Extended Don'ts | ❌ | 8 detailed brand prohibitions + examples |
| 27 | Compliance | ❌ | ANVISA/INMETRO/CONAR/CDC for BR market |
| 28 | Checklist | ❌ | 10-point brand consistency checklist |

### Section 7 — VALIDATION (Blocks 29-32)

| Block | Title | Required | Constraints |
|-------|-------|----------|-------------|
| 29 | Consistency Score | ✅ | archetype alignment across all blocks, target >= 0.85 |
| 30 | Uniqueness Score | ✅ | differentiation from competitors, target >= 8.0 |
| 31 | Competitor Audit | ❌ | side-by-side voice/visual comparison, top 3 |
| 32 | Integration Notes | ❌ | how brand book maps to brand_config.yaml |

## Summary

| Metric | Value |
|--------|-------|
| Total blocks | 32 |
| Required blocks | 18 (1-11, 16, 20-23, 29-30) |
| Optional blocks | 14 (12-15, 17-19, 24-28, 31-32) |
| Minimum viable | 18 blocks filled |
| Full brand book | all 32 blocks |
| Consistency threshold | >= 0.85 |
| Uniqueness threshold | >= 8.0 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_brand_book_generator]] | upstream | 0.68 |
| [[n06_output_brand_book]] | upstream | 0.51 |
| [[spec_n06_part2]] | sibling | 0.47 |
| [[p03_brand_config_extractor]] | upstream | 0.36 |
| [[p03_sp_brand_nucleus]] | upstream | 0.30 |
| [[p07_qg_commercial]] | downstream | 0.29 |
| [[p03_sp_commercial_nucleus]] | upstream | 0.28 |
| [[p11_qg_brand_artifacts]] | downstream | 0.28 |
| [[p07_sr_commercial]] | downstream | 0.28 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.26 |
