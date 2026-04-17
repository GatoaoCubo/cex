---
id: n00_checkpoint_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Checkpoint -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, checkpoint, p12, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A checkpoint is a workflow state snapshot that captures the complete execution state at a defined point in a workflow, enabling resumption after failure, rollback to a known-good state, and auditing of incremental progress. It is the crash-safety mechanism that prevents workflow restarts from losing work already completed.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `checkpoint` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| workflow_id | string | yes | ID of the workflow being checkpointed |
| wave | integer | yes | Wave number at time of checkpoint |
| completed_tasks | array | yes | Task IDs completed before this checkpoint |
| pending_tasks | array | yes | Task IDs remaining after this checkpoint |
| state_snapshot | object | yes | Serialized workflow state variables |
| created_at | datetime | yes | When this checkpoint was created |
| resumable | boolean | yes | Whether execution can resume from this checkpoint |

## When to use
- When a long-running multi-wave mission needs crash recovery capability
- When creating rollback points before risky workflow transitions
- When auditing incremental progress in overnight or autonomous runs

## Builder
`archetypes/builders/checkpoint-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind checkpoint --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: chk_fractal_fill_wave2_end
kind: checkpoint
pillar: P12
nucleus: n07
title: "Example Checkpoint"
version: 1.0
quality: null
---
# Checkpoint: FRACTAL_FILL Wave 2 Complete
workflow_id: wf_fractal_fill
wave: 2
completed_tasks: [n01_kc_build, n02_prompt_build, n03_agent_build]
resumable: true
created_at: "2026-04-17T14:00:00Z"
```

## Related kinds
- `workflow` (P12) -- workflow that this checkpoint belongs to
- `session_state` (P10) -- session-level state that checkpoints may snapshot
- `workflow_run_crate` (P10) -- provenance archive that references checkpoint history
