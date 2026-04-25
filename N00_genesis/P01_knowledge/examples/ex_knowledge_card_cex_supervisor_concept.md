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
tldr: "Agent_group is an L4 entity that fills 12 LPs — complete department with identity, team, tools, memory and governance"
when_to_use: "Understand how to organize LLM agents into specialized departments with full autonomy"
keywords: [agent_group, department, specialization, vertical, agent-team]
long_tails:
  - "How to structure specialized LLM agent departments"
  - "What is the difference between agent and agent_group in CEX"
axioms:
  - "ALWAYS 1 agent_group = 1 domain = full autonomy"
  - "NEVER agent_group executes outside its domain"
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

Agent_group is the highest completeness entity in CEX (Level 4). Fills all 12 Lifecycle Positions: has identity (P02), knowledge (P01), instructions (P03), skills (P04), templates (P05), schemas (P06), tests (P07), architecture (P08), config (P09), memory (P10), learning (P11) and coordination (P12). Equivalent to a complete enterprise department with a team of 22-105 specialized agents.

## Spec

| Property | Value | Note |
|----------|-------|------|
| Level | L4 (maximum) | L1=prompt, L2=chain, L3=agent, L4=agent_group |
| LPs filled | 12/12 | Only entity with total coverage |
| Agents per agent_group | 22-105 | commercial_agent=22 (smallest), builder_agent=105 (largest) |
| Identity files | 2 | PRIME_{SAT}.md + mental_model.yaml |
| Boot time | 5-15s | Depends on loaded MCPs |
| Model | sonnet or opus | Opus for complex tasks (build, deploy) |
| MCPs | 1-3 per agent_group | Brain (universal) + specialized |
| Autonomy | Full within domain | Orchestrator does not interfere with execution |

Reference implementation (organization) — 7 agent_groups:

| Agent_group | Domain | Lens | Model | MCPs | Agents |
|-----------|--------|------|-------|------|--------|
| orchestrator | Orchestration | — | opus | brain+orch | 0 (routes) |
| research_agent | Research | Analytical Envy | sonnet | firecrawl+brain | 45 |
| marketing_agent | Marketing | Creative Lust | sonnet | markitdown+brain | 37 |
| builder_agent | Engineering | Inventive Pride | opus | brain | 105 |
| knowledge_agent | Knowledge | Knowledge Gluttony | sonnet | brain | 38 |
| operations_agent | Operations | Gating Wrath | opus | railway+pg+brain | 37 |
| commercial_agent | Revenue | Strategic Greed | sonnet | brain | 22 |

## Patterns

| Trigger | Action |
|---------|--------|
| Domain requires >10 agents | Create dedicated agent_group |
| Task crosses 2+ domains | Orchestrator decomposes into sub-tasks per agent_group |
| Agent_group needs fast boot | Minimize MCPs (each MCP = +2-5s) |
| Team grows above 50 agents | Subdivide with mental_model by specialty |
| New business domain emerges | Instantiate agent_group with PRIME + mental_model |

## Anti-Patterns

- Agent_group without PRIME.md (no identity = incoherent execution)
- Agent_group executing tasks of another domain (violates separation)
- Orchestrator executing instead of dispatching to agent_group
- Agent_group with 0 agents (empty container, no capability)
- Sharing MCPs between agent_groups (coupling, slow boot)

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
