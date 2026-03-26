# HOP: Main Agent | anuncio_agent v4.0.0

**Step**: 1 of 7
**Purpose**: Parse input and orchestrate workflow
**Input**: `{$INPUT}` (raw input)
**Output**: `{parsed_input}`

---

## 4 ROTAS DE WORKFLOW

| Rota | Modo | Descricao |
|------|------|-----------|
| 1 | PESQUISA Only | Research standalone |
| 2 | **ANUNCIO Only** | Copy standalone -> anuncio_completo.md |
| 3 | PHOTO Only | Fotos standalone |
| 4 | **FULL PIPELINE** | PESQUISA -> **ANUNCIO** -> PHOTO |

---

## TASK

Parse and validate the incoming input, extracting all relevant information for listing generation.

---

## INPUT SOURCES

### Source 1: pesquisa_agent Output (PIPELINE)
```yaml
kind: research_notes
format: markdown (22 blocks)
confidence: 0.95
fields_expected:
  - product_name
  - category
  - head_terms (10-15 termos)
  - longtails (30-50 termos)
  - pain_points
  - desired_gains
  - competitor_avg_rating
  - compliance_notes
  - unique_selling_points
```

### Source 2: Product URL
```yaml
kind: url
format: https://...
confidence: 0.80
scrape_fields:
  - title (as product_name)
  - price
  - category
  - features
  - description
```

### Source 3: Product Brief
```yaml
kind: brief
format: text
confidence: 0.65
extract_fields:
  - product_name (from context)
  - category (from context)
  - features (from description)
```

---

## EXECUTION

### Step 1.1: Identify Source Type
```
IF input contains "research_notes" OR "22 blocos" OR "from_pesquisa":
  source_type = "pesquisa_agent"
  confidence_base = 0.95
ELIF input starts with "http" OR "www":
  source_type = "product_url"
  confidence_base = 0.80
ELSE:
  source_type = "product_brief"
  confidence_base = 0.65
```

### Step 1.2: Extract Required Fields
```yaml
required:
  product_name:
    - Extract main product name
    - Remove brand if generic
    - Max 100 chars

  category:
    - Extract category path
    - Format: "Parent > Child > Subcategory"
    - Use marketplace taxonomy if available
```

### Step 1.3: Extract Optional Fields
```yaml
optional:
  target_audience:
    demographics: "age, gender, location"
    psychographics: "interests, lifestyle"
    pain_points: ["problema1", "problema2"]

  price_range:
    min: number
    max: number
    currency: "BRL"

  features:
    - name: "feature name"
      value: "specification"
      benefit: "customer benefit"

  head_terms:
    - "primary keyword"
    - "secondary keyword"
    - ... (max 20)

  longtails:
    - "longtail 1"
    - "longtail 2"
    - ... (max 50)

  pain_points:
    - "dor 1"
    - "dor 2"

  desired_gains:
    - "ganho 1"
    - "ganho 2"

  competitors:
    - name: "competitor name"
      price: number
      strengths: []
      weaknesses: []

  brand_voice:
    tone: "professional | friendly | luxurious"
    archetype: "brand archetype"

  compliance_notes:
    anvisa: "notes"
    inmetro: "notes"
```

### Step 1.4: Calculate Confidence
```python
# Confidence calculation with NEW weights
weights = {
    "product_name": 0.20,
    "category": 0.15,
    "head_terms": 0.20,
    "features": 0.15,
    "target_audience": 0.10,
    "competitors": 0.05,
    "price_range": 0.05,
    "pain_points": 0.05,
    "desired_gains": 0.05
}

confidence = sum(
    weights[field] * (1.0 if field_present else 0.0)
    for field in weights
)

# Apply source modifier
confidence *= confidence_base
```

### Step 1.5: Intelligent Fallback System
```yaml
confidence >= 0.80:
  action: "generate_full"
  markers: none
  message: "All data available. Generating complete listing."

confidence 0.60-0.79:
  action: "generate_with_suggestions"
  markers: "[VERIFICAR: motivo]"
  message: "Some data missing. Will generate with verification markers."

confidence 0.40-0.59:
  action: "generate_partial"
  markers: "[COMPLETAR: motivo]"
  message: "Limited data. Output will have completion placeholders."

confidence < 0.40:
  action: "request_enrichment"
  markers: N/A
  message: "Insufficient data. Please provide: {missing_fields}"
  stop_workflow: true
```

---

## OUTPUT FORMAT

```json
{
  "parsed_input": {
    "source_type": "pesquisa_agent | url | brief",
    "confidence": 0.85,
    "action": "generate_full | generate_with_suggestions | generate_partial | request_enrichment",

    "required": {
      "product_name": "Whey Protein Isolado 1kg Chocolate",
      "category": "Suplementos > Proteinas > Whey Protein"
    },

    "optional": {
      "target_audience": {
        "demographics": "Homens e mulheres, 18-45 anos, praticantes de musculacao",
        "psychographics": "Focados em resultados, disciplinados",
        "pain_points": ["dificuldade ganhar massa", "preco alto dos suplementos"]
      },
      "price_range": {
        "min": 149,
        "max": 199,
        "currency": "BRL"
      },
      "features": [
        {
          "name": "Proteina por dose",
          "value": "27g",
          "benefit": "Maximo ganho muscular"
        }
      ],
      "head_terms": ["whey protein", "proteina isolada", "suplemento"],
      "longtails": ["whey protein isolado chocolate", "suplemento hipertrofia"],
      "pain_points": ["dificuldade ganhar massa"],
      "desired_gains": ["ganho muscular rapido"],
      "competitors": [],
      "brand_voice": null,
      "compliance_notes": {
        "anvisa": "Produto isento de registro",
        "inmetro": "N/A"
      }
    },

    "missing_fields": [],
    "suggestions": [],
    "markers_to_add": []
  }
}
```

---

## PIPELINE INPUT MAPPING

When receiving from pesquisa_agent, map fields:

```yaml
from_pesquisa:
  product_name -> required.product_name
  category -> required.category
  head_terms -> optional.head_terms
  longtails -> optional.longtails
  pain_points -> optional.target_audience.pain_points
  desired_gains -> optional.desired_gains
  competitor_avg_rating -> optional.competitors.avg_rating
  compliance_notes -> optional.compliance_notes
  unique_selling_points -> features[].benefit
```

---

## VALIDATION

### Required Field Validation
```yaml
product_name:
  - NOT empty
  - min 3 chars
  - max 200 chars
  - NO prohibited terms

category:
  - NOT empty
  - min 3 chars
  - Valid format (contains " > ")
```

### Error Handling
```yaml
if product_name empty:
  error: "MISSING_PRODUCT_NAME"
  action: request_enrichment

if category empty:
  error: "MISSING_CATEGORY"
  action: request_enrichment
```

---

## EXAMPLE

### Input (pesquisa_agent - Rota 4)
```markdown
# Research Notes: Whey Protein Isolado 1kg

## Produto
- Nome: Whey Protein Isolado 1kg Sabor Chocolate
- Categoria: Suplementos > Proteinas > Whey Protein
- Preco: R$ 149-199

## Head Terms
whey protein, proteina isolada, suplemento hipertrofia, whey isolado

## Pain Points
- Dificuldade ganhar massa muscular
- Suplementos caros e ineficazes

## Desired Gains
- Ganho muscular rapido
- Recuperacao pos-treino

## Publico-alvo
Praticantes de musculacao, 18-45 anos, focados em ganho muscular
```

### Output
```json
{
  "parsed_input": {
    "source_type": "pesquisa_agent",
    "confidence": 0.92,
    "action": "generate_full",
    "required": {
      "product_name": "Whey Protein Isolado 1kg Sabor Chocolate",
      "category": "Suplementos > Proteinas > Whey Protein"
    },
    "optional": {
      "price_range": {"min": 149, "max": 199, "currency": "BRL"},
      "head_terms": ["whey protein", "proteina isolada", "suplemento hipertrofia", "whey isolado"],
      "pain_points": ["Dificuldade ganhar massa muscular", "Suplementos caros e ineficazes"],
      "desired_gains": ["Ganho muscular rapido", "Recuperacao pos-treino"],
      "target_audience": {
        "demographics": "18-45 anos, praticantes de musculacao",
        "psychographics": "focados em ganho muscular"
      }
    },
    "missing_fields": ["competitors", "brand_voice"],
    "suggestions": [],
    "markers_to_add": []
  }
}
```

---

**Next Step**: Pass `{parsed_input}` to `prompts/titulo_generator.md`
