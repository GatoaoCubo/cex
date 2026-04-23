---
id: system_health_20260413
kind: knowledge_card
pillar: P07
title: CEX system health sweep 2026-04-13
version: 1.0.0
quality: 8.8
tags: [health, diagnostics, system-test, gen-v2-hardening]
related:
  - polish_fixes_20260413
  - wave2_quality_report
  - self_audit_newpc
  - self_audit_newpc_2026_04_12
  - bld_examples_builder
  - w5_n05_final_report
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_config_kind
---

# System Health -- 2026-04-13

## TL;DR

| Tool | Status | Critical Issues | Action |
|------|--------|----------------|--------|
| cex_doctor.py | WARN | 2 FAIL, 25 WARN | Fix action-paradigm density + complete agent-computer-interface ISOs |
| cex_hooks.py | N/A | No staged files | N/A (hooks fine, 28 errors from validate-all on unclean repo) |
| cex_system_test.py | FAIL | 7/58 fail | See per-tool below; git:clean + runner timeout are main blockers |
| cex_flywheel_audit.py | WARN | 2/109 BROKEN (98%) | N03_builder missing 'output' subdir; agent-computer-interface ISOs incomplete |
| cex_sanitize.py | PASS | 0 non-ASCII | Clean -- 159 files scanned |
| cex_setup_validator.py | WARN | 5 FAIL, 8 INFO | 4 MCP packages unresolvable; GITHUB_TOKEN not set |
| cex_release_check.py | FAIL | 5 FAIL, 23 PASS | README kind/builder counts stale; doctor/hooks/flywheel gates fail |
| cex_quota_check.py | WARN | gemini+codex missing | Only claude + ollama available on PATH |

## Per-Tool Findings

### cex_doctor (builder health)

- Total builders: 161
- Files present: 2086 / 2093 expected (7 missing from agent-computer-interface-builder)
- Avg density: 0.93
- Oversized files: 13 (>6144B standard, >8192B instructions)
- Result: **134 PASS | 25 WARN | 2 FAIL**

**FAIL: action-paradigm-builder** -- 3 ISOs below density floor (min 0.78):
  - bld_examples_action_paradigm.md = 0.76
  - bld_memory_action_paradigm.md = 0.76
  - bld_output_template_action_paradigm.md = 0.75

**FAIL: agent-computer-interface-builder** -- 7 ISOs missing (only 6/13 present):
  - Missing: bld_architecture, bld_collaboration, bld_config, + 4 others

**WARN (25 builders)** -- density/size violations; representative sample:
  - bias-audit-builder: examples=0.75, output_template=0.73, KC=8286B
  - edit-format-builder: density issues on multiple ISOs
  - effort-profile-builder: density violations
  - voice-pipeline-builder: examples=0.75, memory=0.76, tools=0.75; output_template=6712B
  - transport-config-builder: KC=9215B (oversized)
  - streaming-config-builder, thinking-config-builder: multi-ISO density below floor
  - repo-map-builder: KC density=0.78 (borderline), output_template oversized
  - safety-policy-builder: examples=0.75, KC=7480B

### cex_system_test (58 tests)

- Passed: **51/58**
- Failed: **7**

| # | Test | Error |
|---|------|-------|
| 1 | doctor:zero_warn | 25 WARN in doctor output |
| 2 | doctor:zero_fail | 2 FAIL in doctor output |
| 3 | builders:13_isos | agent-computer-interface-builder has only 6/13 ISOs |
| 4 | hooks:validate_all | 28 validation errors (staged artifacts have lint issues) |
| 5 | runner:execute_pass | cex_8f_runner.py timed out after 120s during execute mode |
| 6 | e2e:runs | cex_e2e_test.py exited -1 |
| 7 | git:clean | 136 dirty files (126 untracked + 8 modified) |

- Elapsed: 311.2s (runner timeout accounts for most of this)
- KC library: 181/98 kinds covered (exceeds minimum)

### cex_flywheel_audit (109 checks)

- WIRED: **107** (documented AND working)
- BROKEN: **2**
- PHANTOM: 0
- ORPHAN: 0
- Health: **98%**

**BROKEN #1**: `L2/N03_builder/structure`
  - N03_engineering/ has 10 subdirs; missing: `output`
  - Fix: `mkdir N03_engineering/output`

**BROKEN #2**: `L3/agent-computer-interface-builder/ISOs`
  - Only 6/13 ISOs present
  - Fix: dispatch N03 to complete remaining 7 ISOs

All 7 WIRE checks PASS. All 7 CASCADE checks PASS.

### cex_sanitize (ASCII compliance)

- Scoped: `_tools/` (159 .py files)
- Clean: **159/159**
- Dirty: 0
- Issues: **0 non-ASCII chars**
- Result: PASS -- full ASCII compliance in all executable code

### cex_setup_validator

- Total: **62/75 PASS | 5 FAIL | 8 INFO**

**FAIL: MCP packages (4)** -- npm cannot resolve:
  - N01: `markitdown-mcp`
  - N03: `@anthropic-ai/sdk-mcp-fetch`
  - N06: `markitdown-mcp`
  - N06: `mcp-server-hotmart`

**FAIL: ENV_VARS** -- GITHUB_TOKEN not set (needed by N03, N05)

**INFO** -- could not parse sleep setting (minor config gap)

**PASS highlights**: Ollama responding (port 11434), 5 models pulled
(gemma4:26b, cex-n01:latest, cex-n03:latest, qwen3:14b, qwen3:8b),
RTX 5070 Ti 16303MB GPU available, 1481.9GB free disk, git pre-commit hook installed

### cex_release_check (28 total)

- **5 FAIL / 23 PASS**

| # | Gate | Detail |
|---|------|--------|
| 1 | readme:kinds | README should mention 184 kinds (stale count) |
| 2 | readme:builders | README should mention 163 builders (stale count) |
| 3 | health:doctor_zero_fail | 2 FAILs in doctor |
| 4 | health:hooks_zero_errors | 28 hook errors |
| 5 | health:flywheel_100pct | 98% health (not 100%) |

Model freshness: PASS (no stale claude model IDs in codebase)
Security: PASS (no tracked secrets, .env ignored)
Version sync: PASS
Compilation: PASS (100% compile coverage)
CI/CD: PASS (workflow + quality gates in place)

### Compilation coverage

- Compile coverage: 100% (cex_release_check health:compile_100pct PASS)
- Untracked compiled YAMLs (new from GEN_V2 wave):
  - bld_architecture_edit_format.yaml
  - bld_architecture_prosody_config.yaml
  - bld_architecture_realtime_session.yaml
  - bld_architecture_repo_map.yaml
  - bld_architecture_sandbox_config.yaml
  - bld_architecture_stt_provider.yaml
  - bld_architecture_transport_config.yaml
  - bld_architecture_tts_provider.yaml
  - bld_output_template_agent_computer_interface.md (partial -- 1 file, missing 7 ISOs)

## Process Inventory

- cex_quota_check probe: claude=healthy (4493ms), ollama=healthy (345ms)
- gemini: binary not on PATH
- codex: binary not on PATH
- No orphan Python processes detected during sweep
- Background system_test ran 311s (dominated by 120s runner timeout + e2e)

## Git State

- Modified (staged or unstaged): 8 files (n01-n06 task.md files + 2 compiled YAMLs)
- Untracked: 126 files (new compiled YAMLs, wave validator, audit JSONs, new ISOs)
- Commits in last 24h: **819**
- Last commit: `[N04] GEN_V2: Wave 2 empirical quality report`
- Branch: main

## Recommendations

### Block Wave 3?

**NO BLOCK** -- system is functional at 98% flywheel health. Proceed with caveats:

1. **Do NOT block Wave 3** -- core pipeline (8F, compilation, routing, memory) fully WIRED
2. **Pre-Wave 3 fixes (N03)**: complete agent-computer-interface-builder (7 missing ISOs)
   - Takes ~10 min; unblocks flywheel to 100%
3. **Pre-Wave 3 fix (N03)**: `mkdir N03_engineering/output` -- one command
4. **Pre-Wave 3 fix (N05)**: set GITHUB_TOKEN in environment (needed for N03/N05 GitHub tools)

### Action matrix

| Priority | Issue | Owner | Fix |
|----------|-------|-------|-----|
| P1 | agent-computer-interface-builder: 7 missing ISOs | N03 | Dispatch to complete builder |
| P1 | N03_engineering/output subdir missing | N05 | `mkdir N03_engineering/output` |
| P2 | action-paradigm-builder: 3 ISOs below density | N03 | Rebuild 3 ISOs to density >= 0.78 |
| P2 | GITHUB_TOKEN not set | User | Set env var before next dispatch |
| P3 | README kind/builder counts stale (184/163) | N05 | Update CLAUDE.md + README counts |
| P3 | 25 WARN builders (density/size) | N03 | Batch density improvement pass |
| P4 | runner:execute_pass timeout | N05 | Investigate cex_8f_runner timeout threshold |
| P4 | MCP packages unresolvable (4) | N05 | Verify package names / npm registry |
| P5 | git:clean (136 dirty files) | N07 | Commit wave outputs before next test |

### Wave 3 go/no-go

- 8F pipeline: WIRED (PASS)
- Compilation: 100% (PASS)
- ASCII compliance: PASS
- Quota: claude + ollama available (gemini/codex not on PATH -- no blocker if routing skips them)
- **VERDICT: GO for Wave 3 with P1 fixes applied first**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[polish_fixes_20260413]] | sibling | 0.47 |
| [[wave2_quality_report]] | sibling | 0.42 |
| [[self_audit_newpc]] | upstream | 0.41 |
| [[self_audit_newpc_2026_04_12]] | upstream | 0.35 |
| [[bld_examples_builder]] | upstream | 0.33 |
| [[w5_n05_final_report]] | downstream | 0.30 |
| [[bld_architecture_kind]] | downstream | 0.30 |
| [[kind-builder]] | downstream | 0.28 |
| [[bld_collaboration_kind]] | downstream | 0.28 |
| [[bld_config_kind]] | downstream | 0.26 |
