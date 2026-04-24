---
id: p10_ax_privacy_controls
kind: axiom
8f: F4_reason
pillar: P10
title: "Axiom: Edge-Layer Privacy Controls"
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
quality: 9.0
tags: [axiom, privacy, edge, hooks, tags]
tldr: "Privacy enforced at edge (hook layer), not center (daemon). <private> tags stripped before HTTP send. Data never leaves client boundary unfiltered."
max_bytes: 3072
density_score: 0.90
source: organization-core/records/core/memory/hooks/ (privacy filtering layer)
linked_artifacts:
  template: tpl_axiom_privacy_controls
  related: p10_ax_lifecycle_hooks
related:
  - p01_kc_memory_privacy_controls
  - p10_ax_lifecycle_hooks
  - bld_architecture_daemon
  - p01_kc_memory_lifecycle_hooks
  - bld_collaboration_daemon
  - hook-builder
  - bld_architecture_hook
  - p03_sp_hook_builder
  - daemon-builder
  - p04_hook_NAME
---

# Axiom: Edge-Layer Privacy Controls

## Statement

> Privacy enforcement happens at the edge (hook layer), not at the center (daemon/DB). Content tagged as private never reaches the persistence layer. The client boundary is the security perimeter.

## Rule

```
User message with <private>...</private>
  → Hook layer: strip <private> tags, sanitize content
  → HTTP POST sanitized text to daemon
  → Worker layer: strip <context> tags (prevent re-storage loops)
  → DB write (clean data only)
```

## Tag Types

| Tag | Controlled By | Stripped At | Purpose |
|-----|--------------|------------|---------|
| `<private>` | User | Hook layer (before HTTP send) | User-controlled exclusion from memory |
| `<context>` | System | Worker layer (before re-storage) | Injected context — prevent re-storage loops |

## Worker Skip Signal

When the daemon determines an observation should not be stored (duplicate, low-value, or system-flagged), it returns `skipped: true` in the HTTP response. The hook aborts the observation pipeline without error (exit 0).

## Exit Codes

| Code | Meaning | Effect |
|------|---------|--------|
| 0 | Success or graceful skip | Continue |
| 1 | Non-blocking (tag parse warning) | Log, continue |
| 2 | Blocking (privacy violation detected) | Halt, do NOT persist |

## Invariants
- **Edge enforcement**: private data is stripped BEFORE leaving the client process
- **Never trust daemon for privacy**: daemon is a persistence layer, not a security boundary
- **Exit 2 on violation**: if `<private>` stripping fails, hook MUST block (exit 2) to prevent leak
- **No regex on secrets**: use tag boundaries only — never pattern-match for API keys or passwords

## Violations and Costs

| Violation | Cost |
|-----------|------|
| Strip `<private>` at daemon instead of hook | Data already transmitted over HTTP — breach |
| Regex-match secrets instead of tag-based | False negatives, maintenance burden, security theater |
| Ignore `<context>` re-storage | Infinite loop: inject -> capture -> inject -> capture |
| Exit 0 on strip failure | Private data persisted to DB — irrecoverable |

## Trigger

Auto-applies to: every PostToolUse and UserPromptSubmit hook that processes text content. Privacy check runs BEFORE any HTTP call to daemon.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_privacy_controls]] | upstream | 0.54 |
| [[p10_ax_lifecycle_hooks]] | sibling | 0.34 |
| [[bld_architecture_daemon]] | upstream | 0.28 |
| [[p01_kc_memory_lifecycle_hooks]] | upstream | 0.26 |
| [[bld_collaboration_daemon]] | downstream | 0.25 |
| [[hook-builder]] | upstream | 0.25 |
| [[bld_architecture_hook]] | upstream | 0.24 |
| [[p03_sp_hook_builder]] | upstream | 0.24 |
| [[daemon-builder]] | upstream | 0.23 |
| [[p04_hook_NAME]] | upstream | 0.23 |
