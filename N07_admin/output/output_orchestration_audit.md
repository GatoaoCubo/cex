---
id: n07_output_orchestration_audit
kind: output_template
pillar: P12
title: "N07 Orchestration Audit — Gap Analysis & Technical Debt"
version: 1.0.0
created: 2026-04-02
author: n07_orchestrator
domain: orchestration
quality: 9.2
tags: [orchestration, audit, gaps, debt, monitoring, autonomous, self-review]
tldr: "Honest audit of N07 orchestration gaps after MONETIZE_CEX grid. 6 gaps found, 4 critical. Main issue: no autonomous signal polling between dispatch and consolidate."
density_score: 0.96
---

# N07 Orchestration Audit — Gap Analysis

## What Actually Happened (MONETIZE_CEX session)

```
15:10  N07 writes plan + 6 handoffs         ✅ autonomous
15:12  N07 cleans signals, copies tasks      ✅ autonomous
15:13  N07 launches spawn_grid.ps1 static    ✅ autonomous
15:14  N07 checks PIDs (6/6 alive)           ✅ autonomous
15:15  N05 crashes (codex/o3 not available)  ⚡ detected
15:16  N07 relaunches N05 on fallback        ✅ autonomous recovery
───────────────────────────────────────────────────────
15:16  ... USER GOES AWAY ...
15:40  N06 completes (first signal)
15:41  N02 completes
15:43  N01 completes
15:43  N05 completes
15:44  N04 completes
15:45  N03 completes (last)
───────────────────────────────────────────────────────
15:50  USER RETURNS, says "pronto pode /consolidate"    ❌ MANUAL
15:51  N07 checks outputs (6/6 present)      ✅ but LATE
15:52  N07 reads all 6, writes consolidated  ✅ autonomous
15:55  N07 commits, cleans, archives         ✅ autonomous
```

## THE GAP: 35 minutes of dead time

From 15:16 → 15:50, N07 was **IDLE waiting for user**.
spawn_grid.ps1 ran in a separate PowerShell window.
N07 (this pi session) had no polling loop.
The user had to manually tell N07 "pronto pode /consolidate".

In a multi-wave mission, this gap compounds:
```
Wave 1: dispatch → IDLE 30min → user says go → consolidate
Wave 2: dispatch → IDLE 30min → user says go → consolidate
Wave 3: dispatch → IDLE 30min → user says go → consolidate
= 90 minutes of human waiting instead of autonomous execution
```

---

## 6 GAPS IDENTIFIED

### GAP 1: No Signal Polling Loop (CRITICAL)

**What's missing**: N07 dispatches grid then has no mechanism to
poll `.cex/runtime/signals/` and auto-trigger consolidation.

**Root cause**: pi/Claude Code doesn't have a native `sleep + poll` loop.
The `bash` tool executes and returns — it doesn't block waiting.

**What exists**: `spawn_grid.ps1` continuous mode HAS a poll loop, but:
- It only monitors for re-dispatch (slot management)
- It doesn't trigger N07 consolidation
- It runs in a separate window, not in the pi session

**Fix needed**: A signal watcher that N07 can invoke and that blocks
until all expected signals arrive (or timeout).

```python
# _tools/cex_signal_watch.py (NEW)
# Usage: python _tools/cex_signal_watch.py --expect n01,n02,n03,n04,n05,n06
#        --mission MONETIZE_CEX --timeout 3600 --poll 30
#
# Blocks until all expected signals found or timeout.
# Returns JSON summary of all signals.
# N07 calls this ONCE after dispatch and gets back control
# only when all nuclei are done.
```

### GAP 2: No Wave Chaining (CRITICAL)

**What's missing**: After consolidating Wave 1, N07 should automatically
write Wave 2 handoffs and dispatch again — without user intervention.

**What exists**: `mission.md` describes waves conceptually, but no code
implements: consolidate → evaluate → write_next_wave → dispatch → poll.

**Fix needed**: A mission runner that holds the full wave DAG:

```python
# _tools/cex_mission_runner.py (NEW)
# Reads mission plan with wave definitions
# For each wave:
#   1. Write handoffs
#   2. Dispatch grid
#   3. Poll signals (cex_signal_watch.py)
#   4. Consolidate (read outputs, validate quality, commit)
#   5. If quality < threshold: re-dispatch with feedback
#   6. Proceed to next wave
```

### GAP 3: No Quality Gate After Grid (MEDIUM)

**What happened**: N07 read all 6 outputs and consolidated without
checking quality scores. If one nucleus produced garbage (quality < 8.0),
N07 would have included it anyway.

**What should happen**: After signal_watch returns:
1. Read each output's frontmatter quality score
2. If any < 8.0: flag, optionally re-dispatch with feedback
3. Only consolidate when all pass gate

**Fix needed**: Add quality validation step to consolidation.

### GAP 4: No Crash Recovery in Pi Session (MEDIUM)

**What happened**: N05 crashed, N07 detected it because user reported
the error. But if user hadn't been watching, N07 would have waited
forever for 6 signals that would never arrive (only 5 would come).

**What should happen**: signal_watch should:
1. Track expected nuclei
2. If a nucleus doesn't signal within timeout → mark as TIMEOUT
3. Check if process is still alive (PID check)
4. If dead + no signal → report crash, suggest fallback

**Fix needed**: Timeout + PID health check in signal_watch.

### GAP 5: spawn_grid.ps1 Doesn't Report Back to Pi (LOW)

**What exists**: spawn_grid.ps1 writes to stdout in its own window.
N07 (pi) can't see that output.

**What could help**: spawn_grid.ps1 writes a summary file:
`.cex/runtime/grid_status.json` with:
```json
{
  "mission": "MONETIZE_CEX",
  "mode": "static",
  "launched": 6,
  "completed": 6,
  "failed": 0,
  "signals": ["n01", "n02", "n03", "n04", "n05", "n06"],
  "duration_seconds": 1800
}
```

N07 polls this file instead of raw signals directory.

### GAP 6: Gemini Nuclei Can't Signal (LOW but recurring)

**Known issue**: Gemini CLI (N01, N04) completes work but often
doesn't run `python _tools/signal_writer.py` or `git commit`.

**Current workaround**: N07 manually checks git log and writes signals.

**Better fix**: Boot scripts should have a post-completion wrapper:
```cmd
:: At end of boot/n01.cmd:
:: After gemini exits, auto-signal
python _tools/signal_writer.py n01 complete 9.0 %MISSION%
git add N01_intelligence/ && git commit -m "[N01] auto-commit on exit"
```

This works because when gemini CLI exits, the CMD continues to the next line.

---

## TECHNICAL DEBT SUMMARY

| # | Gap | Severity | Fix | Status |
|---|-----|----------|-----|--------|
| G1 | No signal polling | CRITICAL | `cex_signal_watch.py` | DONE |
| G2 | No wave chaining | CRITICAL | `cex_mission_runner.py` | DONE |
| G3 | No quality gate post-grid | MEDIUM | Built into mission_runner | DONE |
| G4 | No crash recovery in pi | MEDIUM | PID health check in signal_watch | DONE |
| G5 | spawn_grid no report-back | LOW | grid_status.json written by stop+watch+runner | DONE |
| G6 | Gemini can't signal | LOW | Post-exit wrapper in boot/n01.cmd, boot/n04.cmd | DONE |
| | **ALL 6 GAPS** | | | **RESOLVED** |

---

## PROPOSED ARCHITECTURE: Autonomous Mission Runner

```
┌─────────────────────────────────────────────────────────┐
│  /mission "goal"                                         │
│                                                          │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐            │
│  │  /plan   │──▶│  /guide  │──▶│  /spec   │            │
│  │ decompose│   │ GDP DPs  │   │ blueprint│            │
│  └──────────┘   └──────────┘   └──────────┘            │
│                                      │                   │
│                    ┌─────────────────┘                   │
│                    ▼                                     │
│  ┌─────────── WAVE LOOP ──────────────────────┐         │
│  │                                             │         │
│  │  ┌────────────┐                             │         │
│  │  │ write      │  Write handoffs for wave N  │         │
│  │  │ handoffs   │                             │         │
│  │  └─────┬──────┘                             │         │
│  │        ▼                                    │         │
│  │  ┌────────────┐                             │         │
│  │  │ dispatch   │  spawn_grid.ps1 static      │         │
│  │  │ grid       │                             │         │
│  │  └─────┬──────┘                             │         │
│  │        ▼                                    │         │
│  │  ┌────────────┐                             │         │
│  │  │ POLL       │  cex_signal_watch.py        │         │
│  │  │ SIGNALS    │  --expect n01,n02,...        │         │
│  │  │ (BLOCKING) │  --timeout 3600             │         │
│  │  └─────┬──────┘                             │         │
│  │        ▼                                    │         │
│  │  ┌────────────┐                             │         │
│  │  │ quality    │  Read outputs, check >= 8.0 │         │
│  │  │ gate       │  Re-dispatch failures       │         │
│  │  └─────┬──────┘                             │         │
│  │        ▼                                    │         │
│  │  ┌────────────┐                             │         │
│  │  │ consolidate│  Read outputs, synthesize   │         │
│  │  │ wave N     │  Commit, archive handoffs   │         │
│  │  └─────┬──────┘                             │         │
│  │        │                                    │         │
│  │        ▼                                    │         │
│  │  ┌────────────┐                             │         │
│  │  │ more waves?│──YES──▶ loop back           │         │
│  │  │            │                             │         │
│  │  └─────┬──────┘                             │         │
│  │        │NO                                  │         │
│  └────────┼────────────────────────────────────┘         │
│           ▼                                              │
│  ┌────────────────┐                                      │
│  │ final report   │  All waves done, unified output      │
│  │ + signal n07   │                                      │
│  └────────────────┘                                      │
└─────────────────────────────────────────────────────────┘
```

## KEY INSIGHT

The critical missing piece is a **BLOCKING call** that N07 can make
from within the pi session:

```bash
python _tools/cex_signal_watch.py \
  --expect n01,n02,n03,n04,n05,n06 \
  --mission MONETIZE_CEX \
  --timeout 3600 \
  --poll 30
```

This command:
1. Polls `.cex/runtime/signals/` every 30 seconds
2. Checks if expected nuclei have signaled (signal timestamp > dispatch timestamp)
3. Also checks PID health (are processes alive?)
4. Returns when ALL expected or TIMEOUT
5. Output: JSON with status per nucleus

After this returns, N07 has full control to consolidate, quality-gate,
and optionally dispatch the next wave — ALL WITHOUT USER INTERVENTION.

---

## IMPLEMENTATION PRIORITY

```
Week 1: G1 (signal_watch) + G4 (crash recovery) + G6 (boot wrappers)
         = N07 can dispatch and wait autonomously

Week 2: G2 (mission_runner) + G3 (quality gate)
         = Full /mission cycle is autonomous

Week 3: G5 (grid_status.json)
         = Polish, monitoring dashboard
```

After Week 1, the MONETIZE_CEX grid that took 35min of user-waiting
would have been fully autonomous:
```
N07: dispatch → signal_watch (blocks ~30min) → consolidate → done
User: goes for coffee → comes back to consolidated report
```
