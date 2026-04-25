---
quality: 8.7
quality: 8.0
id: p01_ch_cex_v1
kind: changelog
8f: F8_collaborate
pillar: P01
title: "CEX Changelog"
version: "1.0.0"
release_date: "2026-04-19"
author: N04_knowledge
domain: "cex platform"
tags: [changelog, cex, releases, history]
tldr: "CEX changelog covering the 20 most recent commits: HERMES assimilation, SDK coverage, multi-runtime grid, open source prep."
related:
  - p01_kc_cex_project_overview
  - p01_ctx_cex_project
  - dispatch
  - p01_kc_orchestration_best_practices
  - p08_ac_orchestrator
  - roadmap_cex
  - p01_kc_cex_orchestration_architecture
  - spec_cex_system_map
  - spec_infinite_bootstrap_loop
  - n03_readme_technical
density_score: 1.0
---

## [Unreleased]

- Open source global launch preparation (EN-only docs, brand cleanup, README accuracy)

---

## [1.0.0] - 2026-04-19

### Added

- **Path 4 Vertical Nucleus** in CONTRIBUTING.md -- framework for domain-specialized nuclei (N08+) with 5-file minimum viable spec and assimilation review checklist
- **3 intermediate good-first-issues** added to CONTRIBUTING.md: N08_healthcare, N09_fintech, N10_edtech

### Changed

- CONTRIBUTING.md rewritten from scratch with 4 contribution paths (builders, knowledge cards, SDK providers, vertical nuclei)

---

## [0.9.0] - 2026-04-18

### Added

- **HERMES assimilation** (tag `hermes_assimilated_20260418`): 9 new kinds registered, 6 artifact enrichments, 54 cross-runtime mirrors, 6 runtime tools
- **Nucleus interconnection map**: Mermaid diagrams (topology + 8F flow + pillar ownership) across all 8 nuclei
- **Per-nucleus tables** and master `crew_template` (8 nuclei) for the interconnection map
- **GitHub issue templates**: New Builder and Bug Report templates in `.github/`
- **Skill autocreator fix**: deleted 15 junk autocreated skills, repaired skill_autocreator pipeline

### Changed

- All nuclei now use `claude opus-4-6 1M` (budget-optimized: 2 Opus + 5 Sonnet -> all Opus per user directive)

---

## [0.8.0] - 2026-04-18

### Added

- **cex_sdk agent layer**: `CEXAgent` class, `context_loader`, `signal_emitter`, `f8_pipeline` module in `cex_sdk/`
- **SDK chat() API** + barrel exports + `pip install` support
- **FULL_COVERAGE W4b**: cex_sdk schema (P06) -- 12/12 CEX pillars now covered by SDK modules
- **FULL_COVERAGE W5**: tool-to-kind registry 293/293 (100%) via pillar supplement
- **FULL_COVERAGE W4**: cex_sdk 14/14 pillars -- output (P05), architecture (P08), config (P09) modules added
- **FULL_COVERAGE W2**: component_maps for 7/7 nuclei complete (N04/N05/N06/N07 added, avg quality 8.7)
- **FULL_COVERAGE W3**: structural scores applied to 98 null artifacts (avg 7.8)

### Fixed

- SDK pillar count corrected to 11/12 (P06 Schema had no module; W4 added it)

---

## [0.7.0] - 2026-04-16

### Added

- **Showoff runtime fixes**: codex no `--model` flag, gemini flash-lite + gitignore bypass, boot_gen SELF_AUDIT hardcode, `--skip` flag for showoff script
- **Chrome CDP setup**: `boot/chrome_cdp.ps1` + Playwright MCP disabled by default
- **LiteLLM dispatch layer**: 7 boot wrappers + grid-litellm/solo-litellm dispatch modes + JSONL fine-tuning logging on every LLM call
- **Free grid proven**: Ollama-only SMOKE_GRID 6/6 clean, 0 crashes, FT data captured

### Fixed

- `$pid` reserved variable conflict in PowerShell spawn loops (renamed to `$procId`)
- Window title truncation: switched from `MainWindowTitle` to `Win32_Process.CommandLine` for nucleus wrapper identification

---

## [0.6.0] - 2026-04-15

### Added

- **Local model benchmark**: llama3.1:8b wins 5/7 nuclei; qwen3:14b wins N03+N04; gemma4 disqualified (CPU offload thrash)
- **FT base locked**: gemma2:9b sweeps 7/7 nucleus benchmark vs qwen3:14b + haiku
- **Agentic capability bench**: llama3.1:8b = agentic base (11.67/12 score)
- **Free tier routing truth**: 4-wave benchmark; pure ollama-llama wins 4/6; qwen hybrid fails 1/6
- **Rate limits atlas**: 32 Sonnet concurrent = 87.5% success; safe limit ~20; config in `rate_limits.yaml`
- **Hybrid routing architecture**: `cex_router_v2.py` picks Claude/Ollama per task signature

### Fixed

- Gemini kill target: `node.exe` (no `gemini.exe`); orphan cleanup updated
- `--no-autocommit` clarified for Codex: exits without git commit or signal; N07 now verifies and commits Gemini outputs

---

## [0.5.0] - 2026-04-14

### Added

- **Wave 3 + Wave 4 completion**: 300 kinds / 301 builders / 3647 ISOs produced in overnight grid run
- **LiteLLM proxy**: 6 gaps fixed (3.14/orjson, cp1252, stale Railway DB); end-to-end verified
- **Session-aware dispatch v4.0**: multiple N07 orchestrators can run simultaneously; `stop` kills only MY session's nuclei

### Changed

- Dispatch protocol updated: `stop --all` now explicit flag (dangerous); `stop` defaults to session-scoped kill

---

## [0.4.0] - 2026-04-13

### Added

- **BORIS_MERGE (21 items)**: native skills, slash commands, `isolation: worktree`, settings.json hooks, PostToolUse compile, PostCompact memory decay, SessionStart preflight, stop auto-signal, `.mcp.json` root consolidation
- **Composable Crew protocol (WAVE8)**: 5 primitives (crew_template, role_assignment, capability_registry, nucleus_def, team_charter); grid-of-crews composition
- **`cex_crew.py`**: list/show/run crew CLI
- **`--bare` startup**: skip KC index + memory load for fast boot
- **`/simplify`, `/loop`, `/schedule`, `/batch`** commands
- **`swarm N kind`** dispatch mode: N parallel builders in isolated worktrees

---

## [0.3.0] - 2026-04-12

### Added

- **Mega session**: 100+ commits, 300 kinds, Ollama+Aider grid, overnight loop
- **cex_sdk runtime**: 78 `.py` files, 4504 lines; providers, agents, memory, schema modules
- **4-runtime support**: Claude / Codex / Gemini / Ollama routing unified under `cex_router.py`
- **Quality monitor**: `cex_quality_monitor.py` -- snapshots + regression detection
- **Prompt cache**: `cex_prompt_cache.py` + `.cex/cache/` with 301 builders pre-compiled

---

## Migration Guide

### 0.8.x -> 1.0.0

No breaking changes. New builders are additive. If you have custom nucleus configs:
1. Verify `.cex/config/nucleus_models.yaml` has `fallback_chain:` for all nuclei
2. Run `python _tools/cex_doctor.py` -- must show 0 FAIL
3. Re-materialize sub-agents: `python _tools/cex_materialize.py`

### 0.7.x -> 0.8.0

SDK modules restructured. If importing directly from `cex_sdk/`:
1. Update imports to use barrel exports: `from cex_sdk import CEXAgent`
2. Run `pip install -e ".[dev]"` to pick up new dependencies

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_project_overview]] | related | 0.34 |
| [[p01_ctx_cex_project]] | related | 0.32 |
| [[dispatch]] | downstream | 0.31 |
| [[p01_kc_orchestration_best_practices]] | related | 0.30 |
| [[p08_ac_orchestrator]] | downstream | 0.30 |
| [[roadmap_cex]] | related | 0.29 |
| [[p01_kc_cex_orchestration_architecture]] | related | 0.29 |
| [[spec_cex_system_map]] | related | 0.28 |
| [[spec_infinite_bootstrap_loop]] | related | 0.28 |
| [[n03_readme_technical]] | downstream | 0.28 |
