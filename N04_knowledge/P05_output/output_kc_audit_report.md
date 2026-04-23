---
id: p10_out_kc_audit_report
kind: output
pillar: P10
title: "Output: KC Audit Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.1
tags: [output, n04, audit, coverage, staleness, density]
tldr: "KC health report: coverage, staleness, density stats, top gaps."
density_score: 0.91
related:
  - output_kc_quality_audit_20260408
  - p06_schema_freshness
  - bld_examples_lifecycle_rule
  - p10_out_gap_report
  - p06_schema_source_quality
  - p10_out_executive_summary
  - p11_qg_audit_log
  - p06_schema_database
  - p10_out_sql_migration
  - p11_reward_signal
---

# Output: KC Audit Report

## Template
```markdown
# KC Audit Report
**Date**: {{DATE}} | **Total KCs**: {{COUNT}} | **Health**: {{GOOD|AGING|STALE}}

## Summary
| Metric | Value | Threshold | Status |
|--------|-------|-----------|---------|
| Total KCs | {{N}} | 99 target | {{PROGRESS}} |
| Avg Density | {{SCORE}} | >0.85 | {{PASS/FAIL}} |
| Fresh (<90d) | {{N}} ({{%}}) | >60% | {{HEALTHY/CONCERN}} |
| Stale (>90d) | {{N}} ({{%}}) | <40% | {{ACCEPTABLE/ACTION}} |
| Missing (by kind) | {{N}} | 0 ideal | {{CRITICAL/MINOR}} |

## Staleness Distribution
| State | Count | % | Action Required |
|-------|-------|---|-----------------|
| ✅ Fresh (<90d) | {{N}} | {{%}} | Monitor |
| 🟡 Aging (90-180d) | {{N}} | {{%}} | Review queue |
| ⚠️ Stale (180-365d) | {{N}} | {{%}} | Update priority |
| ❌ Deprecated (>365d) | {{N}} | {{%}} | Archive or rewrite |

## Top 5 Critical Gaps
1. **{{KIND}}**: no KC exists → {{IMPACT_SCORE}}/10 impact → build in {{SPRINT}}
2. **{{KIND}}**: no KC exists → {{IMPACT_SCORE}}/10 impact → build in {{SPRINT}}
3. **{{KIND}}**: no KC exists → {{IMPACT_SCORE}}/10 impact → build in {{SPRINT}}
4. **{{KIND}}**: no KC exists → {{IMPACT_SCORE}}/10 impact → build in {{SPRINT}}
5. **{{KIND}}**: no KC exists → {{IMPACT_SCORE}}/10 impact → build in {{SPRINT}}

## Top 5 Stalest KCs (Update Priority)
1. **{{KC_ID}}**: {{DAYS}} days old → density {{SCORE}} → {{HIGH/MED/LOW}} priority
2. **{{KC_ID}}**: {{DAYS}} days old → density {{SCORE}} → {{HIGH/MED/LOW}} priority
3. **{{KC_ID}}**: {{DAYS}} days old → density {{SCORE}} → {{HIGH/MED/LOW}} priority
4. **{{KC_ID}}**: {{DAYS}} days old → density {{SCORE}} → {{HIGH/MED/LOW}} priority
5. **{{KC_ID}}**: {{DAYS}} days old → density {{SCORE}} → {{HIGH/MED/LOW}} priority

## Action Items (This Sprint)
- **Build**: {{N}} missing KCs ({{ESTIMATED_HOURS}}h total)
- **Update**: {{N}} stale KCs ({{ESTIMATED_HOURS}}h total)
- **Archive**: {{N}} deprecated KCs ({{ESTIMATED_HOURS}}h total)
- **Next audit**: {{DATE}} (30 days)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[output_kc_quality_audit_20260408]] | upstream | 0.25 |
| [[p06_schema_freshness]] | upstream | 0.24 |
| [[bld_examples_lifecycle_rule]] | related | 0.24 |
| [[p10_out_gap_report]] | sibling | 0.24 |
| [[p06_schema_source_quality]] | upstream | 0.24 |
| [[p10_out_executive_summary]] | sibling | 0.20 |
| [[p11_qg_audit_log]] | downstream | 0.19 |
| [[p06_schema_database]] | upstream | 0.18 |
| [[p10_out_sql_migration]] | sibling | 0.18 |
| [[p11_reward_signal]] | downstream | 0.17 |
