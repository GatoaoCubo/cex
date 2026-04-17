---
id: p07_regression_check_operations
kind: regression_check
pillar: P07
title: Operations Regression Check Suite
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: regression-detection
quality: 9.0
tags: [regression_check, operations, N05, baseline, quality, delta]
tldr: "Regression check suite comparing current state against golden baselines across performance, quality scores, artifact counts, and test results."
density_score: 0.96
---

# Operations Regression Check Suite

## Overview

This regression check compares the current state of CEX operations against
established baselines. Regressions in performance, quality, artifact counts,
test results, or build health trigger investigation and potential deploy blocks.

## Regression Dimensions

### 1. Performance Regression

| metric | baseline_method | threshold | severity |
|--------|----------------|-----------|----------|
| API p95 latency | Previous benchmark run | > 10% increase | warning |
| API p95 latency | Previous benchmark run | > 25% increase | blocking |
| Startup time | Previous deploy | > 20% increase | warning |
| Memory utilization | Previous 24h average | > 30% increase | warning |
| DB query p95 | Previous benchmark | > 15% increase | warning |

### 2. Quality Score Regression

| metric | baseline_method | threshold | severity |
|--------|----------------|-----------|----------|
| Average artifact quality | Previous quality snapshot | > 0.5 decrease | blocking |
| Minimum artifact quality | Previous quality snapshot | < 7.0 | blocking |
| Builder health pass rate | Previous doctor run | Any decrease | warning |
| Flywheel audit score | Previous audit | > 5% decrease | warning |

### 3. Artifact Count Regression

| metric | baseline_method | threshold | severity |
|--------|----------------|-----------|----------|
| Total source artifacts | Previous count | Any decrease | warning |
| Compiled artifacts | Previous count | Uncompiled source exists | warning |
| Missing frontmatter | Previous scan | Any increase | blocking |
| Invalid YAML | Previous scan | Any increase | blocking |

### 4. Test Result Regression

| metric | baseline_method | threshold | severity |
|--------|----------------|-----------|----------|
| System test pass rate | Previous run (54 tests) | Any decrease | blocking |
| E2E test pass rate | Previous run | Any decrease | blocking |
| Doctor validation | Previous run (118 builders) | Any decrease | warning |

## Execution

```bash
# Run full regression check
python _tools/cex_quality_monitor.py --snapshot  # capture current state
python _tools/cex_quality_monitor.py --compare   # compare against baseline

# Performance regression
python _tools/cex_system_test.py --compare-baseline

# Artifact regression
python _tools/cex_doctor.py | grep -c "PASS"     # compare count vs baseline
python _tools/cex_compile.py --all --dry-run      # check compilation health
```

## Baseline Management

### Recording Baselines

```bash
# After a verified-good state:
python _tools/cex_quality_monitor.py --snapshot --tag baseline_$(date +%Y%m%d)
```

### Baseline Storage

| field | value |
|-------|-------|
| location | `.cex/runtime/baselines/` |
| format | YAML snapshot |
| naming | `baseline_{YYYYMMDD}_{dimension}.yaml` |
| retention | Last 10 baselines per dimension |

## Regression Report Format

```markdown
## Regression Report: {date}

### Status: {CLEAN | WARNING | BLOCKED}

| Dimension | Baseline | Current | Delta | Severity |
|-----------|----------|---------|-------|----------|

### Regressions Found
- {description with evidence}

### Actions Required
- {remediation steps}
```

## Integration with Deploy Pipeline

1. Regression check runs BEFORE deploy pre-flight
2. `blocking` severity regressions prevent `railway up`
3. `warning` severity regressions are logged but do not block
4. Regression check results are included in deploy evidence
