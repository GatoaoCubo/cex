---
kind: architecture
id: bld_architecture_daemon
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of daemon — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Daemon"
version: "1.0.0"
author: n03_builder
tags: [daemon, builder, examples]
tldr: "Golden and anti-examples for daemon construction, demonstrating ideal structure and common pitfalls."
domain: "daemon construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_daemon
  - daemon-builder
  - p04_daemon_autonomous
  - p01_kc_daemon
  - p03_sp_daemon_builder
  - bld_output_template_daemon
  - bld_tools_daemon
  - bld_examples_daemon
  - p11_qg_daemon
  - bld_schema_daemon
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| process_definition | Core body: command, args, working_dir, user | daemon-builder | required |
| schedule | When to run: cron expression or `continuous` | daemon-builder | required |
| restart_policy | What to do on failure: always/on-failure/never + max_retries | daemon-builder | required |
| signal_handlers | How to react to OS signals: SIGTERM, SIGINT, SIGHUP | daemon-builder | required |
| pid_file | Path for PID tracking, prevents duplicate instances | daemon-builder | required |
| health_check | Periodic probe: command + interval + timeout + retries | daemon-builder | required |
| resource_limits | CPU and memory caps: max_cpu_percent, max_memory_mb | daemon-builder | optional |
| log_config | Log destination, rotation policy, retention | daemon-builder | required |
| monitoring | Metrics endpoint, alert thresholds, heartbeat interval | daemon-builder | optional |
| graceful_shutdown | Shutdown command + timeout before SIGKILL | daemon-builder | required |
## Dependency Graph
```
env_config (P09) --provides--> daemon (reads vars, paths, secrets at startup)
runtime_rule (P09) --constrains--> daemon (timeout, resource limits, retry bounds)
guardrail (P11) --bounds--> daemon (circuit breakers, safety boundaries)
daemon --produces--> signal (P12) (heartbeat, completion, error events)
daemon --consumed_by--> workflow (P12) (workflow may gate on daemon liveness)
daemon --may_wrap--> connector (P04) (daemon runs connector sync loop continuously)
daemon --may_wrap--> client (P04) (daemon polls external API via client)
daemon --writes--> log_config (own log sink)
health_check --monitors--> daemon (probes liveness)
```
| From | To | Type | Data |
|------|----|------|------|
| env_config | daemon | depends | config vars, secrets, paths |
| runtime_rule | daemon | constrains | timeout, retry, resource limits |
| guardrail | daemon | bounds | circuit breaker thresholds |
| daemon | signal | produces | heartbeat, error, completion events |
| daemon | workflow | consumed_by | liveness gate for dependent steps |
| daemon | connector | wraps | continuous sync loop |
| daemon | client | wraps | periodic API poll |
## Boundary Table
| daemon IS | daemon IS NOT |
|-----------|---------------|
| A persistent background process that runs continuously or on schedule | A hook — hooks fire once per event and exit |
| Self-managed: owns restart, PID, graceful shutdown | A skill — skills are invoked on demand with phases |
| Responds to OS signals (SIGTERM, SIGINT, SIGHUP) | A cli_tool — cli tools execute and exit immediately |
| Monitored by health checks with liveness probes | A workflow — workflows orchestrate multi-step sequences |
| Runs independently of user interaction | A connector — connectors define integration specs, not lifecycle |
| Has resource limits and log rotation | A plugin — plugins are composable extensions, not standalone processes |
| Produces heartbeat signals to the runtime | An mcp_server — mcp_server exposes tools via protocol, daemon is generic process |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Configuration | env_config, runtime_rule | Provide vars, limits, and constraints at startup |
| Safety | guardrail | Enforce circuit breakers and resource boundaries |
| Runtime | process_definition, schedule, restart_policy, pid_file | Define what runs, when, and how it recovers |
| Self-management | signal_handlers, graceful_shutdown, health_check | Handle OS signals, probes, and clean termination |
| Observability | log_config, monitoring | Capture logs, metrics, and alert thresholds |
| Output | signal | Emit heartbeat and status events to the broader system |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_daemon]] | downstream | 0.69 |
| [[daemon-builder]] | upstream | 0.65 |
| [[p04_daemon_autonomous]] | upstream | 0.55 |
| [[p01_kc_daemon]] | upstream | 0.53 |
| [[p03_sp_daemon_builder]] | upstream | 0.52 |
| [[bld_output_template_daemon]] | upstream | 0.52 |
| [[bld_tools_daemon]] | upstream | 0.48 |
| [[bld_examples_daemon]] | upstream | 0.46 |
| [[p11_qg_daemon]] | downstream | 0.46 |
| [[bld_schema_daemon]] | upstream | 0.45 |
