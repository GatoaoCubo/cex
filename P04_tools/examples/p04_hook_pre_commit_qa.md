---
id: p04_hook_pre_commit_qa
name: pre_commit_quality_gate
description: "Pre-commit hook that runs 5-dimension quality scoring with escalation on repeated failures"
type: pre
trigger_event: pre_commit
script_path: records/core/python/quality_gate.py
lp: P04
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: quality-assurance
quality: 9.0
tags: [hook, pre-commit, quality, scoring, validation]
---

# Pre-Commit Quality Gate Hook

## Purpose
Validates staged files before commit using 5-dimension weighted scoring. Implements AP4+AP5 from Stripe Agentic Engineering: quality-based stop criteria instead of arbitrary retry counts.

## Scoring Dimensions (total = 10.0)
| Dimension | Weight | Checks |
|-----------|--------|--------|
| syntax | 3.0 | No syntax errors in staged files |
| structure | 2.0 | Valid Markdown headers, links |
| size | 1.5 | Files within limits (warn 50KB, block 100KB) |
| lint | 2.0 | Clean lint output |
| completeness | 1.5 | Files not empty, have meaningful content |

## Return Codes
- `0` = PASS (score >= threshold, default 8.0)
- `1` = WARN (score >= 7.0 but < threshold)
- `2` = FAIL (score < 7.0, auto-rollback recommended)

## Escalation
Tracks consecutive failures in `.claude/temp/qg_fail_count.json`. After 3+ consecutive fails, escalates with detailed report. Report saved to `.claude/temp/quality_report.json`.

## Usage
```bash
python records/core/python/quality_gate.py --threshold 8.0
python records/core/python/quality_gate.py --staged-only
python records/core/python/quality_gate.py --report-only
```
