---
mission: POLISH
wave: 2
status: PASS
executed_by: n07_direct
planned_dispatch: ollama (README) + N07 direct (mechanical)
actual_dispatch: N07 direct for all 4 tasks
tasks_completed: 4 of 4
files_deleted: 149
bytes_deleted: ~670KB
commits: 4
ahead_of_origin: 160
---

# POLISH W2 Consolidation

## Summary

Front-page cleanup driven by user's GitHub listing review. Surgical removals
of commit-message-as-filename bug artifacts, orphan root files, duplicate
nucleus/pillar dirs, plus README.md metric refresh to match CLAUDE.md.

**Runtime choice:** ollama was available (qwen2.5-coder:7b up), but the 4
tasks were all mechanical (git rm + 7 surgical number swaps on README).
Per `feedback_multiruntime_verification.md`: mechanical tasks -> N07 direct
is faster than fighting LLM fabrication. Ollama skipped.

## Tasks

| # | task | executor | files | commit |
|---|------|----------|-------|--------|
| 1 | Delete 3 commit-msg-as-filename bug files | N07 | 3 | 6a3560a81 |
| 2 | Delete 6 orphan root files | N07 | 6 | c109cc05b |
| 3 | Delete 5 duplicate/orphan dirs (140 files) | N07 | 140 | bf7524693 |
| 4 | README.md metric+routing refresh | N07 | 1 | c492b46cb |

## Task 1: commit-msg-as-filename bug

Files removed (generator bug, content captured as filename):
- `- Keep and complete YAML frontmatter`
- `- More efficient resource utilization through parallel processing`
- `- Update workflow policies`

Root cause: some artifact writer wrote commit-message-like lines as
filename. Not traced to a specific tool in this wave (deferred to W3 audit).

## Task 2: orphan root files

Files (should have landed in pillar dirs, landed at root instead):
- `core` -> was a truncated `kc_nucleus_def` copy
- `phases` -> `p04_kc_phases` (kind: knowledge_card, missing `.md`)
- `steps` -> `p04_kc_steps` (same bug)
- `quality_gate` -> duplicate of `P01_knowledge/library/kind/kc_quality_gate.md`
- `program.md` -> autoResearch instructions, superseded by `_tools/cex_evolve.py`
- `n02_task_git_workflow_for_agents.md` -> orphan task artifact

Pattern: generators writing to root without pillar path resolution.
Needs linter rule: reject writes to repo root unless whitelisted.

## Task 3: duplicate/orphan dirs

| Dir | Files | Reason |
|-----|-------|--------|
| `N03_builder/` | 30 | Legacy name; CLAUDE.md references `N03_engineering/` |
| `P03_prompts/` | 42 | Plural typo; CLAUDE.md references `P03_prompt/` |
| `n01_knowledge/` | 48 | Lowercase variant; `N01_intelligence/` owns these |
| `n01_knowledge_library/` | 1 | Orphan stub |
| `path/` | 19 | Literal `path/to/` placeholder bug; generator wrote to default |

Reference check: all 5 dirs were only mentioned in historical audit reports
(audit_pi_references, self_audit_n03, system_health_20260413). No active
code depends on them. Canonical copies exist in archetypes/builders/ and
N03_engineering/.

## Task 4: README.md refresh

Before / After (aligned to CLAUDE.md header):

| Metric | Before | After |
|--------|--------|-------|
| Artifact kinds | 132 / 115 | 257 |
| Builders | 128 / 111 | 262 |
| Builder ISOs total | -- | 3381 |
| CLI tools | 83 / 52 / 51 | 82 |
| Nuclei | 7 | 8 (N00-N07) |
| Sub-agents | 110 | 125 |

Routing table rebuilt: dropped Gemini defaults for N01/N04 (free tier
unusable per `project_gemini_free_tier_unusable_2026_04_15.md`). Current
budget split: 2 Opus (N03, N07) + 5 Sonnet. Added Context + Tier columns.
Documented cex_preflight.py ~70% token savings.

Key Numbers: removed stale compiled-artifacts (898) and examples (369)
counts -- they drift faster than doc ships. Kept only load-bearing
metrics (kinds, builders, ISOs, tools, pillars, nuclei, flywheel checks).

## Verification

```
$ git log --oneline -4
c492b46cb docs(readme): POLISH W2 refresh metrics + routing
bf7524693 chore(cleanup): POLISH W2 remove 5 duplicate/orphan dirs (140 files)
c109cc05b chore(cleanup): POLISH W2 remove 6 orphan root files (generator misfires)
6a3560a81 chore(cleanup): POLISH W2 remove 3 commit-msg-as-filename bug files

$ grep -nE "128|115|111|117|52|51" README.md
(no matches)

$ git status
On branch main
nothing to commit, working tree clean

$ git rev-list --count origin/main..HEAD
160
```

## Remote divergence

**160 commits local vs origin/main.** Includes POLISH W1 (9 commits) +
POLISH W2 (4 commits) + ~147 prior cycles. User owns the `git push`
trigger. Front-page staleness visible in the GitHub listing will clear
once pushed.

## Next

1. **git push origin main** -- user trigger; clears 160-commit staleness
2. **Linter rule** -- reject root writes unless whitelisted (prevents W2.1+W2.2 recurrence)
3. **Codex dispatch diagnosis** (deferred from W1) -- why wrapper exits within 2min
4. **Generator audit** -- find which tool produced the 3 commit-msg-as-filename files
