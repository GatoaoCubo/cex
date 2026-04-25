---
id: p07_rc_ops
kind: regression_check
8f: F7_govern
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
related:
  - agent_card_n07
  - p01_kc_cex_orchestration_architecture
  - p12_wf_create_orchestration_agent
  - p01_kc_orchestration_best_practices
  - n07_output_orchestration_audit
  - spec_claude_native_hardening
  - self_audit_n05_codex_2026_04_15
  - agent_card_engineering_nucleus
  - leverage_map_v2_n05_verify
  - p03_sp_orchestration_nucleus
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

## Detection Commands

```bash
# unicode_crash
python _tools/cex_sanitize.py --check --scope _tools/ --scope boot/
# exit 1 = non-ASCII found in executable code

# orphan_processes (PowerShell)
Get-Process claude -EA SilentlyContinue |
  Where-Object { (New-TimeSpan $_.StartTime).TotalHours -gt 2 } |
  ForEach-Object { "$($_.Id) orphan: age $(((New-TimeSpan $_.StartTime).TotalMinutes))min" }

# signal_storm
find .cex/runtime/signals/ -name "*.json" -newer .cex/runtime/signals/.last_check -exec echo {} \; | wc -l
# > 100 in 60s = storm

# self_scoring
grep -rn "^quality: [0-9]" N05_operations/ --include="*.md" | grep -v "README"
# any match = violation

# cross_nucleus_write
git diff --name-only HEAD~1 | grep -v "^N05_operations/" | grep -v "^\.cex/"
# any match outside N05 scope = violation

# compile_drift
for f in $(find N05_operations -name "*.md" -newer N05_operations/compiled/ -type f 2>/dev/null); do
  echo "DRIFT: $f"; done
```

## Retirement Policy

A pattern is retired after:
1. 90 consecutive clean runs (no detections)
2. The root cause was architecturally eliminated (not just worked around)
3. N07 approves removal via decision manifest
4. The pattern is moved to `regression_check_ops_retired.md` with retirement date

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n07]] | downstream | 0.21 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.21 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.20 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.20 |
| [[n07_output_orchestration_audit]] | downstream | 0.19 |
| [[spec_claude_native_hardening]] | related | 0.19 |
| [[self_audit_n05_codex_2026_04_15]] | related | 0.19 |
| [[agent_card_engineering_nucleus]] | upstream | 0.19 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.18 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.18 |
