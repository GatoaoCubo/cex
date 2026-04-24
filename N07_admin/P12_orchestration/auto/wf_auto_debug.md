---
id: p12_wf_auto_debug
kind: workflow
8f: F8_collaborate
pillar: P12
title: "Auto-Debug — Root cause analysis on execution errors"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: error_during_execution
quality: 9.0
tags: [workflow, auto, n07, debug, rca, itil, 5whys]
tldr: "When a tool, test, or dispatch fails, auto-diagnose: classify error, check logs, apply known fix or escalate."
density_score: 0.91
related:
  - p10_lr_bugloop_builder
  - p01_kc_self_healing_skill
  - p12_wf_auto_diagnose
  - p11_bl_agent_group_execution
  - p01_kc_self_healing
  - p12_wf_auto_health
  - p01_kc_feedback_loops
  - p01_kc_error_recovery
  - p12_wf_auto_review
  - p01_kc_bugloop
---

# Auto-Debug

## Trigger
Any error during: tool execution, test run, compilation, dispatch, or 8F pipeline.

## Industry Pattern
ITIL Incident Management + 5-Whys root cause analysis.

## Steps

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | Capture error | stderr / exit code / traceback | Error text |
| 2 | Classify error type | Pattern matching | Category |
| 3 | Check known fixes | `learning_records/` | Prior fix if exists |
| 4 | Apply auto-fix | Depends on category | Fix attempt |
| 5 | Retry operation | Re-run failed command | Pass/fail |
| 6 | Record learning | `cex_memory_update.py` | Learning for next time |
| 7 | Escalate if unresolved | Flag to user | "Fix needed: {details}" |

## Error Categories

| Category | Pattern | Auto-Fix |
|----------|---------|----------|
| Import error | `ModuleNotFoundError` | `pip install {module}` |
| File not found | `FileNotFoundError` | Check path, suggest correct path |
| YAML syntax | `yaml.scanner.ScannerError` | Show line, suggest fix |
| Compile fail | `cex_compile.py` exit 1 | Check frontmatter, fix common issues |
| Doctor fail | Missing builder spec | Check archetype dir, suggest creation |
| Test fail | `pytest` assertion | Show expected vs actual, check recent changes |
| Git conflict | `CONFLICT` in merge | Show conflicting files, suggest resolution |
| Dispatch fail | Spawn error | Check boot file exists, check CLI available |

## Failure Mode
Auto-fix fails after 2 retries → escalate to user with full context: error, diagnosis, attempted fixes, suggested manual action.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_bugloop_builder]] | upstream | 0.33 |
| [[p01_kc_self_healing_skill]] | upstream | 0.30 |
| [[p12_wf_auto_diagnose]] | sibling | 0.30 |
| [[p11_bl_agent_group_execution]] | upstream | 0.28 |
| [[p01_kc_self_healing]] | upstream | 0.28 |
| [[p12_wf_auto_health]] | sibling | 0.27 |
| [[p01_kc_feedback_loops]] | upstream | 0.27 |
| [[p01_kc_error_recovery]] | upstream | 0.26 |
| [[p12_wf_auto_review]] | sibling | 0.23 |
| [[p01_kc_bugloop]] | upstream | 0.23 |
