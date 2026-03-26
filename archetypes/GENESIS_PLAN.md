---
id: genesis_plan
type: plan
version: 1.0.0
created: 2026-03-26
status: active
total_types: 81
total_builders: 81
total_chiefs: 12
total_iso_files: ~1200
---

# GENESIS PLAN — 5 Phases to Build the Archetype Tree

## Overview

```
         STELLA (orchestrator)
            |
    ┌───────┼───────┐
    ▼       ▼       ▼
 Satellites (EDISON, SHAKA, PYTHA...)
    |       |       |
    ▼       ▼       ▼
 12 LP Chiefs (architects)
    |       |       |
    ▼       ▼       ▼
 81 Type Builders (specialists)
    |       |       |
    ▼       ▼       ▼
 Artifacts (KCs, model_cards, skills, agents...)
```

Current: 1/81 builders. 0/12 chiefs. 0/1 archetype template.

---

## PHASE 1: PROVE (1 session)
**Goal**: Validate the 13-ISO-file pattern produces quality 9.5+ artifacts.

| Step | Action | Satellite | Output |
|------|--------|-----------|--------|
| 1.1 | Load model-card-builder's 13 ISOs as context | EDISON | — |
| 1.2 | Produce `p02_mc_google_gemini_2_5_pro.md` | EDISON | model_card |
| 1.3 | Validate with `validate_kc.py` (adapt for mc) | STELLA | score |
| 1.4 | Fix ISO files based on friction found | EDISON | patches |
| 1.5 | Produce 2nd card: `p02_mc_openai_gpt_4o.md` | EDISON | model_card |
| 1.6 | Compare both cards: consistent format? | STELLA | assessment |
| 1.7 | Push CEX (17+ commits) | STELLA | remote sync |

**Exit criteria**: 2 model_cards scoring 9.0+, consistent output, no ISO file changes needed.

**Risk**: builder ISOs might be too vague → fix INSTRUCTIONS or SCHEMA.

---

## PHASE 2: EXTRACT (1-2 sessions)
**Goal**: Extract the universal archetype template (the builder-builder).

| Step | Action | Satellite | Output |
|------|--------|-----------|--------|
| 2.1 | Analyze model-card-builder: what is TYPE-SPECIFIC vs UNIVERSAL | STELLA | analysis |
| 2.2 | Create `archetypes/builders/_template/` (13 generic ISOs) | EDISON | template |
| 2.3 | Create `archetype-builder` (builder that builds builders) | EDISON | meta-builder |
| 2.4 | Test: use archetype-builder to regenerate model-card-builder | EDISON | validation |
| 2.5 | Test: use archetype-builder to create `signal-builder` (simple type) | EDISON | 2nd builder |
| 2.6 | Validate signal-builder produces quality signal artifacts | EDISON | artifacts |
| 2.7 | Publish KC: `p01_kc_cex_archetype_concept.md` | PYTHA | knowledge |

**Exit criteria**: archetype-builder produces builders that produce 9.0+ artifacts.

**Mapping (TYPE-SPECIFIC → UNIVERSAL)**:
```
KNOWLEDGE.md   → mostly type-specific (domain knowledge varies 100%)
MANIFEST.md    → ~80% universal (id, type, lp change; structure same)
SYSTEM_PROMPT  → ~60% universal (role + rules pattern same, content varies)
INSTRUCTIONS   → ~50% universal (3-phase pattern universal, steps vary)
TOOLS.md       → ~70% universal (validate, brain_query, cex_forge shared)
OUTPUT_TEMPLATE → ~40% universal (structure shared, fields type-specific)
SCHEMA.md      → ~30% universal (frontmatter pattern shared, fields vary)
EXAMPLES.md    → 0% universal (fully type-specific)
ARCHITECTURE   → ~50% universal (boundary pattern universal, relationships vary)
CONFIG.md      → ~60% universal (naming/path pattern shared, rules vary)
MEMORY.md      → ~70% universal (pattern structure shared, data varies)
QUALITY_GATES  → ~50% universal (HARD/SOFT pattern shared, gates vary)
COLLABORATION  → ~60% universal (crew pattern shared, roles vary)
```

---

## PHASE 3: SCALE (4-6 sessions)
**Goal**: Mass-produce all 81 builders using multi-model grid.

### Wave Strategy

| Wave | LPs | Types | Sessions | Rationale |
|------|-----|-------|----------|-----------|
| A | P02 | 8 remaining (agent, lens, boot_config...) | 1-2 | Same LP as model_card, most similar |
| B | P01 + P05 | 6 + 4 = 10 | 1 | Knowledge + Output (simpler types) |
| C | P04 + P06 | 10 + 7 = 17 | 1-2 | Tools + Schema (medium complexity) |
| D | P03 | 13 | 1 | Prompt types (self-referential — prompts about prompts) |
| E | P07-P12 | 6+5+5+4+5+7 = 32 | 2 | Eval + Arch + Config + Memory + Feedback + Orchestration |

### Grid Composition Per Wave

```
Each wave uses 4-6 satellites:

  SHAKA (sonnet)    → Research: industry standards for each type
  PYTHA (gemini)    → Spec: compare implementations across providers
  EDISON (opus)     → Build: compose ISO files using archetype-builder
  ATLAS (opus)      → Validate: run quality gates, integration tests

  Per type (~15 min):
    1. SHAKA researches (3 min)
    2. EDISON builds 13 ISOs using template + research (8 min)
    3. ATLAS validates (2 min)
    4. Fix loop if needed (2 min)
```

### Continuous Batching

Waves C-E: >6 types per wave → continuous batching mode.
Each EDISON slot finishes 1 builder → immediately starts next.

```bash
powershell -NoProfile -ExecutionPolicy Bypass \
  -File records/core/powershell/spawn_grid.ps1 \
  -mission GENESIS_WAVE_A -mode continuous -interactive
```

### Target Output

81 builders × ~13 files × ~2KB avg = ~2,100 files, ~4.2MB

---

## PHASE 4: CHIEFS (2 sessions)
**Goal**: Build 12 LP chief architects that manage their LP's builders.

| Step | Action | Output |
|------|--------|--------|
| 4.1 | Design chief template (13 ISOs, architect role) | `archetypes/chiefs/_template/` |
| 4.2 | Build P02-chief first (manages 9 P02 builders including model-card) | `archetypes/chiefs/p02-chief/` |
| 4.3 | Test: P02-chief composes crew to build agent from scratch | validation |
| 4.4 | Build remaining 11 chiefs via grid | 11 chief directories |
| 4.5 | Wire chiefs: each knows its builders + cross-LP collaboration | COLLABORATION.md updates |

**Chief vs Builder**:
```
Builder: "I build model_cards" (specialist, reactive, 1 type)
Chief:   "I architect P02 systems" (coordinator, proactive, manages 9 builders)
         "Need an agent? I compose: model-card + agent + boot-config builders"
```

Chiefs are the first entities with ORCHESTRATION capability.
Builders are pure PRODUCTION.

---

## PHASE 5: INTEGRATE (2 sessions)
**Goal**: Wire archetypes into the CEX production pipeline.

| Step | Action | Satellite | Output |
|------|--------|-----------|--------|
| 5.1 | Build `validate_artifact.py` (generic, all 81 types) | EDISON | tool |
| 5.2 | Update `cex_forge.py` to load archetypes/builders/ | EDISON | tool update |
| 5.3 | Build `cex compile` — archetype → production artifact | EDISON | CLI command |
| 5.4 | Update _docs (ARCHITECTURE, QUICKSTART, LLM_INSTRUCTIONS) | PYTHA | docs |
| 5.5 | Publish KCs: archetype system, builder pattern, chief pattern | PYTHA | 3-5 KCs |
| 5.6 | Final quality audit: all 81 builders produce 9.0+ artifacts | ATLAS | audit report |
| 5.7 | Push CEX final | STELLA | remote sync |

**End state**:
```
Any satellite can:
  1. Receive task: "build X"
  2. Load archetype-builder or specific type-builder
  3. Produce artifact with quality gates
  4. Validate automatically
  5. Commit to correct LP directory

The system builds itself, validates itself, documents itself.
```

---

## Timeline

| Phase | Sessions | Builders | Cumulative |
|-------|----------|----------|------------|
| 1. PROVE | 1 | 1 (tested) | 1/81 |
| 2. EXTRACT | 1-2 | 2 (+ template) | 3/81 |
| 3. SCALE | 4-6 | 78 | 81/81 |
| 4. CHIEFS | 2 | — | + 12 chiefs |
| 5. INTEGRATE | 2 | — | Production |
| **Total** | **10-13** | **81 + 12** | **Complete** |

---

## Norms (apply to ALL phases)

1. **Min 12 ISO files per builder** (fractal floor), no ceiling
2. **archetype/** is the canonical path (never _meta/)
3. **quality: null** always — never self-score
4. **Boundary first** — every builder defines what it IS and IS NOT before anything else
5. **Cite sources** — every KNOWLEDGE.md references real standards (not invented)
6. **Test before template** — never extract pattern from untested builder
7. **Continuous batching** for >6 independent tasks
8. **Push between phases** — never accumulate >20 local commits

