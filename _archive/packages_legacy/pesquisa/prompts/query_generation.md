# HOP: Query Generation v3.0

## PURPOSE
Generate query bank: 15 head + 50 longtail + synonyms + regional BR

## INPUT
```yaml
product_name: required
category: required
known_attributes: optional[]
```

## OUTPUT
```yaml
head_terms[15]: primary high-intent keywords
longtails[30-50]: specific combinations
synonyms{}: term -> alternatives mapping
regional_variations[]: BR-specific terms
```

## EXECUTION

### 1. HEAD TERMS (15)
- Extract nouns from product_name
- Remove connectors: de, da, do, para, com, e
- Add category variants
- Lowercase, no special chars

### 2. LONGTAILS (30-50)
Patterns:
```
{HEAD} {MATERIAL}: inox, plastico, vidro
{HEAD} {SIZE}: 500ml, 1 litro, grande
{HEAD} {CONTEXT}: academia, escritorio, viagem
{HEAD} {BENEFIT}: isolamento, duravel, leve
{HEAD} {ATTRIBUTE}: from known_attributes[]
```

### 3. SYNONYMS
Map each head -> 2-4 alternatives
```
garrafa termica -> [squeeze termico, tumbler, copo termico]
aco inox -> [inoxidavel, inox 304, stainless]
```

### 4. REGIONAL BR
- Diminutivos: garrafinha, squezinho
- Aumentativos: garrafao
- Regionais: cuia termica (sul), termo

## FORMAT
```markdown
## 4) HEAD TERMS (15)
1. termo1
2. termo2
...

## 5) LONGTAILS (30-50)
- "longtail 1"
- "longtail 2"
...

### SINONIMOS
| Termo | Alternativas |
|-------|--------------|

### VARIACOES REGIONAIS
termo1, termo2, termo3
```

## VALIDATION
- [ ] 15 head terms?
- [ ] 30-50 longtails?
- [ ] 2+ synonyms per head?
- [ ] Regional variations included?
- [ ] All PT-BR lowercase?

---
**v3.0** | Information-Dense | feeds Block 4-5
