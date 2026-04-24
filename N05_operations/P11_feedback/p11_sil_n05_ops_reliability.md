---
id: p11_sil_n05_ops_reliability
kind: self_improvement_loop
8f: F7_govern
pillar: P11
title: "N05 Ops Reliability Evolution Loop"
version: "1.0"
created: "2026-04-17"
updated: "2026-04-17"
author: n05_operations
domain: autonomous-reliability-engineering
quality: 9.1
tags: [self_improvement_loop, operations, reliability, N05, autonomous, feedback]
tldr: "N05 autonomous loop: scan infra health, classify failures, fix, verify, and signal N07 -- zero human intervention required."
loop_stages:
  - SCAN
  - CLASSIFY
  - PRIORITIZE
  - FIX
  - VERIFY
  - LEARN
  - REPORT
metrics:
  fix_success_rate: "fixed_count / total_issues_detected"
  mean_time_to_fix: "elapsed seconds between FIX start and VERIFY pass"
  regression_rate: "issues reopened within 7 days / total closed"
  loop_completion_rate: "loops reaching REPORT / loops triggered"
feedback_sources:
  - cex_doctor.py diagnostic output
  - cex_flywheel_audit.py 7-layer report
review_cycle: P7D
density_score: 1.0
related:
  - skill
  - p11_qg_admin_orchestration
  - doctor
  - p10_lr_bugloop_builder
  - p11_qg_artifact
  - agent_card_n07
  - p11_qg_knowledge
  - n07_output_orchestration_audit
  - ctx_cex_new_dev_guide
  - type_hint_retrofit_w6_20260415_2140
---

## Overview

Gating Wrath: infrastructure passes or it does not. This loop enforces that gate
autonomously. Every failure becomes a tracked work item that exits only via verified
fix or escalation record. NOT a bugloop (single-bug patch) nor learning_record
(passive capture).

## Triggers

| Trigger | Source | Condition |
|---------|--------|-----------|
| post-dispatch consolidation | N07 signal | nucleus completes any task |
| overnight evolve | scheduler | `review_cycle: P7D` (daily at 02:00) |
| quality regression | cex_quality_monitor.py | score drops > 0.5 below baseline |
| operator-initiated | /doctor --fix | manual invocation |

## Loop Stages

### S1: SCAN
```bash
python _tools/cex_doctor.py --json > .cex/runtime/sil/scan_doctor.json
python _tools/cex_flywheel_audit.py --json > .cex/runtime/sil/scan_flywheel.json
python _tools/cex_system_test.py --json > .cex/runtime/sil/scan_systest.json
```

### S2: CLASSIFY
Categorize each failure into one of four classes:

| Class | Examples | Auto-fixable |
|-------|----------|-------------|
| config_drift | stale model version, wrong path | yes |
| missing_artifact | absent ISO, no compiled YAML | yes |
| broken_compile | syntax error, encoding violation | yes |
| quality_regression | score < threshold, gate fail | yes |
| security | exposed secret, unsafe permission | NO -- escalate |

### S3: PRIORITIZE
Impact score `= severity * scope`:

| Dimension | blocking | warning |
|-----------|----------|---------|
| security | ESCALATE | P1 |
| shared (cross-nucleus) | P1 | P2 |
| local (N05-only) | P2 | P3 |

### S4: FIX

| Class | Command |
|-------|---------|
| config_drift | `python _tools/cex_model_updater.py --apply` |
| missing_artifact | dispatch builder sub-agent for missing kind |
| broken_compile | `python _tools/cex_sanitize.py --fix --scope <file>` |
| quality_regression | `python _tools/cex_evolve.py --target <file> --threshold 8.5` |

Max 3 attempts per issue; on 3rd failure -> ESCALATE.

### S5: VERIFY
Re-run the diagnostic that surfaced the failure:
```bash
python _tools/cex_doctor.py --check <scope>
python _tools/cex_compile.py <file>
```
Pass: zero failures for fixed item. Fail -> increment attempt counter.

### S6: LEARN
```bash
python _tools/cex_memory_update.py \
  --kind correction \
  --issue "<class>:<description>" \
  --fix "<command>" \
  --result "<pass|escalated>"
```
Record schema: `{issue_class, description, fix_applied, attempts, result, timestamp}`.

### S7: REPORT
Signal N07 with loop summary:
```python
from _tools.signal_writer import write_signal
write_signal('n05', 'sil_complete', {
    'fixed_count': N,
    'remaining_count': M,
    'escalated_count': K,
    'new_issues': [],
    'loop_duration_s': T
})
```

## Guard Rails

| Rail | Rule |
|------|------|
| max_attempts | 3 per issue; exceeded -> ESCALATE |
| security_fence | class=security NEVER auto-fixed; escalate to operator |
| scope_boundary | never modify outside N05_operations/ without N07 dispatch |
| rollback_trigger | new failures > fixed count -> rollback + ESCALATE |
| signal_required | loop always terminates with write_signal (never silent) |

## Metrics

| Metric | Target | Alert |
|--------|--------|-------|
| fix_success_rate | >= 0.90 | < 0.75 |
| mean_time_to_fix | <= 120s | > 300s |
| regression_rate | <= 0.05 | > 0.15 |
| loop_completion_rate | >= 0.95 | < 0.80 |

## Feedback Mechanisms

1. `cex_doctor.py` -- 118 structural checks; sensor for config drift + missing artifacts
2. `cex_flywheel_audit.py` -- 109 checks across 7 layers; detects doc-vs-practice divergence

Both sources feed S2 CLASSIFY independently. Divergence triggers P1 priority.

## Review Process

| Period | Activity | Owner |
|--------|----------|-------|
| P1D | Loop telemetry review (metrics vs targets) | N05 autonomous |
| P7D | Learning record audit -- are corrections reducing recurrence? | N05 autonomous |
| P30D | Guard rail effectiveness review -- escalation rate trending? | N07 + operator |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill]] | upstream | 0.27 |
| [[p11_qg_admin_orchestration]] | related | 0.27 |
| [[doctor]] | upstream | 0.26 |
| [[p10_lr_bugloop_builder]] | upstream | 0.25 |
| [[p11_qg_artifact]] | related | 0.25 |
| [[agent_card_n07]] | downstream | 0.24 |
| [[p11_qg_knowledge]] | related | 0.23 |
| [[n07_output_orchestration_audit]] | downstream | 0.22 |
| [[ctx_cex_new_dev_guide]] | related | 0.22 |
| [[type_hint_retrofit_w6_20260415_2140]] | upstream | 0.22 |
