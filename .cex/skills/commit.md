---
name: commit
description: Stage changes, write conventional commit grouped by nucleus, run pre-commit hooks.
runtime_agnostic: true
invoked_by: [claude, codex, gemini, ollama]
activation:
  triggers: ["/commit", "commit changes", "save to git", "commit this"]
  nuclei: [N00, N01, N02, N03, N04, N05, N06, N07]
  depth: full
mirror_of: .claude/skills/commit.md
---

# commit — CEX-aware git commit

Write a commit that fits this repo's conventions and survives hooks.

## Protocol

1. Inspect state in parallel:
   - `git status -s` (never `-uall`)
   - `git diff --stat`
   - `git log --oneline -5` (match house style)
2. Group staged files by nucleus prefix: `N01_*`, `N02_*`, ..., `_tools/*`, `.claude/*`, `.cex/*`.
3. Compose message:
   - Subject: `[N0x] <verb> <noun>` (<=70 chars). Cross-nucleus touches use `[N07]` with scope in body.
   - Body: 1-3 bullets on WHY, not WHAT. Reference mission name if applicable (e.g., `BORIS_MERGE`).
   - Trailer: `Co-Authored-By: <runtime> <model>` (e.g., `Claude Opus 4.6`, `Codex gpt-4o`, `Gemini 2.5 Pro`, `Ollama qwen3:14b`).
4. Stage specific files. Reject `.env`, `credentials*`, large binaries.
5. Run `git commit` via HEREDOC (PowerShell: `@'...'@`, bash: `<<'EOF'`).
6. If pre-commit hook fails: fix root cause (NEVER `--no-verify`), re-stage, NEW commit (NEVER `--amend`).
7. `git status` after to confirm clean.

## Mandatory refusals

- No `--no-verify`, `--no-gpg-sign`, `--amend` of pushed commits, force-push to main.
- No secret commits. If one slips in, warn loudly.

## Output

Commit SHA, files changed, hook results. <=3 lines.
