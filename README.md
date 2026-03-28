<p align="center">
  <h1 align="center">CEX</h1>
  <p align="center"><strong>A relational model for AI knowledge.</strong></p>
  <p align="center">Organize, compile, and govern everything your LLM needs to know.</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v5.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/LLMs-Claude%20%7C%20GPT%20%7C%20Gemini%20%7C%20Local-8A2BE2" alt="LLMs">
  <img src="https://img.shields.io/badge/pillars-12-orange" alt="Pillars">
  <img src="https://img.shields.io/badge/artifact%20types-78-red" alt="Types">
</p>

---

## What is CEX

CEX is a typed taxonomy and compilation pipeline for AI knowledge. It does for LLM artifacts what SQL did for data: structures them into discoverable, validated, governed types that any model can consume.

You describe **intent** in 8 tokens. CEX compiles it into a **1,200-token governed prompt** with 100% dimensional coverage. 150:1 amplification ratio.

---

## The Problem

- **92% of context is missing.** A human saying "write me an ad" provides ~8% of what an LLM needs. Identity, knowledge, reasoning method, output format, constraints, quality bar -- all absent.
- **Knowledge is unstructured.** Prompts live in flat files, Notion pages, or buried in code. No types, no validation, no discovery index.
- **No governance at rest.** Frameworks validate at runtime. Nobody validates the knowledge *before* it reaches the model.

## The Solution

- **8 typed dimensions.** Every LLM interaction decomposes into 8 orthogonal functions (BECOME, INJECT, REASON, CALL, PRODUCE, CONSTRAIN, GOVERN, COLLABORATE). CEX fills what the human didn't provide.
- **78 artifact types across 12 pillars.** Knowledge cards, agents, prompts, schemas, evals -- each with frontmatter, naming conventions, and validation rules. Like `CREATE TABLE` for AI.
- **Compilation pipeline.** Intent → Capture → Decompose → Hydrate → Compile → Envelope. 80% deterministic, 90% cheaper than full-LLM approaches.

---

## Architecture

```
                           CEX Architecture (5 Layers)

  +------------------------------------------------------------------+
  |  L0  BUILDERS        13 ISO files per type = factory for artifacts |
  |       archetypes/builders/{type}-builder/                         |
  +------------------------------------------------------------------+
  |  L1  PILLARS         12 pillars x 69 types = the taxonomy         |
  |       P01_knowledge/ ... P12_orchestration/                       |
  +------------------------------------------------------------------+
  |  L2  NUCLEI          7 business domains that consume artifacts    |
  |       N01_intelligence/ ... N07_admin/                            |
  +------------------------------------------------------------------+
  |  L3  PIPELINE        8 functions: BECOME > INJECT > REASON >      |
  |       CALL > PRODUCE > CONSTRAIN > GOVERN > COLLABORATE           |
  +------------------------------------------------------------------+
  |  L4  GOVERNANCE      Pre-commit hooks + cex doctor + quality gates |
  |       Naming rules, schema validation, density checks             |
  +------------------------------------------------------------------+


  Compilation Flow:

  Human Intent (8 tok)
       |
       v
  [ CAPTURE ] --> [ DECOMPOSE ] --> [ HYDRATE ] --> [ COMPILE ] --> [ ENVELOPE ]
    raw input    8 dimensions     fill from repo   assemble layers   wrap protocol
    (Python)     (LLM micro)      (Python+SQLite)  (Python+Jinja2)   (Python)
       |              |                |                 |                |
    0 cost        ~$0.001           0 cost            0 cost          0 cost
                                                                        |
                                                                        v
                                                              Governed Prompt (1200 tok)
                                                              Coverage: 8/8 dimensions
```

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/user/cex.git && cd cex

# 2. Initialize a new CEX repo for your company
python _tools/cex_init.py
# Answer 5 questions: name, domain, product, audience, tone
# Generates: 70 builders, 3 knowledge cards, 2 agents, full governance

# 3. Create an artifact
python _tools/cex_forge.py knowledge_card --topic "product pricing"
# Creates typed .md with frontmatter, placed in correct pillar/nucleus

# 4. Compile intent into a governed prompt
python _tools/cex_compile.py "write an ad for my Python course"
# Decomposes -> hydrates from repo -> assembles 8 layers -> outputs envelope

# 5. Validate repo health
python _tools/cex_doctor.py
# Checks: naming, frontmatter, orphans, density, schemas, duplicates
```

---

## The 8 Functions

Every LLM interaction -- from a single prompt to a multi-agent pipeline -- executes these 8 functions in order:

| # | Function | Question it answers | SQL Equivalent |
|---|----------|-------------------|----------------|
| 1 | **BECOME** | Who am I? (identity, persona) | `CREATE TABLE` |
| 2 | **INJECT** | What do I know? (context, knowledge) | `INSERT` |
| 3 | **REASON** | How do I think? (CoT, method) | `WHERE` clause |
| 4 | **CALL** | What tools can I use? | Stored procedure |
| 5 | **PRODUCE** | What do I output? (format, structure) | `SELECT` result |
| 6 | **CONSTRAIN** | What are the rules? (limits, schemas) | `CHECK` + `FK` |
| 7 | **GOVERN** | Is this good enough? (quality, evals) | `EXPLAIN` + audit |
| 8 | **COLLABORATE** | Who is next? (routing, handoff) | `JOIN` + federate |

Empirically validated: 337 artifacts across 12 major frameworks (LangChain, CrewAI, DSPy, AutoGen, etc.) map to these 8 functions with **94.7% coverage**. Zero unmapped AI functions in the remaining 5.3%.

---

## 12 Pillars

| Pillar | Name | Types | Purpose |
|--------|------|-------|---------|
| P01 | Knowledge | 6 | Knowledge cards, RAG sources, glossaries, embeddings |
| P02 | Model | 9 | Agents, lenses, boot configs, mental models, routers |
| P03 | Prompt | 10 | System prompts, templates, chains, CoT, meta-prompts |
| P04 | Tools | 10 | Skills, MCP servers, hooks, plugins, scrapers, connectors |
| P05 | Output | 4 | Response formats, parsers, formatters, naming rules |
| P06 | Schema | 7 | Input schemas, type definitions, validators, interfaces |
| P07 | Evals | 6 | Unit evals, smoke tests, benchmarks, golden tests, rubrics |
| P08 | Architecture | 5 | Satellite specs, patterns, laws, diagrams, component maps |
| P09 | Config | 5 | Env configs, paths, permissions, feature flags, runtime rules |
| P10 | Memory | 4 | Runtime state, brain indexes, learning records, sessions |
| P11 | Feedback | 5 | Quality gates, bugloops, lifecycle rules, guardrails |
| P12 | Orchestration | 7 | Workflows, DAGs, spawn configs, signals, handoffs, crews |

Every artifact has typed frontmatter (`id`, `kind`, `pillar`, `title`), lives at a semantic path, and follows the naming grammar: `{layer}_{kind}_{topic}.{ext}`.

---

## Tools

| Tool | Usage | Purpose |
|------|-------|---------|
| `cex_init.py` | `python _tools/cex_init.py` | Bootstrap a new CEX repo (5 questions, 30 seconds) |
| `cex_forge.py` | `python _tools/cex_forge.py <kind> --topic <t>` | Create a new typed artifact with frontmatter |
| `cex_compile.py` | `python _tools/cex_compile.py "<intent>"` | Compile human intent into governed LLM prompt |
| `cex_pipeline.py` | `python _tools/cex_pipeline.py` | Run the full 8-function pipeline |
| `cex_doctor.py` | `python _tools/cex_doctor.py` | Diagnose repo health (naming, schemas, orphans) |
| `cex_feedback.py` | `python _tools/cex_feedback.py` | Process user feedback into knowledge updates |
| `cex_index.py` | `python _tools/cex_index.py` | Regenerate INDEX.md from repo contents |
| `distill.py` | `python _tools/distill.py` | Compile .md artifacts to .yaml/.json |
| `validate_builder.py` | `python _tools/validate_builder.py <builder>` | Validate builder ISO files (13-file checklist) |
| `validate_schema.py` | `python _tools/validate_schema.py` | Validate all _schema.yaml files |
| `bootstrap.py` | `python _tools/bootstrap.py` | Full scaffold: nuclei + pillars + types |
| `bump_version.py` | `python _tools/bump_version.py` | Semantic version bump across repo |
| `setup_hooks.sh` | `bash _tools/setup_hooks.sh` | Install pre-commit governance hooks |

---

## CEX vs Alternatives

| Capability | Manual Prompting | Agent Frameworks | Knowledge Tools | **CEX** |
|-----------|-----------------|------------------|-----------------|---------|
| Structured types | No | No | Partial | **69 types, 12 pillars** |
| Discovery index | No | No | Tag-based | **Semantic naming = O(1) lookup** |
| Dimensional coverage | ~8% | ~30% | ~20% | **100% (8/8 functions)** |
| Compilation pipeline | No | Runtime only | No | **5-phase, 80% deterministic** |
| Governance at rest | No | No | No | **Pre-commit + doctor + gates** |
| Schema validation | No | Runtime | Partial | **Frontmatter + _schema.yaml** |
| Self-improving | No | No | Manual | **Feedback loop (few-shot, constraints)** |
| Model-agnostic | N/A | Framework-locked | N/A | **Claude, GPT, Gemini, local** |
| Cost per compilation | Full LLM | Full LLM | N/A | **90% cheaper (hybrid engine)** |

---

## How It Works (End to End)

```
Human: "write an ad for my Python course"      <- 8 tokens, 5.6% coverage

CEX:   CAPTURE   -> 8 tokens captured
       DECOMPOSE -> 8 dimensions scored (BECOME: 0%, INJECT: 20%, ...)
       HYDRATE   -> fills from repo:
                    BECOME:    bld_system_prompt_copywriter.md
                    INJECT:    knowledge_card_python_course.md + 3 few_shots
                    REASON:    AIDA framework (Attention-Interest-Desire-Action)
                    PRODUCE:   tpl_response_format_ad.md
                    CONSTRAIN: max 2200 chars, casual tone, emoji max 3
                    GOVERN:    clarity >= 8, persuasion >= 9
       COMPILE   -> 8 layers assembled in function order
       ENVELOPE  -> system prompt + context + user prompt + routing metadata

Output: 1,200-token governed prompt             <- 100% coverage, 150:1 amplification
```

The brain learns from every interaction. Successful outputs become few-shot examples. Negative feedback updates constraints. Quality scores improve routing. Day 1: functional. Day 30: expert.

---

## Repo Structure

```
cex/
  _docs/               Whitepaper, architecture, quickstart
  _tools/              CLI tools (init, forge, compile, doctor, ...)
  archetypes/          Builder templates (13 ISO files per type)
  packages/            Distributable packages
  P01_knowledge/       Pillar: knowledge cards, RAG, glossaries
  ...
  P12_orchestration/   Pillar: workflows, DAGs, signals
  N01_intelligence/    Nucleus: research domain
  ...
  N07_admin/           Nucleus: administration domain
  INDEX.md             Auto-generated artifact index
  LLM_PIPELINE.md     8 functions specification
  CLAUDE.md            LLM entry point (Claude)
  CONTRIBUTING.md      Contributor guide
```

---

## Key Numbers

| Metric | Count |
|--------|-------|
| Pillars | 12 |
| Artifact types | 69 |
| Business nuclei | 7 |
| LLM functions | 8 |
| Builder ISO files | 13 per type |
| Examples | 179 |
| Templates | 69 |
| Compiled artifacts | 121 |
| Active builders | 69 / 69 |
| CLI tools | 13 |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on artifact creation, builder development, and quality gates.

Every contribution must pass:
- Naming convention (`{layer}_{kind}_{topic}.{ext}`)
- Frontmatter validation (`id`, `kind`, `pillar`, `title`)
- Density check (>= 0.80)
- Quality gate (>= 7.0 for experimental, >= 8.0 for published)

---

## Documentation

| Document | Description |
|----------|-------------|
| [Whitepaper](/_docs/WHITEPAPER_CEX.md) | Full thesis: the SQL analogy, proofs, market gap |
| [Architecture](/_docs/ARCHITECTURE.md) | 5-layer structure, schemas, governance rules |
| [LLM Pipeline](LLM_PIPELINE.md) | 8 functions specification |
| [Index](INDEX.md) | Complete artifact inventory |

---

## License

[MIT](LICENSE)

---

<p align="center">
  <em>SQL organized data. CEX organizes intelligence.</em>
</p>
