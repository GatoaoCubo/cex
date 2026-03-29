---
id: p11_qg_shaka_research
kind: quality_gate
pillar: P11
title: "Gate: Shaka Research Quality"
version: "1.0.0"
created: "2023-10-03"
updated: "2023-10-03"
author: "quality-gate-builder"
domain: "shaka_research"
quality: null
tags: [quality-gate, shaka-research, pre-publish]
tldr: "Ensures research artifacts meet defined quality standards before release"
density_score: 0.85
---
## Definition
| Property   | Value                       |
|------------|-----------------------------|
| Metric     | aggregate_score             |
| Threshold  | 0.8                         |
| Operator   | >=                          |
| Scope      | All research artifacts prior to release |

## Hard Gates
| gate_id | description                                             | threshold              | block |
|---------|---------------------------------------------------------|------------------------|-------|
| H01     | YAML frontmatter parses correctly                       | 100%                   | true  |
| H02     | ID matches the required pattern                         | 100%                   | true  |
| H03     | kind field is `quality_gate`                            | 100%                   | true  |
| H04     | title is descriptive and non-empty                      | 100%                   | true  |
| H05     | quality field set to null                               | 100%                   | true  |
| H06     | All mandatory fields are present in the artifact        | 100%                   | true  |

## Soft Gates
| gate_id | description                                 | max_penalty | weight |
|---------|---------------------------------------------|-------------|--------|
| S01     | Completeness of content                     | 10%         | 25%    |
| S02     | Accuracy of information provided            | 15%         | 30%    |
| S03     | Logical structure and coherence             | 5%          | 20%    |
| S04     | Relevance and applicability                 | 10%         | 15%    |
| S05     | Clarity and readability of language         | 5%          | 10%    |

## Scoring Formula
`final_score = (S01 * 0.25) + (S02 * 0.30) + (S03 * 0.20) + (S04 * 0.15) + (S05 * 0.10)`

## Bypass Policy
- **Who can override**: Admin or designated quality assurance officer
- **Condition**: Emergency release that critically depends on meeting business continuity requirements
- **Logging Requirement**: Each bypass must be logged with a detailed justification, timestamp, actor responsible, and the bypass expiry date clearly documented in the project repository audit log.

## Audit Trail
- **What is logged**: Each gate's evaluation result, including timestamp, pass/fail status, and responsible reviewer.
- **Retention policy**: Logs must be retained for a minimum of 24 months to ensure traceability and auditing capabilities.

---

This defined quality gate articulates a comprehensive framework for assessing research artifacts within the Shaka Research nucleus, ensuring alignment with established quality criteria before distribution.
