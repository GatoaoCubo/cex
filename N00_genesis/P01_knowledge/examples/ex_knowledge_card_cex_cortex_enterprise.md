---
id: p01_kc_cex_cortex_enterprise
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Cortex Enterprise — Modular LLM Brain with CEO Orchestrator and Agent_group Departments"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, cortex-enterprise, orchestrator, ceo-cognitivo, emergent-properties, brain]
tldr: "Cortex Enterprise eh cerebro empresarial modular: CEO cognitivo (roteia, nunca executa) + N agent_groups verticalizados + propriedades emergentes"
when_to_use: "Entender a arquitetura de sistema multi-agente com orquestrador central e departamentos autonomos"
keywords: [cortex-enterprise, orchestrator, ceo, brain, modular-architecture]
long_tails:
  - "Como construir um cerebro empresarial com LLMs e agentes especializados"
  - "Qual o papel do orquestrador central num sistema multi-agente"
axioms:
  - "SEMPRE orquestrador roteia, NUNCA executa"
  - "NUNCA agent_group depende de outro agent_group para completar tarefa"
linked_artifacts:
  primary: p01_kc_cex_agent_group_concept
  related: [p01_kc_cex_pipeline_execution, p01_kc_cex_function_become]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p12_wf_stella_dispatch
  - p01_kc_cex_agent_group_concept
  - bld_collaboration_agent_card
  - p03_pt_agent_group_orchestrator
  - p01_kc_cex_pipeline_execution
  - bld_knowledge_card_handoff
  - p01_kc_handoff
  - bld_knowledge_card_agent_card
  - agent-card-builder
  - p12_crew_agent_group_grid
---

## Summary

Cortex Enterprise eh um cerebro empresarial modular baseado em LLM. Arquitetura: orquestrador central (CEO cognitivo) que roteia mas NUNCA executa + N agent_groups verticalizados com autonomia total no seu dominio. Cada organizacao instancia seu Cortex[X]. organization eh a implementacao de referencia com 7 agent_groups e 284 agentes. O sistema exibe 5 propriedades emergentes: bootstrapping, metacircularidade, scaffolding cognitivo, arquitetura fractal e auto-correcao distribuida.

## Spec

| Componente | Funcao | Regra |
|------------|--------|-------|
| Orquestrador (orchestrator) | CLARIFY-ENRICH-COMPOSE-EXECUTE-MONITOR | Roteia, nunca executa |
| Agent_groups (6 exec) | Departamentos verticalizados | 1 dominio = 1 agent_group |
| Agents (284 total) | Funcionarios especializados | ISO files definem execucao |
| Handoffs | Despacho estruturado | Contexto + seeds + scope fence |
| Signals | Comunicacao inter-agent_group | JSON com status + score |
| Pool (1957 KCs) | Memoria institucional | Knowledge cards indexadas |

Propriedades emergentes do Cortex instanciado:

| Propriedade | Mecanismo | Referencia |
|-------------|-----------|------------|
| Bootstrapping | KCs alimentam agentes que geram KCs melhores | GCC self-hosting (1980s) |
| Metacircularidade | Agentes descrevem propria execucao via ISO | SICP eval (Abelson 1996) |
| Scaffolding cognitivo | Handoffs direcionam sem sobrecarregar contexto | Vygotsky ZPD (1978) |
| Arquitetura fractal | 12 LPs repetem em 4 niveis (prompt-agent-sat-sys) | Mandelbrot (1982) |
| Auto-correcao distribuida | Review chain 3-tier entre entidades independentes | Reflexion (Shinn 2023) |

Ciclo de dispatch do orquestrador (5 fases):

| Fase | Input | Output |
|------|-------|--------|
| CLARIFY | Pedido do usuario | Tabela de tasks por agent_group |
| ENRICH | Keywords por task | Contexto via brain_query |
| COMPOSE | Tasks + contexto | Handoff .md por agent_group |
| EXECUTE | Handoffs | Agent_groups em execucao paralela |
| MONITOR | Signals + git log | Relatorio consolidado |

## Patterns

| Trigger | Action |
|---------|--------|
| Tarefa multi-dominio | Orquestrador decompoe em waves por agent_group |
| Conhecimento novo gerado | Agente produz KC, pool indexa, busca melhora |
| Agent_group falha | Sistema detecta (signal), diagnostica (log), adapta (retry/reroute) |
| Complexidade >= 70% | Ativar review chain 3-tier (implementer-spec-quality) |
| Novo dominio de negocio | Instanciar agent_group com PRIME + mental_model + agentes |

## Anti-Patterns

- Orquestrador executando codigo, pesquisa ou copy (perde visao global)
- Agent_group acessando dominio de outro agent_group (viola separacao)
- Sistema sem pool de conhecimento (sem bootstrapping, sem melhoria)
- Agentes sem ISO files (sem identidade, execucao inconsistente)
- Handoffs sem scope fence (agent_group toca o que nao deve)

## Code

<!-- lang: python | purpose: cortex orchestrator dispatch -->
```python
cortex = CortexEnterprise(
    orchestrator="stella",
    agent_groups=["shaka", "lily", "edison", "pytha", "atlas", "york"],
    pool=KnowledgePool(count=1957),
)
# CLARIFY: decompose user request
tasks = cortex.clarify(user_input)
# ENRICH: brain_query per agent_group
for task in tasks:
    task.context = cortex.enrich(task.agent_group, task.keywords)
# COMPOSE: write structured handoffs
handoffs = cortex.compose(tasks)
# EXECUTE: dispatch to agent_groups
cortex.dispatch(handoffs)
# MONITOR: check signals, consolidate
cortex.monitor(timeout=300)
```

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_agent_group_concept
- related: p01_kc_cex_pipeline_execution

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_stella_dispatch]] | downstream | 0.45 |
| [[p01_kc_cex_agent_group_concept]] | sibling | 0.40 |
| [[bld_collaboration_agent_card]] | downstream | 0.29 |
| [[p03_pt_agent_group_orchestrator]] | downstream | 0.29 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.28 |
| [[bld_knowledge_card_handoff]] | sibling | 0.28 |
| [[p01_kc_handoff]] | sibling | 0.26 |
| [[bld_knowledge_card_agent_card]] | sibling | 0.26 |
| [[agent-card-builder]] | downstream | 0.24 |
| [[p12_crew_agent_group_grid]] | downstream | 0.23 |
