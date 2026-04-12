---
id: p12_handoff_builder_construction
kind: handoff
pillar: P12
title: "Handoff Contract — N03 Builder"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 8.9
tags: [handoff, builder, N03, contract, dispatch, orchestration]
tldr: "Handoff contract defining what N07 must provide and what N03 must deliver when receiving construction tasks."
density_score: 0.94
linked_artifacts:
  primary: "N03_builder/orchestration/dispatch_rule_builder.md"
  related:
    - N03_builder/orchestration/workflow_builder.md
    - N03_builder/orchestration/signal_builder.md
---

# Handoff Contract — N03 Builder

## Purpose

Defines the contract between N07 Orchestrator (sender) and N03 Builder (receiver)
for construction task handoffs. Both sides must comply to ensure clean task flow,
no re-asking of decided questions, and proper completion signaling.

## Inbound Contract (N07 → N03)

### Required Fields in Handoff File

```yaml
---
nucleus: N03
task: dispatch
created: {ISO timestamp}
---
```

### Required Sections

| Section | Content |
|---------|---------|
| `# Task for N03` | Clear description of what to build |
| `## DECISIONS` | Path to decision manifest if GDP decisions were made |
| `## ON COMPLETION` | Commit convention and signal command |
| `## SIGNAL` | Exact signal_writer command to emit |

### Handoff File Location

```
.cex/runtime/handoffs/n03_task.md
```

### Example Handoff

```markdown
---
nucleus: N03
task: dispatch
created: 2026-04-07T19:00:00-03:00
---
# Task for N03

Build the agent_card for N03 builder nucleus with full 8F pipeline.

## DECISIONS (from user -- DO NOT re-ask)
Read: .cex/runtime/decisions/decision_manifest.yaml

## ON COMPLETION
1. Commit: git add -A && git commit -m "[N03] <description>"
2. Signal complete:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
```

## Outbound Contract (N03 → N07)

### On Success

1. **Commit**: All artifacts committed with `[N03]` prefix
2. **Signal**: `write_signal('n03', 'complete', 9.0)` to `.cex/runtime/signals/`
3. **Artifacts**: Listed in signal JSON `artifacts` field

### On Error

1. **Signal**: `write_signal('n03', 'error', 0.0, 'error description')`
2. **No partial commits**: Revert or stash incomplete work
3. **Error detail**: Include what failed and at which 8F step

### On Progress (long tasks)

1. **Signal**: `write_signal('n03', 'progress', 0.0, 'step N of M')`
2. **Periodic**: Every 3-4 artifacts or every 10 minutes

## Rules

1. N03 MUST read the entire handoff before starting
2. N03 MUST NOT re-ask questions listed under `## DECISIONS`
3. N03 MUST commit with `[N03]` prefix
4. N03 MUST signal on completion (success or error)
5. N07 MUST provide decision manifest path if GDP decisions exist
6. N07 MUST provide clear task description (not vague intent)
7. Handoff file is consumed once — move to `.cex/runtime/handoffs/_done/` after

## References

- Signal protocol: N03_builder/orchestration/signal_builder.md
- Dispatch rules: N03_builder/orchestration/dispatch_rule_builder.md
- Workflow: N03_builder/orchestration/workflow_builder.md
