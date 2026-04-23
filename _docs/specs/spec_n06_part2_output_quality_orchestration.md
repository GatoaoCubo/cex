---
id: spec_n06_part2
kind: constraint_spec
pillar: P06
title: Spec N06 Part 2 -- Output Templates Schemas Quality Orchestration
version: 1.0.0
created: 2026-04-01
author: n07_admin
domain: brand-configuration-layer
quality_target: 9.0
status: EXECUTED
scope: N06_commercial
depends_on: spec_n06_brand_verticalization
tags: [spec, n06, brand, output, schemas, quality-gates, orchestration]
tldr: Waves 3-4 do N06 -- 32-block brand book, brand_config schema, voice guide, visual identity, quality gates, orchestration.
density_score: 0.95
quality: 9.1
updated: "2026-04-07"
---

# Spec N06 Part 2 -- Output, Schemas, Quality, Orchestration

## PRE-REQUISITOS COMPLETOS

- [x] Part 1 Spec (348 lines, brand_config.yaml design, 8F decomposition)
- [x] Wave 2 KCs: 10 complete (7 SHAKA + 3 migrated, 180KB)
  - kc_brand_book_patterns (18KB), kc_brand_voice_systems (18KB)
  - kc_brand_archetypes (16KB), kc_brand_frameworks (22KB)
  - kc_icp_frameworks (16KB), kc_competitive_positioning (15KB)
  - kc_brand_propagation_arch (13KB), kc_brand_monetization_models (11KB)
  - kc_brand_naming_patterns (8KB), kc_brand_tokens_pipeline (5KB)
- [x] Identity rewrite planned (agent, system_prompt, card, boot, mcp, seed)

---

## WAVE 3A: SCHEMAS (P06) -- 4 CREATE em N06/P06_schema/

### 3.1 brand_config_schema.yaml
Validates .cex/brand/brand_config.yaml. 7 sections:
identity: required [BRAND_NAME, BRAND_TAGLINE, BRAND_MISSION, BRAND_VALUES(3-7)], optional [SLOGAN, VISION, STORY(200-2000 chars)].
archetype: required [BRAND_ARCHETYPE: enum 12 Jungian], optional [SHADOW, PERSONALITY(3-7 traits)].
voice: required [TONE, FORMALITY(1-5)], optional [ENTHUSIASM, HUMOR, WARMTH, AUTHORITY(1-5), DO(3+), DONT(3+), LANGUAGE].
audience: required [ICP, TRANSFORMATION(pattern: From X to Y through Z)], optional [AGE, LOCATION, INCOME, VALUES, FEARS, ASPIRATIONS].
visual: required [COLORS(primary+secondary+accent)], optional [FONTS(heading+body+mono), LOGO_URL, FAVICON_URL, STYLE].
positioning: required [CATEGORY, UVP], optional [DIFFERENTIATOR, COMPETITORS, CONTENT_PILLARS(3-7)].
monetization: required [PRICING_MODEL(enum: subscription|one-time|credits|freemium|marketplace|hybrid), CURRENCY], optional [PRICE_ANCHOR, TIERS, PAYMENT_PROVIDERS].
Total: 13 required fields, 28 optional fields.

### 3.2 brand_book_schema.yaml
Validates 32-block Brand Book output (brunasena model universalized):
Section 1 IDENTITY (blocks 1-5): names(3 types), taglines(40-60 chars), archetype(primary+secondary), traits(5), essence(1 phrase).
Section 2 POSITIONING (blocks 6-10): UVP(headline+sub+3 proofs), segment(demo+psycho+behavioral), differentiation, promise, Ries and Trout statement.
Section 3 VOICE (blocks 11-15): 5D scale, language style, 5 dos, 5 donts, 10 example phrases.
Section 4 VISUAL (blocks 16-19): palette(HEX+RGB+psychology), typography, 9 mood board concepts(3x3), visual guidelines.
Section 5 NARRATIVE (blocks 20-24): origin(500+ chars), mission(100-150), vision(100-150), 5 values, manifesto(300+).
Section 6 GUIDELINES (blocks 25-28): 8 extended dos, 8 donts, compliance(ANVISA/INMETRO/CONAR/CDC), 10-point checklist.
Section 7 VALIDATION (blocks 29-32): consistency score >= 0.85, uniqueness >= 8.0, competitor audit, integration notes.
Required blocks: 1-10, 11, 16, 20-23, 29-30 (18/32). Full: all 32.

### 3.3 brand_voice_contract.yaml
Validates voice consistency: 5D scores within tolerance(1) of brand_config. Tone matrix per channel (social +1 casual, docs +1 formal, ads context-dependent). Do/Dont hard constraints. Example phrases = calibration reference.

### 3.4 brand_audit_schema.yaml
Audit dimensions: archetype_alignment(0.25), voice_consistency(0.20), visual_coherence(0.20), positioning_clarity(0.15), narrative_integrity(0.10), config_completeness(0.10). Passing: 0.85. Health: 0.95+ Excellent, 0.85-0.94 Healthy, 0.70-0.84 Needs work, <0.70 Critical.

---

## WAVE 3B: OUTPUT TEMPLATES (P05) -- 8 CREATE em N06/P05_output/

### 3.5 output_brand_book.md
Crown jewel. 32-block Brand Book (brunasena universalized). S1 Identity(5): names, taglines, archetype, traits, essence. S2 Positioning(5): UVP, segment, differentiation, promise, Ries-Trout. S3 Voice(5): 5D scale, language, dos, donts, 10 phrases. S4 Visual(4): palette(HEX+RGB), typography, mood board 3x3, guidelines. S5 Narrative(5): origin, mission, vision, values, manifesto. S6 Guidelines(4): extended dos/donts, compliance BR, checklist. S7 Validation(4): consistency >= 0.85, uniqueness >= 8.0, audit, integration. All fill-in variables. Zero hardcoded.

### 3.6 output_brand_config.md
Template .cex/brand/brand_config.yaml. All 7 sections with comments, defaults, examples. Extractor prompt fills from Brand Book.

### 3.7 output_brand_one_pager.md
1-page: Logo+Name+Tagline+Archetype+3 Values+UVP+Colors+Fonts+ICP+Transformation. Shareable PDF.

### 3.8 output_brand_voice_guide.md
5D radar, tone matrix per channel, voice attributes We are X not Y, 5 dos/donts, 10 phrases, LLM injection snippet.

### 3.9 output_visual_identity_sheet.md
Color swatches(HEX+HSL+RGB), font specimens, logo usage rules, photography style, dark mode.

### 3.10 output_competitive_map.md
2D perceptual grid, brand+competitors, whitespace, Blue Ocean ERRC, competitive audit, gap analysis.

### 3.11 output_brand_discovery_report.md
Research output: market intelligence, keyword analysis, gaps, audience insights, recommendation.

### 3.12 output_pricing_page.md
HTML pricing page. 2-4 tiers, anchoring, social proof, FAQ, CTA per tier, responsive. BR: BRL, PIX, parcelamento.

---

## WAVE 4A: QUALITY GATES (P07) -- 2 REWRITE

### 4.1 quality_gate_commercial.md

| Gate | Threshold | Required |
|------|-----------|----------|
| config_complete | 13 required fields | yes |
| config_valid | schema pass | yes |
| archetype_real | 1/12 Jungian | yes |
| voice_5d | 5 dims scored | yes |
| voice_consistent | within tolerance | yes |
| positioning_unique | UVP != competitor | yes |
| naming_screened | domain+trademark | no |
| brand_book_18 | 18/32 blocks | yes |
| brand_book_32 | 32/32 blocks | no |
| consistency >= 0.85 | audit score | yes |
| uniqueness >= 8.0 | uniqueness score | yes |
| propagation_test | nuclei resolve vars | yes |
| visual_contrast | WCAG 4.5:1 | yes |
| transformation_arc | From/To/Through | yes |

### 4.2 scoring_rubric_commercial.md
Dual: BRAND(archetype 0-3, voice 0-2, positioning 0-2, visual 0-2, narrative 0-1) + MONETIZATION(pricing 0-3, funnel 0-2, conversion 0-2, revenue 0-2, market 0-1). Average to 10. Min 8.0, golden 9.0.

---

## WAVE 4B: ORCHESTRATION (P12) -- 2 REWRITE

### 4.3 dispatch_rule_commercial.md
keywords: brand, marca, identidade, brand-book, persona, arquetipo, voz, naming, tagline, posicionamento, UVP, ICP, design-tokens, paleta, pricing, curso, funnel, monetizar, receita, upsell, checkout.
receives_from: [N01, N07]. handoff_to: [N02(voice+visual), N03(tokens), N05(deploy)].
model: sonnet(discovery)/opus(brand book). mcps: [fetch, stripe, hotmart].
N06 runs FIRST on new CEX instance (brand before everything).

### 4.4 workflow_commercial.md
BRAND: intent > discovery(12-15 Qs) > research > archetype(12 Jungian) > 32-block book > extract config > validate > propagate > audit.
MONETIZATION: product > pricing > tiers > funnel(TOFU/MOFU/BOFU) > course > revenue > validate.
BRIDGE: brand book > extract pricing > align funnel with voice > price by archetype > deliver on-brand.

---

## ARTEFATOS PART 2 (16: 12 CREATE + 4 REWRITE)

W3A: 4 schemas (brand_config, brand_book, voice_contract, audit)
W3B: 8 outputs (brand_book, config_template, one-pager, voice_guide, visual_identity, competitive_map, discovery_report, pricing_page)
W4A: 2 quality (gate 14 checks, rubric dual brand+monetization)
W4B: 2 orchestration (dispatch_rule, workflow brand+monetization+bridge)
