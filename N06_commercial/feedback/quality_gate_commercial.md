---
id: p11_qg_commercial_nucleus
kind: quality_gate
pillar: P11
title: "Gate: Commercial Nucleus"
version: "1.0.0"
created: "2023-10-10"
updated: "2023-10-10"
author: "system"
domain: "commercial_nucleus"
quality: null
tags: [quality-gate, commercial, governance]
tldr: "Pre-deployment gate for commercial nucleus artifacts: ensures compliance, usability, and performance."
density_score: 0.85
---
## Definition
| Property | Value |
|----------|-------|
| Metric | aggregate_quality_score |
| Threshold | 0.80 |
| Operator | >= |
| Scope | All commercial nucleus artifacts before deployment |
## HARD Gates
| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| H01 | YAML parses without error | N/A | true |
| H02 | id matches pattern /^p11_qg_[a-z][a-z0-9_]+$/ | N/A | true |
| H03 | id equals filename stem | N/A | true |
| H04 | kind is exactly 'quality_gate' | N/A | true |
| H05 | quality field is null | N/A | true |
| H06 | All required fields are present in frontmatter | N/A | true |
| H07 | Compliance with commercial regulations | 100% | true |
| H08 | Artifact size <= 4096 bytes | N/A | true |
## SOFT Gates
| gate_id | description | max_penalty | weight |
|---------|-------------|-------------|--------|
| S01 | Usability score | 10% | 30% |
| S02 | Performance efficiency | 10% | 30% |
| S03 | Documentation completeness | 10% | 20% |
| S04 | Alignment with strategic objectives | 10% | 20% |
## Scoring Formula
final_quality_score = (S01_score * 0.30) + (S02_score * 0.30) + (S03_score * 0.20) + (S04_score * 0.20)
PASS if all HARD gates pass AND final_quality_score >= 0.80
## Bypass Policy
- Who: Admin
- Conditions: Only if hard constraints temporarily unverifiable
- Logging: Bypass must be logged with timestamp, actor, and justification
## Audit Trail
- What is logged: Gate evaluation results, timestamps, any bypass occurrences
- Retention policy: Logs retained for 24 months
---
