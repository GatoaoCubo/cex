---
id: n06_output_brand_book
kind: output_template
pillar: P05
title: "Brand Book Output — 32-Block Template"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-book
quality: 9.2
updated: 2026-04-07
tags: [output, brand, brand-book, 32-block, n06]
tldr: "Crown jewel output. 32-block Brand Book covering identity, positioning, voice, visual, narrative, guidelines, validation. All {{BRAND_*}} variables — zero hardcoded values."
density_score: 0.95
axioms:
  - "NEVER hardcode brand values — all {{BRAND_*}} mustache variables only."
  - "ALWAYS generate all 32 blocks — partial brand books create inconsistency."
linked_artifacts:
  primary: p03_brand_book_generator
  related: [n06_schema_brand_book, p01_kc_brand_book_patterns, n06_output_brand_config, n06_output_brand_voice_guide]
---

# Brand Book — {{BRAND_NAME}}

> {{BRAND_TAGLINE}}

---

## SECTION 1 — IDENTITY

### Block 1: Names
- **Primary**: {{BRAND_NAME}}
- **Short**: {{BRAND_NAME_SHORT}}
- **Hashtag**: #{{BRAND_HASHTAG}}

### Block 2: Taglines
1. {{TAGLINE_OPTION_1}} ← winner
2. {{TAGLINE_OPTION_2}}
3. {{TAGLINE_OPTION_3}}

### Block 3: Archetype
- **Primary**: {{BRAND_ARCHETYPE}} — {{ARCHETYPE_DESCRIPTION}}
- **Secondary Influence**: {{ARCHETYPE_SECONDARY}}
- **Shadow (avoid)**: {{BRAND_ARCHETYPE_SHADOW}} — {{SHADOW_DESCRIPTION}}

### Block 4: Personality Traits
1. {{TRAIT_1}} — {{TRAIT_1_DESCRIPTION}}
2. {{TRAIT_2}} — {{TRAIT_2_DESCRIPTION}}
3. {{TRAIT_3}} — {{TRAIT_3_DESCRIPTION}}
4. {{TRAIT_4}} — {{TRAIT_4_DESCRIPTION}}
5. {{TRAIT_5}} — {{TRAIT_5_DESCRIPTION}}

### Block 5: Brand Essence
> "{{BRAND_ESSENCE}}"

---

## SECTION 2 — POSITIONING

### Block 6: Unique Value Proposition
**Headline**: {{UVP_HEADLINE}}
**Subheadline**: {{UVP_SUBHEADLINE}}

**Proof Points**:
1. {{PROOF_1}}
2. {{PROOF_2}}
3. {{PROOF_3}}

### Block 7: Market Segment
- **Demographics**: {{SEGMENT_DEMOGRAPHICS}}
- **Psychographics**: {{SEGMENT_PSYCHOGRAPHICS}}
- **Behavioral**: {{SEGMENT_BEHAVIORAL}}

### Block 8: Differentiation
> "We are the only {{BRAND_CATEGORY}} that {{BRAND_DIFFERENTIATOR}}"

| Attribute | {{BRAND_NAME}} | {{COMPETITOR_1}} | {{COMPETITOR_2}} |
|-----------|----------------|-------------------|-------------------|
| {{ATTR_1}} | ✅ | ❌ | ⚠️ |
| {{ATTR_2}} | ✅ | ✅ | ❌ |
| {{ATTR_3}} | ✅ | ❌ | ❌ |

### Block 9: Transformation Promise
> From **{{BEFORE}}** to **{{AFTER}}** through **{{BRIDGE}}**

### Block 10: Ries & Trout Statement
> "{{BRAND_NAME}} is the **{{BRAND_CATEGORY}}** for **{{BRAND_ICP}}** who want **{{AFTER}}**"

---

## SECTION 3 — VOICE

### Block 11: 5D Voice Scale

| Dimension | Score | Description |
|-----------|-------|-------------|
| Formality | {{BRAND_VOICE_FORMALITY}}/5 | {{FORMALITY_DESC}} |
| Enthusiasm | {{BRAND_VOICE_ENTHUSIASM}}/5 | {{ENTHUSIASM_DESC}} |
| Humor | {{BRAND_VOICE_HUMOR}}/5 | {{HUMOR_DESC}} |
| Warmth | {{BRAND_VOICE_WARMTH}}/5 | {{WARMTH_DESC}} |
| Authority | {{BRAND_VOICE_AUTHORITY}}/5 | {{AUTHORITY_DESC}} |

### Block 12: Language Style
- **Sentence structure**: {{SENTENCE_STYLE}}
- **Vocabulary level**: {{VOCABULARY_LEVEL}}
- **Jargon policy**: {{JARGON_POLICY}}

### Block 13: Voice Do's
1. {{VOICE_DO_1}}
2. {{VOICE_DO_2}}
3. {{VOICE_DO_3}}
4. {{VOICE_DO_4}}
5. {{VOICE_DO_5}}

### Block 14: Voice Don'ts
1. {{VOICE_DONT_1}}
2. {{VOICE_DONT_2}}
3. {{VOICE_DONT_3}}
4. {{VOICE_DONT_4}}
5. {{VOICE_DONT_5}}

### Block 15: Example Phrases
1. {{PHRASE_1}}
2. {{PHRASE_2}}
3. {{PHRASE_3}}
4. {{PHRASE_4}}
5. {{PHRASE_5}}
6. {{PHRASE_6}}
7. {{PHRASE_7}}
8. {{PHRASE_8}}
9. {{PHRASE_9}}
10. {{PHRASE_10}}

---

## SECTION 4 — VISUAL

### Block 16: Color Palette

| Role | HEX | RGB | Psychology |
|------|-----|-----|------------|
| Primary | {{PRIMARY_HEX}} | {{PRIMARY_RGB}} | {{PRIMARY_PSYCH}} |
| Secondary | {{SECONDARY_HEX}} | {{SECONDARY_RGB}} | {{SECONDARY_PSYCH}} |
| Accent | {{ACCENT_HEX}} | {{ACCENT_RGB}} | {{ACCENT_PSYCH}} |
| Background | {{BG_HEX}} | {{BG_RGB}} | {{BG_PSYCH}} |
| Foreground | {{FG_HEX}} | {{FG_RGB}} | {{FG_PSYCH}} |
| Surface | {{SURFACE_HEX}} | {{SURFACE_RGB}} | {{SURFACE_PSYCH}} |

### Block 17: Typography

| Role | Font | Weight | Size Scale |
|------|------|--------|------------|
| Heading | {{HEADING_FONT}} | {{HEADING_WEIGHT}} | {{HEADING_SCALE}} |
| Body | {{BODY_FONT}} | {{BODY_WEIGHT}} | {{BODY_SCALE}} |
| Mono | {{MONO_FONT}} | {{MONO_WEIGHT}} | {{MONO_SCALE}} |

**Pairing rationale**: {{FONT_PAIRING_RATIONALE}}

### Block 18: Mood Board (3×3)

| | Column 1 | Column 2 | Column 3 |
|-|----------|----------|----------|
| Row 1 | {{MOOD_1}} | {{MOOD_2}} | {{MOOD_3}} |
| Row 2 | {{MOOD_4}} | {{MOOD_5}} | {{MOOD_6}} |
| Row 3 | {{MOOD_7}} | {{MOOD_8}} | {{MOOD_9}} |

### Block 19: Visual Guidelines
- **Logo usage**: {{LOGO_GUIDELINES}}
- **Photography style**: {{PHOTO_STYLE}}
- **Icon style**: {{ICON_STYLE}}
- **Dark mode**: {{DARK_MODE_RULES}}

---

## SECTION 5 — NARRATIVE

### Block 20: Origin Story
{{BRAND_STORY}}

### Block 21: Mission
> {{BRAND_MISSION}}

### Block 22: Vision
> {{BRAND_VISION}}

### Block 23: Values
1. **{{VALUE_1}}** — {{VALUE_1_EXPLANATION}}
2. **{{VALUE_2}}** — {{VALUE_2_EXPLANATION}}
3. **{{VALUE_3}}** — {{VALUE_3_EXPLANATION}}
4. **{{VALUE_4}}** — {{VALUE_4_EXPLANATION}}
5. **{{VALUE_5}}** — {{VALUE_5_EXPLANATION}}

### Block 24: Manifesto
{{BRAND_MANIFESTO}}

---

## SECTION 6 — GUIDELINES

### Block 25: Extended Do's
1. {{EXT_DO_1}}
2. {{EXT_DO_2}}
3. {{EXT_DO_3}}
4. {{EXT_DO_4}}
5. {{EXT_DO_5}}
6. {{EXT_DO_6}}
7. {{EXT_DO_7}}
8. {{EXT_DO_8}}

### Block 26: Extended Don'ts
1. {{EXT_DONT_1}}
2. {{EXT_DONT_2}}
3. {{EXT_DONT_3}}
4. {{EXT_DONT_4}}
5. {{EXT_DONT_5}}
6. {{EXT_DONT_6}}
7. {{EXT_DONT_7}}
8. {{EXT_DONT_8}}

### Block 27: Compliance
- **ANVISA**: {{ANVISA_NOTES}}
- **INMETRO**: {{INMETRO_NOTES}}
- **CONAR**: {{CONAR_NOTES}}
- **CDC**: {{CDC_NOTES}}

### Block 28: Brand Consistency Checklist
- [ ] Name spelled correctly ({{BRAND_NAME}})
- [ ] Tagline matches approved version
- [ ] Colors match brand palette (HEX values)
- [ ] Fonts match brand typography stack
- [ ] Voice tone matches 5D scores (±1 tolerance)
- [ ] Archetype personality consistent
- [ ] Transformation arc present (From/To/Through)
- [ ] UVP stated correctly
- [ ] No competitor language copied
- [ ] Compliance reviewed for market

---

## SECTION 7 — VALIDATION

### Block 29: Consistency Score
**Score**: {{CONSISTENCY_SCORE}} / 1.00
**Threshold**: >= 0.85
**Status**: {{CONSISTENCY_STATUS}}

### Block 30: Uniqueness Score
**Score**: {{UNIQUENESS_SCORE}} / 10.0
**Threshold**: >= 8.0
**Status**: {{UNIQUENESS_STATUS}}

### Block 31: Competitor Audit
| Dimension | {{BRAND_NAME}} | {{COMPETITOR_1}} | {{COMPETITOR_2}} | {{COMPETITOR_3}} |
|-----------|----------------|-------------------|-------------------|-------------------|
| Voice tone | {{OWN_VOICE}} | {{C1_VOICE}} | {{C2_VOICE}} | {{C3_VOICE}} |
| Visual style | {{OWN_VISUAL}} | {{C1_VISUAL}} | {{C2_VISUAL}} | {{C3_VISUAL}} |
| Positioning | {{OWN_POS}} | {{C1_POS}} | {{C2_POS}} | {{C3_POS}} |

### Block 32: Integration Notes
This brand book maps to `brand_config.yaml` as follows:
- Blocks 1-5 → `identity` + `archetype` sections
- Blocks 6-10 → `positioning` + `audience` sections
- Blocks 11-15 → `voice` section
- Blocks 16-19 → `visual` section
- Blocks 20-24 → `identity` section (story, mission, vision, values)
- Blocks 25-28 → guidelines (not in config, reference only)
- Blocks 29-32 → validation metadata

Run `python _tools/brand_validate.py` to verify config extraction.
