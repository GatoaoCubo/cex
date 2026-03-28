# HOP: Prompt Generator | photo_agent v4.2.0

**Phase**: 2-3
**Purpose**: Generate CONVERSION prompts from analysis
**Input**: `{PRODUTO, COR, MATERIAL, FORMA, BENEFICIO_PRINCIPAL, emotional_contexts}`
**Output**: `{IMAGEM 3x3, JSON monobloco (productName + prompts)}`
**Framework**: CONVERSION (Emotion > Angle)

---

## CRITICAL CHANGE v4.2

### ANTES (v3.x - ERRADO)
```
OUTPUT 2 = 9 blocos separados de codigo
```

### AGORA (v4.2 - CORRETO)
```
PROMPT 2 = 1 BLOCO UNICO com 9 cenas sequenciais
         -> Usuario copia 1 prompt
         -> LLM gera 9 imagens em sequencia
         -> 1 prompt = 9 image outputs
```

**NAO SEPARAR EM 9 BLOCOS DIFERENTES!**

---

## TASK

Generate prompts using extracted product attributes and emotional contexts:

1. **IMAGEM 3x3 GRID**: Gerar via gpt-image-1 (9 cenas em 1 imagem)
2. **PROMPT 1**: Grid 3x3 - 1 bloco unico
3. **PROMPT 2**: 9 Cenas Sequenciais - 1 bloco unico

---

## CONVERSION FRAMEWORK

### OLD Approach (v10)
```
- Flat Lay (aesthetic without purpose)
- Packaging (low conversion)
- Technical View (angle-based)
- Scale Reference (informational)
```

### NEW Approach (v4.2)
```
- Problem State (pain trigger)
- Solution Moment (relief trigger)
- Transformation (desire trigger)
- Social Belonging (belonging trigger)
- Benefit Proof (curiosity trigger)
- Emotional Peak (pleasure trigger)
- Lifestyle Dream (aspiration trigger)
```

**100% of scenes have PSYCHOLOGICAL PURPOSE**

---

## CRITICAL RULES

### Every Prompt Must Start With
```
{user_image} {seed:[RANDOM]}
```

This is NON-NEGOTIABLE. Without this anchor, the AI will invent a product.

### Required Elements
```yaml
all_prompts:
  - "{user_image} {seed:[RANDOM]}" at START
  - "photorealistic NOT 3D render NOT illustration NOT CGI"
  - "no text, no logos, no watermarks"
  - "8K"
  - "brand/style lock"
  - Emotional trigger specification

scenes_1_and_9:
  - "fidelity weight 5"
  - "exact color"
  - "marketplace compliant"
  - "white #FFFFFF"

scenes_2_3_4_6:
  - "fidelity weight 4"
  - Specific emotional context

scenes_5_7_8:
  - "fidelity weight 3"
  - Creative flexibility for emotional scenes
```

---

## PROMPT 1 GENERATION (Grid 3x3)

### Template (1 BLOCO UNICO)
```
{user_image} {seed:[RANDOM]} [GENERATE_3x3_GRID_9_SCENES]

Professional e-commerce product photography GRID 3x3 (9 scenes in ONE image) of {PRODUTO}.
Product specs: {COR} {MATERIAL} {FORMA}. Main benefit: {BENEFICIO_PRINCIPAL}.

GRID LAYOUT:
[1-Hero #FFFFFF][2-Problem context][3-Solution moment]
[4-Transformation][5-Social belonging][6-Benefit macro]
[7-Emotional peak][8-Lifestyle dream][9-Marketplace #FFFFFF]

Scene 1: Hero trust, white #FFFFFF, centered 85%, high-key softbox, fidelity weight 5.
Scene 2: Problem state, realistic context, natural light, pain recognition.
Scene 3: Solution moment, product solving problem, relief visible.
Scene 4: Transformation, after state achieved, warm light, desire trigger.
Scene 5: Social belonging, real people using naturally, family/friends context.
Scene 6: Benefit proof, macro of key feature, ring light, curiosity trigger.
Scene 7: Emotional peak, pleasure/joy moment, golden warm light.
Scene 8: Lifestyle dream, premium environment, elegant ambient light.
Scene 9: Marketplace, white #FFFFFF, centered 85%, fidelity weight 5, trust closure.

Canon EOS R5, photorealistic NOT 3D NOT illustration NOT CGI.
MAINTAIN EXACT {COR} {MATERIAL} across all 9 scenes - FIDELITY CRITICAL.
No text, no logos, no watermarks, brand/style lock. 8K marketplace compliant.
Generate as SINGLE 3x3 GRID image.
```

---

## PROMPT 2 GENERATION (9 Cenas Sequenciais)

### Template (1 BLOCO UNICO - NAO 9 SEPARADOS)

```
{user_image} {seed:[RANDOM]} [GENERATE_9_IMAGES_SEQUENTIALLY]

Generate 9 SEPARATE IMAGES in sequence for {PRODUTO}. Product specs: {COR} {MATERIAL} {FORMA}.
CRITICAL: Generate ALL 9 images without stopping. 1 prompt = 9 images output.

IMAGE 1/9 - HERO TRUST:
{PRODUTO}, hero shot, white #FFFFFF background, {COR} {MATERIAL}, centered 85%, high-key softbox, Canon R5 85mm f/8, photorealistic, fidelity weight 5, exact color match, professional trustworthy, 8K.

IMAGE 2/9 - PROBLEM STATE:
{PRODUTO}, problem state scene, showing frustration/inconvenience this product solves, {PROBLEMA_CONTEXTO}, realistic environment, natural light, 35-50mm f/2.8-f/4, pain recognition, photorealistic, 8K.

IMAGE 3/9 - SOLUTION MOMENT:
{PRODUTO}, solution moment, product ACTIVELY RESOLVING problem, {SOLUCAO_CONTEXTO}, relief visible, 50mm f/4-f/5.6, satisfaction trigger, photorealistic, 8K.

IMAGE 4/9 - TRANSFORMATION:
{PRODUTO}, transformation scene, AFTER state achieved, {RESULTADO_CONTEXTO}, warm welcoming light, 50mm f/2.8-f/4, aspiration trigger, photorealistic, 8K.

IMAGE 5/9 - SOCIAL BELONGING:
{PRODUTO}, social belonging, real people using naturally, {SOCIAL_CONTEXTO}, group/family context, natural window light, 35mm f/2.8-f/4, belonging trigger, photorealistic, 8K.

IMAGE 6/9 - BENEFIT PROOF:
{PRODUTO}, benefit proof macro, close-up KEY FEATURE delivering {BENEFICIO_PRINCIPAL}, {FEATURE_DETALHE}, ring light, 100mm macro f/2.8-f/4, curiosity trigger, photorealistic, 8K.

IMAGE 7/9 - EMOTIONAL PEAK:
{PRODUTO}, emotional peak, moment of PLEASURE/JOY, {EMOCAO_CONTEXTO}, genuine smile, golden warm light, 85mm f/2.8, pleasure trigger, photorealistic, 8K.

IMAGE 8/9 - LIFESTYLE DREAM:
{PRODUTO}, lifestyle dream, PREMIUM ASPIRATIONAL environment, {LIFESTYLE_CONTEXTO}, elegant setting, ambient light, 24-35mm f/4, aspiration trigger, photorealistic, 8K.

IMAGE 9/9 - MARKETPLACE:
{PRODUTO}, marketplace compliance, white #FFFFFF, {COR} {MATERIAL}, centered 85%, high-key soft-even, 85mm f/8-f/11, photorealistic NOT 3D, fidelity weight 5, exact color, trust closure, 8K.

CRITICAL INSTRUCTIONS:
- Generate ALL 9 images in ONE execution - DO NOT STOP
- Maintain EXACT product appearance across all 9
- Each image is SEPARATE (not a grid)
- 1 prompt submission = 9 image outputs
```

**ESTE E 1 BLOCO UNICO - NAO SEPARAR EM 9!**

---

## SUBSTITUTION RULES

When generating output, substitute:

### Product Attributes
- `{PRODUTO}` -> extracted description
- `{COR}` -> extracted hex code
- `{MATERIAL}` -> extracted material
- `{FORMA}` -> extracted shape
- `{BENEFICIO_PRINCIPAL}` -> main benefit

### Emotional Contexts
- `{PROBLEMA_CONTEXTO}` -> realistic problem context
- `{SOLUCAO_CONTEXTO}` -> solution being delivered
- `{RESULTADO_CONTEXTO}` -> transformation achieved
- `{SOCIAL_CONTEXTO}` -> social/group context
- `{FEATURE_DETALHE}` -> key feature close-up
- `{EMOCAO_CONTEXTO}` -> moment of joy
- `{LIFESTYLE_CONTEXTO}` -> premium environment

---

## PNL TRIGGERS BY SCENE

| Scene | Trigger | Mechanism | Prompt Keyword |
|-------|---------|-----------|----------------|
| 1 | Trust | "Professional = trustworthy" | `trust and professionalism` |
| 2 | Pain | "MY problem = relevance" | `pain recognition trigger` |
| 3 | Relief | "WORKS = confidence" | `satisfaction trigger` |
| 4 | Desire | "I WANT = motivation" | `aspiration trigger` |
| 5 | Belonging | "People like me = validation" | `belonging trigger` |
| 6 | Curiosity | "I SEE quality = conviction" | `curiosity trigger` |
| 7 | Pleasure | "I'll FEEL = anchor" | `pleasure trigger` |
| 8 | Aspiration | "MY future = desire" | `aspiration trigger` |
| 9 | Action | "Ready to buy = closure" | `trust closure` |

---

## OUTPUT FORMAT (JSON MONOBLOCO - 2 CAMPOS)

```json
{
  "productName": "Nome do Produto",
  "prompts": "## Analise\n...\n## PROMPT 1\n```\n...\n```\n## PROMPT 2\n```\n...\n```"
}
```

**IMPORTANTE**: O campo `prompts` contem:
- Analise do produto
- PROMPT 1 (1 bloco unico - grid 3x3)
- PROMPT 2 (1 bloco unico - 9 cenas sequenciais)

---

## VALIDATION

Before outputting:
- [ ] ALL prompts start with `{user_image} {seed:[RANDOM]}`
- [ ] All product placeholders substituted
- [ ] All emotional context placeholders substituted
- [ ] PROMPT 1 = 1 bloco unico (grid 3x3)
- [ ] PROMPT 2 = 1 bloco unico (NAO 9 separados)
- [ ] Scenes 1 and 9 have `fidelity weight 5` and `#FFFFFF`
- [ ] Each scene has emotional trigger keyword
- [ ] All scenes have photorealistic tags
- [ ] No empty aesthetic shots (flat lay, packaging without context)

---

**HOP Version**: 4.2.0
**Last Updated**: 2025-12-18
**Framework**: CONVERSION + 3x3 GRID + MONOBLOCO
