---
id: p01_kc_amazon_ads_benchmarks_brasil
type: knowledge_card
lp: P01
title: "Amazon Ads Brasil: Benchmarks Operacionais de 2026"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: PYTHA
domain: research
quality: null
tags: [amazon-ads, brasil, acos, cpc, roas, benchmarks]
tldr: "Brasil roda com CPC e ACOS muito abaixo dos EUA; breakeven ACOS = margem, e target saudavel fica margem menos 6 pontos."
when_to_use: "Definir metas de Amazon Ads no Brasil sem importar benchmarks americanos"
keywords: [amazon_ads_br, acos_target, cpc_brasil, sponsored_products, tACOS]
long_tails:
  - "Qual ACOS target usar em Amazon Ads Brasil por margem"
  - "Por que benchmark de Amazon Ads EUA quebra conta no Brasil"
axioms:
  - "SEMPRE calcular ACOS target a partir da margem operacional"
  - "NUNCA escalar campanha BR usando meta media dos EUA"
linked_artifacts:
  primary: null
  related: [p01_kc_catalogo_proprio_mercado_livre]
density_score: null
data_source: "Benchmark sintetizado para CPC, CTR, CVR, ACOS e sazonalidade de Amazon Ads no Brasil"
---

## Quick Reference

topic: paid media benchmark | scope: Amazon Ads Brasil | criticality: high
formula base: breakeven ACOS = margem % | target = margem % - 6 pp

## Conceitos Chave

- BR tem leilao menos denso que EUA, logo CPC cai
- Sponsored Products concentra melhor relacao volume x ACOS
- TACOS acima de 8% ja pede revisao em varias categorias BR
- Prime Day e Black Friday exigem buffer forte de budget

## Comparativo

| Metrica | Brasil | EUA | Leitura |
|--------|--------|-----|---------|
| Sellers anunciando | 15-20% | 60-70% | BR menos concorrido |
| CPC medio | R$0.15-0.60 | $0.80-1.50 | BR 3-5x mais barato |
| ACOS medio | 12-18% | 25-35% | BR aceita meta mais dura |

| Campanha | CPC | CTR | CVR | ACOS |
|---------|-----|-----|-----|------|
| Sponsored Products | R$0.25-0.40 | 0.35-0.50% | 10-14% | 12-18% |
| Sponsored Brands | R$0.40-0.70 | 0.20-0.35% | 7-10% | 15-22% |
| Sponsored Display | R$0.15-0.30 | 0.12-0.20% | 4-7% | 20-30% |

## Regras de Ouro

- SEMPRE usar margem para definir teto de ACOS
- SEMPRE iniciar bids BR em faixa local, nao dolarizada
- NUNCA chamar TACOS de 15% "saudavel" no BR por default
- SEMPRE ampliar budget antes dos picos sazonais

## Code

<!-- lang: python | purpose: derive healthy ACOS target from margin -->
```python
def acos_targets(margem_pct: float) -> dict:
    breakeven = margem_pct
    target = max(margem_pct - 6.0, 0.0)
    return {"breakeven_acos": breakeven, "target_acos": target}
```

## References

- external: https://advertising.amazon.com/solutions/products/sponsored-products
- external: https://advertising.amazon.com/library/guides/acos-advertising-cost-of-sales
- external: https://advertising.amazon.com/
- deepens: p01_kc_catalogo_proprio_mercado_livre
