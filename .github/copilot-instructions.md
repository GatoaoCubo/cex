# CEX — GitHub Copilot Instructions

## What Is This Repository?

CEX is a typed, indexed knowledge base for building LLM agents.
It organizes agent components into **12 pillars**, **7 nuclei**, and
**78 artifact types** across a 5-layer architecture.

## Architecture (5 Layers)

- **L0 DNA** — `archetypes/builders/{type}-builder/` — 13 ISO files per builder (factory blueprints)
- **L1 Schema** — `P01_knowledge/` through `P12_orchestration/` — schemas, templates, examples
- **L2 Instance** — `N01_intelligence/` through `N07_admin/` — domain-specific instances
- **L3 Engine** — `_tools/` — CLI pipeline, validators, compiler
- **L4 Root** — `CLAUDE.md`, `README.md`, `INDEX.md` — entry points

## Navigation

- **By function**: `archetypes/builders/{type}-builder/` (e.g., `agent-builder/`)
- **By pillar**: `P{NN}_{name}/` (P01 through P12)
- **By domain**: `N{XX}_{name}/` (N01 through N07)
- **Full spec**: `_docs/ARCHITECTURE.md`
- **Governance**: `archetypes/CODEX.md`

## The 8 LLM Functions (Pipeline Order)

1. **BECOME** — Identity, persona, system prompt
2. **INJECT** — Context, knowledge cards
3. **REASON** — Chain-of-thought, planning
4. **CALL** — Tools, APIs, MCP servers
5. **PRODUCE** — Final output
6. **CONSTRAIN** — Schemas, validation
7. **GOVERN** — Quality gates, evals
8. **COLLABORATE** — Signals, handoffs, orchestration

These are a **pipeline** (sequential), not categories.

## 12 Pillars

- **P01 Knowledge** — knowledge_card, rag_source, glossary_entry, context_doc, embedding_config, few_shot_example
- **P02 Model** — agent, lens, boot_config, mental_model, model_card, router, fallback_chain, agent_package, axiom
- **P03 Prompt** — system_prompt, user_prompt, prompt_template, few_shot, chain_of_thought, react, chain, meta_prompt, router_prompt, planner
- **P04 Tools** — skill, mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon, component
- **P05 Output** — response_format, parser, formatter, naming_rule
- **P06 Schema** — input_schema, type_def, validator, interface, validation_schema, artifact_blueprint, grammar
- **P07 Evals** — unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric
- **P08 Architecture** — agent_card, pattern, law, diagram, component_map
- **P09 Config** — env_config, path_config, permission, feature_flag, runtime_rule
- **P10 Memory** — runtime_state, knowledge_index, learning_record, session_state
- **P11 Feedback** — quality_gate, bugloop, lifecycle_rule, guardrail, optimizer
- **P12 Orchestration** — workflow, dag, spawn_config, signal, handoff, dispatch_rule, crew

## 7 Nuclei (Business Domains)

- **N01** intelligence (Research)
- **N02** marketing (Marketing)
- **N03** engineering (Engineering)
- **N04** knowledge (Knowledge management)
- **N05** operations (Operations)
- **N06** commercial (Commercial)
- **N07** admin (Administration)

## Naming Convention

```
{layer}_{kind}_{topic}.{ext}

bld_  = builder (L0)     | bld_system_prompt_agent.md
tpl_  = template (L1)    | tpl_knowledge_card.md
ex_   = example (L1)     | ex_knowledge_card_rag.md
(none)= instance (L2)    | knowledge_card_company_product.md
```

Rules: lowercase, snake_case, ASCII only, max 50 chars.
Every artifact exists as dual output: `.md` (human) + `.yaml`/`.json` (machine).

## Tools

- `python _tools/cex_doctor.py` — health check, validates structure
- `python _tools/validate_builder.py` — validates builder ISO completeness
- `python _tools/cex_compile.py --all` — compiles .md to .yaml/.json
- `python _tools/distill.py` — extracts YAML frontmatter

## Quality Gate

- **>= 9.5** Golden (reference quality)
- **>= 8.0** Skilled (published)
- **>= 7.0** Learning (experimental)
- **< 7.0** Rejected (redo)

Density minimum: 0.8. YAML frontmatter required (id, type, quality, keywords).

## Key Rules

- `id` field must equal the filename stem
- Nucleus schemas inherit from root pillar schemas — never remove fields, only add
- Builders have 13 ISO files — cross-validate before commit
- Bullets max 80 chars, no prose blocks > 3 lines
- Artifacts live in `N{XX}/P{NN}/{type}/` — never outside this structure

## Key Files

- `CLAUDE.md` — LLM entry point with function lookup table
- `LLM_PIPELINE.md` — full 8-function pipeline specification
- `archetypes/CODEX.md` — governance rules, variables, lifecycle
- `_docs/ARCHITECTURE.md` — architecture deep dive (5 layers, 7 nuclei, 12 pillars)
- `_docs/NAMING_CONVENTION.md` — naming grammar
- `CEX_ARCHITECTURE_MAP.md` — visual architecture map
