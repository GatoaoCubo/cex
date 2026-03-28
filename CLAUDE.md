# CEX — LLM Entry Point

> **You are inside a CEX repository.** A typed, indexed knowledge base
> for building LLM agents. 69 kinds, 69 builders, 12 pillars, 7 nuclei.
> Navigate by filename: `{layer}_{kind}_{topic}.{ext}`.

---

## Architecture (5 Layers)

| Layer | Location | Contains |
|-------|----------|----------|
| L0 DNA | `archetypes/builders/{kind}-builder/` | 13 ISO files per builder (factory) |
| L1 Schema | `P01_knowledge/` — `P12_orchestration/` | `_schema.yaml` + `templates/` + `examples/` + `compiled/` |
| L2 Instance | `N01_intelligence/` — `N07_admin/` | Domain-specific instances (7 nuclei) |
| L3 Engine | `_tools/` | 17 CLI tools (forge, motor, crew, doctor, compile, ...) |
| L4 Root | `CLAUDE.md`, `README.md`, `INDEX.md` | Entry points and navigation |

## Quick Navigation

| Need | Where |
|------|-------|
| How CEX works | `README.md` |
| 8 LLM Functions | `LLM_PIPELINE.md` |
| Architecture deep dive | `_docs/ARCHITECTURE.md` |
| Whitepaper | `_docs/WHITEPAPER_CEX.md` |
| Governance rules | `archetypes/CODEX.md` |
| Naming rules | `_docs/NAMING_CONVENTION.md` |
| Visual architecture map | `CEX_ARCHITECTURE_MAP.md` |
| Motor 8F spec | `_docs/MOTOR_8F_SPEC.md` |
| Crew patterns research | `_docs/CREW_PATTERNS_RESEARCH.md` |

## 12 Pillars × 69 Kinds

| Pillar | Name | Kinds | Primary Types |
|--------|------|:-----:|---------------|
| P01 | Knowledge | 6 | knowledge_card, rag_source, glossary_entry, context_doc, embedding_config, few_shot_example |
| P02 | Model | 9 | agent, lens, boot_config, mental_model, model_card, router, fallback_chain, iso_package, axiom |
| P03 | Prompt | 5 | system_prompt, prompt_template, chain, action_prompt, instruction |
| P04 | Tools | 9 | skill, mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon |
| P05 | Output | 4 | response_format, parser, formatter, naming_rule |
| P06 | Schema | 5 | input_schema, type_def, validator, interface, validation_schema |
| P07 | Evals | 6 | unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric |
| P08 | Architecture | 5 | pattern, law, diagram, component_map, director |
| P09 | Config | 5 | env_config, path_config, permission, feature_flag, runtime_rule |
| P10 | Memory | 4 | runtime_state, brain_index, learning_record, session_state |
| P11 | Feedback | 5 | quality_gate, bugloop, lifecycle_rule, guardrail, optimizer |
| P12 | Orchestration | 6 | workflow, dag, spawn_config, signal, handoff, dispatch_rule |

## 8 Functions (Pipeline)

| # | Function | Verb | Pillar Sources | Find builders |
|---|----------|------|---------------|---------------|
| 1 | BECOME | Be | P02, P03 | `bld_system_prompt_*`, `bld_manifest_*` |
| 2 | INJECT | Know | P01, P10 | `bld_knowledge_card_*`, `bld_memory_*` |
| 3 | REASON | Think | P03 | `bld_instruction_*` |
| 4 | CALL | Do | P04 | `bld_tools_*` |
| 5 | PRODUCE | Generate | P05 | `bld_output_template_*` |
| 6 | CONSTRAIN | Restrict | P06, P08 | `bld_schema_*` |
| 7 | GOVERN | Evaluate | P07, P11 | `bld_quality_gate_*` |
| 8 | COLLABORATE | Coordinate | P12 | `bld_collaboration_*` |

Sequential pipeline. BECOME before INJECT. GOVERN before COLLABORATE.

## 7 Nuclei

| ID | Domain | Files | Status |
|----|--------|:-----:|--------|
| N01 | Intelligence | 6 | Skeleton |
| N02 | Marketing | 5 | Skeleton |
| N03 | Engineering | 3 | Skeleton |
| N04 | Knowledge | 2 | Skeleton |
| N05 | Operations | 2 | Skeleton |
| N06 | Commercial | 2 | Skeleton |
| N07 | Admin | 2 | Skeleton |

## Tools (L3 Engine)

| Tool | Command | Purpose |
|------|---------|---------|
| **Forge v2** | `python _tools/cex_forge.py --lp P01 --type knowledge_card --seeds "x" --builder` | Generate artifact with builder context |
| **Motor 8F** | `python _tools/cex_8f_motor.py --intent "create sales agent"` | Decompose intent into builder plan |
| **Crew Runner** | `python _tools/cex_crew_runner.py --plan plan.json --dry-run` | Orchestrate builder pipeline |
| **Doctor** | `python _tools/cex_doctor.py` | Validate repo health |
| **Compile** | `python _tools/cex_compile.py --all` | .md → .yaml/.json |
| **Pipeline** | `python _tools/cex_pipeline.py --type X --topic Y` | 5-stage build |
| **Init** | `python _tools/cex_init.py` | Scaffold new CEX project |
| **Compare** | `python _tools/compare_builders.py --original X --generated Y` | Diff builders |

## Naming Grammar

```
bld_{iso}_{kind}.md   = Builder ISO file (L0)
tpl_{kind}.md         = Template (L1)
ex_{kind}_{topic}.md  = Example (L1)
{kind}_{topic}.md     = Instance (L2, in nuclei)
```

Lowercase. Snake_case. ASCII only. Max 50 chars.

## Quality Gate

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Reference quality |
| >= 8.0 | Skilled | Published |
| >= 7.0 | Learning | Experimental |
| < 7.0 | Rejected | Redo |

Density >= 0.80. Frontmatter required: `id`, `kind`, `pillar`, `title`.
