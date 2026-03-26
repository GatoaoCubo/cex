---
# TEMPLATE: CIP Image Brief (P03 Prompt)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P03_prompt/_schema.yaml (types.prompt_template)
# Max 2KB | quality_min: 7.0
# Sintaxe: {{MUSTACHE}} = template engine | [BRACKET] = humano/agente decide

id: p03_pt_cip_image_brief
kind: prompt_template
pillar: P03
title: "CIP Image Brief"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: marketing
quality: 8.5
tags: [image, cip, branding, visual, prompt-template]
tldr: "Structured image generation prompt with brand safety and lighting control"
when_to_use: "When generating product/brand images via AI (Midjourney, DALL-E, Flux)"
keywords: [image-generation, brand-visual, cip, creative-brief]
variables:
  - name: brand_name
    type: string
    description: "Exact brand name to embed in image context (prevents AI inventing text)"
    example: "Agua Marinha Home"
  - name: category
    type: string
    description: "Deliverable category"
    example: "digital"
  - name: lighting_modifier
    type: string
    description: "Lighting style for visual consistency"
    example: "soft natural window light"
  - name: style
    type: string
    description: "Visual style direction"
    example: "minimalist scandinavian"
density_score: 0.85
---

# CIP Image Brief

## Purpose
Generate brand-safe, consistent AI image prompts with controlled lighting, style, and category-specific deliverable lists.

## Variables

| Var | Tipo | Descricao | Exemplo |
|-----|------|-----------|---------|
| `{{brand_name}}` | string | Brand name (REQUIRED — prevents AI text hallucination) | Agua Marinha Home |
| `{{category}}` | enum | print / digital / signage / merch / vehicle / env | digital |
| `{{lighting_modifier}}` | string | Lighting style for consistency across assets | soft natural window light |
| `{{style}}` | string | Visual style keywords | minimalist scandinavian |
| `{{deliverables_count}}` | int | Number of variations to generate | 3 |
| `{{aspect_ratio}}` | string | Output dimensions | 1:1, 4:5, 16:9 |
| `{{negative_prompts}}` | list | What to exclude from generation | [text, watermark, logo] |

## Template Body

```
BRAND: {{brand_name}}
CATEGORY: {{category}}
STYLE: {{style}}
LIGHTING: {{lighting_modifier}}

BRIEF:
Generate {{deliverables_count}} image(s) for {{brand_name}} in {{category}} format.
Visual style: {{style}}.
Lighting: {{lighting_modifier}}.
Aspect ratio: {{aspect_ratio}}.

REQUIREMENTS:
1. No text/typography in the image (brand name provided for context only)
2. Consistent lighting across all variations
3. Category-appropriate composition:
   - print: CMYK-safe colors, bleed area consideration
   - digital: RGB, screen-optimized contrast
   - signage: high contrast, readable at distance
   - merch: mockup-ready, transparent areas where needed
   - vehicle: wrap-compatible, seam-aware layout
   - env: spatial context, scale reference

EXCLUDE: {{negative_prompts}}

OUTPUT: {{deliverables_count}} variations with consistent style
```

## Quality Gates
- brand_name REQUIRED: never generate without explicit brand context
- lighting_modifier REQUIRED: unlighted prompts produce inconsistent sets
- No vague prompts: "make something cool" is rejected — specifics required
- category must be one of: print / digital / signage / merch / vehicle / env
- No embedded text in generated images (text hallucination prevention)

## Examples

**Exemplo 1**
- Input: `brand_name=Agua Marinha Home, category=digital, lighting=soft natural window light, style=minimalist scandinavian, deliverables_count=3`
- Output: 3 product lifestyle images, soft lit, scandinavian aesthetic, no text, 1:1 ratio

**Exemplo 2**
- Input: `brand_name=Gato ao Cubo, category=merch, lighting=studio flat light, style=playful geometric, deliverables_count=2`
- Output: 2 mockup-ready designs, flat studio lit, geometric cat motifs, transparent background areas

## Verification
- [ ] brand_name is non-empty and matches client brand
- [ ] category is valid enum value
- [ ] lighting_modifier specified (not empty)
- [ ] Generated images contain no hallucinated text
- [ ] Style consistency across all deliverables in set

## Semantic Bridge
- Also known as: image brief, visual prompt, creative brief
- Keywords: ai-image, brand-photography, product-visual
- Equivalents: Midjourney: /imagine prompt | DALL-E: generation prompt | Flux: prompt template
