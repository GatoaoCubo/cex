---
mission: SCORE_REFORM
nucleus: n03
wave: M1b
created: 2026-04-17
priority: CRITICAL
effort: opus_high
---

# N03 SCORE_REFORM M1b: Fix cex_evolve.py -- heuristic->quality + sweep priority

## CONTEXT

cex_score.py was already fixed by N05 (commit 7eb7b96d1).
Your job: fix _tools/cex_evolve.py only.

Read the FULL file first: `_tools/cex_evolve.py`
Also read: `_tools/cex_score.py` (to understand update_quality, score_structural, score_rubric)

## THE PROBLEM

cex_evolve.py heuristic mode improves artifacts but NEVER writes the quality score.
After a full heuristic sweep, 587 files still have `quality: null` even though
they were touched and improved. The Karpathy loop is broken because it cannot
see its own output.

## FIX 1: heuristic mode writes quality after improvement

In `cex_evolve.py`, find the function(s) that apply heuristic improvements
and write the modified file to disk.

After the file write, add:
```python
# Import at top of file (add if not present):
from cex_score import score_structural, score_rubric, update_quality

# After each heuristic file write:
try:
    struct_raw, _ = score_structural(str(filepath))
    rubric_raw, _, _ = score_rubric(str(filepath))
    heuristic_q = round((struct_raw + rubric_raw) / 2, 1)
    update_quality(str(filepath), heuristic_q)
except Exception:
    pass  # score failure must never break the evolve loop
```

This closes the loop: heuristic improves content -> scores it -> writes quality field.
The quality field is now observable by subsequent runs.

## FIX 2: sweep prioritizes quality:null files first

In the sweep function, find where candidate files are collected/sorted.
Add a sort key so quality:null files come first:

```python
def _sweep_priority(fp: Path) -> float:
    """Sort key: null=0 (highest priority), then ascending by quality."""
    q = get_current_quality(fp)
    if q is None:
        return 0.0   # null = score first
    return q         # lower score = higher priority

# Apply before the sweep loop:
files_to_process = sorted(candidates, key=_sweep_priority)
```

## FIX 3: add --apply-scores flag to sweep subcommand

At end of sweep(), when --apply-scores flag is set, run a scoring pass on
all files that were modified during the sweep:

```python
# Track modified files during sweep (add to the loop):
modified_files = []
# ... in the improvement loop, after writing:
modified_files.append(fp)

# After loop ends, if --apply-scores:
if getattr(args, 'apply_scores', False):
    from cex_score import score_structural, score_rubric, update_quality
    print(f"\n[SCORE] Applying scores to {len(modified_files)} modified files...")
    for fp in modified_files:
        try:
            struct_raw, _ = score_structural(str(fp))
            rubric_raw, _, _ = score_rubric(str(fp))
            q = round((struct_raw + rubric_raw) / 2, 1)
            update_quality(str(fp), q)
            print(f"  {fp.name}: {q}")
        except Exception as e:
            print(f"  {fp.name}: score failed ({e})")
```

Add the argparse flag:
```python
sweep_parser.add_argument('--apply-scores', action='store_true',
    help='After sweep, write quality scores to all modified artifacts')
```

## VERIFICATION

```bash
# Test: pick 3 quality:null files and run heuristic evolve on them
# They should have quality: X.X after (not null)

# Find 3 null files in N02:
NULL_FILES=$(grep -rl "quality: null" N02_marketing/ | head -3 | tr '\n' ' ')
python _tools/cex_evolve.py single $(echo $NULL_FILES | cut -d' ' -f1) --target 9.0 --max-rounds 1

# Verify quality was written:
head -20 $(echo $NULL_FILES | cut -d' ' -f1) | grep quality

# Sanitize:
python _tools/cex_sanitize.py --check --scope _tools/
```

## IMPORTANT: ASCII-only rule

All code must be ASCII-only (0x00-0x7F). No emoji, no accented chars,
no smart quotes in the Python source. Use [OK], [FAIL], [WARN] instead of emoji.
Run `python _tools/cex_sanitize.py --check --scope _tools/` before committing.

## COMPLETION

```bash
git add _tools/cex_evolve.py
git commit -m "[N03] SCORE_REFORM M1b: heuristic->quality write + sweep priority + --apply-scores"
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'score_reform_m1b_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] heuristic mode writes quality: X.X after each file improvement
- [ ] sweep sorts quality:null files first
- [ ] --apply-scores flag added and functional
- [ ] 3 test artifacts go from quality:null to quality: X.X
- [ ] cex_sanitize.py passes
- [ ] signal sent: n03 -> score_reform_m1b_complete
