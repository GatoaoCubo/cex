---
id: p10_out_gap_report
kind: output
pillar: P10
title: "Output: Gap Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 8.7
tags: [output, n04, gap, report, coverage, missing]
tldr: "Missing KC analysis by kind, domain, and nucleus. Prioritized gap list."
density_score: 0.91
---

# Output: Gap Report

## Template
```markdown
# Knowledge Gap Report
**Date**: {{DATE}} | **Total Kinds**: {{KIND_COUNT}} | **Covered**: {{COVERED}} | **Missing**: {{MISSING}}

## Coverage by Kind Type

| Type | Total | With KC | Missing | Coverage |
|------|-------|---------|---------|----------|
| Core kinds | {{N}} | {{N}} | {{N}} | {{%}} |
| Domain kinds | {{N}} | {{N}} | {{N}} | {{%}} |
| Platform kinds | {{N}} | {{N}} | {{N}} | {{%}} |

## Top Priority Gaps

| # | Kind | Pillar | Impact | Reason |
|---|------|--------|--------|--------|
| 1 | {{KIND}} | {{PILLAR}} | High | {{WHY_IT_MATTERS}} |
| 2 | {{KIND}} | {{PILLAR}} | High | {{WHY_IT_MATTERS}} |

## Per-Nucleus Coverage
| Nucleus | .md Files | Schemas | Outputs | KCs | Score |
|---------|-----------|---------|---------|-----|-------|
| N01 | {{N}} | {{N}} | {{N}} | {{N}} | {{%}} |
| N02 | {{N}} | {{N}} | {{N}} | {{N}} | {{%}} |

## Recommendations
1. {{PRIORITY_1}}: create {{KC_NAME}} (impact: high)
2. {{PRIORITY_2}}: refresh {{KC_NAME}} (stale: {{DAYS}}d)
```
