---
name: btw
description: Capture an ad-hoc observation, fact, or decision the user drops mid-work ("by the way…") into the right memory or KC without breaking flow. Use when user says "/btw", "btw …", or "remember this".
related:
  - p04_skill_memory_extract
  - bld_collaboration_memory_type
  - bld_collaboration_memory_scope
  - p01_kc_memory_scope
  - bld_manifest_memory_type
  - memory-scope-builder
  - atom_22_memory_taxonomy
  - bld_memory_runtime_state
  - bld_knowledge_card_memory_scope
  - SPEC_04_memory_system
---

# btw — inline memory capture

User is in flow and drops context that should survive the session. Route it, don't interrupt.

## Decision tree

1. Classify the input:
   - **User fact / preference / correction** → `~/.claude/projects/.../memory/` as `feedback_*.md` or `user_*.md`.
   - **Project state / decision / deadline** → `.cex/runtime/` or `N0x/memory/` as `project_*.md`.
   - **External pointer (Linear, Slack, Grafana)** → `reference_*.md`.
   - **Reusable domain knowledge** → `P01_knowledge/library/kind/kc_*.md` (full KC, not memory).
2. Check for duplicates via `Grep` on the target dir before writing a new file.
3. Update `MEMORY.md` index with 1-line hook (≤150 chars).
4. Confirm capture in 1 line: `Saved: <path> — <topic>`. Return to prior task.

## What NOT to capture

- Transient task state (use TaskCreate instead).
- Code patterns already visible in the repo.
- Git history / who-changed-what.
- Anything already in `CLAUDE.md`.

## Frontmatter template

```yaml
---
name: {slug}
description: {1 line — used to surface this memory later}
type: {user|feedback|project|reference}
---

{body — lead with the fact; for feedback/project add **Why:** and **How to apply:**}
```

## Multi-runtime note

This skill is cross-runtime. Non-Claude runtimes read the mirrored copy under `.cex/skills/btw.md` via their boot wrapper. Behavior is identical.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_skill_memory_extract]] | related | 0.32 |
| [[bld_collaboration_memory_type]] | related | 0.31 |
| [[bld_collaboration_memory_scope]] | related | 0.29 |
| [[p01_kc_memory_scope]] | related | 0.29 |
| [[bld_manifest_memory_type]] | related | 0.25 |
| [[memory-scope-builder]] | related | 0.25 |
| [[atom_22_memory_taxonomy]] | related | 0.24 |
| [[bld_memory_runtime_state]] | related | 0.23 |
| [[bld_knowledge_card_memory_scope]] | related | 0.23 |
| [[SPEC_04_memory_system]] | related | 0.22 |
