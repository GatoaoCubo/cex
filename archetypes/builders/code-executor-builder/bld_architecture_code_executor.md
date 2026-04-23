---
kind: architecture
id: bld_architecture_code_executor
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of code_executor — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Code Executor"
version: "1.0.0"
author: n03_builder
tags: [code_executor, builder, examples]
tldr: "Golden and anti-examples for code executor construction, demonstrating ideal structure and common pitfalls."
domain: "code executor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_code_executor_builder
  - code-executor-builder
  - p01_kc_code_executor
  - bld_examples_code_executor
  - bld_collaboration_code_executor
  - p11_qg_code_executor
  - bld_instruction_code_executor
  - bld_knowledge_card_code_executor
  - bld_output_template_code_executor
  - bld_schema_code_executor
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
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Agent runs shell command | code_executor | cli_tool | cli_tool=single cmd; executor=arbitrary code in sandbox |
| Background process runs code | code_executor | daemon | daemon persists; executor is ephemeral per call |
| LLM calls a function | code_executor | function_def | function_def=schema; executor=actual runtime |
## Decision Tree
- Untrusted code in sandbox? → code_executor
- Single shell command? → cli_tool
- Persistent background job? → daemon
- JSON Schema for tool_use? → function_def
## Neighbor Comparison
| Dimension | code_executor | cli_tool | Difference |
|---|---|---|---|
| Isolation | Sandbox (Docker/E2B) | Host shell | Executor has security boundary |
| Input | Arbitrary code string | Command + flags | Executor runs multi-line programs |
| Lifetime | Ephemeral + teardown | Ephemeral | Sandbox adds setup/teardown cost |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_code_executor_builder]] | upstream | 0.64 |
| [[code-executor-builder]] | upstream | 0.63 |
| [[p01_kc_code_executor]] | upstream | 0.48 |
| [[bld_examples_code_executor]] | upstream | 0.46 |
| [[bld_collaboration_code_executor]] | downstream | 0.46 |
| [[p11_qg_code_executor]] | downstream | 0.45 |
| [[bld_instruction_code_executor]] | upstream | 0.43 |
| [[bld_knowledge_card_code_executor]] | upstream | 0.43 |
| [[bld_output_template_code_executor]] | upstream | 0.41 |
| [[bld_schema_code_executor]] | upstream | 0.40 |
