---
id: p02_agent_ml_ads
name: organization-ml-ads
description: Mercado Livre Product Ads strategy, ROAS optimization, and campaign management
version: 1.0.0
pillar: P02
kind: agent
8f: F2_become
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
domain: marketing
quality: 9.1
tags: [mercado-livre, ads, roas, campaign, marketplace]
tldr: Skill de Product Ads ML com calculadora de preco, classificacao de funil, estrutura de campanhas e otimizacao semanal
user_invocable: true
trigger: /ml-ads
when_to_use: Planejar campanha ML Ads, calcular ROAS target, otimizar performance semanal, simular cenarios
when_not_to_use: Meta/Google Ads (usar ads-agent), pesquisa de mercado (usar pesquisa-agent)
phases:
  - Pricing Calculator
  - Campaign Structure
  - Weekly Optimizer
examples:
  - /ml-ads planejar "fone bluetooth TWS" --custo 35 --preco 89.90
  - /ml-ads roas --margem 40 --comissao 16
  - /ml-ads otimizar --periodo 7d
density_score: 0.91
linked_artifacts:
  agent: records/agents/ml-ads/README.md
  kc: records/pool/knowledge/KC_knowledge_agent_069_CAT_LOGO_PR_PRIO_MERCADO_LIVRE.md
related:
  - p02_agent_amazon_ads
  - p01_kc_brand_monetization_models
  - p01_kc_amazon_ads_benchmarks_brasil
  - bld_schema_optimizer
  - p02_agent_pesquisa
  - p06_is_creation_data
  - p06_is_quality_audit
  - n02_kc_campaign
  - p02_agent_web_researcher
---

# ML Ads Skill

## Purpose

ML Ads e o **estrategista de Product Ads do Mercado Livre** do organization. Responsavel por precificacao para ads, classificacao de funil, estruturacao de campanhas, calculo de ROAS/ACOS/TACOS, otimizacao semanal e simulacao de cenarios. Domain: Marketing (marketing_agent agent_group).

## Workflow Phases

### Phase 1: Pricing Calculator
**Input**: `custo_unitario`, `preco_venda`, `comissao_ml`, `frete_medio`
**Action**: Calcular preco minimo viavel com ads, margem liquida, breakeven ROAS
**Output**: `preco_minimo_ads`, `margem_liquida`, `breakeven_roas`

### Phase 2: Campaign Structure
**Input**: `funil_stage`, `historico_vendas`, `margem_target`
**Action**: Classificar produto no funil, montar estrutura de campanhas base + otimizadas
**Output**: `campaign.structure`, `budget_daily`, `target_roas`

### Phase 3: Weekly Optimizer
**Input**: `performance_data`, `periodo` (default: 7d)
**Action**: Analisar dados, pausar losers (ROAS < breakeven), promover winners (ROAS > target)
**Output**: `paused_campaigns`, `promoted_campaigns`, `optimization_report`

## Usage

```bash
# Planejar campanha para produto
/ml-ads planejar "fone bluetooth TWS" --custo 35 --preco 89.90

# Calcular ROAS target por margem
/ml-ads roas --margem 40 --comissao 16

# Otimizacao semanal
/ml-ads otimizar --periodo 7d

# Simulacao de cenario
/ml-ads simular --investimento 500 --produtos 20
```

## Input / Output

```yaml
input:
  produto: string            # Nome do produto
  custo_unitario: float      # Custo em BRL
  preco_venda: float         # Preco de venda em BRL
  comissao_ml: float         # Comissao ML (%) - default 16%
  frete_medio: float         # Custo medio de frete
  margem_target: float       # Margem desejada (%)
  historico_vendas: object   # Opcional: dados historicos

output:
  pricing:
    preco_minimo_ads: float  # Preco minimo viavel com ads
    margem_liquida: float    # Margem apos todos os custos
    breakeven_roas: float    # ROAS minimo para nao perder
  campaign:
    funil_stage: enum        # visibilidade|crescimento|rentabilidade
    structure:
      base_campaigns: int    # Campanhas de teste
      optimized: int         # Campanhas otimizadas
    budget_daily: float      # Orcamento diario sugerido
  metrics:
    target_roas: float
    target_acos: float
    target_tacos: float
    projected_roi: float
```

## Funnel Classification

| Estagio | Criterio | Estrategia Ads |
|---------|----------|----------------|
| Visibilidade | < 50 vendas/mes | Broad match, CPC baixo, volume |
| Crescimento | 50-200 vendas/mes | Exact match, bid otimizado |
| Rentabilidade | > 200 vendas/mes | ROAS target, max conversao |

## Anti-Patterns
- Rodar ads sem calcular breakeven primeiro: preco insustentavel, margem negativa
- Usar broad match em estagio Rentabilidade: ACOS explode sem conversao qualificada
- Otimizar com < 3 dias de dados: ruido estatistico, pausa prematura de winners

## Metrics

| Metrica | Threshold | Acao |
|---------|-----------|------|
| ROAS calculation accuracy | +/- 5% vs real | Recalibrar modelo |
| Margin validation | >= 0% liquida | Alertar preco insustentavel |
| Campaign structure | Max 20 produtos/base | Segmentar em grupos |
| Weekly optimization | >= 3 dias dados | Esperar mais dados |

## Cross-References
- `pricing` agent: Estrategia de precificacao geral (upstream)
- `ads` agent: Meta/Google Ads — nao ML (alternativa)
- `pesquisa` agent: Dados de mercado para competitividade (upstream)
- `anuncio` agent: Copy otimizado para listings ML (downstream)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_amazon_ads]] | sibling | 0.38 |
| [[p01_kc_brand_monetization_models]] | upstream | 0.23 |
| [[p01_kc_amazon_ads_benchmarks_brasil]] | upstream | 0.21 |
| [[bld_schema_optimizer]] | downstream | 0.19 |
| [[p02_agent_pesquisa]] | sibling | 0.17 |
| [[p06_is_creation_data]] | downstream | 0.17 |
| [[p06_is_quality_audit]] | downstream | 0.17 |
| [[n02_kc_campaign]] | upstream | 0.16 |
| [[p02_agent_web_researcher]] | sibling | 0.15 |
