---
id: self_improvement_loop_n05
kind: self_improvement_loop
pillar: P11
title: "N05 Quality Gate Evolution Loop"
version: "1.0"
created: "2026-04-17"
updated: "2026-04-17"
author: n05_operations
domain: quality-gate-enforcement
quality: null
tags: [self_improvement_loop, operations, quality, N05, slo, shift_left, gating_wrath]
tldr: "Autonomous loop: scan artifacts below SLO, trigger cex_evolve.py, update thresholds from failure rates, push validation earlier in pipeline."
loop_stages:
  - SCAN
  - TRIAGE
  - EVOLVE
  - VERIFY
  - CALIBRATE
  - SHIFT_LEFT
trigger: scheduled
frequency: daily
slo_threshold: 8.5
escalation_threshold: 7.0
max_retries: 2
---

# N05 Quality Gate Evolution Loop

## Purpose

Autonomous quality enforcement loop driven by Gating Wrath. Nothing passes without meeting SLO. Artifacts below threshold are evolved, thresholds are recalibrated from empirical data, and validation gates are pushed earlier in the pipeline.

## Loop Stages

### SCAN

```bash
python _tools/cex_quality_monitor.py --snapshot --threshold 8.5
```

| Target | Source | Metric |
|--------|--------|--------|
| P07_evals artifacts | `N05_operations/P07_evals/` | quality frontmatter field |
| P09_config artifacts | `N05_operations/P09_config/` | quality frontmatter field |
| All nucleus artifacts | `N01-N07_*/P*/` | quality frontmatter field |

Output: list of artifacts with `quality < 8.5` or `quality: null`.

### TRIAGE

| Quality Range | Action | Priority |
|---------------|--------|----------|
| < 7.0 | Immediate evolve + N07 escalation signal | CRITICAL |
| 7.0 - 8.0 | Batch evolve, next cycle | HIGH |
| 8.0 - 8.5 | Heuristic pass only | MEDIUM |
| >= 8.5 | No action | PASS |
| null | Score first via `cex_score.py`, then re-triage | UNKNOWN |

### EVOLVE

```bash
python _tools/cex_evolve.py --target <artifact_path> --mode heuristic --threshold 8.5
python _tools/cex_evolve.py --target <artifact_path> --mode agent --threshold 9.0
```

| Mode | Cost | When |
|------|------|------|
| heuristic | 0 tokens | First pass, structural fixes (frontmatter, density, naming) |
| agent | LLM call | When heuristic cannot reach 8.5, quality delta > 1.0 |

Max 2 retries per artifact per cycle. If still below SLO after retries, flag for manual review.

### VERIFY

```bash
python _tools/cex_score.py --apply <artifact_path>
python _tools/cex_doctor.py --check <artifact_path>
python _tools/cex_compile.py <artifact_path>
```

Gate: artifact must pass all three. If `cex_doctor.py` reports structural issues, return to EVOLVE.

### CALIBRATE

Update SLO thresholds based on empirical failure rates from the last 30 days.

| Metric | Calculation | Action |
|--------|-------------|--------|
| Failure rate | `count(quality < 8.5) / total_artifacts` | If < 5%, raise SLO to 9.0 |
| Regression rate | `count(quality_decreased)` / `total_scored` | If > 10%, investigate root cause |
| Evolve success rate | `count(improved) / count(attempted)` | If < 50%, review evolve prompts |

Threshold updates written to: `.cex/config/quality_slo.yaml`

### SHIFT_LEFT

Push validation earlier in the pipeline based on failure patterns.

| Failure Pattern | Shift-Left Action |
|-----------------|-------------------|
| Repeated frontmatter failures | Add F1 CONSTRAIN pre-check to builder ISOs |
| Density below 0.85 | Add F6 PRODUCE density gate before F7 |
| Missing cross-references | Add F3 INJECT verification step |
| Naming convention violations | Add F1 naming validation to pre-commit hook |

Implementation: update `_tools/cex_hooks.py` pre-commit checks and builder `bld_instruction_*.md` ISOs.

## Completion Signal

```python
from _tools.signal_writer import write_signal
write_signal('n05', 'quality_loop_complete', avg_quality)
```

## Integration

| System | Connection |
|--------|-----------|
| `cex_quality_monitor.py` | SCAN data source |
| `cex_evolve.py` | EVOLVE engine |
| `cex_score.py` | VERIFY scorer |
| `cex_doctor.py` | VERIFY structural check |
| `cex_hooks.py` | SHIFT_LEFT enforcement point |
| `.cex/config/quality_slo.yaml` | CALIBRATE persistence |
| `signal_writer.py` | Completion notification to N07 |
