---
kind: architecture
id: bld_architecture_spawn_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of spawn_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Spawn Config"
version: "1.0.0"
author: n03_builder
tags: [spawn_config, builder, examples]
tldr: "Golden and anti-examples for spawn config construction, demonstrating ideal structure and common pitfalls."
domain: "spawn config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Architecture: spawn_config in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 19-field metadata header (id, kind, pillar, domain, mode, agent_group, etc.) | spawn-config-builder | active |
| mode_config | Spawn mode selection: solo, grid, or continuous | author | active |
| cli_flags | Command-line flags for the spawn process (model, mcp-config, permissions) | author | active |
| mcp_profile | Path to MCP configuration file for the agent_group | author | active |
| timeout_policy | Maximum execution time and idle timeout for the spawned agent_group | author | active |
| handoff_reference | Path to the handoff file the agent_group should read at boot | author | active |
| agent_group_model_pair | Which agent_group runs on which LLM model | author | active |
## Dependency Graph
```
orchestrator    --creates-->    spawn_config  --consumed_by-->  spawn_script
agent_card  --informs-->    spawn_config  --produces-->     terminal_process
spawn_config    --signals-->    spawn_event
```
| From | To | Type | Data |
|------|----|------|------|
| orchestrator | spawn_config | produces | orchestrator generates config for agent_group launch |
| agent_card (P08) | spawn_config | dependency | agent_group spec informs model and MCP selection |
| spawn_config | spawn_script (PowerShell) | consumes | script reads config to launch terminal process |
| spawn_config | terminal_process | produces | running agent_group instance in a terminal |
| spawn_config | spawn_event (P12) | signals | emitted when agent_group is spawned or fails to start |
| handoff (P12) | spawn_config | dependency | handoff file referenced by spawn for task instructions |
## Boundary Table
| spawn_config IS | spawn_config IS NOT |
|-----------------|---------------------|
| A configuration for launching agent_groups via scripts | A runtime signal between agent_groups (signal P12) |
| Specifies mode (solo/grid/continuous), flags, and timeouts | A task routing rule (dispatch_rule P12) |
| References handoff files and MCP profiles | A multi-step orchestration flow (workflow P12) |
| Pairs agent_groups with LLM models | A full agent_group specification (agent_card P08) |
| Consumed by PowerShell spawn scripts | An agent identity or persona (agent P02) |
| Scoped to one launch event or mission | A persistent runtime configuration (runtime_rule P09) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | orchestrator, agent_card | Supply launch requirements and agent_group specs |
| Configuration | frontmatter, mode_config, agent_group_model_pair | Define what mode and model to use |
| Parameters | cli_flags, mcp_profile, timeout_policy | Specify technical launch parameters |
| Task | handoff_reference | Link to the task the agent_group should execute |
| Execution | spawn_script, terminal_process, spawn_event | Launch the agent_group and signal the event |
