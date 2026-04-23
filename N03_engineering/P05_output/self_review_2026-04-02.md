---
id: n03_self_review_20260402
kind: context_doc
nucleus: N03
pillar: P09
quality: 9.0
date: 2026-04-02
type: self-review
author: N03
mission: SELF_REVIEW
related:
  - n05_self_review_2026-04-02
  - bld_collaboration_kind
  - wave2_quality_report
  - p03_sp_n03_creation_nucleus
  - polish_fixes_20260413
  - bld_collaboration_builder
  - bld_config_kind
  - kind-builder
  - system_health_20260413
  - bld_architecture_kind
---

# N03 Self-Review — 2026-04-02

## Summary

| Metric | Value |
|--------|-------|
| Builders | 107 (49 PASS / 57 WARN / 1 FAIL) |
| Tests | 497 passed / 15 failed |
| SDK | 79 .py / 4,537 lines |
| _tools | 53 .py files |
| Oversized ISOs | 79 files across 57 builders |
| N03 artifacts | 80 .md + 40 compiled = 120 files |
| N03 avg quality | 8.98 / 10 |

---

## 1. CRITICAL Gaps (must fix)

### C1. `compiled` builder: 1 FAIL — not a real builder

`archetypes/builders/compiled/` contains 253 compiled YAML files (the output of `cex_compile.py`), NOT builder ISOs. Doctor expects 13 ISOs (manifest, instruction, system_prompt, etc.) but finds only `.yaml` artifacts.

**Root cause**: `compiled/` is a compilation output directory that was placed inside `archetypes/builders/` by accident or convention. It is NOT a builder.

**Fix**: Either (a) exclude `compiled/` from doctor's scan with a denylist, or (b) move compiled YAML files to a dedicated `archetypes/compiled/` directory outside `builders/`.

### C2. `score_artifact()` never returns below 7.0 — 3 test failures

`_tools/cex_score.py:594` — structural scoring formula:

```python
score = 8.0 + (raw / 10.0) * 1.3
score = round(min(score, 9.3), 1)
score = max(score, 7.0)
```

When `score_structural()` returns raw=0 (missing file, empty file, no frontmatter), the formula yields 8.0. The floor at `max(score, 7.0)` never activates because the base is already 8.0.

**Failing tests**:
- `test_score_missing_file`: expects 0.0, gets 8.0
- `test_score_no_frontmatter`: expects <8.0, gets 8.0
- `test_score_empty_file`: expects <7.0, gets 8.0

**Root cause**: `score_structural()` doesn't penalize for missing/empty/malformed files — it returns raw=0 as "unknown" instead of negative. The formula then inflates 0 to 8.0.

**Fix**: `score_artifact()` should check for file existence and frontmatter validity BEFORE applying the formula. Return 0.0 for missing files, apply penalty for no-frontmatter.

### C3. `skill-builder` incomplete — 12 test failures

All 12 `test_schema_evolution.py` failures trace to ONE builder: `skill-builder`. It is missing:

| Missing Field | ISO |
|---------------|-----|
| keywords | bld_manifest_skill.md |
| triggers | bld_manifest_skill.md |
| capabilities (3-layer) | bld_manifest_skill.md |
| memory_scope | bld_memory_skill.md |
| observation_types | bld_memory_skill.md |
| effort | bld_config_skill.md |
| max_turns | bld_config_skill.md |
| disallowed_tools | bld_config_skill.md |
| permission_scope | bld_config_skill.md |
| Tool Permissions section | bld_tools_skill.md |

**Root cause**: `skill-builder` was created but never updated to match the schema evolution requirements (runtime fields, memory taxonomy, capabilities layers, tool permissions). All other 106 builders pass these checks.

**Fix**: Hydrate `skill-builder` ISOs with the missing fields using `cex_schema_hydrate.py` or manual update.

### C4. Signal flow broken — signals/ directory always empty

`.cex/runtime/signals/` is created by `spawn_solo.ps1` but remains empty after dispatch. Signals are either:
- Never written (signal_writer.py called incorrectly), or
- Written then immediately archived to `.cex/runtime/archive/`

**Impact**: `spawn_grid.ps1` and `spawn_monitor.ps1` check `.cex/runtime/signals/` for completion detection. Empty directory = nuclei never appear "complete".

**Fix**: Trace the signal write path end-to-end. Verify signal_writer.py writes to `signals/` and archival only happens on consolidate.

### C5. PID path split between spawn scripts

| Script | PID File Path |
|--------|---------------|
| spawn_solo.ps1 | `.cex/runtime/pids/spawn_pids.txt` |
| spawn_grid.ps1 | `.cex/temp/spawn_pids.txt` |
| spawn_monitor.ps1 | `.cex/temp/spawn_pids.txt` |
| spawn_stop.ps1 | `.cex/temp/spawn_pids.txt` |

**Impact**: Solo-spawned nuclei are invisible to monitor and stop. Grid-spawned nuclei are invisible to solo's PID tracking.

**Fix**: Unify all scripts to use `.cex/runtime/pids/spawn_pids.txt`.

### C6. `boot/n07.cmd` missing

All nuclei n01-n06 have boot scripts. N07 (orchestrator) does not. `spawn_solo.ps1` validates nucleus in `{n01-n06}` — N07 cannot be spawned as a nucleus task.

**Impact**: Self-spawn and overnight orchestrator restart impossible via standard dispatch.

**Fix**: Create `boot/n07.cmd` mirroring `boot/cex.cmd` configuration (pi, opus-4-6).

---

## 2. WARN Gaps (should fix)

### W1. 79 oversized ISOs across 57 builders

| ISO Type | Count Over Limit | Limit | Size Range |
|----------|-----------------|-------|------------|
| bld_system_prompt_*.md | 28 | 4096B | 4097–4170B |
| bld_instruction_*.md | 27 | 6144B | 6149–6284B |
| bld_quality_gate_*.md | 20 | 4096B | 4097–4141B |
| bld_architecture_*.md | 3 | 4096B | 4102–4170B |
| bld_knowledge_card_*.md | 1 | 4096B | 4101B |

**Overage range**: 1–188 bytes over limit. Average overage: ~80 bytes.

**Analysis**: These are NOT bloated files. The overages are minimal (0.02%–4.5% over limit). Content is dense and substantive — trimming risks losing essential instructions.

**Strategy options**:
1. **Raise limits**: system_prompt → 4200B, instruction → 6400B, quality_gate → 4200B. Pragmatic, preserves content.
2. **Targeted trim**: Remove trailing whitespace, blank lines, redundant headers. Could recover 50-100B per file.
3. **Accept as WARN**: Current behavior is functional. WARNs don't block builds.

**Recommendation**: Option 2 first (whitespace trim), then option 1 for remaining.

### W2. Two separate 8F executors (architectural confusion)

| Executor | File | Lines | Role |
|----------|------|-------|------|
| cex_8f_runner.py | 1,237L | Direct 8F pipeline (F1-F8 as methods) |
| cex_crew_runner.py | 969L | DAG executor from Motor's JSON plan |

These are NOT integrated. `cex_8f_motor.py` (1,385L) generates a JSON plan that `cex_crew_runner.py` consumes. Meanwhile `cex_8f_runner.py` implements F1-F8 independently.

**Impact**: Two incompatible execution paths, different error handling, different output formats.

**Recommendation**: Clarify roles — Runner = single-artifact direct build, CrewRunner = multi-artifact DAG orchestration. Document when to use which.

### W3. F7 GOVERN incomplete vs spec

Spec requires (from `n03-8f-enforcement.md`):
- 12LP checklist (12 points) — **NOT IMPLEMENTED** in runner
- 5D scoring (D1-D5 weighted) — **NOT IMPLEMENTED** in runner
- Density measurement (>= 0.85) — **NOT CALCULATED** at runtime

Runner implements 6 hard gates (H01-H06) only. This is functional but under-spec.

### W4. F4/F6 LLM calls unprotected

`cex_8f_runner.py` lines ~556 (F4 REASON) and ~763 (F6 PRODUCE) call `execute_prompt()` without try/except. If LLM is unavailable or returns error, the entire pipeline crashes.

### W5. dispatch.sh has no error handling

- No `set -e`
- No exit code checks from PowerShell
- No nucleus name validation
- No empty-task protection
- Silent failures throughout

### W6. Boot scripts use hardcoded paths

All `boot/*.cmd` use `set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex`. Non-portable.

**Fix**: `set CEX_ROOT=%~dp0..` to compute from script location.

### W7. Boot script structural inconsistency

- n02.cmd: minimal (395B, inline flags)
- n06.cmd: maximal (1717B, variables, MCP, settings)
- Mixed model versions: opus-4-0 (n03) vs sonnet-4 (n02, n05) vs opus-4-6 (cex.cmd)
- n01-claude.cmd and n04-claude.cmd override Gemini→Claude without documentation (loses 1M→128k context)

### W8. signal_writer.py weak validation

- Accepts any nucleus name (no ValidateSet)
- Accepts any status string
- No quality_score range check
- Uses local time, not UTC
- No path traversal protection

---

## 3. Test Failures Analysis

### Total: 497 passed / 15 failed

| Test File | Failures | Root Cause | Real Bug? |
|-----------|----------|------------|-----------|
| test_schema_evolution.py | 12 | `skill-builder` missing runtime/evolution fields | **YES** — builder is incomplete |
| test_score.py | 3 | `score_artifact()` formula floors at 8.0 | **YES** — scoring bug |

### test_schema_evolution.py — 12 failures (all `skill-builder`)

Tests check that ALL builders have evolved to include runtime fields (effort, max_turns, permission_scope, disallowed_tools), memory taxonomy (memory_scope, observation_types), discovery fields (keywords, triggers, capabilities), and tool permissions.

106/107 builders pass. `skill-builder` is the sole holdout — it was created but never hydrated with these fields.

**Verdict**: Real failures. Tests are correct and up-to-date. The builder is incomplete.

**Fix**: Run `python _tools/cex_schema_hydrate.py --builder skill-builder` or manually add missing fields to the 4 affected ISOs (manifest, memory, config, tools).

### test_score.py — 3 failures (scoring formula)

| Test | Expected | Got | Issue |
|------|----------|-----|-------|
| test_score_missing_file | 0.0 | 8.0 | Missing file not detected |
| test_score_no_frontmatter | <8.0 | 8.0 | No penalty for no frontmatter |
| test_score_empty_file | <7.0 | 8.0 | No penalty for empty content |

`score_structural()` returns raw=0 for all edge cases. Formula: `8.0 + (0/10)*1.3 = 8.0`. Never below 7.0.

**Verdict**: Real bug. The scoring function cannot distinguish between "unknown" (raw=0) and "terrible" (raw should be negative).

**Fix**: Add pre-checks in `score_artifact()`:
```python
if not Path(path).exists(): return (0.0, "file not found")
if not has_frontmatter(path): return (max(raw * 0.5, 3.0), "no frontmatter")
if Path(path).stat().st_size == 0: return (0.0, "empty file")
```

---

## 4. Builder Trim Strategy

### The problem: 79 files across 57 builders exceed size limits

| Limit | Files Over | Avg Overage | Max Overage |
|-------|-----------|-------------|-------------|
| 4096B (system_prompt, quality_gate, architecture, KC) | 52 | ~50B | 74B |
| 6144B (instruction) | 27 | ~90B | 140B |

### Content analysis

Sampled 10 oversized files. Findings:
- **0 files** have padding or filler content
- **All files** have dense, substantive content
- Common overhead: trailing blank lines (1-3), section headers with extra whitespace, redundant `---` separators

### Recommended trim strategy (priority order)

1. **Whitespace normalization** (estimated recovery: 30-80B per file)
   - Strip trailing whitespace on all lines
   - Remove trailing blank lines
   - Collapse double blank lines to single
   - Expected: fixes ~30 of 79 files

2. **Header compaction** (estimated recovery: 20-50B per file)
   - Remove blank line between `---` and first heading
   - Use consistent `##` vs `###` hierarchy
   - Expected: fixes ~20 more files

3. **Raise limits for remaining** (if 20+ files still over after trim)
   - system_prompt: 4096 → 4200B (+2.5%)
   - instruction: 6144 → 6400B (+4.2%)
   - quality_gate: 4096 → 4200B (+2.5%)
   - Justification: Content is legitimate, not bloat

4. **Do NOT**: Remove content sections, truncate examples, or strip quality gate criteria. These are load-bearing.

---

## 5. SDK Gaps

### Overall: 79 .py / 4,537 lines — Production-grade, NOT stubs

| Component | Status | Notes |
|-----------|--------|-------|
| 6 LLM providers | REAL | Anthropic (streaming), OpenAI, Google, Ollama (streaming), OpenRouter, LiteLLM |
| Workflow engine | COMPLETE | Step, Parallel, Loop, Condition, Router — all with real ThreadPoolExecutor |
| Knowledge pipeline | COMPLETE | 6 readers (CSV, JSON, MD, PDF, Web), 3 chunkers, 2 embedders, 1 reranker |
| Tool framework | COMPLETE | Function (auto JSON Schema), Toolkit (auto-discovery), MCP client |
| VectorDB | FUNCTIONAL | ChromaDB backend only |
| Memory | FUNCTIONAL | 4 modes: ALWAYS, AGENTIC, PROPOSE, HITL |
| Guardrails | FUNCTIONAL | PII detection + prompt injection |
| Session | FUNCTIONAL | Disk persistence to .cex/runtime/sessions/ |
| Eval | FRAMEWORK | QualityGateEval works, extensible |
| Tracing | FUNCTIONAL | OpenTelemetry exporter |
| Circular imports | ZERO | Clean DAG architecture verified |

### SDK gaps (minor)

| Gap | Severity | Notes |
|-----|----------|-------|
| Only 1 VectorDB backend (ChromaDB) | LOW | Sufficient for local dev; Pinecone/Weaviate can be added |
| Only 1 reranker backend (Cohere) | LOW | Extensible; Jina/BGE can be added |
| Streaming only for Anthropic + Ollama | LOW | Other providers fallback to invoke() |
| Memory compression needs tuning | MEDIUM | Framework present, parameters not calibrated |
| No integration tests with live APIs | MEDIUM | test_sdk_integrity.py is structural, not functional |

---

## 6. N03_engineering/ Artifacts

### Inventory: 80 .md + 40 compiled = 120 files

| Subdir | Files | Pillar | Purpose |
|--------|-------|--------|---------|
| agents/ | 3 | P02 | Agent, axiom, mental model |
| architecture/ | 6 | P08 | Patterns (construction triad, 3-phase, consultant, crew dispatch) |
| compiled/ | 40 | — | Generated YAML derivatives |
| config/ | 1 | P09 | Boot config |
| feedback/ | 3 | P11 | Guardrails, quality gates (12LP, H01-H07) |
| knowledge/ | 6 | P01 | KCs (engineering, software eng, tooling, construction laws), FSEs |
| memory/ | 1 | P10 | Learning record |
| orchestration/ | 9 | P12 | DAG, dispatch rules, handoff, signal, spawn config, workflows |
| output/ | 1 | P05 | Response format |
| prompts/ | 3 | P03 | Chain, prompt template, system prompt |
| quality/ | 3 | P07 | Benchmark, scoring rubrics (5D, engineering) |
| schemas/ | 2 | P06 | Input schema, interface |
| tools/ | 2 | P04 | Function defs, CLI tool |

### Classification

- **69/80 (86%) pure engineering** — meta-construction domain, 8F pipeline, builders, quality gates
- **11/80 (14%) hybrid** — software-engineering verticalization (added 2026-03-31): master KC, dispatch rules, workflows for code review/spec-to-code, CLI tool
- **0/80 generic** — all domain-scoped

### Agent config: WELL-CONFIGURED

`agent_engineering.md` (quality 8.9, density 0.92):
- Clear identity ("I am the Builder Nucleus. My input is human intent.")
- 11 quantified capabilities, 25 tools with script names + line counts
- Explicit boundaries (does/does not)
- Crew role defined (META-CONSTRUCTOR)
- All 13 required frontmatter fields present

---

## 7. Cross-Nucleus Integration

### dispatch.sh: FRAGILE

- No `set -e`, no exit code checks, no validation
- Silent failures on invalid nucleus names
- No empty-task protection

### spawn_solo.ps1: ROBUST

- ValidateSet enforces nucleus in {n01-n06}
- Creates runtime dirs, embeds manifest, tracks PIDs
- Proper quoting (avoids nested-quote hell)

### spawn_grid.ps1: WORKS with quirks

- Queue management, stuck detection (90min threshold)
- PID path inconsistency with spawn_solo (see C5)

### signal_writer.py: WEAK

- No input validation
- Local time, not UTC
- No archival automation
- Works for all nuclei (accepts any string)

### Boot scripts: FUNCTIONAL but inconsistent

- All 6 nucleus scripts (n01-n06) boot correctly
- n07.cmd MISSING (C6)
- Hardcoded paths (W6)
- Mixed structures and model versions (W7)

### Runtime state

- `.cex/runtime/signals/` — EMPTY (broken flow, C4)
- `.cex/runtime/pids/` — 4 stale PIDs from 2026-04-01
- `.cex/temp/spawn_pids.txt` — 18 stale PIDs from 2026-04-02
- `.cex/runtime/handoffs/` — 18 current SELF_REVIEW tasks (valid)
- `.cex/runtime/archive/` — 23 signals + 7 tasks (properly archived)
- `.cex/runtime/locks/` — EMPTY (clean, no zombie locks)

---

## 8. 8F Pipeline Gaps

### cex_8f_runner.py (1,237L) — REAL implementation, 75% spec-compliant

| Function | Status | Spec Compliance | Issue |
|----------|--------|-----------------|-------|
| F1 CONSTRAIN | REAL | 70% | Loads schemas but doesn't read kinds_meta.json, no naming pattern extraction |
| F2 BECOME | REAL | 100% | Loads manifests, system prompts, persona |
| F3 INJECT | REAL | 95% | 9 injection sources. Missing explicit match % calculation |
| F4 REASON | REAL | 80% | LLM plans structure. Unprotected LLM call |
| F5 CALL | REAL | 90% | Scans tools + existing artifacts |
| F6 PRODUCE | REAL | 85% | 9-section prompt. Unprotected LLM call, no token limit check |
| F7 GOVERN | PARTIAL | 60% | 6 hard gates work. Missing: 12LP checklist, 5D scoring, density measurement |
| F8 COLLABORATE | REAL | 90% | Save, compile, index, commit. Tight subprocess timeouts |

### cex_8f_motor.py (1,385L) — PLAN GENERATOR, not executor

- Parses intent (PT+EN verbs, 300+ keyword mappings)
- Classifies objects to kinds
- Generates JSON execution plan for crew_runner
- Does NOT execute F1-F8 itself

### cex_crew_runner.py (969L) — DAG executor for motor plans

- Consumes motor's JSON plan
- Composes 9-section prompts per builder
- Fork/inline execution modes
- Quality gate at score >= 7.0

### Key architectural gap

Two separate, incompatible execution paths:
1. Direct: `cex_8f_runner.py "intent" --execute` (single artifact, F1-F8 internal)
2. Motor: `cex_8f_motor.py` → JSON → `cex_crew_runner.py` (multi-artifact, DAG)

---

## Recommended Actions (priority order)

### P0 — Critical (blocks correctness)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | Hydrate `skill-builder` with missing fields (manifest, memory, config, tools) | 30min | Fixes 12 test failures |
| 2 | Fix `score_artifact()` edge cases (missing file → 0.0, empty → 0.0, no FM → penalty) | 1h | Fixes 3 test failures |
| 3 | Unify PID file path across all spawn scripts | 15min | Fixes monitor/stop for solo-spawned nuclei |
| 4 | Trace and fix signal write flow (ensure signals/ receives files) | 1h | Fixes grid completion detection |

### P1 — High (blocks robustness)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 5 | Create `boot/n07.cmd` for orchestrator | 15min | Enables N07 spawn via dispatch |
| 6 | Add try/except to F4 REASON and F6 PRODUCE LLM calls | 30min | Prevents pipeline crash on LLM failure |
| 7 | Add error handling to dispatch.sh (set -e, validation, exit codes) | 30min | Prevents silent dispatch failures |
| 8 | Exclude `compiled/` from doctor scan or move out of builders/ | 15min | Eliminates 1 FAIL |

### P2 — Medium (improves quality)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 9 | Whitespace trim across 79 oversized ISOs | 1h | Reduces WARN count by ~30 |
| 10 | Raise ISO size limits for remaining (4096→4200, 6144→6400) | 15min | Eliminates remaining WARNs |
| 11 | Implement 12LP checklist in F7 GOVERN | 2h | Spec compliance |
| 12 | Implement 5D scoring in F7 GOVERN | 3h | Spec compliance |
| 13 | Make boot script paths relative (`%~dp0..`) | 30min | Portability |
| 14 | Add validation to signal_writer.py | 30min | Robustness |

### P3 — Low (nice to have)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 15 | Document when to use runner vs crew_runner | 30min | Reduces confusion |
| 16 | Add VectorDB backends (Pinecone, Weaviate) | 4h | SDK completeness |
| 17 | Add streaming to OpenAI/Google providers | 2h | SDK feature parity |
| 18 | Signal archival automation | 1h | Runtime hygiene |
| 19 | Document n01-claude.cmd / n04-claude.cmd override purpose | 15min | Maintainability |

---

## Raw Numbers

```
Builders:           107 total (49 PASS / 57 WARN / 1 FAIL)
Builder ISOs:       1,378 files / 1,391 expected (missing: 13 in compiled/)
Builder total size: 3,937 KB
Builder avg density: 0.98

Tests:              497 passed / 15 failed (97.1% pass rate)
Test failures:      12 schema_evolution (skill-builder) + 3 score (formula bug)

SDK modules:        79 .py files
SDK lines:          4,537
SDK circular imports: 0
SDK providers:      6 (all functional)
SDK workflow types: 5 (Step, Parallel, Loop, Condition, Router)

N03 artifacts:      80 .md + 40 compiled
N03 avg quality:    8.98
N03 domain purity:  86% pure engineering / 14% hybrid

_tools:             53 .py files
Boot scripts:       9 .cmd (n07 missing)
Spawn scripts:      5 (1 .sh + 4 .ps1)

Runtime signals:    0 active / 23 archived
Runtime PIDs:       22 stale (4 in pids/ + 18 in temp/)
Runtime handoffs:   18 active (SELF_REVIEW)
Runtime locks:      0 (clean)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n05_self_review_2026-04-02]] | related | 0.31 |
| [[bld_collaboration_kind]] | downstream | 0.27 |
| [[wave2_quality_report]] | upstream | 0.25 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.24 |
| [[polish_fixes_20260413]] | downstream | 0.24 |
| [[bld_collaboration_builder]] | downstream | 0.24 |
| [[bld_config_kind]] | related | 0.24 |
| [[kind-builder]] | upstream | 0.23 |
| [[system_health_20260413]] | upstream | 0.23 |
| [[bld_architecture_kind]] | upstream | 0.23 |
