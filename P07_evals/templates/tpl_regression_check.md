---
id: p07_regression_check
kind: regression_check
pillar: P07
version: 1.0.0
title: "Template — Regression Check"
tags: [template, regression, testing, monitoring, quality]
tldr: "Detects quality regressions by comparing current outputs against known-good baselines. Runs after model updates, prompt changes, or config modifications."
quality: 9.0
---

# Regression Check: [CHECK_NAME]

## Purpose
[WHAT regression this detects — quality drop after model update, format break after prompt change]

## Trigger
Run this check when:
- Model version changes (e.g., sonnet-3.5 → sonnet-4)
- System prompt or builder ISO modified
- Configuration change deployed
- Weekly scheduled (catch slow drift)

## Baseline

| Metric | Baseline Value | Tolerance |
|--------|---------------|-----------|
| Quality score avg | [8.8] | ±0.2 |
| Gate pass rate | [95%] | ±5% |
| Format compliance | [100%] | 0% (no tolerance) |
| Latency p50 | [1200ms] | ±20% |
| Retry rate | [10%] | ±5% |

## Test Execution
```bash
# Run regression suite
python _tools/cex_system_test.py --regression

# Compare against baseline
python -c "
baseline = {'quality_avg': 8.8, 'gate_pass': 0.95}
current = run_eval_suite()
for metric, expected in baseline.items():
    actual = current[metric]
    if abs(actual - expected) > TOLERANCE[metric]:
        alert(f'REGRESSION: {metric} {expected} -> {actual}')
"
```

## Comparison Report
```
## Regression Report — [DATE]
| Metric | Baseline | Current | Status |
|--------|----------|---------|--------|
| Quality avg | 8.8 | [N.N] | [PASS/FAIL] |
| Gate pass | 95% | [N%] | [PASS/FAIL] |
| Format | 100% | [N%] | [PASS/FAIL] |
```

## On Regression Detected
1. **Alert**: Notify via configured notifier (Slack, email)
2. **Bisect**: Identify which change caused regression
3. **Rollback**: Revert to last known-good configuration
4. **Fix forward**: If rollback not possible, fix and re-verify
5. **Update baseline**: After fix, update baseline values

## Quality Gate
- [ ] Baseline values documented with measurement date
- [ ] Tolerance thresholds defined per metric
- [ ] Trigger conditions listed (when to run)
- [ ] Rollback procedure documented
