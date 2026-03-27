---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of satellite_spec — inventory, dependencies, and architectural position
---

# Architecture: satellite_spec in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 24-field metadata header (id, kind, pillar, domain, model, mcps, etc.) | satellite-spec-builder | active |
| role_definition | Primary domain and responsibility of the satellite | author | active |
| model_config | LLM model selection with provider and parameters | author | active |
| mcp_servers | List of MCP servers the satellite connects to at boot | author | active |
| boot_sequence | Ordered steps for satellite initialization | author | active |
| constraints | Resource limits, domain boundaries, and prohibited actions | author | active |
| dispatch_rules | How tasks are routed to this satellite based on keywords | author | active |
| monitoring | Health checks, signal emission, and observability configuration | author | active |

## Dependency Graph

```
router          --dispatches_to-->  satellite_spec  --configures-->  agent
spawn_config    --launches-->       satellite_spec  --depends-->     mcp_server
satellite_spec  --signals-->        health_status
```

| From | To | Type | Data |
|------|----|------|------|
| router (P02) | satellite_spec | data_flow | task dispatched to satellite based on routing rules |
| spawn_config (P12) | satellite_spec | dependency | launch configuration for terminal spawn |
| satellite_spec | agent (P02) | produces | satellite instantiates agents within its domain |
| satellite_spec | mcp_server (P04) | dependency | satellite requires specific MCP servers at runtime |
| satellite_spec | health_status (P12) | signals | periodic health and availability signals |
| model_card (P02) | satellite_spec | dependency | model specifications inform model_config selection |

## Boundary Table

| satellite_spec IS | satellite_spec IS NOT |
|-------------------|----------------------|
| A complete specification of an autonomous satellite | An individual agent identity (agent P02) |
| Defines model, MCPs, boot sequence, and constraints | A boot configuration for one provider (boot_config P02) |
| Scoped to a domain with dispatch rules and monitoring | A reusable architecture solution (pattern P08) |
| Includes resource limits and prohibited actions | An inviolable operational rule (law P08) |
| Configures observability with health checks and signals | A visual architecture representation (diagram P08) |
| Documents the full satellite as a deployable unit | An inventory of generic system components (component_map P08) |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | frontmatter, role_definition | Satellite name, domain, and primary responsibility |
| Configuration | model_config, mcp_servers, boot_sequence | Model, tools, and initialization procedure |
| Governance | constraints, dispatch_rules | Domain boundaries and task routing criteria |
| Operations | monitoring, health_status | Health checks and observability |
| Integration | router, spawn_config, agent | How the satellite is launched and receives work |
