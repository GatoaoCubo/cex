# CEX Architecture Map — Audit v1.0

> **Ctrl+G** = Graph View. Colors = 8 LLM Functions.
> **AUDIT DATE**: 2026-03-27 | **STATUS**: 2 naming systems coexist

---

## Graph Color Legend (by 8 Functions)

| Color | Function | Builder files (bld_*) | Count |
|-------|----------|----------------------|-------|
| 🔴 Red | BECOME (Who am I?) | bld_system_prompt_*, bld_manifest_* | 141 |
| 🔵 Blue | INJECT (What do I know?) | bld_knowledge_card_*, bld_examples_*, bld_memory_* | 211 |
| 🟢 Green | REASON + CALL | bld_instruction_*, bld_tools_*, bld_config_* | 211 |
| 🟡 Yellow | PRODUCE + CONSTRAIN | bld_output_template_*, bld_schema_* | 141 |
| 🟣 Purple | GOVERN | bld_quality_gate_*, bld_architecture_* | 141 |
| 🩵 Cyan | COLLABORATE | bld_collaboration_* | 71 |

| Color | Layer | Content |
|-------|-------|---------|
| Deep blue | CORE pillars (P01-P04) | Knowledge, Model, Prompt, Tools |
| Orange | QUALITY pillars (P05-P08) | Output, Schema, Evals, Architecture |
| Purple | SCALE pillars (P09-P12) | Config, Memory, Feedback, Orchestration |
| Gray | Templates (tpl_*) | 85 schema definitions |
| White | Root docs | CLAUDE.md, README, INDEX, CODEX, WHITEPAPER |

---

## Repo Health Dashboard

```
TOTAL FILES: 4,262

  ✅ Compliant (naming v2.0):     1,044 (24%)
     932 bld_*.md (builders)
      85 tpl_*.md (templates)
      27 ex_*.md  (examples)

  ⚠️  Real content, wrong name:     342 (8%)
     158 p{NN}_{abbrev}_*.md (old examples)
     177 compiled .yaml (follow source)
       7 _legacy files

  💀 Phantom scaffold (delete):   1,890 (44%)
     1,890 .gitkeep in N01-N07

  ❓ Misplaced (audit needed):      157 (4%)
     157 files in packages/

  🔧 Tools + config (audit):        ~35 (1%)
     29 _tools/*.py (~24 obsolete)
      4 _config (credentials)

  📄 Root + docs (OK):              ~35 (1%)
```

---

## Two Naming Systems (coexisting)

### System B — STANDARD (naming v2.0) ✅

Grammar: `{layer}_{kind}_{topic}.{ext}`

| Layer | Prefix | Example | Count |
|-------|--------|---------|-------|
| Builder (L0) | `bld_` | `bld_system_prompt_agent.md` | 932 |
| Template (L1) | `tpl_` | `tpl_knowledge_card.md` | 85 |
| Example (L1) | `ex_` | `ex_knowledge_card_rag.md` | 27 |

**Total compliant: 1,044 files**

### System A — LEGACY (to be renamed) ❌

Grammar: `p{NN}_{abbreviation}_{topic}.{ext}`

| Abbreviation | Kind | Example | Count |
|------|------|---------|-------|
| kc | knowledge_card | p01_kc_rag_fundamentals.md | 70 |
| pt | prompt_template | p03_pt_chain.md | 5 |
| agent | agent | p02_agent_gateway.md | 4 |
| skill | skill | p04_skill_web_scraper.md | 4 |
| ax | axiom | p09_ax_lifecycle_hooks.md | 4 |
| qg | quality_gate | p07_qg_density.md | 3 |
| +60 more | ... | ... | 68 |

**Total legacy: 158 files → need rename to ex_{kind}_{topic}.md**

---

## Layer Architecture (5 levels)

### L0: DNA — [[archetypes]] (70 builders × 13 files)

```
archetypes/builders/
├── agent-builder/           ← 1 of 70 builders
│   ├── bld_system_prompt_agent.md    🔴 BECOME
│   ├── bld_instruction_agent.md      🟢 REASON
│   ├── bld_knowledge_card_agent.md   🔵 INJECT
│   ├── bld_schema_agent.md           🟡 CONSTRAIN
│   ├── bld_quality_gate_agent.md     🟣 GOVERN
│   ├── bld_output_template_agent.md  🟡 PRODUCE
│   ├── bld_architecture_agent.md     🟣 GOVERN
│   ├── bld_collaboration_agent.md    🩵 COLLABORATE
│   ├── bld_memory_agent.md           🔵 INJECT
│   ├── bld_manifest_agent.md         🔴 BECOME
│   ├── bld_examples_agent.md         🔵 INJECT
│   ├── bld_config_agent.md           🟢 CALL
│   └── bld_tools_agent.md            🟢 CALL
└── ... (70 builders total)
```

### L1: Schema — 12 Pillars (P01-P12)

```
P01_knowledge/          ← CORE: INJECT function
├── templates/          ← tpl_{kind}.md (85 total across all pillars)
│   ├── tpl_knowledge_card.md
│   ├── tpl_context_doc.md
│   └── tpl_rag_source.md
├── examples/           ← MIXED: ex_* (new) + p01_* (old)
│   ├── ex_knowledge_card_rag.md        ✅ naming v2.0
│   ├── p01_kc_bm25_search.md          ❌ old naming
│   └── p01_kc_cex_function_become.md   ❌ old naming
└── compiled/           ← .yaml (materialized views)
    └── ex_knowledge_card_rag.yaml
```

### L2: Departments — 7 Nuclei (N01-N07) 💀

```
N01_intelligence/       ← 270 .gitkeep files, ZERO real content
N02_marketing/          ← 270 .gitkeep files, ZERO real content
...
N07_admin/              ← 270 .gitkeep files, ZERO real content
                        
TOTAL: 1,890 phantom files. DELETE ALL.
```

### L3: Pipeline Engine

```
_tools/
├── cex_compile.py      ← COMPILE phase
├── cex_forge.py        ← CREATE artifacts
├── cex_doctor.py       ← GOVERN (diagnostics)
├── validate_*.py (6)   ← CONSTRAIN (validation)
├── bootstrap.py        ← cex init
└── ~12 obsolete        ← AUDIT needed
```

### L4: Root Documents

| File | Purpose | SQL analog |
|------|---------|-----------|
| [[CLAUDE.md]] | LLM entry point | CONNECTION STRING |
| [[README.md]] | Human entry point | DB README |
| [[LLM_PIPELINE.md]] | 8 functions | TABLE OF CONTENTS |
| [[INDEX.md]] | Registry | INFORMATION_SCHEMA |
| [[archetypes/CODEX.md]] | Governance | CONSTRAINTS |
| [[_docs/WHITEPAPER_CEX.md]] | Thesis | DESIGN DOC |
| [[_docs/NAMING_CONVENTION.md]] | Index spec | INDEX DEF |

---

## 8 Functions → File Discovery (INDEX power)

| Function | Find command | Results |
|----------|-------------|---------|
| BECOME | `find -name "bld_system_prompt_*"` | 71 |
| INJECT | `find -name "bld_knowledge_card_*"` | 71 |
| REASON | `find -name "bld_instruction_*"` | 71 |
| CALL | `find -name "bld_tools_*"` | 71 |
| PRODUCE | `find -name "bld_output_template_*"` | 71 |
| CONSTRAIN | `find -name "bld_schema_*"` | 71 |
| GOVERN | `find -name "bld_quality_gate_*"` | 71 |
| COLLABORATE | `find -name "bld_collaboration_*"` | 71 |

---

## Cleanup Plan (Priority Order)

| # | Action | Files | Impact |
|---|--------|-------|--------|
| 1 | Delete N01-N07 .gitkeep | 1,890 | -44% bloat |
| 2 | Rename 158 old examples → ex_* | 158 | +158 compliant |
| 3 | Re-compile 177 yaml | 177 | follows source |
| 4 | Audit packages/ (reclassify or delete) | 157 | -4% or reclassify |
| 5 | Audit _tools/ (mark obsolete) | ~24 | clarity |
| 6 | Delete _legacy/ | 7 | cleanup |
| 7 | Gitignore _config/credentials | 2 | security |

**After cleanup: 4,262 → ~1,571 files. All naming v2.0 compliant.**

---

*CEX v3.0 — "SQL organized data. CEX organizes intelligence."*
