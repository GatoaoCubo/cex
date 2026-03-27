---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of cli_tool — inventory, dependencies, and architectural position
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| command | Named invocation unit — the top-level verb the tool exposes | cli_tool | required |
| flag | Optional modifier altering command behavior (--verbose, --dry-run) | cli_tool | required |
| arg | Positional input value consumed by a command | cli_tool | required |
| output_format | Shape of stdout result (text, json, table, yaml) | cli_tool | required |
| exit_code | Numeric return value with defined semantic meaning | cli_tool | required |
| config_file | Optional file-based configuration source | cli_tool | optional |
| env_config | Environment variables that override defaults | P09 | external |
| guardrail | Execution constraints — timeouts, allowed paths, rate caps | P11 | external |
| agent | Runtime caller that invokes the tool via shell | P02 | consumer |
| hook | Event-driven caller that triggers the tool pre/post action | P04 | consumer |

## Dependency Graph

```
env_config   --produces--> command
config_file  --produces--> command
flag         --depends-->  command
arg          --depends-->  command
command      --produces--> output_format
command      --produces--> exit_code
guardrail    --depends-->  command
agent        --depends-->  command
hook         --depends-->  command
```

| From | To | Type | Data |
|------|----|------|------|
| env_config | command | produces | runtime overrides (API keys, paths) |
| config_file | command | produces | file-based configuration values |
| flag | command | depends | modifier affecting execution behavior |
| arg | command | depends | positional input for the command |
| command | output_format | produces | stdout result in specified format |
| command | exit_code | produces | numeric status code (0=ok, non-zero=error) |
| guardrail | command | depends | timeout and execution constraint policy |
| agent | command | depends | shell invocation from agent runtime |
| hook | command | depends | event-triggered shell invocation |

## Boundary Table

| cli_tool IS | cli_tool IS NOT |
|-------------|----------------|
| Invoked explicitly via terminal or shell call | A background process that persists (that is daemon) |
| Executes a single task then exits with a code | A reusable capability with defined phases (that is skill) |
| Input via args, flags, stdin; output via stdout/stderr | A pluggable extension to a host system (that is plugin) |
| Standalone executable — no host runtime required | An API consumer over HTTP (that is client) |
| Returns numeric exit code with semantic meaning | A tool exposed via MCP protocol (that is mcp_server) |
| One binary / script per distinct operation | A bidirectional service integration (that is connector) |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| configuration | env_config, config_file | Supply runtime values and path overrides |
| interface | command, flag, arg | Define the CLI surface — what callers can invoke |
| execution | output_format, exit_code | Shape result output and signal success or failure |
| governance | guardrail | Apply timeouts and execution constraints |
| callers | agent, hook | Runtime consumers that invoke the tool |
