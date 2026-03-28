---
kind: architecture
id: bld_architecture_hook
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of hook — inventory, dependencies, and architectural position
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
