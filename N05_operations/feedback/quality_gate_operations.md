---
id: p11_qg_operations_nucleus
kind: quality_gate
pillar: P11
title: "Gate: Operations Nucleus"
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n05_operations
domain: operations-engineering
quality: null
tags: [quality_gate, N05, operations, testing, deployment]
tldr: Validation gate for N05 outputs covering evidence quality, runtime relevance, rollback discipline, and release-safe actionability.
density_score: 0.97
---

## Definition

| Property | Value |
|----------|-------|
| Metric | operational_readiness_score |
| Threshold | 0.88 |
| Operator | >= |
| Scope | All N05 artifacts, reviews, test/debug outputs, deploy validations, and CI/CD remediation reports |

## Hard Gates

| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| H01 | YAML frontmatter parses without error | 100% | true |
| H02 | `kind` matches the artifact file type | 100% | true |
| H03 | `quality` is `null` in source artifact frontmatter | 100% | true |
| H04 | Output is domain-specific to operations/devops, not generic filler | 100% | true |
| H05 | Findings or fixes are tied to concrete evidence, or the evidence gap is explicitly stated | 100% | true |
| H06 | Validation commands or review basis are reproducible in repo context | 100% | true |
| H07 | Release-affecting output includes rollback or explains why rollback is not relevant | 100% | true |
| H08 | Deploy, CI, or infra guidance does not ignore environment/config assumptions | 100% | true |
| H09 | Output does not claim completion while known failing signals remain unaddressed | 100% | true |

## Soft Gates

| gate_id | description | max_penalty | weight |
|---------|-------------|-------------|--------|
| S01 | Accuracy of diagnosis or review findings | 0.10 | 0.24 |
| S02 | Validation depth on affected path | 0.10 | 0.24 |
| S03 | CI/CD and deploy safety awareness | 0.10 | 0.18 |
| S04 | Remediation precision and blast-radius control | 0.10 | 0.14 |
| S05 | Rollback and observability quality | 0.10 | 0.10 |
| S06 | Clarity and handoff utility | 0.10 | 0.10 |

## Scoring Formula

`operational_readiness_score = (S01 * 0.24) + (S02 * 0.24) + (S03 * 0.18) + (S04 * 0.14) + (S05 * 0.10) + (S06 * 0.10)`

Pass condition:

- all hard gates pass
- `operational_readiness_score >= 0.88`

## Bypass Policy

- **Allowed by**: orchestrator or repository owner
- **Valid only for**: time-critical incident response or degraded validation infrastructure
- **Required record**: missing evidence, blast radius, rollback path, timestamp, approver

## Audit Trail

Record:

- artifact id and version
- evaluator
- commands, diffs, tests, or logs used as evidence
- pass/fail by hard gate
- soft-gate subscores
- final score
- bypass data if used

Retention: 24 months minimum or active repo lifetime, whichever is longer.
