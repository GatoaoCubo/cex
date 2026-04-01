---
id: p12_wf_auto_review
kind: workflow
pillar: P12
title: "Auto-Review — Validate nucleus output on arrival"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: nucleus_output_arrives
quality: null
tags: [workflow, auto, n07, review, quality, gate]
tldr: "When a nucleus signals complete, auto-review its output: frontmatter, compilation, quality gate, doctor check."
density_score: 0.92
---

# Auto-Review

## Trigger
Nucleus signals complete (`signal_writer.py`), or new commits detected from a dispatched nucleus.

## Industry Pattern
Pull Request review / code review gate. Output doesn't ship until it passes review.

## Steps

| # | Action | Tool | Pass Criteria |
|---|--------|------|---------------|
| 1 | Detect new artifacts | `git log --oneline -N` | Commits from nucleus |
| 2 | Compile all new files | `cex_compile.py {paths}` | 100% compile success |
| 3 | Run doctor on changed builders | `cex_doctor.py` | 0 new FAIL |
| 4 | Check frontmatter completeness | grep for required fields | All present |
| 5 | Check quality:null policy | `grep "quality: null"` on new files | quality:null (not self-scored) |
| 6 | Check density | `grep density_score` | >= 0.85 |
| 7 | Verify signal was sent | `ls .cex/runtime/signals/{nucleus}_*` | Signal exists |

## Verdicts

| Result | Action |
|--------|--------|
| All pass | Mark task complete. Proceed to consolidate. |
| Minor issues (WARN) | Auto-fix if possible (compile, add missing field). Log. |
| Major failure | Flag to user: "N0X output needs attention: {issue}" |

## Auto-Fix Capabilities
- Missing `quality: null` → inject it
- Missing compilation → run `cex_compile.py`
- Missing signal → write signal with score from review

## Failure Mode
Review itself fails → log error, mark output as "unreviewed," proceed.
