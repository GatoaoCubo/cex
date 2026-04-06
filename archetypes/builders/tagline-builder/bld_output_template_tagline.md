---
id: bld_output_template_tagline
kind: output_template
pillar: P05
builder: tagline-builder
version: 1.0.0
---
# Output Template: Tagline

Use this template to produce structured tagline deliverables. Every field must be filled.
The recommended tagline goes in the frontmatter `title` field for indexing.

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
- **Site Hero**: Use recommended tagline as-is, pair with sub-headline for context
- **Social Bio**: Use medium variant, append URL or CTA
- **Ad Headline**: Use short variant for display ads, medium for search ads
- **Email Subject**: Use question or provocative variant for higher open rates
- **Pitch Deck**: Use aspirational variant on title slide, functional on solution slide

## Revision History
- v1.0.0: Initial tagline set generated from brand_config + USP extraction
- Future: A/B test results can inform which variant wins for each context
- Memory: Approved taglines stored in builder memory for consistency across future builds
```
