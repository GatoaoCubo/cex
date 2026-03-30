---
kind: architecture
id: bld_architecture_spawn_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of spawn_config — inventory, dependencies, and architectural position
---

# Architecture: spawn_config in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 19-field metadata header (id, kind, pillar, domain, mode, agent_node, etc.) | spawn-config-builder | active |
| mode_config | Spawn mode selection: solo, grid, or continuous | author | active |
| cli_flags | Command-line flags for the spawn process (model, mcp-config, permissions) | author | active |
| mcp_profile | Path to MCP configuration file for the agent_node | author | active |
| timeout_policy | Maximum execution time and idle timeout for the spawned agent_node | author | active |
| handoff_reference | Path to the handoff file the agent_node should read at boot | author | active |
| agent_node_model_pair | Which agent_node runs on which LLM model | author | active |
## Dependency Graph
```
orchestrator    --creates-->    spawn_config  --consumed_by-->  spawn_script
agent_card  --informs-->    spawn_config  --produces-->     terminal_process
spawn_config    --signals-->    spawn_event
```
| From | To | Type | Data |
|------|----|------|------|
| orchestrator | spawn_config | produces | orchestrator generates config for agent_node launch |
| agent_card (P08) | spawn_config | dependency | agent_node spec informs model and MCP selection |
| spawn_config | spawn_script (PowerShell) | consumes | script reads config to launch terminal process |
| spawn_config | terminal_process | produces | running agent_node instance in a terminal |
| spawn_config | spawn_event (P12) | signals | emitted when agent_node is spawned or fails to start |
| handoff (P12) | spawn_config | dependency | handoff file referenced by spawn for task instructions |
## Boundary Table
| spawn_config IS | spawn_config IS NOT |
|-----------------|---------------------|
| A configuration for launching agent_nodes via scripts | A runtime signal between agent_nodes (signal P12) |
| Specifies mode (solo/grid/continuous), flags, and timeouts | A task routing rule (dispatch_rule P12) |
| References handoff files and MCP profiles | A multi-step orchestration flow (workflow P12) |
| Pairs agent_nodes with LLM models | A full agent_node specification (agent_card P08) |
| Consumed by PowerShell spawn scripts | An agent identity or persona (agent P02) |
| Scoped to one launch event or mission | A persistent runtime configuration (runtime_rule P09) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | orchestrator, agent_card | Supply launch requirements and agent_node specs |
| Configuration | frontmatter, mode_config, agent_node_model_pair | Define what mode and model to use |
| Parameters | cli_flags, mcp_profile, timeout_policy | Specify technical launch parameters |
| Task | handoff_reference | Link to the task the agent_node should execute |
| Execution | spawn_script, terminal_process, spawn_event | Launch the agent_node and signal the event |
