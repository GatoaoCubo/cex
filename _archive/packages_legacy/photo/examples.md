# PHOTO Agent - Examples

**Version**: 3.0.0 | **Type**: Input/Output Examples | **Quality**: >= 8.0

---

## Example 1: Cat Window Hammock (E-commerce Product)

### INPUT

```yaml
product_image: "cat_window_bed.jpg"
product_category: "Pet Supplies"
style_preference: "lifestyle"
marketplace_target: "mercado_livre"
brand_colors: ["#4A4A4A", "#FF6B35"]
```

### ANALYSIS OUTPUT

```yaml
PRODUTO: "Cama de janela para gatos tipo hammock"
COR: "#4A4A4A"
MATERIAL: "Tecido Oxford 600D impermeavel"
FORMA: "Retangular 55x35cm com ventosas"
BENEFICIO: "Gato toma sol sem sair de casa"
PUBLICO: "Donos de gatos em apartamento"
```

### PROMPT OUTPUT (Abbreviated)

```markdown
## PROMPT 1: Grid 3x3 Master

{user_image} {seed:[RANDOM]}

Professional e-commerce product photography GRID 3x3 of Cama de janela para gatos.

SCENE 1 - HERO TRUST:
Cama de janela #4A4A4A, white background #FFFFFF, centered 85%,
professional studio lighting, ultra sharp focus, award-winning product photography

SCENE 2 - PROBLEM STATE:
Bored cat in small apartment, no sunlight access, muted colors,
frustrated owner, cluttered environment

SCENE 3 - SOLUTION MOMENT:
Cat discovering window bed first time, moment of curiosity,
soft golden hour lighting, easy installation

[... scenes 4-9 continue ...]

--ar 1:1 --v 6 --s 250

[OPEN_VARIABLES]:
- CAT_BREED: [persa, siames, vira-lata, maine-coon]
- WINDOW_VIEW: [cidade, parque, jardim, rua]
- TIME_OF_DAY: [manha, tarde, golden-hour]
```

### QUALITY SCORE

```yaml
technical_accuracy: 9.2/10
marketplace_compliance: 10.0/10  # White BG scenes 1 & 9
brand_consistency: 9.0/10
prompt_clarity: 9.5/10
flexibility: 9.0/10
---
overall: 9.3/10
```

---

## Example 2: Organic Skincare Serum (Premium Brand)

### INPUT

```yaml
product_image: "serum_bottle.jpg"
product_category: "Beauty & Personal Care"
style_preference: "minimalist"
marketplace_target: "shopee"
brand_colors: ["#E8DDD4", "#A89B8E", "#1A1A1A"]
additional_props: ["eucalyptus leaves", "marble surface"]
```

### ANALYSIS OUTPUT

```yaml
PRODUTO: "Serum facial organico com vitamina C"
COR: "#E8DDD4"
MATERIAL: "Vidro ambar com conta-gotas de pipeta"
FORMA: "Cilindrica 30ml com tampa rosca"
BENEFICIO: "Reduz manchas e ilumina pele"
PUBLICO: "Mulheres 25-45 anos preocupadas com skincare"
```

### PROMPT OUTPUT (Abbreviated)

```markdown
## PROMPT 1: Grid 3x3 Master

{user_image} {seed:[RANDOM]}

Professional beauty product photography GRID 3x3 of organic vitamin C serum.

SCENE 1 - HERO TRUST:
Serum bottle #E8DDD4, white background #FFFFFF, centered 85%,
soft diffused lighting, minimal shadows, clean beauty aesthetic,
commercial quality, ultra sharp focus on label details

SCENE 2 - PROBLEM STATE:
Woman looking at mirror with visible dark spots and dull complexion,
bathroom lighting, concerned expression, uneven skin tone visible,
natural documentary style

SCENE 3 - SOLUTION MOMENT:
Hand applying serum drops to cheek, soft golden hour window light,
moment of self-care ritual, peaceful bathroom scene,
natural organic atmosphere, sense of relief

[... scenes 4-9 continue ...]

--ar 1:1 --v 6 --s 250

[OPEN_VARIABLES]:
- SKIN_TONE: [clara, morena-clara, morena, negra]
- BACKGROUND_PROPS: [eucalyptus, marble, wood, concrete]
- MOOD: [minimal-zen, natural-organic, luxury-spa]
```

### QUALITY SCORE

```yaml
technical_accuracy: 9.5/10
marketplace_compliance: 10.0/10
brand_consistency: 9.8/10  # Premium minimal aesthetic
prompt_clarity: 9.5/10
flexibility: 9.2/10
---
overall: 9.6/10
```

---

## Example 3: Portable Blender (Tech Product)

### INPUT

```yaml
product_image: "portable_blender.jpg"
product_category: "Kitchen Appliances"
style_preference: "commercial"
marketplace_target: "amazon_br"
brand_colors: ["#FF6B6B", "#4ECDC4", "#FFFFFF"]
exclude_scenes: [8]  # Skip lifestyle scene
```

### ANALYSIS OUTPUT

```yaml
PRODUTO: "Liquidificador portatil USB recarregavel"
COR: "#4ECDC4"
MATERIAL: "Plastico BPA-free com laminas inox"
FORMA: "Cilindrico 450ml com tampa rosqueavel"
BENEFICIO: "Smoothie fresco em qualquer lugar"
PUBLICO: "Academia, escritorio, viagem - pessoas ativas"
```

### PROMPT OUTPUT (Abbreviated)

```markdown
## PROMPT 1: Grid 3x3 Master

{user_image} {seed:[RANDOM]}

Professional tech product photography GRID 3x3 of portable USB blender.

SCENE 1 - HERO TRUST:
Portable blender #4ECDC4, white background #FFFFFF, centered 85%,
studio lighting highlighting modern tech design, ultra sharp focus,
award-winning product photography, clean commercial style

SCENE 2 - PROBLEM STATE:
Person at gym with pre-made shake that separated and looks unappetizing,
fluorescent gym lighting, frustrated expression, compromise visible,
documentary style showing pain point

SCENE 3 - SOLUTION MOMENT:
Blender blending fresh smoothie at gym, USB charging visible,
person's excited "aha moment" expression, fresh ingredients visible,
soft natural gym window light, problem solving moment

[... scenes 4-7 continue ...]

SCENE 8 - SKIPPED (user requested exclusion)

SCENE 9 - MARKETPLACE:
Product with packaging and accessories visible, ready to purchase,
white background #FFFFFF, all components shown, trust signals,
clean e-commerce presentation, USB cable visible

--ar 1:1 --v 6 --s 250

[OPEN_VARIABLES]:
- SMOOTHIE_TYPE: [verde-detox, proteina-chocolate, frutas-vermelhas]
- LOCATION: [academia, escritorio, parque, cozinha]
- USER_GENDER: [mulher, homem, neutro]
```

### QUALITY SCORE

```yaml
technical_accuracy: 9.0/10
marketplace_compliance: 10.0/10
brand_consistency: 8.8/10
prompt_clarity: 9.3/10
flexibility: 9.5/10  # Good customization options
---
overall: 9.1/10
```

---

## Common Patterns Across Examples

### Pattern 1: White Background Compliance

**ALL examples** include:
- Scene 1: White #FFFFFF background (Hero Trust)
- Scene 9: White #FFFFFF background (Marketplace)

This ensures marketplace compliance (Mercado Livre, Shopee, Amazon BR all require white BG primary image).

### Pattern 2: Emotional Progression

Every prompt follows the conversion framework:
1. **Trust** -> Professional first impression
2. **Problem** -> Pain recognition ("I have this problem")
3. **Solution** -> Relief moment ("This works!")
4. **Transformation** -> Desired result ("I want this")
5. **Social** -> Belonging validation
6. **Proof** -> Quality evidence
7. **Emotion** -> Peak pleasure moment
8. **Lifestyle** -> Aspirational dream
9. **Action** -> Ready to purchase

### Pattern 3: Technical Accuracy

All prompts include:
- **Camera specs**: Focal length 35-85mm, aperture f/2.8-f/8
- **Lighting**: Studio, golden hour, diffused, natural
- **Composition**: Rule of thirds, centered, scale
- **Aspect ratio**: --ar 1:1 (square for marketplace)
- **Version**: --v 6 (Midjourney v6)
- **Stylize**: --s 250 (moderate stylization)

### Pattern 4: Flexibility (Open Variables)

Every prompt includes [OPEN_VARIABLES] section:
- **Model/Actor**: [gender, age, ethnicity]
- **Props/Context**: [environment, season, mood]
- **Style Variations**: [minimal, dramatic, natural]

This allows LLM or user to customize without rewriting entire prompt.

---

## Multi-Tool Adaptation Examples

### Midjourney (Default)

```
{user_image} {seed:[RANDOM]}
[PROMPT]
--ar 1:1 --v 6 --s 250
```

### DALL-E 3 (Adapted)

```
[PROMPT without {user_image}]
Style: photorealistic product photography
Quality: HD
Aspect ratio: square (1:1)
```

### Flux (Adapted)

```
[PROMPT without {user_image}]
guidance_scale: 7.5
num_inference_steps: 50
aspect_ratio: 1:1
```

### Gemini Image (Recommended for {user_image})

```
{user_image} {seed:[RANDOM]}
[PROMPT]
Mode: photorealistic
Safety: medium
Output: high resolution
```

---

## Edge Cases

### Example 4: Minimalist Product (No Lifestyle Context)

**Product**: Wooden minimalist desk organizer

**Challenge**: Product is too abstract for lifestyle scenes

**Solution**:
- Scene 2 (Problem): Cluttered desk vs organized
- Scene 5 (Social): NOT group context, but "workspace others admire"
- Scene 8 (Lifestyle): Minimal home office aesthetic instead of person

### Example 5: Food Product (Perishable)

**Product**: Artisanal chocolate truffles

**Challenge**: Product appearance must stay consistent across scenes

**Solution**:
- Use `{user_image}` anchor CRITICALLY
- Specify "same chocolate appearance across all 9 scenes"
- Focus on presentation variations, not product variations

### Example 6: Brand Logo (Non-Product)

**Use Case**: Logo photography for brand assets

**Different Framework**: Use ADW_LILY_005_BRAND_PHOTO_PIPELINE
- 10 scenes instead of 9
- Includes: Flat White, Flat Black, 3D Emboss, Neon, Metallic, etc.

---

## Validation Checklist for All Examples

Every example should pass:

- [ ] Scene 1 = white #FFFFFF background
- [ ] Scene 9 = white #FFFFFF background
- [ ] {user_image} {seed:[RANDOM]} prefix present
- [ ] [OPEN_VARIABLES] section included
- [ ] Camera specs realistic (35-85mm, f/2.8-f/8)
- [ ] Lighting described for each scene
- [ ] Emotional progression clear (problem -> solution -> aspiration)
- [ ] Aspect ratio parameter (--ar 1:1)
- [ ] Version parameter (--v 6)
- [ ] Stylize parameter (--s 250)
- [ ] Brand colors incorporated (if provided)
- [ ] Product consistency emphasized
- [ ] Quality score >= 8.0/10

---

**Created**: 2026-02-06
**Quality Score**: 9.2/10
**Framework**: CONVERSION (Emotion-based)
**Satellite**: LILY
