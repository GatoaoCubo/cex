---
id: p01_kc_supabase_pricing
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Pricing — Tiers, Limites, Cost Optimization"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, pricing, tiers, free, pro, team, enterprise, cost, platform]
tldr: "4 tiers: Free (USD 0, 500MB DB, 2 projetos), Pro (USD 25/mo, 8GB DB), Team (USD 599/mo, SOC2+SSO), Enterprise (custom). Overage billing no Pro+."
when_to_use: "Quando decidir tier Supabase ou otimizar custos de projeto existente"
keywords: [supabase-pricing, free-tier, pro-tier, cost-optimization]
long_tails:
  - Quanto custa Supabase Pro por mes com overages
  - Limites do free tier do Supabase em 2025
  - Como otimizar custos no Supabase Pro tier
axioms:
  - SEMPRE comece no Free tier para validar — upgrade quando necessário
  - NUNCA ignore overage pricing — DB storage pode escalar rápido
  - SEMPRE monitore usage dashboard para evitar surpresas no billing
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_storage]
density_score: 0.93
data_source: "https://supabase.com/pricing"
related:
  - p04_ex_content_monetization_saas
  - bld_config_supabase_data_layer
  - commercial_readiness_20260413
  - n06_intent_resolution_depth_spec
  - p01_kc_supabase_database
  - bld_schema_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - bld_output_template_pricing_page
  - commercial_readiness_20260414
  - p01_kc_cost_budget
---

# Supabase Pricing

## Quick Reference
```yaml
topic: supabase_pricing
scope: Free, Pro, Team, Enterprise tiers + overage costs
owner: n04_knowledge
criticality: high
url: https://supabase.com/pricing
```

## Tier Comparison
| Recurso | Free (USD 0) | Pro (USD 25/mo) | Team (USD 599/mo) | Enterprise |
|---------|-------------|-----------------|---------------------|------------|
| Projetos | 2 ativos | Ilimitado | Ilimitado | Ilimitado |
| Database | 500 MB | 8 GB | 8 GB | Custom |
| Bandwidth | 5 GB | 250 GB | 250 GB | Custom |
| Storage | 1 GB | 100 GB | 100 GB | Custom |
| Edge Functions | 500K/mo | 2M/mo | 2M/mo | Custom |
| Auth MAU | 50.000 | 100.000 | 100.000 | Custom |
| Realtime msgs | 2M/mo | 5M/mo | Ilimitado | Custom |
| Concurrent RT | 200 | 500 | 1000+ | Custom |
| Daily backups | Não | 7 dias | 14 dias | Custom |
| PITR | Não | Addon | Addon | Incluso |
| SOC2 | Não | Não | Sim | Sim |
| SSO SAML | Não | Addon | Incluso | Incluso |
| Support | Community | Email | Priority | Dedicated |

## Overage Pricing (Pro+)
| Recurso | Incluído (Pro) | Overage |
|---------|---------------|---------|
| Database | 8 GB | USD 0.125/GB |
| Bandwidth | 250 GB | USD 0.09/GB |
| Storage | 100 GB | USD 0.021/GB |
| Auth MAU | 100K | USD 0.00325/MAU |
| Edge invocations | 2M | USD 0.002/1K |
| Realtime msgs | 5M | USD 0.0025/1K |

## Addons (Pro+)
| Addon | Preço | O Que Faz |
|-------|-------|-----------|
| PITR | USD 100/mo | Point-in-time recovery |
| Custom domain | USD 10/mo | Seu domínio na API URL |
| Compute (Small) | Incluso Pro | 2 CPU, 1 GB RAM |
| Compute (Medium) | USD 100/mo | 2 CPU, 2 GB RAM |
| Compute (Large) | USD 200/mo | 2 CPU, 4 GB RAM |
| Compute (XL) | USD 400/mo | 4 CPU, 8 GB RAM |
| Compute (2XL) | USD 950/mo | 8 CPU, 16 GB RAM |
| IPv4 | USD 4/mo | Dedicated IPv4 address |

## Decision Tree
```text
Projeto novo / MVP / teste?
  → FREE (validar, iterar, sem custo)

Produção com <100K MAU, <8GB DB?
  → PRO (USD 25/mo, suficiente para maioria)

Produção com SOC2, SSO, suporte priority?
  → TEAM (USD 599/mo, compliance ready)

>100K MAU, SLA 99.99%, dedicated support?
  → ENTERPRISE (negociar custom)
```

## Cost Optimization Tips
| Tip | Economia Estimada |
|-----|-------------------|
| `pg_stat_statements` → otimizar queries lentas | 20-40% CPU/RAM |
| Index em colunas de filtro/RLS | 50-90% query time |
| Storage: servir webp via transforms | 40-60% bandwidth |
| CDN (Pro) para assets estáticos | 50-70% bandwidth |
| Connection pooler (Supavisor) | Menos compute addon |
| Edge Functions: cache results | 30-50% invocations |
| Realtime: filtrar por tabela/evento | Menos mensagens |
| Cleanup: pg_cron para deletar dados expirados | DB storage |

## Custos por Vertical
| Vertical | Tier | Custo/mês |
|----------|------|-----------| 
| MVP / Side project | Free | USD 0 |
| E-commerce pequeno | Pro | USD 25-35 |
| SaaS B2B (500 users) | Pro | USD 30-60 |
| Marketplace (10K listings) | Pro+Compute | USD 130-200 |
| Content platform (50K posts) | Team | USD 620-700 |

## Anti-Patterns
| Anti-Pattern | Custo Extra | Fix |
|-------------|-------------|-----|
| Sem spend cap no Pro | Overage inesperado | Habilitar spend cap |
| Dados nunca deletados | DB cresce infinitamente | pg_cron cleanup |
| Imagens originais servidas | Bandwidth 5-10x | Transforms + CDN |
| Projeto Free inativo | Pausado após 7 dias | Mover para Pro ou deletar |

## Golden Rules
- COMECE Free, suba para Pro quando validar product-market fit
- HABILITE spend cap no Pro para evitar surpresas
- MONITORE Dashboard > Usage semanalmente
- PROJETE para o tier — não assuma Enterprise features no Free

## References
- Pricing: https://supabase.com/pricing
- Spend cap: https://supabase.com/docs/guides/platform/spend-cap
- Compute addons: https://supabase.com/docs/guides/platform/compute-add-ons

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ex_content_monetization_saas]] | downstream | 0.31 |
| [[bld_config_supabase_data_layer]] | downstream | 0.28 |
| [[commercial_readiness_20260413]] | downstream | 0.26 |
| [[n06_intent_resolution_depth_spec]] | downstream | 0.26 |
| [[p01_kc_supabase_database]] | sibling | 0.24 |
| [[bld_schema_supabase_data_layer]] | downstream | 0.24 |
| [[bld_knowledge_card_supabase_data_layer]] | sibling | 0.24 |
| [[bld_output_template_pricing_page]] | downstream | 0.21 |
| [[commercial_readiness_20260414]] | downstream | 0.21 |
| [[p01_kc_cost_budget]] | sibling | 0.20 |
