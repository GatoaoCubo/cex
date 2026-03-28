---
kind: architecture
id: bld_architecture_boot_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of boot_config — inventory, dependencies, and architectural position
---

# Architecture: boot_config in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 15 required + 7 recommended fields (id, kind, pillar, provider, model, version, etc.) | boot-config-builder | required |
| provider_block | Target runtime identifier (claude, cursor, codex, openai, etc.) | author | required |
| identity_block | Agent name, role, and satellite assignment for this initialization | author | required |
| model_selection | Specific model ID and version to load (references model_card) | model_card | required |
| constraints_block | Token limits, context window, timeout, retries, max_turns | author | required |
| tools_block | Ordered list of tools and MCPs available on this provider runtime | author | required |
| permissions_block | Allowed and denied operations scoped to this provider | author | required |
| flags_block | Provider-specific CLI flags and startup options (e.g., --dangerously-skip-permissions) | author | optional |
| mcp_config | MCP server configurations and connection parameters | author | optional |

## Dependency Graph

```
model_card   --produces-->  boot_config  --produces_for-->  spawn_config
agent        --produces-->  boot_config  --consumed_by-->   workflow
system_prompt --depends-->  boot_config
boot_config  --signals-->   agent_instance (initialized and ready)
boot_config  --depends-->   provider_runtime (must exist before boot)
```

| From | To | Type | Data |
|------|----|------|------|
| model_card (P02) | boot_config | data_flow | LLM ID, capabilities, context window, cost per token |
| agent (P02) | boot_config | data_flow | identity to initialize (name, role, satellite) |
| system_prompt (P03) | boot_config | depends | persona reference loaded during initialization sequence |
| boot_config | spawn_config (P12) | produces | runtime parameters consumed by orchestration spawner |
| boot_config | workflow (P12) | data_flow | initialization step in orchestrated agent lifecycle |
| boot_config | agent_instance | signals | agent becomes executable after boot_config is applied |
| provider_runtime | boot_config | depends | provider must exist for the config to be valid |

## Boundary Table

| boot_config IS | boot_config IS NOT |
|----------------|-------------------|
| Provider-specific initialization for one agent on one runtime | The agent definition itself (agent) |
| A technical config mapping agent identity to provider parameters | A description of LLM capabilities or costs (model_card) |
| Scoped to a single provider (one boot_config per provider per agent) | Environment variables for the whole system (env_config) |
| The bridge between agent definition and executable instance | Orchestration logic for spawning multiple agents (spawn_config) |
| Editable and versioned — tuned per provider and deployment | An immutable fundamental truth (axiom) |
| Consumed at initialization time, not at task execution time | A routing rule or fallback sequence (router, fallback_chain) |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Inputs | model_card, agent, system_prompt | Supply LLM spec, agent identity, and persona reference |
| Identity | identity_block, provider_block | Bind agent identity to a specific provider runtime |
| Configuration | model_selection, constraints_block, flags_block | Set model, token limits, timeouts, and CLI options |
| Capabilities | tools_block, permissions_block, mcp_config | Define what the agent can do and access on this provider |
| Outputs | spawn_config feed, workflow step, agent_instance | Enable orchestrated spawning and produce executable agent |
