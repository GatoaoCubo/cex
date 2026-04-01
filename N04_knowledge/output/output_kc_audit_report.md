---
id: p10_out_kc_audit_report
kind: output
pillar: P10
title: "Output: KC Audit Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: null
tags: [output, n04, audit, coverage, staleness, density]
tldr: "KC health report: coverage, staleness, density stats, top gaps."
density_score: 0.91
---

# Output: KC Audit Report

## Template
```markdown
# KC Audit Report
**Date**: {{DATE}} | **Total KCs**: {{COUNT}} | **Health**: {{GOOD|AGING|STALE}}

## Summary
| Metric | Value |
|--------|-------|
| Total KCs | {{N}} |
| Avg Density | {{SCORE}} |
| Fresh (<90d) | {{N}} ({{%}}) |
| Stale (>90d) | {{N}} ({{%}}) |
| Missing (by kind) | {{N}} |

## Staleness Distribution
| State | Count | % |
|-------|-------|---|
| ✅ Fresh | {{N}} | {{%}} |
| 🟡 Aging | {{N}} | {{%}} |
| ⚠️ Stale | {{N}} | {{%}} |
| ❌ Deprecated | {{N}} | {{%}} |

## Top 5 Gaps
1. {{KIND}}: no KC exists ({{IMPACT}})
2. ...

## Top 5 Stalest KCs
1. {{KC_ID}}: last updated {{DATE}} ({{DAYS}} days ago)
2. ...

## Recommendations
- {{ACTION_1}}
- {{ACTION_2}}
```
