---
id: p11_qg_orchestration_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Orchestration Artifacts"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "quality-gate-builder"
domain: "orchestration"
quality: 9.1
tags: [quality-gate, orchestration, nucleus-routing, handoff, signal, dispatch, workflow]
tldr: "Pre-pool gate for orchestration artifacts: 8 HARD checks + 8-dimension scoring >= 8.0"
density_score: 0.91
---
## Definition

| Property | Value |
|----------|-------|
| Metric | orchestration_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All orchestration artifacts (workflows, handoffs, dispatch_rules, signals, coordination patterns) before pool merge |

## HARD Gates

Failure on any single gate sets final score to 0 and blocks pool merge immediately.

| ID | Criterion | Failure Action |
|----|-----------|----------------|
| H01 | Frontmatter block parses as valid YAML without errors | block |
| H02 | `id` matches the required namespace pattern for the artifact kind | block |
| H03 | `id` value equals the filename stem exactly (case-sensitive) | block |
| H04 | `kind` field matches a registered orchestration artifact type in `kinds_meta.json` | block |
| H05 | `quality` field is null at authoring time (no self-scoring) | block |
| H06 | All required frontmatter fields present and non-empty (id, kind, pillar, title, version, created, updated, author, domain, tags, tldr) | block |
| H07 | Nucleus routing reference present: artifact identifies which nucleus executes or is targeted | block |
| H08 | No build operations performed directly — all artifact construction delegated to appropriate nucleus via `dispatch.sh` | block |

## SOFT Scoring

Score each dimension 0 (absent or fails) to 1 (present and passes). Weights sum to 100%.

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Routing completeness | 20% | Nucleus routing table or routing reference covers all artifact kinds handled by the artifact |
| Handoff structure | 20% | Handoff includes mission, nucleus, task, and decisions fields; references `decision_manifest.yaml` |
| Signal protocol | 15% | `complete`, `retry`, and `cancel` signals defined and mapped to concrete outcomes |
| GDP compliance | 15% | Subjective decisions documented in manifest before dispatch, or manifest reference explicitly present |
| Dispatch validity | 10% | Dispatch uses `bash _spawn/dispatch.sh` exclusively — no raw `start cmd`, no inline powershell |
| Consolidation protocol | 10% | Post-dispatch steps defined: detect → verify → stop → commit (Gemini) → signal |
| Anti-pattern absence | 5% | No task passed as CLI arg to boot scripts; no nested-quote dispatch patterns present |
| Density | 5% | `density_score` field present and >= 0.80 |

**Scoring formula**: `final_score = SUM(score_i × weight_i) × 10` where weights are decimal fractions (20% = 0.20)

**PASS condition**: All HARD gates pass AND `final_score >= 8.0`

## Actions

| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as reference; use as template for new orchestration artifact authors |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle permitted |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |

## Bypass

| Field | Value |
|-------|-------|
| condition | Experimental nucleus in active design with unstable schema not yet registered in `kinds_meta.json` |
| approver | N07 Orchestrator (pillar owner) must approve in writing before bypass takes effect |
| audit_log | Record in `.cex/runtime/decisions/bypass_log.md` with date, approver, artifact id, and justification |
| expiry | 14 days from bypass grant; artifact must reach full gate compliance before expiry or is rejected |

**H01 (YAML parse) and H05 (quality null) are never bypassable under any condition.**