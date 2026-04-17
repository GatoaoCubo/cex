---
id: p10_lr_n07_orchestrator_ops
kind: learning_record
pillar: P10
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: learning-record-builder
nucleus: N07
domain: "orchestration"
quality: 8.8
tags: [n07, orchestration, dispatch, routing, process-management, token-efficiency, wave-structure]
tldr: "N07 operational lessons: PID tree-kill, fake-signal verification, codex no-autocommit, rate limits, solo > grid on budget"
topic: "N07 orchestrator accumulated operational lessons from dispatch cycles"
outcome: PARTIAL
score: 8.5
context: "N07_admin P10 memory -- lessons accumulated across N01-N07 dispatch cycles, multiple missions, 2026-04-07 to 2026-04-17"
agent_group: "n07_orchestrator"
reproducibility: HIGH
impact: "Prevents re-learning known failure modes; each lesson avoids 15-45 min incident per recurrence"
timestamp: "2026-04-17T00:00:00Z"
decay_rate: 0.02
confidence: 0.85
dependencies: []
keywords: [dispatch, pid, taskkill, wrapper, routing, wave, handoff, rate-limit, token-budget, fake-signal]
linked_artifacts:
  primary: null
  related: [p10_lr_continuous_batching_speedup, p08_n07_grid_orchestration_mastery]
---
<!-- 8F: F1=learning_record/P10 F2=13ISOs/SlothLens F3=schema+examples+memory+MEMORY.md F4=9lessons/7cats F5=no-prior-file F6=produced F7=null/PARTIAL/gates-pass F8=compile -->

## Summary

9 dispatch-cycle lessons captured 2026-04-07 to 2026-04-17. Three systemic failures: wrapper PID != worker PID (orphaned processes); Ollama/Codex emit valid-format signals without completing work (false wave completion); Codex exits without committing (silent data loss). PARTIAL: routing architecture evolving.

## Pattern

1. `taskkill /F /PID <pid> /T`: tree-kill removes wrapper + claude.exe + node.exe + uvx. `Stop-Process` leaves workers orphaned.
2. Resolve worker PID: `Get-DescendantPids` via `Win32_Process` CIM BFS; record wrapper+worker in spawn_pids.txt.
3. Verify file-exists + git-commit before trusting signal; Ollama fabricates content, Codex exits 0 without committing.
4. Codex post-signal: `git log --oneline -5 N0x_*/`; if no commit, run `git add + commit` before wave advance.
5. Solo-sequential for <= 3 tasks: 30k boot tokens per spawn; grid-of-6 = 180k before first artifact line.
6. Cap Sonnet concurrent at 20: 32 concurrent = 87.5% success; 20 = near-100%.
7. Opus for N03 + N07 only; Sonnet covers N01, N02, N04, N05, N06.
8. Poll at 60-90s intervals via background bash loop; tight polling consumes N07 context window.
9. `$pid` is reserved in PowerShell (current process PID); use `$procId` or similar as loop variable.

## Anti-Pattern

1. `Start-Process -PassThru` PID for kill: wrapper PID; orphans claude.exe.
2. Ollama signal trusted: fabricated KC content passes format checks, silently corrupts downstream.
3. Codex exit assumed = commit: never commits; N07 must git-commit every Codex nucleus.
4. Grid for <= 3 tasks: 150k+ boot tokens, zero parallelism benefit.
5. `$pid` as loop var: silent zero-worker dispatch, no error raised.
6. Gemini free-tier in grid: 25+ min on "Thinking..." with zero output.

## Context

- Environment: Win11 Pro, Claude Code Anthropic Max, PowerShell 7, WSL bash, dispatch.sh
- Period: 2026-04-07 to 2026-04-17, ~8 missions, N01-N06 dispatched
- Runtimes: Claude (active), Codex (active), Ollama (excluded), Gemini (excluded)
- Decay: lessons > 90 days summarized to one-line; rate limits re-tested on tier change

## Impact

- PID tree-kill: prevents orphaned claude.exe billing; 15-30 min per incident saved.
- Fake-signal verify: prevents corrupted artifacts from passing wave gate; 20-45 min re-run avoided.
- Codex no-autocommit: prevents wave advance on uncommitted work; 10-30 min re-dispatch avoided.
- Rate cap 20: eliminates 12.5% failure rate at 32 concurrent; 5-15 min retry overhead per wave.
- Solo > grid heuristic: saves 150k+ boot tokens (~$0.60-1.20) per unnecessary grid.
- $pid reserved: prevents silent zero-worker dispatch; 20-60 min debug time avoided.

## Reproducibility

| Lesson | Confidence | Caveat |
|--------|-----------|--------|
| PID tree-kill | HIGH | Windows process semantics; deterministic |
| Ollama fake-signal | HIGH | qwen3:8b+14b, llama3.1:8b confirmed |
| Codex no-autocommit | HIGH | CLI design; permanent until upstream fix |
| Rate cap 20 | MEDIUM | Account-scoped; re-test after tier upgrade |
| $pid reserved | HIGH | PowerShell language spec; permanent |
| Solo > grid | MEDIUM | 30k estimate; re-evaluate as pricing changes |

## References

1. `.claude/rules/n07-orchestrator.md` -- kill-tree, PID tracking, session-aware stop
2. `.claude/rules/n07-autonomous-lifecycle.md` -- non-blocking poll, taskkill /T
3. `MEMORY.md` -- Wrapper PID Pitfall, Codex no-autocommit, Rate limits atlas
4. `N07_admin/P10_memory/grid_orchestration_mastery.md` -- wave structure

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | orchestration |
| Nucleus | N07 |
| Pipeline | 8F |
| Compiler | cex_compile.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
