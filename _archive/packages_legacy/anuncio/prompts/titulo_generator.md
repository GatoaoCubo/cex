# HOP: Titulo Generator | anuncio_agent v4.0.0

**Step**: 2 of 7
**Purpose**: Generate 3 optimized titles for marketplace listing
**Input**: `{parsed_input}` from Step 1
**Output**: `{titulos[3]}`

---

## WORKFLOW ROUTES (Confidence-Based Behavior)

| Route | Confidence | Behavior |
|-------|------------|----------|
| Full Generation | >=0.80 | Generate without markers |
| With Suggestions | 0.60-0.79 | Add [VERIFICAR] markers |
| Partial | 0.40-0.59 | Add [COMPLETAR] markers |
| Request Enrichment | <0.40 | Stop and request more info |

---

## TASK

Generate 3 title variants (A, B, C) optimized for Brazilian marketplaces with:
- 58-60 characters EXACT
- ZERO connectors (e, com, de, para, etc.)
- Keywords at the start
- Different value propositions per variant

---

## RULES (CRITICAL)

### Character Limits
```yaml
minimum: 58
maximum: 60
tolerance: 0
action_if_wrong: auto_adjust
```

### Prohibited Connectors (ZERO TOLERANCE)
```yaml
prohibited:
  - "e"      # and
  - "com"    # with
  - "de"     # of
  - "para"   # for
  - "ou"     # or
  - "em"     # in
  - "por"    # by
  - "no"     # in the
  - "na"     # in the (feminine)
  - "do"     # of the
  - "da"     # of the (feminine)
  - "dos"    # of the (plural)
  - "das"    # of the (plural feminine)
  - "ao"     # to the

alternative_strategies:
  - Use hyphen: "Whey Protein - Chocolate"
  - Use plus: "Whey + BCAA"
  - Juxtaposition: "Whey Protein Isolado 1kg Chocolate"
  - Specification: "Whey Protein 1kg 27g Proteina"
```

### Structure
```yaml
format: "[KEYWORD PRINCIPAL] [ESPECIFICACAO] [DIFERENCIAL]"
keyword_position: first
quantity_placement: after_product_name
differentiator: required
```

### Prohibited Patterns
```yaml
never_use:
  - "PROMOCAO"
  - "OFERTA"
  - "DESCONTO"
  - "GRATIS"
  - "FRETE GRATIS"
  - "MELHOR PRECO"
  - "MAIS BARATO"
  - ALL_CAPS (except acronyms)
  - Excessive punctuation (!!!, ???)
  - Emojis
```

---

## EXECUTION

### Step 2.1: Extract Seed Keywords
```python
# From parsed_input
seeds = []

# Priority 1: head_terms
if parsed_input.head_terms:
    seeds.extend(parsed_input.head_terms[:5])

# Priority 2: product_name tokens
product_tokens = parsed_input.product_name.split()
seeds.extend([t for t in product_tokens if len(t) > 3])

# Priority 3: category last level
category_parts = parsed_input.category.split(" > ")
seeds.append(category_parts[-1])
```

### Step 2.2: Generate Title Variants
```yaml
Variant A (Primary):
  focus: "Main keyword + core specification"
  structure: "[Keyword] [Product] [Size] [Flavor/Type]"
  example: "Whey Protein Isolado 1kg Chocolate Premium"

Variant B (Benefit Focus):
  focus: "Keyword + main benefit"
  structure: "[Keyword] [Product] [Benefit Attribute]"
  example: "Whey Protein Isolado 27g Proteina Alta Pureza"

Variant C (Differentiator):
  focus: "Keyword + unique selling point"
  structure: "[Keyword] [Product] [Differentiator]"
  example: "Whey Protein Isolado Importado Zero Lactose"
```

### Step 2.3: Validate Each Title
```python
def validate_title(title):
    errors = []

    # Check length
    char_count = len(title)
    if char_count < 58:
        errors.append(f"TOO_SHORT: {char_count} chars (min 58)")
    if char_count > 60:
        errors.append(f"TOO_LONG: {char_count} chars (max 60)")

    # Check connectors
    prohibited = ["e", "com", "de", "para", "ou", "em", "por", "no", "na", "do", "da"]
    words = title.lower().split()
    for word in words:
        if word in prohibited:
            errors.append(f"CONNECTOR_FOUND: '{word}'")

    # Check prohibited patterns
    if any(p in title.upper() for p in ["PROMOCAO", "OFERTA", "DESCONTO"]):
        errors.append("PROHIBITED_TERM")

    return len(errors) == 0, errors
```

### Step 2.4: Auto-Fix If Needed
```yaml
if too_short:
  actions:
    - Add specification (tamanho, sabor, cor)
    - Add quality adjective (Premium, Profissional)
    - Expand abbreviation

if too_long:
  actions:
    - Remove adjectives
    - Use abbreviation (kg, g, ml)
    - Remove redundant words

if connector_found:
  actions:
    - Replace with hyphen
    - Juxtapose words
    - Remove connector, adjust structure
```

---

## OUTPUT FORMAT

```json
{
  "titulos": [
    {
      "variant": "A",
      "text": "Whey Protein Isolado 1kg Chocolate Suico Premium",
      "chars": 59,
      "keywords_used": ["whey protein", "isolado", "chocolate"],
      "validation": {
        "char_count": "PASS",
        "no_connectors": "PASS",
        "keyword_first": "PASS"
      }
    },
    {
      "variant": "B",
      "text": "Whey Protein Isolado 27g Proteina Alta Pureza 1kg",
      "chars": 60,
      "keywords_used": ["whey protein", "isolado", "proteina"],
      "validation": {
        "char_count": "PASS",
        "no_connectors": "PASS",
        "keyword_first": "PASS"
      }
    },
    {
      "variant": "C",
      "text": "Whey Protein Isolado Importado Zero Lactose 1kg",
      "chars": 58,
      "keywords_used": ["whey protein", "isolado", "importado"],
      "validation": {
        "char_count": "PASS",
        "no_connectors": "PASS",
        "keyword_first": "PASS"
      }
    }
  ],
  "metadata": {
    "all_valid": true,
    "fixes_applied": 0,
    "keywords_coverage": 0.85
  }
}
```

---

## EXAMPLES

### Good Titles (CORRECT)
```
Whey Protein Isolado 1kg Chocolate Premium Importado (58)
Suplemento Whey Protein 27g Proteina Zero Lactose 1kg (58)
Proteina Whey Isolada 1kg Sabor Chocolate Suico Pro (57)
```

### Bad Titles (INCORRECT)
```
WRONG: Whey Protein Isolado de Chocolate com 1kg e Premium
       (connectors: de, com, e)

WRONG: Whey Protein PROMOCAO Desconto Imperdivel Compre Agora
       (prohibited terms)

WRONG: Whey Protein Isolado
       (too short: 22 chars)

WRONG: Suplemento Whey Protein Isolado Importado Premium Alta Qualidade Sabor Chocolate Suico 1kg
       (too long: 95 chars)
```

---

## VALIDATION CHECKLIST

Before outputting:
- [ ] All 3 titles between 58-60 chars
- [ ] ZERO connectors in any title
- [ ] Keywords appear in first 3 words
- [ ] Each title has different value proposition
- [ ] No prohibited terms
- [ ] No ALL_CAPS except acronyms
- [ ] No emojis or special characters

---

## INTELLIGENT FALLBACK

If input confidence < 0.40, this HOP requests enrichment from pesquisa agent or asks USER for clarification.

Fallback logic is implemented directly in validators, not as a separate module.

---

**Next Step**: Pass `{titulos}` to `prompts/keywords_expander.md`
