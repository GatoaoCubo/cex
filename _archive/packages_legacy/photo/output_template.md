# OUTPUT TEMPLATE | photo_agent v5.0.0 (PURE MARKDOWN)

**Version**: 5.0.0 | **Date**: 2025-12-20
**Format**: Image + Plain Markdown Text
**Framework**: CONVERSION (Emotion-based)

---

## CRITICAL CHANGES v5.0

**REMOVED**:
- JSON structured output
- Widget rendering
- `productName` field
- `prompts` field
- `imageUrl` field

**NEW BEHAVIOR**:
- gpt-image-1 generates 3x3 grid automatically
- Image appears in chat first
- Then plain markdown text with analysis + 2 prompts
- User copies prompts and uses in Gemini/Nanobana

---

## OUTPUT FORMAT (2 PARTS)

```
+---------------------------------------------+
|  PART 1: IMAGE (automatic)                  |
|  [3x3 GRID - gerada pelo gpt-image-1]       |
|  (aparece automaticamente no chat)          |
+---------------------------------------------+

+---------------------------------------------+
|  PART 2: MARKDOWN TEXT                      |
|  - Analise do Produto (tabela)              |
|  - Contextos Emocionais (7 items)           |
|  - PROMPT 1: Grid 3x3 (copy/paste ready)   |
|  - PROMPT 2: 9 Cenas Sequenciais            |
|  - CONFIDENCE score                         |
+---------------------------------------------+
```

---

## MARKDOWN STRUCTURE

```markdown
[IMAGEM 3x3 GRID - ja foi gerada acima automaticamente]

## Analise do Produto

| Atributo | Valor |
|----------|-------|
| **Produto** | [descricao concisa] |
| **Cor** | [#HEXCODE] |
| **Material** | [material + acabamento] |
| **Forma** | [formato/estrutura] |
| **Beneficio Principal** | [problema que resolve] |
| **Publico** | [quem compra] |

### Contextos Emocionais
- **PROBLEMA**: [contexto de dor]
- **SOLUCAO**: [momento de resolucao]
- **TRANSFORMACAO**: [resultado alcancado]
- **SOCIAL**: [contexto de grupo]
- **FEATURE**: [detalhe chave]
- **EMOCAO**: [momento de prazer]
- **LIFESTYLE**: [ambiente aspiracional]

---

## PROMPT 1: Grid 3x3 (1 imagem com 9 cenas)

> **Como usar**: Copie o bloco abaixo, abra Gemini/Nanobana, anexe sua imagem do produto, cole e gere.

```
{user_image} {seed:[RANDOM]} [GENERATE_3x3_GRID_9_SCENES]

Professional e-commerce product photography GRID 3x3 (9 scenes in ONE image) of [PRODUTO].

[Scene 1: Hero Trust][Scene 2: Problem State][Scene 3: Solution Moment]
[Scene 4: Transformation][Scene 5: Social Belonging][Scene 6: Benefit Proof]
[Scene 7: Emotional Peak][Scene 8: Lifestyle Dream][Scene 9: Marketplace Context]

CRITICAL REQUIREMENTS:
- Generate as SINGLE IMAGE with 3x3 grid layout
- Maintain EXACT product appearance across all 9 scenes
- Each scene shows different context/emotion
- Professional lighting and composition

SCENE DETAILS:

SCENE 1 - HERO TRUST (top-left):
[produto], white background #FFFFFF, centered composition 85%, professional studio lighting, ultra sharp focus, award-winning product photography

SCENE 2 - PROBLEM STATE (top-center):
[contexto de dor/problema que o produto resolve], muted colors, frustrated expression, cluttered environment

SCENE 3 - SOLUTION MOMENT (top-right):
[produto sendo usado], moment of relief, soft golden hour lighting, person discovering solution

SCENE 4 - TRANSFORMATION (middle-left):
Before/after split composition, [resultado alcancado], dramatic improvement, side-by-side comparison

SCENE 5 - SOCIAL BELONGING (middle-center):
[contexto social/grupo], friends enjoying together, warm inviting atmosphere, lifestyle photography

SCENE 6 - BENEFIT PROOF (middle-right):
Close-up of [feature chave], technical detail visible, macro photography, professional lighting highlighting quality

SCENE 7 - EMOTIONAL PEAK (bottom-left):
[momento de prazer/satisfacao], genuine smile, soft bokeh background, emotional connection moment

SCENE 8 - LIFESTYLE DREAM (bottom-center):
[ambiente aspiracional], luxury setting, premium lifestyle context, aspirational composition

SCENE 9 - MARKETPLACE CONTEXT (bottom-right):
Product in packaging, ready to purchase, clean e-commerce style, call-to-action implicit

TECHNICAL SPECS:
- Resolution: 1024x1024 minimum
- Style: Professional product photography
- Lighting: Studio quality
- Consistency: Same product across all 9 scenes
- Layout: Perfect 3x3 grid with equal spacing

Generate as SINGLE 3x3 GRID image.
```

---

## PROMPT 2: 9 Cenas Sequenciais (1 prompt = 9 imagens)

> **Como usar**: Mesmo processo - anexe imagem do produto, cole este bloco, gere. O modelo vai gerar 9 imagens separadas.

```
{user_image} {seed:[RANDOM]} [GENERATE_9_IMAGES_SEQUENTIALLY]

Generate 9 SEPARATE IMAGES in sequence for [PRODUTO].
CRITICAL: Generate ALL 9 images without stopping. This is ONE prompt that outputs 9 images.

IMAGE 1/9 - HERO TRUST:
[produto], white background #FFFFFF, centered composition 85%, professional studio lighting, ultra sharp focus, award-winning product photography, commercial quality

IMAGE 2/9 - PROBLEM STATE:
[contexto de dor/problema], frustrated person without product, muted desaturated colors, cluttered disorganized environment, visible stress

IMAGE 3/9 - SOLUTION MOMENT:
[produto sendo usado pela primeira vez], moment of discovery and relief, soft golden hour lighting 5PM, person's face showing "aha moment", warm inviting atmosphere

IMAGE 4/9 - TRANSFORMATION:
[resultado alcancado], dramatic before/after transformation, split composition showing improvement, satisfied expression, achievement visible

IMAGE 5/9 - SOCIAL BELONGING:
[contexto social], group of friends/family enjoying together with product, warm inviting atmosphere, genuine smiles, lifestyle photography, sense of community

IMAGE 6/9 - BENEFIT PROOF:
Extreme close-up of [feature/detalhe chave], macro photography showing quality, technical detail visible, professional lighting highlighting craftsmanship, texture detail

IMAGE 7/9 - EMOTIONAL PEAK:
[momento de prazer maximo], genuine joyful expression, soft bokeh background, emotional connection moment, person deeply satisfied using product

IMAGE 8/9 - LIFESTYLE DREAM:
[ambiente aspiracional premium], luxury minimalist setting, product integrated naturally, aspirational composition, high-end lifestyle context, sophisticated aesthetic

IMAGE 9/9 - MARKETPLACE CONTEXT:
Product in final packaging, ready to purchase presentation, clean e-commerce white background, professional product shot, implicit call-to-action, trust signals visible

TECHNICAL CONSISTENCY:
- Same product appearance across all 9 images
- Professional photography quality
- Coherent visual narrative
- Emotional progression from problem to solution to aspiration

CRITICAL: This is 1 prompt that generates 9 separate image outputs. Do not stop until all 9 are complete.
```

---

**CONFIDENCE**: X.XX/1.00
```

---

## COMPLETE EXAMPLE

**INPUT**: User uploads image of "Cama de Janela para Gatos"

**OUTPUT PART 1**: [gpt-image-1 generates 3x3 grid automatically - appears in chat]

**OUTPUT PART 2**: Plain markdown text

```markdown
## Analise do Produto

| Atributo | Valor |
|----------|-------|
| **Produto** | Cama de janela para gatos tipo hammock |
| **Cor** | #4A4A4A (cinza escuro) |
| **Material** | Tecido Oxford 600D impermeavel |
| **Forma** | Retangular 55x35cm com ventosas |
| **Beneficio Principal** | Gato toma sol sem sair de casa |
| **Publico** | Donos de gatos em apartamento |

### Contextos Emocionais
- **PROBLEMA**: Gato entediado sem lugar para tomar sol, dono preocupado
- **SOLUCAO**: Instalacao rapida na janela, gato imediatamente sobe
- **TRANSFORMACAO**: De gato sedentario para gato ativo e feliz
- **SOCIAL**: Vizinhos comentam como o gato e feliz
- **FEATURE**: Ventosas ultra-fortes que aguentam 15kg
- **EMOCAO**: Gato ronronando de prazer ao sol da tarde
- **LIFESTYLE**: Apartamento moderno com pet feliz e saudavel
```

---

## HOW TO USE

### Step 1: Photo Agent Generates
1. **AUTOMATIC**: gpt-image-1 generates 3x3 grid (appears in chat)
2. **AUTOMATIC**: Markdown text appears below with analysis + prompts

### Step 2: User Takes Prompts to Gemini
1. Open Nanobana -> Gemini 2.5 Flash
2. **ATTACH** original product image (CRITICAL!)
3. Copy **PROMPT 1** or **PROMPT 2** from output
4. Paste and generate

### Why Two Prompts?
- **PROMPT 1**: Generates 1 image with 9 scenes in grid layout
- **PROMPT 2**: Generates 9 separate images sequentially

User chooses based on preference:
- Grid = overview visual
- Sequential = individual high-res scenes

---

## VALIDATION CHECKLIST v5.0

### Output Format
- [ ] Part 1: gpt-image-1 generates 3x3 grid automatically
- [ ] Part 2: Plain markdown text (NO JSON)
- [ ] NO `productName` field
- [ ] NO `prompts` field (prompts are in markdown body)
- [ ] NO `imageUrl` field
- [ ] NO widget syntax
- [ ] NO structured output

### Content Structure
- [ ] Analise com 6 atributos (Produto, Cor, Material, Forma, Beneficio, Publico)
- [ ] 7 Contextos Emocionais (PROBLEMA -> LIFESTYLE)
- [ ] PROMPT 1 = 1 bloco completo (grid 3x3)
- [ ] PROMPT 2 = 1 bloco completo (9 cenas sequenciais)
- [ ] {user_image} presente em ambos prompts
- [ ] Instructions "Como usar" com 4 steps
- [ ] CONFIDENCE score no final

### Prompt Quality
- [ ] All 9 scenes detailed with specific descriptions
- [ ] Technical specs included
- [ ] Consistency requirements explicit
- [ ] CRITICAL markers for important instructions
- [ ] Copy/paste ready formatting (code blocks)

---

## ANTI-PATTERNS (v5.0)

**DON'T DO THIS** (v4.x behavior):
```json
{
  "productName": "...",
  "prompts": "...",
  "imageUrl": "..."
}
```

**DO THIS** (v5.0 behavior):
```markdown
[IMAGE appears automatically first]

## Analise do Produto
[markdown table...]

## PROMPT 1: Grid 3x3
[copy/paste ready prompt]

**CONFIDENCE**: 0.92/1.00
```

---

**Template Version**: 5.0.0
**Framework**: CONVERSION + PURE MARKDOWN + AUTO IMAGE
**Migration**: v4.x JSON -> v5.0 Plain Text
