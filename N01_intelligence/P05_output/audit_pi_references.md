---
id: audit_pi_references
kind: knowledge_card
pillar: P01
title: "PI Reference Audit -- Full Codebase Sweep"
version: 1.0.0
quality: 8.9
created: 2026-04-08
mission: PICLEANUP
nucleus: n01
tags: [audit, pi, cleanup, migration, claude-code]
tldr: "30 source files contain stale PI references. 4 critical, 5 high, 9 medium, 12 low. Action required for N04 cleanup."
---

# PI Reference Audit -- Full Codebase Sweep

## Executive Summary

| Metric | Count |
|--------|-------|
| **Total source files with PI refs** | 30 |
| **CRITICAL** (LLM-loaded) | 4 |
| **HIGH** (user-facing docs) | 5 |
| **MEDIUM** (specs/plans) | 9 |
| **LOW** (archive/compiled/package) | 12 |
| **False positives filtered** | 80+ ("API client", "/login", "wrapper" in non-PI context) |

**Context**: CEX pivoted from PI wrapper to Claude Code native on 2026-04-08.
Anthropic blocks third-party app subscriptions. PI as deployment wrapper is dead.
All references below are stale and actively misleading to LLMs loading this context.

## Search Patterns Used

| Pattern | Purpose |
|---------|---------|
| `pi run`, `pi --`, `pi --model`, `pi --continue` | PI CLI invocations |
| `@mariozechner/pi-coding-agent` | PI npm package import |
| `cex-pi-package`, `.pi/`, `pi CLI` | PI infrastructure |
| `pi coding agent`, `pi runtime` | PI as runtime references |
| `pi_package`, `pi-extension`, `pi theme`, `pi skill` | PI extension system |
| `pi compact`, `pi /handoff`, `pi natively` | PI-specific features |

## CRITICAL -- LLM-Loaded Files (fix FIRST)

These files are auto-loaded into nucleus context via rules/agent cards/tools.
Stale PI refs here cause nuclei to reference non-existent infrastructure.

| # | File | Line | PI Reference | Suggested Fix |
|---|------|------|--------------|---------------|
| 1 | `.claude/rules/n07-autonomous-lifecycle.md` | 110 | `# - node started at same time as pi (pi runtime)` | Replace with `# - node started at same time as claude (Claude Code runtime)` |
| 2 | `_tools/cex_intent.py` | 286 | `errors["CLI-Pi"] = "pi CLI not in PATH"` | Remove entire PI CLI check block; PI is no longer a valid provider |
| 3 | `_tools/cex_boot_gen.py` | 302 | `"""DEPRECATED: pi CLI is no longer supported. Use claude CLI instead."""` | Remove deprecated PI function entirely or update docstring |
| 4 | `.cex/system_test_results.json` | 257 | `"CLI-Pi: pi CLI not in PATH"` | Regenerate test results after fixing cex_intent.py (auto-fixes) |

## HIGH -- User-Facing Documentation

Users read these. Stale PI refs cause confusion about how to run CEX.

| # | File | Line(s) | PI Reference | Suggested Fix |
|---|------|---------|--------------|---------------|
| 5 | `_docs/ROADMAP.md` | 82-83 | `.pi/agents/*.md`, `.pi/extensions/subagent/` | Replace with `.claude/agents/`, `.claude/commands/` |
| 6 | `_docs/plans/plan_H2_COMPLETION_20260407.md` | 43, 44, 46 | "pi runtime" x3 | Replace with "Claude Code runtime" |
| 7 | `P01_knowledge/library/domain/meta/kc_cex_orchestration_architecture.md` | 46 | `N07 (pi CLI)` | Replace with `N07 (claude CLI)` |
| 8 | `P08_architecture/examples/ex_diagram_supervisor_grid.md` | 30 | `(pi runtime)` | Replace with `(Claude Code runtime)` |
| 9 | `P08_architecture/examples/ex_component_map_codexa_core.md` | 24 | `pi runtime, rules` | Replace with `Claude Code runtime, rules` |

## MEDIUM -- Specs and Plans (historical, less urgent)

These contain design-time context. PI refs here are misleading but not actively breaking.

| # | File | Line(s) | PI Reference | Suggested Fix |
|---|------|---------|--------------|---------------|
| 10 | `_docs/specs/spec_n07_bootstrap_context.md` | 72, 238, 239 | `cex-pi-package` x3, "Pi skills", "pi themes" | Full rewrite needed -- replace PI package refs with Claude Code equivalents |
| 11 | `_docs/specs/spec_infinite_bootstrap_loop.md` | 48, 65, 78, 80, 116, 124, 139-140, 213, 215, 218, 226, 275, 278, 281, 284, 378 | 16+ PI refs: `pi --continue`, `pi --model`, `.pi/agents/`, `pi compact()`, `pi /handoff`, `pi subagent extension` | HEAVIEST FILE -- needs full rewrite or archive. Entire architecture assumes PI |
| 12 | `N03_builder/P12_orchestration/spawn_config_builder.md` | 13, 54 | "pi CLI", `pi --model opus-4-6` | Replace with `claude CLI`, `claude --model opus-4-6` |
| 13 | `N04_knowledge/P12_orchestration/spawn_config_knowledge.md` | 31 | `pi --model opus-4-6` | Replace with `claude --model opus-4-6` |
| 14 | `_tmp_prose_audit.py` | 11 | `"cex-pi-package"` in skip filter | Remove cex-pi-package from skip list (or delete temp file) |
| 15 | `extensions/ollama-provider/index.ts` | 12 | `import type { ExtensionAPI } from "@mariozechner/pi-coding-agent"` | Archive entire extensions/ directory -- PI extension system is dead |
| 16 | `P01_knowledge/library/domain/compiled/kc_cex_orchestration_architecture.yaml` | 64 | `N07 (pi CLI)` | Auto-fixes when source .md (#7) is fixed and recompiled |
| 17 | `P08_architecture/compiled/ex_diagram_supervisor_grid.yaml` | 19 | `(pi runtime)` | Auto-fixes when source .md (#8) is fixed and recompiled |
| 18 | `P08_architecture/compiled/ex_component_map_codexa_core.yaml` | 18 | `pi runtime, rules` | Auto-fixes when source .md (#9) is fixed and recompiled |

## LOW -- Archive, Backup, Package Code

These are historical artifacts. Low priority but should be cleaned eventually.

| # | File | PI Reference | Suggested Fix |
|---|------|--------------|---------------|
| 19 | `boot/_backup_2026-04-02/n07.cmd` | `pi --model anthropic/claude-opus-4-6` | Archive directory -- backup of pre-pivot boot |
| 20 | `boot/_backup_2026-04-02/cex.cmd` | `pi --model anthropic/claude-opus-4-6` | Archive directory |
| 21 | `cex-pi-package/package.json` | `"pi-package"` keyword | Archive entire directory to `_archive/cex-pi-package/` |
| 22 | `cex-pi-package/extensions/cex-subagent/index.ts` | `@mariozechner/pi-coding-agent` import | Archive |
| 23 | `cex-pi-package/extensions/cex-subagent/agents.ts` | `.pi/agents/*.md` refs | Archive |
| 24 | `cex-pi-package/extensions/cex-nucleus-ui.ts` | `@mariozechner/pi-coding-agent` import | Archive |
| 25 | `.pi/extensions/subagent/index.ts` | PI agent scope refs, `@mariozechner` import | Delete `.pi/` directory entirely |
| 26 | `.pi/extensions/subagent/agents.ts` | `@mariozechner/pi-coding-agent` import | Delete `.pi/` directory |
| 27 | `_docs/compiled/spec_n07_bootstrap_context.yaml` | compiled PI refs | Auto-fixes when source is fixed |
| 28 | `_docs/compiled/spec_infinite_bootstrap_loop.yaml` | compiled PI refs (15+) | Auto-fixes when source is fixed |
| 29 | `N03_builder/compiled/spawn_config_builder.yaml` | compiled PI refs | Auto-fixes when source is fixed |
| 30 | `.cex/retriever_index.json` | Indexed PI references from above files | Regenerate index after cleanup |

## Directories to Archive or Delete

| Directory | Action | Reason |
|-----------|--------|--------|
| `cex-pi-package/` | Archive to `_archive/cex-pi-package/` | Dead PI package -- TypeScript extensions for PI runtime |
| `.pi/` | Delete | PI project config directory -- not used by Claude Code |
| `boot/_backup_2026-04-02/` | Delete or archive | Pre-pivot boot scripts with PI commands |
| `extensions/ollama-provider/` | Evaluate | Uses PI extension API import -- may need rewrite for Claude Code |

## Compiled Files (auto-fix strategy)

8 compiled YAML files contain PI references inherited from their source .md files.
These do NOT need manual editing. Fix the source, then recompile:

```bash
python _tools/cex_compile.py --all
```

This regenerates all compiled/ YAML from source .md, automatically removing PI refs.

## Comparison: Cleanup Approaches

| Approach | Effort | Risk | Coverage |
|----------|--------|------|----------|
| **Manual file-by-file** | High (30 files) | Low | 100% precise |
| **sed/replace script** | Low | Medium (false positives) | 90% |
| **Fix source + recompile** | Medium | Low | 100% for compiled files |
| **Archive dead dirs + fix source** | Recommended | Low | 100% |

**Recommended approach**: Archive 3 dead directories (12 LOW files eliminated),
fix 18 source files manually, recompile to fix 8 compiled files. Net: 18 manual edits.

## Priority Queue for N04

1. Fix 4 CRITICAL files (LLM-loaded -- immediate)
2. Fix 5 HIGH files (user-facing docs -- same day)
3. Archive `cex-pi-package/`, `.pi/`, `boot/_backup_2026-04-02/` (12 files gone)
4. Fix 6 remaining MEDIUM source files
5. Recompile: `python _tools/cex_compile.py --all`
6. Regenerate: `python _tools/cex_retriever.py` (rebuild index)
7. Regenerate: `python _tools/cex_system_test.py` (fresh test results)

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**
