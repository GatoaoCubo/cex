---
quality: 8.4
quality: 7.7
id: spec_full_coverage_plan
kind: knowledge_card
pillar: P08
nucleus: n07
mission: FULL_COVERAGE
title: "CEX 100% Coverage Spec — All Pillars, Kinds, 8F, Nuclei"
version: 1.0.0
tags: [spec, coverage, bootstrap, self-build, mission-plan, full-coverage]
created: 2026-04-18
density_score: 1.0
updated: "2026-04-22"
---

# CEX 100% Coverage Spec

> **Target:** Every coverage dimension at 100%. No dark corners.
> **Method:** 5 waves across 7 nuclei. CEX builds itself.
> **Measurement:** `python _tools/cex_flywheel_audit.py audit` all PASS.

---

## 1. CURRENT STATE AUDIT (2026-04-18)

### Tier 1 — Kind Scaffolding (per-kind artifacts)

| Dimension | Current | Target | Gap | % Done |
|-----------|---------|--------|-----|--------|
| Builders (12 ISOs each) | 295/293 | 295 | 0 | **100%** |
| KCs in N00_genesis/library/kind/ | 293/293 | 293 | 0 | **100%** |
| Sub-agents in .claude/agents/ | 293/293 | 293 | 0 | **100%** |
| Compiled YAMLs in builders/compiled/ | 2,637 | 2,637 | 0 | **100%** |
| depends_on in kinds_meta.json | 62/293 | 293 | 231 | 21% |
| Builder ISO set (HERMES 4: scoring_rubric, llm_judge, skill, context_file) | 0/295 | 295 | 295 | 0% |

### Tier 2 — Nucleus Fractal (per-nucleus per-pillar)

| Dimension | Current | Target | Gap | % Done |
|-----------|---------|--------|-----|--------|
| Pillar slots occupied (7N x 12P) | 84/84 | 84 | 0 | **100%** |
| component_map present | 3/7 nuclei | 7 | 4 | 43% |
| Per-nucleus benchmark artifact (P07) | 2/7 | 7 | 5 | 29% |
| Per-nucleus workflow coverage (P12, 3+ kinds) | ~4/7 | 7 | 3 | 57% |
| Per-nucleus data_contract (P06) | ~3/7 | 7 | 4 | 43% |
| N07 P07 evals (only 2 artifacts) | 2 | 8+ | 6 | 25% |

### Tier 3 — Quality Distribution

| Bracket | Count | % | Action |
|---------|-------|---|--------|
| quality >= 9.0 | 669 | 66.6% | -- |
| quality 8.0-8.99 | 246 | 24.5% | evolve sweep |
| quality < 8.0 | 8 | 0.8% | priority evolve |
| quality: null | 81 | 8.1% | score + evolve |
| **Total artifacts scanned** | **1,004** | | |

**Target:** 100% at quality >= 8.5, 80%+ at >= 9.0.

### Tier 4 — SDK Domain Coverage

| SDK Domain | Pillars Covered | Pillars Missing | Notes |
|------------|-----------------|-----------------|-------|
| eval/ | P07 | -- | OK |
| guardrails/ | P11 | -- | OK |
| knowledge/ | P01 | -- | OK |
| memory/ | P10 | -- | OK |
| models/ | P02 | -- | OK |
| reasoning/ | P03, P07 | -- | partial |
| session/ | P02, P12 | -- | bridge module |
| tools/ | P04 | -- | OK |
| tracing/ | P10 | -- | OK |
| vectordb/ | P01, P10 | -- | OK |
| workflow/ | P12 | -- | OK |
| **MISSING** | **P05 Output** | output/ | no SDK |
| **MISSING** | **P08 Architecture** | architecture/ | no SDK |
| **MISSING** | **P09 Config** | config/ | no SDK |

**Gap:** 3 SDK domains missing = 74 kinds (P05 23 + P08 14 + P09 37) have no runtime module.

### Tier 5 — Wiring Completeness

| Wire | Status | Gap |
|------|--------|-----|
| F3b auto-persist hook | WIRED (N05 BOOTSTRAP_SELF_W1) | -- |
| F5 CALL tool-to-kind registry | 47/300 kinds mapped | 300 kinds unmapped |
| depends_on dependency graph | 62/293 patched | 231 missing |
| Flywheel audit all-PASS | UNKNOWN | Run to verify |
| Cross-nucleus handoff ACK | NOT wired | design + build |
| Per-kind example instance (live artifact) | ~40% | ~60% missing |

---

## 2. COVERAGE DEFINITION

**100% coverage** = all 6 tiers at target simultaneously.

| Tier | Measurable 100% Condition |
|------|--------------------------|
| T1 Scaffolding | `cex_doctor.py` 0 FAIL + all 300 kinds have depends_on |
| T2 Fractal | Every nucleus: component_map + benchmark + 3+ P12 workflows + data_contract |
| T3 Quality | 0 artifacts with quality: null or quality < 8.0; 80%+ at >= 9.0 |
| T4 SDK | 3 new SDK domains (output, architecture, config) with base classes |
| T5 Wiring | tool-to-kind for all 300 kinds; flywheel audit 109/109 PASS |
| T6 Evals | Every nucleus P07: quality_gate + scoring_rubric + benchmark + llm_judge |

---

## 3. WAVE PLAN

### WAVE 1 — depends_on Completion (N01 + N07 tool)

**Owner:** N01 (research) + N07 (tool extension)
**Artifacts:** expanded KNOWN_DEPS in `cex_kind_deps.py` covering all 231 missing kinds

**N01 task:**
- Read all 293 KCs + builder architecture files
- For each of the 300 kinds missing depends_on: infer dependencies from KC references + builder architecture sections
- Output: dependency patch file `.cex/kind_deps_patch.json` with 231 entries
- Format: `{kind: [dep1, dep2, ...]}`

**N07 tool task:**
- Extend `_tools/cex_kind_deps.py` KNOWN_DEPS dict with all 231 entries from N01 output
- Run: `python _tools/cex_kind_deps.py --patch`
- Verify: all 300 kinds have depends_on
- Commit: `[N07] FULL_COVERAGE W1: 293/300 kinds with depends_on`

**Success gate:** `python -c "import json; d=json.load(open('.cex/kinds_meta.json')); print(sum(1 for v in d.values() if v.get('depends_on')))"`
Expected: >= 280 (some leaf kinds have no deps — that is correct, not a gap)

---

### WAVE 2 — Nucleus Fractal Completion (N04, N05, N06, N07 parallel)

**Owner:** 4 nuclei in parallel grid
**Missing:** component_map for N04, N05, N06, N07; benchmark + P07 fills

**N04 task (Knowledge):**
- Build `N04_knowledge/P08_architecture/component_map_n04.md`
  - Map: KC library -> RAG pipeline -> entity memory -> knowledge index -> search
  - Data flows, component inventory, inter-nucleus deps
- Build `N04_knowledge/P07_evaluation/benchmark_n04.md` (kind: benchmark)
  - KC quality metrics, RAG retrieval accuracy, memory freshness
- Build `N04_knowledge/P06_schema/data_contract_n04_to_n01.md` (kind: data_contract)
  - Contract: N04 knowledge output -> N01 research consumption

**N05 task (Operations):**
- Build `N05_operations/P08_architecture/component_map_n05.md`
  - Map: quality gates -> CI/CD -> tool pipeline -> eval loop -> signals
- Build `N05_operations/P07_evaluation/benchmark_n05.md`
  - Quality gate pass rate, eval latency, doctor clean rate
- Build `N05_operations/P12_orchestration/workflow_quality_loop_n05.md` (kind: workflow)
  - The continuous quality improvement loop: scan -> score -> evolve -> gate -> commit

**N06 task (Commercial):**
- Build `N06_commercial/P08_architecture/component_map_n06.md`
  - Map: research -> copy -> pricing -> funnel -> feedback -> retention
- Build `N06_commercial/P07_evaluation/benchmark_n06.md`
  - Revenue pipeline metrics, churn rate, conversion funnel KPIs
- Build `N06_commercial/P06_schema/data_contract_n06_pricing.md`
  - Contract: N06 pricing output -> N02 copy consumption

**N07 task (Orchestrator):**
- Build `N07_admin/P08_architecture/component_map_n07.md`
  - Map: GDP -> dispatch -> wave management -> signal polling -> consolidate
- Build `N07_admin/P07_evaluation/benchmark_dispatch_efficiency.md`
  - avg dispatch-to-signal time, missions per day, quality floor compliance
- Build `N07_admin/P07_evaluation/scoring_rubric_orchestration.md` (kind: scoring_rubric)
  - Rubric for evaluating handoff quality, wave design quality
- Build `N07_admin/P07_evaluation/llm_judge_orchestration.md` (kind: llm_judge)
  - LLM-as-judge prompt for evaluating N07 orchestration decisions
- Build `N07_admin/P11_feedback/learning_record_n07.md` (kind: learning_record)
  - Capture orchestration lessons from BOOTSTRAP_SELF_W1 + SELF_AUDIT missions
- Build `N07_admin/P11_feedback/regression_check_n07.md` (kind: regression_check)
  - What N07 checks each mission to avoid repeating past failures

---

### WAVE 3 — Quality Sweep (all nuclei via cex_evolve.py)

**Owner:** N05 orchestrates, all nuclei contribute via evolve sweep
**Target:** 0 quality: null, 0 quality < 8.0, 80%+ at >= 9.0

**Steps:**
1. Score all null artifacts: `python _tools/cex_evolve.py sweep --target 8.5 --max-rounds 1 --score-only`
2. Identify < 8.0 artifacts: `python _tools/cex_evolve.py report --below 8.0`
3. Improve bottom 8: dispatch N03 to rewrite (these are in engineering domain)
4. Full sweep: `python _tools/cex_evolve.py sweep --target 9.0 --max-rounds 2`
5. Verify: no quality: null or < 8.0 remaining

**Note:** quality: null in NEW artifacts from BOOTSTRAP_SELF_W1 and SELF_AUDIT missions
is expected — they need peer review scoring. This wave assigns those scores.

---

### WAVE 4 — SDK Domain Expansion (N03 + N05)

**Owner:** N03 (builds), N05 (wires + tests)
**Gap:** P05 Output, P08 Architecture, P09 Config have no cex_sdk module

**N03 task — Build 3 SDK domains:**

`cex_sdk/output/` — P05 Output runtime module
- `base.py`: OutputFormatter abstract base class
  - `format(artifact: dict, target: str) -> str`
  - targets: markdown, json, yaml, html, pdf
- `formatters/`: MarkdownFormatter, JSONFormatter, HTMLFormatter
- `__init__.py`

`cex_sdk/architecture/` — P08 Architecture runtime module
- `base.py`: ArchitectureAnalyzer abstract base
  - `component_map(nucleus_dir: str) -> dict`
  - `decision_record(decision: dict) -> str`
- `analyzers/`: ComponentMapAnalyzer, NamingRuleChecker
- `__init__.py`

`cex_sdk/config/` — P09 Config runtime module
- `base.py`: ConfigLoader abstract base
  - `load(kind: str, path: str) -> dict`
  - `validate(config: dict, schema: dict) -> bool`
- `loaders/`: EnvConfigLoader, FeatureFlagLoader, RateLimitLoader, SecretConfigLoader
- `__init__.py`

**N05 task — Wire + test:**
- Add 3 new modules to `cex_sdk/__init__.py`
- Write `cex_sdk/tests/test_output.py`, `test_architecture.py`, `test_config.py`
- Run: `python -m pytest cex_sdk/tests/ -q`

---

### WAVE 5 — Wiring Completion (N01 + N07)

**Owner:** N01 (research), N07 (tool extension)
**Gap:** tool-to-kind for 300 kinds; flywheel audit; cross-nucleus ACK

**N01 task — Extend tool-to-kind registry:**
- Read `.cex/kind_tool_registry.json` (currently 47 kinds mapped)
- Read all `_tools/cex_*.py` docstrings more deeply: many tools handle multiple kinds
- For each of 246 unmapped kinds: find the most relevant tool by name similarity + docstring
- Output: `.cex/kind_tool_registry_extended.json` with 300 kinds mapped
- Update `_tools/cex_kind_tool_map.py` HEURISTICS dict with explicit kind->tool mappings

**N07 task — Flywheel audit + ACK protocol:**
- Run: `python _tools/cex_flywheel_audit.py audit` — capture all failures
- For each failure: identify fix (many will be documentation gaps, not code)
- Fix top 10 flywheel failures in place
- Design `_tools/cex_handoff_ack.py`:
  - nuclei write `.cex/runtime/handoffs/.ack/{nucleus}_{mission}.json` at session start
  - N07 polls for ACK before marking nucleus as working
  - Closes race condition where n0X_task.md overwritten before nucleus reads it
- Build `cex_handoff_ack.py` and integrate into `boot/n0{1-6}.ps1` (write ACK at startup)

---

## 4. SPEC SUMMARY TABLE

| Wave | Nuclei | Primary Output | Success Metric |
|------|--------|----------------|----------------|
| W1 depends_on | N01 + N07 | 293/300 kinds with depends_on | `cex_kind_deps.py --report` shows 0 gaps |
| W2 Fractal | N04, N05, N06, N07 | 4 component_maps + 6+ P07 artifacts | All 7 nuclei have component_map + benchmark |
| W3 Quality | All (via evolve) | 0 null + 0 < 8.0 quality | `cex_evolve.py report` shows 100% scored |
| W4 SDK | N03 + N05 | 3 new cex_sdk domains | `pytest cex_sdk/tests/ -q` all pass |
| W5 Wiring | N01 + N07 | 300 kinds tool-mapped + ACK protocol | `cex_flywheel_audit.py audit` 109/109 PASS |

**Total new artifacts:** ~60 artifacts + 3 SDK domains + 293 depends_on patches + 246 tool mappings

---

## 5. AUTOMATION LEVERAGE

High-ROI tools to run BEFORE dispatching each wave:

```bash
# W1: Seed deps from existing KC cross-references (free, no LLM)
python _tools/cex_kind_deps.py --scan > .cex/runtime/kind_deps_scan.txt

# W2: Find which nuclei are missing which mandatory artifacts
python -c "
from pathlib import Path
for nd in ['N04_knowledge','N05_operations','N06_commercial','N07_admin']:
    missing = [k for k in ['component_map','benchmark','data_contract']
               if not list(Path(nd).rglob(f'*{k}*.md'))]
    if missing: print(f'{nd}: missing {missing}')
"

# W3: Find all null/low quality artifacts before sweep
python _tools/cex_evolve.py report --below 8.5

# W4: Verify SDK imports work after building
python -c "from cex_sdk import output, architecture, config; print('OK')"

# W5: Run flywheel before and after to measure delta
python _tools/cex_flywheel_audit.py audit --format json > .cex/quality/flywheel_pre_w5.json
```

---

## 6. DISPATCH COMMANDS

```bash
# W1
bash _spawn/dispatch.sh solo n01 "FULL_COVERAGE W1 — depends_on research for 300 kinds"

# W2
bash _spawn/dispatch.sh grid FULL_COVERAGE_W2   # handoffs: n04, n05, n06, n07

# W3
python _tools/cex_evolve.py sweep --target 9.0 --max-rounds 2

# W4
bash _spawn/dispatch.sh grid FULL_COVERAGE_W4   # handoffs: n03, n05

# W5
bash _spawn/dispatch.sh grid FULL_COVERAGE_W5   # handoffs: n01, n07
```

---

## 7. FINAL VERIFICATION

Run after all 5 waves complete:

```bash
python _tools/cex_doctor.py                          # 0 FAIL
python _tools/cex_flywheel_audit.py audit            # 109/109 PASS
python _tools/cex_kind_deps.py --report              # 0 gaps
python _tools/cex_kind_tool_map.py --output /dev/null # 300 kinds indexed
python _tools/cex_evolve.py report                   # 0 null, 0 < 8.0
python -c "from cex_sdk import output, architecture, config; print('SDK OK')"
python -m pytest cex_sdk/tests/ -q                  # all pass
git log --oneline -20                               # clean history
```

**All pass = 100% coverage achieved.**

---

## 8. ESTIMATED EFFORT

| Wave | Sessions | Duration | Parallelism |
|------|----------|----------|-------------|
| W1 | 1 N01 + N07 tool work | ~15min | Solo + in-session |
| W2 | 4-nucleus grid | ~10min | 4x parallel |
| W3 | evolve sweep | ~20min | automated |
| W4 | 2-nucleus grid | ~20min | 2x parallel |
| W5 | 2-nucleus grid | ~15min | 2x parallel |
| **Total** | **~5 sessions** | **~80min wall clock** | **max 4x parallel** |

---

## 9. WHAT IS INTENTIONALLY NOT IN SCOPE

| Item | Reason |
|------|--------|
| HERMES ISO set (scoring_rubric, llm_judge, skill, context_file) for all 301 builders | 1,180 new files — separate HERMES_ISO_BACKFILL mission |
| Public GitHub release automation | Requires human review gate |
| LiteLLM / multi-runtime CI | Separate MULTIRUNTIME mission |
| Fine-tuning dataset generation | Separate FT mission |
| Per-kind example instances (live artifacts for all 300 kinds) | EXAMPLE_LIBRARY mission |
