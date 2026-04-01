---
id: p11_qg_creation_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Creation Artifacts"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "quality-gate-builder"
domain: "creation"
quality: 8.9
tags: [quality-gate, creation, artifacts, governance, p11]
tldr: "Quality gate for newly created artifacts: ensures structural integrity, completeness, and production readiness with 8.0+ score threshold."
density_score: 0.92
---
## Definition
A creation quality gate evaluates newly built artifacts across all pillars before they enter the production pool. This gate ensures structural validity, content completeness, and adherence to CEX standards for any artifact kind during the creation phase.

| Property | Value |
|----------|-------|
| Metric | creation_quality_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All newly created artifacts before pool acceptance |

## HARD Gates
All checks must pass. Single failure = immediate rejection.

| ID  | Criterion | Failure Action |
|-----|-----------|----------------|
| H01 | YAML frontmatter parses without syntax errors | block |
| H02 | ID follows pillar naming convention (pXX_kind_slug) | block |
| H03 | ID equals filename stem exactly | block |
| H04 | Kind field matches valid artifact type in kinds registry | block |
| H05 | Quality field is null at creation time (no self-scoring) | block |
| H06 | All required frontmatter fields present and non-empty | block |
| H07 | Body content >= 200 characters (prevents stub artifacts) | block |
| H08 | Pillar assignment matches artifact kind schema | block |
| H09 | File size within schema limits for artifact type | block |
| H10 | No placeholder text ({{}} brackets) in final output | block |

## SOFT Gates
Weighted scoring dimensions. Total weights = 100%.

| ID  | Criterion | Weight | Scoring Method |
|-----|-----------|--------|----------------|
| S01 | Structural completeness (all required sections present) | 20% | binary |
| S02 | Content density >= 0.80 (information per byte ratio) | 15% | graduated |
| S03 | Domain expertise evident (technical accuracy, specificity) | 20% | graduated |
| S04 | Examples or concrete implementation details included | 15% | binary |
| S05 | Clear boundaries defined (what IS vs what IS NOT) | 10% | graduated |
| S06 | Actionable content (user can execute or apply) | 10% | graduated |
| S07 | Proper tagging and metadata completeness | 5% | binary |
| S08 | Reference links or citations where appropriate | 5% | binary |

## Scoring Formula
```
aggregate_score = SUM(gate_score * weight for each SOFT gate)
final_score = aggregate_score * 10
PASS: all HARD gates pass AND final_score >= 8.0
FAIL: any HARD gate fails OR final_score < 8.0
```

## Actions
| Outcome | Score Range | Consequence |
|---------|-------------|-------------|
| GOLDEN | >= 9.5 | Immediate pool acceptance; flag as reference example |
| PUBLISH | >= 8.0 | Pool acceptance; production ready |
| REVIEW | 7.0-7.9 | Return to author with dimensional feedback; one revision allowed |
| REJECT | < 7.0 | Block from pool; requires substantial rework before resubmission |

## Bypass Policy
| Field | Value |
|-------|-------|
| Conditions | Experimental artifact in active design phase with unstable schema |
| Approver | Nucleus lead + pillar owner joint approval required |
| Audit Trail | Record in `.cex/runtime/decisions/bypasses.log` with timestamp, approver signatures, and justification |
| Expiry | 7 days from bypass grant; artifact must achieve full compliance before expiry |
| Non-bypassable | H01 (YAML syntax), H05 (quality null), H10 (no placeholders) |