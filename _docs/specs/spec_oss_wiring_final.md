---
id: spec_oss_wiring_final
kind: constraint_spec
pillar: P06
title: "OSS Wiring Final -- Close Every Gap Before Public Release"
version: 1.0.0
created: 2026-04-21
updated: 2026-04-21
author: n07_orchestrator
domain: open-source-readiness
quality: 8.5
quality_target: 9.0
status: SPEC
scope: cross-nucleus
depends_on:
  - spec_cexai_rebrand
tags: [oss, wiring, export, security, versioning, spec]
tldr: "12 actionable fixes across 3 waves to close every gap found by 4 parallel audit agents before CEXAI goes public."
density_score: null
related:
  - spec_cexai_rebrand
  - spec_exchange_protocol
  - contributor_guide_cex
---

# OSS Wiring Final -- Close Every Gap Before Public Release

## 1. THE PROBLEM

Four parallel audit agents scanned the entire CEXAI repo across 4 dimensions:
agent/skill wiring, runtime/toolchain, nucleus self-construction, and OSS safety.
Combined findings: **98% infrastructure wired, 12 gaps remaining**.

None are architectural. All are configuration, content, or safety fixes. This spec
closes them in 3 waves so the repo can go public with zero tech debt.

## 2. AUDIT RESULTS (SOURCE OF TRUTH)

### 2.1 What Is Wired (no action needed)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Pillar schemas | 12/12 | All `_schema.yaml` present, 1,922 lines total |
| Kind registry | 293 | `.cex/kinds_meta.json` fully populated |
| Builders | 295 | `archetypes/builders/` with 12 ISOs each |
| Kind KCs | 302 | `N00_genesis/P01_knowledge/library/kind/` |
| Compiled YAMLs | 4,696 | Across all nuclei |
| Boot scripts | 51 | 7 nuclei x 5 runtimes + support scripts |
| Dispatch infra | 16 subcommands | `_spawn/dispatch.sh` fully functional |
| Hooks | 4 types | PostToolUse, PostCompact, SessionStart, Stop |
| CI/CD | 3 workflows | ci.yml, quality.yml, claude_learn.yml |
| .gitignore | Proper | .env, runtime/, compiled/, credentials excluded |
| LICENSE | MIT | Properly referenced in README |
| Issue templates | 3 | bug_report, knowledge_card, new_builder |
| Obsidian vault | Complete | Homepage, Dataview, 7 plugins, canvas |
| Skills | 14 mirrored | `.cex/skills/` ↔ `.claude/skills/` |
| Commands | 21 | All reference existing tools |
| cex_sdk | 104 .py | 20 submodules, importable |
| _tools | 230 .py | All syntactically valid, 178 entry points |
| Nucleus defs | 8/8 | All `nucleus_def_n{XX}.md` present |
| Agent cards | 7/8 | N01-N07 (N00 is archetype, acceptable) |
| Nucleus directories | 8/8 | All 12 pillars in every nucleus |
| Non-ASCII code | 0 violations | Clean across all .py files |

### 2.2 What Needs Fixing (12 items)

| # | Gap | Severity | Wave | Owner |
|---|-----|----------|------|-------|
| G1 | SECURITY.md placeholder email `security@<your-domain>` | BLOCKER | W1 | N07 |
| G2 | CODE_OF_CONDUCT.md placeholder email `community@<your-domain>` | BLOCKER | W1 | N07 |
| G3 | Version mismatch: README+pyproject=10.2.0, CHANGELOG=10.3.0, tag=v10.4.0-cexai | BLOCKER | W1 | N07 |
| G4 | Export script misses `N*/P10_memory/` strip (80 instance files would leak) | BLOCKER | W1 | N07 |
| G5 | `brand_config.yaml` not in `.gitignore` (latent risk) | HIGH | W1 | N07 |
| G6 | Export script commit message hardcodes v10.3.0 | HIGH | W1 | N07 |
| G7 | N07 missing `kc_admin_vocabulary.md` (orchestration domain vocabulary) | MEDIUM | W2 | N07 |
| G8 | CHANGELOG missing v10.4.0-cexai entry for rebrand | MEDIUM | W2 | N07 |
| G9 | No PR template at `.github/pull_request_template.md` | MEDIUM | W2 | N07 |
| G10 | 292 stale handoff files in `.cex/runtime/handoffs/` | LOW | W2 | N07 |
| G11 | ~~`cex_hooks.py install` function not implemented~~ | ~~LOW~~ | -- | RESOLVED (already wired: `install_git_hook()` at line 816) |
| G12 | Export script needs P10_memory awareness in README "Next steps" | LOW | W2 | N07 |

### 2.3 Confirmed Non-Issues

| Suspected gap | Why it's not a gap |
|---------------|-------------------|
| `.cex/agents/` empty (0 vs 295 in `.claude/agents/`) | By design: `.claude/agents/` is Claude Code-specific; cross-runtime uses `archetypes/builders/` (301 builders) |
| N00 missing agent_card + component_map | N00 is archetype, not operational; has `kind_agent_card/` library instead |
| Quality self-scoring (87.5% of artifacts) | Scores assigned by peer nuclei during /showoff + /consolidate cycles, not self-scored; reset to null on export via import protocol |
| interfaces.py missing in cex_sdk | Interfaces distributed in module `__init__.py` files; functional |
| Encoding pragmas missing in _tools/ | Python 3 defaults to UTF-8; non-blocking |

## 3. EXECUTION PLAN

### Wave 1: OSS Blockers (6 fixes, N07 direct)

All fixes are simple edits. No nucleus dispatch needed.

| Action | Path | Change |
|--------|------|--------|
| EDIT | `SECURITY.md` | Replace `security@<your-domain>` with `security@gatoaocubo3.com` |
| EDIT | `CODE_OF_CONDUCT.md` | Replace `community@<your-domain>` with `community@gatoaocubo3.com` |
| EDIT | `README.md` | Update version badge from v10.2.0 to v10.4.0 |
| EDIT | `pyproject.toml` | Update version from 10.2.0 to 10.4.0 |
| EDIT | `_tools/cex_export_public.sh` | Add `rm -rf "$TARGET_DIR"/N0[1-7]_*/P10_memory/` + update commit version |
| EDIT | `.gitignore` | Add `.cex/brand/brand_config.yaml` pattern |

### Wave 2: Wiring Gaps (6 fixes, N07 direct + 1 agent)

| Action | Path | Change |
|--------|------|--------|
| CREATE | `N07_admin/P01_knowledge/kc_admin_vocabulary.md` | Orchestration domain controlled vocabulary |
| CREATE | `.github/pull_request_template.md` | Standard PR template with CEX conventions |
| EDIT | `CHANGELOG.md` | Add v10.4.0 entry (CEXAI rebrand + this wiring pass) |
| CLEAN | `.cex/runtime/handoffs/` | Archive 292 stale handoffs to `_done/` |
| EDIT | `_tools/cex_hooks.py` | Add stub `install()` function that prints setup instructions |
| EDIT | `_tools/cex_export_public.sh` | Add P10_memory note in "Next steps" output |

### Wave 3: Validate (compile + doctor + export check)

| Action | Tool | Expected |
|--------|------|----------|
| Compile changed files | `cex_compile.py` | 0 errors |
| Run doctor | `cex_doctor.py` | 0 FAIL |
| Verify export strip | Read export script logic | P10_memory covered |
| Version consistency check | grep v10.4.0 across files | All aligned |

## 4. ACCEPTANCE CRITERIA

- [ ] SECURITY.md has real email (not placeholder)
- [ ] CODE_OF_CONDUCT.md has real email (not placeholder)
- [ ] Version = 10.4.0 in README, pyproject.toml, CHANGELOG, export script
- [ ] Export script strips N*/P10_memory/ for N01-N07
- [ ] brand_config.yaml in .gitignore
- [ ] N07 has vocabulary KC
- [ ] CHANGELOG has v10.4.0 entry
- [ ] PR template exists
- [ ] Stale handoffs archived
- [ ] cex_hooks.py install prints instructions
- [ ] cex_doctor.py returns 0 FAIL
- [ ] All files compile

## 5. USER ACTION REQUIRED (CANNOT BE AUTOMATED)

| # | Action | Why N07 cannot do it |
|---|--------|---------------------|
| U1 | Rotate ALL API keys in `.env` before public push | Security: only the key owner can rotate |
| U2 | Confirm contact emails (security@ and community@) | Policy: domain ownership verification |
| U3 | Run `bash _tools/cex_export_public.sh` for final export | Destructive: creates clean repo |
| U4 | `gh repo create GatoaoCubo/cex --public` | Auth: requires GitHub token |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_cexai_rebrand]] | parent | -- |
| [[spec_exchange_protocol]] | sibling | -- |
| [[contributor_guide_cex]] | downstream | -- |
| [[kc_artificial_sins]] | sibling | -- |
