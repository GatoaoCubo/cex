---
id: p11_qg_edison_eng
kind: quality_gate
pillar: P11
title: "Edison Engineering Quality Gate"
version: "1.0.0"
created: "2023-10-04"
updated: "2023-10-04"
author: "quality-gate-builder"
domain: "engineering"
quality: null
tags: [quality-gate, engineering, review]
tldr: "Quality gate ensures engineering work meets standards before proceeding."
density_score: 0.85
---
## Definition
| Property | Value |
|----------|-------|
| Metric | combined_score |
| Threshold | 0.8 |
| Operator | >= |
| Scope | All engineering artifacts before pool merge |

## HARD Gates
| Gate ID | Description | Threshold | Block |
|---------|-------------|-----------|-------|
| H01 | Frontmatter parses correctly | N/A | true |
| H02 | ID matches `p11_qg_` pattern | N/A | true |
| H03 | ID equals filename stem | N/A | true |
| H04 | Kind is literal `quality_gate` | N/A | true |
| H05 | Quality is set to null | N/A | true |
| H06 | Required fields are present | N/A | true |

## SOFT Gates
| Gate ID | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| S01 | Technical completeness | -0.3 | 30% |
| S02 | Correctness of content | -0.4 | 40% |
| S03 | Safety adherence | -0.2 | 20% |
| S04 | Usability standards | -0.1 | 10% |

## Scoring Formula
The final score is calculated as follows:
`aggregate_score = SUM(gate_score * weight for each SOFT gate) if all HARD gates pass`

## Bypass Policy
Who: Admin  
Condition: In case of urgent release with non-critical SOFT gate failure  
Audit Requirement: Override must be logged with a timestamp, actor, and justification.  
Note: HARD gates cannot be bypassed.

## Audit Trail
Every evaluation is logged with:
- Timestamp
- Actor performing the evaluation
- Outcome of each gate
Retention Policy: Logs are retained for a minimum of 1 year or until the next full audit cycle.

This artifact ensures a rigorous quality governance process, focusing on transparency and traceability through meticulous evaluation and logging practices.
