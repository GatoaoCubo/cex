---
id: p07_sr_geographic_business_density
kind: scoring_rubric
pillar: P07
title: Geographic Business Density Scoring Rubric
version: 1.0.0
created: 2026-04-03
updated: 2026-04-03
author: builder_agent
domain: crm-research
framework: custom
dimensions_count: 5
scale: 10
aggregation: weighted_avg
llm_function: GOVERN
tags: [scoring_rubric, geographic, density, crm, expansion, priority, GATO3]
tldr: "Framework de avaliacao para priorizar cidades por densidade de negocios pet, saturacao, potencial de expansao e alinhamento com estrategia GATO3 ring-based."
quality: 9.1
density_score: null
---

# Geographic Business Density Scoring Rubric

## Overview
Rubrica para avaliar e ranquear cidades candidatas a expansao CRM GATO3. Mede 5 dimensoes que determinam se uma cidade vale o investimento de research e outreach. Usado apos Phase 7 (Scoring) da pipeline CRM para priorizar proximo ciclo de expansao.

## Dimensions

| # | Dimension | Weight | Measurability | Automation |
|---|-----------|--------|---------------|------------|
| D1 | Density Score | 30% | objective | automated |
| D2 | Market Saturation | 20% | semi-objective | semi-automated |
| D3 | ICP Alignment | 20% | subjective | manual |
| D4 | Competition Landscape | 15% | semi-objective | semi-automated |
| D5 | Logistics Feasibility | 15% | objective | automated |

**Total: 100%**

## D1: Density Score (30%)
**Formula**: `businesses_pet / (populacao / 10000)`

| Score | Criteria |
|-------|----------|
| 10 | >= 3.0 biz/10k hab — mercado denso, alta oportunidade B2B |
| 9 | 2.5-2.9 — densidade forte, multiplas verticais presentes |
| 7 | 1.5-2.4 — densidade moderada, oportunidade seletiva |
| 5 | 1.0-1.4 — densidade baixa, requer validacao manual |
| 3 | 0.5-0.9 — densidade muito baixa, alto risco de ROI negativo |
| 1 | < 0.5 — mercado insuficiente para prospecao ativa |

## D2: Market Saturation (20%)
**Formula**: `concorrentes_curadoria_premium / total_businesses_pet`

| Score | Criteria |
|-------|----------|
| 10 | < 5% saturacao — mercado virgem para curadoria premium |
| 9 | 5-10% — pouca competicao em segmento premium |
| 7 | 10-20% — competicao moderada, diferenciacao necessaria |
| 5 | 20-35% — mercado competitivo, entrar apenas com UVP forte |
| 3 | 35-50% — alta saturacao, risco de guerra de precos |
| 1 | > 50% — mercado saturado, nao recomendado |

## D3: ICP Alignment (20%)
**Criterios**: Populacao 25-45, renda B-C+, urbano, cultura pet

| Score | Criteria |
|-------|----------|
| 10 | Cidade com perfil demografico perfeito para ICP GATO3 — alta renda, urbano, cultura pet forte |
| 9 | 4/5 criterios ICP presentes, desvio menor em 1 dimensao |
| 7 | 3/5 criterios — maioria alinhada, ajuste de messaging necessario |
| 5 | 2/5 — alinhamento parcial, requer campanha adaptada |
| 3 | 1/5 — baixo alinhamento, apenas oportunismo pontual |
| 1 | 0/5 — perfil nao compativel com ICP |

## D4: Competition Landscape (15%)
**Criterios**: Presenca de redes nacionais, pet shops independentes, marketplaces ativos

| Score | Criteria |
|-------|----------|
| 10 | Mercado fragmentado, sem redes dominantes — ideal para curadoria |
| 9 | 1 rede presente mas < 20% market share |
| 7 | 2-3 redes, mercado competitivo mas viavel |
| 5 | Redes dominam 40%+ — dificil penetracao B2B |
| 3 | Oligopolio local — poucos players grandes controlam |
| 1 | Monopolio ou mercado fechado |

## D5: Logistics Feasibility (15%)
**Criterios**: Distancia do HQ (SCS), custo frete, infraestrutura entrega

| Score | Criteria |
|-------|----------|
| 10 | Ring 1 (ABC) — entrega propria, custo minimo, visita presencial facil |
| 9 | Ring 1 adjacente — ate 30km do HQ |
| 7 | Ring 2 (Grande SP) — frete acessivel, visita com agendamento |
| 5 | Ring 3 (Estado SP) — requer transportadora, visita esporadica |
| 3 | Ring 4 nacional capital — apenas e-commerce, sem presenca local |
| 1 | Ring 4 interior — custo logistico inviavel para B2B |

## Tier Thresholds

| Tier | Score Range | Action |
|------|-------------|--------|
| Prioritaria | >= 8.0 | Research imediato + outreach ativo |
| Promissora | 6.0-7.9 | Research programado, proximo ciclo |
| Monitorar | 4.0-5.9 | Apenas e-commerce passivo |
| Descartar | < 4.0 | Nao investir recursos de prospecao |

## Calibration
- **Referencia**: Sao Caetano do Sul (Ring 1) = score esperado 9.0+
- **Baseline**: Sao Bernardo do Campo (Ring 1) = score esperado 8.0+
- **Validacao**: Comparar ranking com resultados reais de CRM R1-R4

## Footer
Framework: custom (geographic-density) | Quality: null | Domain: crm-research
