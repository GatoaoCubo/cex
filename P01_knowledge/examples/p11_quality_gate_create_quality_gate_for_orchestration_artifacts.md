---
id: p11_qg_orchestration
kind: quality_gate
pillar: P11
title: "Gate: Orchestration Artifacts"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "quality-gate-builder"
domain: "orchestration"
quality: 8.9
target_kind: ["workflow", "dag", "schedule", "dispatch_rule", "handoff"]
delivery_threshold: 8.0
bypass_policy: "admin"
dimensions: ["completeness", "efficiency", "resilience", "traceability", "resource_awareness", "documentation"]
tags: [quality-gate, orchestration, workflow, dispatch, P11]
tldr: "Quality gate for orchestration artifacts: validates workflow logic, nucleus references, and execution safety with 8.0+ threshold."
density_score: 0.91
---
## Definition

Quality gate for orchestration artifacts that coordinate multiple nuclei, manage workflows, or control task dispatch. Ensures logical consistency, executable structure, and safe resource utilization.

| Property | Value |
|----------|-------|
| Metric | weighted_orchestration_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All orchestration artifacts (workflow, dag, schedule, dispatch_rule, handoff) before production deployment |

## HARD Gates

ALL must pass. Single failure = REJECT regardless of soft score.

| ID  | Criterion | Failure Action |
|-----|-----------|----------------|
| H01 | YAML frontmatter parses without syntax errors | block |
| H02 | `id` field matches pattern `p{NN}_*` for target pillar | block |
| H03 | `id` field equals filename stem exactly | block |
| H04 | `kind` field matches one of target orchestration kinds | block |
| H05 | `quality` field is null at creation time | block |
| H06 | All required frontmatter fields present and non-empty | block |
| H07 | All referenced nucleus IDs (n01-n07) exist in system registry | block |
| H08 | Workflow contains no circular dependencies or infinite loops | block |
| H09 | Every workflow step defines concrete action with clear success criteria | block |
| H10 | Error handling paths defined for all failure scenarios | block |

## SOFT Gates

Weighted scoring dimensions contributing to final quality score.

| ID  | Criterion | Weight | Scoring Method |
|-----|-----------|--------|----------------|
| S01 | Completeness: all workflow steps documented with inputs/outputs | 0.20 | graduated |
| S02 | Efficiency: minimal redundant steps, optimal nucleus utilization | 0.20 | graduated |
| S03 | Resilience: graceful degradation and retry logic for failures | 0.20 | graduated |
| S04 | Traceability: clear step naming and execution logging | 0.15 | binary |
| S05 | Resource awareness: respects nucleus capabilities and load limits | 0.15 | graduated |
| S06 | Documentation: clear purpose, usage examples, and dependencies | 0.10 | binary |

## Scoring Formula

```
aggregate_score = SUM(gate_score * weight for each SOFT gate)
final_score = aggregate_score * 10
PASS condition: all HARD gates pass AND final_score >= 8.0
```

Weight verification: 0.20 + 0.20 + 0.20 + 0.15 + 0.15 + 0.10 = 1.00 ✓

## Actions

| Outcome | Score Range | Consequence |
|---------|-------------|-------------|
| GOLDEN | >= 9.5 | Deploy to production; use as reference template |
| PUBLISH | 8.0 - 9.4 | Deploy to production with standard monitoring |
| REVIEW | 7.0 - 7.9 | Return for revision with detailed feedback |
| REJECT | < 7.0 | Block deployment; major rework required |

## Bypass Policy

| Field | Value |
|-------|-------|
| Conditions | Experimental orchestration patterns under active research; emergency hotfix deployments with time constraints |
| Approver | P11 pillar owner or N07 orchestrator lead |
| Audit requirement | Record in `.cex/runtime/decisions/bypasses.md` with timestamp, approver signature, business justification, and review date |
| Expiry | 7 days from bypass grant; must achieve full compliance before production use |
| Non-bypassable | H01 (YAML parsing), H05 (quality null), H07 (nucleus references), H08 (circular dependencies) |