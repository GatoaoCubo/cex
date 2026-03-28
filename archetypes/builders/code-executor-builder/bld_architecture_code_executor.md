---
kind: architecture
id: bld_architecture_code_executor
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of code_executor — inventory, dependencies, and architectural position
---

# Architecture: code_executor
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| runtime | Primary language runtime (python, node, etc.) | code_executor | required |
| sandbox_type | Isolation mechanism (docker, e2b, wasm, vm, process) | code_executor | required |
| languages | Supported programming languages with versions | code_executor | required |
| timeout | Maximum execution time per invocation | code_executor | required |
| resource_limits | CPU, memory, disk constraints | code_executor | recommended |
| network_access | Network connectivity policy | code_executor | recommended |
| file_io | File system access policy | code_executor | recommended |
| persistent_session | State persistence between calls | code_executor | recommended |
| agent | Runtime caller that submits code for execution | P02 | consumer |
| function_def | Interface definition that may target this executor | P04 | consumer |
## Dependency Graph
```
sandbox_type --provides-->  isolation (security boundary)
runtime      --provides-->  language_support
languages    --constrains-> code (what can execute)
timeout      --constrains-> execution (kill after N seconds)
resource_limits --constrains-> execution (CPU, memory caps)
agent        --submits-->   code_executor (code to run)
function_def --targets-->   code_executor (runtime binding)
```
| From | To | Type | Data |
|------|----|------|------|
| sandbox_type | isolation | provides | Security boundary (docker, e2b, etc.) |
| runtime | language_support | provides | Available language runtimes |
| languages | code | constrains | What languages can execute |
| timeout | execution | constrains | Max time before kill |
| resource_limits | execution | constrains | CPU, memory, disk caps |
| agent | code_executor | submits | Code string for execution |
| function_def | code_executor | targets | Runtime binding for function |
## Boundary Table
| code_executor IS | code_executor IS NOT |
|-----------------|---------------------|
| An isolated sandbox for running untrusted code | A terminal command (that is cli_tool) |
| Ephemeral or persistent execution environment | A background daemon process (that is daemon) |
| Defined by language support and resource limits | A protocol server (that is mcp_server) |
| Invoked by agents to execute generated code | An API client (that is api_client) |
| Time-bounded with mandatory timeout | A JSON Schema interface (that is function_def) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| isolation | sandbox_type | Define security boundary |
| runtime | runtime, languages | What code can execute |
| limits | timeout, resource_limits | Constrain execution resources |
| access | network_access, file_io | Control external access |
| state | persistent_session | Manage execution state |
| consumers | agent, function_def | Runtime callers |
