---
id: p11_qg_operations_quality_gate
kind: quality_gate
pillar: P11
title: "Operations Nucleus Quality Gate"
version: "1.0.0"
created: "2023-10-30"
updated: "2023-10-30"
author: "quality-gate-builder"
domain: "operations"
quality: null
tags: [quality-gate, operations, pre-deployment]
tldr: "Quality gate for operations ensuring compliance with operational standards before deployment."
density_score: 0.85
---

## Hard Gates

| gate_id | description                                | threshold | block |
|---------|--------------------------------------------|-----------|-------|
| H01     | YAML frontmatter parses correctly          | 100%      | true  |
| H02     | ID matches the pattern /^p11_qg_[a-z][a-z0-9_]+$/ | 100%  | true  |
| H03     | ID equals filename stem                    | 100%      | true  |
| H04     | kind is 'quality_gate'                      | 100%      | true  |
| H05     | Quality is set to null                     | 100%      | true  |
| H06     | All required fields are present in artifact | 100%     | true  |

## Soft Gates

| gate_id | description                                | max_penalty | weight |
|---------|--------------------------------------------|-------------|--------|
| S01     | Completeness of operational procedures     | 10%         | 0.35   |
| S02     | Correctness of alignment with standard protocols | 10%   | 0.35   |
| S03     | Usability and clarity of instructions      | 10%         | 0.30   |

## Scoring Formula

final_score = (S01 * 0.35) + (S02 * 0.35) + (S03 * 0.30)
The gate passes if all HARD gates pass and final_score >= 0.80.

## Bypass Policy

- Authorized Personnel: Admin
- Condition: Critical operational need with sufficient justification
- Logging Requirement: Bypass must be logged with timestamp, actor, and justification in the deployment logs.

## Audit Trail

Every gate evaluation logs the following:
- Timestamp
- Evaluator ID
- Artifact ID and version
- Passed/Failed status of each HARD gate
- Scores for each SOFT gate
- Final score
- Any bypass actions performed
Retention policy: Logs are to be retained for 18 months in the operations archive system.
---
