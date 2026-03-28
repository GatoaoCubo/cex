# HOP: Keywords Expander | anuncio_agent v4.0.0

**Step**: 3 of 7
**Purpose**: Expand keywords into 2 optimized blocks
**Input**: `{parsed_input, titulos}` from Steps 1+2
**Output**: `{keywords[2]}`

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

Expand seed keywords into 2 comprehensive blocks with:
- 115-120 terms per block
- No duplicates between blocks
- Semantic variations included
- Natural language integration ready

---

## RULES

### Block Structure
```yaml
block_1:
  name: "Backend/Categorias"
  purpose: "Indexacao em busca"
  terms: 115-120
  focus: "Primary keywords, category terms, product attributes"

block_2:
  name: "Tags/Atributos"
  purpose: "Variacao semantica"
  terms: 115-120
  focus: "Long-tail, synonyms, use cases, benefits"

total_unique_terms: 230-240
no_duplicates_between_blocks: true
```

### Expansion Strategies
```yaml
strategies:
  singular_plural:
    - "whey protein" -> "whey proteins"
    - "suplemento" -> "suplementos"

  with_without_accent:
    - "proteina" -> "proteina"
    - "musculo" -> "musculo"

  synonyms:
    - "proteina" -> "proteina, po proteico, shake"
    - "suplemento" -> "complemento alimentar"

  common_misspellings:
    - "whey" -> "wey, way, wei"
    - "protein" -> "proteinn, proteen"

  long_tail:
    - "whey protein" -> "whey protein para ganhar massa"
    - "suplemento" -> "suplemento pos treino"

  use_cases:
    - "treino", "musculacao", "academia"
    - "hipertrofia", "definicao", "ganho massa"

  benefits:
    - "energia", "recuperacao", "performance"
    - "sabor", "solubilidade", "digestao"
```

### Prohibited Terms
```yaml
never_include:
  - Competitor brand names
  - "melhor que [competitor]"
  - "original" (implies others are fake)
  - "genuino", "legitimo" (same reason)
  - Misleading claims
```

---

## EXECUTION

### Step 3.1: Collect Seed Keywords
```python
seeds = []

# From parsed_input
if parsed_input.head_terms:
    seeds.extend(parsed_input.head_terms)

# From product_name
product_words = parsed_input.product_name.lower().split()
seeds.extend([w for w in product_words if len(w) > 2])

# From category
category_parts = parsed_input.category.split(" > ")
seeds.extend([p.lower() for p in category_parts])

# From titulos (Step 2)
for titulo in titulos:
    title_words = titulo.text.lower().split()
    seeds.extend([w for w in title_words if len(w) > 3])

# Deduplicate
seeds = list(set(seeds))
```

### Step 3.2: Expand Block 1 (Backend/Categorias)
```yaml
focus: Core keywords + attributes
expansion_types:
  - Primary keywords (as-is)
  - Singular/plural variations
  - Category hierarchy terms
  - Product attributes (size, color, flavor)
  - Technical specifications
  - Brand modifiers (premium, profissional)

target_count: 115-120 terms
```

### Step 3.3: Expand Block 2 (Tags/Atributos)
```yaml
focus: Semantic variations + long-tail
expansion_types:
  - Synonyms
  - Misspellings
  - Long-tail queries
  - Use case keywords
  - Benefit keywords
  - Question keywords ("como usar", "para que serve")
  - Comparison keywords ("melhor whey 2025")

target_count: 115-120 terms
exclude: All terms already in Block 1
```

### Step 3.4: Validate and Balance
```python
def validate_keywords(block1, block2):
    # Check counts
    assert 115 <= len(block1) <= 120, "Block 1 count out of range"
    assert 115 <= len(block2) <= 120, "Block 2 count out of range"

    # Check no duplicates
    overlap = set(block1) & set(block2)
    assert len(overlap) == 0, f"Duplicates found: {overlap}"

    # Check no prohibited
    prohibited = ["melhor que", "original", "genuino", "legitimo"]
    for term in block1 + block2:
        for p in prohibited:
            assert p not in term.lower(), f"Prohibited term: {term}"

    return True
```

---

## OUTPUT FORMAT

```json
{
  "keywords": [
    {
      "block": 1,
      "name": "Backend/Categorias",
      "terms": [
        "whey protein",
        "proteina isolada",
        "suplemento alimentar",
        "whey isolado",
        "proteina whey",
        "..."
      ],
      "count": 118
    },
    {
      "block": 2,
      "name": "Tags/Atributos",
      "terms": [
        "whey protein para ganhar massa",
        "suplemento pos treino",
        "proteina para hipertrofia",
        "..."
      ],
      "count": 117
    }
  ],
  "metadata": {
    "total_unique": 235,
    "seeds_used": 15,
    "expansion_rate": 15.7,
    "duplicates_removed": 12
  }
}
```

---

## EXPANSION EXAMPLES

### Seed: "whey protein"

**Block 1 Expansions:**
```
whey protein, proteina whey, whey, protein, proteina,
whey isolado, whey concentrado, whey hidrolisado,
whey protein isolado, whey protein concentrado,
proteina isolada, proteina concentrada,
suplemento whey, po de whey, shake whey,
whey 1kg, whey 900g, whey 2kg,
whey chocolate, whey baunilha, whey morango
```

**Block 2 Expansions:**
```
whey protein para ganhar massa muscular,
melhor whey protein 2025,
whey protein importado eua,
como tomar whey protein corretamente,
whey protein pos treino,
whey protein antes de dormir,
whey protein para emagrecer,
whey protein para mulheres,
qual melhor whey protein,
whey protein sem lactose,
wey protein, way protein (misspellings)
```

---

## OUTPUT AS TEXT (for copy)

### Block 1 Format
```
whey protein, proteina isolada, suplemento alimentar, whey isolado, proteina whey, suplemento proteico, po proteico, shake proteina, whey 1kg, proteina 1 quilo, [continue for 115-120 terms]
```

### Block 2 Format
```
whey protein para ganhar massa, suplemento pos treino, proteina para hipertrofia, whey protein academia, melhor whey 2025, [continue for 115-120 terms]
```

---

## VALIDATION CHECKLIST

Before outputting:
- [ ] Block 1 has 115-120 terms
- [ ] Block 2 has 115-120 terms
- [ ] Zero duplicates between blocks
- [ ] No prohibited terms
- [ ] Seeds are represented in both blocks
- [ ] Variations included (plural, accents, synonyms)
- [ ] Long-tail keywords in Block 2

---

**Next Step**: Pass `{keywords}` to `prompts/bullet_points.md`
