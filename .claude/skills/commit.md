---
name: commit
description: Stage changes, write conventional commit grouped by nucleus, run pre-commit hooks. Use when user says "commit", "/commit", or explicitly asks to save changes to git.
related:
  - p01_kc_git_hooks_ci
  - kc_git_workflow_for_agents
  - p04_hook_pre_commit_qa
  - p03_ins_action_protocol
  - p12_wf_auto_ship
  - p12_ho_admin_template
  - p11_gr_action_reversibility
  - bld_examples_handoff
  - p01_kc_orchestration_best_practices
  - agent_card_engineering_nucleus
---

# commit — CEX-aware git commit

Write a commit that fits this repo's conventions and survives hooks.

## Protocol

1. Inspect state in parallel:
   - `git status -s` (never `-uall`)
   - `git diff --stat`
   - `git log --oneline -5` (match house style)
2. Group staged files by nucleus prefix: `N01_*`, `N02_*`, ..., `_tools/*`, `.claude/*`.
3. Compose message:
   - Subject: `[N0x] <verb> <noun>` (≤70 chars). If touches multiple nuclei, use `[N07]` + scope names in body.
   - Body: 1-3 bullets on WHY, not WHAT.
   - Trailer: `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
4. Stage specific files (no `git add -A` unless user explicit). Reject `.env`, `credentials*`, large binaries.
5. Run `git commit` via HEREDOC for multiline safety.
6. If pre-commit hook fails: fix underlying issue (NEVER `--no-verify`), re-stage, create a NEW commit (NEVER `--amend`).
7. `git status` after to confirm clean.

## Mandatory refusals

- No `--no-verify`, no `--no-gpg-sign`, no `--amend` of published commits.
- No force-push, no destructive ops without explicit user request.
- Do not commit secrets. If a secret sneaked in, warn loudly.

## Output

Report: commit SHA, files changed, hook results. Under 3 lines.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_git_hooks_ci]] | related | 0.46 |
| [[kc_git_workflow_for_agents]] | related | 0.35 |
| [[p04_hook_pre_commit_qa]] | related | 0.35 |
| [[p03_ins_action_protocol]] | related | 0.31 |
| [[p12_wf_auto_ship]] | related | 0.30 |
| [[p12_ho_admin_template]] | related | 0.28 |
| [[p11_gr_action_reversibility]] | related | 0.26 |
| [[bld_examples_handoff]] | related | 0.26 |
| [[p01_kc_orchestration_best_practices]] | related | 0.26 |
| [[agent_card_engineering_nucleus]] | related | 0.25 |
