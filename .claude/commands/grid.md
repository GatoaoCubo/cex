---
description: "Execute a spec — dispatch nuclei autonomously. Usage: /grid [spec_name]"
quality: 9.0
title: "Grid"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p12_wf_admin_orchestration
  - p12_wf_orchestration_pipeline
  - p12_wf_engineering_pipeline
  - ctx_cex_new_dev_guide
  - n07_output_orchestration_audit
  - skill
  - p01_kc_orchestration_best_practices
  - continuous_batching_report
  - p01_kc_orchestration
  - dispatch
---

# /grid — Autonomous Execution

> **Input**: A `/spec` + decision manifest
> **What**: Dispatches nuclei to build everything in the spec
> **Output**: Artifacts built, committed, signaled
> **Next step**: `/consolidate`

## Prerequisites

Before `/grid`, you need:
1. ✅ A plan (`/plan` or mental model)
2. ✅ Decisions made (`/guide` → `decision_manifest.yaml`)
3. ✅ A spec (`/spec` → `_docs/specs/spec_*.md`)

If any is missing, suggest the user run that step first.

## Steps

### Step 1: Load spec

```bash
# Find the latest spec
ls -t _docs/specs/spec_*.md | head -1

# Or user specifies: /grid spec_n06_brand
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
bash _spawn/dispatch.sh solo n06 "Wave 1: brand identity — see spec"

# Wait for signal...

# Wave 2 (parallel — can run together)
bash _spawn/dispatch.sh grid WAVE2

# Wave 3 (after wave 2 completes)
bash _spawn/dispatch.sh solo n05 "Wave 3: deploy — see spec"
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
1. Wave 1: build artifacts for nucleus A
2. Wave 2: build artifacts for nuclei B+C
3. Wave 3: build artifacts for nucleus D
4. After each wave: compile + doctor + commit

## Grid is AUTONOMOUS

Once dispatched:
1. Nuclei read the spec + manifest
2. They follow 8F pipeline
3. They do NOT ask the user anything
4. They commit and signal when done
5. N07 monitors but does NOT intervene unless failure

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_admin_orchestration]] | related | 0.41 |
| [[p12_wf_orchestration_pipeline]] | related | 0.38 |
| [[p12_wf_engineering_pipeline]] | related | 0.38 |
| [[ctx_cex_new_dev_guide]] | related | 0.36 |
| [[n07_output_orchestration_audit]] | related | 0.34 |
| [[skill]] | related | 0.34 |
| [[p01_kc_orchestration_best_practices]] | related | 0.32 |
| [[continuous_batching_report]] | related | 0.31 |
| [[p01_kc_orchestration]] | related | 0.30 |
| [[dispatch]] | related | 0.29 |
