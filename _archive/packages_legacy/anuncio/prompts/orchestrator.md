# ADW ORCHESTRATOR | anuncio_agent v5.0.0

**Type**: Agent Design Workflow (ADW)
**Version**: 5.0.0 | **Date**: 2025-12-18
**Output**: Widget Collapsible (copy-ready TXT)

---

## OUTPUT FORMAT (PRIORITY)

```
================================================================================
                         ANUNCIO COMPLETO - [PRODUTO]
================================================================================

[TITULOS] -----------------------------------------------------------------------
TITULO A: [58-60 chars]
TITULO B: [58-60 chars]
TITULO C: [58-60 chars]

[KEYWORDS] ----------------------------------------------------------------------
BLOCO 1: [115-120 termos]
BLOCO 2: [115-120 termos, zero duplicatas]

[BULLETS] -----------------------------------------------------------------------
1-10: [250-299 chars cada]

[DESCRICAO] ---------------------------------------------------------------------
[StoryBrand >= 3300 chars]

================================================================================
                              PRONTO PARA PUBLICAR
================================================================================
```

**REGRAS**: ZERO emojis | ZERO metadados | ZERO scores | Texto PURO

---

## WORKFLOW (7 Steps Internos)

```
INPUT -> [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] -> OUTPUT (Widget)
          |     |     |     |     |     |     |
        PARSE TITLES  KW  BULLETS DESC   QA  FORMAT
```

---

## STEP 1: PARSE INPUT

**HOP**: `prompts/main_agent.md`
**Input**: `{$INPUT}` (raw input)
**Output**: `{parsed_input}`

Actions:
1. Identify source (pesquisa_agent | url | brief)
2. Extract: product_name, category
3. Calculate confidence
4. Determine fallback action

Fallback:
```yaml
confidence >= 0.80: generate_full
confidence 0.60-0.79: generate_with_suggestions
confidence 0.40-0.59: generate_partial
confidence < 0.40: request_enrichment
```

---

## STEP 2: GENERATE TITLES

**HOP**: `prompts/titulo_generator.md`
**Input**: `{parsed_input}`
**Output**: `{titulos[3]}`

Rules:
- 58-60 chars EXACT
- ZERO conectores: e, com, de, para, ou, em, por, no, na, do, da
- 3 variantes (A, B, C)

---

## STEP 3: EXPAND KEYWORDS

**HOP**: `prompts/keywords_expander.md`
**Input**: `{parsed_input, titulos}`
**Output**: `{keywords[2]}`

Rules:
- 2 blocos
- 115-120 termos por bloco
- ZERO duplicatas entre blocos

---

## STEP 4: GENERATE BULLETS

**HOP**: `prompts/bullet_points.md`
**Input**: `{parsed_input, titulos, keywords}`
**Output**: `{bullets[10]}`

Rules:
- 10 bullets
- 250-299 chars EXACT
- Benefit-first
- Mental triggers (min 5)
- ZERO emojis

---

## STEP 5: BUILD DESCRIPTION

**HOP**: `prompts/descricao_builder.md`
**Input**: `{ALL outputs}`
**Output**: `{descricao}`

StoryBrand 7 Parts:
1. HERO: Cliente como heroi
2. PROBLEM: Problema que enfrenta
3. GUIDE: Produto como guia
4. PLAN: 3 passos simples
5. CTA: Chamada para acao
6. FAILURE: Consequencia de nao agir
7. SUCCESS: Transformacao positiva

Rules:
- >= 3300 chars
- Mobile-first formatting
- ZERO emojis

---

## STEP 6: QA VALIDATION (INTERNO)

**HOP**: `prompts/qa_validation.md`
**Input**: `{titulos, keywords, bullets, descricao}`
**Output**: `{corrections}`

Validation (NAO EXIBIR):
- Titulos 58-60 chars
- Zero conectores
- Keywords 115-120/bloco
- Zero duplicatas
- Bullets 250-299 chars
- Descricao >= 3300 chars

**IMPORTANTE**: Se falhar, CORRIGIR automaticamente.
NAO mostrar erros ou warnings ao usuario.

---

## STEP 7: FORMAT OUTPUT

**Template**: `output_template.md`
**Input**: `{ALL corrected outputs}`
**Output**: `Widget Collapsible`

Actions:
1. Montar Widget format
2. Verificar ZERO emojis
3. Verificar ZERO metadados
4. Output texto PURO copy-ready

---

## PIPELINE INTEGRATION

### From PESQUISA
```yaml
from_pesquisa:
  product_name, category, head_terms, longtails,
  pain_points, desired_gains, compliance_notes
```

### To PHOTO
```yaml
to_photo:
  product_name, key_benefits, target_audience,
  messaging_focus
```

---

## ERROR HANDLING

```yaml
validation_fail:
  action: auto_correct
  never: show_error_to_user

compliance_violation:
  action: block
  escalate: true
```

---

**Version**: 5.0.0 | Widget Collapsible | Copy-Ready
