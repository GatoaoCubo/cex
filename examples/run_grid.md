# Run Grid

This walkthrough shows the multi-nucleus path: write handoffs, dispatch a grid mission, monitor progress, then consolidate. Run this after [build_one_artifact.md](build_one_artifact.md).

## Prerequisites

- The repo is healthy (`python _tools/cex_doctor.py`)
- Mission handoffs exist in `.cex/runtime/handoffs/`
- Bash can invoke `_spawn/dispatch.sh`

## 1. Confirm the handoffs

Grid mode reads per-nucleus handoffs from `.cex/runtime/handoffs/`. For example, this repo currently contains mission-specific files such as:

```text
.cex/runtime/handoffs/OPENSOURCE_FIX_n01.md
.cex/runtime/handoffs/OPENSOURCE_FIX_n03.md
.cex/runtime/handoffs/OPENSOURCE_FIX_n04.md
.cex/runtime/handoffs/OPENSOURCE_FIX_n05.md
```

## 2. Dispatch the grid

```bash
bash _spawn/dispatch.sh grid OPENSOURCE_FIX
```

Expected immediate output:

```text
[DISPATCH] Grid: OPENSOURCE_FIX (cli=claude)
```

Under the hood, `_spawn/dispatch.sh` calls `_spawn/spawn_grid.ps1`, starts up to six nuclei, and records their PIDs and session IDs in `.cex/runtime/pids/`.

## 3. Monitor the run

```bash
bash _spawn/dispatch.sh status
```

The monitor prints a compact table. Real output from this repo uses this format:

```text
  NUCLEUS   STATUS     QUALITY  TIME
  --------- ---------- -------  ----
  N05       CRASHED      -      0min
  N01       RUNNING      -      0min
  N03       RUNNING      -      0min
  N04       RUNNING      -      0min
  N05       RUNNING      -      0min
```

Status comes from two sources:

- process liveness from `.cex/runtime/pids/spawn_pids.txt`
- completion signals from `.cex/runtime/signals/signal_n0x_*.json`

## 4. Inspect handoffs and outputs while the grid runs

Useful paths:

- `.cex/runtime/handoffs/` for the task each nucleus received
- `.cex/runtime/signals/` for completion/error signals
- `N0x_*/` for the files each nucleus created or updated

## 5. Consolidate after completion

The orchestrator rules describe this sequence:

```bash
python _tools/cex_doctor.py
bash _spawn/dispatch.sh stop
git log --oneline -n 5
```

If the mission completed cleanly, each nucleus should have committed its own output slice before signaling complete.

## What gets committed

For a normal grid mission, nuclei commit the files they own. In this handoff wave:

- N01 owns research/audit outputs
- N03 owns engineering/build outputs
- N04 owns docs, examples, and knowledge-facing outputs
- N05 owns validation and code/test outputs

That separation is why handoffs and signals live in `.cex/runtime/`: they let the orchestrator monitor progress without merging all work into one giant manual commit.

## Next steps

After the grid is done, review the new files, rerun the relevant validators, and open the repo for external contributors.
