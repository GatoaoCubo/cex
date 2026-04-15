---
id: n05_leverage_map_v2_verification
title: "N05 Operations - LEVERAGE_MAP_V2 Verification Cycle"
kind: quality_gate
pillar: P11
nucleus: n05
mission: LEVERAGE_MAP_V2
quality: null
tags: [verification, gap-analysis, tooling, operations]
created: 2026-04-15T16:00:00-03:00
---

## Verification Summary

### Tool Added: cex_coverage.py
**Status**: [PASS] Present, functional, tested

**What it does:**
- Scans kinds_meta.json (257 kinds registered)
- Finds artifacts by naming pattern per kind
- Reports pillar-by-pillar coverage %
- Lists gaps for backfill prioritization

**Output format (human + JSON):**
```
Pillar  Kinds  Covered  Coverage  Gaps
P01     28     5        17.9%     23 (agentic_rag, changelog, chunk_strategy...)
P02     22     3        13.6%     19 (agent_profile, axiom, boot_config...)
```

**Quality**: Correct math, excludes runtime + archetypes, useful for ops work.

---

## Coverage Snapshot (2026-04-15)

| Pillar | Total Kinds | Covered | Coverage % | Gap Count |
|--------|-------------|---------|-----------|-----------|
| P01    | 28          | 5       | 17.9      | 23        |
| P02    | 22          | 3       | 13.6      | 19        |
| P03    | 20          | 7       | 35.0      | 13        |
| P04    | 34          | 2       | 5.9       | 32        |
| P05    | 23          | 1       | 4.3       | 22        |
| P06    | 8           | 0       | 0.0       | 8         |
| P07    | 23          | 0       | 0.0       | 23        |
| P08    | 12          | 2       | 16.7      | 10        |
| P09    | 28          | 2       | 7.1       | 26        |
| P10    | 18          | 2       | 11.1      | 16        |
| P11    | 26          | 1       | 3.8       | 25        |
| P12    | 15          | 2       | 13.3      | 13        |
| **TOTAL** | **257**  | **30**  | **11.7%** | **227**   |

**Interpretation**: 30 of 257 kinds have at least 1 artifact built. 227 gaps remain. This is the backfill queue.

---

## New Wired Tools (since V1)

### Added in this cycle:
1. **cex_coverage.py** — Gap detection by pillar/kind (NEW)

### Existing ops tools (14 wired):
1. cex_doctor.py — Health check (naming, density, 13-file completeness)
2. cex_e2e_test.py — End-to-end test suite
3. cex_grid_test.py — Grid dispatch validation
4. cex_litellm_test.py — LiteLLM provider routing
5. cex_system_test.py — System validation (54 tests)
6. cex_sanitize.py — ASCII-only code check
7. cex_hooks.py — Pre-commit validation
8. cex_release_check.py — Release gate
9. cex_setup_validator.py — PC readiness
10. cex_score.py — Peer review scoring
11. cex_wave_validator.py — Wave validation
12. cex_provider_discovery.py — Provider health
13. cex_quota_check.py — Token quota pre-flight
14. cex_coverage.py — Artifact coverage (NEW)

---

## Still Missing (Critical Gaps for N05)

### Tier 1: Blocking operations
- **cex_regression.py** — Regression detection (compare past test runs vs current)
- **cex_ci_gate.py** — Pre-merge artifact validation (blocking gate before git push)
- **cex_code_review.py** — Automated code review (lint, style, security basics)

### Tier 2: Deployment readiness
- **cex_deploy_validator.py** — Artifact -> deploy readiness checklist
- **cex_rollback.py** — Automated git-aware rollback with signal cleanup
- **cex_incident_autopsy.py** — Post-incident root cause analysis

### Tier 3: Observability
- **cex_perf_profiler.py** — Token count, latency per artifact
- **cex_security_scan.py** — OWASP, injection, auth flow scanning
- **cex_audit_log.py** — Change tracking (who/what/when) for compliance
- **cex_sla_monitor.py** — SLA tracking (uptime, latency SLOs)

---

## Top 3 Priorities for Next Build Wave

### Priority 1: cex_regression.py
**Why critical:**
- Tests exist (system_test, e2e_test) but no baseline snapshot
- Cannot detect regressions without historical comparison
- Gates N07's autonomous mission mode (needs: "did we break anything?")

**Spec:**
- Read: latest test run results (JSON from cex_system_test.py)
- Load: past snapshot from `.cex/baseline/test_snapshot.json`
- Compare: metrics (pass/fail, error patterns, latency deltas)
- Report: regression table (metric, baseline, current, delta %)
- Gate: fail if metric regression > 5%

**Builder**: N05 | **Pillar**: P07 | **Kind**: regression_check | **Effort**: medium

---

### Priority 2: cex_code_review.py
**Why critical:**
- 105 tools in _tools/ -- no automated style checks
- N05 code quality is manual (peer review) only
- ASCII rule automated (cex_sanitize.py) but code review is not

**Spec:**
- Scan: _tools/*.py for violations
- Check: PEP 8 basics (indent, line length, naming)
- Check: ASCII-only rule (cex_sanitize.py wrapper)
- Check: docstring presence (>= 1 per public function)
- Check: type hints (>= 50% of functions)
- Report: violation table with fix suggestions
- Mode: --check (dry) vs --fix (auto)

**Builder**: N05 | **Pillar**: P07 | **Kind**: golden_test | **Effort**: medium

---

### Priority 3: cex_ci_gate.py
**Why critical:**
- cex_release_check.py covers releases only
- Need PRE-MERGE gate that blocks bad artifacts
- No blocking gate between "artifact built" and "git push"

**Spec:**
- Read: staged artifacts (git diff --name-only --cached)
- Check: exists + frontmatter + sanitize + doctor passing
- Check: kind in kinds_meta.json
- Check: quality >= 8.0 (cex_score.py)
- Report: per-artifact pass/fail
- Gate: exit 1 if any fails (blocks git commit)
- Integration: pre-commit hook in cex_hooks.py

**Builder**: N05 | **Pillar**: P07 | **Kind**: quality_gate | **Effort**: medium

---

## Metadata

- **Cycle**: LEVERAGE_MAP_V2 / Verify Cycle 1
- **Nucleus**: N05 Operations
- **Verified by**: cex_coverage.py (analysis verified manually)
- **Date**: 2026-04-15
- **Next milestone**: After regression_check, code_review, ci_gate built
