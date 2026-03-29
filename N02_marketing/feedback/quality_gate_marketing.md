---
id: p11_qg_marketing_nucleus
kind: quality_gate
pillar: P11
title: "Gate: Marketing Nucleus"
version: "1.0.0"
created: "2023-11-02"
updated: "2023-11-02"
author: "system"
domain: "marketing"
quality: null
tags: [quality-gate, marketing, pre-publish]
tldr: "Quality gate for marketing artifacts: 8 HARD checks + 6-dimension scoring >= 8.0"
density_score: 0.90
## Hard Gates
| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| H01     | Frontmatter parses without error | N/A | true |
| H02     | ID matches the pattern `^p11_qg_[a-z][a-z0-9_]+$` | N/A | true |
| H03     | ID equals filename stem | N/A | true |
| H04     | Kind matches `quality_gate` | N/A | true |
| H05     | Quality is set to null | N/A | true |
| H06     | Required frontmatter fields are present | 12 fields | true |
| H07     | Artifact size within limit | <= 4096 bytes | true |
| H08     | Title contains "Gate" | N/A | true |

## Soft Gates
| gate_id | description                                   | max_penalty | weight |
|---------|-----------------------------------------------|-------------|--------|
| S01     | Completeness (all required sections present)  | -2          | 20%    |
| S02     | Clarity (clear and unambiguous language)      | -1.5        | 15%    |
| S03     | Brevity (conciseness without losing meaning)  | -1          | 10%    |
| S04     | Consistency (consistent use of terminology)   | -1.5        | 15%    |
| S05     | Accuracy (factual correctness)                | -2          | 20%    |
| S06     | Relevance (contextual appropriateness)        | -2          | 20%    |

## Scoring Formula
aggregate_score = SUM(gate_score * weight for each SOFT gate)
PASS condition: all HARD gates pass AND aggregate_score >= 8.0

## Bypass Policy
Who may override: admin
Conditions for bypass: If the score is between 7.5 and 8.0, and the artifact is critical for a major campaign launch
Audit requirement: Must include timestamp, actor (admin), and justification in the audit log

## Audit Trail
Each gate evaluation must log the following:
- Gate ID
- Result (pass/fail)
- Timestamp
- Evaluator identity
- Comments on fail conditions
Retention Policy: Logs are retained for 2 years for auditing purposes.

---