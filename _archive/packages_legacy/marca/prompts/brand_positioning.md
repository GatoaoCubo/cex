# HOP: Brand Positioning | marca_agent v2.0.0

**Phase**: 3
**Purpose**: Define UVP, competitive differentiation, and positioning statement
**Input**: Discovery + Archetype from Phases 1-2
**Output**: `{uvp, competitive_map, differentiation_statement, positioning_statement}`

---

## TASK

Create clear market positioning that differentiates the brand from competitors and establishes unique value.

---

## POSITIONING FRAMEWORKS

### Unique Value Proposition (UVP)
```yaml
formula: "Para [AUDIENCE] que [NEED], [BRAND] e [CATEGORY] que [DIFFERENTIATOR]"
requirements:
  - Specific target audience
  - Clear need/problem
  - Category frame
  - Unique differentiator
  - Max 2 sentences
```

### Ries & Trout Positioning Statement
```yaml
template: |
  Para [TARGET SEGMENT] que [NEED/WANT],
  [BRAND NAME] e o/a [CATEGORY FRAME]
  que [KEY BENEFIT]
  porque [REASON TO BELIEVE].
```

### Differentiation Statement
```yaml
format: "We are the only [CATEGORY] that [DIFFERENTIATOR]"
purpose: Single-sentence uniqueness claim
```

---

## EXECUTION

### Step 1: Competitive Mapping
```
1. List 3-5 direct competitors
2. Define 2 key positioning dimensions
3. Map each competitor on grid
4. Identify whitespace
```

### Step 2: UVP Construction
```
1. Combine audience + need
2. Add category frame
3. Insert differentiator
4. Validate uniqueness
```

### Step 3: Positioning Statement
```
1. Apply Ries & Trout template
2. Include reason to believe
3. Keep under 50 words
4. Test for memorability
```

### Step 4: Differentiation
```
1. Extract single strongest point
2. Frame as "only X that Y"
3. Validate defensibility
4. Check competitor claims
```

---

## OUTPUT FORMAT

```json
{
  "positioning": {
    "uvp": "Para [audience] que [need], [brand] e [category] que [diff]",
    "competitive_map": [
      {"competitor": "Comp A", "positioning": "How positioned", "gap": "Opportunity"},
      {"competitor": "Comp B", "positioning": "How positioned", "gap": "Opportunity"},
      {"competitor": "Comp C", "positioning": "How positioned", "gap": "Opportunity"}
    ],
    "differentiation_statement": "We are the only [X] that [Y]",
    "positioning_statement": "Full Ries & Trout statement"
  },
  "confidence": 0.88
}
```

---

## DISPLAY FORMAT

```markdown
## POSITIONING

### Unique Value Proposition
> "[UVP - max 2 sentences]"

### Competitive Map
| Competitor | Positioning | Gap |
|------------|-------------|-----|
| [Comp 1] | [How positioned] | [Opportunity] |
| [Comp 2] | [How positioned] | [Opportunity] |
| [Comp 3] | [How positioned] | [Opportunity] |

### Differentiation Statement
**We are the only [CATEGORY] that [DIFFERENTIATOR]**

### Positioning Statement
> "[Full Ries & Trout statement]"
```

---

## VALIDATION

Before proceeding:
- [ ] UVP follows formula and is specific
- [ ] At least 3 competitors mapped
- [ ] Differentiation is defensible
- [ ] Positioning statement under 50 words

---

**Next**: Pass positioning to `prompts/verbal_identity.md`
