---
id:
kind:
pillar:
title:
version: 1.0.0
quality: 8.6
density_score: 1.0
related:
  - p12_ho_admin_template
  - p03_sp_n03_creation_nucleus
  - agent_card_engineering_nucleus
  - p12_dr_software_project
  - p01_kc_git_hooks_ci
  - spec_multi_runtime_features
  - p12_mission_software_engineering_n03
  - p12_wf_auto_ship
  - p01_kc_orchestration_best_practices
  - p02_agent_creation_nucleus
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_ho_admin_template]] | related | 0.25 |
| [[p03_sp_n03_creation_nucleus]] | related | 0.23 |
| [[agent_card_engineering_nucleus]] | related | 0.22 |
| [[p12_dr_software_project]] | related | 0.21 |
| [[p01_kc_git_hooks_ci]] | related | 0.21 |
| [[spec_multi_runtime_features]] | related | 0.20 |
| [[p12_mission_software_engineering_n03]] | related | 0.18 |
| [[p12_wf_auto_ship]] | related | 0.18 |
| [[p01_kc_orchestration_best_practices]] | related | 0.17 |
| [[p02_agent_creation_nucleus]] | related | 0.17 |
