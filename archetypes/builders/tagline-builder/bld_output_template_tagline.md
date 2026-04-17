---
id: bld_output_template_tagline
kind: output_template
pillar: P05
builder: tagline-builder
version: 1.0.0
quality: 9.1
title: "Output Template Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: PRODUCE
---
# Output Template: Tagline
Structured tagline deliverable. Fill every field. Recommended tagline goes in frontmatter `title`.
```markdown
---
id: tagline_{{BRAND_SLUG}}
kind: tagline
pillar: P03
title: "{{RECOMMENDED_TAGLINE}}"
version: 1.0.0
created: {{DATE}}
author: tagline-builder
quality: null
tags: [tagline, brand, {{BRAND_SLUG}}, marketing]
brand: "{{BRAND_NAME}}"
---
# Tagline: {{BRAND_NAME}}

## USP
{{USP_ONE_SENTENCE}}

## Recommended
> **{{RECOMMENDED_TAGLINE}}**

**Reasoning**: {{REASONING}}

## Variants

### Short (3-5 words)
| # | Text | Approach | Score |
|---|------|----------|-------|
{{SHORT_VARIANTS}}

### Medium (6-10 words)
| # | Text | Approach | Score |
|---|------|----------|-------|
{{MEDIUM_VARIANTS}}

### Long (11-15 words)
| # | Text | Approach | Score |
|---|------|----------|-------|
{{LONG_VARIANTS}}

## Context Adaptations

| Context | Text |
|---------|------|
| Site Hero | {{HERO}} |
| Social Bio | {{BIO}} |
| Ad Headline | {{AD}} |
| Email Subject | {{EMAIL}} |
| Pitch Deck | {{PITCH}} |

## Competitors Avoided
{{COMPETITORS_TABLE}}

## Usage Guide

| Context | Variant | Pairing |
|---------|---------|---------|
| Site Hero | Recommended as-is | Sub-headline for context |
| Social Bio | Medium variant | Append URL or CTA |
| Display Ads | Short variant | Visual + brand logo |
| Search Ads | Medium variant | Description line below |
| Email Subject | Question/provocative | Preview text complements |
| Pitch Title | Aspirational variant | Logo + one visual |
| Pitch Solution | Functional variant | Problem-solution frame |

## Scoring Criteria

| Dimension | Weight | Measures |
|-----------|--------|----------|
| Memorability | 30% | Rhythm, brevity, recall ease |
| Differentiation | 25% | Distance from competitor taglines |
| Brand Fit | 20% | Voice, values, personality match |
| Versatility | 15% | Works across all 5+ contexts |
| Emotional Pull | 10% | Desire, curiosity, aspiration |

## Revision History

| Version | Change | Source |
|---------|--------|--------|
| v1.0.0 | Initial set from brand_config + USP | tagline-builder |
| Future | A/B test winners per context | analytics |
| Memory | Approved taglines stored for consistency | builder memory |
```
