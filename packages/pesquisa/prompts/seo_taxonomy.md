# HOP: SEO Taxonomy v3.0

## PURPOSE
Consolidate inbound (MP) + outbound (organic) + compliance

## INPUT
```yaml
head_terms[]: from query_generation.md
longtails[]: from query_generation.md
marketplace_data: from marketplace_search.md
competitor_data: from competitor analysis HOP
```

## EXECUTION

### 1. INBOUND (Marketplace)
```yaml
categories: primary > secondary > tertiary
attributes: filterable + searchable
keywords: title + description + backend
```

### 2. OUTBOUND (Organic)
```yaml
informational: "como escolher {q}", "qual melhor {q}"
commercial: "{q} review", "{q} vale a pena"
navigational: brand searches
```

### 3. SERP/SOCIAL
```
Google: "melhor {q} 2025", "{q} review"
YouTube: "{q} unboxing", "teste {q}"
TikTok: "{q} brasil"
Reclame Aqui: "site:reclameaqui.com.br {brand}"
```

### 4. COMPLIANCE (BR)
```yaml
ANVISA: food contact, cosmetics -> laudo, BPA-free
INMETRO: electronics, toys -> certificacao
CONAR: avoid superlatives sem prova
CDC: Art.49 (7 dias arrependimento)
LGPD: consent if collecting data
Decreto_7962: CNPJ + endereco + SAC visivel
```

## OUTPUT
```markdown
## 7) OUTBOUND (SERP/social)
- Google | YouTube | TikTok | RA

## 14) RECLAME AQUI
- URL | Reputacao | Nota
- Reclamacoes | % Resp | % Resolvidas
- Top 3 queixas

## 21) COMPLIANCE & RISCOS
### ANVISA | INMETRO | CONAR
### CDC | LGPD | Decreto 7.962
```

## VALIDATION
- [ ] RA checked main brands?
- [ ] ANVISA/INMETRO applicability?
- [ ] CONAR claims reviewed?
- [ ] Category paths identified?
- [ ] Content keywords for organic?

---
**v3.0** | Information-Dense | feeds Blocks 7, 14, 21
