<p align="center">
  <h1 align="center">CEX</h1>
  <p align="center"><strong>The typed knowledge system for LLM agents.</strong></p>
  <p align="center">Organize, compile, govern, and deploy everything your AI needs to know.</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v10.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/LLMs-Claude%20%7C%20GPT%20%7C%20Gemini%20%7C%20Ollama-8A2BE2" alt="LLMs">
  <img src="https://img.shields.io/badge/pillars-12-orange" alt="Pillars">
  <img src="https://img.shields.io/badge/artifact%20kinds-257-red" alt="Kinds">
  <img src="https://img.shields.io/badge/tools-113-brightgreen" alt="Tools">
</p>

---

## What is CEX

CEX is a typed taxonomy, compilation pipeline, and governance system for AI knowledge. It does for LLM artifacts what SQL did for data: structures them into discoverable, validated, governed types that any model can consume.

You describe **intent** in 8 tokens. CEX compiles it into a **governed prompt** with 100% dimensional coverage. It also **reverse-compiles** your knowledge base into any format: CLAUDE.md, .cursorrules, CustomGPT instructions, or MCP servers.

### Key capabilities

- **257 artifact kinds** across 12 pillars, each with typed frontmatter and validation
- **8-function pipeline** (8F): CONSTRAIN > BECOME > INJECT > REASON > CALL > PRODUCE > GOVERN > COLLABORATE
- **259 builder factories** with 3381 ISO files total (13 per kind: schema, prompt, examples, quality gate, ...)
- **Multi-provider routing**: Claude, GPT, Gemini, Ollama -- with health checks and automatic fallback
- **Reverse compiler**: export your knowledge base to CLAUDE.md, .cursorrules, CustomGPT JSON
- **Self-healing**: model updater detects stale versions, flywheel audits doc-vs-practice integrity
- **8 business nuclei** (N00-N07): independent AI agents that build, research, market, deploy, and govern

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/user/cex.git && cd cex

# 2. Install dependencies
pip install -r requirements.txt             # Core (pyyaml, tiktoken)
pip install -r requirements-llm.txt         # LLM providers (optional)

# 3. Bootstrap your brand
python _tools/cex_bootstrap.py              # Answer ~6 questions about your company
# Or: just type /init in any Claude session with CEX loaded

# 4. Build your first artifact
python _tools/cex_8f_runner.py "create knowledge card about product pricing" --kind knowledge_card --execute

# 5. Validate system health
python _tools/cex_doctor.py                 # Builder integrity (260 builders)
python _tools/cex_hooks.py validate-all     # Frontmatter validation
python _tools/cex_flywheel_audit.py audit   # Full system audit (109 checks)
```

See [QUICKSTART.md](QUICKSTART.md) for a detailed 5-minute walkthrough.

---

## The 8 Functions (8F Pipeline)

Every LLM interaction decomposes into 8 orthogonal functions:

| # | Function | What it does | Pipeline step |
|---|----------|-------------|---------------|
| F1 | **CONSTRAIN** | Load schema, limits, naming rules | `bld_schema` + `bld_config` |
| F2 | **BECOME** | Set identity, persona, boundaries | `bld_system_prompt` + `bld_manifest` |
| F3 | **INJECT** | Load knowledge, examples, memory | `bld_knowledge_card` + `bld_examples` + `bld_memory` |
| F4 | **REASON** | Plan approach, check GDP decisions | LLM reasoning + `cex_gdp.py` |
| F5 | **CALL** | Discover tools, check existing work | `bld_tools` + `cex_retriever.py` |
| F6 | **PRODUCE** | Generate artifact with full context | LLM call with token budget |
| F7 | **GOVERN** | Validate output against hard gates | Frontmatter, size, naming, schema |
| F8 | **COLLABORATE** | Save, signal, hand off | `signal_writer.py` + git commit |

```bash
# Run the full pipeline
python _tools/cex_8f_runner.py "your intent" --kind <kind> --execute

# Dry run (no LLM calls, shows what would happen)
python _tools/cex_8f_runner.py "your intent" --kind <kind> --dry-run --verbose
```

---

## Architecture

```
Layer 0 — BUILDERS       259 factories x 13 ISOs = 3381 artifact constructors
Layer 1 — PILLARS        12 pillars x 257 kinds = the taxonomy
Layer 2 — NUCLEI         8 business domains (N00 Genesis + N01-N07) = the organization
Layer 3 — PIPELINE       8F functions = the assembly line
Layer 4 — GOVERNANCE     hooks + doctor + quality gates = the quality bar
Layer 5 — TOOLS          113 Python CLI tools = the runtime
Layer 6 — WIRING         SDK modules + flywheel = the nervous system
```

## 12 Pillars

| Pillar | Name | Purpose |
|--------|------|---------|
| P01 | Knowledge | Knowledge cards, RAG sources, glossaries |
| P02 | Model | Agents, lenses, boot configs, mental models |
| P03 | Prompt | System prompts, templates, chains, CoT |
| P04 | Tools | Skills, MCP servers, hooks, plugins |
| P05 | Output | Response formats, parsers, naming rules |
| P06 | Schema | Input schemas, validators, interfaces |
| P07 | Evals | Benchmarks, smoke tests, rubrics |
| P08 | Architecture | Specs, patterns, diagrams |
| P09 | Config | Env configs, feature flags, runtime rules |
| P10 | Memory | Learning records, sessions, brain indexes |
| P11 | Feedback | Quality gates, guardrails, lifecycle rules |
| P12 | Orchestration | Workflows, DAGs, signals, handoffs |

---

## Multi-Provider Routing

CEX routes each nucleus to the best LLM for its job:

| Nucleus | Domain | Default Provider | Context | Tier |
|---------|--------|-----------------|---------|------|
| N01 | Research / Intelligence | Claude Sonnet 4.6 | 200K | Sonnet |
| N02 | Marketing / Copy | Claude Sonnet 4.6 | 200K | Sonnet |
| N03 | Engineering / Builder | Claude Opus 4.6 | 1M | **Opus** |
| N04 | Knowledge / RAG | Claude Sonnet 4.6 | 200K | Sonnet |
| N05 | Operations / DevOps | Claude Sonnet 4.6 | 200K | Sonnet |
| N06 | Commercial / Monetization | Claude Sonnet 4.6 | 200K | Sonnet |
| N07 | Orchestrator | Claude Opus 4.6 | 1M | **Opus** |

Budget-optimized: 2 Opus + 5 Sonnet. Pre-flight context compression via `cex_preflight.py` (local Ollama or Haiku) reduces token burn ~70% before nucleus boot.

Configuration lives in `.cex/config/nucleus_models.yaml` (single source of truth). All boot scripts, routing, and tools read from it.

```bash
# Check model health
python _tools/cex_model_updater.py --check

# Auto-discover and update when new models release
python _tools/cex_model_updater.py --full
```

---

## Reverse Compiler

CEX artifacts compile **down** to any format an LLM consumes:

```bash
python _tools/cex_compile.py --target claude-md      # -> CLAUDE.md (system prompt)
python _tools/cex_compile.py --target cursorrules     # -> .cursorrules
python _tools/cex_compile.py --target customgpt       # -> CustomGPT instructions JSON
```

This means CEX is the **source of truth** for your AI knowledge. Edit once in CEX, deploy everywhere.

---

## Dispatch & Multi-Nucleus

```bash
bash _spawn/dispatch.sh solo n03 "build agent card for sales"   # Single nucleus
bash _spawn/dispatch.sh grid MISSION_NAME                       # Up to 6 parallel
bash _spawn/dispatch.sh status                                  # Monitor all
bash _spawn/dispatch.sh stop                                    # Stop MY session only
bash _spawn/dispatch.sh stop n03                                # Stop specific nucleus
bash _spawn/dispatch.sh stop --all                              # Stop ALL (DANGEROUS)
```

---

## Tools (113 total)

### Core Pipeline
| Tool | Purpose |
|------|---------|
| `cex_8f_runner.py` | Full 8F pipeline (--execute, --dry-run, --verbose) |
| `cex_8f_motor.py` | Intent parser + classifier + plan |
| `cex_crew_runner.py` | Prompt composer: ISOs + memory + context |
| `cex_run.py` | Unified entry: intent -> discover -> plan -> prompt |
| `cex_compile.py` | .md -> .yaml compilation + reverse compiler |

### Discovery & Routing
| Tool | Purpose |
|------|---------|
| `cex_router.py` | Multi-provider routing with health + fallback |
| `cex_skill_loader.py` | Load builder ISOs in correct order |
| `cex_query.py` | TF-IDF builder discovery |
| `cex_retriever.py` | Semantic artifact similarity |
| `cex_model_updater.py` | Self-healing model version management |

### Memory & Knowledge
| Tool | Purpose |
|------|---------|
| `cex_memory_select.py` | Relevant memory injection (keyword + LLM) |
| `cex_memory_update.py` | Memory decay + append + prune |
| `cex_memory_types.py` | Memory classification (4 types) |
| `cex_memory_age.py` | Age-weighted ranking (linear decay) |
| `cex_token_budget.py` | Token counting + budget allocation |

### Quality & Governance
| Tool | Purpose |
|------|---------|
| `cex_doctor.py` | Builder health check (260 builders) |
| `cex_hooks.py` | Pre/post validation + git hooks |
| `cex_score.py` | Peer review scoring (--apply) |
| `cex_flywheel_audit.py` | Full system audit (109 checks) |
| `cex_gdp.py` | Guided Decision Protocol enforcement |

### Automation
| Tool | Purpose |
|------|---------|
| `cex_auto.py` | Self-healing flywheel (scan, plan, cycle) |
| `cex_evolve.py` | Autonomous artifact improvement loop |
| `cex_mission.py` | Goal -> decomposed artifacts |
| `cex_mission_runner.py` | Autonomous orchestration (waves -> grid) |
| `cex_flywheel_worker.py` | Nucleus gap analysis + 8F builds |

### Setup & Brand
| Tool | Purpose |
|------|---------|
| `cex_bootstrap.py` | First-run brand setup |
| `cex_init.py` | Initialize new CEX repo |
| `cex_forge.py` | Create typed artifact from template |
| `brand_inject.py` | Replace brand placeholders |
| `brand_validate.py` | Validate brand config |
| `brand_propagate.py` | Push brand context to all nuclei |

---

## Key Numbers

| Metric | Count |
|--------|-------|
| Artifact kinds | 257 |
| Builders (factories) | 259 |
| Builder ISO files | 13 per kind (3381 total) |
| Sub-agents | 259 |
| CLI tools | 113 |

> Counts are live-verifiable: `python _tools/cex_stats.py`.
| Pillars | 12 |
| Business nuclei | 8 (N00-N07) |
| 8F functions | 8 |
| Flywheel checks | 109 (100% WIRED) |

---

## Repo Structure

```
cex/
  .cex/                  Runtime config, brand, router, cache
    config/              nucleus_models.yaml, router_config.yaml
    brand/               Brand config + templates
    runtime/             Handoffs, signals, decisions, plans
    quality/             Audit reports, overnight logs
  _tools/                82 Python CLI tools (cex_*.py)
  _spawn/                Dispatch scripts (solo, grid, monitor, swarm)
  _docs/                 Whitepaper, architecture docs, specs
  archetypes/            Builder templates (260 builders x 13 ISOs)
    builders/            One directory per kind
    _shared/             Shared skills across all builders
  boot/                  Boot scripts per nucleus (claude/codex/gemini/ollama)
  cex_sdk/               SDK runtime (providers, models, memory, 78 modules)
  P01_knowledge/ ...     12 pillar directories
  P12_orchestration/
  N00_genesis/           Genesis archetype (template for nuclei)
  N01_intelligence/ ...  8 nucleus directories
  N07_admin/
  CLAUDE.md              LLM entry point
  QUICKSTART.md          5-minute getting started
  CONTRIBUTING.md        Contributor guide
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Every contribution must pass:

- Naming convention (`{layer}_{kind}_{topic}.{ext}`)
- Frontmatter validation (`id`, `kind`, `pillar`, `title`, `quality`)
- Quality gate (>= 8.0 for published artifacts)
- Pre-commit hooks (`python _tools/cex_hooks.py validate-all`)

---

## License

[MIT](LICENSE)

---

<p align="center">
  <em>SQL organized data. CEX organizes intelligence.</em>
</p>
