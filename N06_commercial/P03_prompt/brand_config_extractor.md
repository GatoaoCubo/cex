---
id: p03_brand_config_extractor
kind: prompt_template
pillar: P03
title: "Brand Config Extractor — Brand Book → brand_config.yaml"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-config
quality: 9.1
updated: 2026-04-07
tags: [prompt, brand, config, extractor, yaml, n06]
tldr: "Extracts machine-readable brand_config.yaml from 32-block Brand Book. Maps blocks to 41 mustache variables across 7 sections."
density_score: 0.93
axioms:
  - "ALWAYS validate extracted config with brand_validate.py — 13 required fields must pass."
  - "NEVER leave mustache variables unresolved — {{BRAND_*}} in output = extraction failure."
linked_artifacts:
  primary: n06_output_brand_config
  related: [n06_schema_brand_config, n06_output_brand_book, p03_brand_book_generator]
---

# Brand Config Extractor

## Input
Completed 32-block Brand Book (from `brand_book_generator.md`).

## Output
Valid `.cex/brand/brand_config.yaml` file with all required fields populated.

## Extraction Mapping

### identity (from Blocks 1-2, 20-24)
```
BRAND_NAME       ← Block 1 primary name
BRAND_TAGLINE    ← Block 2 winning tagline
BRAND_SLOGAN     ← Block 2 alternate (if campaign-specific)
BRAND_MISSION    ← Block 21 mission statement
BRAND_VISION     ← Block 22 vision statement
BRAND_VALUES     ← Block 23 value names (array of 3-7)
BRAND_STORY      ← Block 20 origin story (full text)
```

### archetype (from Blocks 3-4)
```
BRAND_ARCHETYPE         ← Block 3 primary archetype (1 of 12 Jungian)
BRAND_ARCHETYPE_SHADOW  ← Block 3 shadow archetype
BRAND_PERSONALITY       ← Block 4 traits (array of 5)
```

### voice (from Blocks 11-15)
```
BRAND_VOICE_TONE        ← Block 11 tone description
BRAND_VOICE_FORMALITY   ← Block 11 formality score (1-5)
BRAND_VOICE_ENTHUSIASM  ← Block 11 enthusiasm score (1-5)
BRAND_VOICE_HUMOR       ← Block 11 humor score (1-5)
BRAND_VOICE_WARMTH      ← Block 11 warmth score (1-5)
BRAND_VOICE_AUTHORITY   ← Block 11 authority score (1-5)
BRAND_VOICE_DO          ← Block 13 do's (array of 3+)
BRAND_VOICE_DONT        ← Block 14 don'ts (array of 3+)
BRAND_LANGUAGE          ← Inferred from Discovery Q15
```

### audience (from Blocks 7, 9)
```
BRAND_ICP              ← Block 7 psychographic description
BRAND_ICP_AGE          ← Block 7 demographic age range
BRAND_ICP_LOCATION     ← Block 7 geographic
BRAND_ICP_INCOME       ← Block 7 income class
BRAND_ICP_VALUES       ← Block 7 psychographic values
BRAND_ICP_FEARS        ← Block 7 behavioral fears
BRAND_ICP_ASPIRATIONS  ← Block 7 behavioral aspirations
BRAND_TRANSFORMATION   ← Block 9 transformation arc
```

### visual (from Blocks 16-19)
```
BRAND_COLORS.primary    ← Block 16 primary HEX
BRAND_COLORS.secondary  ← Block 16 secondary HEX
BRAND_COLORS.accent     ← Block 16 accent HEX
BRAND_COLORS.background ← Block 16 background HEX (or inferred)
BRAND_COLORS.foreground ← Block 16 foreground HEX (or inferred)
BRAND_COLORS.surface    ← Block 16 surface HEX (or inferred)
BRAND_FONTS.heading     ← Block 17 heading font
BRAND_FONTS.body        ← Block 17 body font
BRAND_FONTS.mono        ← Block 17 mono font
BRAND_LOGO_URL          ← Block 19 logo reference
BRAND_FAVICON_URL       ← Block 19 favicon reference
BRAND_STYLE             ← Block 18 dominant mood (e.g. "minimal-dark")
```

### positioning (from Blocks 6, 8, 10, Block 28)
```
BRAND_CATEGORY         ← Block 10 category
BRAND_UVP              ← Block 6 UVP statement
BRAND_DIFFERENTIATOR   ← Block 8 unique differentiator
BRAND_COMPETITORS      ← Block 31 competitor names (array)
BRAND_CONTENT_PILLARS  ← Discovery Q13 content themes (array of 3-7)
```

### monetization (from Discovery Q14-Q15)
```
BRAND_PRICING_MODEL      ← Q14 revenue model
BRAND_CURRENCY           ← Q15 currency code
BRAND_PRICE_ANCHOR       ← Highest-tier price
BRAND_TIERS              ← Tier names (array)
BRAND_PAYMENT_PROVIDERS  ← Q15 payment platforms (array)
```

## Validation Rules
1. Run `brand_validate.py` after extraction — all 13 required fields must pass
2. Archetype MUST be exactly 1 of 12 enum values (lowercase)
3. Voice scores MUST be integers 1-5
4. Colors MUST be valid HEX (#RRGGBB)
5. Transformation MUST follow pattern "From X to Y through Z"
6. BRAND_UVP must be >= 20 characters
