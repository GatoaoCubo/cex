---
id: n07_memory_industry_audit
kind: memory-summary
nucleus: N07
pillar: P10
title: "Industry Terminology Audit: CEX kinds vs Anthropic/OpenAI/Google/LangChain"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: N07_orchestrator
quality: 9.1
tags: [terminology, audit, industry, anthropic, openai, google, langchain, permanent]
tldr: "Maps all 117 CEX kinds against official terminology from 4 major providers. Identifies 8 gaps, 12 mismatches, and 1 critical problem: schemas in Portuguese."
density_score: null
source_session: SELF_BOOTSTRAP_2026-04-07
---

# Industry Terminology Audit

## Source Matrix

| Provider | Key docs | CEX relevance |
|----------|----------|---------------|
| **Anthropic** | Messages API, Tool Use, MCP, Computer Use, Extended Thinking, Prompt Caching | P03, P04, P10 |
| **OpenAI** | Assistants API, Agents SDK, Structured Outputs, Function Calling, Swarm | P02, P04, P06, P12 |
| **Google** | A2A Protocol, Gemini API, Vertex AI, Agent Builder | P08, P02, P12 |
| **LangChain/LangGraph** | Chains, Agents, Memory, Retrievers, Graph State, Supervisor | P03, P02, P10, P04 |
| **CrewAI** | Agents, Tasks, Crews, Tools, Process types | P02, P12, P04 |
| **MCP** | Servers, Tools, Resources, Prompts, Capabilities | P04, P03, P08 |

## Pillar-by-Pillar Validation

### P01 Knowledge — "O que o agente SABE"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| knowledge_card | **knowledge artifact** / grounding doc | Google (grounding) | ✅ Aligned |
| rag_source | **data source** / grounding source | All (RAG) | ✅ Aligned |
| glossary_entry | **term definition** | — | ✅ Unique to CEX, valid |
| context_doc | **context document** | Anthropic (system prompt sections) | ✅ Aligned |
| embedding_config | **embedding model config** | OpenAI, LangChain | ✅ Aligned |
| few_shot_example | **few-shot example** | All providers | ✅ Industry standard term |
| chunk_strategy | **chunking strategy** / text splitter | LangChain | ✅ Aligned |
| retriever_config | **retriever configuration** | LangChain, LlamaIndex | ✅ Aligned |
| vector_store | **vector store** / vector database | All | ⚠️ Industry says "vector store" not "vectordb backend" |
| embedder_provider | **embedding provider** | — | ✅ OK |

### P02 Model — "QUEM o agente EH"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| agent | **agent definition** | All (OpenAI Agents SDK, CrewAI, LangGraph) | ✅ Aligned |
| agent_package | **agent bundle** / agent config | — | ✅ CEX-specific, valid |
| lens | **persona** / personality injection | — | ⚠️ "Lens" is CEX-unique. Industry uses "persona" or "role" |
| boot_config | **agent initialization** / bootstrap config | — | ✅ OK |
| mental_model | **cognitive architecture** / reasoning profile | — | ⚠️ "Mental model" in psych means something different |
| model_card | **model card** | Anthropic, Google, Hugging Face | ✅ Industry standard |
| model_provider | **model provider** / LLM provider | All | ✅ Industry standard |
| router | **router** / intent router | LangChain, Semantic Router | ✅ Industry standard |
| fallback_chain | **fallback chain** / retry chain | LangChain | ✅ Aligned |
| handoff_protocol | **handoff protocol** | OpenAI Swarm/Agents SDK | ✅ Industry standard |
| axiom | **constitutional principle** / invariant rule | Anthropic (Constitutional AI) | ⚠️ "Axiom" is math term. Anthropic uses "constitutional principle" |
| memory_scope | **memory scope** / context scope | LangGraph | ✅ OK |

### P03 Prompt — "COMO o agente FALA"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| system_prompt | **system prompt** / system instruction | All | ✅ Industry standard |
| prompt_template | **prompt template** | All | ✅ Industry standard |
| chain | **chain** / prompt chain | LangChain | ✅ Industry standard |
| action_prompt | **action prompt** / tool-calling prompt | — | ✅ OK |
| instruction | **instruction** / task instruction | All | ✅ Industry standard |
| constraint_spec | **constraint specification** / guardrail prompt | — | ✅ OK |
| reasoning_trace | **chain-of-thought** / reasoning trace | Anthropic (extended thinking), OpenAI (reasoning) | ✅ Aligned |
| prompt_version | **prompt version** / prompt registry entry | — | ✅ OK |
| tagline | **tagline** / brand copy | — | ⚠️ Not LLM-specific. More marketing. Should this be in P03? |

### P04 Tools — "O que o agente USA"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| function_def | **function definition** / tool definition | OpenAI (function calling), Anthropic (tool use) | ✅ Aligned |
| mcp_server | **MCP server** | Anthropic (MCP protocol) | ✅ Industry standard |
| code_executor | **code interpreter** / sandbox | OpenAI (code interpreter) | ⚠️ OpenAI calls it "code interpreter" |
| computer_use | **computer use** | Anthropic | ✅ Industry standard (Anthropic coined it) |
| search_tool | **web search tool** | All | ✅ Aligned |
| browser_tool | **browser tool** / web browser | Anthropic (computer use), Playwright | ✅ Aligned |
| cli_tool | **CLI tool** / command-line tool | — | ✅ Standard |
| document_loader | **document loader** | LangChain | ✅ Industry standard |
| retriever | **retriever** | LangChain, LlamaIndex | ✅ Industry standard |
| api_client | **API client** / HTTP tool | — | ✅ Standard |
| db_connector | **database connector** | — | ✅ Standard |
| webhook | **webhook** | — | ✅ Standard |
| content_monetization | — | — | ❌ NOT a tool. Misplaced in P04. Should be P11 or P08. |
| daemon | **background service** / long-running process | — | ✅ Standard (Unix) |
| hook | **hook** / lifecycle hook | — | ✅ Standard |
| plugin | **plugin** / extension | — | ✅ Standard |
| vision_tool | **vision tool** / image analysis | OpenAI (vision), Anthropic (vision) | ✅ Aligned |
| audio_tool | **audio tool** / speech processing | OpenAI (audio) | ✅ Aligned |

### P05 Output — "O que o agente ENTREGA"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| response_format | **response format** / structured output | OpenAI (response_format param) | ✅ Industry standard |
| parser | **output parser** | LangChain | ✅ Aligned |
| formatter | **output formatter** | — | ✅ OK |
| output_validator | **output validator** | — | ✅ OK |
| landing_page | — | — | ⚠️ Not an LLM concept. Web dev artifact. |

### P06 Schema — "CONTRATOS de validacao"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| input_schema | **input schema** / request schema | OpenAI (structured outputs) | ✅ Aligned |
| validation_schema | **JSON schema** / validation schema | OpenAI, Anthropic | ✅ Aligned |
| type_def | **type definition** | TypeScript, Pydantic | ✅ Standard |
| interface | **interface** / API contract | — | ✅ Standard |
| validator | **validator** / schema validator | — | ✅ Standard |
| enum_def | **enum definition** | — | ✅ Standard |

### P07 Evals — "COMO medir qualidade"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| unit_eval | **unit evaluation** | OpenAI Evals | ✅ Aligned |
| smoke_eval | **smoke test** | Standard QA | ✅ Standard |
| e2e_eval | **end-to-end evaluation** | — | ✅ Standard |
| benchmark | **benchmark** | All (MMLU, HumanEval, etc.) | ✅ Industry standard |
| golden_test | **golden test** / reference test | — | ✅ Standard |
| scoring_rubric | **scoring rubric** / evaluation rubric | OpenAI Evals, Anthropic | ✅ Aligned |
| llm_judge | **LLM-as-judge** | OpenAI, Anthropic research | ✅ Industry standard |
| eval_dataset | **evaluation dataset** | All | ✅ Industry standard |
| red_team_eval | **red teaming** | Anthropic, OpenAI (safety) | ✅ Industry standard |
| regression_check | **regression test** | Standard QA | ✅ Standard |
| trace_config | **trace configuration** / observability config | LangSmith, Weights & Biases | ✅ Aligned |

### P08 Architecture — "COMO escala"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| agent_card | **agent card** | Google A2A | ✅ Industry standard (just renamed!) |
| pattern | **design pattern** | Software eng. | ✅ Standard |
| law | **architectural invariant** / hard constraint | — | ⚠️ "Law" is strong. "Invariant" or "constraint" is industry. |
| diagram | **architecture diagram** | — | ✅ Standard |
| component_map | **component map** / service map | — | ✅ Standard |
| director | **orchestrator** / supervisor | LangGraph | ⚠️ Overlaps with P12. "Director" not industry standard. |
| decision_record | **ADR** (Architecture Decision Record) | Standard eng. practice | ✅ Industry standard |
| naming_rule | **naming convention** | — | ✅ Standard |

### P09 Config — "COMO configura"

All kinds here are standard infrastructure terms. ✅ No issues.

### P10 Memory — "O que LEMBRA"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| knowledge_index | **knowledge index** / semantic index | LlamaIndex | ⚠️ "Brain" is metaphor. "Knowledge index" is industry. |
| entity_memory | **entity memory** | LangChain | ✅ Industry standard |
| learning_record | **learning record** / experience log | — | ✅ OK |
| memory_summary | **conversation summary** / memory summary | LangChain | ✅ Aligned |
| runtime_state | **runtime state** / session state | — | ✅ Standard |
| session_state | **session state** | — | ✅ Standard |
| session_backend | **session backend** / state store | — | ✅ Standard |
| compression_config | **context compression** config | LangChain | ✅ Aligned |
| memory_type | **memory type** / memory taxonomy | — | ✅ OK |

### P11 Feedback — "COMO melhora"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| quality_gate | **quality gate** | CI/CD standard | ✅ Industry standard |
| bugloop | **bug detection loop** / error correction cycle | — | ✅ CEX-specific, valid |
| guardrail | **guardrail** | OpenAI Agents SDK, Anthropic | ✅ Industry standard |
| lifecycle_rule | **lifecycle hook** / lifecycle rule | — | ✅ Standard |
| optimizer | **optimizer** / performance tuner | — | ✅ Standard |
| reward_signal | **reward signal** / RLHF reward | OpenAI, Anthropic (RLHF) | ✅ Aligned |

### P12 Orchestration — "COMO coordena"

| CEX kind | Industry term | Provider | Status |
|----------|--------------|----------|--------|
| workflow | **workflow** / pipeline | All | ✅ Industry standard |
| dag | **DAG** (directed acyclic graph) | Airflow, LangGraph | ✅ Industry standard |
| spawn_config | **spawn configuration** / process config | — | ✅ Standard |
| signal | **signal** / event | POSIX, event-driven | ✅ Industry standard |
| handoff | **handoff** / task delegation | OpenAI Swarm/Agents SDK | ✅ Industry standard |
| dispatch_rule | **routing rule** / dispatch policy | — | ✅ OK |
| checkpoint | **checkpoint** / state snapshot | ML standard | ✅ Industry standard |
| schedule | **schedule** / cron schedule | — | ✅ Standard |
| workflow_primitive | **workflow primitive** / atomic operation | — | ✅ OK |

## Critical Findings

### PROBLEM 1: Schemas in Portuguese
ALL 12 _schema.yaml files use Portuguese descriptions:
- "O que o agente SABE" should be "What the agent KNOWS"
- "QUEM o agente EH" should be "WHO the agent IS"
- Fails the Llama-7B test. Non-PT models can't parse context.

### PROBLEM 2: 8 kinds with naming mismatches
| Kind | CEX name | Industry name | Fix |
|------|----------|---------------|-----|
| vector_store | vector_store | **vector_store** | Rename (LangChain, LlamaIndex standard) |
| knowledge_index | knowledge_index | **knowledge_index** | Rename (metaphor → industry) |
| code_executor | code_executor | **code_interpreter** | Consider rename (OpenAI term) |
| law | law | **invariant** | Consider rename |
| director | director | **supervisor** | Consider rename (LangGraph term) |
| axiom | axiom | **constitutional_principle** | Consider rename (Anthropic term) |
| mental_model | mental_model | **cognitive_profile** | Consider rename (avoid psych overlap) |
| content_monetization | content_monetization | — | Misplaced in P04 (not a tool) |

### PROBLEM 3: Missing kinds (industry has, CEX doesn't)
| Concept | Provider | Suggested pillar | Priority |
|---------|----------|-----------------|----------|
| **prompt_cache** | Anthropic, Google | P09 or P10 | Medium |
| **fine_tune_config** | OpenAI | P02 or P07 | Low (CEX is prompt-based) |
| **safety_filter** | All providers | P11 | Medium |
| **streaming_config** | All providers | P09 | Low |
| **context_window_config** | All | P09 or P10 | Medium |
| **multi_modal_config** | OpenAI, Anthropic, Google | P09 | Medium |
| **citation** | Anthropic, Google (grounding) | P01 | Medium |
| **trace** (not config) | LangSmith, W&B | P07 | Low |

## Recommendations

1. **URGENT**: Translate all _schema.yaml descriptions to English
2. **HIGH**: Rename 5 kinds that directly conflict with industry terms
3. **MEDIUM**: Add 4-5 missing kinds for major provider features
4. **LOW**: Move content_monetization from P04 to correct pillar
5. **ONGOING**: Cross-reference new provider releases quarterly
