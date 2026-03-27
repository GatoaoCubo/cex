---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of spawn_config — inventory, dependencies, and architectural position
---

# Architecture: spawn_config in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 19-field metadata header (id, kind, pillar, domain, mode, satellite, etc.) | spawn-config-builder | active |
| mode_config | Spawn mode selection: solo, grid, or continuous | author | active |
| cli_flags | Command-line flags for the spawn process (model, mcp-config, permissions) | author | active |
| mcp_profile | Path to MCP configuration file for the satellite | author | active |
| timeout_policy | Maximum execution time and idle timeout for the spawned satellite | author | active |
| handoff_reference | Path to the handoff file the satellite should read at boot | author | active |
| satellite_model_pair | Which satellite runs on which LLM model | author | active |

## Dependency Graph

```
orchestrator    --creates-->    spawn_config  --consumed_by-->  spawn_script
satellite_spec  --informs-->    spawn_config  --produces-->     terminal_process
spawn_config    --signals-->    spawn_event
```

| From | To | Type | Data |
|------|----|------|------|
| orchestrator | spawn_config | produces | orchestrator generates config for satellite launch |
| satellite_spec (P08) | spawn_config | dependency | satellite spec informs model and MCP selection |
| spawn_config | spawn_script (PowerShell) | consumes | script reads config to launch terminal process |
| spawn_config | terminal_process | produces | running satellite instance in a terminal |
| spawn_config | spawn_event (P12) | signals | emitted when satellite is spawned or fails to start |
| handoff (P12) | spawn_config | dependency | handoff file referenced by spawn for task instructions |

## Boundary Table

| spawn_config IS | spawn_config IS NOT |
|-----------------|---------------------|
| A configuration for launching satellites via scripts | A runtime signal between satellites (signal P12) |
| Specifies mode (solo/grid/continuous), flags, and timeouts | A task routing rule (dispatch_rule P12) |
| References handoff files and MCP profiles | A multi-step orchestration flow (workflow P12) |
| Pairs satellites with LLM models | A full satellite specification (satellite_spec P08) |
| Consumed by PowerShell spawn scripts | An agent identity or persona (agent P02) |
| Scoped to one launch event or mission | A persistent runtime configuration (runtime_rule P09) |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Source | orchestrator, satellite_spec | Supply launch requirements and satellite specs |
| Configuration | frontmatter, mode_config, satellite_model_pair | Define what mode and model to use |
| Parameters | cli_flags, mcp_profile, timeout_policy | Specify technical launch parameters |
| Task | handoff_reference | Link to the task the satellite should execute |
| Execution | spawn_script, terminal_process, spawn_event | Launch the satellite and signal the event |
