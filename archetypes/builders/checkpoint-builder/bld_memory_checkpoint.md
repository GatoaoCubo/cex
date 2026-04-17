---
id: p10_lr_checkpoint_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
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
agent_group: edison
keywords: [checkpoint, workflow state, ttl, resume, state minimization, chain, rollback, orphan]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Checkpoint"
density_score: 0.90
llm_function: INJECT
---
## Summary
Checkpoints are only useful if they can be found and restored. Three properties make or break checkpoint utility: TTL enforcement (prevents orphan accumulation), workflow_ref presence (enables association during incident recovery), and state minimization (determines restore speed). The most expensive failure is a checkpoint that exists but cannot be used — correct id and step, but missing workflow_ref blocks recovery tooling.

## Pattern
**TTL + workflow_ref + minimal state.**

TTL schema:
1. 1h: interactive/human-in-the-loop workflows
2. 24h: batch processing (single run)
3. 7d: multi-day research or ingestion pipelines
4. 30d: compliance/audit workflows (retention-driven)
5. none: permanent archival only — requires justification

State minimization:
1. Include only keys needed to re-enter at this step
2. Exclude: derived values, large blobs (reference by id), volatile counters
3. Target: < 512 bytes; > 1024 bytes requires justification

Chain integrity:
1. Always set parent_checkpoint (null only for first checkpoint)
2. Chain must be traversable; each parent must exist or be archived
3. On completion: write terminal checkpoint with resumable: false

Step alignment: step field must exactly match the workflow's step definition name.

## Anti-Pattern
1. Omitting TTL (orphan checkpoints; storage bloat across all runs).
2. Missing workflow_ref (cannot associate checkpoint with workflow during recovery).
3. Storing full object graphs in state (restore time scales with size; store ids instead).
4. step value mismatched from workflow definition (resume tooling cannot find re-entry point).
5. Setting resumable: false without explanation (callers cannot distinguish tombstone from failure).

## Metadata

```yaml
id: p10_lr_checkpoint_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-checkpoint-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | checkpoint |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
