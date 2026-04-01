---
id: p11_qg_orchestration_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Orchestration Artifacts"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "quality-gate-builder"
domain: "orchestration"
quality: 8.9
tags: [quality-gate, orchestration, n07, coordination, dispatch]
tldr: "Quality gate for orchestration artifacts: validates nucleus routing, handoff structure, and signal protocols >= 8.0"
density_score: 0.88
---
## Definition
| Property | Value |
|----------|-------|
| Metric | orchestration_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All orchestration artifacts (workflows, handoffs, dispatch_rules, coordination patterns) |

## HARD Gates
Failure on any gate blocks artifact regardless of soft score.

| ID  | Criterion | Failure Action |
|-----|-----------|----------------|
| H01 | Frontmatter parses as valid YAML without errors | block |
| H02 | `id` matches pillar namespace pattern | block |
| H03 | `id` equals filename stem exactly | block |
| H04 | `kind` field matches expected orchestration artifact type | block |
| H05 | `quality` field is null (no self-scoring) | block |
| H06 | All required frontmatter fields present and non-empty | block |
| H07 | Nucleus routing table present with valid N01-N07 mappings | block |
| H08 | Handoff protocol defined with clear input/output specifications | block |
| H09 | Signal emission points documented for coordination events | block |
| H10 | Dispatch logic is deterministic (no ambiguous routing rules) | block |

## SOFT Gates
Weighted dimensions contributing to quality score.

| ID  | Criterion | Weight | Scoring Method |
|-----|-----------|--------|----------------|
| S01 | Nucleus assignment accuracy (correct domain-to-nucleus mapping) | 20% | graduated |
| S02 | Handoff completeness (all required data flows specified) | 20% | binary |
| S03 | Signal protocol adherence (proper event emission and handling) | 15% | graduated |
| S04 | Coordination efficiency (minimal nucleus hops for task completion) | 15% | graduated |
| S05 | Error handling coverage (failure modes and recovery paths defined) | 10% | binary |
| S06 | Documentation clarity (orchestration flow is comprehensible) | 10% | graduated |
| S07 | Dependency management (prerequisites and order dependencies explicit) | 10% | binary |

## Scoring Formula
```
aggregate_score = (
  S01_score * 0.20 +
  S02_score * 0.20 + 
  S03_score * 0.15 +
  S04_score * 0.15 +
  S05_score * 0.10 +
  S06_score * 0.10 +
  S07_score * 0.10
) * 10
```

**Pass condition**: All HARD gates pass AND aggregate_score >= 8.0

## Actions
| Outcome | Consequence |
|---------|-------------|
| GOLDEN (>= 9.5) | Promote to reference orchestration pattern; use as template for new patterns |
| PUBLISH (>= 8.0) | Deploy to production orchestration pool; mark as coordination-ready |
| REVIEW (>= 7.0) | Return to author with dimensional feedback; single revision cycle allowed |
| REJECT (< 7.0) | Block from pool; requires fundamental restructure before re-evaluation |

## Bypass Policy
| Field | Value |
|-------|-------|
| Conditions | Experimental orchestration pattern with unstable nucleus architecture OR emergency coordination fix |
| Approver | N07 chief orchestrator must authorize in writing |
| Audit requirement | Log in `.cex/runtime/decisions/bypasses.md` with date, approver, justification, and expiry |
| Expiry | 7 days for emergency fixes, 21 days for experimental patterns |
| Non-bypassable | H01 (YAML validity), H05 (quality null), H07 (nucleus routing) |