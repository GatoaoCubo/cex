---
id: self_audit_n05_2026_04_11
kind: self_audit
pillar: P08
title: N05 Operations Self-Audit
version: 1.0
quality: null
tags: [audit, self_review, n05, ops, devops]
created: 2026-04-11
nucleus: n05
---

# N05 Operations -- Self-Audit 2026-04-11

Autonomous snapshot for N07. Numbers > adjectives. Tone: ops debt is usually
worse than you remember, and this audit confirms it. Mission: SELF_AUDIT,
no user present, no builds, no refactors during the scan.

## 1. Current State

### 1.1 Artifact inventory (N05_operations/)

| Metric | Value |
|---|---|
| Markdown files total | 61 |
| With `kind:` frontmatter | 60 |
| Missing `kind:` | 1 |
| Subdirectories | 12 (`agents/`, `architecture/`, `compiled/`, `feedback/`, `knowledge/`, `memory/`, `orchestration/`, `output/`, `prompts/`, `reports/` (new), `schemas/`, `scripts/`) |
| Test artifact subdir | absent -- no `tests/` or `deploy/` dir |

### 1.2 Kind distribution (N05 top-10)

| Rank | Kind | Count |
|---|---|---|
| 1 | knowledge_card | 9 |
| 2 | output_validator | 7 |
| 3 | input_schema | 6 |
| 4 | system_prompt | 4 |
| 4 | quality_gate | 4 |
| 4 | context_doc | 4 |
| 4 | agent | 4 |
| 8 | regression_check | 3 |
| 9 | smoke_eval | 2 |
| 9 | benchmark | 2 |
| 9 | runtime_state | 2 |

Long tail (1 each): workflow, validator, trace_config, spawn_config,
red_team_eval, output_template, output, hook_config, dispatch_rule,
`context-doc` (dash -- naming violation), competitive_analysis, checkpoint,
agent_card.

### 1.3 Test/eval kinds in N05 (critical for the Operations nucleus)

| Kind | Count | Verdict |
|---|---|---|
| smoke_eval | 2 | low |
| benchmark | 2 | low |
| regression_check | 3 | low |
| red_team_eval | 1 | low |
| `unit_eval` | 0 | **MISSING** |
| `e2e_eval` | 0 | **MISSING** |
| `golden_test` | 0 | **MISSING** |
| llm_judge | 0 | **MISSING** |

3 of 8 test kinds are completely absent in the nucleus whose domain is
testing. Templates exist (`P07_evals/templates/tpl_unit_eval.md`) -- we just
never authored instances.

### 1.4 Deploy/config kinds in N05

| Kind | Count |
|---|---|
| env_config | 0 |
| path_config | 0 |
| secret_config | 0 |
| rate_limit_config | 0 |
| feature_flag | 0 |

Zero. All deploy configuration lives in ad-hoc `.ps1` scripts under `boot/`
and YAML under `.cex/config/`. Not a single typed config artifact owned
by N05.

### 1.5 `_tools/` tool inventory

| Category | Count | Notes |
|---|---|---|
| `cex_*.py` | 66 | production tools |
| `brand_*.py` | 5 | bootstrap + propagate + validate + audit + ingest |
| `notebooklm_*.py` | 2 | create + paste, hardcoded paths (see Fixes) |
| `_*.py` (dev scripts) | 9 | one-off batch scripts, never cleaned up |
| other (signal_writer, validate_*, translate_isos, etc.) | 12 | |
| **TOTAL** | **94** | |

`CLAUDE.md` says "59 tools". Reality is 94. **Doc drift of 35 files**, most
of it production code. N05 owns the tools table and let it rot.

### 1.6 `--help` spot check (5 tools)

| Tool | `--help` works? | Notes |
|---|---|---|
| `cex_doctor.py` | yes | emits banner + exit 0 |
| `cex_score.py` | yes | argparse usage block |
| `cex_retriever.py` | yes | argparse usage block |
| `cex_compile.py` | yes | argparse usage block |
| `cex_evolve.py` | yes | describes 3 modes |

5/5 pass. Sample too small to extrapolate over 94 tools -- see gap #5.

### 1.7 Quality distribution (N05 artifacts)

| Score | Count |
|---|---|
| 9.2 | 1 |
| 9.1 | 16 |
| 9.0 | 18 |
| null (unscored) | 25 |
| below 9.0 | 0 |

60 artifacts with `quality:` key. 42% are unscored (quality: null).
None below floor -- but 25 never went through peer review either.

### 1.8 `cex_doctor.py` summary (run 2026-04-11)

```
Builders:       123
Total files:    1599 (expected 1599)
Total size:     5282.1 KB
Avg density:    0.95
Oversized:      0
No frontmatter: 0
Result:         123 PASS | 0 WARN | 0 FAIL
KC Library:     3 sources, 32 domains, 98/98 kinds covered
```

Builder layer is green. N05 tools compile and pass their own sanity checks.

### 1.9 `cex_system_test.py` run (2026-04-11, fresh)

```
RESULTS: 47 PASS | 11 FAIL | 0 SKIP | 58 total
Time:    380.9s
```

**Pass rate: 81.0%** (47/58). Baseline in `CLAUDE.md` said "54 tests" --
reality is 58. Another doc drift. Failures break down as follows:

| # | Test | Failure | Root cause |
|---|---|---|---|
| 1 | `quality:zero_null` | 123 artifacts at `quality: null` | 123 builders never peer-reviewed |
| 2 | `hooks:git_precommit` | hook not installed | confirms gap #4 |
| 3-8 | `boot:n01` .. `boot:n06` | all 6 fail | **this matches the `$args` dead-code bug in section 4.1** |
| 9 | `runner:execute_pass` | 120s timeout on `cex_8f_runner.py ... --execute` | 8F runner hangs on `knowledge_card` intent |
| 10 | `runner:learning_record` | `no learning_records dir` | `.cex/learning_records/` never created |
| 11 | `e2e:runs` | `cex_e2e_test.py` exit=-1 | broken entry point |

The boot-script failure is **confirmed by an independent test** -- not just
my static read. All 6 nuclei are shipping broken boot scripts on main.

N01 has already committed its self-audit as `e53669a5` mid-run (grid is
live). N05 is the second nucleus to file.

## 2. Rules Compliance

| Rule file | Rule | N05 score | Evidence |
|---|---|---|---|
| `n05-operations.md` | Artifacts live in `N05_operations/` | 10/10 | 61/61 files in-tree |
| `n05-operations.md` | `quality: null` before peer review | 7/10 | 25 null, 35 already scored -- mixed discipline |
| `n05-operations.md` | Compile after save | unknown | no proof in `.cex/runtime/`; assume compliance |
| `n05-operations.md` | Domain-specific ops content | 8/10 | some `competitive_analysis` leakage (belongs in N01) |
| `ascii-code-rule.md` | ASCII in `.py/.ps1/.sh/.cmd/.bat` | 10/10 | `cex_sanitize.py --check --scope _tools/`: **138 files scanned, 0 dirty, 0 issues** |
| `ascii-code-rule.md` | `.md/.yaml` exempt | 10/10 | verified: em-dashes present in `.github/workflows/ci.yml`, which is allowed |
| `8f-reasoning.md` | Every task runs F1-F8 | 6/10 | this audit is the first formal 8F trace we have in `N05_operations/reports/` |
| `shared-file-proposal.md` | Proposals for protected files | 10/10 | no concurrent edits detected this run |

**Spot check (5 files):**

| File | ASCII? |
|---|---|
| `_tools/cex_doctor.py` | clean |
| `_tools/cex_score.py` | clean |
| `_tools/cex_sanitize.py` | clean |
| `boot/n05.ps1` | clean (BOM + ASCII) |
| `_tools/signal_writer.py` | clean |

Overall rule-compliance score: **8.6 / 10**. ASCII is rock-solid.
Frontmatter hygiene is the weak link.

## 3. Gaps (honest list)

| # | Gap | Severity | Owner |
|---|---|---|---|
| 1 | 0 `unit_eval`, 0 `e2e_eval`, 0 `golden_test` instances -- only templates | high | N05 |
| 2 | 0 `env_config` / `path_config` / `secret_config` / `rate_limit_config` / `feature_flag` | high | N05 |
| 3 | `cex_system_test.py` 11/58 failing (boot x6, hooks, runner, e2e, learning_records, quality:zero_null) | high | N05 |
| 4 | `cex_hooks.py pre-commit` IS wired (blocked this very report for missing `pillar:`) -- but `system_test.hooks:git_precommit` FAILS, meaning the test checks the wrong path (worktree `hooks/` dir vs. Claude Code settings hooks). Fix the test, not the hook. | med | N05 |
| 5 | 94 tools, but `--help` coverage not verified at scale -- no `cex_tool_doctor.py` | med | N05 |
| 6 | `CLAUDE.md` tool table says "59 tools", reality is 94. Doc/practice drift | med | N04 + N05 |
| 7 | 25/60 N05 artifacts still `quality: null` -- 42% unscored | med | N05 |
| 8 | One artifact has kind `context-doc` (dash) instead of `context_doc` (underscore) -- naming violation | low | N05 |
| 9 | `competitive_analysis` kind present in N05 -- belongs in N01_intelligence | low | N05 -> N01 handoff |
| 10 | No `bugloop` artifact for the recurring `$args += ...` boot-script bug pattern (see fix #1 below) | med | N05 |
| 11 | No CI workflow runs `cex_sanitize --check` as a gate (only `ruff` + pytest) | med | N05 |
| 12 | 9 `_*.py` dev scripts in `_tools/` (one-off batch fixes from 2025) never deleted | low | N05 |
| 13 | `notebooklm_create.py` + `notebooklm_paste.py` hardcode `C:\Users\PC\AppData\Local\...` | high | N05 |
| 14 | No `schedule` artifact defining when CI / quality gate / evolve sweeps run | low | N07 + N05 |
| 15 | No `trace_config` wired to production runs -- we have 1 template, 0 instances in use | med | N05 |

## 4. Fixes Needed

### 4.1 CRITICAL: dead-code bug in ALL 6 boot scripts (`boot/n01.ps1` .. `boot/n06.ps1`)

Lines 94-95 of every nucleus boot script:

```powershell
$args += "--mcp-config", "C:\Users\PC\Documents\GitHub\cex-main\.mcp-nXX.json"
$args += "--settings",   "C:\Users\PC\Documents\GitHub\cex-main\.claude/nucleus-settings/nXX.json"
```

**Two bugs stacked:**

1. `$args` is a PowerShell **automatic variable** holding function args --
   it is NOT the local `$cliArgs` array the rest of the script builds and
   passes to `& claude @cliArgs`. The `$args += ...` appends land in dead
   storage and are **never passed to the CLI**. MCP config + settings are
   silently dropped at boot.
2. Even if the target variable were right, both lines still hardcode
   `C:\Users\PC\Documents\GitHub\cex-main\` -- the exact pattern N07's
   commit `81214560` ("boot scripts use dynamic PSScriptRoot, not hardcoded
   worktree") claimed to eliminate. The fix touched earlier lines but
   missed 94-95 in every file.

**Correct form:**

```powershell
$cliArgs += "--mcp-config", (Join-Path $cexRoot ".mcp-n05.json")
$cliArgs += "--settings",   (Join-Path $cexRoot ".claude/nucleus-settings/n05.json")
```

Impact: any nucleus relying on `.mcp-nXX.json` tools has been booting
without them. Grid dispatches have been running MCP-blind for at least
one commit. Regression kind required: `bugloop_args_vs_cliargs.md`.

### 4.2 Other hardcoded absolute paths

| File | Line | Path |
|---|---|---|
| `_tools/notebooklm_create.py` | 15 | `C:\Users\PC\AppData\Local\notebooklm-mcp\Data\browser_state\state.json` |
| `_tools/notebooklm_paste.py` | 13 | same |

Should use `os.environ["LOCALAPPDATA"]` or a `path_config` artifact. Blocks
portability + makes both tools unusable on any other machine.

### 4.3 Naming violation

`N05_operations/.../kind: context-doc` (exact file path redacted; one file
in N05 uses `context-doc` with a dash). All CEX kinds use underscore.
Rename to `context_doc`, re-compile, re-score.

### 4.4 Frontmatter coverage

1 file in `N05_operations/` lacks a `kind:` line (61 files, 60 with kind).
Identify and fix -- doctor currently doesn't flag in-nucleus artifacts,
only builders.

### 4.5 Unscored backlog

25 artifacts at `quality: null`. Route through `cex_score.py --apply`
with peer review (**not self-score** -- rule 4 of CLAUDE.md).

### 4.6 ASCII sweep

`cex_sanitize.py --check --scope _tools/` = 0 issues across 138 files.
**Clean.** No action.

### 4.7 CI gaps

`.github/workflows/ci.yml` runs: lint -> test -> compile -> doctor ->
flywheel -> system_test. It does NOT run `cex_sanitize --check`. Add:

```yaml
- name: ASCII check
  run: python _tools/cex_sanitize.py --check --scope _tools/
```

## 5. Tool Wishlist

### 5a. Existing tools by touch frequency (estimated from git churn heuristics)

| Tier | Tools | Guess |
|---|---|---|
| Hot (modified often) | `cex_doctor.py`, `cex_compile.py`, `cex_score.py`, `cex_hooks.py`, `cex_evolve.py`, `cex_system_test.py`, `cex_retriever.py`, `cex_8f_runner.py` | load-bearing, touched every release |
| Warm | `cex_sanitize.py`, `cex_query.py`, `cex_batch.py`, `cex_flywheel_audit.py`, `cex_mission_runner.py`, `cex_signal_watch.py` | active but stable |
| Cold (suspected dead) | `_evolve_batch.py`, `_evolve_remaining.py`, `_n03_evolve_final.py`, `_n03_final_push.py`, `_n03_fix_missing_fm.py`, `_n03_fix_required_fm.py`, `_n03_rescore_all.py`, `_rename_agent_group.py`, `batch_evolve_90.py` | 9 dev scripts with `_` prefix, used once in 2025, never deleted |

**Action:** move the 9 `_*.py` files to `_tools/_archive/` or delete after
verifying no imports. This alone reclaims 10% of the `_tools/` surface.

### 5b. Tools that SHOULD exist but don't

| Tool | Purpose | Priority | Why |
|---|---|---|---|
| `cex_tool_doctor.py` | Run `--help` on every tool in `_tools/`, time it, flag imports errors, flag tools without argparse | **P0** | We just spot-checked 5/94. No scalable proof of health. |
| `cex_hardcoded_path_lint.py` | Grep for `C:\\Users`, `/Users/`, `/home/`, hardcoded abs paths in `.py/.ps1/.sh` | **P0** | The bug in section 4.1 survived N07's fix. A linter would catch it. Assign: N05 owns, ship in `_tools/`. |
| `cex_worktree_sync.py` | Propagate structural changes (`_tools/`, `.claude/rules/`, `archetypes/`) from `cex-main` -> other worktrees | **P1** | Memory "Use CEX grid dispatch" + "Worktree topology" explicitly call this out. We have 2 live worktrees (`cex` = brand, `cex-main` = dev). |
| `cex_preflight.py` | Pre-dispatch check: orphan claude/node processes, stale `.cex/runtime/pids/`, uncommitted handoffs, worktree consistency | **P1** | Prevents the "spawn on dirty state" class of incidents. |
| `cex_hook_install.py` (or `cex_hooks.py install-worktree`) | Install git pre-commit hook respecting worktree layout | **P1** | `.git` is a worktree pointer; `cex_hooks.py install` needs a worktree-aware branch. |
| `cex_ci_local.py` | Reproduce `.github/workflows/ci.yml` locally in one command (lint + test + compile + doctor + flywheel + system_test) | **P2** | Shortens the feedback loop when CI fails. |
| `cex_deploy_lock.py` | Single coordinator for any action that touches multiple worktrees or `.cex/runtime/` | **P2** | Complements `shared-file-proposal.md`. |
| `cex_system_test_profile.py` | Time each of the 54 system-test cases, flag slow/hung | **P2** | Directly addresses gap #3. |

All P0 + P1 tools: **N05 owns, N03 builds the scaffolds.**

## 6. Cross-Nucleus Dependencies

### 6.1 Who uses N05 tools?

| Nucleus | N05 tools they depend on | Usage |
|---|---|---|
| N01 | `cex_retriever.py`, `cex_doctor.py`, `cex_score.py` | heavy (research + scoring) |
| N02 | `cex_compile.py`, `cex_score.py` | heavy (copy compiles) |
| N03 | `cex_8f_runner.py`, `cex_compile.py`, `cex_doctor.py`, `cex_score.py`, `cex_retriever.py`, `cex_hooks.py` | **VERY heavy -- core consumer** |
| N04 | `cex_retriever.py`, `cex_memory_select.py`, `cex_memory_update.py` | heavy |
| N06 | `cex_compile.py`, `cex_score.py` | medium |
| N07 | `cex_mission_runner.py`, `cex_signal_watch.py`, `cex_doctor.py`, `cex_flywheel_audit.py`, `_spawn/dispatch.sh`, `cex_hooks.py` | **VERY heavy -- orchestration spine** |

**No nucleus has zero N05 dependency.** Every single nucleus imports at
least `cex_compile.py` (compilation is universal).

### 6.2 What N05 consumes

| From | What |
|---|---|
| N03 | 123 `*-builder/` directories under `archetypes/` (13 ISOs each) for test infra scaffolds |
| P07 | `tpl_unit_eval.md`, `tpl_smoke_eval.md`, `tpl_e2e_eval.md`, `tpl_golden_test.md`, `tpl_regression_check.md` |
| P09 | config templates for env/path/secret |
| `.claude/rules/` | `n05-operations.md`, `ascii-code-rule.md`, `shared-file-proposal.md`, `8f-reasoning.md` |

### 6.3 Change coordination

Current mechanism: `shared-file-proposal.md` rule -- write `.proposal.md`
under `.cex/runtime/proposals/`, N07 merges post-wave. **Status:** rule
documented, `cex_mission_runner.py` is supposed to create the dir per
wave (per the rule), but no `applied/` or `conflicts/` subdir exists in
`.cex/runtime/proposals/` because the dir itself is currently absent.

**Action:** create `.cex/runtime/proposals/{,applied,conflicts}/` scaffold
and add a smoke test that exercises the proposal-merge path.

### 6.4 Blast radius

Any breaking change to these tools will cascade:

| Tool | Breaks if wrong |
|---|---|
| `cex_compile.py` | all nuclei (universal compilation step) |
| `cex_doctor.py` | N07 orchestration loop (doctor runs between waves) |
| `cex_retriever.py` | N01 research, N04 RAG, F3 INJECT across all builders |
| `_spawn/dispatch.sh` | N07 grid dispatch (all 6 nuclei at once) |
| `cex_hooks.py` | every commit everywhere (when it's installed) |

These 5 files are the load-bearing walls. They need:

1. A dedicated `golden_test` for each (currently: 0).
2. A `regression_check` artifact (currently: `regression_check_operations.md`
   is the only one and it's generic).
3. CI job that runs each in isolation, not just the big `system_test`.

## Summary (for N07)

| Signal | Value |
|---|---|
| Ops layer stability | yellow (doctor 123/123, ASCII 138/138, system_test **47/58 = 81%**) |
| Ops layer coverage | **yellow** (0 unit/e2e/golden tests, 0 deploy configs, no learning_records dir) |
| Ops layer integrity | **red** (boot scripts: all 6 fail system_test and carry dead-code bug) |
| Tool-table doc drift | **yellow** (CLAUDE.md: 59, reality: 94) |
| Highest-leverage fix | `cex_hardcoded_path_lint.py` + fix `$args` bug in `boot/n0X.ps1` |
| Highest-leverage new tool | `cex_tool_doctor.py` (94 tools, 5 spot-checked is not enough) |

End of report.
