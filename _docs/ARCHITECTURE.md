# CEX Architecture

**v1.0 | 2026-03-22**

---

## 1. Layer Map

```
+------------------------------------------------------------------+
|                        CEX FRAMEWORK                            |
+------------------------------------------------------------------+
|  CORE Layer (P01-P04)       "What the agent IS and KNOWS"       |
|    P01 Knowledge     — Facts, domain cards, context docs        |
|    P02 Model         — Identity, capabilities, routing          |
|    P03 Prompt        — Instructions, system prompts, HOPs       |
|    P04 Tools         — Skills, MCPs, connectors, hooks          |
+------------------------------------------------------------------+
|  QUALITY Layer (P05-P08)    "How the agent PERFORMS"            |
|    P05 Output        — Structured responses, output schemas     |
|    P06 Schema        — Validation contracts, type definitions   |
|    P07 Evals         — Quality metrics, benchmarks, scorecards  |
|    P08 Architecture  — System design, scaling patterns          |
+------------------------------------------------------------------+
|  SCALE Layer (P09-P12)      "How the agent OPERATES at scale"   |
|    P09 Config        — Environment, feature flags, secrets      |
|    P10 Memory        — State, persistence, retrieval indexes    |
|    P11 Feedback      — Learning loops, corrections, drift logs  |
|    P12 Orchestration — Workflows, dispatch, multi-agent coord   |
+------------------------------------------------------------------+
```

---

## 2. Artifact Pipeline

Every LP follows the same production chain:

```
_schema.yaml
    |  Defines: types (68 total), constraints, frontmatter fields,
    |           max_bytes, quality_min, density_min
    v
_generator.md
    |  Defines: step-by-step authoring protocol, anti-patterns,
    |           density rules, type-specific guidance
    v
templates/
    |  Defines: fillable structure with {{MUSTACHE}} and [BRACKET]
    |           variables — one template per primary type
    v
examples/
       Validated instances: density >= 0.80, quality >= 7.0,
       dual output (.md + .yaml), id == filename stem
```

---

## 3. Data Flow: User Input to Indexed Artifact

```
User Input
    |
    v
[1] bootstrap.sh
    |  Creates LP structure: P01-P12/ + archetypes/ + _tools/
    |  Copies schemas, generators, templates into new repo
    v
[2] _generator.md (LP-specific)
    |  User reads: step-by-step authoring guide for target LP
    |  Resolves: [BRACKET] decisions (author fills open variables)
    v
[3] Template fill
    |  {{MUSTACHE}} vars resolved by template engine or author
    |  YAML frontmatter populated: id, type, lp, quality, tags...
    v
[4] validate_examples.py
    |  Checks: schema compliance, density >= 0.80,
    |          frontmatter completeness, max_bytes, naming
    v
[5] Pool / Brain
       Artifact indexed for semantic retrieval (keywords + embeddings)
       Available for: agent hydration, template generation, reuse
```

---

## 4. LP Map — 12 Leverage Points

| LP | Domain | Layer | Primary Type | Schema | Gen | Tpl | Ex |
|----|--------|-------|-------------|--------|-----|-----|----|
| P01 | Knowledge | CORE | domain_kc | YES | YES | 3 | 7 |
| P02 | Model | CORE | agent | YES | YES | 1 | 4 |
| P03 | Prompt | CORE | prompt_template | YES | YES | 1 | 4 |
| P04 | Tools | CORE | skill | YES | YES | 1 | 3 |
| P05 | Output | QUALITY | output_schema | YES | YES | 1 | 0 |
| P06 | Schema | QUALITY | validation_schema | YES | YES | 0 | 0 |
| P07 | Evals | QUALITY | eval_metric | YES | YES | 0 | 0 |
| P08 | Architecture | QUALITY | arch_diagram | YES | YES | 0 | 0 |
| P09 | Config | SCALE | config_manifest | YES | YES | 0 | 0 |
| P10 | Memory | SCALE | memory_schema | YES | YES | 0 | 0 |
| P11 | Feedback | SCALE | feedback_loop | YES | YES | 0 | 0 |
| P12 | Orchestration | SCALE | workflow | YES | YES | 0 | 0 |

**Totals**: 12 schemas | 12 generators | 7 templates | 18 examples | 68 types

---

## 5. Schema → Type Hierarchy

```
_schema.yaml (per LP)
    |
    +-- primary type (1 per LP, has full generator + template)
    |     ex: P01 -> domain_kc
    |
    +-- secondary types (3-8 per LP, schema defined, no generator yet)
          ex: P01 -> rag_source, glossary_entry, context_doc,
                     embedding_config, few_shot_example
```

68 total types:
- CORE (P01-P04): 27 types
- QUALITY (P05-P08): 20 types
- SCALE (P09-P12): 21 types

---

## 6. Dual Output Pattern

Every artifact = 2 files:

```
p01_kc_ecommerce_br.md      # Human: dense markdown, version-controlled
p01_kc_ecommerce_br.yaml    # LLM: structured for embedding and retrieval
```

Exceptions:
- `_schema.yaml` — YAML only (machine contract)
- `_generator.md` — MD only (human authoring guide)

---

## 7. Meta-Hierarchy

```
archetypes/CODEX.md          DNA — all rules, anatomy, tiers (read first)
archetypes/MANDAMENTOS.md    10 immutable laws (never violate)
archetypes/META_TEMPLATE.md  Template that generates templates (shokunin)
archetypes/GLOSSARY.md       Terms: LP, density, dual output, shokunin
archetypes/ROADMAP.md        6 waves — what was built and what is next
archetypes/MIGRATION_MAP.md  9,916 files classified into LP buckets
archetypes/GOLDEN_CANDIDATES.md  22 priority candidates for migration
archetypes/DENSITY_REPORT.md     18 examples analyzed (density + tier)
archetypes/VALIDATION_REPORT.md  Chain test results (ATLAS, 2026-03-22)
```

---

## 8. Quality Gates

| Gate | Rule | Enforced by |
|------|------|------------|
| density_score | >= 0.80 | validate_examples.py |
| quality | >= 7.0 | frontmatter check |
| max_bytes | 4,096 | _schema.yaml per LP |
| frontmatter | 13 required fields | validate_schema.py |
| keywords | >= 3 | validate_examples.py |
| bullets | >= 3 | validate_examples.py |
| id == filename | exact match | validate_examples.py |
| prose limit | max 3 lines continuous | manual + linter |

---

*CEX Architecture v1.0 | 2026-03-22*
