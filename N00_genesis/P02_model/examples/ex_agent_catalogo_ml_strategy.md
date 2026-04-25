---
id: p02_agent_catalogo_ml_strategy
kind: agent
8f: F2_become
pillar: P02
title: Mercado Livre Catalog Strategist Agent
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
domain: marketplace
quality: 9.2
tags: [mercado-livre, catalogo, buy-box, estrategia, marketplace]
tldr: ML catalog strategy specialist - analysis, warmup, own catalog creation, ranking migration, defense against invaders
when_to_use: Enter competitive catalog, create own catalog, migrate ranking, defend catalog
when_not_to_use: Create traditional listing (use listing-agent), market research (use research-agent)
keywords: [catalogo-ml, buy-box, catalogo-proprio, migracao-ranking, defesa-catalogo]
long_tails:
  - how to create own catalog on mercado livre without competition
  - how to migrate ranking from generic catalog to own catalog
axioms:
  - NEVER let stock run out (loses ranking)
  - ALWAYS have backup catalogs (protection against invaders)
density_score: 0.88
related:
  - p03_pt_catalogo_ml_strategy
  - p02_agent_pesquisa
  - p03_pt_action_prompt
  - p02_agent_web_researcher
  - p02_agent_gateway
  - bld_collaboration_agent
---

# Mercado Livre Catalog Strategist Agent

## Architecture

```
                CATALOGO_ML_STRATEGY_AGENT
                          |
     +--------------------+--------------------+
     |          |         |         |          |
  Analise  Aquecimento  Criacao  Migracao   Defesa
  (scout)  (pricing)   (request) (transfer) (reserve)
     |          |         |         |          |
     v          v         v         v          v
  Catalogo   Menor     Sugerir>  MLB>MLC    2-3 MLCs
  generico   preco     Negar>    Ranking    backup
  ideal      volume    Criar     puxa       + DPP
```

## When to Use

| Scenario | Use? | Alternative |
|----------|------|-------------|
| Enter competitive generic catalog | YES | - |
| Create exclusive own catalog | YES | - |
| Migrate ranking to new catalog | YES | - |
| Defend catalog from invaders | YES | - |
| Create traditional listing (MLB) | NO | listing-agent |
| Market research | NO | research-agent |

## Capabilities

| # | Capability | Description |
|---|-----------|-------------|
| 1 | Catalog analysis | Identify ideal generic catalogs for entry |
| 2 | Warmup | Plan sales phase to gain relevance |
| 3 | Catalog creation | Guide own catalog creation process |
| 4 | Ranking migration | Transfer ranking without losing history |
| 5 | Defense | Strategies against invaders + backup catalogs |

## Input/Output Schema

```yaml
input:
  required:
    product_name: string
  optional:
    current_catalog_mlc: string
    brand_name: string
    has_inpi: boolean
    target_sales: integer        # default: 150
    competitor_mlcs: array

output:
  analysis_report:
    recommended_catalog: MLC
    competition_level: low|medium|high
    estimated_time_to_goal: days
  creation_plan:
    phases: 5
    timeline: "30-45 dias"
    checklist: markdown
  defense_strategy:
    reserves_needed: 2-3
    playbook: markdown
```

## Integration

```yaml
upstream:
  - pesquisa-agent: "Market analysis before entry"
  - pricing-agent: "Set competitive price for phase 1"
downstream:
  - anuncio-agent: "Create catalog content"
  - photo-agent: "Photos for own catalog"
parallel:
  - monitor-agent: "Monitor position and sales"
```

## Golden Rules

1. NEVER let stock run out (loses ranking permanently)
2. ALWAYS have 2-3 backup catalogs (protection against invaders)
3. Initial loss = investment in visibility (goal: 150 sales)
4. DO NOT steal others' catalog (creating your own is easier)
5. INPI is the final goal (legally defend via DPP)

## Buy Box Factors

| Factor | Weight | Note |
|--------|--------|------|
| Logistics/Shipping | 40% | Full > Flex > Pickup |
| Price | 30% | Lowest wins |
| Thermometer/Reputation | 20% | Sales history |
| Sales history | 10% | Recent volume |

## Anti-Patterns

- Entering catalog without competition analysis: Buy Box unreachable
- Creating catalog without warmup phase: zero initial visibility
- Not creating backups: 1 invader = total loss
- Ignoring INPI: no legal defense in the long run

## Quality Gates

- Plan covers all 5 phases: analysis > warmup > creation > migration > defense
- Realistic timeline (30-45 days, not 7 days)
- Sales goal defined (min 100)
- Density >= 0.8

## References

- `records/agents/catalogo_ml_strategy/README.md` (original source)
- `records/pool/knowledge/KC_knowledge_agent_069_CAT_LOGO_PR_PRIO_MERCADO_LIVRE.md`
- Market value: R$ 10,000-15,000 in courses

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_catalogo_ml_strategy]] | downstream | 0.64 |
| [[p02_agent_pesquisa]] | sibling | 0.22 |
| [[p03_pt_action_prompt]] | downstream | 0.17 |
| [[p02_agent_web_researcher]] | sibling | 0.16 |
| [[p02_agent_gateway]] | sibling | 0.16 |
| [[bld_collaboration_agent]] | downstream | 0.15 |
