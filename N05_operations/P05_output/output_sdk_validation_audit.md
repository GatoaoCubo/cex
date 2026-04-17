---
id: output_sdk_validation_audit
name: SDK Validation Ops Audit
kind: output
pillar: P10_output
domain: operations
nucleus: N05
mission: SDK_VALIDATION
created: 2026-04-06
quality: 9.0
density_score: 1.0
---

# N05 Operations — SDK Validation Audit Report

**Date**: 2026-04-06
**Mission**: SDK_VALIDATION
**Model**: claude-opus-4-6 (1M context)

---

## T1. Dependencies Check — PASS

All dependencies resolve. Only 2 core deps required:
- `pyyaml>=6.0` — installed (6.0.3)
- `tiktoken>=0.7.0` — installed (0.12.0)

No missing packages. Transitive deps (regex, requests, etc.) all satisfied.

**Note**: pip 25.3 → 26.0.1 upgrade available (non-blocking).

---

## T2. CI Workflow Audit — PASS (1 BUG FIXED)

### ci.yml (6 jobs) — CORRECT
| Job | Does | Status |
|-----|------|--------|
| lint | Ruff check _tools/*.py | OK |
| test | pytest with coverage | OK |
| compile | cex_compile.py --all | OK |
| doctor | cex_doctor.py | OK |
| flywheel | cex_flywheel_audit.py audit | OK |
| system-test | cex_system_test.py --quick | OK |

Pipeline: lint → test + compile → doctor + flywheel → system-test. Correct DAG.
No obsolete model references (CI has no LLM calls — CEX_USE_API=0).

### quality.yml (2 jobs) — BUG FIXED

**Bug found**: `paths` referenced wrong directory names:
- `N05_code/**` → fixed to `N05_operations/**`
- `N06_brand/**` → fixed to `N06_commercial/**`

**Impact**: Quality workflow was NOT triggering on N05/N06 changes to main.
**Fix applied**: Updated paths to match actual directory names.

Jobs: quality-check → release-gate. Correct.

---

## T3. Boot Scripts Audit — PASS

All primary boot scripts (n01-n07.cmd) use `claude-opus-4-6`:

| Script | CLI | Model | Status |
|--------|-----|-------|--------|
| n01.cmd | claude | claude-opus-4-6 | OK |
| n02.cmd | claude | claude-opus-4-6 | OK |
| n03.cmd | claude | claude-opus-4-6 | OK |
| n04.cmd | claude | claude-opus-4-6 | OK |
| n05.cmd | claude | claude-opus-4-6 | OK |
| n06.cmd | claude | claude-opus-4-6 | OK |
| n07.cmd | pi | claude-opus-4-6 | OK |

Fallback scripts correctly use alternate providers:
- n01-gemini.cmd → gemini-2.5-pro
- n04-gemini.cmd → gemini-2.5-pro
- n05-codex.cmd → codex/o4-mini
- n07-ollama.cmd → ollama/qwen3:32b

All consistent with nucleus_models.yaml config.

---

## T4. Spawn Pipeline Check — PASS

### spawn_solo.ps1 (v4.0)
- Reads CLI from `.cex/config/nucleus_models.yaml` — confirmed (line 33-45)
- Writes handoff with decision manifest pointer — confirmed (line 50-83)
- Always boots interactive (no CLI arg task) — confirmed (line 91)
- PID tracking to spawn_pids.txt — confirmed (line 106)
- Grid positioning for 6 windows — confirmed

### spawn_grid.ps1 (v1.0)
- Handoff discovery: `${mission}_*.md` pattern — confirmed (line 41)
- Nucleus extraction: last segment of filename — confirmed (line 59-63)
- Static mode (all at once) + Continuous mode (slot-based) — confirmed
- Signal-based completion detection — confirmed (line 143-148)
- Stuck detection at 90min threshold — confirmed (line 154)

### dispatch.sh
- Agent spawn pre-flight: `cex_agent_spawn.py --validate` — confirmed (line 15-19)
- Routes to spawn_solo/grid/monitor/stop — confirmed
- All PowerShell calls use -NoProfile -ExecutionPolicy Bypass — confirmed

---

## T5. Environment Audit — PASS

`.env.example` present with all required keys:
- `ANTHROPIC_API_KEY` — present
- `OPENAI_API_KEY` — present
- No obsolete vars (CODEX_* removed)
- Provider keys organized by nucleus domain

---

## T6. Git Health — PASS

Working tree clean except expected items:
- `M CLAUDE_GENERATED.md` — tracked, modified (expected)
- `?? N04_knowledge/P05_output/output_content_factory_internal_audit.md` — new untracked (expected from N04 run)

Recent commits show healthy progression:
1. `dd5fc47` — opus-4-6 upgrade (config-driven)
2. `a2e44e2` — N06 Content Factory BIZ model
3. `9bcc7e6` — release-gate: 466/466 tests PASS
4. `fb4d64b` — quality log update
5. `963bfbf` — doctor 107 PASS

---

## T7. Estrutura Fractal N05 — PASS

48 files across proper fractal structure:
- `agents/` — agent_operations.md
- `architecture/` — agent_card_operations.md
- `compiled/` — 16 .yaml files (all compiled)
- `feedback/` — quality_gate_operations.md
- `knowledge/` — 8 KCs (railway, postgresql, deploy patterns)
- `memory/` — checkpoint_operations.md
- `orchestration/` — spawn_config + workflow + dispatch_rule
- `output/` — deploy checklist, health endpoint, railway toml, etc.
- `prompts/` — system_prompt_operations.md
- `schemas/` — 6 contracts (API response, env, health, middleware, railway, startup)

Real domain-specific content throughout — no placeholders detected.

---

## T8. Model Upgrade Verification — PASS

All nuclei confirmed on opus-4-6:

| Nucleus | CLI | Model | Fallback |
|---------|-----|-------|----------|
| N07 | pi | anthropic/claude-opus-4-6 | ollama/qwen3:32b |
| N01 | claude | claude-opus-4-6 | gemini/gemini-2.5-pro |
| N02 | claude | claude-opus-4-6 | gemini/gemini-2.5-pro |
| N03 | claude | claude-opus-4-6 | gemini/gemini-2.5-pro |
| N04 | claude | claude-opus-4-6 | gemini/gemini-2.5-pro |
| N05 | claude | claude-opus-4-6 | gemini/gemini-2.5-pro |
| N06 | claude | claude-opus-4-6 | gemini/gemini-2.5-pro |

Generated by `cex_boot_gen.py` from `.cex/config/nucleus_models.yaml`.

---

## Summary

| Task | Status | Issues |
|------|--------|--------|
| T1 Dependencies | PASS | pip upgrade available (cosmetic) |
| T2 CI Workflows | PASS | **BUG FIXED**: quality.yml wrong paths (N05_code→N05_operations, N06_brand→N06_commercial) |
| T3 Boot Scripts | PASS | All opus-4-6 |
| T4 Spawn Pipeline | PASS | Config-driven, interactive boot |
| T5 Environment | PASS | .env.example current |
| T6 Git Health | PASS | Clean tree |
| T7 N05 Structure | PASS | 48 files, real content |
| T8 Model Upgrade | PASS | All opus-4-6 confirmed |

**Critical fix**: quality.yml path references corrected — N05/N06 changes were silently ignored by CI.

**Overall**: 8/8 PASS. Infrastructure healthy. 1 bug fixed.
