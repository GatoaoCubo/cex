---
id: p12_wf_auto_handoff
kind: workflow
pillar: P12
title: "Auto-Handoff — Session end / context overflow management"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: session_end_or_overflow
quality: 9.0
tags: [workflow, auto, n07, handoff, session, context, overflow]
tldr: "When session ends or context window fills: commit all work, write handoff with progress, archive state for next session."
density_score: 0.93
related:
  - p01_kc_context_overflow
  - p01_kc_handoff
  - handoff-builder
  - bld_architecture_handoff
  - bld_collaboration_handoff
  - bld_collaboration_session_state
  - p03_sp_handoff_builder
  - handoff-protocol-builder
  - p12_ho_admin_template
  - bld_knowledge_card_handoff
---

# Auto-Handoff

## Trigger
- Session about to end (user says goodbye, timeout)
- Context window approaching limit (>80% used)
- Explicit: user says "I need to go" or "save progress"

## Industry Pattern
Shift handoff in operations. Outgoing shift documents state for incoming shift.

## Steps

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | Commit all pending work | `git add -A && git commit` | No work lost |
| 2 | Write handoff document | Write to `.cex/runtime/handoffs/` | Progress summary |
| 3 | Write signals for any completed tasks | `signal_writer.py` | Signals for peers |
| 4 | Archive current plan state | Copy plan + manifest to archive | Recoverable |
| 5 | Update CLAUDE.md if needed | Edit brand/status sections | System prompt current |

## Handoff Document Format

```markdown
# Handoff — {timestamp}

## Completed This Session
- {list of completed tasks}

## In Progress
- {task}: {what's done, what's left}

## Pending
- {tasks not started}

## Files Modified
- {git diff --stat}

## Next Session Start With
1. Read this handoff
2. Run /doctor
3. Continue from: {specific task}
```

## Failure Mode
Can't commit (conflict) → stash + write handoff anyway. Next session resolves conflict.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_context_overflow]] | upstream | 0.39 |
| [[p01_kc_handoff]] | related | 0.34 |
| [[handoff-builder]] | related | 0.33 |
| [[bld_architecture_handoff]] | upstream | 0.31 |
| [[bld_collaboration_handoff]] | related | 0.31 |
| [[bld_collaboration_session_state]] | upstream | 0.30 |
| [[p03_sp_handoff_builder]] | upstream | 0.30 |
| [[handoff-protocol-builder]] | upstream | 0.30 |
| [[p12_ho_admin_template]] | related | 0.29 |
| [[bld_knowledge_card_handoff]] | upstream | 0.29 |
