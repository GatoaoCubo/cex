---
id: p11_qg_checkpoint
kind: quality_gate
pillar: P11
title: "Gate: checkpoint"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "workflow checkpoint — saved state snapshot enabling resumable, auditable workflow execution"
quality: 9.0
tags: [quality-gate, checkpoint, P12, workflow, resume, state]
tldr: "Pass/fail gate for checkpoint artifacts: workflow_ref presence, state schema, TTL declaration, resume protocol, and lifecycle policy."
density_score: 0.90
llm_function: GOVERN
---
# Gate: checkpoint
## Definition
| Field | Value |
|---|---|
| metric | checkpoint artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: checkpoint` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p12_ck_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p12_ck_foo` but file is `p12_ckpt_bar.md` |
| H04 | Kind equals literal `checkpoint` | `kind: state` or `kind: snapshot` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `workflow_ref`, `step`, `tldr`, or `tags` |
| H07 | workflow_ref is non-empty string | `workflow_ref: ""` or field absent |
| H08 | step is non-empty string | `step: ""` or field absent |
| H09 | tags includes "checkpoint" | Tags list present but does not contain "checkpoint" |
| H10 | Body has all 4 required sections | Missing Overview, State, Resume, or Lifecycle section |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| State schema completeness | 1.0 | All state keys listed with type and size hint; no undocumented keys |
| Resume protocol clarity | 1.0 | Step-by-step resume instructions; prerequisites stated; re-entry point named |
| TTL declaration | 1.0 | ttl field present with valid value; justification if ttl: none |
| Lifecycle policy | 0.5 | Cleanup and archival policy declared; chain linkage documented |
| Idempotency declaration | 1.0 | Resume explicitly states whether re-running is safe and why |
| Boundary clarity | 1.0 | Explicitly not a signal, session_state, or workflow artifact |
| Retry modeling | 0.5 | retry_count field used; error field covers failure state |
| Chain linkage | 0.5 | parent_checkpoint referenced or null with explanation |
| Workflow alignment | 1.0 | step value matches a named step in the referenced workflow |
| Domain specificity | 1.0 | State keys, step name, and TTL specific to declared workflow domain |
| Serialization safety | 1.0 | State uses only safe serialization (yaml/json); no binary blobs in spec |
| Testability | 0.5 | Resume steps verifiable with known state; expected outcome documented |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Bootstrap checkpoint created during initial workflow scaffolding, not yet connected to a live workflow_ref |
| approver | Author self-certification with comment explaining bootstrap scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — bootstrap checkpoints must be promoted to >= 7.0 or removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |
