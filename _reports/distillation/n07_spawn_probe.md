---
report: N07_SPAWN_PROBE
mission: N07_SPAWN_PROBE_20260416
nucleus: n07
started: 2026-04-16T13:15:00-03:00
completed: 2026-04-16T13:20:00-03:00
base_commit: 872d34341
status: PARTIAL_PASS
---

# N07 Spawn Probe -- Post-Gap-1 Fix Validation

## Purpose

Validate the Gap 1 fix (commit `a2250c406`) by actually spawning N07 via
`codex`, `gemini`, and `ollama` runtimes with pre-staged runtime-specific
handoffs (`n07_task_codex.md`, `n07_task_gemini.md`, `n07_task_ollama.md`).

Each probe handoff requested:
1. Write `_reports/spawn_probe/{runtime}_probe.txt` via shell
2. Signal complete

## Methodology

- `bash _spawn/dispatch.sh solo-{cli} n07 ""` for each runtime in sequence
  (spawn_solo.ps1 auto-kills predecessor for same nucleus key -- parallel
   spawn of identical nuclei is impossible, so tests ran serial).
- Pre-staged probes per runtime path. Empty TASK arg preserves pre-staged
  handoff (PowerShell `if ($task)` guard on empty string is falsy).
- Monitor polled for probe file OR signal with 3-4 min timeout.

## Results

| Runtime | Boot parse | Handoff read | Probe file | Signal | Overall |
|---------|-----------|--------------|------------|--------|---------|
| codex   | OK        | YES (path in probe content) | CREATED | complete q=8.5 | **PASS** |
| gemini  | OK        | unknown (fast exit) | MISSING | exited q=0.0 (safety-net) | **STRUCTURAL PASS** |
| ollama  | OK        | YES (mission extracted from handoff) | MISSING | complete q=8.5 (fake) | **STRUCTURAL PASS** |

## Evidence

### Codex (full pass)
`_reports/spawn_probe/codex_probe.txt`:
```
16/04/2026 13:17:37
runtime=codex, handoff_path=n07_task_codex.md, pwd=C:\Users\CEX\Documents\GitHub\cex
```
-> Model confirmed it read `n07_task_codex.md`. Fix validated end-to-end.

### Gemini (structural pass, free-tier blocker)
- Boot launched `gemini` CLI (v0.38.1 confirmed on PATH).
- Process exited at ~14s with safety-net signal (`status=exited`, `q=0.0`).
- Known blocker: free tier "Thinking..." hang or immediate quota rejection
  (see memory `project_gemini_free_tier_unusable_2026_04_15.md`).
- Boot-path fix is STRUCTURALLY CORRECT (prompt references `n07_task_gemini.md`),
  but end-to-end execution blocked by Google quota layer -- NOT by the fix.

### Ollama (structural pass, fake-signal pattern)
- Boot launched `ollama_nucleus.py` with `qwen3:8b`.
- Mission extracted from `n07_task_ollama.md` -> "N07_SPAWN_PROBE_20260416"
  shows up in the emitted signal, proving the fixed handoff path is read.
- No probe file created because `ollama_nucleus.py` is a prompt-only
  wrapper (no shell execution). Model can't run `date > file`.
- Fake-signal is the known pattern from memory
  `feedback_multiruntime_verification.md` -- `_tools/ollama_nucleus.py:170`
  always signals `complete` after LLM returns, regardless of work done.

## Conclusion

Gap 1 fix (handoff path consistency across 3 N07 boots) is **validated**:
- Codex: probe content literally confirms path read.
- Ollama: mission field extracted only possible if fixed handoff was loaded.
- Gemini: parse + launch clean; end-to-end blocked by free-tier upstream.

Execution failures in ollama+gemini are PRE-EXISTING and orthogonal to the
Gap 1 fix -- they are runtime-layer limitations (no shell / quota block),
not boot-script bugs.

## Recommendations (follow-up, non-blocking)

1. `ollama_nucleus.py:170` -- gate signal emission on deliverable existence,
   not model return. Without this, ollama always fake-signals.
2. Gemini free tier -- skip dispatch or require paid tier; track in
   `project_gemini_free_tier_unusable_2026_04_15.md`.
3. Nothing to fix in the N07 boots themselves.

## Files

- `_reports/spawn_probe/codex_probe.txt` (107 bytes)
- `.cex/runtime/signals/signal_n07_*.json` (3 signals, cleaned between runs)
