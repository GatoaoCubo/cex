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
tldr: "BR runs with CPC and ACOS below the US; breakeven ACOS = margin, healthy target = margin minus 6 points."
when_to_use: "Set Amazon Ads goals in Brazil without importing American benchmarks"
keywords: [amazon_ads_br, acos_target, cpc_brasil, sponsored_products, tACOS]
long_tails:
  - "What ACOS target to use in Amazon Ads Brazil by margin"
  - "Why US Amazon Ads benchmarks break accounts in BR"
axioms:
  - "ALWAYS calculate ACOS target from operational margin"
  - "NEVER scale BR campaign using US average target"
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

## Key Concepts

- BR auction less dense than US reduces CPC
- Sponsored Products has best cost x ACOS ratio
- TACOS above 8% already requires review in BR
- Seasonal peaks require strong budget buffer

## Comparison

| Metric | Brazil | US | Reading |
|--------|--------|-----|---------|
| Sellers ads | 15-20% | 60-70% | BR less competitive |
| Average CPC | R$0.15-0.60 | $0.80-1.50 | BR 3-5x cheaper |
| Average ACOS | 12-18% | 25-35% | BR accepts hard target |

| Campanha | CPC | CTR | CVR | ACOS |
|----------|-----|-----|-----|------|
| Spons. Products | R$0.25-0.40 | 0.35-0.50% | 10-14% | 12-18% |
| Spons. Brands | R$0.40-0.70 | 0.20-0.35% | 7-10% | 15-22% |
| Spons. Display | R$0.15-0.30 | 0.12-0.20% | 4-7% | 20-30% |

| Margin | Target ACOS | Max TACOS | Strategy |
|--------|-------------|-----------|----------|
| > 40% | 20-25% | 12-15% | Aggressive |
| 30-40% | 15-20% | 10-12% | Balanced |
| 20-30% | 12-15% | 6-8% | Conservative |
| < 20% | 8-12% | 3-5% | Defensive |

| Period | CPC Inflation | Extra Budget |
|--------|--------------|--------------|
| Jan-Feb | -10 to -20% | Normal |
| Mar (Consumer Day) | +15 to +20% | +20% |
| May (Mothers Day) | +10 to +20% | +25% |
| Jul (Prime Day) | +25 to +35% | +40% |
| Nov (Black Friday) | +30 to +50% | +50-80% |
| Dec (Christmas) | +20 to +30% | +30% |

## Golden Rules

- ALWAYS use margin to define ACOS ceiling
- ALWAYS start bids in BR range, not dollarized
- NEVER use TACOS 15% as "healthy" in BR
- ALWAYS increase budget before seasonal peaks

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
