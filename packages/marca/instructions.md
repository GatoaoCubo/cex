# MARCA Agent - Instructions

> **How to execute brand strategy creation**
> **Version**: 1.0.0

---

## Execution Protocol

### Phase 0: Context Loading (2-5s)
1. Validate brand brief completeness
2. Identify product category for compliance rules
3. Load archetype reference framework
4. Check for competitor/inspiration context

### Phase 1: Brand Identity (3-5min)
Execute identity builder:

```yaml
Block 1 - Brand Names:
  generate:
    - 1 descriptive name (benefit + suffix)
    - 1 evocative name (emotion/feeling)
    - 1 creative name (neologism/combination)
  validation:
    - Pronounceable in Brazilian Portuguese
    - No trademark conflicts
    - Memorable and distinct

Block 2 - Taglines:
  generate: 3 taglines
  constraints:
    - 40-60 characters each (strict)
    - One benefit-focused
    - One emotional
    - One positioning
  validation: Character count within range

Block 3 - Archetype:
  select:
    primary: From 12 Jungian archetypes
    secondary: Complementary archetype
  justify: Alignment with audience + category

Block 4 - Personality Traits:
  generate: 5 unique traits
  categories:
    - Core (from archetype)
    - Communication (how brand speaks)
    - Behavior (how brand acts)
    - Emotional (how brand makes people feel)
    - Differentiator (unique to this brand)

Block 5 - Brand Essence:
  synthesize: One-sentence identity
  formula: "[BRAND] is [ARCHETYPE_ACTION] that [BENEFIT] for [AUDIENCE] through [DIFFERENTIATOR]"
  max_chars: 150
```

### Phase 2: Positioning (3-5min)
Execute positioning strategy:

```yaml
Block 6 - UVP:
  components:
    headline: Main value proposition
    subheadline: Supporting statement
    proof_points: 3 evidence items
  differentiation: >= 70% from competitors

Block 7 - Target Segment:
  dimensions:
    demographic: Age, gender, income, location
    psychographic: Values, lifestyle, attitudes
    behavioral: Purchase habits, brand loyalty

Block 8 - Competitive Differentiation:
  analyze:
    tangible: Product features, price, quality
    intangible: Brand perception, emotional connection

Block 9 - Brand Promise:
  format: Single verifiable commitment
  test: Can customer verify this promise?

Block 10 - Positioning Statement:
  format: Ries & Trout formula
  template: |
    Para [TARGET_AUDIENCE] que [NEED/DESIRE],
    [BRAND] e [CATEGORY]
    que [KEY_BENEFIT]
    porque [REASON_TO_BELIEVE].
```

### Phase 3: Tone of Voice (3-5min)
Execute voice definition:

```yaml
Block 11 - Personality Dimensions:
  scales: # 1-5 positioning
    formality: Casual <-> Formal
    enthusiasm: Calm <-> Energetic
    humor: Serious <-> Playful
    authority: Peer <-> Expert

Block 12 - Language Style:
  define:
    vocabulary: Word types, complexity
    syntax: Sentence structure, length
    tone: Emotional register

Block 13 - Messaging Do's:
  generate: 5-8 guidelines
  format: Rule + Example

Block 14 - Messaging Don'ts:
  generate: 5-8 prohibitions
  format: Prohibition + Why + Alternative

Block 15 - Example Phrases:
  generate: 10 context-specific phrases
  contexts:
    - Headline
    - Social media post
    - Product description
    - Email subject
    - CTA button
    - Customer service
    - Error message
    - Thank you message
    - Promotional
    - Educational
```

### Phase 4: Visual Identity (2-4min)
Execute visual definition:

```yaml
Block 16 - Color Palette:
  generate:
    primary: 1-2 colors (HEX, RGB, CMYK)
    secondary: 2-3 colors
    accent: 1-2 colors
  include: Color psychology meaning
  validate: WCAG AA contrast compliance

Block 17 - Typography:
  recommend:
    primary: Headlines (font name + fallback)
    secondary: Body text (font name + fallback)
  include: Usage guidelines

Block 18 - Mood Board Prompts:
  generate: 9 image prompts (3x3 grid)
  categories:
    - 3 product context
    - 3 lifestyle/audience
    - 3 brand values/emotion

Block 19 - Visual Style Guidelines:
  define:
    photography_style: Lighting, composition, filters
    graphic_style: Shapes, patterns, icons
    overall_aesthetic: Minimalist, bold, organic, etc.
```

### Phase 5: Brand Narrative (2-4min)
Execute narrative creation:

```yaml
Block 20 - Origin Story:
  length: >= 500 characters
  elements: Problem, insight, solution, journey

Block 21 - Mission Statement:
  length: 100-150 characters
  focus: What we do today

Block 22 - Vision Statement:
  length: 100-150 characters
  focus: What we aspire to become

Block 23 - Core Values:
  generate: 5 defensible values
  format: Value + Definition + Example behavior

Block 24 - Brand Manifesto:
  length: >= 300 characters
  tone: Inspiring, authentic, memorable
```

### Phase 6: Brand Guidelines (2-3min)
Execute guidelines compilation:

```yaml
Block 25 - Extended Messaging Do's:
  generate: 8-10 comprehensive rules
  categorize: By channel/context

Block 26 - Extended Messaging Don'ts:
  generate: 8-10 comprehensive prohibitions
  include: Real examples to avoid

Block 27 - Compliance Rules:
  check:
    ANVISA: Health/food/cosmetics claims
    INMETRO: Electronics/toys/safety
    CONAR: Advertising ethics
    CDC: Consumer protection
  generate: Category-specific rules

Block 28 - Consistency Checklist:
  generate: 10-point verification list
  covers: All brand touchpoints
```

### Phase 7: Validation (1-2min)
Execute final validation:

```yaml
Block 29 - Consistency Score:
  calculate: Cross-section alignment
  range: 0.0 - 1.0
  threshold: >= 0.85

Block 30 - Uniqueness Score:
  calculate: Differentiation from competitors
  range: 0 - 10
  threshold: >= 8.0

Block 31 - Competitive Audit:
  summarize: Position vs competitors
  identify: Gaps and opportunities

Block 32 - Integration Notes:
  generate: Handoff instructions
  for: anuncio_agent, photo_agent, curso_agent
```

---

## Cross-Validation Rules

| Check | Elements | Threshold |
|-------|----------|-----------|
| Archetype-Voice | Archetype traits vs tone dimensions | Alignment >= 80% |
| Identity-Positioning | Essence vs UVP | Semantic similarity >= 0.7 |
| Visual-Personality | Colors vs traits | Psychology match |
| Narrative-Values | Story vs values | All values in story |

---

## Error Handling

| Error | Response |
|-------|----------|
| Incomplete brief | Request missing fields |
| Archetype conflict | Re-evaluate with justification |
| Tagline length fail | Compress/expand and retry |
| Low consistency score | Identify misalignment and fix |
| Compliance violation | Flag and suggest alternatives |

---

## Output Format

```json
{
  "report_id": "MARCA-{timestamp}",
  "status": "COMPLETE | PARTIAL",
  "blocks_completed": 32,

  "scores": {
    "consistency": 0.92,
    "uniqueness": 8.7,
    "compliance": "PASS"
  },

  "sections": {
    "identity": { "blocks": [1,2,3,4,5], "status": "COMPLETE" },
    "positioning": { "blocks": [6,7,8,9,10], "status": "COMPLETE" },
    "voice": { "blocks": [11,12,13,14,15], "status": "COMPLETE" },
    "visual": { "blocks": [16,17,18,19], "status": "COMPLETE" },
    "narrative": { "blocks": [20,21,22,23,24], "status": "COMPLETE" },
    "guidelines": { "blocks": [25,26,27,28], "status": "COMPLETE" },
    "validation": { "blocks": [29,30,31,32], "status": "COMPLETE" }
  },

  "issues": [],
  "recommendations": [],
  "integration_ready": true
}
```

---

*MARCA Instructions v1.0.0 | LILY Satellite*
