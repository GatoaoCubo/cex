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
tldr: "Cortex Enterprise is a modular enterprise brain: cognitive CEO (routes, never executes) + N verticalized agent_groups + emergent properties"
when_to_use: "Understand multi-agent system architecture with central orchestrator and autonomous departments"
keywords: [cortex-enterprise, orchestrator, ceo, brain, modular-architecture]
long_tails:
  - "How to build an enterprise brain with LLMs and specialized agents"
  - "What is the role of the central orchestrator in a multi-agent system"
axioms:
  - "ALWAYS orchestrator routes, NEVER executes"
  - "NEVER agent_group depends on another agent_group to complete a task"
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

Cortex Enterprise is a modular enterprise brain based on LLM. Architecture: central orchestrator (cognitive CEO) that routes but NEVER executes + N verticalized agent_groups with full autonomy in their domain. Each organization instantiates its Cortex[X]. Organization is the reference implementation with 7 agent_groups and 284 agents. The system exhibits 5 emergent properties: bootstrapping, metacircularity, cognitive scaffolding, fractal architecture, and distributed self-correction.

## Spec

| Component | Function | Rule |
|-----------|----------|------|
| Orchestrator | CLARIFY-ENRICH-COMPOSE-EXECUTE-MONITOR | Routes, never executes |
| Agent_groups (6 exec) | Verticalized departments | 1 domain = 1 agent_group |
| Agents (284 total) | Specialized workers | ISO files define execution |
| Handoffs | Structured dispatch | Context + seeds + scope fence |
| Signals | Inter-agent_group communication | JSON with status + score |
| Pool (1957 KCs) | Institutional memory | Indexed knowledge cards |

Emergent properties of the instantiated Cortex:

| Property | Mechanism | Reference |
|----------|-----------|-----------|
| Bootstrapping | KCs alimentam agentes que geram KCs melhores | GCC self-hosting (1980s) |
| Metacircularidade | Agentes descrevem propria execucao via ISO | SICP eval (Abelson 1996) |
| Scaffolding cognitivo | Handoffs direcionam sem sobrecarregar contexto | Vygotsky ZPD (1978) |
| Arquitetura fractal | 12 LPs repetem em 4 niveis (prompt-agent-sat-sys) | Mandelbrot (1982) |
| Auto-correcao distribuida | Review chain 3-tier entre entidades independentes | Reflexion (Shinn 2023) |

Orchestrator dispatch cycle (5 phases):

| Phase | Input | Output |
|-------|-------|--------|
| CLARIFY | User request | Task table by agent_group |
| ENRICH | Keywords per task | Context via brain_query |
| COMPOSE | Tasks + context | Handoff .md per agent_group |
| EXECUTE | Handoffs | Agent_groups in parallel execution |
| MONITOR | Signals + git log | Consolidated report |

## Patterns

| Trigger | Action |
|---------|--------|
| Multi-domain task | Orchestrator decomposes into waves by agent_group |
| New knowledge generated | Agent produces KC, pool indexes, search improves |
| Agent_group fails | System detects (signal), diagnoses (log), adapts (retry/reroute) |
| Complexity >= 70% | Activate 3-tier review chain (implementer-spec-quality) |
| New business domain | Instantiate agent_group with PRIME + mental_model + agents |

## Anti-Patterns

- Orchestrator executing code, research, or copy (loses global view)
- Agent_group accessing another agent_group's domain (violates separation)
- System without knowledge pool (no bootstrapping, no improvement)
- Agents without ISO files (no identity, inconsistent execution)
- Handoffs without scope fence (agent_group touches what it should not)

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
