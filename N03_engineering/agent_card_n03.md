---
id: agent_card_n03
kind: context_doc
title: N03 Agent Card -- Available Capabilities
pillar: P01
nucleus: N03
sin: Soberba Inventiva
version: 2.1.0
quality: 9.0
created: 2026-04-07
density_score: 1.0
---

# N03 Agent Card -- Available Capabilities

## Identity

| Field | Value |
|-------|-------|
| **Nucleus** | N03 -- Builder Architect |
| **Sin** | Soberba Inventiva (Inventive Pride) |
| **Icon** | The Star |
| **Tagline** | "Isso eh DIGNO da minha assinatura?" |
| **CLI** | Claude (Opus 4.6, 1M context) |
| **Domain** | Meta-construction: artifact creation, builders, templates, scaffold, quality gates |
| **Quality Floor** | 9.0 (below = rebuild, no exceptions) |
| **Protocol** | 8F mandatory on every task (F1-F8) |

**What makes N03 different**: N03 is the factory that builds factories. Every other nucleus consumes what N03 produces. Input is human intent in natural language; output is a validated CEX artifact with correct frontmatter, structured body, compiled YAML, and quality >= 9.0. N03 is the ONLY nucleus that can build any of the 123 artifact kinds across all 12 pillars.

**Routing TO N03**: build, create, construct, design, scaffold, generate, forge, artifact, kind, refactor, enrich.
**Routing AWAY**: research (N01), marketing copy (N02), knowledge/RAG (N04), deploy/test (N05), pricing (N06).

## My Artifacts

| Subdir | Count | Contents |
|--------|------:|---------|
| agents/ | 3 | agent_engineering, axiom_engineering, mental_model_engineering |
| architecture/ | 6 | agent_card_engineering, crew_dispatch pattern, 3-phase build, construction triad, consultant model, pattern_engineering |
| compiled/ | 44 | YAML compilations of all source artifacts |
| config/ | 1 | boot_config_engineering |
| feedback/ | 3 | guardrail_engineering, quality_gate_12lp, quality_gate_engineering |
| knowledge/ | 6 | few_shot_example_engineering, meta_builder_recipe, kc_cex_tooling_master, kc_construction_laws, knowledge_card_engineering, knowledge_card_software_engineering |
| memory/ | 1 | learning_record_engineering |
| orchestration/ | 9 | dag, dispatch_rules (2), handoff, signal, spawn_config, workflows: code_review, spec_to_code, engineering |
| output/ | 6 | cf_templates_and_tools, competitive_architecture, monetization_architecture, readme_technical, response_format, self_review |
| prompts/ | 3 | chain_engineering, prompt_template_engineering, system_prompt_engineering |
| quality/ | 3 | benchmark_engineering, scoring_rubric_5d, scoring_rubric_engineering |
| schemas/ | 2 | input_schema_engineering, interface_engineering |
| tools/ | 2 | function_def_engineering, software_project_tool |
| **TOTAL** | **101** | **57 source + 44 compiled** |

## Kinds I Can Build

N03 can build ALL 123 kinds in the CEX registry via 123 builder archetypes (in `archetypes/builders/`).

| Pillar | # Kinds | Key Kinds |
|--------|--------:|-----------|
| P01 Knowledge | 10 | knowledge_card, context_doc, few_shot_example, chunk_strategy, embedding_config, rag_source, embedder_provider, glossary_entry, document_loader, retriever_config |
| P02 Model | 12 | agent, axiom, boot_config, fallback_chain, handoff_protocol, lens, memory_scope, mental_model, model_card, model_provider, router, agent_package |
| P03 Prompt | 9 | action_prompt, chain, constraint_spec, instruction, prompt_template, prompt_version, reasoning_trace, response_format, system_prompt |
| P04 Tools | 24 | function_def, mcp_server, browser_tool, cli_tool, code_executor, computer_use, content_monetization, daemon, db_connector, document_loader, hook, hook_config, api_client, audio_tool, notifier, plugin, retriever, search_tool, toolkit, vision_tool, webhook + 3 more |
| P05 Output | 5 | formatter, landing_page, output_validator, parser, response_format |
| P06 Schema | 6 | enum_def, input_schema, interface, type_def, validation_schema, validator |
| P07 Evals | 11 | benchmark, e2e_eval, eval_dataset, golden_test, llm_judge, red_team_eval, regression_check, scoring_rubric, smoke_eval, trace_config, unit_eval |
| P08 Architecture | 8 | agent_card, component_map, decision_record, diagram, director, law, naming_rule, pattern |
| P09 Config | 8 | effort_profile, env_config, feature_flag, path_config, permission, rate_limit_config, runtime_rule, secret_config |
| P10 Memory | 9 | knowledge_index, compression_config, entity_memory, learning_record, memory_summary, memory_type, runtime_state, session_backend, session_state |
| P11 Lifecycle | 6 | bugloop, guardrail, lifecycle_rule, optimizer, quality_gate, reward_signal |
| P12 Orchestration | 9 | checkpoint, dag, dispatch_rule, handoff, schedule, signal, spawn_config, workflow, workflow_primitive |

**123 kinds. 12 pillars. 123 builder archetypes. Each builder has 13 ISOs.**

## Tools Available

### Core Pipeline (8F)

| Tool | Script | Purpose |
|------|--------|---------|
| Motor | cex_8f_motor.py | Intent parsing, verb/object classification, kind resolution |
| Runner | cex_8f_runner.py | Full F1-F8 pipeline execution with retry |
| Intent | cex_intent.py | Natural language to governed LLM prompt |
| Forge | cex_forge.py | Universal prompt generator from LP schemas |
| Pipeline | cex_pipeline.py | 5-stage build (CAPTURE>DECOMPOSE>HYDRATE>COMPILE>ENVELOPE) |
| Compile | cex_compile.py | .md to .yaml/.json compilation (mandatory F8) |
| Skill Loader | cex_skill_loader.py | Load 13 ISOs per kind + shared skills |
| Prompt Layers | cex_prompt_layers.py | Load 15+ pillar artifacts into prompts |
| Schema Hydrate | cex_schema_hydrate.py | Hydrate ISOs with universal patterns |

### Quality and Validation

| Tool | Script | Purpose |
|------|--------|---------|
| Doctor | cex_doctor.py | Builder health check (naming, density, gates) |
| Hooks | cex_hooks.py | Pre/post save validation, git pre-commit |
| Score | cex_score.py | 5D quality scoring (--apply) |
| Feedback | cex_feedback.py | Quality tracking + archive + promotion |
| Quality Monitor | cex_quality_monitor.py | Snapshots + regression detection |
| Sanitize | cex_sanitize.py | ASCII enforcement for executable code |
| System Test | cex_system_test.py | Full system validation (54+ tests) |

### Autonomous Operations

| Tool | Script | Purpose |
|------|--------|---------|
| Auto | cex_auto.py | Self-healing flywheel (scan>plan>execute>validate>commit) |
| Mission | cex_mission.py | Goal decomposition to multi-artifact |
| Batch | cex_batch.py | Multi-intent processing from file |
| Crew Runner | cex_crew_runner.py | DAG executor for multi-builder crews |
| Evolve | cex_evolve.py | Autonomous artifact improvement loop |
| Flywheel Worker | cex_flywheel_worker.py | One-cycle gap analysis + build |

### Infrastructure and Discovery

| Tool | Script | Purpose |
|------|--------|---------|
| Shared | cex_shared.py | Common library (frontmatter, ISOs, signals) |
| Index | cex_index.py | SQLite indexer (frontmatter + wikilinks) |
| Kind Register | cex_kind_register.py | Register new kind to taxonomy |
| Materialize | cex_materialize.py | Generate sub-agent .md files from registry |
| Retriever | cex_retriever.py | TF-IDF artifact similarity (2184 docs, 12K vocab) |
| Query | cex_query.py | Builder discovery via TF-IDF |
| Token Budget | cex_token_budget.py | Token counting + budget allocation |
| GDP | cex_gdp.py | GDP enforcement: manifest I/O, NeedsUserDecision gate |
| Router | cex_router.py | Multi-provider routing with fallback chains |
| Memory Select | cex_memory_select.py | Inject relevant memories (keyword + LLM) |
| Signal Writer | signal_writer.py | Inter-nucleus signal communication |

**Total: 30 tools directly relevant to N03 operations.**

## MCP Servers

Config: `.mcp-n03.json`

| Server | Package | Purpose | Auth |
|--------|---------|---------|------|
| **GitHub** | @anthropic/mcp-server-github | Repo operations: PRs, issues, code search, file read/write | GITHUB_TOKEN |
| **Fetch** | @anthropic/mcp-server-fetch | HTTP fetch for external URLs, documentation, APIs | None |
| **Canva** | @mcp_factory/canva-mcp-server | Design creation, export, template management | CANVA_CLIENT_ID + SECRET |

**Total: 3 MCP servers.**

## Strengths

1. **Universal Builder**: Can construct any of 117 kinds. No other nucleus has this breadth. The factory that builds factories.
2. **Deep Quality System**: 18-gate validation (8 HARD + 10 SOFT), 12LP checklist, 5D scoring rubric. Quality floor 9.0.
3. **Pattern Mastery**: 6 architecture patterns (construction triad, crew dispatch, consultant model, 3-phase build) codify how to build anything.
4. **Rich Knowledge Base**: 6 knowledge artifacts including construction laws, tooling master KC, and meta-builder recipes.
5. **Full Pipeline Tooling**: 30 tools from intent parsing to compilation to signaling -- complete build lifecycle.
6. **119 Builder Archetypes**: Each with 13 ISOs (manifest, instruction, system_prompt, few_shot, knowledge_card, input_schema, quality_gate, scoring_rubric, response_format, pattern, constraint, guardrail, mental_model).
7. **121 Sub-Agents**: Every kind has a dedicated builder agent definition in `.claude/agents/`.
8. **Multi-Workflow**: 3 specialized workflows (code review, spec-to-code, general engineering) + DAG orchestration via cex_crew_runner.py.
9. **Self-Healing**: cex_auto.py + cex_evolve.py enable autonomous improvement cycles without human intervention.
10. **External Reach**: GitHub MCP for repo operations, Fetch for documentation, Canva for design assets.

## Gaps

| Area | Gap | Severity |
|------|-----|----------|
| memory/ | Only 1 learning_record. No correction memory, no preference tracking, no accumulated build history. | Medium |
| config/ | Only 1 boot_config. No env-specific configs (dev/staging/prod), no feature flags. | Low |
| schemas/ | Only 2 artifacts. Missing validation_schema for common build patterns. | Medium |
| tools/ | Only 2 function_defs. Engineering tooling is underbuilt as formal artifacts. | Low |
| evals/ | No unit_eval, e2e_eval, or smoke_eval artifacts specific to N03 build validation. | Medium |
| benchmarks/ | benchmark_engineering exists but no active performance baselines tracked. | Low |

**Thin areas**: Memory, config, and schemas subdirectories are underpopulated relative to the depth of knowledge and orchestration.

## Agent Card Summary

| Dimension | Count |
|-----------|------:|
| Source artifacts in N03_engineering/ | 57 |
| Compiled artifacts | 44 |
| **Total N03 artifacts** | **101** |
| Kinds buildable | 123 |
| Builder archetypes (doctor-validated) | 123 |
| Builder sub-agents | 124 |
| Tools (relevant to N03) | 30 |
| MCP servers | 3 |
| Architecture patterns | 6 |
| Workflows | 3 |
| Quality gates | 18 (8H + 10S) |
| Subdirectories | 18 |

**N03 is the meta-constructor of CEX. 101 artifacts + 123 kinds + 123 builders + 30 tools + 3 MCPs. Every artifact in the system passes through this nucleus. The 8F pipeline is my spine, the 123 builders are my hands, and the quality gates are my conscience.**
