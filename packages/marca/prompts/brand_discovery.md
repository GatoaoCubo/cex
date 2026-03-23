# HOP: Brand Discovery | marca_agent v2.0.0

**Phase**: 1
**Purpose**: Extract brand essence from product/service brief
**Input**: Brand brief (product, audience, category, price)
**Output**: `{core_benefit, audience_persona, transformation_promise}`

---

## TASK

Analyze the brand brief and extract core essence: what problem is solved, who benefits, and what transformation is delivered.

---

## EXTRACTION RULES

### Core Benefit
```yaml
purpose: Define the primary value delivered
format: 1-2 sentences
questions:
  - What problem does the product solve?
  - What is the primary transformation delivered?
  - What emotional need does it fulfill?
```

### Audience Persona
```yaml
demographics:
  age_range: [from target_audience]
  gender: [predominant or all]
  location: [Brazil focus]
  income_class: [from price_range: popular=C/D, premium=B/C, luxury=A/B]

psychographics:
  values: [3-5 core values]
  fears: [2-3 primary fears]
  aspirations: [2-3 desires]
  lifestyle: [1-2 sentence description]

behaviors:
  purchase_triggers: [what makes them buy]
  information_sources: [where they research]
  brand_affinities: [brands they already love]
```

### Transformation Promise
```yaml
format: "From [BEFORE] to [AFTER] through [BRIDGE]"
components:
  BEFORE: How does the customer feel now?
  AFTER: How will they feel after using product?
  BRIDGE: What makes this transformation possible?
```

---

## EXECUTION

### Step 1: Parse Brief
```
1. Identify product category
2. Extract target audience description
3. Determine price positioning
4. Note any competitors mentioned
```

### Step 2: Benefit Extraction
```
1. Identify primary problem solved
2. Determine emotional benefit
3. Define functional benefit
4. Synthesize into core value
```

### Step 3: Persona Building
```
1. Demographics from brief data
2. Psychographics from category norms
3. Behaviors from price segment
4. Validate coherence
```

### Step 4: Promise Formulation
```
1. Define current state (pain)
2. Define desired state (gain)
3. Identify transformation mechanism
4. Write promise statement
```

---

## OUTPUT FORMAT

```json
{
  "discovery": {
    "core_benefit": "Primary value in 1-2 sentences",
    "audience_persona": {
      "demographics": "Age, gender, location, income",
      "psychographics": "Values, fears, aspirations",
      "key_insight": "Golden insight about audience"
    },
    "transformation_promise": "From [X] to [Y] through [Z]"
  },
  "confidence": 0.90
}
```

---

## DISPLAY FORMAT

```markdown
## DISCOVERY BRIEF

### Core Benefit
[1-2 sentences describing primary value]

### Audience Persona
**Demographics**: [summary]
**Psychographics**: [summary]
**Key Insight**: [1 sentence golden insight about audience]

### Transformation Promise
> "From [BEFORE] to [AFTER] through [BRIDGE]"
```

---

## VALIDATION

Before proceeding:
- [ ] Core benefit is specific and compelling
- [ ] Audience persona has all 3 components
- [ ] Transformation promise follows From/To/Through format
- [ ] Key insight is actionable

---

**Next**: Pass discovery to `prompts/archetype_selection.md`
