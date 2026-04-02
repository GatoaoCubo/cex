---
id: p11_qg_engineering_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Engineering Artifacts"
version: "1.1.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "quality-gate-builder"
domain: "engineering"
quality: 9.0
tags: [quality-gate, engineering, technical, architecture, code, p11]
tldr: "Quality gate for engineering artifacts: 10 HARD gates + 5-dimension scoring >= 8.5 before pool acceptance"
density_score: 0.91
---
## Definition

| Property | Value |
|----------|-------|
| Metric | engineering_quality_score |
| Threshold | 8.5 |
| Operator | >= |
| Scope | All engineering artifacts (code, system designs, technical specs, architecture docs, API definitions) before pool merge |

## HARD Gates

Failure on any single gate sets final score to 0 and blocks pool merge immediately.

| ID  | Criterion | Failure Action |
|-----|-----------|----------------|
| H01 | Frontmatter block parses as valid YAML without errors | block |
| H02 | `id` matches required namespace pattern for the artifact kind | block |
| H03 | `id` value equals filename stem exactly (case-sensitive) | block |
| H04 | `kind` field matches literal artifact type registered in `kinds_meta.json` | block |
| H05 | `quality` field is null at authoring time (self-scoring forbidden) | block |
| H06 | All required frontmatter fields present and non-empty | block |
| H07 | Artifact includes at least one concrete, runnable implementation example or code snippet | block |
| H08 | No security anti-patterns present (hardcoded credentials, injection vectors, plaintext secrets) | block |
| H09 | Testability criteria or acceptance conditions are explicitly stated | block |
| H10 | Body size does not exceed kind-specific max_bytes limit | block |

## SOFT Scoring

Score each dimension 0–1 (graduated or binary per scoring method). Weights sum to 100%.

| ID  | Dimension | Weight | Scoring Method | Criteria |
|-----|-----------|--------|----------------|----------|
| S01 | Technical Depth | 25% | graduated | Covers edge cases, failure modes, and performance characteristics |
| S02 | Completeness | 25% | graduated | All required sections present; no placeholder content (`TODO`, `TBD`, `...`) |
| S03 | Maintainability | 20% | graduated | Modular structure; dependencies explicit; upgrade path documented |
| S04 | Security Posture | 15% | binary | Threat model addressed or explicitly out-of-scope with justification |
| S05 | Documentation Quality | 15% | graduated | Examples are executable; terminology consistent with CEX glossary |

## Scoring Formula

```
hard_pass = ALL(H01..H10 pass)
soft_score = S01*0.25 + S02*0.25 + S03*0.20 + S04*0.15 + S05*0.15
engineering_quality_score = hard_pass ? (soft_score * 10) : 0
PASS = hard_pass AND engineering_quality_score >= 8.5
```

Weights verified: 0.25 + 0.25 + 0.20 + 0.15 + 0.15 = 1.00

## Actions

| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as reference; flag for engineering nucleus onboarding |
| PUBLISH | >= 8.5 | Merge to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with per-dimension failure report; one revision cycle |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |

## Bypass

| Field | Value |
|-------|-------|
| condition | Prototype artifact in active design iteration (schema not yet stable); SOFT-only failure with score 8.0–8.4 |
| approver | Pillar owner (N05 or N03 lead) must approve in writing before bypass activates |
| audit_log | Record in `records/pool/audits/bypasses.md`: date, approver, gate IDs bypassed, rationale |
| expiry | 14 days from grant; artifact must reach full compliance before expiry or is auto-rejected |

**Non-bypassable gates**: H01 (frontmatter parse) and H05 (quality null) cannot be bypassed under any condition.