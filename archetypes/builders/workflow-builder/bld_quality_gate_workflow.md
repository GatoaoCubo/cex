---
id: p11_qg_workflow
kind: quality_gate
pillar: P12
title: "Gate: Workflow"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: workflow
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - workflow
  - orchestration
  - P12
tldr: "Validates multi-step orchestration flows for steps, dependency ordering, completion signals, and recovery."
llm_function: GOVERN
---
## Definition
A workflow defines a multi-step orchestration: ordered or parallel steps, the agent assigned to each, dependencies between steps, and completion signals. Workflows must be executable by automated runners without human interpretation. This gate ensures every workflow is acyclic, complete, and safe to run end-to-end.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p12_wf_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `workflow` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `steps`, `execution`, `signals` all defined and non-empty |
| H07 | Steps list has minimum depth | `steps` contains at least 2 entries |
| H08 | Dependency graph or ordering present | Each step either declares `depends_on` or body has an explicit sequential ordering |
| H09 | Completion signals defined | `signals` field names at least one completion signal per terminal step |
| H10 | steps_count matches body | The declared step count matches the number of steps actually present in the body |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | No prose restating what the steps table shows |
| Steps have agent assignment | 1.0 | Each step names the agent or component responsible |
| Dependency graph is acyclic | 1.0 | No step depends on a step that depends on it |
| Parallel vs sequential explicit | 0.5 | `execution` is set per step or globally |
| Error recovery per step | 1.0 | Each step has `on_failure` (retry, skip, abort, or escalate) |
| Tags include workflow | 0.5 | `tags` contains `"workflow"` |
| Wave ordering for parallel steps | 1.0 | Parallel steps declare a `wave` number |
| Timeout per step | 0.5 | Each step has `timeout_ms` or inherits a workflow-level timeout |
| Rollback strategy documented | 0.5 | Body describes how to undo completed steps on later failure |
| Signal references are valid | 1.0 | `signals` field references known signal kinds |
| No prompt chaining in body | 1.0 | Orchestration only; no LLM prompt text or task instructions |
Sum of weights: 9.0. `soft_score = sum(weight * gate_score) / 9.0 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference workflow |
| >= 8.0 | PUBLISH — safe for automated execution in production |
| >= 7.0 | REVIEW — runnable but recovery or signal references need work |
| < 7.0 | REJECT — do not run; steps are incomplete or dependencies are ambiguous |
## Bypass
| Field | Value |
|-------|-------|
| condition | Workflow is a one-time migration or incident response procedure that will not be re-run; formal gating would delay the response |
| approver | Lead engineer or on-call responsible for the affected system |
| audit_log | Entry required in `.claude/bypasses/workflow_{date}.md` with the incident or migration ticket ID |
| expiry | Single execution only; workflow must be archived or brought to PUBLISH score before any second run |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.
