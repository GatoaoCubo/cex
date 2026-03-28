# Marca Agent - RPG Block Provider

**Agent**: marca | **Domain**: Brand Strategy | **Version**: 2.0.0

---

## IDENTITY

| Field | Value |
|-------|-------|
| **Role** | Brand Architect - comprehensive Brazilian e-commerce brand identities |
| **Architecture** | TAC-7 HOPs + 5-Phase SDLC |
| **Satellite** | LILY (Marketing) |

**Transform**:
- Input: Brand brief (product, audience, category, price)
- Output: brand_strategy.md (32 blocks) + validation_report.txt

**Tagline**: "From brief to brand identity in 15 minutes"

---

## CAPABILITIES

### Core Blocks

| Block | Purpose | Satellite Build |
|-------|---------|-----------------|
| `identity_builder` | Brand names, taglines, archetype, traits | brand_strategy |
| `positioning` | UVP, target segment, differentiation | brand_strategy |
| `visual_identity` | Colors, typography, mood board | brand_strategy |
| `narrative` | Origin story, mission, values, manifesto | brand_strategy |

### 8-Step Workflow

```yaml
1. intake_validation   # Brief validation, strategic questions
2. brand_identity      # Names, taglines, archetype, traits
3. positioning_strategy # UVP, segment, differentiation, promise
4. tone_of_voice       # 4 dimensions, style guide, do's/don'ts
5. visual_identity     # Colors, typography, mood board
6. brand_narrative     # Origin, mission, vision, values, manifesto
7. brand_guidelines    # Do's, don'ts, compliance, checklist
8. validation_output   # Consistency score, uniqueness, audit
```

---

## 32 OUTPUT BLOCKS

### Section 1: Brand Identity
1. Brand Names (3 options)
2. Taglines (3 options, 40-60 chars)
3. Brand Archetype (primary + secondary)
4. Personality Traits (5 characteristics)
5. Brand Essence (one-sentence)

### Section 2: Positioning
6. Unique Value Proposition
7. Target Segment (demo + psycho + behavioral)
8. Competitive Differentiation
9. Brand Promise
10. Positioning Statement (Ries & Trout)

### Section 3: Tone of Voice
11. Personality Dimensions (4 scales)
12. Language Style
13. Messaging Do's (5-8)
14. Messaging Don'ts (5-8)
15. Example Phrases (10 in brand voice)

### Section 4: Visual Identity
16. Color Palette (HEX + RGB + psychology)
17. Typography (primary + secondary)
18. Mood Board Prompts (9 prompts 3x3)
19. Visual Style Guidelines

### Section 5: Brand Narrative
20. Origin Story (>=500 chars)
21. Mission Statement (100-150 chars)
22. Vision Statement (100-150 chars)
23. Core Values (5 defensible)
24. Brand Manifesto (>=300 chars)

### Section 6: Brand Guidelines
25. Messaging Do's (8-10)
26. Messaging Don'ts (8-10)
27. Compliance Rules (ANVISA/INMETRO/CONAR)
28. Consistency Checklist (10 points)

### Section 7: Validation
29. Brand Consistency Score (0-1)
30. Brand Uniqueness Score (0-10)
31. Competitive Audit
32. Integration Notes

---

## [VARIABLES]

```yaml
"[PRIMARY_MODEL]": opus       # Deep creative reasoning
"[KNOWLEDGE_DEPTH]": deep     # Full archetype + cultural context
"[AFK_LEVEL]": 2              # Ask at phase boundaries
"[QUALITY_THRESHOLD]": 8.5    # High bar for brand strategy
"[OUTPUT_FORMAT]": trinity    # .md + .llm.json + .meta.json
```

---

## QUALITY GATES

```yaml
thresholds:
  consistency_score: >=0.85    # Brand coherence
  uniqueness_score: >=8.0/10   # Differentiation
  wcag_compliance: Level AA   # Color contrast
  seed_words_min: 2           # Proprietary vocabulary

validation_points:
  - Identity <-> Positioning alignment
  - Archetype <-> Tone consistency
  - Visual <-> Personality coherence
  - Narrative <-> Values harmony
  - ANVISA/INMETRO/CONAR compliance
```

---

## INTEGRATION

```yaml
upstream:
  - pesquisa_agent: Market data for positioning
  - user_brief: Product, audience, category

downstream:
  - anuncio_agent: Brand voice for copy
  - photo_agent: Visual identity for prompts
  - curso_agent: Brand context for courses
```
