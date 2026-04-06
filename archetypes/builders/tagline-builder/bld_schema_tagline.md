---
id: bld_schema_tagline
kind: schema
pillar: P06
builder: tagline-builder
version: 1.0.0
---
# Schema: Tagline Output

```yaml
# Required frontmatter
id: string           # unique tagline artifact id
kind: tagline
pillar: P03
title: string        # the recommended tagline itself
version: string
created: date
author: string
quality: null        # never self-score
tags: [tagline, brand, ...]

# Body structure
brand: string        # brand name
usp: string          # core unique selling proposition (1 sentence)

variants:
  short:             # 3-5 words
    - text: string
      approach: enum[emotional, functional, aspirational, provocative, minimal]
      score: float   # 1-10
  medium:            # 6-10 words
    - text: string
      approach: enum
      score: float
  long:              # 11-15 words
    - text: string
      approach: enum
      score: float

recommended:
  text: string
  reasoning: string  # why this one wins
  contexts:          # adapted for each context
    site_hero: string
    social_bio: string
    ad_headline: string
    email_subject: string
    pitch_deck: string

competitors_avoided:
  - brand: string
    tagline: string
    why_different: string
```
