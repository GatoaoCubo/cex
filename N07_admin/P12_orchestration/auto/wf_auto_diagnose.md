---
id: p12_wf_auto_diagnose
kind: workflow
pillar: P12
title: "Auto-Diagnose — Observability when health degrades"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: health_degraded
quality: 9.0
tags: [workflow, auto, n07, diagnose, observability, sre]
tldr: "When /doctor shows degradation (new FAILs, WARN increase, test regressions), deep-diagnose root cause and suggest fixes."
density_score: 0.91
related:
  - p12_wf_auto_debug
  - p12_wf_auto_review
  - p10_lr_bugloop_builder
  - p12_wf_auto_ship
  - p01_kc_feedback_loops
  - p12_wf_auto_rollback
  - p12_wf_auto_health
  - p01_kc_self_healing_skill
  - p01_kc_zero_touch
  - p01_kc_incident_response
---

# Auto-Diagnose

## Trigger
- Doctor shows more FAILs than last run
- Test suite has new failures
- Compilation rate drops below 100%
- Signal from nucleus reports error

## Industry Pattern
SRE observability — detect degradation, correlate signals, identify root cause.

## Steps

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | Run full doctor | `cex_doctor.py` | Current state |
| 2 | Compare with baseline | Previous doctor output / git log | Delta |
| 3 | Run full test suite | `pytest _tools/tests/ -q` | Failures list |
| 4 | Check recent commits | `git log --oneline -20` | What changed |
| 5 | Correlate | Match failures to recent changes | Root cause hypothesis |
| 6 | Suggest fix | Based on correlation | Fix plan |
| 7 | Auto-fix if safe | Compile fixes, frontmatter fixes | Attempt |
| 8 | Report | Summary to user | Diagnosis report |

## Diagnosis Report Format

```
━━━ Diagnosis Report ━━━
  Status:     DEGRADED (was HEALTHY)
  New FAILs:  2 (skill-builder, webhook-builder)
  Root Cause: commit abc123 removed bld_system_prompt_skill.md
  Suggested:  Recreate file or revert commit
  Auto-fix:   Not safe (needs content, not just structure)
━━━━━━━━━━━━━━━━━━━━━━━━
```

## Failure Mode
Can't determine root cause → show all signals (doctor, tests, recent commits) and let user decide.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_debug]] | sibling | 0.41 |
| [[p12_wf_auto_review]] | sibling | 0.32 |
| [[p10_lr_bugloop_builder]] | upstream | 0.30 |
| [[p12_wf_auto_ship]] | sibling | 0.29 |
| [[p01_kc_feedback_loops]] | upstream | 0.28 |
| [[p12_wf_auto_rollback]] | sibling | 0.26 |
| [[p12_wf_auto_health]] | sibling | 0.24 |
| [[p01_kc_self_healing_skill]] | upstream | 0.22 |
| [[p01_kc_zero_touch]] | upstream | 0.22 |
| [[p01_kc_incident_response]] | upstream | 0.21 |
