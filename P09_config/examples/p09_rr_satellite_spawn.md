---
id: p09_rr_satellite_spawn
type: runtime_rule
lp: P09
title: "Runtime Rule: Satellite Spawn Constraints"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: PYTHA
quality: 9.0
tags: [runtime, satellite, spawn, constraints, bsod]
tldr: "Spawn rules: max 3 satellites + STELLA (BSOD at 4), 5s between terminals, -p flag mandatory for TSP, inline prompt < 200 chars"
max_bytes: 512
density_score: 0.91
source: codexa-core/.claude/rules/boot-autonomy-flags.md + MEMORY.md constraints
linked_artifacts:
  spawn_config: p12_spawn_grid_continuous
---

# Runtime Rule: Satellite Spawn Constraints

## Hard Limits

```yaml
spawn_limits:
  max_concurrent_satellites: 3   # + STELLA = 4 total. BSOD confirmed at 5
  delay_between_terminals: 5s    # RAM stability — never skip
  max_inline_prompt_chars: 200   # TSP -p flag limit — longer prompts hang
  satellite_boot_timeout: 30s    # Kill and retry if no output after 30s
```

## Required Flags

```bash
# TSP satellite spawn (mandatory flags):
claude --dangerously-skip-permissions --no-chrome -p

# -p (non-interactive): skips workspace trust dialog — MANDATORY for automation
# --dangerously-skip-permissions: skips tool permission prompts
# --no-chrome: all satellites (chrome only via boot/chrome.cmd)
```

## Spawn Script Rules

```powershell
# CORRECT:
spawn_solo.ps1 -sat pytha -task "Read handoff and execute" -interactive

# WRONG (all cause failures):
tsp_manager.py spawn        # invisible window, cannot kill claude.exe
spawn with --mcp-config     # absolute paths hang in PS->cmd chain
```

## Environment Variables

```batch
# REQUIRED in boot scripts (v2.1.50+ fix):
set CLAUDECODE=
set CODEXA_SATELLITE={SAT_NAME}&&claude --dangerously-skip-permissions ...

# Note: set VAR=val&& (no space before &&)
```

## BSOD Prevention

```yaml
bsod_history: 2026-02-18
cause: USB power suspend + Intel I219-V driver race condition
prevention:
  - hybrid_sleep: disabled
  - usb_selective_suspend: disabled
  - hibernate: disabled
  - wake_on_lan: disabled
threshold: NEVER spawn 4+ satellites simultaneously
```

## Handoff Offload Rule

When task > 200 chars, write to handoff file:
```bash
# Inline prompt (PASS):
"Read .claude/handoffs/CEX7_batch_2_pytha.md e execute"  # 53 chars

# Inline prompt (FAIL — hangs with -p):
"Execute these 10 tasks: [1] research market... [2] build agent..." # 400+ chars
```
