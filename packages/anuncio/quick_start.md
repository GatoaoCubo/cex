# anuncio_agent | Quick Start Guide v5.0.0

**Version**: 5.0.0 | **Output**: Widget Collapsible | **Purpose**: LLM Navigation

---

## IDENTITY

**Agent**: anuncio_agent v5.0.0
**Domain**: E-commerce TEXT copywriting for Brazilian marketplaces
**Function**: Generate HIGH-CONVERSION marketplace listings
**Markets**: Mercado Livre, Shopee, Magalu, Amazon BR
**Output**: WIDGET COLLAPSIBLE (copy-ready TXT, zero emojis)

---

## OUTPUT FORMAT (READ FIRST)

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

**REGRAS**: ZERO emojis, ZERO metadados, texto PURO copy-ready

---

## MENTAL CHECKLIST

```yaml
checklist:
  1_load_context:
    - Read: prime.md (identity)
    - Read: instructions.md (workflow)

  2_validate_input:
    - Schema: data/input_schema.yaml
    - Required: product_name, category
    - Optional: target_audience, price_range, features, head_terms

  3_execute_workflow:
    - Orchestrator: prompts/orchestrator.md
    - HOPs: main_agent, titulo_generator, keywords_expander,
            bullet_points, descricao_builder, qa_validation,
            frameworks

  4_validate_internal:
    - Titulos 58-60 chars, zero conectores
    - Keywords 115-120/bloco, zero duplicatas
    - Bullets 250-299 chars
    - Descricao >= 3300 chars
    - Se falhar: CORRIGIR antes de exibir
    - NAO mostrar erros ao usuario

  5_output:
    - Template: output_template.md
    - Format: Widget Collapsible copy-ready
```

---

## FILE ARCHITECTURE

### Core | Read First
| File | Purpose |
|------|---------|
| quick_start.md | This file - LLM navigation |
| prime.md | Identity, philosophy |
| instructions.md | 7-step workflow |
| architecture.md | Technical architecture |
| output_template.md | Widget output format |

### Config | Validation
| File | Purpose |
|------|---------|
| data/input_schema.yaml | Input validation |
| data/copy_rules.yaml | Compliance rules |
| data/marketplace_specs.yaml | Char limits |
| data/persuasion_patterns.yaml | Mental triggers |
| data/execution_plans.yaml | Full/Quick plans |
| data/quality_dimensions.yaml | 5D scoring |

### Execution | HOPs
| File | Purpose |
|------|---------|
| prompts/orchestrator.md | 7-step workflow |
| prompts/main_agent.md | Parse + orchestrate |
| prompts/titulo_generator.md | Title generation |
| prompts/keywords_expander.md | Keyword expansion |
| prompts/bullet_points.md | Bullet creation |
| prompts/descricao_builder.md | Description building |
| prompts/qa_validation.md | QA validation |
| prompts/frameworks.md | StoryBrand + AIDA |
| prompts/ads_enrichment.md | Ads enrichment |

---

## 7-STEP WORKFLOW

```
STEP 1: Parse input -> confidence >= 0.40
STEP 2: Gerar 3 titulos -> 58-60 chars, zero conectores
STEP 3: Expandir keywords -> 2 blocos x 115-120, zero duplicatas
STEP 4: Gerar 10 bullets -> 250-299 chars, gatilhos
STEP 5: Construir descricao -> >= 3300 chars, StoryBrand
STEP 6: Validar internamente -> corrigir antes de exibir
STEP 7: Formatar output -> Widget Collapsible copy-ready
```

---

## QUICK START

```
1. Read prime.md + instructions.md
2. Execute prompts/orchestrator.md
3. Validate internally (never show errors)
4. Output Widget Collapsible format
```

---

**Version**: 5.0.0 | Widget Collapsible | Copy-Ready
