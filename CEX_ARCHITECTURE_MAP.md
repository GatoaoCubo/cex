# CEX Architecture Map — v2.0

> **Ctrl+G** = Graph View | **278+ connections** | Colors = hierarchy

---

## Color Hierarchy (4 levels, warm→cool)

### Level 1: Root Documents (WHITE — entry points)

| Color | Files |
|-------|-------|
| ⬜ Bright white | [[CLAUDE]], [[README]], [[INDEX]], [[LLM_PIPELINE]], [[CEX_ARCHITECTURE_MAP]] |
| 🩶 Light gray | [[archetypes/CODEX]], [[archetypes/GLOSSARY]], [[_docs/WHITEPAPER_CEX]], [[_docs/NAMING_CONVENTION]] |

### Level 2: 8 Functions × Builders (L0 DNA — 932 files)

| Color | Function | Builder files | Count |
|-------|----------|--------------|-------|
| 🔴 Red | BECOME (Who am I?) | bld_system_prompt_*, bld_manifest_* | 141 |
| 🔵 Blue | INJECT (What do I know?) | bld_knowledge_card_*, bld_examples_*, bld_memory_* | 211 |
| 🟢 Green | REASON + CALL | bld_instruction_*, bld_tools_*, bld_config_* | 211 |
| 🟡 Yellow | PRODUCE + CONSTRAIN | bld_output_template_*, bld_schema_* | 141 |
| 🟣 Purple | GOVERN | bld_quality_gate_*, bld_architecture_* | 141 |
| 🩵 Cyan | COLLABORATE | bld_collaboration_* | 71 |
| ⚪ Gray | Templates | tpl_* (structural, not content) | 85 |

### Level 3: 12 Pillars (L1 Schema — by group)

| Color | Group | Pillars | Functions |
|-------|-------|---------|-----------|
| 💙 Deep blue | CORE | [[P01_knowledge]], [[P02_model]], [[P03_prompt]], [[P04_tools]] | BECOME, INJECT, REASON, CALL |
| 🟠 Orange | QUALITY | [[P05_output]], [[P06_schema]], [[P07_evals]], [[P08_architecture]] | PRODUCE, CONSTRAIN, GOVERN |
| 💜 Soft purple | SCALE | [[P09_config]], [[P10_memory]], [[P11_feedback]], [[P12_orchestration]] | GOVERN, COLLABORATE |

### Level 4: 7 Nuclei (L2 Fractal Modules — rainbow gradient)

Each nucleus = fractal copy of all 12 pillars, scoped to one department.

| Color | Nucleus | Domain | Description |
|-------|---------|--------|-------------|
| 🔴 Deep red | [[N01_intelligence]] | Orchestration | Routing, decisions, task dispatch |
| 🟠 Orange | [[N02_marketing]] | Marketing | Content, ads, copy, social |
| 🟡 Yellow | [[N03_engineering]] | Engineering | Code, components, infrastructure |
| 🟢 Green | [[N04_knowledge]] | Knowledge | Documentation, indexing, RAG |
| 🩵 Teal | [[N05_operations]] | Operations | Deploy, testing, monitoring |
| 🔵 Blue | [[N06_commercial]] | Commercial | Sales, pricing, e-commerce |
| 🟣 Violet | [[N07_admin]] | Admin | Config, governance, maintenance |

---

## Fractal Pattern (same structure at every level)

```
CEX REPO (DATABASE)
│
├── archetypes/builders/     L0 DNA — 69 builders × 13 files
│   └── {builder}/
│       └── bld_{kind}_{topic}.md    ← colored by 8 functions
│
├── P01-P12/                 L1 SCHEMA — 12 pillars
│   ├── templates/
│   │   └── tpl_{kind}.md           ← gray (structural)
│   ├── examples/
│   │   └── ex_{kind}_{topic}.md    ← colored by pillar group
│   └── compiled/
│       └── {kind}_{topic}.yaml     ← materialized view
│
├── N01-N07/                 L2 INSTANCE — 7 fractal modules
│   ├── knowledge/                   mirrors P01
│   ├── agents/                      mirrors P02
│   ├── prompts/                     mirrors P03
│   ├── tools/                       mirrors P04
│   ├── output/                      mirrors P05
│   ├── schemas/                     mirrors P06
│   ├── quality/                     mirrors P07
│   ├── architecture/                mirrors P08
│   ├── config/                      mirrors P09
│   ├── memory/                      mirrors P10
│   ├── feedback/                    mirrors P11
│   └── orchestration/               mirrors P12
│
├── _tools/                  L3 ENGINE — 13 scripts (pipeline runtime)
│   ├── cex_doctor.py               ← v2: naming + density + 13-file check
│   ├── validate_builder.py         ← v2: bld_* naming + pre-commit
│   ├── cex_index.py                ← SQLite index + wikilink graph
│   ├── cex_pipeline.py             ← 5-stage: CAPTURE→COMPILE→ENVELOPE
│   ├── cex_feedback.py             ← quality tracking + auto-archive
│   ├── cex_init.py                 ← CLI scaffolder (5 questions)
│   ├── cex_compile.py              ← .md → .yaml compiler
│   ├── cex_forge.py                ← builder forge
│   ├── changelog_gen.py            ← CHANGELOG generator
│   ├── setup_hooks.sh              ← pre-commit hook installer
│   ├── bootstrap.py                ← initial setup
│   ├── bump_version.py             ← version bumper
│   ├── distill.py                  ← .md → compiled sync
│   └── validate_schema.py          ← schema validation
│
└── Root docs                L4 — entry points (white)
```

**The fractal**: L0 DEFINES the kinds. L1 TEMPLATES the kinds. L2 INSTANTIATES the kinds per department. Same naming grammar at every level. Same 12 categories at every level.

---

## Naming Grammar (fractal, same everywhere)

```
LAYER          PREFIX    EXAMPLE                              WHERE
─────          ──────    ───────                              ─────
L0 Builder     bld_      bld_system_prompt_agent.md           archetypes/builders/
L1 Template    tpl_      tpl_knowledge_card.md                P01_knowledge/templates/
L1 Example     ex_       ex_knowledge_card_rag.md             P01_knowledge/examples/
L2 Instance    (none)    knowledge_card_company_product.md    N01_intelligence/knowledge/
L2 Instance    (none)    agent_copywriter_marketing.md        N02_marketing/agents/
```

**Rule**: filename = identity = primary key = index entry.
One `find -name` query → exact results. Zero file opens needed.

---

## Cross-Layer Connections (Foreign Keys)

```
L0 bld_system_prompt_agent.md
    ↕ defines pattern for
L1 ex_agent_copywriter.md
    ↕ inherited by
L2 agent_copywriter_marketing.md (N02)
    ↕ uses knowledge from
L2 knowledge_card_company_product.md (N01)
    ↕ validated by
L2 quality_gate_sales.md (N02)
    ↕ pattern from
L1 ex_quality_gate_copy.md
    ↕ built by
L0 bld_quality_gate_quality_gate.md
```

**Every connection = 1 [[wikilink]] = 1 edge in graph = 1 FK in the database.**

---

## SQL Mapping (visual)

```
CEX REPO       = DATABASE
  P01-P12      = 12 SCHEMAS
    kind       = TABLE (69 types)
      .md      = ROW (instance)
  N01-N07      = 7 TENANT SCHEMAS (same tables, different data)
  id           = PRIMARY KEY
  references[] = FOREIGN KEY
  naming       = INDEX
  builder      = STORED PROCEDURE
  gate         = CHECK CONSTRAINT
  pre-commit   = TRIGGER
  compiled/    = MATERIALIZED VIEW
  _schema.yaml = INFORMATION_SCHEMA
```

---

---

## KC Library (Knowledge Card Lifecycle)

79 Knowledge Cards across 17 domains feed the CEX pipeline via Motor 8F INJECT.

### KC Lifecycle: PESQUISAR > DESTILAR > CONSTRUIR > VALIDAR

```
PESQUISAR (research)           DESTILAR (distill)
  External sources               Raw -> atomic facts
  Firecrawl, web, docs           density >= 0.8
  brain_query()                  frontmatter validation
       |                              |
       v                              v
CONSTRUIR (build)              VALIDAR (validate)
  ex_knowledge_card_*.md         cex_doctor checks
  Compiled to .yaml              quality_min: 7.0
  Wired to feeds_kinds           cex_compile --all
```

### KC Domain Distribution (17 domains)

| Domain Group | Domains | KCs | Coverage |
|-------------|:-------:|:---:|:--------:|
| CEX Core | cex_taxonomy, meta | 49 | 62% |
| Engineering | llm_engineering, execution, architecture | 10 | 13% |
| Knowledge | research, knowledge_engineering, llm_memory | 9 | 11% |
| Specialist | 8 remaining domains | 11 | 14% |

### KC Sources (3 types)

| Source | Description | Flow |
|--------|-------------|------|
| Distilled | Research → atomic facts | research_lead → knowledge_lead → P01 |
| Authored | Manual expert knowledge | Human → P01 |
| Generated | Tool-extracted structured data | _tools/ → P01 |

### feeds_kinds Wiring

```
KC Domain (17)  -->  feeds_kinds mapping  -->  Motor 8F INJECT function
                                               |
                                               v
                                          Builder execution
                                          (context injection)
```

KCs are injected during the INJECT function (Function 2 of 8).
Each KC's `domain:` field determines which builders receive it.

---

## Tools Layer (L3 ENGINE — _tools/)

13 scripts powering the CEX runtime. Added during overnight Waves 1-3.

| Tool | Version | Wave | Role |
|------|---------|------|------|
| [[cex_doctor]] | v2 | W1 Governance | Validates naming v2.0, density >= 0.8, 13-file completeness per builder |
| [[validate_builder]] | v2 | W1 Governance | Enforces bld_* naming, integrates with pre-commit hook (7 checks) |
| [[cex_index]] | v1 | W2 Engine | Builds SQLite index (.cex/index.db), scans all files, maps wikilink graph |
| [[cex_pipeline]] | v1 | W2 Engine | 5-stage pipeline: CAPTURE > DECOMPOSE > HYDRATE > COMPILE > ENVELOPE |
| [[cex_feedback]] | v1 | W2 Engine | Quality tracking, auto-archive scores < 7.0, promote scores >= 8.0 |
| [[cex_init]] | v1 | W3 Product | CLI scaffolder: 5 questions to functional CEX repo on day 1 |
| [[cex_compile]] | v1 | W5 Review | Compiles .md examples to .yaml in compiled/ directories |
| [[cex_forge]] | v1 | W2 Engine | Builder forge for new archetypes |
| [[changelog_gen]] | v1 | W4 Launch | Generates CHANGELOG.md from git history |
| [[setup_hooks]] | v1 | W1 Governance | Installs pre-commit hooks (7 checks) |
| [[bootstrap]] | v1 | pre-overnight | Initial repo setup |
| [[bump_version]] | v1 | pre-overnight | Semantic version bumper |
| [[distill]] | v1 | pre-overnight | .md to compiled/ sync engine |
| [[validate_schema]] | v1 | pre-overnight | Schema YAML validation |

---

*CEX v6.0.0 — "SQL organized data. CEX organizes intelligence."*
