---
kind: architecture
id: bld_architecture_hook
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of hook — inventory, dependencies, and architectural position
quality: 9.0
title: "Architecture Hook"
version: "1.0.0"
author: n03_builder
tags: [hook, builder, examples]
tldr: "Golden and anti-examples for hook construction, demonstrating ideal structure and common pitfalls."
domain: "hook construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - hook-builder
  - p03_sp_hook_builder
  - bld_instruction_hook
  - hook-config-builder
  - bld_collaboration_hook
  - bld_knowledge_card_hook
  - bld_schema_hook
  - p04_hook_NAME
  - bld_collaboration_hook_config
  - p11_qg_hook
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| trigger_config | Event type and timing (pre/post/both) that fires the hook | author | required |
| script_path | Executable script invoked when trigger fires | author | required |
| conditions | Boolean predicates that must pass before execution | author | optional |
| timeout_ms | Maximum allowed execution time before abort | author | required |
| blocking | Whether hook blocks the main event flow until completion | author | required |
| error_strategy | Behavior on failure: abort, warn, or ignore | author | required |
| env_injection | Environment variables passed into the hook script | author | optional |
| async_flag | Whether hook runs in background without blocking | author | optional |
## Dependency Graph
```
agent         --triggers--> hook
workflow      --triggers--> hook
spawn_config  --triggers--> hook
hook          --may_emit--> signal
hook          --may_call--> cli_tool
```
| From | To | Type | Data |
|------|----|------|------|
| agent | hook | data_flow | event type, tool name, session context |
| workflow | hook | data_flow | lifecycle event, step transition |
| spawn_config | hook | data_flow | session start/stop event |
| hook | signal | data_flow | execution result, status, metrics |
| hook | cli_tool | data_flow | invocation args, environment vars |
## Boundary Table
| hook IS | hook IS NOT |
|---------|-------------|
| Single-event interceptor with side effects | Policy declaration for long-term lifecycle |
| Fires once per event occurrence | Continuously running background process |
| Stateless reaction to a named event | Full system extension with its own API |
| Can be pre, post, or both for one event type | Structured workflow with named phases |
| Executes external script or command | Agent identity or behavioral definition |
| Optionally blocking or async | Data connector to external services |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Event binding | trigger_config, conditions | Define when the hook activates |
| Execution | script_path, timeout_ms, async_flag | Control how the hook runs |
| Safety | blocking, error_strategy | Govern impact on the main event flow |
| Context | env_injection | Supply runtime data to hook scripts |
| Reporting | signal | Communicate hook outcome downstream |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hook-builder]] | upstream | 0.56 |
| [[p03_sp_hook_builder]] | upstream | 0.56 |
| [[bld_instruction_hook]] | upstream | 0.55 |
| [[hook-config-builder]] | upstream | 0.54 |
| [[bld_collaboration_hook]] | downstream | 0.48 |
| [[bld_knowledge_card_hook]] | upstream | 0.47 |
| [[bld_schema_hook]] | upstream | 0.47 |
| [[p04_hook_NAME]] | upstream | 0.46 |
| [[bld_collaboration_hook_config]] | downstream | 0.46 |
| [[p11_qg_hook]] | downstream | 0.46 |
