---
id: p10_out_gap_report
kind: output
pillar: P10
title: "Output: Gap Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [output, n04, gap, report, coverage, missing]
tldr: "Missing KC analysis by kind, domain, and nucleus. Prioritized gap list."
density_score: 0.91
related:
  - p10_out_taxonomy_map
  - p01_kc_gap_detection
  - leverage_map_v2_n05_verify
  - self_review_2026-04-02
  - self_audit_newpc
  - ai2ai_coverage_matrix_20260414
  - spec_mission_100pct_coverage
  - n02_self_review_2026-04-02
  - agent_card_n04
  - audit_intent_resolution
---

# Output: Gap Report

## Usage Guidelines

**When to use:**
- Before major knowledge expansion initiatives
- During quarterly knowledge audits
- When onboarding shows knowledge gaps
- Before nucleus capability assessments

**When NOT to use:**
- For individual artifact quality issues (use quality gates)
- For real-time knowledge needs (use retriever)
- For content updates vs missing content

**Anti-patterns:**
- Tracking gaps but never filling them
- Equal priority for all gaps (no impact weighting)
- Outdated reports driving current decisions

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_out_taxonomy_map]] | sibling | 0.29 |
| [[p01_kc_gap_detection]] | upstream | 0.26 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.25 |
| [[self_review_2026-04-02]] | upstream | 0.25 |
| [[self_audit_newpc]] | upstream | 0.22 |
| [[ai2ai_coverage_matrix_20260414]] | upstream | 0.22 |
| [[spec_mission_100pct_coverage]] | upstream | 0.21 |
| [[n02_self_review_2026-04-02]] | upstream | 0.21 |
| [[agent_card_n04]] | upstream | 0.20 |
| [[audit_intent_resolution]] | upstream | 0.20 |
