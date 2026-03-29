---
id: p11_qg_pytha_knucleus
kind: quality_gate
pillar: P11
title: "Quality Gate for Pytha Knowledge Nucleus"
version: "1.0.0"
created: "2023-10-05"
updated: "2023-10-05"
author: "quality-gate-builder"
domain: "knowledge_management"
quality: null
tags: [quality-gate, pytha, knowledge-nucleus]
tldr: "Defines mandatory adherence to quality criteria for Pytha Knowledge Nucleus before publishing."
density_score: 0.95
---

## Definition
| Property | Value |
|----------|-------|
| Metric | aggregate_score |
| Threshold | 0.8 |
| Operator | >= |
| Scope | All artifacts submitted to Pytha Knowledge Nucleus |

## HARD Gates
| Gate ID | Description | Threshold | Block |
|---------|-------------|-----------|-------|
| H01 | YAML frontmatter valid and parses correctly | True | true |
| H02 | ID matches pattern `^p11_qg_[a-z][a-z0-9_]+$` | True | true |
| H03 | Title field is non-empty | True | true |
| H04 | Domain field is valid and recognized | True | true |
| H05 | quality field is null | True | true |
| H06 | Tags contain at least 'knowledge-nucleus' | True | true |

## SOFT Gates
| Gate ID | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| S01 | Completeness: All essential sections present | 10 | 40% |
| S02 | Accuracy: Information correct and verifiable | 10 | 30% |
| S03 | Relevance: Content is within scope of the nucleus | 10 | 30% |

## Scoring Formula
The final score is computed with the formula:
\[ \text{aggregate_score} = \frac{\sum (\text{SOFT gate score} \times \text{weight})}{\sum \text{weights}} \]
An artifact must have all HARD gates pass and an aggregate_score of at least 0.8.

## Bypass Policy
- Approver: Only a domain admin can override a failed gate.
- Conditions: Allowable if the failure is isolated to a non-essential criterion and comprehensive justification is provided.
- Audit Requirement: Log must include timestamp, actor, reason for bypass, and expected follow-up actions.

## Audit Trail
For each gate evaluation:
- Log entry must include the artifact ID, evaluation timestamp, HARD/ SOFT gate results, final score, and evaluator's identity.
- Retention Policy: Logs are retained for a minimum of 12 months or until the artifact is deprecated, whichever is longer.
---
