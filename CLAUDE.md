# CEX Boot Chain

> **You are inside CEX** — a typed knowledge system for LLM agents.
> 99 kinds, 99 builders, 12 pillars, 7 nuclei, 8F pipeline.

---

## STEP 1: WHAT IS CEX

CEX is **LLM-for-LLM**: a taxonomy where every artifact has a `kind`, every kind has a builder (13 ISOs), and builders compose through the **8 Function pipeline**.

```
User intent → OBJECT_TO_KINDS → Builder selection → 8F Runner → Artifact
```

## STEP 2: THE 8F PIPELINE

Every artifact is produced by running 8 functions in sequence:

| # | Function | Verb | What it does |
|---|----------|------|-------------|
| F1 | CONSTRAIN | Restrict | Load schema + config for the kind |
| F2 | BECOME | Be | Load agent identity + system prompt |
| F3 | INJECT | Know | Load knowledge cards + memory |
| F4 | REASON | Think | LLM plans the approach (haiku) |
| F5 | CALL | Do | Parse available tools |
| F6 | PRODUCE | Generate | LLM generates the artifact (sonnet) |
| F7 | GOVERN | Evaluate | 6 hard gates validate output |
| F8 | COLLABORATE | Coordinate | Save artifact + signal completion |

**Runner**: `python _tools/cex_8f_runner.py --kind <kind> --topic <topic>`
**Dry-run**: `python _tools/cex_8f_runner.py --kind <kind> --topic <topic> --dry-run`
**Intent**: `python _tools/cex_8f_motor.py --intent "create X for Y"`

## STEP 3: KEY PATHS

| What | Where |
|------|-------|
| **Builders** (99) | `archetypes/builders/{kind}-builder/` (13 ISOs each) |
| **Schemas** (12) | `P{01-12}_*/` → `_schema.yaml` (kind definitions) |
| **Templates** | `P{01-12}_*/templates/tpl_{kind}.md` |
| **Examples** (244) | `P{01-12}_*/examples/ex_{kind}_{topic}.md` |
| **KC Library** (28) | `P01_knowledge/library/domain/` (domain knowledge) |
| **Tools** (19) | `_tools/` (forge, motor, runner, doctor, ...) |
| **Nuclei** (7) | `N{01-07}_*/` (domain instances, fractal of 12 pillars) |
| **Taxonomy** | `archetypes/TAXONOMY_LAYERS.yaml` |
| **Kind→Template** | `archetypes/TYPE_TO_TEMPLATE.yaml` (100 entries) |
| **Kind→Builder** | `_docs/8F_BUILDER_MAP.yaml` |
| **Architecture** | `CEX_ARCHITECTURE_MAP.md` |
| **8F Spec** | `_docs/MOTOR_8F_SPEC.md` |
| **Docs** | `_docs/` (whitepaper, naming, LLM instructions) |

## STEP 4: THE 12 PILLARS

| P# | Name | Kinds | Core Types |
|----|------|:-----:|-----------|
| P01 | Knowledge | 8 | knowledge_card, rag_source, glossary, context_doc, chunk_strategy, embedding_config, few_shot, retriever_config |
| P02 | Model | 11 | agent, lens, boot_config, mental_model, model_card, router, fallback_chain, agent_package, axiom, handoff_protocol, reward_signal |
| P03 | Prompt | 7 | system_prompt, prompt_template, chain, action_prompt, instruction, persona_prompt, output_schema_P03 |
| P04 | Tools | 18 | skill, mcp_server, hook, plugin, client, cli_tool, scraper, connector, daemon, function_def, search_tool, vision_tool, code_executor, webhook, batch_runner, api_adapter, cache_layer, rate_limiter |
| P05 | Output | 4 | response_format, parser, formatter, naming_rule |
| P06 | Schema | 6 | input_schema, type_def, validator, interface, validation_schema, output_schema_P06 |
| P07 | Evals | 10 | unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric, regression_test, ab_test, bias_eval, latency_eval |
| P08 | Architecture | 8 | pattern, law, diagram, component_map, director, decision_record, naming_rule, agent_card |
| P09 | Config | 7 | env_config, path_config, permission, feature_flag, runtime_rule, secret_config, deploy_config |
| P10 | Memory | 6 | runtime_state, brain_index, learning_record, session_state, memory_scope, conversation_log |
| P11 | Feedback | 6 | quality_gate, bugloop, lifecycle_rule, guardrail, optimizer, reward_signal |
| P12 | Orchestration | 8 | workflow, dag, spawn_config, signal, handoff, dispatch_rule, checkpoint, schedule |

## STEP 5: THE 7 NUCLEI

Each nucleus mirrors ALL 12 pillars, filled with domain-specific content.

| ID | Domain | Maps to | Subdirs |
|----|--------|---------|:-------:|
| N01 | Intelligence | Research (research_lead) | 12 |
| N02 | Marketing | Marketing (marketing_lead) | 12 |
| N03 | Engineering | Build (builder_lead) | 12 |
| N04 | Knowledge | Indexing (knowledge_lead) | 12 |
| N05 | Operations | Execute (operations_lead) | 12 |
| N06 | Commercial | Monetize (commercial_lead) | 12 |
| N07 | Admin | Orchestrate (orchestrator) | 12 |

Pattern: `ex_pattern_nucleus_fractal.md` in `P08_architecture/examples/`

## STEP 6: COMMON TASKS

### Create an artifact
```bash
python _tools/cex_8f_runner.py --kind knowledge_card --topic "my_topic"
```

### Decompose an intent
```bash
python _tools/cex_8f_motor.py --intent "create a sales agent with tools"
```

### Check repo health
```bash
python _tools/cex_doctor.py
```

### Generate from template
```bash
python _tools/cex_forge.py --lp P01 --type knowledge_card --seeds "topic keywords" --builder
```

### Compile examples
```bash
python _tools/cex_compile.py --all
```

## STEP 7: QUALITY GATE

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Reference quality |
| >= 8.0 | Skilled | Published |
| >= 7.0 | Learning | Experimental |
| < 7.0 | Rejected | Redo |

**Density** >= 0.80 | **Frontmatter** required: id, kind, pillar | **Max body**: per schema

## CONSTRAINTS

**NEVER**: Invent kinds not in schemas | Skip frontmatter | Use quality != null in generated artifacts
**ALWAYS**: Check schema before creating | Use builders for production | Run doctor after changes
