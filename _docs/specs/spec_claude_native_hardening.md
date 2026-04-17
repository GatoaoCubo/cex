---
id: spec_claude_native_hardening
kind: context_doc
title: "Mission CLAUDE_NATIVE: Harden CEX for Claude Code Runtime"
version: 1.0.0
quality: 9.0
created: 2026-04-08
mission: CLAUDE_NATIVE
waves: 3
nuclei: [n01, n02, n03, n04, n05, n06]
density_score: 0.93
---

# Mission: CLAUDE_NATIVE_HARDENING

## Goal

Harden CEX for Claude Code as sole runtime. Clean PI debt, fix grid UX,
integrate new Claude Code features, and have every nucleus self-audit
for missing tools and capabilities.

## Source Intel

- N01 audit: 30 files with PI refs (4 critical, 5 high, 9 medium, 12 low)
- N04 G6 cleanup: 5 docs updated (ARCHITECTURE, QUICKSTART, HIERARCHY, NAMING, PLAYBOOK)
- PI vs Claude Code gap analysis: 0 real gaps, 5 new features to integrate
- Grid test: MoveWindow timing issue on N04

## Wave 1 -- Infrastructure (N05 + N03)

Must complete before Wave 2. Fixes the runtime and tools other nuclei depend on.

### N05: Fix Grid UX + Boot Script Hardening
1. **MoveWindow timing fix**: `_spawn/spawn_grid.ps1` line 110 — 3s sleep
   may not be enough for PS1 boot to render window. Increase to 5s or add
   retry loop that polls `MainWindowHandle -ne 0`.
2. **Integrate `--name` flag**: All boot scripts (boot/n0X.ps1 + .cmd) should
   pass `--name "CEX-N0X-MISSION"` so sessions are trackable in `/resume`.
3. **Integrate `--fork-session`**: overnight.ps1 and overnight_infinite.cmd
   should use `--continue --fork-session` for safe context resumption.
4. **PID file format**: spawn_grid.ps1 line 114 writes `{pid} {nucleus}` but
   dispatch.sh stop expects `{pid} {nucleus} {cli} {session_id} {timestamp}`.
   Fix format to match expected schema.
5. **Validate**: Run `bash _spawn/dispatch.sh stop --dry-run` after fixes.
6. **Self-audit**: What native Claude Code tools/features should N05 have
   in its MCP config or settings that it currently lacks? Check:
   - GitHub MCP server (for CI/CD integration)
   - Any missing --flags that improve operations

### N03: Clean PI from Builders + Shared ISOs
1. **Spawn configs**: Fix `N03_builder/P12_orchestration/spawn_config_builder.md`
   and `N04_knowledge/P12_orchestration/spawn_config_knowledge.md` — replace
   `pi --model` with `claude --model`.
2. **Shared ISOs**: Scan `archetypes/builders/_shared/` for PI references.
3. **Agent definitions**: Scan `.claude/agents/` for any PI-specific patterns.
4. **Self-audit**: What native Claude Code capabilities should builders use
   that they currently don't? Check if `.claude/agents/*.md` reference the
   right sub-agent tools and capabilities.
5. **Compile all changed files**.

## Wave 2 -- Content Cleanup (N01 + N04 + N06) [parallel]

PI reference cleanup across all non-infrastructure files.

### N01: Clean PI from Specs + Create Missing KCs
1. **Critical specs**: Rewrite `spec_infinite_bootstrap_loop.md` for Claude
   Code reality (--continue, Agent tool, --fork-session instead of PI
   extensions). This is the biggest single file.
2. **Critical specs**: Fix `spec_n07_bootstrap_context.md` (lines 68,70,72)
   and `spec_context_assembly.md` (lines 53,55).
3. **Medium specs**: Fix remaining 9 medium-severity files from audit.
4. **Create KC**: `kc_claude_code_native_features.md` documenting all
   Claude Code features CEX uses (--name, --continue, --fork-session,
   --append-system-prompt, --agents, --mcp-config, Agent tool, etc).
5. **Self-audit**: What research tools/MCP servers should N01 have that
   it currently lacks? Check brave-search, firecrawl, web-fetch configs.

### N04: Clean PI from KCs + Update Remaining Docs
1. **KCs with PI refs**: Scan P01_knowledge/library/ for PI references.
   Fix: `kc_cex_orchestration_architecture.md` (line 46: "pi CLI").
2. **Remaining stale docs**: WHITEPAPER_CEX.md, FAQ.md, ONBOARDING.md,
   LLM_INSTRUCTIONS.md — these were identified as stale but not in G6 wave.
3. **Architecture examples**: Fix `ex_component_map_codexa_core.md` and
   `ex_diagram_supervisor_grid.md` (reference "pi runtime").
4. **Self-audit**: What knowledge management tools should N04 have?
   Check embedding configs, RAG sources, vector store integration status.

### N06: Clean PI from Commercial + Self-Audit Monetization
1. **Scan N06_commercial/** for any PI references (pricing, funnels that
   assume PI wrapper as distribution).
2. **Update monetization strategy**: If any content_monetization artifacts
   assume PI-based subscription model, update for Claude Code native
   distribution (git clone, template repo, consulting model).
3. **Self-audit**: What commercial tools/integrations should N06 have?
   Check: Stripe MCP, payment APIs, analytics. Are MCP configs current?

## Wave 3 -- Validation + Marketing (N02 + N05) [parallel]

### N05: Full System Validation
1. Run `python _tools/cex_doctor.py` — must be 123 PASS.
2. Run `python _tools/cex_flywheel_audit.py` — target 100%.
3. Run `python _tools/cex_system_test.py` — all tests pass.
4. Verify: all boot scripts work (`boot/n0X.cmd` and `boot/n0X.ps1`).
5. Verify: `setup.cmd` still passes on current state.
6. Report: consolidated validation results.

### N02: Update Marketing for Claude-Native
1. **Scan N02_marketing/** for PI references.
2. **Update brand voice artifacts**: If any copy/campaigns reference PI
   wrapper, app store, or subscription model — update for Claude Code.
3. **Self-audit**: What creative tools should N02 have? Check: Canva MCP,
   puppeteer for screenshots, social publishing APIs. Are configs current?
4. **Produce**: Updated elevator pitch for CEX as Claude Code native
   knowledge system (not a wrapper app).

## Decision Manifest Addendum

```yaml
mission: CLAUDE_NATIVE_20260408
decisions:
  pi_replacement: claude_code_native
  grid_layout: 3x2 (3 cols, 2 rows)
  boot_preference: ps1 (sin-aware) over cmd (legacy)
  new_features: [--name, --fork-session, --continue]
  overnight_pattern: --continue --fork-session
  self_audit: every_nucleus_must_report_missing_tools
  quality_floor: 9.0
```

## Success Criteria

| Check | Expected |
|-------|----------|
| PI references in CRITICAL files | 0 |
| PI references in HIGH files | 0 |
| Doctor | 123 PASS |
| Grid dispatch test (6 nuclei) | All position correctly |
| Boot scripts have --name flag | 6/6 |
| PID format matches stop parser | Yes |
| Each nucleus self-audit report | 6/6 delivered |
| spec_infinite_bootstrap_loop.md | Rewritten for Claude Code |
