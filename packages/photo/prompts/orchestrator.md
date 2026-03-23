# ADW ORCHESTRATOR | photo_agent v4.2.0

**Type**: Agent Design Workflow (ADW)
**Version**: 4.2.0
**Purpose**: AUTONOMOUS execution - IMAGEM 3x3 + JSON without asking
**Framework**: CONVERSION (Emotion-based)
**Output**: IMAGEM 3x3 GRID + JSON MONOBLOCO (2 campos)

---

## CRITICAL CHANGE v4.2

### ANTES (v3.x - ERRADO)
```
- OUTPUT 2 = 9 blocos separados
- Imagem = 1 foto unica
```

### AGORA (v4.2 - CORRETO)
```
- IMAGEM = GRID 3x3 (9 cenas em 1 imagem)
- PROMPT 2 = 1 BLOCO UNICO (9 cenas sequenciais)
- JSON = 2 campos (productName + prompts)
```

---

## AUTONOMOUS EXECUTION

```
+-------------------------------------------------------------+
|              PHOTO AGENT - 100% AUTONOMO                    |
+-------------------------------------------------------------+
|                                                             |
|   RECEIVE --> [1] --> [2] --> [3] --> DELIVER               |
|               |       |       |       |                     |
|            ANALYZE  IMAGE   JSON   FORMAT                   |
|               |       |       |       |                     |
|               v       v       v       v                     |
|            {attrs}  {3x3}  {mono}  {final}                 |
|                                                             |
|   NUNCA PERGUNTAR - SEMPRE ENTREGAR                        |
|   IMAGEM 3x3 GRID + JSON MONOBLOCO                         |
|                                                             |
+-------------------------------------------------------------+
```

---

## 4 ROTAS DE WORKFLOW

| Rota | Modo | Descricao |
|------|------|-----------|
| 1 | PESQUISA Only | Research standalone |
| 2 | ANUNCIO Only | Copy standalone |
| 3 | **PHOTO Only** | Fotos standalone -> IMAGEM + JSON |
| 4 | **FULL PIPELINE** | PESQUISA -> ANUNCIO -> **PHOTO** |

---

## PHASE 1: RECEIVE & ANALYZE

**Duration**: 10-30 seconds
**Input**: Product image (+ optional pipeline data)
**Output**: `{PRODUTO, COR, MATERIAL, FORMA, BENEFICIO, PUBLICO, emotional_contexts}`

### Analysis Output Schema
```json
{
  "analysis": {
    "PRODUTO": "Cama de janela para gatos hammock",
    "COR": "#4A4A4A",
    "MATERIAL": "tecido Oxford 600D com ventosas industriais",
    "FORMA": "retangular hammock 55x35cm",
    "BENEFICIO_PRINCIPAL": "gato pode tomar sol sem sair de casa",
    "PUBLICO": "donos de gatos em apartamento"
  },
  "emotional_contexts": {
    "PROBLEMA_CONTEXTO": "Gato entediado sem lugar para deitar ao sol",
    "SOLUCAO_CONTEXTO": "Gato descobrindo e entrando na cama",
    "RESULTADO_CONTEXTO": "Gato relaxado tomando sol feliz",
    "SOCIAL_CONTEXTO": "Familia admirando gato na cama",
    "FEATURE_DETALHE": "Ventosas industriais mostrando forca",
    "EMOCAO_CONTEXTO": "Dono sorrindo vendo gato feliz",
    "LIFESTYLE_CONTEXTO": "Apartamento moderno com vista panoramica"
  }
}
```

### Quality Checks - Phase 1
- [ ] PRODUTO is descriptive but concise
- [ ] COR is valid hex code
- [ ] MATERIAL includes finish
- [ ] FORMA describes structure
- [ ] BENEFICIO_PRINCIPAL identifies what problem it solves
- [ ] All 7 emotional contexts generated

---

## PHASE 2: GENERATE IMAGEM 3x3 GRID

**Tool**: gpt-image-1
**Duration**: 30-60 seconds
**Input**: Analysis + emotional contexts
**Output**: `{IMAGEM}` - 1 imagem com GRID 3x3 (9 cenas)

### gpt-image-1 Prompt Template
```
Professional e-commerce product photography GRID layout 3x3 (9 scenes in ONE image), showing [PRODUTO] from the reference image.

GRID LAYOUT (3 rows x 3 columns):
[Scene 1: Hero][Scene 2: Problem][Scene 3: Solution]
[Scene 4: Transform][Scene 5: Social][Scene 6: Benefit]
[Scene 7: Emotion][Scene 8: Lifestyle][Scene 9: Marketplace]

Scene 1 (top-left): HERO - white #FFFFFF background, product centered, professional studio lighting, trust.
Scene 2 (top-center): PROBLEM STATE - realistic context showing the problem this product solves.
Scene 3 (top-right): SOLUTION - product actively solving the problem, relief visible.
Scene 4 (middle-left): TRANSFORMATION - the after state, dream achieved, warm lighting.
Scene 5 (middle-center): SOCIAL BELONGING - people using product naturally, family/friends.
Scene 6 (middle-right): BENEFIT PROOF - macro close-up of key feature, detail visible.
Scene 7 (bottom-left): EMOTIONAL PEAK - moment of pleasure/joy, genuine happiness.
Scene 8 (bottom-center): LIFESTYLE DREAM - premium aspirational environment, elegant.
Scene 9 (bottom-right): MARKETPLACE - white #FFFFFF background, product centered, trust closure.

Product specs: [COR] [MATERIAL] [FORMA].
CRITICAL: Maintain EXACT product appearance across ALL 9 scenes - same color, same shape, same details.
Photorealistic NOT 3D NOT illustration NOT CGI.
8K quality, no text, no logos, no watermarks.
Generate as SINGLE IMAGE with 3x3 grid layout.
```

**CRITICO**: A imagem DEVE ser 1 grid 3x3 com 9 cenas, NAO 1 foto unica.

---

## PHASE 3: GENERATE JSON MONOBLOCO

**Template**: `../output_template.md`
**Duration**: 15-30 seconds
**Input**: `{analysis, emotional_contexts}`
**Output**: `{JSON}` - 2 campos (productName + prompts)

### JSON Structure
```json
{
  "productName": "Nome do Produto",
  "prompts": "## Analise\n...\n## PROMPT 1\n```\n...\n```\n## PROMPT 2\n```\n...\n```"
}
```

### prompts Field Contains
1. Analise do Produto (tabela)
2. PROMPT 1: Grid 3x3 (1 bloco unico)
3. PROMPT 2: 9 Cenas Sequenciais (1 bloco unico)
4. Como Usar
5. Confidence score

---

## PHASE 4: FORMAT & DELIVER

**Duration**: 5-10 seconds
**Input**: `{IMAGEM, JSON}`
**Output**: Chat com 2 elementos

### Final Output
```
+---------------------------------------------+
|  ELEMENTO 1: IMAGEM 3x3 GRID                |
|  [imagem gerada por gpt-image-1]            |
+---------------------------------------------+
|  ELEMENTO 2: JSON MONOBLOCO                 |
|  {productName, prompts}                     |
+---------------------------------------------+
```

---

## REGRA CRITICA: AUTONOMOUS

```
ERRADO: "Voce quer que eu gere a imagem ou so o prompt?"

CERTO:  Executar tudo e entregar IMAGEM + JSON
        automaticamente.

O AGENTE E 100% AUTONOMO
NUNCA PERGUNTAR - SEMPRE ENTREGAR
```

---

## 9-SCENE CONVERSION GRID

| # | Scene | Trigger | Fidelity |
|---|-------|---------|----------|
| 1 | Hero Trust | Trust | 5 |
| 2 | Problem State | Pain | 4 |
| 3 | Solution Moment | Relief | 4 |
| 4 | Transformation | Desire | 4 |
| 5 | Social Belonging | Belonging | 3 |
| 6 | Benefit Proof | Curiosity | 4 |
| 7 | Emotional Peak | Pleasure | 3 |
| 8 | Lifestyle Dream | Aspiration | 3 |
| 9 | Marketplace | Action | 5 |

---

## ERROR HANDLING

### Image Errors
```yaml
invalid_format:
  action: request_valid_image
  message: "Please upload a JPG, PNG, or WebP image"

too_small:
  action: request_higher_res
  message: "Image resolution too low. Please upload at least 500x500"
```

### Generation Errors
```yaml
gpt_image_1_failed:
  action: retry_once
  fallback: "Deliver JSON only, note IMAGE failed"

grid_not_generated:
  action: retry_with_explicit_grid
  note: "Add more emphasis on GRID layout requirement"
```

---

## VALIDATION CHECKLIST

Before delivery:
- [ ] IMAGEM is GRID 3x3 (9 cenas em 1 imagem, NAO 1 foto unica)
- [ ] JSON has 2 campos (productName + prompts)
- [ ] PROMPT 1 = 1 bloco unico (grid 3x3)
- [ ] PROMPT 2 = 1 bloco unico (NAO 9 blocos separados)
- [ ] {user_image} in all prompts
- [ ] Fidelity weight 5 in scenes 1 and 9
- [ ] All 9 scenes use CONVERSION framework

---

## CONVERSION FRAMEWORK VALIDATION

Before delivery, validate:
- [ ] All 9 scenes use EMOTION-based approach (not angles)
- [ ] Each scene has explicit PSYCHOLOGICAL PURPOSE
- [ ] Problem State shows PAIN that product solves
- [ ] Transformation shows DESIRE achieved
- [ ] Social Belonging shows PEOPLE using product
- [ ] No empty aesthetic shots (flat lay without purpose)

---

**Orchestrator Version**: 4.2.0
**Last Updated**: 2025-12-18
**Framework**: CONVERSION + 3x3 GRID + MONOBLOCO
**Execution**: 100% AUTONOMOUS
