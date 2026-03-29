---
id: p11_qg_engineering_artifact
kind: quality_gate
pillar: P11
title: "Gate: Engineering Artifact Quality"
version: "1.0.0"
created: "2023-10-07"
updated: "2023-10-07"
author: "system"
domain: "engineering"
quality: null
tags: [quality-gate, engineering, artifact-assessment]
tldr: "Ensure engineering artifacts meet quality standards: 8 HARD checks + 5 SOFT scoring dimensions"
density_score: 0.90
---
## Definition
| Property | Value |
|----------|-------|
| Metric | aggregate_score |
| Threshold | 7.0 |
| Operator | >= |
| Scope | All engineering artifacts before deployment |

## HARD Gates
| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| H01 | Frontmatter YAML parses without errors | N/A | true |
| H02 | ID matches pattern /^p11_qg_[a-z][a-z0-9_]+$/ | N/A | true |
| H03 | ID matches filename stem | N/A | true |
| H04 | kind is exactly 'quality_gate' | N/A | true |
| H05 | quality field is null | N/A | true |
| H06 | All required frontmatter fields are present | N/A | true |
| H07 | Size does not exceed 2048 bytes | ≤ 2048 bytes | true |
| H08 | At least 2 external references validated | ≥ 2 references | true |

## SOFT Gates
| gate_id | description | max_penalty | weight |
|---------|-------------|-------------|--------|
| S01 | Completeness of documentation | 0.5 | 20% |
| S02 | Code quality and standard adherence | 0.5 | 20% |
| S03 | Design meets architectural guidelines | 0.5 | 20% |
| S04 | Evidence of testing and validation | 0.5 | 20% |
| S05 | Adherence to security best practices | 0.5 | 20% |

## Scoring Formula
final_score = (sum of (SOFT gate scores * respective weights)) * (hard_pass ? 1 : 0). The final score must be 7.0 or above for passing.

## Bypass Policy
- Who: Only engineering leads
- Condition: Soft score of 6.5-6.9 with a committed remediation plan
- Logging Requirement: Bypass must be documented with timestamp, actor, and remediation plan

## Audit Trail
- Log Evaluation: Each evaluation logs the timestamp, artifact ID, pass/fail status, and final score
- Retention Policy: Logs retained for a minimum of 1 year
---
