---
id: p10_ax_session_compression
kind: axiom
pillar: P10
title: "Axiom: Session Compression (Dual-ID Pattern)"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
quality: 9.0
tags: [axiom, compression, session, dual-id, stop]
tldr: "Compression fires exactly once at Stop hook. Dual-ID pattern: content_session_id (stable, for DB) vs memory_session_id (lazy, for SDK resume)."
max_bytes: 3072
density_score: 0.91
source: organization-core/records/core/memory/hooks/ (Stop hook compression)
linked_artifacts:
  template: tpl_axiom_session_compression
  related: p10_ax_lifecycle_hooks
related:
  - p01_kc_memory_session_compression
  - p10_ax_lifecycle_hooks
  - p10_ss_[session_slug]
  - p01_kc_memory_summary
  - p10_memory_summary
  - p01_kc_memory_lifecycle_hooks
  - bld_collaboration_memory_summary
  - p01_kc_session_state
  - memory-summary-builder
  - bld_memory_session_state
---

# Axiom: Session Compression (Dual-ID Pattern)

## Statement

> Compression fires exactly once per session at the Stop hook. It produces a summary from accumulated observations. Original observations are retained for citation; the summary is the primary retrieval artifact.

## Rule

```
Stop hook fires
  → Check compression_status for content_session_id
  → If "pending":
      → Fetch all observations for content_session_id
      → Generate summary via LLM (single call)
      → Store summary linked to content_session_id
      → Set compression_status = "done"
  → If "done": no-op (idempotent)
```

## Dual Session IDs

| ID | Lifecycle | Purpose |
|----|-----------|---------|
| `content_session_id` | Stable — assigned at session creation | ALL database operations (observations, summaries, lookups) |
| `memory_session_id` | Lazy-captured — may be NULL initially | SDK session resume only (e.g., Claude API `session_id`) |

## Invariants
- **Once per session**: Stop hook triggers compression exactly once. Re-entry is idempotent via `compression_status` check
- **Dual-ID separation**: NEVER use `memory_session_id` for DB queries — it may be NULL or change
- **NULL check before resume**: If `memory_session_id` is NULL, session cannot be resumed via SDK — create new session
- **Retain originals**: Compression produces summary but does NOT delete raw observations (needed for citation and audit)
- **Single LLM call**: Summary generated in one pass, not incremental — controls cost

## Violations and Costs

| Violation | Cost |
|-----------|------|
| Compress at PostToolUse instead of Stop | N compressions instead of 1 — token waste proportional to tool count |
| Use memory_session_id for DB queries | NULL pointer errors, orphaned records, broken lookups |
| Delete raw observations after compression | Loss of citation trail, audit failure, irreversible |
| Skip compression_status check | Duplicate summaries on Stop re-entry (crash recovery) |

## Trigger

Auto-applies to: Stop hook implementation. Compression is the final memory operation before session teardown.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_session_compression]] | upstream | 0.47 |
| [[p10_ax_lifecycle_hooks]] | sibling | 0.31 |
| [[p10_ss_[session_slug]]] | related | 0.30 |
| [[p01_kc_memory_summary]] | related | 0.28 |
| [[p10_memory_summary]] | related | 0.28 |
| [[p01_kc_memory_lifecycle_hooks]] | upstream | 0.28 |
| [[bld_collaboration_memory_summary]] | downstream | 0.27 |
| [[p01_kc_session_state]] | related | 0.27 |
| [[memory-summary-builder]] | related | 0.26 |
| [[bld_memory_session_state]] | related | 0.26 |
