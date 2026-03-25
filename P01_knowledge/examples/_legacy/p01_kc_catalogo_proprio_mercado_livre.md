---
id: p01_kc_catalogo_proprio_mercado_livre
type: knowledge_card
lp: P01
title: Catalogo Proprio Mercado Livre - Estrategia Completa
version: 1.0.0
created: 2026-03-03
updated: 2026-03-22
author: PYTHA
domain: ecommerce
quality: 10.0
tags: [marketplace, catalogo, mercado-livre, buy-box, estrategia]
tldr: Estrategia completa de catalogo proprio no ML com Buy Box factors, timeline e metricas
when_to_use: Quando precisa criar ou otimizar catalogo proprio no Mercado Livre
keywords: [catalogo-proprio, buy-box, mercado-livre, marketplace-strategy, logistica-full]
long_tails:
  - como criar catalogo proprio no mercado livre
  - fatores que influenciam o buy box no ML
axioms:
  - Nunca ruptura ou perder ranking
  - Prejuizo inicial = investimento em posicionamento
linked_artifacts:
  workflow: p12_wf_catalogo_ml_creator
  prompt: p03_pt_catalogo_ml_strategy
density_score: 0.92
---

# Catalogo Proprio Mercado Livre

## Quick Reference
- Buy Box: Logistica 40% | Preco 30% | Reputacao 20% | Historico 10%
- Timeline: 30-45 dias para posicionamento inicial
- Margem zero por 30 dias (investimento)
- Full logistica = requisito obrigatorio para Buy Box

## Fases
1. PESQUISA: identificar top 20 produtos por volume (dados ML)
2. CATALOGO: criar listings com fotos e descricoes otimizadas
3. PRECO: agressivo nos primeiros 30 dias (margem zero)
4. LOGISTICA: ativar Full (ML coleta e entrega)
5. ESCALA: expandir catalogo baseado em dados de venda

## Regras de Ouro
1. NUNCA ficar sem estoque (ruptura mata ranking)
2. Preco sempre competitivo (+-5% da concorrencia)
3. Responder perguntas em < 1h (impacta reputacao)
4. Frete gratis via Full (nao absorva frete manualmente)
5. Fotos proprias > fotos genericas do fabricante

## Flow

```
PESQUISA          CATALOGO          PRECO            LOGISTICA         ESCALA
   |                 |                |                 |                |
   v                 v                v                 v                v
[Top 20 SKUs]  [Criar Listings]  [Margem Zero]    [Ativar Full]    [Expandir]
[Volume ML]    [Fotos proprias]  [30 dias]        [ML coleta]      [Dados venda]
[Gap analise]  [SEO titulo]     [-5% concorr.]   [Frete gratis]   [+20 SKUs/mes]
   |                 |                |                 |                |
   v                 v                v                 v                v
 ~3 dias          ~5 dias          ~30 dias          ~7 dias         continuo
   |                 |                |                 |                |
   +--------+--------+-------+-------+--------+-------+                |
            |                |                 |                        |
            v                v                 v                        |
      [CHECKPOINT]     [CHECKPOINT]      [CHECKPOINT]                   |
      20 listings      Buy Box em         Margem > 0                   |
      publicados       5+ produtos        em 10+ SKUs                  |
                                                |                      |
                                                +----------+-----------+
                                                           |
                                                           v
                                                    [CICLO CONTINUO]
                                                    Repetir com novos
                                                    top 20 por volume
```

### Metricas por Etapa

| Etapa | Duracao | KPI | Meta |
|-------|---------|-----|------|
| Pesquisa | 3 dias | SKUs mapeados | 20 com volume > 50/mes |
| Catalogo | 5 dias | Listings ativos | 20 com fotos proprias |
| Preco | 30 dias | Buy Box share | >= 30% dos SKUs |
| Logistica | 7 dias | Full ativado | 100% dos SKUs |
| Escala | continuo | Revenue growth | +15% MoM |

### Decisao: Quando Parar Margem Zero

```
SE (vendas >= 10/mes por SKU) E (Buy Box >= 30%)
  ENTAO: aumentar margem gradualmente (+2% por semana)
SENAO: manter margem zero por mais 15 dias
SE (60 dias sem Buy Box): avaliar se SKU vale continuar
```

## Comparativo
- Catalogo proprio vs Anuncio normal: 3x mais controle de marca
- Full vs Flex: Full ganha Buy Box, Flex perde para Full
- Preco agressivo vs Margem: primeiros 30d preco > margem