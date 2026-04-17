---
id: mem_learning_record_n05
kind: learning_record
pillar: P10
nucleus: N05
title: "N05 Operations Learning Record"
version: "1.0.0"
quality: 9.0
tags: [n05, operations, learning_record, gating_wrath, retrieval, release_gate, evidence]
density_score: 0.97
---
<!-- 8F: F1=learning_record/P10 F2=learning-record-builder F3=nucleus_def_n05+P10_schema+kc_learning_record+examples+retrieval stack docs F4=codify what worked and failed for ops retrieval
     F5=shell+apply_patch+cex_compile F6=approx-6KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/P10_memory/mem_learning_record_n05.md -->

# N05 Operations Learning Record

## Intent

This learning record captures what N05 should remember about retrieving and using operational evidence for code review, CI triage, deploy gating, and rollback decisions.

The record is persistent because these lessons should shape future behavior.

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | `P10` |
| Nucleus | `N05` |
| Topic | `ops_retrieval_and_gate_quality` |
| Outcome | `success_with_constraints` |
| Score | `9.0` |
| Reproducibility | `high` |
| Decay | `60 days review` |

## Event

The pattern encoded here is the result of aligning chunking, embedding, hybrid retrieval, and memory compression around N05's gatekeeper role.

Observed successful posture:

- evidence-first retrieval
- strict environment and service filters
- low-signal block instead of guesswork
- compact top_k
- explicit degraded mode when dense search is unavailable

## What Worked

| Pattern | Why it worked |
|---------|---------------|
| hybrid search with strong filters | combined exact identifiers with semantic incident matching |
| event-bounded chunking for logs | preserved traceback and deploy phase integrity |
| compact top_k of 6 | reduced summary drift and verdict hedging |
| explicit insufficiency response | prevented false confidence during gate decisions |
| vector model pinning | kept index behavior stable across rebuilds |

## What Failed

| Anti-pattern | Failure |
|--------------|---------|
| dense-only retrieval | exact test ids and env keys were missed |
| generic long chunks | reranker returned broad prose instead of the failing evidence |
| silent fallback to another embedder | index semantics drifted without visibility |
| memory summaries outranking raw evidence | verdicts became overgeneralized |
| weak freshness control | old deploy incidents contaminated current triage |

## Primary Lesson

For N05, retrieval quality is not mainly a ranking problem.

It is a governance problem.

When the retrieval stack preserves exact evidence boundaries and refuses to bluff under weak signal, gate decisions become sharper and safer. When the stack optimizes for broad contextual richness, false approvals become more likely.

## Actionable Pattern

Recommended behavior for future sessions:

1. retrieve direct evidence first
2. retrieve learning and memory second
3. refuse approval when evidence is sparse or stale
4. treat model or namespace drift as a rebuild event
5. keep summaries compact and subordinate to logs, tests, and checklists

## Evidence Snapshots

Representative evidence classes that benefited from this pattern:

- failing pytest ids
- readiness probe errors
- startup timeout traces
- deploy rollback conditions
- config contract mismatches

These are exactly the classes that cause expensive mistakes when over-summarized.

## Gating Wrath Bias

This learning should bias N05 toward:

- blocking unsafe releases sooner
- asking for the exact service/environment when missing
- preferring precise chunks over inspirational handbook text
- exposing degraded search mode in responses

It should bias N05 away from:

- optimistic approval based on partial evidence
- silent semantic drift
- mixed-source verdicts with no clear evidence chain

## Transferability

| Context | Applies? | Notes |
|---------|----------|-------|
| release gate review | yes | strongest fit |
| incident triage | yes | use direct evidence first |
| architecture ideation | partial | retrieval still useful, gate posture less central |
| generic research | no | broader retrieval may be acceptable elsewhere |

## Update Conditions

Update this record if:

- recall benchmarks show top_k should change
- fallback strategy changes materially
- a new failure pattern appears in deploy or test triage
- the dense provider or vector backend changes

Do not update it for:

- one-off incidents with no repeated pattern
- temporary experiments that never reached the default path

## Validation Checklist

- learning is specific, not motivational
- includes both pattern and anti-pattern
- has an operational score
- can be acted on in future sessions
- clearly distinguishes evidence order

## Decision Summary

The main remembered lesson is simple:

N05 performs best when retrieval is governed like a release gate.

That means explicit contracts, visible degradation, compact evidence packets, and a willingness to block when the signal is weak.
