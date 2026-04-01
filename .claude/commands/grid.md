---
description: "Execute a spec — dispatch nuclei autonomously. Usage: /grid [spec_name]"
---

# /grid — Autonomous Execution

> **Input**: A `/spec` PSPEC + decision manifest
> **What**: Dispatches nuclei to build everything in the spec
> **Output**: Artifacts built, committed, signaled
> **Next step**: `/consolidate`

## Prerequisites

Before `/grid`, you need:
1. ✅ A plan (`/plan` or mental model)
2. ✅ Decisions made (`/guide` → `decision_manifest.yaml`)
3. ✅ A spec (`/spec` → `_docs/pspecs/PSPEC_*.md`)

If any is missing, suggest the user run that step first.

## Steps

### Step 1: Load spec

```bash
# Find the latest spec
ls -t _docs/pspecs/PSPEC_*.md | head -1

# Or user specifies: /grid PSPEC_N06_BRAND
```

Read the spec. Extract: waves, artifact list, nucleus assignments, dependencies.

### Step 2: Verify manifest exists

```bash
python _tools/cex_bootstrap.py --check
ls .cex/runtime/decisions/decision_manifest.yaml
```

If no manifest → warn: "No decisions on file. Nuclei will use defaults. Run `/guide` first?"

### Step 3: Dispatch by wave

Follow the spec's wave order. Respect dependencies.

```bash
# Wave 1 (sequential — must complete first)
bash _spawn/dispatch.sh solo n06 "Wave 1: brand identity — see PSPEC_N06"

# Wait for signal...

# Wave 2 (parallel — can run together)
bash _spawn/dispatch.sh grid WAVE2

# Wave 3 (after wave 2 completes)
bash _spawn/dispatch.sh solo n05 "Wave 3: deploy — see PSPEC_N05"
```

### Step 4: Monitor

```bash
bash _spawn/dispatch.sh status
git log --oneline -10
ls -lt .cex/runtime/signals/ | head -5
```

### Step 5: Report progress

As each nucleus signals complete:

```
━━━ Grid Progress ━━━
  Wave 1: N06 brand ████████████ DONE (q=9.0)
  Wave 2: N02 frontend ████████░░ 80%
  Wave 2: N01 research ████████████ DONE (q=9.0)
  Wave 3: N05 deploy ░░░░░░░░░░ WAITING
  ━━━ 2/4 nuclei complete ━━━
```

When all waves done → suggest: "All nuclei complete. Type `/consolidate` to verify and clean up."

## In-session mode

If no spawn/grid infrastructure (single session), execute waves sequentially yourself:
- Wave 1: build artifacts for nucleus A
- Wave 2: build artifacts for nuclei B+C
- Wave 3: build artifacts for nucleus D
- After each wave: compile + doctor + commit

## Grid is AUTONOMOUS

Once dispatched:
- Nuclei read the PSPEC + manifest
- They follow 8F pipeline
- They do NOT ask the user anything
- They commit and signal when done
- N07 monitors but does NOT intervene unless failure
