# Cross-Wave Cleanup Protocol

**Mandatory between every wave of /mission, /grid, /showoff, /batch, and any multi-spawn orchestration.**
If wave N leaves processes alive, wave N+1 gets resource contention, stale signals, and false "already running" guards.

## The 4 runtimes and their kill targets

| Runtime | Wrapper | Worker | Kill target |
|---------|---------|--------|-------------|
| claude | `powershell -File boot/n0X.ps1` | `claude.exe` + `node.exe` (MCP) | wrapper PID tree-kill |
| gemini | `powershell -File boot/n0X_gemini.ps1` | `node.exe` (no gemini.exe) | wrapper PID tree-kill + orphan node scan |
| codex | `powershell -File boot/n0X_codex.ps1` | `codex.exe` | wrapper PID tree-kill |
| ollama | `powershell -File boot/n0X_ollama.ps1` | `python.exe` (ollama_nucleus.py) | wrapper PID tree-kill |

**Never** use `Get-Process gemini` (returns empty) or filter by `MainWindowTitle` (truncates/lies).
**Always** use `Win32_Process.CommandLine` matching `boot/n0[1-7](_gemini|_codex|_ollama)?\.ps1`.

## Cleanup protocol (every between-wave gate)

```bash
bash _spawn/dispatch.sh stop             # MY session: PID file + CommandLine + orphan node
# optional surgical:
bash _spawn/dispatch.sh stop n03         # specific nucleus everywhere
bash _spawn/dispatch.sh stop --all       # everything including other N07 sessions
```

`spawn_stop.ps1` runs 3 passes internally:

1. **PID file scan** — session-filtered by `{sess}` column in `.cex/runtime/pids/spawn_pids.txt`
2. **CommandLine scan** — `Win32_Process` WHERE CommandLine LIKE `%boot/n0X_*.ps1%` (session-safe: skips pids tracked by other sessions)
3. **Orphan node scan** — `node.exe` with dead parent AND `CommandLine` mentioning `gemini|codex|@google|@openai` gets tree-killed

Each pass uses `taskkill /F /PID <id> /T` (tree-kill). `Stop-Process` does NOT tree-kill and will orphan children.

## Integration points

Every orchestrator that advances between waves MUST call the protocol:

| Orchestrator | Hook | Location |
|--------------|------|----------|
| `cex_mission_runner.py` | `between_wave_consolidate()` | end of each wave |
| `cex_showoff.py` | `between_wave_consolidate()` | `_tools/cex_showoff.py:201` |
| `cex_auto.py` | after cycle commits | `_tools/cex_auto.py` |
| `dispatch.sh swarm` | after all workers signal | `_spawn/spawn_swarm.sh` |

The between-wave function MUST:

1. Archive wave signals to `.cex/runtime/signals_archive/` (don't let them accumulate past ~50)
2. Commit stray artifacts under the wave's pillar/nucleus directory
3. Call `bash _spawn/dispatch.sh stop` (MY session only, NOT `--all`)
4. Verify zero wrappers survive: `Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Where CommandLine -match 'boot/n0'` returns empty
5. Report wave status (signals N/M, artifacts K, elapsed seconds)

## Forbidden anti-patterns

| Don't | Why |
|-------|-----|
| `Get-Process gemini` | Returns empty — gemini runs inside node |
| `Where MainWindowTitle -match ...` | Title truncates to prompt-theme value |
| `Stop-Process -Id <pid>` on wrapper | Orphans the worker tree |
| `foreach ($pid in ...)` in PS | `$pid` is reserved read-only — loop silently skips |
| Skipping cleanup between waves | Stale processes compete for GPU/rate limits next wave |
| `stop --all` during another N07 run | Kills their nuclei too |

## Verification recipe

```powershell
# After any stop, this MUST return zero rows:
Get-CimInstance Win32_Process |
  Where-Object { $_.CommandLine -match 'boot[/\\]n0[1-7](_gemini|_codex|_ollama)?\.ps1' } |
  Select ProcessId, CommandLine
```

If non-empty, either `spawn_stop.ps1` has a bug OR a different session owns those processes. Check pid file's `{sess}` column before escalating to `--all`.

## Properties

| Property | Value |
|----------|-------|
| Kind | `rule` |
| Pillar | cross-cutting |
| Domain | orchestration hygiene |
| Applies to | /mission, /grid, /showoff, /batch, /swarm, any multi-spawn |
| Quality target | 9.0+ |
