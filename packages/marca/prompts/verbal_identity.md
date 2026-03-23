# HOP: Verbal Identity | marca_agent v2.0.0

**Phase**: 4
**Purpose**: Define brand voice, names, taglines, and messaging guidelines
**Input**: Discovery + Archetype + Positioning from Phases 1-3
**Output**: `{brand_names, taglines, voice_dimensions, example_phrases, dos_donts}`

---

## TASK

Create the complete verbal identity system: how the brand sounds, what it's called, and messaging rules.

---

## BRAND VOICE DIMENSIONS

### Nielsen Norman 4D Scale
```yaml
dimensions:
  formal_casual: 1-5        # 1=very formal, 5=very casual
  enthusiastic_factual: 1-5 # 1=matter-of-fact, 5=enthusiastic
  respectful_irreverent: 1-5 # 1=respectful, 5=irreverent
  serious_funny: 1-5        # 1=serious, 5=funny
```

### Language Style
```yaml
vocabulary: simple | intermediate | advanced
sentence_structure: short | medium | long
person: 1st (nos) | 2nd (voce) | 3rd (a marca)
portuguese_br: true  # Avoid Portugal-isms
```

---

## BRAND NAMING

### Name Types
```yaml
descriptive:
  format: "[BENEFIT] + [SUFFIX]"
  purpose: Direct communication
  example: "Organica", "VitaFit"

evocative:
  format: "[EMOTION/FEELING]"
  purpose: Emotional trigger
  example: "Serena", "Impulso"

creative:
  format: "[NEOLOGISM]"
  purpose: Unique memorable word
  example: "Codexa", "Nubank"
```

---

## TAGLINE REQUIREMENTS

```yaml
count: 3 options
length: 40-60 characters each
types:
  - benefit_focused: What you get
  - emotional: How you feel
  - positioning: What makes us different
```

---

## EXECUTION

### Step 1: Voice Dimensions
```
1. Score each dimension 1-5
2. Justify based on archetype
3. Write interpretation
4. Validate consistency
```

### Step 2: Brand Names
```
1. Generate 3 name options
2. One per type (descriptive, evocative, creative)
3. Include rationale for each
4. Check availability (if possible)
```

### Step 3: Taglines
```
1. Write 3 taglines
2. Count characters (40-60)
3. Label focus type
4. Validate brand voice alignment
```

### Step 4: Example Phrases
```
1. Write 10 phrases in brand voice
2. Cover different contexts (social, support, marketing)
3. Demonstrate voice dimensions
4. Test consistency
```

### Step 5: Messaging Guidelines
```
1. Write 5-8 Do's with examples
2. Write 5-8 Don'ts with examples
3. Include specific words to use/avoid
4. Reference archetype alignment
```

---

## OUTPUT FORMAT

```json
{
  "verbal_identity": {
    "brand_names": [
      {"type": "descriptive", "name": "Name1", "rationale": "Why"},
      {"type": "evocative", "name": "Name2", "rationale": "Why"},
      {"type": "creative", "name": "Name3", "rationale": "Why"}
    ],
    "taglines": [
      {"text": "Tagline 1", "chars": 45, "focus": "benefit"},
      {"text": "Tagline 2", "chars": 48, "focus": "emotional"},
      {"text": "Tagline 3", "chars": 52, "focus": "positioning"}
    ],
    "voice_dimensions": {
      "formal_casual": {"score": 3, "interpretation": "Balanced"},
      "enthusiastic_factual": {"score": 4, "interpretation": "Confident"},
      "respectful_irreverent": {"score": 2, "interpretation": "Professional"},
      "serious_funny": {"score": 2, "interpretation": "Serious but not rigid"}
    },
    "example_phrases": ["phrase1", "phrase2", "...10 total"],
    "messaging_dos": ["do1", "do2", "...5-8 total"],
    "messaging_donts": ["dont1", "dont2", "...5-8 total"]
  },
  "confidence": 0.90
}
```

---

## DISPLAY FORMAT

```markdown
## VERBAL IDENTITY

### Brand Names (3 Options)
| Type | Name | Rationale |
|------|------|-----------|
| Descriptive | [NAME] | [WHY] |
| Evocative | [NAME] | [WHY] |
| Creative | [NAME] | [WHY] |

### Taglines (40-60 chars)
| # | Tagline | Chars | Focus |
|---|---------|-------|-------|
| 1 | "[TAGLINE]" | XX | Benefit |
| 2 | "[TAGLINE]" | XX | Emotional |
| 3 | "[TAGLINE]" | XX | Positioning |

### Voice Dimensions
| Dimension | Score | Interpretation |
|-----------|-------|----------------|
| Formal-Casual | X/5 | [description] |
| Enthusiastic-Factual | X/5 | [description] |
| Respectful-Irreverent | X/5 | [description] |
| Serious-Funny | X/5 | [description] |

### Example Phrases (10 in Brand Voice)
1. [phrase in brand voice]
2. [phrase in brand voice]
... (10 total)

### Messaging Do's
1. [guideline + example]
... (5-8 total)

### Messaging Don'ts
1. [what to avoid + why]
... (5-8 total)
```

---

## VALIDATION

Before proceeding:
- [ ] 3 brand name options with rationale
- [ ] 3 taglines 40-60 chars each
- [ ] All 4 voice dimensions scored
- [ ] 10 example phrases
- [ ] 5-8 Do's and Don'ts

---

**Next**: Pass verbal identity to `prompts/visual_identity.md`
