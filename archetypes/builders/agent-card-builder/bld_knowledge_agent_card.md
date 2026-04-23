---
kind: knowledge_card
id: bld_knowledge_card_agent_card
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for agent_card production — atomic searchable facts
sources: agent-card-builder MANIFEST.md + SCHEMA.md, microservices architecture, multi-agent systems
quality: 9.1
title: "Knowledge Card Agent Card"
version: "1.0.0"
author: n03_builder
tags: [agent_card, builder, examples]
tldr: "Golden and anti-examples for agent card construction, demonstrating ideal structure and common pitfalls."
domain: "agent card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_agent_card
  - bld_memory_agent_card
  - agent-card-builder
  - p03_ins_agent_card_builder
  - p11_qg_agent-card
  - p03_sp_agent_card_builder
  - bld_architecture_agent_card
  - bld_collaboration_spawn_config
  - bld_architecture_spawn_config
  - dispatch-rule-builder
---

# Domain Knowledge: agent_card
## Executive Summary
Agent_group specs define autonomous processing units in multi-agent architectures — each spec declares one agent_group's domain, LLM model, MCP servers, boot sequence, constraints, and dispatch keywords. Each agent_group owns ONE domain with no cross-domain responsibilities. They differ from agents (individual entities inside a agent_group), boot configs (how to start a provider), patterns (abstract reusable solutions), and spawn configs (runtime launch parameters) by being the complete architectural specification of what a agent_group IS and what it does.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| Kind | `agent_card` (exact literal) |
| ID pattern | `p08_ac_{slug}` |
| Required frontmatter | 24+ fields |
| Quality gates | 10 HARD + 10 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Key fields | role, model, mcps, domain, boot_sequence, dispatch_keywords |
| Scaling limit | Max 3 concurrent + orchestrator (BSOD at >4) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Single domain ownership | Each agent_group owns ONE domain; no cross-domain responsibilities |
| Model-to-task matching | opus for reasoning-heavy; sonnet for speed/volume |
| MCP as tool interface | MCP servers are the agent_group's external tool access |
| Ordered boot sequence | Idempotent, ordered initialization steps |
| Constraints as boundaries | Define what agent_group CANNOT do, not aspirations |
| Dispatch keywords as contract | Routing contract with orchestrator; concrete nouns/verbs |
| Explicit dependencies | No hidden couplings between agent_groups |
| Signal-based monitoring | Signal on complete/failure enables autonomous recovery |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Cross-domain responsibilities | Violates single-domain principle; creates coupling |
| Missing boot sequence | Cannot reliably start or recover the agent_group |
| No dispatch keywords | Orchestrator cannot route tasks to this agent_group |
| Constraints section empty | No boundaries = scope creep inevitable |
| > 4 concurrent agent_groups | Resource exhaustion; system instability |
| Hidden dependencies | Undeclared coupling causes cascade failures |
| No monitoring/signal config | Cannot detect completion or failure |
## Application
1. Define agent_group role and domain (ONE domain only)
2. Select LLM model matching task complexity
3. List MCP servers with config file path
4. Define ordered, idempotent boot sequence
5. Set constraints (what agent_group CANNOT do)
6. Define dispatch keywords (routing contract)
7. Specify scaling limits and monitoring config
8. Document dependencies explicitly
9. Validate: 10 HARD + 10 SOFT gates, body <= 4096 bytes
## References
- agent-card-builder SCHEMA.md v1.0.0
- Newman, Sam. Building Microservices (2015)
- Wooldridge, Michael. Introduction to MultiAgent Systems (2009)
- Kubernetes Pod Specification (resource limits, health checks)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent_card]] | downstream | 0.52 |
| [[bld_memory_agent_card]] | downstream | 0.50 |
| [[agent-card-builder]] | downstream | 0.47 |
| [[p03_ins_agent_card_builder]] | downstream | 0.44 |
| [[p11_qg_agent-card]] | downstream | 0.42 |
| [[p03_sp_agent_card_builder]] | downstream | 0.38 |
| [[bld_architecture_agent_card]] | downstream | 0.35 |
| [[bld_collaboration_spawn_config]] | downstream | 0.32 |
| [[bld_architecture_spawn_config]] | downstream | 0.29 |
| [[dispatch-rule-builder]] | downstream | 0.29 |
