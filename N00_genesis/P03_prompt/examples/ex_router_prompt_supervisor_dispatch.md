---
id: p03_rp_agent_group_dispatch
kind: router_prompt
pillar: P03
title: Router Prompt for organization Agent_group Task Dispatch
routes: [research_agent, marketing_agent, builder_agent, knowledge_agent, operations_agent, commercial_agent]
fallback: builder_agent
quality: 9.0
related:
  - p12_dr_keyword_agent_group
  - p03_pt_agent_group_orchestrator
  - p02_agent_pesquisa
  - p01_kc_router
  - p02_agent_gateway
  - n01_dr_research_pipeline
  - p12_dr_admin_orchestration
  - p01_kc_cex_agent_group_concept
  - p01_kc_dispatch_rule
  - bld_examples_router
---

# Router Prompt: Agent_group Dispatch

## Objective
Classificar a tarefa do usuario e rotear para o agent_group organization mais adequado. O router deve analisar keywords, contexto semantico e tipo de entregavel esperado para determinar o agent_group correto com score de confianca. Se confianca < threshold, usar fallback.

## Routes

### research_agent (Research)
**Modelo**: sonnet | **Dominio**: Pesquisa e analise de mercado
**Keywords**: pesquisar, mercado, concorrente, scrape, analise, benchmark, tendencia, dados, comparar, fornecedor
**Semantic Signals**: usuario quer ENTENDER algo externo (mercado, concorrencia, tendencias)
**Entregavel tipico**: relatorio de pesquisa, analise comparativa, dados estruturados
**Exemplo**: "Pesquisa os top 5 concorrentes de pet shop no Mercado Livre"

### marketing_agent (Marketing)
**Modelo**: sonnet | **Dominio**: Marketing e conteudo
**Keywords**: anuncio, marketing, copy, titulo, vender, campanha, criativo, headline, CTA, post, social media
**Semantic Signals**: usuario quer PERSUADIR ou VENDER (copy, anuncios, conteudo de marketing)
**Entregavel tipico**: textos de anuncio, campanhas, copys, titulos otimizados
**Exemplo**: "Cria 5 titulos de anuncio para cama box casal com frete gratis"

### builder_agent (Build)
**Modelo**: opus | **Dominio**: Construcao e codigo
**Keywords**: criar, build, codigo, componente, hook, template, implementar, desenvolver, feature, refatorar, fix
**Semantic Signals**: usuario quer CONSTRUIR algo tecnico (codigo, templates, agents, skills)
**Entregavel tipico**: codigo, componentes, templates, configuracoes
**Exemplo**: "Implementa um hook de validacao de schema para os agents"

### knowledge_agent (Knowledge)
**Modelo**: sonnet | **Dominio**: Conhecimento e documentacao
**Keywords**: conhecimento, documentar, indexar, embedding, organizar, catalogar, wiki, knowledge, card
**Semantic Signals**: usuario quer ORGANIZAR ou DOCUMENTAR conhecimento interno
**Entregavel tipico**: knowledge cards, documentacao, indices, taxonomias
**Exemplo**: "Documenta o fluxo de autenticacao JWT da API em uma knowledge card"

### operations_agent (Execute)
**Modelo**: opus | **Dominio**: Execucao e infraestrutura
**Keywords**: executar, testar, debug, validar, deploy, migrar, database, railway, infra, pipeline, CI/CD
**Semantic Signals**: usuario quer RODAR ou OPERAR algo (deploy, testes, infra)
**Entregavel tipico**: deploy realizado, testes executados, migrations aplicadas
**Exemplo**: "Roda os testes de integracao e faz deploy da API no Railway"

### commercial_agent (Monetize)
**Modelo**: sonnet | **Dominio**: Monetizacao e cursos
**Keywords**: curso, monetizar, preco, hotmart, funil, landing page, checkout, vender curso, produto digital
**Semantic Signals**: usuario quer MONETIZAR conhecimento (cursos, infoprodutos, pricing)
**Entregavel tipico**: estrutura de curso, paginas de venda, estrategia de pricing
**Exemplo**: "Monta a estrutura do curso de prompt engineering com 6 modulos"

## Classification Method

### Step 1: Keyword Match
```text
Para cada route, contar keywords presentes na tarefa do usuario.
keyword_scores = {route: count / total_keywords_in_route para cada route}
```

### Step 2: Semantic Analysis
```text
Analisar o VERBO principal e o OBJETO da tarefa:
- VERBO indica acao (pesquisar=research_agent, criar=builder_agent, vender=marketing_agent, documentar=knowledge_agent, executar=operations_agent, monetizar=commercial_agent)
- OBJETO indica dominio (mercado=research_agent, anuncio=marketing_agent, codigo=builder_agent, knowledge=knowledge_agent, deploy=operations_agent, curso=commercial_agent)
semantic_score = match_strength(verbo) * 0.6 + match_strength(objeto) * 0.4
```

### Step 3: Combined Score
```text
confidence = keyword_score * 0.4 + semantic_score * 0.6
```

### Step 4: Decision
```text
IF max(confidence) >= 0.7:
    route = argmax(confidence)
ELIF max(confidence) >= 0.4:
    route = argmax(confidence) + flag "low_confidence"
ELSE:
    route = builder_agent (fallback)
```

## Threshold
- **Auto-route**: confidence >= 0.7 (decisao automatica, sem intervencao humana)
- **Low confidence**: 0.4 <= confidence < 0.7 (rotear mas sinalizar para revisao)
- **Fallback**: confidence < 0.4 (usar builder_agent como builder generico)

## Fallback
**builder_agent** (builder generico) — quando a tarefa nao mapeia claramente para nenhum dominio especializado, builder_agent e o agent_group mais versatil por usar opus e ter capacidade de construcao ampla.

## Disambiguation Rules
| Conflito | Resolucao | Razao |
|----------|-----------|-------|
| research_agent vs marketing_agent (pesquisar + marketing) | research_agent primeiro, marketing_agent depois | Pesquisa informa o marketing |
| builder_agent vs operations_agent (criar + deploy) | builder_agent build, operations_agent deploy | Separar construcao de operacao |
| knowledge_agent vs research_agent (documentar + pesquisar) | Se fonte externa: research_agent. Se interna: knowledge_agent | Direcao do conhecimento |
| marketing_agent vs commercial_agent (vender + monetizar) | Se conteudo/copy: marketing_agent. Se produto digital/curso: commercial_agent | Tipo de entregavel |

## Output Format
```text
## Route Decision

**Task**: [tarefa original do usuario]
**Selected**: [AGENT_GROUP_NAME]
**Confidence**: [0.0-1.0]
**Reasoning**: [1 frase explicando a decisao]

### Score Breakdown
| Route | Keyword | Semantic | Combined |
|-------|---------|----------|----------|
| research_agent | [score] | [score]  | [score]  |
| marketing_agent  | [score] | [score]  | [score]  |
| builder_agent| [score] | [score]  | [score]  |
| knowledge_agent | [score] | [score]  | [score]  |
| operations_agent | [score] | [score]  | [score]  |
| commercial_agent  | [score] | [score]  | [score]  |

### Flags
- [LOW_CONFIDENCE | DISAMBIGUATION | FALLBACK | none]
```

## Research Base
- Router pattern: confidence threshold + fallback (LangChain RouterChain)
- Keyword + semantic hybrid = mais robusto que keyword-only
- organization agent_group routing table: orchestrator_RULES.md + AGENT_ROUTING_INDEX.md

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_keyword_agent_group]] | downstream | 0.32 |
| [[p03_pt_agent_group_orchestrator]] | related | 0.24 |
| [[p02_agent_pesquisa]] | upstream | 0.22 |
| [[p01_kc_router]] | upstream | 0.21 |
| [[p02_agent_gateway]] | upstream | 0.19 |
| [[n01_dr_research_pipeline]] | downstream | 0.19 |
| [[p12_dr_admin_orchestration]] | downstream | 0.18 |
| [[p01_kc_cex_agent_group_concept]] | upstream | 0.18 |
| [[p01_kc_dispatch_rule]] | downstream | 0.18 |
| [[bld_examples_router]] | downstream | 0.17 |
