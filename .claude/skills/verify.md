---
id:
kind:
pillar:
title:
version: 1.0.0
quality: 8.6
density_score: 1.0
---

# N03 — 3 items only, 1 commit, then signal

**Done**: 22/25 BORIS items across 7 commits (see `git log --grep BORIS_MERGE`)

## Remaining 3 items → 1 commit `[N03] BORIS_MERGE Wave D tail: D1+D3+D4`

- **D1** `.claude/skills/verify.md` + mirror `.cex/skills/verify.md` — chain: `bun run test || npm test || pytest` (~60 lines each)
- **D3** `_tools/cex_boot_gen.py` — update template to emit `isolation: worktree` frontmatter + `--dangerously-skip-permissions` + permissions allowlist stub
- **D4** `.cex/experiments/smoke_boris_merge.yaml` — smoke spec for `/fullrun boris_merge` across claude/codex/ollama (skip gemini per 2026-04-15 memory)

## Signal after 1 commit
```bash
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('n03', 'complete', 9.0, mission='BORIS_MERGE_TAIL')"
```
