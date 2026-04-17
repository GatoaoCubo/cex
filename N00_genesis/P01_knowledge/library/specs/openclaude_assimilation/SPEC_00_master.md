---
id: spec_00_master
kind: spec
pillar: P01
title: "OpenClaude→CEX Assimilation Master Spec"
version: 1.0.0
status: active
created: 2026-04-05
quality: 9.0
dependencies: [SPEC_01, SPEC_02, SPEC_03, SPEC_04, SPEC_05, SPEC_06, SPEC_07]
---

# OpenClaude → CEX: Structural Assimilation Spec

## Provenance

**Source**: `openclaude-main` (Claude Code CLI open-source fork, 165K LoC TypeScript)
**Target**: `cex_sdk` (4.5K LoC Python) + `_spawn/` + `_tools/`
**Method**: Pattern harvesting — extract architectural patterns, rewrite in Python.
**NOT**: Code porting, npm dependency, TypeScript compilation.

## Architecture Map

| # | OpenClaude Module | Lines | CEX Target | Sub-Spec |
|---|-------------------|-------|------------|----------|
| 1 | `src/coordinator/` + coordinator prompts | ~600 | N07 orchestrator rules + cex_mission_runner.py | SPEC_01 |
| 2 | `src/P04_tools/AgentTool/` (fork/spawn/run) | ~2800 | _spawn/ + cex_crew_runner.py | SPEC_02 |
| 3 | `src/query/tokenBudget.ts` + BudgetTracker | ~100 | _tools/cex_token_budget.py | SPEC_03 |
| 4 | `src/memdir/` (scan/age/relevance/types) | ~900 | _tools/cex_memory_*.py | SPEC_04 |
| 5 | `src/skills/` (bundled/load/dynamic) | ~1200 | builder ISO runtime loader | SPEC_05 |
| 6 | `smart_router.py` + provider catalogue | ~300 | nucleus routing config | SPEC_06 |
| 7 | `src/tools/*/permissions*` + coordinator GDP | ~400 | GDP enforcement layer | SPEC_07 |

## Execution Plan

### Wave 1 — SPEC (this wave)
All 7 sub-specs produced in parallel. Each contains:
- Pattern extracted (pseudocode, not TS)
- Python adaptation design
- Files affected in CEX
- Acceptance criteria
- 8F impact analysis

### Wave 2 — IMPLEMENT
Sequential by dependency:
```
SPEC_03 (token budget)     ─┐
SPEC_04 (memory)           ─┤── Foundation (no deps)
SPEC_07 (GDP)              ─┘
SPEC_06 (routing)          ── Infra (needs SPEC_03)
SPEC_05 (skills/ISO)       ── Runtime (needs SPEC_04)
SPEC_02 (agent spawn)      ── Core (needs SPEC_05, SPEC_06)
SPEC_01 (coordinator)      ── Apex (needs all above)
```

## 8F Stress Points

| Function | Risk | Mitigation |
|----------|------|------------|
| F1 CONSTRAIN | New patterns may not map to existing 114 kinds | Create `integration` kind if needed |
| F2 BECOME | Builder ISOs don't exist for infra code | Use N05-builder (operations) |
| F3 INJECT | 165K LoC corpus is too large for context | Pre-filtered to ~5K relevant lines |
| F4 REASON | TypeScript→Python translation is lossy | Pattern-level, not line-level |
| F5 CALL | New tools may conflict with existing | Namespace: `cex_oc_*.py` prefix during dev |
| F6 PRODUCE | Integration code has no template | Fresh approach, density target relaxed to 0.75 |
| F7 GOVERN | Quality gates for infra differ from content | Custom gate: tests pass + backward compat |
| F8 COLLABORATE | Changes touch multiple pillars | Atomic commits per spec, not per file |

## Legal Note

OpenClaude derives from Anthropic's inadvertently exposed source.
CEX assimilates **architectural patterns** only — no code copying.
All implementations are original Python, referencing patterns by description.
