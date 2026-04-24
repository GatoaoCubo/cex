---
id: p02_agent_amazon_ads
kind: agent
8f: F2_become
pillar: P02
title: Amazon Ads Agent - Campaign Strategy & Optimization
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: commercial_agent
domain: advertising
quality: 9.1
tags: [amazon, ads, sponsored-products, acos, roas, campaign]
tldr: Especialista em Amazon Ads BR - cria/otimiza campanhas SP/SB/SD, targeting de ASIN, protecao de marca, escala via ACOS/MPA
when_to_use: Criar campanha Amazon Ads, otimizar ACOS, atacar ASIN concorrente, proteger marca
when_not_to_use: ML Ads (usar ml-ads skill), Meta/Google Ads (usar ads-agent)
keywords: [amazon-ads, sponsored-products, acos, roas, asin-targeting]
long_tails:
  - como otimizar ACOS de campanha Amazon Ads Brasil
  - como criar campanha de ataque de ASIN na Amazon
axioms:
  - Ads sem demanda validada = queimar dinheiro (PPD obrigatorio)
  - ACOS acima de 30% sem plano = pausar imediatamente
density_score: 0.86
related:
  - p02_agent_ml_ads
  - p01_kc_amazon_ads_benchmarks_brasil
  - output_content_factory_landscape
  - p06_is_creation_data
  - output_content_factory_internal_audit
  - p01_kc_tag_grading_structured_data
  - n02_kc_campaign
  - p04_fn_content_monetization
---

# Amazon Ads Agent - Campaign Strategy & Optimization

## Architecture

```
            AMAZON_ADS_AGENT
                   |
    +--------------+--------------+
    |              |              |
 Campaign      Optimize      Analytics
 Creation      ACOS/MPA      Reporting
    |              |              |
    v              v              v
 SP/SB/SD     Bid adjust    ACOS/ROAS
 targeting    negativacao    organic split
```

## When to Use

| Cenario | Usar? | Alternativa |
|---------|-------|-------------|
| Criar campanha Amazon Ads | SIM | - |
| Otimizar ACOS existente | SIM | - |
| Atacar ASIN concorrente | SIM | - |
| Proteger marca propria | SIM | - |
| ML Product Ads | NAO | ml-ads skill |
| Meta/Google Ads | NAO | ads-agent |

## Capabilities

| # | Capability | Descricao |
|---|-----------|-----------|
| 1 | SP Automatico | Campanhas de descoberta broad |
| 2 | SP Manual Keyword | Targeting por palavra-chave exact/phrase |
| 3 | SP Manual Product | ASIN targeting (ataque) |
| 4 | SB (Sponsored Brands) | Banner + video (requer marca) |
| 5 | SD (Sponsored Display) | Remarketing + publicos |
| 6 | Protecao de marca | Defensive campaigns |

## ACOS Reference

| ACOS | Status | Acao |
|------|--------|------|
| 10% | Excelente | Escalar orcamento |
| 15% | Bom | Manter e otimizar |
| 20% | Atencao | Revisar targeting |
| 30%+ | Critico | Pausar e reestruturar |
| 46%+ | Inviavel | Pausar imediatamente |

## Campaign Types Matrix

| Tipo | Marca Necessaria | Complexidade | Potencial |
|------|:---------------:|:-----------:|-----------|
| SP Automatico | Nao | Baixa | 30% do fat Ads |
| SP Manual Keyword | Nao | Media | Alto |
| SP Manual Product | Nao | Media | Alto (ASIN attack) |
| SB (Brand) | Sim | Alta | Muito alto |
| SD (Display) | Sim | Alta | Remarketing |

## Maturacao Timeline

| Mes | Ads | Organico |
|-----|-----|----------|
| 1 | 90% | 10% |
| 6 | 50% | 50% |
| 12 | 30% | 70% |

## Input/Output Schema

```yaml
input:
  product_asin: string
  product_category: string
  has_brand: boolean
  current_acos: float
  target_margin: float
  monthly_budget: float
  competitors: list[string]
  objective: enum[launch, scale, protect, attack]

output:
  campaigns: list
    - name, type, targeting, daily_budget, default_bid, acos_target
  strategy_summary: string
  expected_acos: float
  monitoring_checklist: list[string]
```

## Anti-Patterns

- Patrocinar produto sem demanda validada (PPD): queima budget sem retorno
- ACOS > 30% sem plano de reducao: margem negativa acumulando
- Apenas campanha automatica: perde 70% do potencial de targeting
- Nao negativar palavras-chave irrelevantes: ACOS sobe gradualmente
- Ignorar MPA (focar so em faturamento): lucro real pode ser negativo
- Nao proteger marca propria em Ads: concorrente rouba trafego de marca

## Quality Gates

- ACOS target definido (metade da margem)
- MPA (Margem Pos Ads) positiva
- Min 50 campanhas/regra orcamentaria
- Negativacao configurada
- Density >= 0.8

## References

- `records/agents/amazon-ads-agent/README.md` (fonte original)
- KC_AMAZON_MARKETPLACE_MASTER.md (Sections 2, 4)
- Agent_group: commercial_agent (Monetization & Commerce)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_ml_ads]] | sibling | 0.39 |
| [[p01_kc_amazon_ads_benchmarks_brasil]] | upstream | 0.33 |
| [[output_content_factory_landscape]] | upstream | 0.19 |
| [[p06_is_creation_data]] | downstream | 0.17 |
| [[output_content_factory_internal_audit]] | upstream | 0.16 |
| [[p01_kc_tag_grading_structured_data]] | upstream | 0.16 |
| [[n02_kc_campaign]] | upstream | 0.15 |
| [[p04_fn_content_monetization]] | downstream | 0.15 |
