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
├── archetypes/builders/     L0 DNA — 70 builders × 13 files
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
    kind       = TABLE (78 types)
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

*CEX v3.0 — "SQL organized data. CEX organizes intelligence."*
