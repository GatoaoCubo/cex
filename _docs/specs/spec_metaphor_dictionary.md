---
id: spec_metaphor_dictionary
kind: context_doc
title: Metaphor Dictionary -- Internal Language to Universal Terms
version: 1.1.0
quality: 9.0
pillar: P01
created: 2026-04-07
purpose: When the user says X, the system means Y. Translation table for all internal metaphors.
density_score: 1.0
---

# Metaphor Dictionary

The user (and internal docs) use metaphors to explain concepts. LLMs and artifacts must use universal terms. This dictionary maps one to the other.

## Game Architecture Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| card | artifact | **artifact** (MLOps, CI/CD) | .md file with YAML frontmatter |
| deck (file) | agent self-description | **agent card** (Google A2A, MCP) | agent_card_n0X.md — capabilities, routing, gaps |
| deck (concept) | assembled context | **context assembly** (prompt eng.) | artifacts selected + composed for one task |
| base deck | boot context | **system prompt** / agent init | agent_card + rules + sin identity (loaded on startup) |
| mission deck | task context | **task spec** / instruction payload | task_spec + referenced builders + KCs + templates |
| hand | active context | **working context** / working set (OS) | all artifacts loaded during one 8F pipeline run |
| draw | F3 INJECT | **retrieval** (the R in RAG) | pulling artifacts from library into working context |
| play | F6 PRODUCE | **generation** / inference | generating output using loaded context |
| round | 8F cycle | **pipeline run** (MLOps) | one complete F1-F8 pipeline execution |
| table | grid dispatch | **multi-agent orchestration** (LangGraph, CrewAI) | multiple agents working in parallel |
| dealer | N07 orchestrator | **orchestrator** / supervisor agent | selects context, writes task specs, dispatches |
| slot | {{mustache}} variable | **template variable** / slot (NLU) | template field the LLM fills contextually |
| combo | context combination | **prompt composition** | multiple artifacts assembled for compound effect |
| library | CEX repository | **knowledge base** / artifact store | all artifacts across 12 pillars + 117 kinds |
| game | pipeline | **pipeline** (MLOps, CI/CD) | the 8F execution flow |

## Architecture Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| genesis | base layer | **schema layer** / archetype layer | archetypes/ + P{01-12}/ schemas + templates (read-only) |
| mold | archetype builder | **archetype** / template (OOP: class) | archetypes/builders/{kind}-builder/ (13 components) |
| filled mold | nucleus artifact | **instance** (OOP: class→instance) | N{01-06}_*/ domain-specific instances |
| fractal | mirrored structure | **convention over configuration** (Rails) | nuclei mirror the 12 pillar categories |
| building | CEX system | **system** / repository | the full repository with all layers |
| floor | nucleus domain | **agent domain** | one N0X directory with its artifacts |
| superintendent | nucleus agent | **autonomous agent** | the LLM running in that nucleus |
| department | sector/domain | **domain** | research, marketing, builder, knowledge, operations, commercial |

## Process Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| spawn | launch process | **spawn/fork** (POSIX) ✅ | Start-Process cmd -> boot/n0X.cmd -> pi |
| kill | terminate process | **kill/SIGTERM** (POSIX) ✅ | taskkill /F /PID /T (tree-kill) |
| idle | completed but alive | **idle** ✅ | process finished task, waiting for input |
| boot | startup sequence | **bootstrap** ✅ | CMD sets theme -> pi loads agent card + rules + prompt |
| overnight | autonomous background run | **batch job** / cron job | boot/overnight_h1.cmd (evolve + audit) |
| grid | parallel layout | **agent topology** / multi-agent layout | 6 windows, 2x3, dynamic resolution |
| signal | completion message | **event/signal** (POSIX, event-driven) ✅ | .cex/runtime/signals/signal_n0X_*.json |
| handoff | task document | **task spec** (CEX keeps "handoff" as convention) | .cex/runtime/handoffs/n0X_task.md |
| wave | sequential group | **execution phase** / wave (deployment) ✅ | set of parallel dispatches with gate between |

## Quality Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| improve | evolve artifact | **optimize** / AutoML evolve | cex_evolve.py (heuristic or agent mode) |
| fix | update/refactor | **refactor** / patch ✅ | edit specific file or tool |
| check | audit/validate | **audit** / lint ✅ | cex_doctor.py + cex_flywheel_audit.py |
| clean | sanitize | **sanitize** ✅ | cex_sanitize.py (ASCII compliance) |
| gate | quality threshold | **quality gate** (CI/CD) ✅ | quality >= 8.5 to pass, cex_score.py |
| ship | release | **release** / ship ✅ | cex_release_check.py (28 checks, all green) |

## Brand Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| blank brain | unbootstrapped CEX | **unconfigured instance** | {{BRAND_*}} variables unresolved |
| assimilate | bootstrap brand | **bootstrap** / provision ✅ | /init -> brand_config.yaml -> brand_inject.py |
| the X | brand variable | **brand identity** (unique to CEX) | CEX = C + E + X, where X = the brand identity |
| digital asset | configured CEX instance | **configured instance** / deployed agent | CEX + brand = specialized AI system |

## Intent Resolution Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| translate / transmute (at F1) | resolve intent | **intent resolution** (NLU: Rasa, Dialogflow, Amazon Lex) | N07 transmutation -> 8F F1 CONSTRAIN |
| translate / transmute (at F3) | rewrite query | **query rewriting** (Search/RAG: Google, ES, LlamaIndex) | cex_query.py + cex_retriever.py -> 8F F3 INJECT |
| translate / transmute (at F6) | optimize prompt | **prompt optimization** (LLM: DSPy "prompt compilation") | cex_crew_runner.py -> 8F F6 PRODUCE |
| understand me | parse intent | **intent classification** (NLU) | `cex_8f_motor.py` intent parser + `kinds_meta.json` |
| fill in the blanks | complete parameters | **slot filling** (NLU, dialogue systems) | prompt_template {{vars}} + brand_inject.py |
| figure out what I mean | disambiguate | **disambiguation** (NLU, search) | GDP clarifying questions + N07 restatement |
| rewrite my question | optimize query | **query rewriting** (IR, RAG) | 8F F1 CONSTRAIN + F4 REASON |
| assemble the context | build prompt | **prompt composition** / context assembly | `cex_crew_runner.py` + `cex_prompt_layers.py` |

## Input/Output Pipeline Metaphors

| User says | System means | Industry term | CEX implementation |
|-----------|-------------|---------------|-------------------|
| feed it | provide input | **injection** / input provision | 8F F3 INJECT (load KCs, memory, brand into prompt) |
| spit out / produce | generate output | **generation** / inference | 8F F6 PRODUCE (LLM generates artifact) |
| cook / bake | process through pipeline | **pipeline execution** (MLOps) | 8F F1-F8 full pipeline run |
| filter | select relevant items | **retrieval filtering** / re-ranking | `cex_retriever.py` top_k + reranker |
| mix / blend | combine multiple sources | **fusion** / ensemble (ML) | multi-source context assembly in F3 |
| stamp / seal | validate and approve | **quality gate** (CI/CD) | 8F F7 GOVERN + `cex_score.py` |

## Operational Metaphors

| User says | System means | Industry term | CEX implementation | Teach? |
|-----------|-------------|---------------|-------------------|--------|
| teach it | inject examples | **in-context learning** (few-shot prompting) | few_shot_example kind, P03 prompt injection | YES -- "Few-shot, not fine-tuning" |
| remember this | persist to memory | **entity memory** / knowledge persistence | entity_memory kind, P10 + cex_memory_update.py | YES -- "Entity memory, not conversation history" |
| forget this | prune memory | **memory eviction** (cache management) | cex_memory_update.py --prune | YES -- "Eviction, like cache invalidation" |
| connect to X | integrate API/MCP | **tool registration** / MCP server config | mcp_server kind, P04 + api_client kind | YES -- "MCP tool registration" |
| speed it up | optimize latency | **inference optimization** (batch/cache/quantize) | prompt_cache kind, P10 + context_window_config | YES -- "Inference optimization, not just fewer tokens" |
| make it cheaper | reduce cost | **token budget optimization** | cex_token_budget.py + context_window_config | YES -- "Token budget, the unit of LLM cost" |
| make it smarter | improve quality | **prompt optimization** / model upgrade | cex_prompt_optimizer.py + cex_evolve.py | YES -- "Prompt optimization first, model upgrade second" |
| test it | run evaluation | **evaluation** (unit/e2e/smoke) | unit_eval, e2e_eval, smoke_eval, benchmark kinds | YES if ambiguous -- "Which eval type?" |

## MLOps / LLM Ops Metaphors

| User says | System means | Industry term | CEX implementation | Teach? |
|-----------|-------------|---------------|-------------------|--------|
| -- | A/B test for models/prompts | **experiment** (MLOps) | cex_experiments/ + results.tsv | YES -- "Experiment, not just 'try'" |
| -- | versioned model/prompt store | **registry** (MLOps: MLflow, W&B) | archetypes/ + compiled/ (local registry) | YES -- "Registry, like Docker Hub for models" |
| -- | data-to-inference provenance | **lineage** (MLOps: MLflow, DVC) | 8F trace (F1-F8) = artifact lineage | YES -- "Lineage, not just 'history'" |
| evolve | optimization sweep | **sweep** (MLOps: W&B, Optuna) | cex_evolve.py (heuristic + agent mode) | YES -- "Sweep, not just 'improve'" |
| quality_gate | evaluation milestone snapshot | **checkpoint** (MLOps: PyTorch, HF) | cex_score.py --apply (snapshot at gate) | YES -- "Checkpoint, not just 'gate'" |
| -- | full pass through dataset | **epoch** (MLOps: deep learning) | one cex_evolve.py --all cycle = 1 epoch | YES -- "Epoch = one full pass" |
| -- | async grouped API requests | **batch** (API: OpenAI, Anthropic) | cex_batch.py (multi-intent processing) | YES -- "Batch API, not just 'queue'" |
| -- | token allocation limit | **token budget** (LLM Ops) | cex_token_budget.py + context_window_config | YES -- "Token budget = cost ceiling" |
| cex_score.py | benchmark framework | **evaluation harness** (MLOps: lm-eval, HELM) | cex_score.py + unit_eval + e2e_eval kinds | YES -- "Eval harness, not just 'scorer'" |
| overnight.ps1 | long-running compute task | **training job** (MLOps: SageMaker, Vertex AI) | boot/overnight_h1.cmd (evolve + audit) | YES -- "Training job, not just 'overnight'" |
| prompt_compiler | automated prompt improvement | **prompt optimization** (DSPy: prompt compilation) | cex_prompt_compiler.py + p03_pc_*.md | YES -- "DSPy-style prompt compilation" |
| cex_retriever | query-retrieve-rerank flow | **retrieval pipeline** (RAG: LlamaIndex, LangChain) | cex_retriever.py (TF-IDF + rerank) | YES -- "Retrieval pipeline, not just 'search'" |
| -- | vector space semantic shift | **embedding drift** (MLOps: Arize, WhyLabs) | not yet implemented (monitor embedding_config) | YES -- "Drift = silent quality decay" |
| -- | model serving API | **inference endpoint** (MLOps: HF, SageMaker) | cex_router.py provider endpoints | YES -- "Inference endpoint, not just 'API'" |
| cex_router | multi-provider request proxy | **model gateway** (MLOps: LiteLLM, Portkey) | cex_router.py (4 providers x 7 nuclei) | YES -- "Gateway, not just 'router'" |

## Rules

1. **Artifacts, code, docs**: use "Industry term" column. ALWAYS.
2. **User input**: accept "User says" column, translate silently.
3. **This dictionary**: the ONLY place both columns coexist.
4. **Llama-7B test**: if the term needs this dictionary to be understood, it's wrong for artifacts.
5. **Rename cascade**: changing a term requires CRUD across all files that reference it. See `N07_admin/P10_memory/terminology_standardization.md` for the full map.
6. **Didactic protocol**: check `N07_admin/P10_memory/taught_terms_registry.md` before teaching. Teach once per term, never repeat. See N02's didactic protocol spec for format guidelines.
