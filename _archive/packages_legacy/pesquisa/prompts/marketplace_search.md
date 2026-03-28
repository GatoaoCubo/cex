# HOP: Marketplace Search v3.0

## PURPOSE
Execute searches across 9 BR marketplaces, extract structured data

## INPUT
```yaml
head_terms[]: from query_generation.md
longtails[]: from query_generation.md
marketplaces[]: default all 9
```

## 9 MARKETPLACES

| # | Platform | Pattern | Priority |
|---|----------|---------|----------|
| 1 | ML | `site:mercadolivre.com.br {q}` | P1 |
| 2 | Shopee | `site:shopee.com.br {q}` | P1 |
| 3 | Magalu | `site:magazineluiza.com.br {q}` | P2 |
| 4 | Amazon | `site:amazon.com.br {q}` | P2 |
| 5 | Americanas | `site:americanas.com.br {q}` | P3 |
| 6 | Casas Bahia | `site:casasbahia.com.br {q}` | P3 |
| 7 | Submarino | `site:submarino.com.br {q}` | P3 |
| 8 | TikTok | `tiktok shop brasil {q}` | P4 |
| 9 | Shein | `site:br.shein.com {q}` | P4 |

## EXECUTION

### Strategy
- Top 5 head -> P1+P2 (4 MP)
- All head -> at least P1 (2 MP)
- Log EVERY query + URL

### Extract per result
```yaml
title | price: "R$ XX,XX" | original_price
rating: "X.X/5.0" | reviews: N
seller | seller_rep | badges[]
shipping: "Frete gratis" | "R$ XX"
url | marketplace
```

## OUTPUT
```markdown
## 6) INBOUND
| MP | Query | URL | Preco | Rating | Reviews | Seller |
|----|-------|-----|-------|--------|---------|--------|

### Padroes
- Preco medio: R$ XX
- Rating medio: X.X/5.0
- Frete gratis: XX%
```

## VALIDATION
- [ ] >=3 MP searched?
- [ ] >=15 queries logged + URLs?
- [ ] Prices BRL (R$ XX,XX)?
- [ ] Ratings X.X/5.0?

---
**v3.0** | Information-Dense | feeds Block 6
