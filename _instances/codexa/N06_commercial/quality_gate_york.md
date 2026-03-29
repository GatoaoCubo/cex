---
id: p11_qg_york_commercial_nucleus
kind: quality_gate
pillar: P11
title: "Gate: York Commercial Nucleus"
version: "1.0.0"
created: "2023-10-20"
updated: "2023-10-20"
author: "system"
domain: "commercial_nucleus"
quality: null
tags: [quality-gate, york, commercial_nucleus]
tldr: "Numeric quality gate for York Commercial Nucleus focusing on mandatory and quality enhancement criteria."
density_score: 0.85
---

## Definition
| Property   | Value                    |
|------------|--------------------------|
| Metric     | aggregate_score          |
| Threshold  | 0.80                     |
| Operator   | >=                       |
| Scope      | All commercial nucleus components before activation |

## Hard Gates
| gate_id | description                            | threshold | block |
|---------|----------------------------------------|-----------|-------|
| H01     | Frontmatter YAML parses without error  | Pass/Fail | true  |
| H02     | `id` matches pattern /^p11_qg_[a-z][a-z0-9_]+$/ | Pass/Fail | true  |
| H03     | `kind` is "quality_gate"               | Pass/Fail | true  |
| H04     | Required fields present                | Pass/Fail | true  |

## Soft Gates
| gate_id | description                    | max_penalty | weight |
|---------|--------------------------------|-------------|--------|
| S01     | Completeness of features       | 0.2         | 30%    |
| S02     | Documentation clarity          | 0.1         | 25%    |
| S03     | Compliance with commercial standards | 0.1 | 20%    |
| S04     | Usability in commercial applications | 0.2 | 25%    |

## Scoring Formula
The final score is calculated as follows:
`final_score = hard_pass ? sum(soft_gate_score * weight) / sum(weights) : 0`, where `hard_pass` indicates all HARD gates are passed.

## Bypass Policy
- Who may override: Admin
- Conditions for bypass: In exceptional commercial project circumstances where temporary deployment is critical.
- Audit requirement: Any bypass must be logged with a timestamp, actor details, and justification for the decision.

## Audit Trail
Every evaluation must log:
- Artifact ID
- Evaluation timestamp
- HARD gate results
- SOFT gate scores
- Final score
- Any bypass occurrences
Audit logs must be retained for a minimum of 12 months for review and quality assurance purposes.
---
