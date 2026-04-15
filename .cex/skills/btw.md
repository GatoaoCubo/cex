---
name: btw
description: Capture an ad-hoc observation, fact, or decision into the right memory or KC without breaking flow.
runtime_agnostic: true
invoked_by: [claude, codex, gemini, ollama]
activation:
  triggers: ["/btw", "btw ", "by the way", "remember this", "remember that"]
  nuclei: [N00, N01, N02, N03, N04, N05, N06, N07]
  depth: full
mirror_of: .claude/skills/btw.md
---

# btw — inline memory capture

User is in flow and drops context that should survive the session. Route it, don't interrupt.

## Decision tree

1. Classify:
   - **User fact / preference / correction** -> `<project_memory>/` as `feedback_*.md` or `user_*.md`.
   - **Project state / decision / deadline** -> `.cex/runtime/` or `N0x/memory/` as `project_*.md`.
   - **External pointer** -> `reference_*.md`.
   - **Reusable domain knowledge** -> `P01_knowledge/library/kind/kc_*.md` (full KC, not memory).
2. Grep target dir for duplicates before writing a new file.
3. Update `MEMORY.md` index with 1-line hook (<=150 chars).
4. Confirm in 1 line: `Saved: <path> -- <topic>`. Return to prior task.

## What NOT to capture

- Transient task state (use TaskCreate / TodoWrite).
- Code patterns already visible in the repo.
- Git history / who-changed-what.
- Anything already in CLAUDE.md.

## Frontmatter template

```yaml
---
name: {slug}
description: {1 line trigger}
type: {user|feedback|project|reference}
---

{body -- fact first; feedback/project add **Why:** and **How to apply:**}
```

## Runtime path resolution

- Claude: `~/.claude/projects/<project_hash>/memory/`
- Codex/Gemini/Ollama: `.cex/memory/{runtime}/` (per-runtime local, synced nightly via `cex_memory_sync.py`)
