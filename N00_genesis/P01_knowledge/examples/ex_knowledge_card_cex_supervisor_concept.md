---
id: p01_kc_cex_agent_group_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Agent_group Concept — Verticalized Departments as Complete LLM Entities"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, agent_group, department, specialization, agent-team, boot-sequence]
tldr: "Agent_group eh entidade L4 que preenche 12 LPs — departamento completo com identidade, equipe, tools, memoria e governanca"
when_to_use: "Entender como organizar agentes LLM em departamentos especializados com autonomia total"
keywords: [agent_group, department, specialization, vertical, agent-team]
long_tails:
  - "Como estruturar departamentos de agentes LLM especializados"
  - "Qual a diferenca entre agent e agent_group no CEX"
axioms:
  - "SEMPRE 1 agent_group = 1 dominio = autonomia total"
  - "NUNCA agent_group executa fora do seu dominio"
linked_artifacts:
  primary: p01_kc_cex_cortex_enterprise
  related: [p01_kc_cex_function_become, p01_kc_cex_pipeline_execution]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - bld_collaboration_agent_card
  - agent-card-builder
  - p01_kc_cex_cortex_enterprise
  - bld_knowledge_card_agent_card
  - bld_examples_agent_card
  - p12_wf_stella_dispatch
  - p03_ins_agent_card_builder
  - bld_collaboration_spawn_config
  - p11_qg_agent-card
  - p01_gl_agent_group
---

## Summary

Agent_group eh a entidade de maior completude no CEX (Level 4). Preenche todos os 12 Lifecycle Positions: tem identidade (P02), conhecimento (P01), instrucoes (P03), skills (P04), templates (P05), schemas (P06), testes (P07), arquitetura (P08), config (P09), memoria (P10), learning (P11) e coordenacao (P12). Equivale a um departamento empresarial completo com equipe de 22-105 agentes especializados.

## Spec

| Propriedade | Valor | Nota |
|-------------|-------|------|
| Level | L4 (maximo) | L1=prompt, L2=chain, L3=agent, L4=agent_group |
| LPs preenchidos | 12/12 | Unica entidade com cobertura total |
| Agentes por agent_group | 22-105 | commercial_agent=22 (menor), builder_agent=105 (maior) |
| Arquivos de identidade | 2 | PRIME_{SAT}.md + mental_model.yaml |
| Boot time | 5-15s | Depende de MCPs carregados |
| Modelo | sonnet ou opus | Opus para tarefas complexas (build, deploy) |
| MCPs | 1-3 por agent_group | Brain (universal) + especializados |
| Autonomia | Total no dominio | Orquestrador nao interfere na execucao |

Implementacao de referencia (organization) — 7 agent_groups:

| Agent_group | Dominio | Lens | Modelo | MCPs | Agentes |
|-----------|---------|------|--------|------|---------|
| orchestrator | Orquestracao | — | opus | brain+orch | 0 (roteia) |
| research_agent | Pesquisa | Analytical Envy | sonnet | firecrawl+brain | 45 |
| marketing_agent | Marketing | Creative Lust | sonnet | markitdown+brain | 37 |
| builder_agent | Engenharia | Inventive Pride | opus | brain | 105 |
| knowledge_agent | Conhecimento | Knowledge Gluttony | sonnet | brain | 38 |
| operations_agent | Operacoes | Gating Wrath | opus | railway+pg+brain | 37 |
| commercial_agent | Receita | Strategic Greed | sonnet | brain | 22 |

## Patterns

| Trigger | Action |
|---------|--------|
| Dominio requer >10 agentes | Criar agent_group dedicado |
| Tarefa cruza 2+ dominios | Orquestrador decompoe em sub-tarefas por agent_group |
| Agent_group precisa de boot rapido | Minimizar MCPs (cada MCP = +2-5s) |
| Equipe cresce acima de 50 agentes | Subdividir com mental_model por especialidade |
| Novo dominio de negocio emerge | Instanciar agent_group com PRIME + mental_model |

## Anti-Patterns

- Agent_group sem PRIME.md (sem identidade = execucao incoerente)
- Agent_group executando tarefas de outro dominio (viola separacao)
- Orquestrador executando ao inves de despachar para agent_group
- Agent_group com 0 agentes (container vazio, sem capacidade)
- Compartilhar MCPs entre agent_groups (acoplamento, boot lento)

## Code

<!-- lang: python | purpose: agent_group instantiation -->
```python
agent_group = Agent_group(
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
# L4: 12/12 LPs preenchidos = agent_group completo
```

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_cortex_enterprise
- related: p01_kc_cex_function_become
- related: p01_kc_cex_pipeline_execution

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent_card]] | downstream | 0.46 |
| [[agent-card-builder]] | downstream | 0.36 |
| [[p01_kc_cex_cortex_enterprise]] | sibling | 0.35 |
| [[bld_knowledge_card_agent_card]] | sibling | 0.34 |
| [[bld_examples_agent_card]] | downstream | 0.31 |
| [[p12_wf_stella_dispatch]] | downstream | 0.30 |
| [[p03_ins_agent_card_builder]] | downstream | 0.29 |
| [[bld_collaboration_spawn_config]] | downstream | 0.28 |
| [[p11_qg_agent-card]] | downstream | 0.28 |
| [[p01_gl_agent_group]] | related | 0.27 |
