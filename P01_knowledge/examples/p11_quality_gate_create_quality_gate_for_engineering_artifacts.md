---
id: p11_qg_engineering_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Engineering Artifacts"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "quality-gate-builder"
domain: "engineering"
quality: 8.9
tags: [quality-gate, engineering, technical-quality, governance]
tldr: "Pre-deployment gate for engineering artifacts: 8 HARD checks + 6-dimension scoring >= 8.0 for production readiness."
density_score: 0.87
---
## Definition

| Property | Value |
|----------|-------|
| Metric | engineering_quality_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All engineering artifacts before production deployment or pool merge |

Quality gate for engineering artifacts including system designs, code components, technical specifications, architecture decisions, and engineering process documentation. Ensures technical correctness, maintainability, and operational readiness.

## HARD Gates

Failure on any single gate results in immediate rejection regardless of SOFT scores.

| ID | Criterion | Failure Action |
|----|-----------|---------------|
| H01 | Frontmatter parses as valid YAML without syntax errors | block |
| H02 | ID follows required namespace pattern for artifact kind | block |
| H03 | ID field exactly matches filename stem | block |
| H04 | Kind field contains correct literal value for artifact type | block |
| H05 | Quality field is null at authoring time | block |
| H06 | All required frontmatter fields present and non-empty | block |
| H07 | Technical specifications include concrete implementation details | block |
| H08 | Engineering standards compliance documented with specific standard references | block |

## SOFT Scoring

Weighted dimensions contributing to final quality score. Each dimension scored 0.0-1.0.

| ID | Dimension | Weight | Scoring Method |
|----|-----------|--------|---------------|
| S01 | Technical Accuracy | 25% | graduated (partial credit for minor technical issues) |
| S02 | Completeness | 20% | graduated (partial credit for missing optional sections) |
| S03 | Maintainability | 20% | binary (0 if lacks maintenance documentation, weight if present) |
| S04 | Documentation Quality | 15% | graduated (partial credit for incomplete but present documentation) |
| S05 | Standards Compliance | 10% | binary (0 if violates standards, weight if compliant) |
| S06 | Operational Usability | 10% | graduated (partial credit for limited but functional usability) |

**Scoring Formula**:
```
aggregate_score = (S01_score * 0.25) + (S02_score * 0.20) + (S03_score * 0.20) + (S04_score * 0.15) + (S05_score * 0.10) + (S06_score * 0.10)
final_score = aggregate_score * 10
PASS condition: all HARD gates pass AND final_score >= 8.0
```

## Actions

| Outcome | Score Range | Consequence |
|---------|-------------|-------------|
| GOLDEN | >= 9.5 | Artifact proceeds to golden pool as reference implementation |
| PUBLISH | 8.0 - 9.4 | Artifact approved for production deployment |
| REVIEW | 7.0 - 7.9 | Artifact returned with specific improvement requirements |
| REJECT | < 7.0 | Artifact blocked from deployment, requires substantial rework |

## Bypass Policy

| Field | Requirements |
|-------|-------------|
| Conditions | Emergency deployment with documented risk assessment and mitigation plan |
| Approver | Engineering Lead AND Security Lead dual approval required |
| Audit Trail | Record in engineering_gate_bypasses.log with timestamp, approvers, risk assessment, and remediation timeline |
| Expiry | Bypass valid for maximum 72 hours; artifact must achieve full compliance within expiry period |

**Non-bypassable Gates**: H01 (YAML syntax), H05 (quality field), H08 (standards compliance) cannot be bypassed under any circumstances.