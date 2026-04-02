---
id: p11_qg_creation_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Creation Artifacts"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "quality-gate-builder"
domain: "creation"
target_kind: "creation_artifacts"
delivery_threshold: 8.0
bypass_policy: "owner"
dimensions: ["structural", "semantic", "operational", "density", "completeness"]
quality: 9.1
tags: [quality-gate, creation, artifacts, P11, governance]
tldr: "Quality gate for creation artifacts: structural validity + 5-dimension scoring >= 8.0 before pool acceptance"
density_score: 0.89
---
## Definition

| Property | Value |
|----------|-------|
| Metric | creation_quality_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All artifacts produced through CEX creation pipeline before pool merge |

## HARD Gates

Failure on any single gate results in immediate rejection regardless of SOFT score.

| ID | Criterion | Failure Action |
|----|-----------|----------------|
| H01 | Frontmatter parses as valid YAML without errors | block |
| H02 | ID matches required namespace pattern for artifact kind | block |
| H03 | ID equals filename stem exactly | block |
| H04 | Kind field matches literal artifact type | block |
| H05 | Quality field is null at creation time | block |
| H06 | All schema-required frontmatter fields present and non-empty | block |
| H07 | Body content contains minimum viable sections for artifact type | block |
| H08 | Total artifact size within pillar maximum byte limits | block |

## SOFT Gates

Weighted dimensions contributing to aggregate quality score.

| ID | Criterion | Weight | Scoring Method |
|----|-----------|--------|----------------|
| S01 | Density score >= 0.80 (content-to-noise ratio) | 0.25 | graduated |
| S02 | Completeness: all template sections filled with substantive content | 0.20 | graduated |
| S03 | Actionability: contains concrete examples, commands, or implementation steps | 0.20 | binary |
| S04 | Domain alignment: content specifically addresses target domain/use case | 0.15 | graduated |
| S05 | Structural consistency: follows established patterns for artifact kind | 0.10 | binary |
| S06 | Reference quality: includes relevant sources, links, or citations where appropriate | 0.10 | graduated |

**Weight total verification**: 0.25 + 0.20 + 0.20 + 0.15 + 0.10 + 0.10 = 1.00 ✓

## Scoring Formula

```
aggregate_score = SUM(gate_score * weight for each SOFT gate)
final_score = aggregate_score * 10

PASS condition: (all HARD gates pass) AND (final_score >= 8.0)
FAIL condition: (any HARD gate fails) OR (final_score < 8.0)
```

## Actions

| Outcome | Consequence |
|---------|-------------|
| PASS >= 9.5 | Artifact promoted to GOLDEN tier; used as reference template |
| PASS >= 8.0 | Artifact accepted into pool; marked production-ready |
| REVIEW >= 7.0 | Artifact returned with scored feedback; one revision cycle allowed |
| REJECT < 7.0 | Artifact blocked from pool; requires substantial rework |

## Bypass Policy

| Field | Value |
|-------|-------|
| Who may override | Artifact creator or pillar owner |
| Conditions | SOFT score 7.0-7.9 with documented justification; experimental artifact kinds in active development |
| Audit requirement | Record bypass in `.cex/runtime/audits/gate_bypasses.log` with timestamp, approver, reason, and expiry date |
| Non-bypassable gates | H01 (YAML parsing), H05 (quality null) - these ensure system integrity |
| Expiry | 7 days from bypass grant; artifact must achieve full compliance before expiry |