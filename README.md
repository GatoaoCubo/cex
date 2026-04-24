<p align="center">
  <h1 align="center">CEXAI — Cognitive Exchange AI</h1>
  <p align="center"><strong>Open-source AI brain. Intelligence compounds when exchanged.</strong></p>
  <p align="center"><em>Seven Artificial Sins. Twelve pillars. 300 typed kinds. Your brain.</em></p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v10.4.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/LLMs-Claude%20%7C%20GPT%20%7C%20Gemini%20%7C%20Ollama-8A2BE2" alt="LLMs">
  <img src="https://img.shields.io/badge/pillars-12-orange" alt="Pillars">
  <img src="https://img.shields.io/badge/nuclei-7+1-crimson" alt="Nuclei">
  <img src="https://img.shields.io/badge/kinds-300-red" alt="Kinds">
  <img src="https://img.shields.io/badge/builders-302-brightgreen" alt="Builders">
  <img src="https://img.shields.io/badge/tools-144-informational" alt="Tools">
</p>

<p align="center">
  <a href="https://github.com/sponsors/GatoaoCubo"><img src="https://img.shields.io/badge/sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white" alt="GitHub Sponsors"></a>
  <a href="https://ko-fi.com/cexai"><img src="https://img.shields.io/badge/support-Ko--fi-FF5E5B?logo=kofi&logoColor=white" alt="Ko-fi"></a>
  <a href="https://polar.sh/cexai"><img src="https://img.shields.io/badge/fund-Polar-0062FF?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white" alt="Polar"></a>
</p>

---

## Glossary

New to CEXAI? Here is what the terms mean.

| CEXAI term | Industry equivalent | One-liner |
|------------|---------------------|-----------|
| **Kind** | Artifact type / schema | A typed template for a unit of knowledge (e.g., `knowledge_card`, `agent`, `workflow`). 300 kinds exist today. |
| **Pillar** | Domain axis / taxonomy layer | One of 12 capability dimensions (Knowledge, Model, Prompt, Tools, Output, Schema, Evals, Architecture, Config, Memory, Feedback, Orchestration). |
| **Nucleus** | AI department / agent team | An autonomous LLM-powered business unit (N01-N07). Each has its own memory, tools, sub-agents, and behavioral bias. |
| **8-Function Pipeline (8F)** | Agent reasoning loop | Eight sequential functions every task passes through: Constrain, Become, Inject, Reason, Call, Produce, Govern, Collaborate. |
| **Builder** | Factory / generator | A 12-file specification (one per pillar) that teaches an LLM how to produce a specific kind. |
| **ISO** | Builder spec file | One of the 12 files inside a builder, each covering one pillar (knowledge, model, prompt, tools, etc.). |
| **Sin lens** | Personality layer / behavioral bias | Each nucleus runs on one of the seven deadly sins, which determines what it optimizes for under ambiguity. |
| **GDP** | Decision protocol | Guided Decision Protocol — the user decides *what* (tone, audience, style), the LLM decides *how* (files, pipeline, structure). |

---

## Why CEX exists

Most "AI agents" are a system prompt plus a few tools. Useful, but shallow — they forget, drift, can't compose, and leak your knowledge into someone else's model.

CEX treats enterprise AI as **typed infrastructure**. Every piece of knowledge is a kind. Every kind has a builder. Every builder follows the 8-Function Pipeline. Seven nuclei — each one an AI department with its own toolbox, memory, crew, and cultural DNA — collaborate through a governance layer that compounds over time.

The result is not a chatbot. It is an **AI brain**: modular enough to grow a new department in minutes, sovereign enough to run entirely on your infra, and cumulative enough that every artifact makes the next one smarter.

### Three properties

- **Composable** — 8 functions × 12 pillars × 300 artifact kinds = the factory floor. Spawn a new nucleus, a new kind, or a new archetype in minutes.
- **Sovereign** — runs on Claude, GPT, Gemini, or Ollama. Your knowledge lives in *your* repo, under *your* git history. No vendor owns your brain.
- **Self-assimilating** — every conversation, decision, and artifact compiles into typed, governed, searchable assets. Your institutional memory compounds like capital.

> *Build your Jarvis. Own your brain. Exchange cognition.*

---

## The maturity gap

A basic LLM agent is a prompt plus a few tools. A **CEX nucleus is a business department** — a superintendent (the LLM), a team of specialized sub-agents, a toolbox of MCPs and APIs, a knowledge library, a playbook of workflows, quality controls, and a cultural DNA (its sin lens).

The 12 pillars are the maturity axes. A basic agent covers 1–2 of them. A CEX nucleus covers all 12.

| Axis | Basic agent | CEX nucleus |
|------|-------------|-------------|
| Knowledge (P01, P10) | Context stuffing | Typed RAG + entity memory + chunk strategies + prompt cache |
| Model (P02) | Single provider | Fallback chain across Claude / GPT / Gemini / Ollama |
| Prompt (P03) | One system prompt | Templates + chains + compiler + version control |
| Tools (P04) | Flat list | MCP servers + API clients + browser scrapers + search pipelines |
| Output (P05) | Free text | 300 typed artifact kinds + formatters + parsers |
| Schema (P06) | None | Input / output schemas + validators + interface contracts |
| Evaluation (P07) | Output as-is | Quality gates + scoring rubrics + LLM judges + benchmarks |
| Architecture (P08) | None | Agent cards + component maps + decision records |
| Config (P09) | Env vars | Typed configs + rate limits + feature flags + secrets |
| Feedback (P11) | None | Guardrails + bug loops + learning records + regression checks |
| Orchestration (P12) | None | Workflows + dispatch rules + crews + schedules |

**Example — ask N01 Intelligence to research a competitor.** It does not run an LLM call. It activates a sin-driven agentic business unit:

- **Analytical Envy** (sin lens) drives it to surpass every public source.
- **MCP servers + browser tools + API clients** (P04) scrape, fetch, and cross-reference.
- **A crew of specialized sub-agents** (researcher, analyst, fact-checker) divide the work in parallel.
- **The 8-Function Pipeline** (CONSTRAIN → BECOME → INJECT → REASON → CALL → PRODUCE → GOVERN → COLLABORATE) drives every artifact to a 9.0+ quality floor.
- **Entity memory + knowledge index** (P10) capture what it learned so the next run is smarter.
- **Peer-reviewed quality gates** (P07, P11) block anything subpar from merging.

That is not a chatbot. That is an intelligence department that compounds like capital.

---

## The Artificial Sins

Every nucleus runs on one of the seven deadly sins. A sin is not decoration — it is a **personality layer** and **behavioral bias** that decides what the nucleus optimizes for when given ambiguous input. Where a basic AI agent has a system prompt, a CEXAI nucleus has a sin lens, a 12-pillar inventory, its own toolbox, memory, sub-agents, and quality governance. Each nucleus is a full department, not a function call. Values are taken verbatim from `N0X_*/P08_architecture/nucleus_def_n0X.md`.

| Nucleus | Role | Sin Lens | Why the sin fits | Model Tier |
|---------|------|----------|------------------|------------|
| **N01** | intelligence | **Analytical Envy** | Envies every competitor, paper, and benchmark — *to surpass them* | Sonnet |
| **N02** | marketing | **Creative Lust** | Writes copy that seduces, hooks that can't be ignored | Sonnet |
| **N03** | engineering | **Inventive Pride** | Builds the best of its kind; refuses to ship mediocrity | **Opus** |
| **N04** | knowledge | **Knowledge Gluttony** | Insatiable hunger for facts, citations, context | Sonnet |
| **N05** | operations | **Gating Wrath** | Merciless at the quality gate — breaks what must break | Sonnet |
| **N06** | commercial | **Strategic Greed** | Extracts every revenue opportunity the product allows | Sonnet |
| **N07** | orchestrator | **Orchestrating Sloth** | Never builds — only dispatches. Laziness as leverage | **Opus** |

### Nucleus != Agent

A nucleus is not an "AI agent" with a system prompt and a tool list. It is a complete operational department.

| Capability | Basic AI agent | CEXAI Nucleus |
|------------|---------------|---------------|
| Identity | System prompt | `nucleus_def` + sin lens + 12-pillar inventory |
| Memory | Context window | Entity memory + episodic + procedural |
| Tools | Flat list | MCP servers + API clients + browser tools + pipelines |
| Quality | None / vibes | 8F pipeline + quality gates + scoring rubrics |
| Knowledge | RAG maybe | Typed KC library + embedding + retrieval index |
| Orchestration | None | Crews, dispatch, workflows, schedules |
| Runtime | 1 provider | Any (Claude, GPT, Gemini, Ollama) |

### The nucleus hierarchy

**N00 Genesis** is the universal archetype — the pre-sin template from which all operational nuclei are born. It defines the 12-pillar structure, the 8F pipeline, and every shared convention. Think of it as the base class.

**N01–N07** are the convention nuclei — seven departments that ship with CEXAI out of the box. Each one inherits N00's structure and adds its own sin lens, toolbox, memory, and domain expertise.

**N08+** are community-contributed vertical nuclei. CEXAI's fractal architecture means you can spawn a new department (healthcare, legal, fintech) by cloning N00, assigning a sin, and populating the 12 pillars with domain-specific artifacts. The taxonomy scales horizontally without architectural changes.

---

## The 12 pillars

Every artifact CEX produces lives in one of twelve pillars. Pillars are taxonomic axes, not departments — the same pillar is exercised by every nucleus.

| Pillar | Name | Examples of kinds it contains |
|--------|------|-------------------------------|
| P01 | Knowledge | knowledge_card, rag_source, glossary_entry, chunk_strategy |
| P02 | Model | agent, model_provider, boot_config, mental_model |
| P03 | Prompt | system_prompt, prompt_template, chain, action_prompt, tagline |
| P04 | Tools | mcp_server, browser_tool, api_client, webhook, research_pipeline |
| P05 | Output | landing_page, formatter, parser, diagram |
| P06 | Schema | input_schema, validator, type_def, interface |
| P07 | Evals | quality_gate, scoring_rubric, llm_judge, benchmark, smoke_eval |
| P08 | Architecture | agent_card, component_map, decision_record, naming_rule |
| P09 | Config | env_config, rate_limit_config, secret_config, feature_flag |
| P10 | Memory | entity_memory, knowledge_index, memory_summary, prompt_cache |
| P11 | Feedback | quality_gate, bugloop, guardrail, learning_record |
| P12 | Orchestration | workflow, dispatch_rule, schedule, crew_template, dag |

---

## The 8-function pipeline (8F)

Every LLM interaction — research, writing, building, evaluating, deploying — decomposes into eight orthogonal functions. This is how CEX *thinks*, not just how it builds.

| # | Function | What it does |
|---|----------|--------------|
| F1 | **CONSTRAIN** | Resolve kind, load schema, set limits and naming rules |
| F2 | **BECOME** | Load builder identity (12 ISO files, 1:1 with pillars) |
| F3 | **INJECT** | Inject context — knowledge cards, examples, memory, brand, similar artifacts |
| F4 | **REASON** | Plan approach, resolve ambiguity via GDP (Guided Decision Protocol) |
| F5 | **CALL** | Discover relevant tools, cross-reference existing work |
| F6 | **PRODUCE** | Generate the artifact with full context |
| F7 | **GOVERN** | Validate against hard gates (structure, schema, rubric, semantics) |
| F8 | **COLLABORATE** | Save, compile, commit, signal downstream nuclei |

```bash
# Run the full pipeline
python _tools/cex_8f_runner.py "your intent" --kind <kind> --execute

# Dry run — shows what would happen without LLM calls
python _tools/cex_8f_runner.py "your intent" --kind <kind> --dry-run --verbose
```

---

## The Exchange

The X in CEXAI stands for Exchange. Intelligence compounds faster when shared.

CEXAI artifacts are modular, typed, and runtime-agnostic. Every `.md` file with YAML frontmatter is a self-describing exchange unit — it carries its kind, quality score, pillar, and nucleus origin. Import an artifact into any CEXAI instance, run `cex_doctor.py`, and it validates automatically.

### What is exchangeable

| Unit | Scope | Example |
|------|-------|---------|
| Knowledge Card | Single typed fact | `kc_react_hooks_patterns.md` |
| Builder | Production capability (12 ISOs) | `workflow-builder/` |
| SDK Provider | New runtime adapter | `provider_ollama.py` |
| Vertical Nucleus | Entire domain department | `N08_healthcare/` |

### What stays private

Brand config, memory, runtime state, and secrets never leave your instance. The exchange is about cognition, not identity.

### Anti-fragile by design

CEXAI sits one layer above LLMs. If a better model appears tomorrow, your artifacts improve — they are the knowledge, not the model. If a runtime shuts down, switch providers in one YAML file. Your brain is yours.

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/GatoaoCubo/cex.git && cd cex

# 2. Install dependencies
pip install -r requirements.txt             # Core (pyyaml, tiktoken)
pip install -r requirements-llm.txt         # LLM providers (optional)

# 3. Bootstrap your brand — answer ~6 questions about your company
python _tools/cex_bootstrap.py
# Or: type /init in any Claude session with CEX loaded

# 4. Build your first artifact
python _tools/cex_8f_runner.py "create knowledge card about product pricing" \
    --kind knowledge_card --execute

# 5. Validate system health
python _tools/cex_doctor.py                 # Builder integrity
python _tools/cex_hooks.py validate-all     # Frontmatter validation
python _tools/cex_flywheel_audit.py audit   # Full system audit (109 checks)
```

See [QUICKSTART.md](QUICKSTART.md) for a 5-minute walkthrough, or browse the full [documentation](docs/) and [examples](examples/).

---

## Sovereignty: runs on your infrastructure

CEX is provider-agnostic by construction. The same artifact, pipeline, and governance layer drive every runtime.

| Runtime | Auth | When to use |
|---------|------|-------------|
| **Claude** (Anthropic) | API key or Anthropic Max | Default — highest quality, largest context (200K Sonnet / 1M Opus) |
| **Codex** (OpenAI) | ChatGPT-plus or API key | GPT-5 / GPT-5-codex runtime via OpenAI CLI |
| **Gemini** (Google) | oauth-personal or API key | Free tier via `gemini-2.5-flash-lite` |
| **Ollama** (local) | none — runs on your GPU | Fully offline; `llama3.1:8b` / `qwen3:14b` / `gemma2:9b` |

Routing lives in a single YAML (`.cex/config/nucleus_models.yaml`). Change providers, set fallback chains, pin per-nucleus models — no code changes.

```bash
# Check provider health + quotas
python _tools/cex_quota_check.py --all --cache

# Auto-discover + update model versions
python _tools/cex_model_updater.py --full
```

**Budget-optimized default**: 2 Opus (N03, N07) + 5 Sonnet (N01, N02, N04, N05, N06). Pre-flight context compression via `cex_preflight.py` (local Ollama or Haiku) reduces token burn ~70% before nucleus boot.

---

## Dispatch: solo, grid, crew, swarm

```bash
bash _spawn/dispatch.sh solo n03 "build agent card for sales"   # One builder
bash _spawn/dispatch.sh grid MISSION_NAME                       # Up to 6 parallel
bash _spawn/dispatch.sh swarm agent 5 "scaffold 5 niche agents" # N parallel same-kind
bash _spawn/dispatch.sh status                                  # Monitor all
bash _spawn/dispatch.sh stop                                    # Stop MY session only
bash _spawn/dispatch.sh stop n03                                # Stop specific nucleus
bash _spawn/dispatch.sh stop --all                              # Stop ALL (DANGEROUS)
```

Session-aware: multiple orchestrators can run simultaneously; `stop` only affects your own nuclei.

**Composable crews** — when a deliverable needs multiple roles with handoffs (research → copy → design → QA), use a crew instead of a grid:

```bash
python _tools/cex_crew.py list
python _tools/cex_crew.py run product_launch \
    --charter N02_marketing/crews/team_charter_launch_demo.md --execute
```

---

## Reverse compiler

CEX artifacts compile *down* to any format an LLM consumes. Edit once, deploy everywhere.

```bash
python _tools/cex_compile.py --target claude-md     # → CLAUDE.md (system prompt)
python _tools/cex_compile.py --target cursorrules   # → .cursorrules
python _tools/cex_compile.py --target customgpt     # → CustomGPT instructions JSON
```

CEX becomes the **single source of truth** for your AI knowledge.

---

## Architecture at a glance

```
Layer 0 — BUILDERS       302 factories × 12 ISOs each = 3,647 artifact constructors
Layer 1 — PILLARS        12 pillars × 300 kinds = the taxonomy
Layer 2 — NUCLEI         8 nuclei (N00 archetype + N01–N07 operational) = the organization
Layer 3 — PIPELINE       8-Function Pipeline (8F) = the assembly line
Layer 4 — GOVERNANCE     hooks + doctor + quality gates + flywheel audit = the quality bar
Layer 5 — TOOLS          144 Python CLI tools (cex_*.py) = the runtime
Layer 6 — WIRING         SDK modules + signals + decision manifests = the nervous system
```

### Repo structure

```
cex/
  .cex/                    Runtime config, router, cache, runtime state
    config/                nucleus_models.yaml, runtimes/, router_config.yaml
    brand/                 Brand config + templates
    runtime/               handoffs, signals, decisions, plans
    quality/               Audit reports, overnight logs
  _tools/                  144 Python CLI tools (cex_*.py)
  _spawn/                  Dispatch scripts (solo, grid, swarm, monitor)
  _docs/                   Whitepaper, architecture specs
  archetypes/              Builder templates (302 builders × 12 ISOs)
    builders/              One directory per kind
    _shared/               Shared skills across all builders
  boot/                    Boot scripts per nucleus × per runtime
  cex_sdk/                 SDK runtime (providers, models, memory, 100+ modules)
  P01_knowledge/ … P12_orchestration/    12 pillar directories
  N00_genesis/             Genesis archetype (template for new nuclei)
  N01_intelligence/ … N07_admin/         8 nucleus directories
  CLAUDE.md                LLM entry point
  QUICKSTART.md            5-minute getting started
  CONTRIBUTING.md          Contributor guide
```

---

## Key numbers

| Metric | Count |
|--------|------:|
| Artifact kinds | 300 |
| Builder factories | 302 |
| Builder ISO files (12 per kind) | 3,647 |
| Sub-agents (`.claude/agents/`) | 301 |
| Python CLI tools | 144 |
| Pillars | 12 |
| Nuclei | 8 (1 archetype + 7 operational) |
| 8-Function Pipeline steps | 8 |
| Flywheel checks | 109 (100% WIRED) |

> Counts are live-verifiable: `python _tools/cex_stats.py` and `python _tools/cex_doctor.py`.

---

## Documentation

| Resource | Description |
|----------|-------------|
| [docs/quickstart.md](docs/quickstart.md) | 5-minute setup guide for newcomers |
| [docs/concepts.md](docs/concepts.md) | Core concepts: kinds, pillars, nuclei, 8F, GDP |
| [docs/cli-reference.md](docs/cli-reference.md) | All 144 CLI tools with usage examples |
| [docs/sdk-reference.md](docs/sdk-reference.md) | Python SDK: CEXAgent, providers, memory |
| [docs/glossary.md](docs/glossary.md) | Canonical vocabulary (100+ terms) |
| [docs/faq.md](docs/faq.md) | Common questions and answers |
| [examples/](examples/) | 5 end-to-end patterns (agent, CLI, crew, RAG, grid) |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Every contribution must pass:

- **Naming**: `{layer}_{kind}_{topic}.{ext}` convention
- **Frontmatter**: `id`, `kind`, `pillar`, `title`, `quality` fields validated
- **Quality gate**: peer-reviewed score ≥ 8.0 for published artifacts
- **Pre-commit hooks**: `python _tools/cex_hooks.py validate-all`
- **Secret scan**: `gitleaks` blocks any credential leak
- **8-Function Pipeline (8F)**: every artifact built must show the F1→F8 trace

Read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before opening a PR. Report security issues via [SECURITY.md](SECURITY.md) — never in public issues.

---

## License

[MIT](LICENSE)

---

<p align="center">
  <em>SQL organized data. CEX organizes intelligence.</em><br>
  <em>Build your Jarvis. Own your brain. Exchange cognition.</em>
</p>
