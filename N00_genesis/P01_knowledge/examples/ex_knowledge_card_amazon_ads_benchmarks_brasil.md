---
id: p01_kc_amazon_ads_benchmarks_brasil
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Amazon Ads Brasil: Benchmarks Operacionais de 2026"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: research
quality: 9.1
tags: [amazon-ads, brasil, acos, cpc, roas, benchmarks]
tldr: "BR roda com CPC e ACOS abaixo dos EUA; breakeven ACOS = margem, target saudavel = margem menos 6 pontos."
when_to_use: "Definir metas de Amazon Ads no Brasil sem importar benchmarks americanos"
keywords: [amazon_ads_br, acos_target, cpc_brasil, sponsored_products, tACOS]
long_tails:
  - "Qual ACOS target usar em Amazon Ads Brasil por margem"
  - "Por que benchmark de Amazon Ads EUA quebra conta no BR"
axioms:
  - "SEMPRE calcular ACOS target a partir da margem operacional"
  - "NUNCA escalar campanha BR usando meta media dos EUA"
linked_artifacts:
  primary: null
  related: [p01_kc_catalogo_proprio_mercado_livre]
density_score: 1.0
data_source: "Benchmark de CPC, CTR, CVR, ACOS e sazonalidade Amazon Ads BR"
related:
  - p02_agent_amazon_ads
  - p02_agent_ml_ads
  - p01_kc_llm_benchmark_ecommerce_copy
---

## Quick Reference

topic: paid media benchmark | scope: Amazon Ads Brasil | criticality: high
formula: breakeven ACOS = margem % | target = margem % - 6 pp

## Conceitos Chave

- Leilao BR menos denso que EUA reduz CPC
- Sponsored Products tem melhor custo x ACOS
- TACOS acima de 8% ja pede revisao no BR
- Picos sazonais exigem buffer forte de budget

## Comparativo

| Metrica | Brasil | EUA | Leitura |
|---------|--------|-----|---------|
| Sellers ads | 15-20% | 60-70% | BR menos concorrido |
| CPC medio | R$0.15-0.60 | $0.80-1.50 | BR 3-5x mais barato |
| ACOS medio | 12-18% | 25-35% | BR aceita meta dura |

| Campanha | CPC | CTR | CVR | ACOS |
|----------|-----|-----|-----|------|
| Spons. Products | R$0.25-0.40 | 0.35-0.50% | 10-14% | 12-18% |
| Spons. Brands | R$0.40-0.70 | 0.20-0.35% | 7-10% | 15-22% |
| Spons. Display | R$0.15-0.30 | 0.12-0.20% | 4-7% | 20-30% |

| Margem | ACOS alvo | TACOS max | Estrategia |
|--------|-----------|-----------|------------|
| > 40% | 20-25% | 12-15% | Agressivo |
| 30-40% | 15-20% | 10-12% | Equilibrado |
| 20-30% | 12-15% | 6-8% | Conservador |
| < 20% | 8-12% | 3-5% | Defensivo |

| Periodo | Inflacao CPC | Budget extra |
|---------|-------------|-------------|
| Jan-Fev | -10 a -20% | Normal |
| Mar (Consumidor) | +15 a +20% | +20% |
| Mai (Maes) | +10 a +20% | +25% |
| Jul (Prime Day) | +25 a +35% | +40% |
| Nov (Black Friday) | +30 a +50% | +50-80% |
| Dez (Natal) | +20 a +30% | +30% |

## Regras de Ouro

- SEMPRE usar margem para definir teto de ACOS
- SEMPRE iniciar bids em faixa BR, nao dolarizada
- NUNCA usar TACOS 15% como "saudavel" no BR
- SEMPRE ampliar budget antes dos picos sazonais

## Code

<!-- lang: python | purpose: derive ACOS targets from margin -->
```python
def acos_targets(margem_pct: float) -> dict:
    breakeven = margem_pct
    target = max(margem_pct - 6.0, 0.0)
    return {"breakeven_acos": breakeven, "target_acos": target}
```

## References

- external: https://advertising.amazon.com/solutions/products/sponsored-products
- external: https://advertising.amazon.com/library/guides/acos
- external: https://advertising.amazon.com/
- deepens: p01_kc_catalogo_proprio_mercado_livre


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_amazon_ads]] | downstream | 0.36 |
| [[p02_agent_ml_ads]] | downstream | 0.23 |
| [[p01_kc_llm_benchmark_ecommerce_copy]] | sibling | 0.17 |
