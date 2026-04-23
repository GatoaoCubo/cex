---
id: bld_schema_tagline
kind: schema
pillar: P06
builder: tagline-builder
version: 1.0.0
quality: 9.1
title: "Schema Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - n06_schema_brand_config
  - bld_schema_landing_page
  - bld_schema_training_method
  - bld_schema_multimodal_prompt
  - bld_schema_model_architecture
  - bld_schema_action_paradigm
  - bld_schema_retriever_config
  - bld_schema_dataset_card
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

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `schema` |
| Pillar | P06 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | sibling | 0.55 |
| [[bld_schema_experiment_tracker]] | sibling | 0.50 |
| [[n06_schema_brand_config]] | related | 0.48 |
| [[bld_schema_landing_page]] | sibling | 0.43 |
| [[bld_schema_training_method]] | sibling | 0.42 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.40 |
| [[bld_schema_model_architecture]] | sibling | 0.40 |
| [[bld_schema_action_paradigm]] | sibling | 0.38 |
| [[bld_schema_retriever_config]] | sibling | 0.38 |
| [[bld_schema_dataset_card]] | sibling | 0.38 |
