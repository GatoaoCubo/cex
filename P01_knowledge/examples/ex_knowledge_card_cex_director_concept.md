---
id: p01_kc_cex_agent_node_concept
kind: knowledge_card
pillar: P01
title: "CEX Satellite Concept — Verticalized Departments as Complete LLM Entities"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.0
tags: [cex, agent_node, department, specialization, agent-team, boot-sequence]
tldr: "Satellite eh entidade L4 que preenche 12 LPs — departamento completo com identidade, equipe, tools, memoria e governanca"
when_to_use: "Entender como organizar agentes LLM em departamentos especializados com autonomia total"
keywords: [agent_node, department, specialization, vertical, agent-team]
long_tails:
  - "Como estruturar departamentos de agentes LLM especializados"
  - "Qual a diferenca entre agent e agent_node no CEX"
axioms:
  - "SEMPRE 1 agent_node = 1 dominio = autonomia total"
  - "NUNCA agent_node executa fora do seu dominio"
linked_artifacts:
  primary: p01_kc_cex_cortex_enterprise
  related: [p01_kc_cex_function_become, p01_kc_cex_pipeline_execution]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
---

## Summary

Satellite eh a entidade de maior completude no CEX (Level 4). Preenche todos os 12 Lifecycle Positions: tem identidade (P02), conhecimento (P01), instrucoes (P03), skills (P04), templates (P05), schemas (P06), testes (P07), arquitetura (P08), config (P09), memoria (P10), learning (P11) e coordenacao (P12). Equivale a um departamento empresarial completo com equipe de 22-105 agentes especializados.

## Spec

| Propriedade | Valor | Nota |
|-------------|-------|------|
| Level | L4 (maximo) | L1=prompt, L2=chain, L3=agent, L4=agent_node |
| LPs preenchidos | 12/12 | Unica entidade com cobertura total |
| Agentes por agent_node | 22-105 | commercial_agent=22 (menor), builder_agent=105 (maior) |
| Arquivos de identidade | 2 | PRIME_{SAT}.md + mental_model.yaml |
| Boot time | 5-15s | Depende de MCPs carregados |
| Modelo | sonnet ou opus | Opus para tarefas complexas (build, deploy) |
| MCPs | 1-3 por agent_node | Brain (universal) + especializados |
| Autonomia | Total no dominio | Orquestrador nao interfere na execucao |

Implementacao de referencia (organization) — 7 agent_nodes:

| Satellite | Dominio | Lens | Modelo | MCPs | Agentes |
|-----------|---------|------|--------|------|---------|
| orchestrator | Orquestracao | — | opus | brain+orch | 0 (roteia) |
| research_agent | Pesquisa | Inveja Analitica | sonnet | firecrawl+brain | 45 |
| marketing_agent | Marketing | Luxuria Estrategica | sonnet | markitdown+brain | 37 |
| builder_agent | Engenharia | Soberba Inventiva | opus | brain | 105 |
| knowledge_agent | Conhecimento | Gula Sistematica | sonnet | brain | 38 |
| operations_agent | Operacoes | Ira Realizadora | opus | railway+pg+brain | 37 |
| commercial_agent | Receita | Avareza Visionaria | sonnet | brain | 22 |

## Patterns

| Trigger | Action |
|---------|--------|
| Dominio requer >10 agentes | Criar agent_node dedicado |
| Tarefa cruza 2+ dominios | Orquestrador decompoe em sub-tarefas por agent_node |
| Satellite precisa de boot rapido | Minimizar MCPs (cada MCP = +2-5s) |
| Equipe cresce acima de 50 agentes | Subdividir com mental_model por especialidade |
| Novo dominio de negocio emerge | Instanciar agent_node com PRIME + mental_model |

## Anti-Patterns

- Satellite sem PRIME.md (sem identidade = execucao incoerente)
- Satellite executando tarefas de outro dominio (viola separacao)
- Orquestrador executando ao inves de despachar para agent_node
- Satellite com 0 agentes (container vazio, sem capacidade)
- Compartilhar MCPs entre agent_nodes (acoplamento, boot lento)

## Code

<!-- lang: python | purpose: agent_node instantiation -->
```python
agent_node = Satellite(
    name="shaka",
    domain="market_research",
    model="sonnet",
    mcps=["firecrawl", "brain"],
    prime="PRIME_research_agent.md",
    mental_model="mental_model.yaml",
    agents=load_agents("shaka", count=45),
)
# BECOME: prime + mental_model configuram identidade
# CALL: mcps definem ferramentas disponiveis
# L4: 12/12 LPs preenchidos = agent_node completo
```

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_cortex_enterprise
- related: p01_kc_cex_function_become
- related: p01_kc_cex_pipeline_execution
