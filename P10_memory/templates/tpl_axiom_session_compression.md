---
# TEMPLATE: Axiom — Session Compression (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.axiom)
# Max 3072 bytes

id: p10_ax_{{RULE_SLUG}}
kind: axiom
pillar: P10
title: "Axiom: Session Compression"
quality: {{QUALITY_8_TO_10}}
---

# Axiom: Session Compression

## Rule
Compression fires exactly once per session at the Stop hook. It produces a summary from accumulated observations. Original observations are retained for citation; the summary is the primary retrieval artifact.

## Dual Session IDs

| ID | Lifecycle | Purpose |
|----|-----------|---------|
| `content_session_id` | Stable — assigned at session creation | Used for ALL database operations (observations, summaries, lookups) |
| `memory_session_id` | Lazy-captured — may be NULL initially | Used only for SDK session resume (e.g., Claude API `session_id`) |

## Invariants
- **Once per session**: Stop hook triggers compression exactly once. Re-entry is idempotent (check `compression_status`).
- **Dual-ID separation**: Never use `memory_session_id` for DB queries — it may be NULL.
- **NULL check before resume**: If `memory_session_id` is NULL, session cannot be resumed via SDK. Create a new session instead.
- **Retain originals**: Compression produces a summary but does NOT delete raw observations (needed for citation and audit).

## Compression Flow
```
Stop fires → Check compression_status → If "pending":
  → Fetch all observations for content_session_id
  → Generate summary via LLM
  → Store summary with content_session_id
  → Set compression_status = "done"
```

## Rationale
- Why: Per-tool compression wastes tokens and creates partial summaries; once-at-stop is optimal cost/quality
- Protects: Token budget — compression is expensive and must run exactly once

## Examples
- Correct: Stop hook checks `compression_status == "pending"`, compresses, sets to "done"
- Incorrect: PostToolUse triggers compression on every tool call (N compressions instead of 1)
