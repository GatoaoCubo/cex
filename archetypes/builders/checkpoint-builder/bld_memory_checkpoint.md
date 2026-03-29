---
id: p10_lr_checkpoint_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Checkpoints without TTL accumulated as orphan artifacts in 6 of 9 workflows reviewed, consuming 40-200MB of backend storage per workflow run. Checkpoints missing workflow_ref could not be associated with any workflow during incident recovery, making them useless for resume. Checkpoints with unbounded state (full object graphs) took 3-8x longer to restore than checkpoints with minimal resumption-critical state."
pattern: "Always declare TTL. Always set workflow_ref. Minimize state to resumption-critical keys only. Mirror step name in frontmatter exactly to the workflow's step definition."
evidence: "9 workflows audited: 6 had orphan checkpoints from missing TTL; 3 incidents where missing workflow_ref made recovery impossible; 4 workflows where state minimization reduced restore time from 8s to <1s."
confidence: 0.82
outcome: SUCCESS
domain: checkpoint
tags: [checkpoint, ttl, workflow-ref, state-minimization, resume, chain]
tldr: "TTL is mandatory. workflow_ref is load-bearing for recovery. Minimize state to resumption-critical keys. Step name must match workflow definition exactly."
impact_score: 8.0
decay_rate: 0.04
satellite: edison
keywords: [checkpoint, workflow state, ttl, resume, state minimization, chain, rollback, orphan]
---

## Summary
Checkpoints are only useful if they can be found and restored. Three properties make or break checkpoint utility in production: TTL enforcement (prevents orphan accumulation), workflow_ref presence (enables association during incident recovery), and state minimization (determines restore speed).
The most expensive failure mode is a checkpoint that exists but cannot be used: correct id, correct step, but missing workflow_ref means the recovery tooling cannot associate it with the workflow run. The second most expensive is a checkpoint with correct state but no TTL, which means storage debt grows indefinitely across all workflow runs.
## Pattern
**TTL + workflow_ref + minimal state.**
TTL schema (standard):
- 1h: interactive session workflows — short-lived, human-in-the-loop steps
- 24h: batch processing workflows — single run, checkpoint expires after run completes
- 7d: multi-day research or ingestion pipelines — spans multiple sessions
- 30d: compliance or audit workflows — retention requirement drives TTL
- none: permanent archival only — requires explicit justification in description field
State minimization rules:
- Include only keys needed to re-enter the workflow at this step
- Exclude: derived values (recomputable from other state), large blobs (reference by id instead), volatile values (timestamps, counters that reset on resume)
- Target: < 512 bytes state for most checkpoints; > 1024 bytes requires justification
Chain integrity rules:
- Always set parent_checkpoint (null only for the first checkpoint in a workflow)
- Chain must be traversable: each checkpoint's parent must exist or be explicitly archived
- On workflow completion: write a terminal checkpoint with resumable: false for audit trail
Step name alignment:
- step field must exactly match the step name as defined in the workflow artifact
- Mismatched step names cause resume tooling to fail to locate the re-entry point
## Anti-Pattern
- Omitting TTL entirely (orphan checkpoints; storage bloat across all workflow runs).
- Missing workflow_ref (checkpoint cannot be associated with a workflow during recovery).
- Storing full object graphs in state (restore time scales with state size; store ids and re-fetch instead).
- step value that does not match the workflow's step definition (resume tooling cannot find re-entry point).
- Setting resumable: false without explanation (callers cannot distinguish tombstone from transient failure).
- Skipping parent_checkpoint linkage (chain breaks; rollback to previous stable state impossible).
- Conflating checkpoint with signal: checkpoint has serialized state + workflow_ref; signal is a stateless event.
## Context
The 2048-byte body limit for checkpoint is generous enough to document a complete state schema and resume protocol. Use the budget intentionally: Overview (100 bytes), State table (400-600 bytes), Resume steps (500-700 bytes), Lifecycle (200-300 bytes). State table is the densest section — one row per key with type + size + description. Resume section is the most operationally critical — it must be executable by an agent with no additional context.
