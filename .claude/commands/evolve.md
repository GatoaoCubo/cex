You are N07, the orchestrator. The user wants to autonomously improve artifacts.

## What /evolve does

Runs the AutoResearch pattern on CEX artifacts:
- **One artifact, one metric, iterate until quality threshold**
- Keep improvements (git commit), discard failures (git restore)
- Log every experiment to `.cex/experiments/results.tsv`

## Execution

### 1. Parse intent

Determine what to evolve:
- If user specified a file: `cex_evolve.py single <file> --target 9.0`
- If user said "all" or "sweep": `cex_evolve.py sweep --target 8.5`
- If user specified a prompt: `cex_evolve.py prompt <file>`

### 2. Run the loop

```bash
# Single artifact
python _tools/cex_evolve.py single <file> --target 9.0 --max-rounds 5

# All quality:null artifacts
python _tools/cex_evolve.py sweep --target 8.5 --max-rounds 3

# Show history
python _tools/cex_evolve.py report
```

### 3. Report results

After evolution completes, report:
- Files improved (keep count)
- Files unchanged (discard count)
- Files that crashed (crash count)
- Final quality vs. baseline

### 4. Consolidate

Run standard post-change validation:
```bash
python _tools/cex_compile.py --all
python _tools/cex_doctor.py
```

## The AutoResearch pattern (Karpathy)

3-file architecture:
- `program.md` (goals) → CLAUDE.md + quality gates
- `train.py` (modifiable) → the target artifact
- `prepare.py` (metric) → cex_score.py + cex_compile.py

Loop: modify → run → measure → keep or discard. Never stop.
