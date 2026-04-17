# P04 Tools — N07 Admin

> Orchestrating Sloth · dispatch tools, monitors, orchestration CLIs

## Scope in N07
External capabilities the orchestrator uses: spawn scripts, signal
watchers, PID trackers, wave schedulers, consolidation runners.
Sloth wants every repetitive action automated — tools here exist
so N07 never has to type the same thing twice.

## Kinds that live here
- `cli_tool` — orchestration CLI wrappers (`dispatch.sh`, `cex_mission_runner.py`)
- `webhook` — signal/completion endpoints
- `mcp_server` — MCP servers for orchestration (GitHub, Slack notifiers)
- `api_client` — clients for observability (metrics, traces)

## Related
- `orchestration/` — workflows and dispatch rules these tools execute
- `../_spawn/` — dispatch shell layer (repo-root spawn scripts)
- `../_tools/` — the `cex_*.py` toolchain (152 CLIs)
