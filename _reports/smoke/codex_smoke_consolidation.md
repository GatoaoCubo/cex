---
mission: CODEX_SMOKE
wave: 1
status: PASS
executed_by: n07_direct
planned_dispatch: codex exec (inline, no wrapper Start-Process)
actual_dispatch: codex exec inline
tasks_completed: 1 of 1
---

# CODEX_SMOKE W1 Consolidation

## Purpose

Verify POLISH W3.3 (commit `7813eb115` -- strip `--model gpt-5-codex`
pin) works end-to-end through the codex exec pipeline. Baseline
proving the dispatch path can now be trusted for real work.

## Result

**PASS** -- codex executed the handoff, wrote the exact deliverable,
no collateral edits, exit 0 in ~4s wall-clock (3K tokens).

## Execution

```bash
# Handoff written to .cex/runtime/handoffs/n05_task_codex.md
# Inline invocation (bypasses spawn_solo.ps1 Start-Process to capture output):
timeout 180 codex exec --dangerously-bypass-approvals-and-sandbox -C "$(pwd)" \
    "Read .cex/runtime/handoffs/n05_task_codex.md and execute the CODEX_SMOKE task..."
```

## Verification

| Check | Expected | Actual |
|-------|----------|--------|
| Exit code | 0 | 0 |
| Deliverable path | `_reports/smoke/codex_smoke_20260415.md` | Landed exactly |
| Files touched | 1 | 1 (single apply_patch diff) |
| Wall-clock | < 60s | ~4s |
| Token cost | low | 3.059K |
| SMOKE_PASS sentinel | present | present |
| Model used | ChatGPT default (gpt-5.4-ish) | codex printed "GPT-5-based" |

## Caveat

The report file contains a **mojibake artifact** on the CLAUDE.md
first-line capture:

```
- First line of `CLAUDE.md`: # CEX â€" Typed Knowledge System for LLM Agents
```

The actual first line uses a UTF-8 em-dash (`—`). Codex's shell tool
captured bytes from cp1252 console and re-encoded them as UTF-8 when
writing the file, producing `â€"` where `—` should be. This is a
**console I/O encoding issue**, not a W3.3 regression. The emit_exit_signal
and vt_enable helpers already exist in boot/_shared/, but codex's internal
shell tool bypasses them. Non-blocking for the smoke goal.

## Implication for real dispatch

Codex is now safe to route mechanical tasks to via `solo-codex` mode.
Two remaining constraints:

1. **Handoff filename**: must be `{nucleus}_task_codex.md`, not
   `_task.md` (per `feedback_multiruntime_verification.md`).
   `spawn_solo.ps1 -task "..."` arg is still NOT safe for codex --
   write the file manually before dispatching.

2. **UTF-8 output**: avoid asking codex to capture console text with
   unicode chars. Use Python + `encoding="utf-8"` in handoffs that need
   exact bytes.

## Next

1. Exercise `solo-codex` through the actual PowerShell wrapper
   (`bash _spawn/dispatch.sh solo-codex n05` with a prepared handoff)
   to confirm the Start-Process path also works. Inline proves codex;
   wrapper proves the full session-aware dispatch layer.
2. Queue codex for a real mechanical task in the next maintenance
   mission (e.g. _tools/ refactor, test additions).
