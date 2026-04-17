---
mission: VERTICAL_DENSIFICATION
nucleus: n05
wave: W1
created: 2026-04-17
priority: CRITICAL
effort: opus_high
---

# N05 VERTICAL_DENSIFICATION W1: Path Correction + Self-Improvement Loop

## SPEC REFERENCE
Read first: `_docs/specs/spec_vertical_densification.md`
Your wave: W1 (sequential -- must complete before W2 launches)

## TASK 1: Fix 18 Stale Python Path References (BLOCKING)

STRUCT_ALIGN V2 moved root P01-P12 dirs into N00_genesis/.
18 Python files in `_tools/` still use the old flat paths.

### Verification (run first):
```bash
grep -rn '"P0[0-9]' _tools/*.py | grep -v "N00_genesis" | grep -v "compiled" | grep -v ".pyc"
```
This should list ~18+ stale references.

### The Fix Pattern:
Every occurrence of:
```python
"P01_knowledge"   ->  "N00_genesis/P01_knowledge"
"P02_model"       ->  "N00_genesis/P02_model"
"P03_prompt"      ->  "N00_genesis/P03_prompt"
"P04_tools"       ->  "N00_genesis/P04_tools"
"P05_output"      ->  "N00_genesis/P05_output"
"P06_schema"      ->  "N00_genesis/P06_schema"
"P07_evals"       ->  "N00_genesis/P07_evals"
"P08_architecture" -> "N00_genesis/P08_architecture"
"P09_config"      ->  "N00_genesis/P09_config"
"P10_memory"      ->  "N00_genesis/P10_memory"
"P11_feedback"    ->  "N00_genesis/P11_feedback"
"P12_orchestration" -> "N00_genesis/P12_orchestration"
```

Known files with stale refs (verify + fix all):
- `_tools/cex_pipeline.py`
- `_tools/cex_forge.py`
- `_tools/cex_init.py`
- `_tools/cex_feedback.py`
- `_tools/cex_retriever.py`
- `_tools/cex_schema_hydrate.py`
- `_tools/cex_prompt_layers.py`
- `_tools/cex_skill_loader.py`
- `_tools/cex_auto.py`
- `_tools/cex_8f_motor.py`
- `_tools/cex_8f_runner.py`
- `_tools/cex_run.py`
- `_tools/cex_compile.py`
- `_tools/cex_doctor.py`
- `_tools/cex_memory_select.py`
- `_tools/cex_quality_monitor.py`
- `_tools/cex_prompt_cache.py`
- `_tools/cex_flywheel_audit.py`

### Verification after fix:
```bash
grep -rn '"P0[0-9]' _tools/*.py | grep -v "N00_genesis" | grep -v "compiled" | grep -v ".pyc"
```
MUST return empty (0 lines).

### Run system test:
```bash
python _tools/cex_system_test.py
```
Fix any failures introduced by the path corrections.

## TASK 2: Create self_improvement_loop for N05 (gap from SELF_ASSEMBLY)

N05 SELF_ASSEMBLY did not produce `self_improvement_loop_n05.md`. Create it now.

Save path: `N05_operations/P11_feedback/self_improvement_loop_n05.md`

Kind: self_improvement_loop
Pillar: P11
Nucleus: N05
Sin lens: Gating Wrath -- nothing passes without meeting SLO

Content: autonomous reliability evolution loop that:
- Scans for quality < 8.5 in P07/P09 artifacts
- Triggers re-evaluation via cex_evolve.py
- Updates SLO thresholds based on empirical failure rates
- Enforces shift-left: push validation earlier in the pipeline

## COMPLETION SEQUENCE

```bash
# 1. Verify stale paths fixed
grep -rn '"P0[0-9]' _tools/*.py | grep -v "N00_genesis" | grep -v "compiled"
# Must return 0 lines

# 2. Compile
python _tools/cex_compile.py --all

# 3. System test
python _tools/cex_system_test.py

# 4. Commit
git add _tools/ N05_operations/ && git commit -m "[N05] VERTICAL_DENSIFICATION W1: fix 18 stale P0x paths -> N00_genesis/P0x + self_improvement_loop"

# 5. Signal
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'vert_dens_w1_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] grep returns 0 stale path refs in _tools/*.py
- [ ] cex_system_test.py passes (or regression count does not increase)
- [ ] N05_operations/P11_feedback/self_improvement_loop_n05.md created
- [ ] git commit with [N05] VERTICAL_DENSIFICATION W1 message
- [ ] signal sent: n05 -> vert_dens_w1_complete
