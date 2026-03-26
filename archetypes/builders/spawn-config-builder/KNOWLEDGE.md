---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for spawn_config production
sources: CODEXA spawn system, Claude Code CLI, PowerShell automation
---

# Domain Knowledge: spawn_config

## Foundational Concept
Spawn configuration defines HOW a satellite process is launched — what CLI flags,
model, MCP servers, timeout, and interaction mode to use. In CODEXA, satellites are
Claude Code instances spawned via PowerShell scripts (spawn_solo.ps1, spawn_grid.ps1)
that read spawn_config to determine execution parameters.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Docker Compose | Service definition with resources/networking | Analogous: our satellite definition |
| Kubernetes Pod Spec | Container config with resources/probes | Similar: flags, timeout, health |
| Claude Code CLI | --model, --mcp-config, -p flags | Direct: our flags list |
| PM2 ecosystem | Process manager config (instances, env) | Similar: mode, restart policy |

## Key Patterns
- Baseline flags: --dangerously-skip-permissions + --no-chrome mandatory for all spawns
- Non-interactive flag: -p skips workspace trust prompt (critical for automation)
- Prompt sizing: inline < 200 chars, handoff file for longer tasks
- MCP isolation: per-satellite .mcp-{sat}.json prevents tool leakage
- Timeout budgeting: research ~30min, build ~45min, deploy ~15min
- Interactive mode: /k keeps terminal open for monitoring and debugging
- Grid concurrency: max 3 satellites + STELLA to prevent BSOD

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| mode | solo/grid/continuous dispatch modes | Docker Compose profiles |
| prompt_strategy | inline vs handoff file | No direct equivalent |
| mcp_config | Per-satellite MCP server isolation | Docker network isolation |
| interactive | Terminal persistence for monitoring | Docker -it flag |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT spawn_config |
|------|------------|---------------------------|
| boot_config (P02) | Per-provider LLM initialization (temperature, tokens) | Boot is LLM-level, spawn is process-level |
| env_config (P09) | Environment variables (API keys, paths) | Env vars are runtime state, not spawn params |
| handoff (P12) | Task instructions with context and commit | Handoff is WHAT to do, spawn_config is HOW to launch |
| dispatch_rule (P12) | Keyword-to-satellite routing logic | Dispatch decides WHO, spawn_config decides HOW |

## References
- CODEXA: records/framework/powershell/spawn_solo.ps1
- CODEXA: records/framework/powershell/spawn_grid.ps1
- Claude Code: claude --help (CLI flags reference)
