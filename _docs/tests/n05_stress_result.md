---
test: stress_test_p_mode
nucleus: N05
date: 2026-04-06
---

# N05 Stress Test Results: -p Mode Full Nucleus Simulation

## Step 1: cex_sanitize.py Line Count

- **File**: `_tools/cex_sanitize.py`
- **Lines**: 487

## Step 2: Sanitizer Check (boot/ scope)

```
Scanned: 37 files
Clean:   37
Dirty:   0
Issues:  0 non-ASCII chars
```

**Result**: ALL CLEAN

## Step 3: cex_doctor.py Health Check

```
Builders:       119
Total files:    1547 (expected 1547)
Total size:     4446.9 KB
Avg density:    0.98
Oversized:      0 files
No frontmatter: 0 files
Result:         118 PASS | 1 WARN | 0 FAIL
```

| Metric | Value |
|--------|-------|
| PASS | 118 |
| WARN | 1 (tagline-builder: density 0.76 < 0.78) |
| FAIL | 0 |
| KC Coverage | 98/98 kinds |

## Summary

All 6 steps executed successfully. System health is green.
