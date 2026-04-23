---
id: cex_doctor_command
kind: instruction
pillar: P08
description: "CEX repo health check (separate from Claude Code's native /doctor). Tiered: fast | full | audit <name>"
quality: 9.0
title: "/cex-doctor"
version: "2.0.0"
author: n07_orchestrator
tags: [health, audit, doctor, atemporal]
tldr: "Tiered health check: fast (<30s core), full (~2min everything), audit <name> (specific tool)."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-16"
density_score: 0.92
supersedes: doctor
related:
  - doctor
  - skill
  - p11_qg_admin_orchestration
  - spec_token_budget_optimization
  - type_hint_retrofit_w5_20260415_2140
  - validate
  - bld_tools_consolidation_policy
  - p04_output_github_actions
  - bld_tools_model_architecture
  - type_hint_retrofit_w7_w7_report
---

# /cex-doctor — CEX Repo Health (atemporal)

> **`/doctor` belongs to Anthropic** (Claude Code internal diagnostics: MCP, settings, auth, runtime).
> **`/cex-doctor` is ours** (this repo's health: builders, hooks, compile, flywheel, audits).
> Use both. They check different layers.

## Usage

| Invocation | What runs | Time |
|------------|-----------|------|
| `/cex-doctor` | Tier 1 core (4 tools) | ~30s |
| `/cex-doctor --full` | Tier 1 + Tier 2 deep audit | ~2min |
| `/cex-doctor --audit <name>` | Single specific audit | varies |
| `/cex-doctor --list` | List every available audit | instant |

## Tier 1 -- Core (always run)

Run sequentially. Fail-fast on errors (warnings continue).

```bash
python _tools/cex_doctor.py             # builder health (PASS/WARN/FAIL per builder)
python _tools/cex_hooks.py validate-all # frontmatter + naming + density per artifact
python _tools/cex_compile.py --all      # md -> yaml compilation, must be 100%
python _tools/cex_stats.py              # auto-counter (kinds, builders, ISOs, KCs, tools)
```

Report format:
```
Doctor   -- N builders: X PASS / Y WARN / Z FAIL · D files · density A
Validate -- N artifacts: X clean / Y warnings / Z errors
Compile  -- X/Y compiled
Stats    -- {builders, isos, kinds, knowledge_cards, sub_agents, cli_tools, pillars, nuclei}
```

Verdict: green if 0 FAIL + 0 errors + 100% compile.

## Tier 2 -- Deep Audit (`--full` flag)

Adds these to Tier 1:

```bash
python _tools/cex_flywheel_audit.py audit  # 109 doc-vs-practice wires
python _tools/cex_feedback.py              # quality + density distribution per pillar
python _tools/cex_release_check.py         # public release readiness gate
```

Report adds:
```
Flywheel -- 109 wires: X WIRED / Y BROKEN
Feedback -- N artifacts · avg quality Q · M without score · K below density floor
Release  -- ready: yes/no · blockers: [list]
```

## Tier 3 -- Specific Audits (`--audit <name>` flag)

| name | tool | when to use |
|------|------|-------------|
| `security` | `_tools/audit_security_brand.py` | before public push, after secret rotation |
| `dead_code` | `_tools/audit_dead_code.py` | quarterly cleanup |
| `duplicates` | `_tools/audit_duplicates.py` | quarterly cleanup |
| `inventory` | `_tools/audit_inventory.py` | architecture review |
| `quality_dist` | `_tools/audit_quality_distribution.py` | post-cycle quality check |
| `cross_platform` | `_tools/audit_cross_platform.py` | after touching boot scripts |
| `docs_ux` | `_tools/audit_docs_ux.py` | docs revamp |
| `test_ci` | `_tools/audit_test_ci.py` | CI debugging |
| `codex_review` | `_tools/audit_codex_review.py` | codex-runtime validation |
| `brand` | `_tools/brand_audit.py` | brand consistency (6 dimensions) |
| `brand_validate` | `_tools/brand_validate.py` | brand_config schema check |
| `quota` | `_tools/cex_quota_check.py --all --cache` | pre-grid pre-flight |
| `flywheel` | `_tools/cex_flywheel_audit.py audit` | wire integrity |
| `release` | `_tools/cex_release_check.py` | release gate |

## Atemporal Discovery

This list is hand-maintained on purpose -- adding a new audit means:
1. Drop `audit_<name>.py` (or `cex_<feature>_check.py`) under `_tools/`
2. Append a row to the **Tier 3** table above
3. Optionally promote to Tier 1/2 if it's universal

Auto-discovery rule (run from a fresh agent): list every `_tools/audit_*.py`, `_tools/*_audit.py`, `_tools/*_check.py`, `_tools/*_validate*.py`, `_tools/cex_*health*.py`. Anything not in the Tier 3 table is **either new (add it) or deprecated (remove it)**.

## Verdict semantics

| Verdict | Means |
|---------|-------|
| **GREEN** | 0 FAIL, 0 errors, 100% compile, no Tier 2 BROKEN wire |
| **YELLOW** | warnings only -- mission can proceed, schedule cleanup wave |
| **RED** | any FAIL or error -- block dispatch, fix first |

## When to run

| Trigger | Tier |
|---------|------|
| Before any `/mission` or `/grid` | Tier 1 (fast pre-flight) |
| After consolidation of any wave | Tier 1 |
| Daily cron / start of work session | Tier 1 |
| Before public push / release | `--full` + `--audit security` + `--audit release` |
| Quarterly | `--full` + `--audit dead_code --audit duplicates --audit inventory` |
| After touching boots/CI/MCP | `--audit cross_platform --audit test_ci` |

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P08 architecture |
| Domain | CEX system health |
| Pipeline | Tier 1 always; Tier 2/3 on flag |
| Quality target | 9.0+ |
| Density target | 0.85+ |
| Coexists with | `/doctor` (Anthropic native, untouched) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[doctor]] | sibling | 0.39 |
| [[skill]] | sibling | 0.34 |
| [[p11_qg_admin_orchestration]] | downstream | 0.31 |
| [[spec_token_budget_optimization]] | upstream | 0.31 |
| [[type_hint_retrofit_w5_20260415_2140]] | upstream | 0.29 |
| [[validate]] | sibling | 0.29 |
| [[bld_tools_consolidation_policy]] | upstream | 0.28 |
| [[p04_output_github_actions]] | upstream | 0.27 |
| [[bld_tools_model_architecture]] | upstream | 0.27 |
| [[type_hint_retrofit_w7_w7_report]] | related | 0.27 |
