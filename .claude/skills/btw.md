---
name: btw
description: Capture an ad-hoc observation, fact, or decision the user drops mid-work ("by the way…") into the right memory or KC without breaking flow. Use when user says "/btw", "btw …", or "remember this".
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
