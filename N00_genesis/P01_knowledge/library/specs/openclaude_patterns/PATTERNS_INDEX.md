---
id: openclaude_patterns_index
kind: context_doc
pillar: P01
title: "OpenClaude Pattern Extraction — CEX Runtime Equivalents"
version: 1.0.0
created: 2026-04-06
author: n07_orchestrator
quality: 9.0
tags: [openclaude, patterns, extraction, runtime, provider, ux, agent]
density_score: 1.0
related:
  - bld_collaboration_model_provider
  - bld_collaboration_boot_config
  - model-provider-builder
  - p10_lr_boot-config-builder
  - bld_config_model_provider
  - p01_kc_model_provider
  - bld_memory_model_provider
  - boot-config-builder
  - p03_sp_model_provider_builder
  - p01_kc_boot_config
---

# OpenClaude → CEX Pattern Map

> Source: `openclaude-main.zip` (10.1MB, 795 source files, ~11K lines of patterns)
> Strategy: Extract patterns, implement natively in CEX. Zero OpenClaude dependency.

## Pattern Status

| # | OpenClaude Pattern | Source File | Lines | CEX Equivalent | Status |
|---|-------------------|-------------|-------|----------------|--------|
| P01 | Agent Color System | `agentColorManager.ts` | 67 | `cex_boot_gen.py` NUCLEUS_COLORS | DONE |
| P02 | Provider Profiles | `providerProfile.ts` | 698 | `nucleus_models.yaml` + `cex_router.py` | DONE |
| P03 | Provider Discovery | `providerDiscovery.ts` | 190 | `cex_router.py` ping check | PARTIAL |
| P04 | Provider Recommendation | `providerRecommendation.ts` | 318 | `nucleus_models.yaml` fallback chains | DONE |
| P05 | Model Options Registry | `modelOptions.ts` | 646 | `nucleus_models.yaml` + `cex_model_updater.py` | DONE |
| P06 | Theme System | `theme.ts` | 640 | Boot script PS1 colors | PARTIAL |
| P07 | Session Runner | `sessionRunner.ts` | 425 | `spawn_solo.ps1` + `spawn_grid.ps1` | DONE |
| P08 | Multi-Agent Spawn | `spawnMultiAgent.ts` | ~800 | `spawn_grid.ps1` + `cex_agent_spawn.py` | DONE |
| P09 | Provider Launch | `provider-launch.ts` | 200 | `cex_boot_gen.py` build_*_ps1() | DONE |
| P10 | Terminal Setup | `terminalSetup.tsx` | 2100 | Boot script PS1 UX (colors, sizing) | PARTIAL |
| P11 | Bridge UI | `bridgeUI.ts` | 460 | N/A (OpenClaude web bridge, not needed) | SKIP |
| P12 | Fullscreen Layout | `FullscreenLayout.tsx` | 2300 | N/A (React/Ink TUI, different stack) | SKIP |
| P13 | Session Storage | `sessionStorage.ts` | 5000 | `.cex/runtime/` file-based | DONE |
| P14 | MCP Client | `mcp/client.ts` | 3200 | `.mcp-n0X.json` + claude native MCP | DONE |
| P15 | Provider Shim (OpenAI) | `openaiShim.ts` | 1000 | `cex_router.py` provider routing | PARTIAL |
| P16 | Provider Shim (Codex) | `codexShim.ts` | 600 | Boot script codex fallback | DONE |

## What We Have That OpenClaude Doesn't

| CEX Feature | Description |
|-------------|-------------|
| 8F Pipeline | 8-step artifact creation (F1-F8) — no equivalent in OC |
| Builder ISOs | 13 structured files per kind — OC has no builder system |
| GDP Protocol | Guided decisions before dispatch — OC has no user decision gate |
| Knowledge Cards | 119 KCs with retrieval — OC has no knowledge layer |
| Flywheel Audit | 109-check doc-vs-practice — OC has no audit system |
| Session-aware Stop | Kill only YOUR nuclei — OC has basic process stop |
| Nucleus Fractal | 12-pillar structure per nucleus — OC is flat |

## What OpenClaude Has That We Should Extract

### Priority 1: DONE (already implemented)
- Agent colors per nucleus ✅
- Provider routing via config ✅
- Multi-provider fallback chains ✅
- Session tracking with PID files ✅
- PowerShell boot with UX ✅

### Priority 2: PARTIAL (needs completion)
- **P03 Provider Discovery**: Auto-detect which providers are available (ping API endpoints)
- **P06 Theme System**: Only colors done, missing dynamic theme switching
- **P10 Terminal Setup**: Basic sizing done, missing font config and profile generation
- **P15 Provider Shim**: Router selects provider but doesn't normalize API format

### Priority 3: SKIP (not needed for CEX)
- Bridge UI (web-based remote session — we use local terminals)
- Fullscreen Layout (React/Ink TUI — we use PowerShell native)
- Chrome extension integration
- OAuth flow (we use API keys directly)

## Architecture Decision

**We chose**: Extract patterns, implement natively.
**We rejected**: Depend on OpenClaude as runtime.
**Reason**: CEX has a richer architecture (8F, builders, GDP, KCs) that OpenClaude
can't replicate. OpenClaude adds multi-provider but we already solved that.
The UX patterns (colors, sizing, profiles) are simple enough to implement in PS1.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_provider]] | downstream | 0.35 |
| [[bld_collaboration_boot_config]] | downstream | 0.29 |
| [[model-provider-builder]] | downstream | 0.29 |
| [[p10_lr_boot-config-builder]] | downstream | 0.28 |
| [[bld_config_model_provider]] | downstream | 0.26 |
| [[p01_kc_model_provider]] | downstream | 0.26 |
| [[bld_memory_model_provider]] | downstream | 0.25 |
| [[boot-config-builder]] | downstream | 0.24 |
| [[p03_sp_model_provider_builder]] | downstream | 0.23 |
| [[p01_kc_boot_config]] | downstream | 0.23 |
