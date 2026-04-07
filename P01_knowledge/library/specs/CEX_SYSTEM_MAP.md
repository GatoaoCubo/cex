---
id: spec_cex_system_map
kind: context_doc
pillar: P01
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
title: "CEX System Map: Full Fractal Architecture Census"
quality: 9.1
tags: [system-map, architecture, fractal, census, meta]
tldr: "Complete map of CEX 7-layer fractal architecture: 4740+ files, 115 kinds, 12 pillars, 8 nuclei, 50 tools"
input_taxonomy: "symbiosis_audit_v1 -- full-repo cascade verification with wiring and collaboration mapping"
---

# CEX System Map v1.0

## Census

| Layer | Items | Files | Purpose |
|-------|-------|-------|---------|
| L0 Genesis+Config | 1 mold + 87 configs + 13 boot + 5 spawn | 106 | Bootstrap, routing, runtime state |
| L1 Pillars (P01-P12) | 12 pillars x (schema+compiled+examples+templates) | 1196 | Universal typed knowledge store |
| L2 Nuclei (N01-N07) | 7 nuclei x ~13 subdirs (mirrors P01-P12) | 508 | Domain-specific fractal instances |
| L3 Archetypes | 107 builders x 13 ISOs + 3 shared + 109 sub-agents | 1527 | Factories that produce artifacts |
| L4 Knowledge Library | 108 kind KCs + 79 domain KCs + 9 specs | 199 | Deep knowledge for reasoning |
| L5 Tools | 49 cex_* + 50 helpers + 56 SDK modules | 155 | Runtime execution engine |
| L6 Governance | 9 rules + 13 commands + 71 learning records | 94 | Quality, decisions, memory |
| L7 Documentation | 55 _docs + 8 root docs | 63 | Human-facing knowledge |
| **TOTAL** | | **4710** | |

---

## L0: Genesis and Config

```
N00_genesis/           Mold template (all nuclei derive from this)
.cex/
  brand/               Brand identity (brand_config.yaml)
  config/              System config
  runtime/
    decisions/         GDP manifests (user-scope decisions)
    handoffs/          Inter-nucleus task handoffs
    signals/           Completion/error signals
    pids/              Active process tracking
    locks/             Concurrency control
    plans/             Mission plans
    outputs/           Builder outputs
    archive/           Compacted sessions
  memory/              Persistent memory store
  learning_records/    71 post-execution learning records
  experiments/         A/B test results
  quality/             Quality snapshots
  router_config.yaml   Multi-provider routing (4 providers x 7 nuclei)
  kinds_meta.json      115 kind definitions (registry)
boot/
  cex.cmd              N07 orchestrator boot
  n0{1-6}.cmd          Per-nucleus boot scripts
_spawn/
  dispatch.sh          Unified dispatch (solo/grid/status/stop)
  spawn_*.ps1          Windows PowerShell grid execution
```

### Wiring: L0 feeds
- L2 (Nuclei): boot scripts start nuclei; router_config routes them
- L5 (Tools): cex_router.py reads router_config; cex_gdp.py reads decisions/
- L6 (Governance): .claude/rules/ reference runtime state

---

## L1: Pillars (P01-P12) -- Universal Knowledge Store

| Pillar | Function | Files | Domain |
|--------|----------|-------|--------|
| P01_knowledge | INJECT | 710 | Raw knowledge, KCs, embeddings, retrieval |
| P02_model | BECOME | 53 | Agent identity, persona, model cards |
| P03_prompt | CONSTRAIN | 53 | System prompts, instructions, templates |
| P04_tools | CALL | 141 | Skills, tools, hooks, plugins, MCP |
| P05_output | GOVERN | 17 | Formatters, parsers, validators |
| P06_schema | CONSTRAIN | 30 | Type defs, input schemas, enums |
| P07_evals | GOVERN | 36 | Benchmarks, evals, scoring rubrics |
| P08_architecture | INJECT | 34 | Agent cards, patterns, diagrams |
| P09_config | GOVERN | 25 | Env config, feature flags, permissions |
| P10_memory | INJECT | 32 | Entity memory, session state |
| P11_feedback | GOVERN | 28 | Guardrails, quality gates, lifecycle |
| P12_orchestration | PRODUCE | 37 | Workflows, DAGs, signals, handoffs |

Each pillar: _schema.yaml + compiled/ + examples/ + templates/ + README.md

### Wiring
- L2: Each nucleus mirrors pillar structure (N03/prompts = P03)
- L3: Builders READ pillar schemas, WRITE to pillar compiled/
- L4: KCs describe the kinds that populate each pillar
- L5: cex_prompt_layers.py scans compiled/; cex_compile.py manages state

### Artifact Lifecycle Cascade
```
P06 schema --> P03 prompt --> P04 tools --> P11 feedback --> P12 orchestration
  defines      instructs     executes     validates       coordinates
```

---

## L2: Nuclei (N01-N07) -- Domain Fractal Instances

| Nucleus | Domain | Provider | Files |
|---------|--------|----------|-------|
| N01_intelligence | Research/analysis | Gemini 2.5-pro | 74 |
| N02_marketing | Marketing/copy | Claude Sonnet | 89 |
| N03_engineering | Build/create | Claude Opus | 88 |
| N04_knowledge | Knowledge/docs | Gemini 2.5-pro | 81 |
| N05_operations | Code/test/deploy | Codex GPT | 51 |
| N06_commercial | Brand/monetization | Claude Sonnet | 61 |
| N07_admin | Orchestration | Pi Opus | 64 |

Each nucleus has ~13 subdirs mirroring P01-P12:
agents/ architecture/ compiled/ config/ feedback/ knowledge/
memory/ orchestration/ output/ prompts/ quality/ schemas/ tools/

### Inter-Nucleus Cascade
```
N07 orchestrator --> dispatch.sh --> N01-N06 workers
                 <-- signal_writer <-- completion/error signals
                 <-- handoff files <-- inter-nucleus task transfers
```

---

## L3: Archetypes -- Factories That Produce Artifacts

```
archetypes/builders/
  _builder-builder/     Meta-builder (builds new builders)
  _shared/              3 shared skills (all builders inherit):
    skill_guided_decisions.md
    skill_memory_update.md
    skill_verification_protocol.md    [NEW from OpenClaude]
  {kind}-builder/       107 builders, each with 13 ISOs:
    bld_instruction     HOW to build (phases, steps)
    bld_schema          WHAT fields are required
    bld_output_template WHAT the output looks like
    bld_quality_gate    HOW to validate (HARD+SOFT gates)
    bld_examples        GOLDEN and ANTI examples
    bld_knowledge_card  DEEP knowledge about this kind
    bld_system_prompt   IDENTITY for the builder agent
    bld_config          Builder configuration
    bld_manifest        Builder metadata
    bld_architecture    Architectural context
    bld_collaboration   How this builder works with others
    bld_memory          Builder-specific memories
    bld_tools           Tools available to this builder

.claude/agents/         109 sub-agent definitions (from cex_materialize.py)
```

### 8F Pipeline Through ISOs
```
bld_schema(F1 CONSTRAIN) --> bld_system_prompt(F2 BECOME)
  --> bld_knowledge_card+examples(F3 INJECT)
    --> bld_instruction(F4 REASON)
      --> bld_tools(F5 CALL)
        --> bld_output_template(F6 PRODUCE)
          --> bld_quality_gate(F7 GOVERN)
            --> bld_collaboration(F8 COLLABORATE)
```

---

## L4: Knowledge Library

```
P01_knowledge/library/
  kind/           108 kind KCs (1 per kind)
  domain/         79 domain KCs:
    frameworks/     Framework analysis (LangChain, CrewAI, DSPy)
    patterns/       Architectural patterns
    llm_patterns/   LLM-specific patterns
    anti_patterns/  Known failure modes
    operations/     Operational knowledge
    orchestration/  Orchestration patterns
    meta/           Meta-knowledge about knowledge
  specs/          9 spec documents + system map
  sources/        External knowledge sources
```

### Knowledge Cascade
```
External sources --> domain KCs --> kind KCs --> builder bld_knowledge_card
  --> composed prompts (cex_crew_runner) --> LLM context window
```

---

## L5: Tools -- Runtime Engine

### 49 cex_*.py Tools by Category

| Category | Tools |
|----------|-------|
| Core Pipeline | cex_8f_motor, cex_8f_runner, cex_crew_runner, cex_run |
| Orchestration | cex_mission, cex_mission_runner, cex_coordinator, cex_signal_watch |
| Agent Mgmt | cex_agent_spawn, cex_skill_loader, cex_prompt_layers |
| Knowledge | cex_kc_index, cex_retriever, cex_query, cex_research |
| Memory | cex_memory, cex_memory_select, cex_memory_update, cex_memory_age, cex_memory_types |
| Quality | cex_score, cex_feedback, cex_quality_monitor, cex_doctor, cex_system_test |
| Build | cex_compile, cex_schema_hydrate, cex_materialize, cex_forge |
| Evolution | cex_evolve, cex_auto, cex_prompt_optimizer, cex_flywheel_worker |
| Routing | cex_router, cex_token_budget, cex_gdp |
| Bootstrap | cex_bootstrap, cex_init, cex_boot_gen, cex_batch, cex_hooks |
| Utility | cex_shared, cex_errors, cex_output_formatter, cex_intent, cex_index, etc. |

### cex_sdk (56 modules)

| Package | Modules | Purpose |
|---------|---------|---------|
| models/ | 8 providers | Multi-provider LLM access |
| knowledge/ | 12 (readers, chunkers, embedders, reranker) | RAG pipeline |
| tools/ | 6 (decorator, function, toolkit, builtins, MCP) | Tool execution |
| workflow/ | 7 (step, condition, loop, parallel, router) | DAG execution |
| memory/ | 3 (manager, compression, stores) | Session memory |
| guardrails/ | 3 (base, pii, prompt_injection) | Runtime safety |
| + eval, reasoning, session, tracing, vectordb, utils | 7 | Support |

---

## L6: Governance

```
.claude/rules/      9 nucleus rules + GDP + brand-bootstrap
.claude/commands/   13 slash commands (/build /validate /mission /evolve etc.)
.cex/learning_records/   71 post-execution learning records
.cex/experiments/        A/B experiment tracking
```

---

## Symbiosis Map

```
                    L7 Documentation
                         |
                         v (humans read)
    L6 Governance <--> L0 Genesis/Config
         |                |
         v (rules)        v (bootstrap)
    L4 Knowledge <--> L3 Archetypes <--> L1 Pillars
         |                |                  |
         v (KCs)          v (ISOs)           v (schemas)
                     L5 Tools
                     (runtime engine)
                          |
                          v (dispatch, signal, spawn)
                     L2 Nuclei
                     (domain execution)
```

## 7 Critical Dependency Chains

| Chain | Flow |
|-------|------|
| Build | Intent -> motor -> plan -> crew_runner -> ISOs -> LLM -> artifact -> pillar |
| Quality | Artifact -> score -> quality_gate -> learning_record -> builder_memory |
| Knowledge | Source -> KC -> builder_knowledge_card -> prompt -> LLM context |
| Decision | Ambiguity -> GDP -> manifest -> user -> autonomous execution |
| Memory | Observation -> memory_update -> decay -> memory_select -> prompt injection |
| Evolution | Artifact -> evolve -> research -> delta -> verify -> keep/discard |
| Dispatch | Mission -> mission_runner -> waves -> dispatch.sh -> nuclei -> signals |

## OpenClaude Wiring (7 active wires)

| Wire | What | When |
|------|------|------|
| 1 | p03_sp_cex_core_identity | EVERY prompt |
| 2 | p03_ins_doing_tasks | Via INCLUDE in identity |
| 3 | p03_ins_action_protocol | Via INCLUDE in identity |
| 4 | p11_gr_* guardrails | CALL/PRODUCE/COLLABORATE |
| 5 | p03_sp_verification_agent | GOVERN function |
| 6 | p04_skill_compact | 85% context budget |
| 7 | p04_skill_memory_extract | Every 5 executions |

## Fractal Self-Similarity

The same 12-concept structure repeats at 3 levels:

| Concept | P01-P12 (universal) | N01-N07 (domain) | Builders (per-kind) |
|---------|---------------------|-------------------|---------------------|
| Knowledge | P01_knowledge | N{NN}/knowledge | bld_knowledge_card |
| Identity | P02_model | N{NN}/agents | bld_system_prompt |
| Prompts | P03_prompt | N{NN}/prompts | bld_instruction |
| Tools | P04_tools | N{NN}/tools | bld_tools |
| Output | P05_output | N{NN}/output | bld_output_template |
| Schema | P06_schema | N{NN}/schemas | bld_schema |
| Evals | P07_evals | N{NN}/quality | bld_quality_gate |
| Architecture | P08_architecture | N{NN}/architecture | bld_architecture |
| Config | P09_config | N{NN}/config | bld_config |
| Memory | P10_memory | N{NN}/memory | bld_memory |
| Feedback | P11_feedback | N{NN}/feedback | bld_quality_gate |
| Orchestration | P12_orchestration | N{NN}/orchestration | bld_collaboration |

Each nucleus IS a brain that mirrors the universal pillar structure.
The pillars ARE the universal schema that all nuclei instantiate.
The builders ARE the factories that populate both levels.
