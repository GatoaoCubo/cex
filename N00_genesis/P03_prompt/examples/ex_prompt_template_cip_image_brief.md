---
id: p03_pt_cip_image_brief
kind: prompt_template
pillar: P03
title: "CIP Image Brief: Agua Marinha Product Lifestyle"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
agent_group: marketing_agent
domain: marketing
quality: 9.1
tags: [image, cip, branding, visual, prompt-template, product-photography]
tldr: "Filled CIP image brief for Agua Marinha Home lifestyle product shots — soft natural light, scandinavian style"
when_to_use: "Reference example for generating brand-safe AI product images"
keywords: [image-generation, brand-visual, product-lifestyle, ai-photography]
long_tails:
  - como gerar fotos de produto com IA mantendo identidade visual
  - prompt para imagem de produto estilo escandinavo
variables:
  - name: brand_name
    value: "Agua Marinha Home"
  - name: category
    value: "digital"
  - name: lighting_modifier
    value: "soft natural window light, golden hour warmth"
  - name: style
    value: "minimalist scandinavian with warm wood accents"
  - name: deliverables_count
    value: 3
  - name: aspect_ratio
    value: "1:1"
  - name: negative_prompts
    value: [text, watermark, logo, human faces, cluttered background]
density_score: 0.90
---

# CIP Image Brief: Agua Marinha Product Lifestyle

## Context

Agua Marinha Home sells home decor and lifestyle products on Brazilian marketplaces (ML, Shopee, Amazon BR). This brief generates AI product images for Instagram feed posts and marketplace hero images. Brand identity: coastal minimalism, natural materials, warm Scandinavian aesthetic.

## Filled Brief

```
BRAND: Agua Marinha Home
CATEGORY: digital
STYLE: minimalist scandinavian with warm wood accents
LIGHTING: soft natural window light, golden hour warmth

BRIEF:
Generate 3 image(s) for Agua Marinha Home in digital format.
Visual style: minimalist scandinavian with warm wood accents.
Lighting: soft natural window light, golden hour warmth.
Aspect ratio: 1:1.

REQUIREMENTS:
1. No text/typography in the image (brand name provided for context only)
2. Consistent lighting across all 3 variations
3. Category-appropriate composition:
   - digital: RGB, screen-optimized contrast
4. Product centered on natural wood surface or linen textile
5. Background: soft-focus coastal or neutral interior setting
6. Color palette: sand (#C2B280), ocean blue (#4F97A3), warm white (#FAF0E6)
7. Props: dried eucalyptus, ceramic vases, woven baskets (brand-adjacent only)

EXCLUDE: text, watermark, logo, human faces, cluttered background

OUTPUT: 3 variations with consistent style
  - Variation 1: Product on oak shelf, window light from left, eucalyptus accent
  - Variation 2: Product on linen tablecloth, overhead diffused light, ceramic vase nearby
  - Variation 3: Product in styled vignette, golden hour side light, woven basket background
```

## Verification Checklist

- [x] brand_name is non-empty: "Agua Marinha Home"
- [x] category is valid enum: "digital"
- [x] lighting_modifier specified: "soft natural window light, golden hour warmth"
- [x] negative_prompts defined: 5 exclusions listed
- [x] aspect_ratio specified: 1:1 (Instagram feed optimized)
- [x] Each variation has distinct composition while maintaining style unity
- [x] Color palette hex codes provided for reproduction consistency

## Quality Gates Applied

- brand_name present: prevents AI text hallucination in generated images
- lighting_modifier explicit: ensures consistent look across 3 variations
- No vague language: every requirement has specific, measurable criteria
- Category locked to "digital": RGB color space, screen contrast optimization
- Props restricted to brand-adjacent items only (no random objects)

## Platform Mapping

| Platform | Aspect | Adaptation |
|----------|--------|------------|
| Instagram Feed | 1:1 | Use as-is |
| Instagram Story | 9:16 | Extend background vertically, keep product centered |
| Shopee Hero | 1:1 | Add 10% padding for mobile crop safety |
| ML Listing | 4:3 | Slight horizontal crop, maintain product focus |

---
*CIP Image Brief v1.0 | marketing_agent Marketing Domain | 2026-03-24*
