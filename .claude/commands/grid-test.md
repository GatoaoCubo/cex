# /grid-test — Multi-Runtime Wave Orchestration

**Purpose**: Prove CEX orchestrates ANY interactive CLI model. Run the SAME mission across N runtimes sequentially (one wave per runtime), consolidate after each wave, compare results.

**Mental model**: `/mission` but done N times (claude, gemini, codex, ollama-llama, ollama-qwen-coder) sequentially, with `/consolidate` baked in between each wave.

---

## PROTOCOL

### Step 1: VERIFY mission + runtimes
```bash
# Mission must exist
ls .cex/P09_config/missions/{MISSION}/mission.yaml

# Runtimes you want must exist
ls .cex/P09_config/runtimes/

# Handoffs must exist for the mission (6 files, one per nucleus)
ls .cex/runtime/handoffs/ | grep {MISSION_UPPER}
```

If handoffs are missing, run `/guide` or `/spec` first to produce them.

### Step 2: RUN grid-test (BACKGROUND — N07 never idles)
```bash
python _tools/cex_grid_test.py \
    --mission {MISSION} \
    --runtimes claude,gemini,codex,ollama-llama,ollama-qwen-coder \
    --wave-timeout 900 \
    --poll-interval 30 \
    --inter-wave-sleep 15
```

**For N07**: launch this with `Bash run_in_background: true` so you can keep
working (memory writes, spec audits, next-mission planning) while waves
execute. Poll the log file every 60-90s:

```bash
# poll progress without blocking
tail -n 40 _reports/gridtest_{mission}/state.log

# or check for wave-completion markers
grep "WAVE\|archive\|TIMEOUT" _reports/gridtest_{mission}/state.log | tail -20
```

### Step 3: PARTIAL RUNS (skip expensive / unavailable runtimes)
```bash
# ollama-only (free, always works)
python _tools/cex_grid_test.py --mission leverage_map \
    --runtimes ollama-llama,ollama-qwen-coder

# claude-only (paid)
python _tools/cex_grid_test.py --mission leverage_map \
    --runtimes claude

# Skip claude-family if auth unavailable
python _tools/cex_grid_test.py --mission leverage_map --skip-claude-family
```

### Step 4: READ the matrix
```bash
cat _reports/gridtest_{mission}/matrix.md
```

Contains:
- Landed vs usable per runtime
- Timeout per wave
- Per-nucleus byte count across all runtimes (columns = n01..n06, rows = runtimes)

### Step 5: Consolidate into a commit
```bash
git add _reports/gridtest_{mission}/
git commit -m "[N07] grid-test {mission}: {N} runtimes, matrix at _reports/gridtest_{mission}/matrix.md"
```

---

## What each wave does (internal)

```
WAVE k:
  dispatch  -> python _tools/cex_mission_dispatch.py --mission {M} --runtime {R}
              (which calls bash _spawn/dispatch.sh grid-{variant} OR
               powershell spawn_grid_ollama.ps1 with ModelMap)
  poll      -> loop: list output files, check PIDs alive, poll every {poll-interval}s
  close     -> kill all PIDs from wave's PID file (orphan REPL cleanup)
  archive   -> copy outputs + trace.json to _reports/gridtest_{mission}/{runtime}/
            -> write wave_report.json (bytes, iters, reads per nucleus)
  sleep     -> {inter-wave-sleep}s before next wave
```

**Inter-wave sleep** is in-process `time.sleep()` inside the tool, NOT
ScheduleWakeup. N07 never idles -- the tool runs in background while
N07 works on other tasks.

---

## Output Locations

| Path | Contents |
|------|----------|
| `_reports/gridtest_{mission}/state.log` | Real-time orchestrator log |
| `_reports/gridtest_{mission}/{runtime}/LEVERAGE_MAP_V2_n0X.md` | Per-nucleus output (archived) |
| `_reports/gridtest_{mission}/{runtime}/LEVERAGE_MAP_V2_n0X.trace.json` | ReAct trace |
| `_reports/gridtest_{mission}/{runtime}/wave_report.json` | Wave summary (landed/usable/timeout) |
| `_reports/gridtest_{mission}/matrix.md` | Final comparison matrix |

---

## When /grid-test is the right tool

- Validating a new mission across all supported runtimes
- Benchmarking model quality on the SAME task (free vs paid vs local)
- Regression-testing after prompt changes (did qwen get worse? did Claude stay strong?)
- Demonstrating model-agnostic orchestration for stakeholders

## When it's NOT

- Single-runtime work -> use `/mission` instead
- One-off nucleus task -> use `/dispatch solo`
- Parallel independents (not same mission) -> use `/grid`

---

## Operator Gotchas (learned 2026-04-15)

1. **Dual-mode completion detection**: wave finishes when EITHER (a) N output
   files land in the ollama output dir OR (b) N `[N0X] MISSION:` commits land
   since wave-start git ref. So claude/gemini/codex nuclei (which commit but
   don't produce a unified output file) are detected via the commit path.
2. **Ollama orphan REPL windows** persist after agentic_loop exits. `close_wave`
   kills them via `taskkill /F /PID {pid} /T`. Verify with
   `Get-Process powershell` after a wave.
3. **8F-strict prompt regresses small models** (see memory
   `project_qwen_8f_strict_regression.md`). If running qwen/gemma/llama,
   consider reverting to minimal prompt first.
4. **Do NOT ScheduleWakeup** during the run. The tool manages its own sleeps
   internally. N07 polls the log file.
5. **Matrix always has `Committed` column** alongside `Landed` and `Usable` --
   for claude-family, Committed is the source of truth; for ollama, both
   typically match (ollama nuclei auto-commit via boot wrapper).
6. **Stale output stubs poison completion**: `dispatch_wave` cleans any
   existing `{MISSION_UPPER}_n0*.md` (and `.trace.json`) in the output dir
   BEFORE dispatch, so a prior failed run's 9-byte `MAX_ITERS` placeholder
   doesn't instant-satisfy the file-land detector. Use uppercase glob.
7. **Free-tier recommendation: `ollama-llama` (pure)**, not hybrid routing.
   Per-nucleus qwen2.5-coder:7b on content tasks produces 9-byte stubs;
   ollama run-to-run variance (2-6x per nucleus) dominates routing gains.
   See memory `project_free_tier_routing_truth.md`.
8. **Monitoring pattern** while a grid-test runs: `Bash run_in_background`
   for the tool + `Monitor` tailing `state.log` with filter
   `-E "=== WAVE|landed=[3-6]/|close |archive|COMPLETE|FAILED|TIMEOUT"`.
   No polling, live progress, stays out of context until events fire.
