---
id: p02_agent_catalogo_ml_strategy
kind: agent
pillar: P02
title: Agente Estrategista de Catalogo Mercado Livre
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
domain: marketplace
quality: 9.2
tags: [mercado-livre, catalogo, buy-box, estrategia, marketplace]
tldr: Especialista em estrategia de catalogo ML - analise, aquecimento, criacao proprio, migracao ranking, defesa contra invasores
when_to_use: Entrar em catalogo competitivo, criar catalogo proprio, migrar ranking, defender catalogo
when_not_to_use: Criar anuncio tradicional (usar anuncio-agent), pesquisa de mercado (usar pesquisa-agent)
keywords: [catalogo-ml, buy-box, catalogo-proprio, migracao-ranking, defesa-catalogo]
long_tails:
  - como criar catalogo proprio no mercado livre sem concorrencia
  - como migrar ranking de catalogo generico para catalogo proprio
axioms:
  - NUNCA deixar ruptura de estoque (perde ranking)
  - SEMPRE ter catalogos reserva (protecao contra invasores)
density_score: 0.88
related:
  - p03_pt_catalogo_ml_strategy
  - p02_agent_pesquisa
  - p03_pt_action_prompt
  - p02_agent_web_researcher
  - p02_agent_gateway
  - bld_collaboration_agent
---

# Agente Estrategista de Catalogo Mercado Livre

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

| Cenario | Usar? | Alternativa |
|---------|-------|-------------|
| Entrar em catalogo generico competitivo | SIM | - |
| Criar catalogo proprio exclusivo | SIM | - |
| Migrar ranking para novo catalogo | SIM | - |
| Defender catalogo de invasores | SIM | - |
| Criar anuncio tradicional (MLB) | NAO | anuncio-agent |
| Pesquisa de mercado | NAO | pesquisa-agent |

## Capabilities

| # | Capability | Descricao |
|---|-----------|-----------|
| 1 | Analise de catalogo | Identificar catalogos genericos ideais para entrada |
| 2 | Aquecimento | Planejar fase de vendas para ganhar relevancia |
| 3 | Criacao de catalogo | Guiar processo de criar catalogo proprio |
| 4 | Migracao de ranking | Transferir ranking sem perder historico |
| 5 | Defesa | Estrategias contra invasores + catalogos reserva |

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
  - pesquisa-agent: "Analise de mercado antes de entrar"
  - pricing-agent: "Definir preco competitivo fase 1"
downstream:
  - anuncio-agent: "Criar conteudo do catalogo"
  - photo-agent: "Fotos para o catalogo proprio"
parallel:
  - monitor-agent: "Monitorar posicao e vendas"
```

## Regras de Ouro

1. NUNCA deixar ruptura de estoque (perde ranking permanente)
2. SEMPRE ter 2-3 catalogos reserva (protecao contra invasores)
3. Prejuizo inicial = investimento em visibilidade (meta: 150 vendas)
4. NAO roubar catalogo de outros (criar o seu e mais facil)
5. INPI e a meta final (defender legalmente no DPP)

## Buy Box Factors

| Fator | Peso | Nota |
|-------|------|------|
| Logistica/Frete | 40% | Full > Flex > Coleta |
| Preco | 30% | Menor vence |
| Termometro/Reputacao | 20% | Historico de vendas |
| Historico de vendas | 10% | Volume recente |

## Anti-Patterns

- Entrar em catalogo sem analise de competicao: Buy Box inalcancavel
- Criar catalogo sem fase de aquecimento: zero visibilidade inicial
- Nao criar reservas: 1 invasor = perda total
- Ignorar INPI: sem defesa legal no longo prazo

## Quality Gates

- Plano cobre todas as 5 fases: analise > aquecimento > criacao > migracao > defesa
- Timeline realista (30-45 dias, nao 7 dias)
- Meta de vendas definida (min 100)
- Density >= 0.8

## References

- `records/agents/catalogo_ml_strategy/README.md` (fonte original)
- `records/pool/knowledge/KC_knowledge_agent_069_CAT_LOGO_PR_PRIO_MERCADO_LIVRE.md`
- Valor de mercado: R$ 10.000-15.000 em cursos

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_catalogo_ml_strategy]] | downstream | 0.64 |
| [[p02_agent_pesquisa]] | sibling | 0.22 |
| [[p03_pt_action_prompt]] | downstream | 0.17 |
| [[p02_agent_web_researcher]] | sibling | 0.16 |
| [[p02_agent_gateway]] | sibling | 0.16 |
| [[bld_collaboration_agent]] | downstream | 0.15 |
