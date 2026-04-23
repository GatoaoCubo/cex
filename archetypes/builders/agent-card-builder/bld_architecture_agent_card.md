---
kind: architecture
id: bld_architecture_agent_card
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of agent_card — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Agent Card"
version: "1.0.0"
author: n03_builder
tags: [agent_card, builder, examples]
tldr: "Golden and anti-examples for agent card construction, demonstrating ideal structure and common pitfalls."
domain: "agent card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - agent-card-builder
  - bld_collaboration_agent_card
  - bld_architecture_spawn_config
  - bld_knowledge_card_agent_card
  - p03_ins_agent_card_builder
  - p03_sp_agent_card_builder
  - bld_memory_agent_card
  - p11_qg_agent-card
  - bld_architecture_workflow
  - p01_kc_agent_card
---

# Architecture: agent_card in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 24-field metadata header (id, kind, pillar, domain, model, mcps, etc.) | agent-card-builder | active |
| role_definition | Primary domain and responsibility of the agent_group | author | active |
| model_config | LLM model selection with provider and parameters | author | active |
| mcp_servers | List of MCP servers the agent_group connects to at boot | author | active |
| boot_sequence | Ordered steps for agent_group initialization | author | active |
| constraints | Resource limits, domain boundaries, and prohibited actions | author | active |
| dispatch_rules | How tasks are routed to this agent_group based on keywords | author | active |
| monitoring | Health checks, signal emission, and observability configuration | author | active |
## Dependency Graph
```
router          --dispatches_to-->  agent_card  --configures-->  agent
spawn_config    --launches-->       agent_card  --depends-->     mcp_server
agent_card  --signals-->        health_status
```
| From | To | Type | Data |
|------|----|------|------|
| router (P02) | agent_card | data_flow | task dispatched to agent_group based on routing rules |
| spawn_config (P12) | agent_card | dependency | launch configuration for terminal spawn |
| agent_card | agent (P02) | produces | agent_group instantiates agents within its domain |
| agent_card | mcp_server (P04) | dependency | agent_group requires specific MCP servers at runtime |
| agent_card | health_status (P12) | signals | periodic health and availability signals |
| model_card (P02) | agent_card | dependency | model specifications inform model_config selection |
## Boundary Table
| agent_card IS | agent_card IS NOT |
|-------------------|----------------------|
| A complete specification of an autonomous agent_group | An individual agent identity (agent P02) |
| Defines model, MCPs, boot sequence, and constraints | A boot configuration for one provider (boot_config P02) |
| Scoped to a domain with dispatch rules and monitoring | A reusable architecture solution (pattern P08) |
| Includes resource limits and prohibited actions | An inviolable operational rule (law P08) |
| Configures observability with health checks and signals | A visual architecture representation (diagram P08) |
| Documents the full agent_group as a deployable unit | An inventory of generic system components (component_map P08) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | frontmatter, role_definition | Agent_group name, domain, and primary responsibility |
| Configuration | model_config, mcp_servers, boot_sequence | Model, tools, and initialization procedure |
| Governance | constraints, dispatch_rules | Domain boundaries and task routing criteria |
| Operations | monitoring, health_status | Health checks and observability |
| Integration | router, spawn_config, agent | How the agent_group is launched and receives work |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-card-builder]] | related | 0.52 |
| [[bld_collaboration_agent_card]] | related | 0.50 |
| [[bld_architecture_spawn_config]] | sibling | 0.48 |
| [[bld_knowledge_card_agent_card]] | upstream | 0.42 |
| [[p03_ins_agent_card_builder]] | upstream | 0.41 |
| [[p03_sp_agent_card_builder]] | upstream | 0.40 |
| [[bld_memory_agent_card]] | downstream | 0.39 |
| [[p11_qg_agent-card]] | downstream | 0.37 |
| [[bld_architecture_workflow]] | sibling | 0.34 |
| [[p01_kc_agent_card]] | related | 0.32 |
