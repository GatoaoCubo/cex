---
id: p07_rc_ops
kind: regression_check
pillar: P07
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: regression-check-builder
name: "N05 Operations Known-Failure Registry"
baseline_ref: "incident_log/n05_ops_baseline_2026-04-17"
threshold: 0
metrics:
  - unicode_crash
  - orphan_processes
  - signal_storm
  - self_scoring
  - cross_nucleus_write
  - compile_drift
quality: 9.0
tags: [regression_check, n05_operations, known_failure, P07]
tldr: "Six known-failure patterns for N05 ops. Zero-tolerance (threshold=0). Blocks on any detection. Sin lens: Gating Wrath."
description: "Known-failure registry for N05 operations nucleus. Each pattern has a detection command, prevention control, severity, and source incident."
tool: promptfoo
comparison_mode: absolute
fail_action: block
notify: [n07_orchestrator, n05_ops_owner]
cadence: on_pr
scope: "N05_operations nucleus -- all .py tools and dispatch workflows"
density_score: 1.0
---

## Overview

Known-failure registry for N05 operations (sin lens: Gating Wrath). Six incident-derived
and policy-derived patterns that must never recur. Runs on every PR. Owned by N05;
escalates to N07 on any detection.

## Baseline

**baseline_ref**: `incident_log/n05_ops_baseline_2026-04-17`
Zero-failure snapshot captured after ascii-code-rule + orphan-cleanup confirmed green.

**Update policy**: Rotate only when a pattern is added or retired after 90 clean runs.

## Metrics

| ID | Detection | Severity | Source |
|----|-----------|----------|--------|
| `unicode_crash` | `cex_sanitize.py --check` exits 1 | critical | 2026-04-06 |
| `orphan_processes` | claude.exe age > 2h with no signal | high | 2026-04-11 |
| `signal_storm` | signal files > 100 in 60s | high | design review |
| `self_scoring` | `quality:` field != null in artifact | critical | day-1 rule |
| `cross_nucleus_write` | git diff outside N05_operations/ | high | RBAC policy |
| `compile_drift` | .md newer than .yaml counterpart | medium | operational |

**Threshold**: 0 absolute. Binary violations -- zero tolerance, zero variance.

## Failure Protocol

1. **fail_action**: block. No deploy proceeds with any detector red.
2. **Notify**: n07_orchestrator (immediate), n05_ops_owner (5 min).
3. **Remediation**:
   - `unicode_crash`: `cex_sanitize.py --fix` -> verify -> re-stage.
   - `orphan_processes`: `taskkill /F /PID <pid> /T` -> audit dispatch script.
   - `signal_storm`: add rate-gate (max 10/min) to signal-writer call site.
   - `self_scoring`: set `quality: null` -> recompile -> recommit.
   - `cross_nucleus_write`: revert to correct nucleus path -> audit handoff scope.
   - `compile_drift`: `cex_compile.py <path>` on all modified .md files.
4. **Escalation**: unresolved after 30 min -> N07 halts grid dispatch.
