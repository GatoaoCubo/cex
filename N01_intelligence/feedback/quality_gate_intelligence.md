---
id: p11_qg_research_nucleus
kind: quality_gate
pillar: P11
title: "Gate: Research Nucleus"
version: "1.0.0"
created: "2023-10-05"
updated: "2023-10-05"
author: "quality-gate-builder"
domain: "research"
quality: 8.7
tags: [quality-gate, research, evaluation]
tldr: "Gate for ensuring high-quality research outputs before acceptance into the pool."
density_score: 0.95
---

## Definition
| Property | Value |
|----------|-------|
| Metric | aggregate_score |
| Threshold | 0.8 |
| Operator | >= |
| Scope | All research artifacts before pool integration |

## HARD Gates
| gate_id | Description | Threshold | Block |
|---------|-------------|-----------|-------|
| H01 | Frontmatter parses without error | N/A | true |
| H02 | id matches the filename stem | N/A | true |
| H03 | kind == research | N/A | true |
| H04 | quality field must be null | N/A | true |
| H05 | Required fields present | 100% | true |
| H06 | Research must not exceed size limit (4096 bytes) | 4096 bytes | true |

## SOFT Gates
| gate_id | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| S01 | Completeness of references | 0.2 | 20% |
| S02 | Originality and innovation | 0.3 | 30% |
| S03 | Clarity and coherence of argument | 0.2 | 20% |
| S04 | Actionable insights and conclusions | 0.2 | 20% |
| S05 | Compliance with ethical standards | 0.1 | 10% |

## Scoring Formula
`aggregate_score = SUM(gate_score * weight for each SOFT gate)`

PASS condition: all HARD gates pass AND aggregate_score >= 0.8

## Bypass Policy
- Who may override: admin
- Conditions for bypass: For scores between 0.75 and 0.79 with additional peer review
- Audit requirement: Must log timestamp, actor, justification, and expiry of bypass

## Audit Trail
- What is logged: Evaluation results of each gate, timestamp, evaluator ID
- Retention Policy: Logs must be retained for a minimum of 6 months for auditing and review purposes
---
