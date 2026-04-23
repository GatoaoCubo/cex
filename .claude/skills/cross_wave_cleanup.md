---
name: cross-wave-cleanup
description: Clean up wrapper PID trees and orphan runtime processes between waves of /mission, /grid, /showoff, or /batch so the next wave starts clean.
when:
  - After any multi-spawn wave completes and before the next wave starts.
  - When orchestrating /mission, /grid, /showoff, /batch, /swarm, or similar multi-runtime dispatches.
  - When stale boot wrappers, worker trees, or orphan node processes may block a new wave.
kind: skill
pillar: P04
nucleus: n03
quality: 8.7
version: 1.0.0
created: 2026-04-16
multi_runtime: true
runtimes: [claude, codex, gemini, ollama]
density_score: 0.85
related:
  - p01_kc_cex_orchestration_architecture
  - spec_claude_native_hardening
  - n07_output_orchestration_audit
  - p08_ac_admin_orchestrator
  - n07_memory_grid_ops
  - p01_kc_spawn_patterns
  - commercial_readiness_20260414c
  - p01_kc_orchestration_best_practices
  - showoff_w2_n05_gemini
  - showoff_w5_n06_gemini
---

# Cross-Wave Cleanup

## When this fires
- Before wave N+1 after wave N used multi-spawn orchestration.
- When wrappers from `boot/n0X*.ps1` may still be alive.
- When Gemini orphan `node.exe` processes or stale signals can poison the next run.

## What to do
1. Run `bash _spawn/dispatch.sh stop` for normal between-wave cleanup. Use `stop n03` only for surgical cleanup or `stop --all` only when explicitly required across sessions.
2. Rely on the stop flow to do all three passes: PID-file scan, `Win32_Process.CommandLine` scan for `boot/n0[1-7](_gemini|_codex|_ollama)?\.ps1`, and orphan `node.exe` scan for Gemini or Codex leftovers.
3. Treat the wrapper PID tree as the kill target for all runtimes: Claude, Gemini, Codex, and Ollama. Use `taskkill /F /PID <id> /T`; never use `Stop-Process` on wrapper PIDs.
4. Before cleanup between waves, archive wave signals, commit stray artifacts in the wave scope, then stop the session's processes.
5. Verify cleanup by checking that no `powershell.exe` or other process still references `boot/n0*.ps1` in `Win32_Process.CommandLine`.
6. Report the wave status with signal count, artifacts handled, and elapsed time before starting the next wave.

## Example
- Wave A finishes a `/grid` run. Trigger this skill, archive the signals, run `bash _spawn/dispatch.sh stop`, verify no `boot/n0*.ps1` command lines remain, then start Wave B.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.37 |
| [[spec_claude_native_hardening]] | related | 0.33 |
| [[n07_output_orchestration_audit]] | downstream | 0.28 |
| [[p08_ac_admin_orchestrator]] | downstream | 0.25 |
| [[n07_memory_grid_ops]] | downstream | 0.25 |
| [[p01_kc_spawn_patterns]] | upstream | 0.24 |
| [[commercial_readiness_20260414c]] | downstream | 0.24 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.24 |
| [[showoff_w2_n05_gemini]] | downstream | 0.23 |
| [[showoff_w5_n06_gemini]] | downstream | 0.23 |
