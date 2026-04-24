---
id: kc_llm_vocabulary_atlas
kind: knowledge_card
8f: F3_inject
title: "LLM Vocabulary Atlas: Universal Term Registry"
version: "1.0.0"
quality: 8.8
tags: [vocabulary, atlas, taxonomy, standards, protocols, global]
pillar: P01
domain: llm-agent-vocabulary
density_score: 0.95
related:
  - cex_llm_vocabulary_whitepaper
  - taxonomy_completeness_audit
  - n07_memory_industry_audit
  - p01_kc_terminology_rosetta_stone
  - atom_03_openai_agents_sdk
  - atom_32_vendor_glossaries_adk
  - p01_report_intent_resolution
  - kc_llm_agent_frameworks
  - p01_kc_agent
  - atom_05_semantic_kernel
---

# LLM Vocabulary Atlas: Universal Term Registry

Cross-references 15 protocol/framework specs, 40+ academic papers, 10+ Chinese/8 Japanese/6 Korean/3 Indian frameworks, 40+ glossaries/ontologies, and 150+ bleeding-edge terms against CEX's 132 kinds and 12 pillars.

Key finding: No existing system maps typed vocabulary across the full LLM agent lifecycle. CEX `kinds_meta.json` is the only such registry.

---

## 1. Universal Terms (converged across 3+ sources)

Terms appearing in 3+ major frameworks/papers with stable definitions.

| Term | Definition (1 line) | Sources | CEX Kind | CEX Pillar | Status |
|------|---------------------|---------|----------|------------|--------|
| Agent | Autonomous entity with identity, tools, and goals | A2A, MCP, OpenAI, LangChain, CrewAI, AutoGen, DSPy, Semantic Kernel, HF smolagents, Bedrock, Vertex ADK, Wang 2023, Xi 2023 | `agent` | P02 | established |
| Tool | Callable function an agent can invoke | MCP, OpenAI, LangChain, CrewAI, AutoGen, DSPy, Semantic Kernel, Haystack, Bedrock | `function_def` / `toolkit` | P04 | established |
| Tool Use / Function Calling | LLM selecting and invoking tools | OpenAI, Anthropic, Gemini, LangChain, MCP, Bedrock | `function_def` | P04 | established |
| Handoff | Transfer of control between agents | A2A, OpenAI Agents SDK, LangGraph, CrewAI | `handoff` / `handoff_protocol` | P12/P02 | established |
| Guardrail | Safety constraint on agent behavior | OpenAI, NVIDIA NeMo, LangChain, Anthropic, Aegis 2.0 | `guardrail` | P11 | established |
| Session | Stateful conversation context | A2A, OpenAI, MCP, Bedrock, Vertex ADK | `session_state` | P10 | established |
| Task | Unit of work assigned to an agent | A2A, CrewAI, AutoGen, MetaGPT, ChatDev | `action_prompt` / `handoff` | P03/P12 | established |
| Pipeline | Sequence of processing stages | LangChain, Haystack, DSPy, MLOps, Vertex ADK | `chain` / `workflow` | P03/P12 | established |
| Runner / Executor | Runtime that executes agent pipelines | OpenAI Agents SDK, Haystack, LangGraph | `code_executor` / `workflow_primitive` | P04/P12 | established |
| Memory | Persistent state across interactions | LangChain, LlamaIndex, CrewAI, AutoGen, Wang 2023, Xi 2023 | `entity_memory` / `memory_scope` | P10/P02 | established |
| Provider / Model Provider | LLM API backend (Claude, GPT, Gemini) | LangChain, LiteLLM, Portkey, Bedrock, Vertex | `model_provider` | P02 | established |
| Callback / Tracing | Observability hooks for pipeline execution | LangChain, LlamaIndex, Haystack, OpenTelemetry | `trace_config` / `hook` | P07/P04 | established |
| Prompt Template | Reusable prompt with variable slots | LangChain, DSPy, Semantic Kernel, Haystack, Vercel AI SDK | `prompt_template` | P03 | established |
| System Prompt | Identity/instruction preamble for LLM | OpenAI, Anthropic, Google, all frameworks | `system_prompt` | P03 | established |
| Retriever | Component that fetches relevant documents | LangChain, LlamaIndex, Haystack, DSPy | `retriever` / `retriever_config` | P04/P01 | established |
| Embedder / Embedding Model | Converts text to vector representations | LangChain, LlamaIndex, Haystack, Cohere, OpenAI | `embedding_config` / `embedder_provider` | P01 | established |
| Node / Step | Single unit in a graph/pipeline | LangGraph, LlamaIndex, Haystack, Semantic Kernel | `workflow_primitive` | P12 | established |
| Schema / Signature | Typed input/output contract | DSPy, OpenAI, JSON Schema, Pydantic, A2A | `input_schema` / `validation_schema` | P06 | established |
| Artifact | Versioned output of a pipeline stage | MLflow, W&B, CEX, CI/CD | `knowledge_card` (generic) | P01 | established |
| Flow / Workflow | Multi-step orchestrated process | LangGraph, Prefect, CrewAI, AutoGen, Vertex ADK | `workflow` / `dag` | P12 | established |
| Chain | Sequential prompt composition | LangChain, DSPy, Semantic Kernel | `chain` | P03 | established |
| RAG (Retrieval-Augmented Generation) | Pattern combining retrieval + generation | LlamaIndex, LangChain, Haystack, Gao 2023 | `retriever` + `chunk_strategy` + `embedding_config` | P01/P04 | established |
| Vector Store | Database for embedding similarity search | LlamaIndex, LangChain, Haystack, Pinecone, Weaviate | `vector_store` / `knowledge_index` | P01/P10 | established |
| Chunk / Chunking | Splitting documents for embedding | LlamaIndex, LangChain, Haystack | `chunk_strategy` | P01 | established |
| Document Loader | Ingests files into pipeline | LangChain, LlamaIndex, Haystack | `document_loader` | P04 | established |
| Router | Directs tasks to appropriate handlers | LangGraph, Semantic Kernel, Haystack | `router` / `dispatch_rule` | P02/P12 | established |
| Evaluator / Judge | Assesses output quality | RAGAS, DeepEval, OpenAI Evals, Braintrust | `llm_judge` / `scoring_rubric` | P07 | established |
| Benchmark | Quantitative performance measurement | HELM, lm-eval-harness, MMLU, HumanEval | `benchmark` | P07 | established |
| Fine-tuning | Adapting model weights on custom data | OpenAI, HF, Vertex, Bedrock | `finetune_config` | P02 | established |
| Prompt Caching | Reusing computed prompt prefixes | Anthropic, OpenAI, Google | `prompt_cache` | P10 | established |
| Streaming | Real-time token-by-token output delivery | OpenAI SSE, Anthropic, Vercel AI SDK | `streaming_config` | P05 | established |
| MCP (Model Context Protocol) | Standard for tool/resource exposure | Anthropic (open standard) | `mcp_server` | P04 | established |
| A2A (Agent-to-Agent) | Standard for agent interop | Google (open standard) | `handoff_protocol` / `interface` | P02/P06 | established |
| Structured Output | Constrained JSON/schema generation | OpenAI, Anthropic, DSPy, Outlines | `response_format` / `constraint_spec` | P05/P03 | established |
| Reasoning Trace / CoT | Step-by-step thinking before answer | OpenAI o-series, Anthropic Claude, DeepSeek | `reasoning_trace` | P03 | established |
| Few-Shot Example | Input/output pair for in-context learning | All LLM frameworks | `few_shot_example` | P01 | established |
| Knowledge Graph | Entity-relation structured knowledge | LlamaIndex, Neo4j, Microsoft GraphRAG | `knowledge_graph` | P01 | emerging |
| Red Teaming | Adversarial safety testing | Anthropic, OpenAI, NIST, HarmBench | `red_team_eval` | P07 | established |
| Agent Card | Machine-readable agent capability descriptor | Google A2A, CEX | `agent_card` | P08 | emerging |
| Supervisor / Orchestrator | Meta-agent coordinating other agents | LangGraph, AutoGen, CrewAI | `supervisor` | P08 | established |
| Human-in-the-Loop (HITL) | Human approval gate in agent pipeline | LangGraph, CrewAI, Anthropic | `hitl_config` | P11 | established |
| Batch Processing | Async bulk API operations | OpenAI Batch, Anthropic Batches | `batch_config` | P09 | established |
| Feature Flag | Runtime toggle for capabilities | LaunchDarkly, Flagsmith, custom | `feature_flag` | P09 | established |
| Rate Limit | Throughput constraint (RPM/TPM) | All providers, all gateways | `rate_limit_config` | P09 | established |
| Experiment | A/B test for prompts/models | MLflow, W&B, Braintrust | `experiment_config` | P09 | established |
| Ontology | Formal classification system | OWL, SKOS, schema.org | `ontology` | P01 | established |
| Plugin | Hot-pluggable extension | ChatGPT Plugins, Semantic Kernel | `plugin` | P04 | established |
| Webhook | HTTP event-driven endpoint | All integration platforms | `webhook` | P04 | established |
| Daemon | Persistent background process | POSIX, systemd | `daemon` | P04 | established |
| DAG | Directed acyclic graph of dependencies | Airflow, Prefect, Dagster | `dag` | P12 | established |
| Checkpoint | Saved pipeline state for resumption | PyTorch, MLflow, LangGraph | `checkpoint` | P12 | established |
| Signal | Inter-agent event notification | POSIX, event-driven arch | `signal` | P12 | established |
| Fallback Chain | Ordered model failover sequence | LiteLLM, Portkey, CEX | `fallback_chain` | P02 | emerging |
| Reward Signal | Continuous quality feedback | RLHF, DPO, CEX | `reward_signal` | P11 | emerging |
| Multimodal | Multiple input modalities (text+image+audio) | GPT-4V, Gemini, Claude | `multi_modal_config` | P04 | established |
| Computer Use | GUI automation by LLM | Anthropic, browser-use | `computer_use` | P04 | emerging |
| Cost Budget | Token/money spending limits | All providers | `cost_budget` | P09 | emerging |
| Compression | Context window optimization | LlamaIndex, LangChain | `compression_config` | P10 | emerging |

---

## 2. Protocol Vocabulary

| Protocol Term | A2A | MCP | OpenAI Agents SDK | CEX Kind | CEX Pillar |
|---------------|-----|-----|-------------------|----------|------------|
| Agent | AgentCard | -- | Agent | `agent` | P02 |
| Agent Card | AgentCard (.well-known/agent.json) | -- | -- | `agent_card` | P08 |
| Task | Task (pending/working/done) | -- | -- | `handoff` | P12 |
| Tool | -- | Tool (JSON Schema) | function_tool | `function_def` | P04 |
| Resource | -- | Resource (URI-addressed) | -- | `rag_source` | P01 |
| Prompt | -- | Prompt (server-side template) | -- | `prompt_template` | P03 |
| Server | -- | MCP Server | -- | `mcp_server` | P04 |
| Handoff | -- | -- | Handoff (transfer_to_agent) | `handoff` | P12 |
| Guardrail | -- | -- | InputGuardrail / OutputGuardrail | `guardrail` | P11 |
| Runner | -- | -- | Runner (run loop) | `workflow_primitive` | P12 |
| Tracing | -- | -- | TracingProcessor | `trace_config` | P07 |
| Session | Session (task lifecycle) | Session (transport) | -- | `session_state` | P10 |
| Artifact | Artifact (task output parts) | -- | -- | `knowledge_card` | P01 |
| Message | Message (agent-to-agent) | Message (client-server) | Message (conversation) | `signal` | P12 |
| Streaming | StreamingMessage | SSE transport | stream_events | `streaming_config` | P05 |
| Authentication | OAuth 2.0 / API Key | OAuth 2.0 | API Key | `secret_config` | P09 |
| Push Notification | webhook-based | -- | -- | `webhook` | P04 |
| Capability | skills[] in AgentCard | capabilities{} | -- | `skill` | P04 |

---

## 3. Framework Vocabulary

| Framework Term | LangChain | LlamaIndex | CrewAI | AutoGen | DSPy | Semantic Kernel | Haystack | Vercel AI SDK | HF smolagents | Bedrock | Vertex ADK | CEX Kind | CEX Pillar |
|----------------|-----------|------------|--------|---------|------|-----------------|----------|---------------|---------------|---------|------------|----------|------------|
| Agent | Agent / AgentExecutor | Agent | Agent | ConversableAgent | -- | Agent | Agent | -- | Agent | Agent | Agent | `agent` | P02 |
| Tool | Tool / BaseTool | FunctionTool | Tool | register_function | tool() decorator | KernelFunction | Tool | tool() | Tool / @tool | Action | Tool | `function_def` | P04 |
| Chain | LCEL chain | QueryPipeline | -- | -- | Module/ChainOfThought | -- | Pipeline | -- | -- | Chain | -- | `chain` | P03 |
| Memory | ConversationBuffer/Summary | ChatMemoryBuffer | Memory (short/long/entity) | -- | -- | ChatHistory | ChatMessageStore | -- | -- | Memory | Session | `entity_memory` | P10 |
| Retriever | BaseRetriever | QueryEngine | -- | -- | Retrieve | -- | Retriever | -- | -- | KnowledgeBase | -- | `retriever` | P04 |
| Embedder | Embeddings | -- | -- | -- | -- | -- | Embedder | embed() | -- | -- | -- | `embedding_config` | P01 |
| Prompt | PromptTemplate | PromptTemplate | -- | -- | Signature | PromptTemplate | PromptBuilder | -- | -- | PromptTemplate | -- | `prompt_template` | P03 |
| Router | RouterChain | RouterQueryEngine | -- | GroupChat | -- | -- | Router | -- | -- | -- | -- | `router` | P02 |
| Callback | Callbacks | Callbacks | -- | -- | -- | Filters | -- | callbacks | -- | -- | Callbacks | `hook` | P04 |
| Graph | LangGraph StateGraph | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | `dag` | P12 |
| Node | Node (LangGraph) | Node (index) | -- | -- | -- | Step | Component | -- | -- | -- | -- | `workflow_primitive` | P12 |
| Structured Output | with_structured_output | -- | -- | -- | TypedPredictor | -- | -- | generateObject | -- | -- | -- | `response_format` | P05 |
| Document | Document | Document | -- | -- | Example | -- | Document | -- | -- | -- | -- | `knowledge_card` | P01 |
| Splitter | TextSplitter | NodeParser | -- | -- | -- | -- | DocumentSplitter | -- | -- | -- | -- | `chunk_strategy` | P01 |
| VectorStore | VectorStore | VectorStoreIndex | -- | -- | -- | -- | DocumentStore | -- | -- | -- | -- | `vector_store` | P01 |
| Evaluator | LangSmith Evaluator | -- | -- | -- | Evaluate | -- | -- | -- | -- | -- | EvalService | `llm_judge` | P07 |
| Guardrail | -- | -- | -- | -- | Assert/Suggest | InputFilter | -- | -- | -- | Guardrails | -- | `guardrail` | P11 |
| Crew / Team | -- | -- | Crew | GroupChat | -- | -- | -- | -- | ManagedAgent | -- | Team | `supervisor` | P08 |
| Handoff | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | transfer_to_agent | `handoff` | P12 |

---

## 4. Global Framework Vocabulary

### Chinese Frameworks

| Framework | Stars | Unique Terms | Definition | CEX Kind | CEX Pillar |
|-----------|-------|-------------|------------|----------|------------|
| AgentScope (Alibaba) | 23K | ServiceNode | Distributed agent node | `workflow_primitive` | P12 |
| AgentScope | -- | Msg (dict subclass) | Universal message format | `signal` | P12 |
| AgentScope | -- | Pipeline (sequential/if-else/switch/for/while) | Control flow primitives | `workflow` | P12 |
| Dify (open) | 60K | DSL (YAML workflow) | Visual workflow definition | `workflow` | P12 |
| Dify | -- | Knowledge (dataset API) | RAG knowledge base | `rag_source` | P01 |
| Dify | -- | Completion/Chat Message | API message types | `action_prompt` | P03 |
| Coze (ByteDance) | -- | Bot | Agent with plugins/knowledge/workflow | `agent` | P02 |
| Coze | -- | Workflow Node | Visual pipeline step | `workflow_primitive` | P12 |
| MetaGPT | 40K | Role | Agent with profile/goal/constraints | `agent` | P02 |
| MetaGPT | -- | Action | Executable function within Role | `function_def` | P04 |
| MetaGPT | -- | SOP (Standard Operating Procedure) | Multi-role process definition | `workflow` | P12 |
| MetaGPT | -- | Environment | Shared context between Roles | `session_state` | P10 |
| ChatDev | 25K | Phase | Conversation round between roles | `workflow_primitive` | P12 |
| ChatDev | -- | ChatChain | End-to-end development pipeline | `chain` | P03 |
| XAgent | 8K | ToolServer | Sandboxed tool execution environment | `code_executor` | P04 |
| XAgent | -- | PlanEngine | Hierarchical task decomposition | `dag` | P12 |

### Cross-cutting Chinese concepts

| Concept | Origin | Definition | CEX Kind | CEX Pillar |
|---------|--------|------------|----------|------------|
| Interleaved Thinking | DeepSeek, Qwen | Alternating reasoning + action steps | `reasoning_trace` | P03 |
| 300-step tool chains | XAgent | Ultra-long sequential tool execution | `workflow` | P12 |
| SOPs-as-prompts | MetaGPT | Process definitions compiled to prompts | `prompt_compiler` | P03 |
| Thinking-with-Tools | Qwen | Tool calls embedded in reasoning chain | `reasoning_trace` + `function_def` | P03/P04 |

### Japanese Frameworks

| Framework | Org | Unique Terms | Definition | CEX Kind | CEX Pillar |
|-----------|-----|-------------|------------|----------|------------|
| Sakana AI | Sakana | Self-Evolving Agent | Agent that modifies own code | `optimizer` | P11 |
| Sakana AI | -- | AI Scientist | Research paper generation pipeline | `research_pipeline` | P04 |
| cotomi Act | NEC | cotomi Act Agent | Enterprise agent with domain tools | `agent` | P02 |
| tsuzumi | NTT | Adapter Hub | LoRA adapter selection per task | `finetune_config` | P02 |
| tsuzumi | -- | Domain Adapter | Task-specific model specialization | `finetune_config` | P02 |

### Korean Frameworks

| Framework | Org | Unique Terms | Definition | CEX Kind | CEX Pillar |
|-----------|-----|-------------|------------|----------|------------|
| Kanana-2 | Kakao | PlayMCP | MCP-native tool integration | `mcp_server` | P04 |
| HyperCLOVA X | Naver | CLOVA Studio | Model serving + fine-tuning platform | `model_provider` | P02 |
| HyperCLOVA X | -- | Skill (HCX) | Callable capability module | `skill` | P04 |
| Solar Pro3 | Upstage | Document AI | Document parsing + understanding | `document_loader` | P04 |
| (Korean arch.) | Various | P-C-G (Perception-Cognition-Generation) | 3-module agent architecture | `agent` components | P02/P03/P05 |

### Indian Frameworks

| Framework | Org | Unique Terms | Definition | CEX Kind | CEX Pillar |
|-----------|-----|-------------|------------|----------|------------|
| Sarvam | Sarvam AI | 22-language pipeline | Multilingual tokenizer + inference | `model_provider` | P02 |
| Krutrim | Ola | Voice-first agent | Speech-native agent interface | `audio_tool` | P04 |
| AI4Bharat | IIT consortium | IndicTrans / IndicBERT | Indic language foundation models | `model_card` | P02 |

---

## 5. Academic Taxonomy Map

| Paper (short ref) | Taxonomy Structure | Key Terms | CEX Pillar Mapping |
|--------------------|-------------------|-----------|-------------------|
| Wang 2023 (Survey on LLM Agents) | 4 components: Profiling, Memory, Planning, Action | profile module, memory stream, plan-and-execute, ReAct | P02 (profiling), P10 (memory), P12 (planning), P04 (action) |
| Xi 2023 (Rise and Potential) | 3 modules: Brain, Perception, Action | cognitive architecture, environment perception, tool use | P02/P03 (brain), P04 (perception), P04 (action) |
| 2601.12560 (6-component) | Perception, Memory, Planning, Reflection, Action, Profiling | sensor module, episodic memory, plan decomposition, self-reflection | P04, P10, P12, P11, P04, P02 |
| Prompt Report (2406.06608) | 33 terms + 58 techniques | zero-shot, few-shot, CoT, ToT, self-consistency, role prompting | P03 (all prompt techniques) |
| Gao 2023 (RAG Survey) | 3 paradigms: Naive, Advanced, Modular | retrieve-then-read, iterative retrieval, adaptive RAG | P01 (naive), P01/P04 (advanced), P04 (modular) |
| 2504.15965 (Memory Survey) | 3 types: Episodic, Semantic, Procedural | experience replay, fact storage, skill memory | P10 (episodic=`entity_memory`), P01 (semantic=`knowledge_card`), P04 (procedural=`skill`) |
| Aegis 2.0 (Safety) | 12+9 hazard categories | hate speech, self-harm, CSAM, privacy, misinformation | P11 (`guardrail` per category) |
| CLASSic (Eval Framework) | 5 dimensions: Cost, Latency, Accuracy, Security, Stability | token cost, TTFT, task accuracy, jailbreak resistance, output variance | P09 (cost), P07 (latency/accuracy), P11 (security), P07 (stability) |
| 2405.10467 (Design Patterns) | 18 architectural patterns | supervisor, handoff, map-reduce, reflection, tool-use, planning | P08 (`pattern`) -- 1:1 map to CEX patterns |
| STORM (paper) | 4 stages: Discover, Outline, Draft, Polish | perspective-guided QA, multi-source synthesis | P04 (`research_pipeline`) |
| CRAG (2401.15884) | 3 actions: Correct, Incorrect, Ambiguous | retrieval evaluator, knowledge refinement, web search augmentation | P04 (`retriever`) + P11 (`quality_gate`) |
| DSPy (2310.03714) | Modules + Optimizers + Metrics | Predict, ChainOfThought, ReAct, BootstrapFewShot, MIPRO | P03 (`prompt_template`, `chain`), P07 (`scoring_rubric`) |
| ToolBench (2305.16504) | 3-level tool taxonomy: category, tool, API | 16K+ real APIs, instruction tuning, tool retrieval | P04 (`function_def`, `toolkit`) |
| ReAct (2210.03629) | Interleaved Reasoning + Acting | thought, action, observation loop | P03 (`reasoning_trace`) + P04 (`function_def`) |
| Tree of Thoughts (2305.10601) | Tree search over reasoning paths | BFS/DFS over thoughts, evaluation heuristic | P03 (`reasoning_trace`) + P12 (`dag`) |
| Reflexion (2303.11366) | Self-reflection + retry | verbal reinforcement, episodic memory buffer | P11 (`reward_signal`) + P10 (`entity_memory`) |
| CAMEL (2303.17760) | Role-playing agent communication | inception prompting, task decomposition, role specialization | P03 (`system_prompt`) + P02 (`agent`) |

---

## 6. Standards & Ontologies

| Standard / Glossary | Org | Term Count | Format | Ingestible? | URL |
|---------------------|-----|------------|--------|-------------|-----|
| NIST AI 600-1 (AI RMF) | NIST | 511 terms | PDF + CSV glossary | YES (CSV) | csrc.nist.gov/glossary |
| ML Ontology (MLOnto) | W3C community | 700 individuals | OWL/RDF | YES (RDF parse) | ml-schema.github.io/documentation |
| Google ML Glossary | Google | 500+ terms | HTML | YES (scrape structured divs) | developers.google.com/machine-learning/glossary |
| A2A Protocol | Google | ~30 core terms | .proto (protobuf) | YES (parse .proto) | github.com/google/A2A |
| MCP Specification | Anthropic | ~25 core terms | JSON Schema | YES (parse schema) | spec.modelcontextprotocol.io |
| OpenAI API Reference | OpenAI | ~40 terms | OpenAPI spec | YES (parse OpenAPI) | platform.openai.com/docs/api-reference |
| Anthropic API Docs | Anthropic | ~35 terms | Markdown + JSON | YES (scrape) | docs.anthropic.com/en/api |
| HuggingFace Hub Docs | HF | 200+ terms | Markdown | PARTIAL (unstructured) | huggingface.co/docs |
| MLflow Glossary | Databricks | ~50 terms | HTML | YES (structured) | mlflow.org/docs/latest/glossary.html |
| LangChain Glossary | LangChain | ~60 terms | Markdown | YES (parse MD) | python.langchain.com/docs/concepts |
| LlamaIndex Concepts | LlamaIndex | ~40 terms | Markdown | YES (parse MD) | docs.llamaindex.ai/en/stable/understanding |
| Weights & Biases Glossary | W&B | ~80 terms | HTML | YES (structured) | wandb.ai/site/articles/glossary |
| IEEE P3394 (Agent Standard) | IEEE | In development | TBD | NO (unreleased) | standards.ieee.org/ieee/3394 |
| ISO/IEC 22989:2022 | ISO/IEC | AI concepts + terminology | PDF | PARTIAL (paywall) | iso.org/standard/74296.html |
| OWASP LLM Top 10 | OWASP | 10 risk categories | Markdown | YES (structured) | owasp.org/www-project-top-10-for-large-language-model-applications |
| EU AI Act Glossary | EU | ~30 legal terms | PDF + HTML | PARTIAL (legal language) | artificialintelligenceact.eu |

---

## 7. Proposed New CEX Kinds

| Proposed Kind | Pillar | Source Evidence | Priority | Maturity |
|---------------|--------|-----------------|----------|----------|
| `sandbox_config` | P09 | E2B, Modal, Anthropic computer_use; all need isolated execution config | HIGH | Production-ready |
| `agent_registry` | P08 | A2A agent discovery, MLflow model registry pattern; needed for multi-agent routing | HIGH | Emerging standard |
| `tool_registry` | P04 | MCP tool discovery, ToolBench 16K APIs; typed tool catalog | HIGH | Production-ready |
| `edit_format` | P05 | Aider (diff/whole/udiff), Claude Code (search-replace); standardize code edit output | HIGH | Production-ready |
| `browser_session` | P04 | browser-use, Playwright MCP, Stagehand; stateful browser context | HIGH | Production-ready |
| `action_space` | P06 | RL/robotics (VLA), ReAct, ToolBench; formal action type definition | HIGH | Emerging |
| `thinking_budget` | P03 | Anthropic extended thinking, OpenAI reasoning_effort; token allocation for CoT | HIGH | Emerging |
| `episodic_memory` | P10 | 2504.15965 memory taxonomy, Reflexion, MemGPT; experience replay buffer | MEDIUM | Emerging |
| `realtime_session` | P09 | OpenAI Realtime API, WebSocket agents, voice-first (Krutrim) | MEDIUM | Emerging |
| `dom_distiller` | P04 | browser-use DOM pruning, Stagehand selectors; HTML simplification | MEDIUM | Emerging |
| `rolling_context_config` | P10 | Context window management, sliding window, summary-and-forget | MEDIUM | Emerging |
| `online_eval_config` | P07 | Production monitoring, Arize, WhyLabs; real-time quality tracking | MEDIUM | Emerging |
| `injection_detector` | P11 | OWASP LLM01, prompt injection research; input sanitization config | MEDIUM | Emerging |
| `tool_security_config` | P09 | MCP auth, tool permission scoping, sandboxing policy | MEDIUM | Emerging |
| `swarm_config` | P12 | OpenAI Swarm pattern, multi-agent coordination rules | MEDIUM | Experimental |
| `page_snapshot` | P04 | browser-use screenshots, visual grounding for web agents | LOW | Experimental |
| `mcts_config` | P03 | Tree of Thoughts, AlphaCode; Monte Carlo tree search for reasoning | LOW | Experimental |
| `vla_config` | P04 | Vision-Language-Action models (RT-2, Octo); robotics crossover | LOW | Experimental |
| `negotiation_protocol` | P06 | Multi-agent negotiation, CAMEL, debate protocols | LOW | Experimental |
| `prosody_config` | P04 | Voice agent intonation, OpenAI Realtime voice params | LOW | Experimental |
| `metacognition_config` | P03 | Self-reflection scheduling, Reflexion, metacognitive monitoring | LOW | Experimental |
| `safety_taxonomy` | P11 | Aegis 2.0 12+9 categories, NIST AI RMF; structured hazard classification | MEDIUM | Emerging |

---

## 8. Gap Analysis

| CEX Pillar | External Coverage | Gap Assessment | Action |
|------------|-------------------|----------------|--------|
| P01 Knowledge | Strong: RAG, embeddings, chunking, vector stores well-covered | Ontology/taxonomy kinds underused -- no formal SKOS/OWL integration yet | Ingest NIST + MLOnto glossaries as `ontology` artifacts |
| P02 Model | Strong: agent, provider, model_card all present | Missing `agent_registry` for multi-agent discovery (A2A pattern) | Add `agent_registry` kind (HIGH priority) |
| P03 Prompt | Strong: templates, chains, system prompts, reasoning traces | Missing `thinking_budget` for extended thinking allocation | Add `thinking_budget` kind (HIGH priority) |
| P04 Tools | Strong: 15 tool kinds cover most patterns | Missing `tool_registry` (catalog), `browser_session` (stateful), `dom_distiller` | Add 3 kinds (HIGH/MEDIUM priority) |
| P05 Output | Adequate: formatter, parser, response_format, streaming | Missing `edit_format` for code editing output standardization | Add `edit_format` kind (HIGH priority) |
| P06 Schema | Adequate: input_schema, validation_schema, type_def, interface | Missing `action_space` for formal action type definitions | Add `action_space` kind (HIGH priority) |
| P07 Evaluation | Strong: benchmark, eval types, judge, rubric, trace_config | Missing `online_eval_config` for production monitoring | Add `online_eval_config` kind (MEDIUM priority) |
| P08 Architecture | Adequate: agent_card, component_map, pattern, decision_record | Missing `agent_registry` for discovery/catalog | Covered by P02 proposal above |
| P09 Config | Strong: env, rate_limit, secret, feature_flag, cost_budget | Missing `sandbox_config`, `realtime_session`, `tool_security_config` | Add 3 kinds (HIGH/MEDIUM priority) |
| P10 Memory | Adequate: entity_memory, session_state, memory_summary | Missing `episodic_memory` (experience replay), `rolling_context_config` | Add 2 kinds (MEDIUM priority) |
| P11 Feedback | Strong: guardrail, quality_gate, bugloop, reward_signal | Missing `injection_detector`, `safety_taxonomy` | Add 2 kinds (MEDIUM priority) |
| P12 Orchestration | Strong: workflow, dag, signal, handoff, checkpoint, spawn | Missing `swarm_config` for multi-agent swarm patterns | Add `swarm_config` kind (MEDIUM priority) |

---

## 9. Cross-Language Term Map

| English | Chinese (zh) | Japanese (ja) | Korean (ko) | CEX Kind |
|---------|-------------|---------------|-------------|----------|
| Agent | zhi neng ti / dai li | eejento | eijeonnteu | `agent` |
| Tool | gong ju | tsuuru | tul | `function_def` |
| Memory | ji yi | memori | memoli | `entity_memory` |
| Workflow | gong zuo liu | waakufuroo | wokeupeullou | `workflow` |
| Retrieval | jian suo | kensaku | geomssaeg | `retriever` |
| Embedding | xiang liang hua | enbedingu | imbeding | `embedding_config` |
| Prompt | ti shi ci | puronputo | peulompteu | `prompt_template` |
| Knowledge Base | zhi shi ku | chishiki beesu | jisig giban | `knowledge_card` |
| Fine-tuning | wei tiao | fainchuu ningu | paintyuning | `finetune_config` |
| Guardrail | hu lan | gadoreru | gadeuleyil | `guardrail` |
| Evaluation | ping gu | hyouka | pyeong-ga | `scoring_rubric` |
| Pipeline | liu shui xian | paipurain | paibeulain | `workflow` |
| Handoff | jiao jie | handoofu | haendeuopeu | `handoff` |
| Router | lu you qi | ruutaa | lauteo | `router` |
| Supervisor | du dao zhe / guan li yuan | suupabaizaa | seupeobaijeo | `supervisor` |
| Role (MetaGPT) | jue se | rooru | yeoghal | `agent` |
| SOP (MetaGPT) | biao zhun cao zuo gui cheng | esuoopii | pyojun jageopjeolcha | `workflow` |
| Action (MetaGPT) | dong zuo | akushon | aegsyeon | `function_def` |
| Session | hui hua | sesshon | sesyeon | `session_state` |
| Streaming | liu shi | sutoriimingu | seuteuliming | `streaming_config` |

Note: Romanized forms shown for readability (source file is ASCII-only per project rules). Actual CJK characters available in YAML data files.

---

## 10. Ingestion Roadmap

Ranked by signal density, machine-readability, and strategic value.

| Rank | Source | Format | Term Count | Action | Effort |
|------|--------|--------|------------|--------|--------|
| 1 | NIST AI Glossary (CSV) | CSV | 511 | Parse CSV -> `glossary_entry` artifacts per term | LOW |
| 2 | A2A .proto files | Protobuf | ~30 | Parse protobuf -> `interface` + `type_def` artifacts | LOW |
| 3 | MCP JSON Schema | JSON Schema | ~25 | Parse schema -> `input_schema` + `function_def` artifacts | LOW |
| 4 | OpenAI OpenAPI spec | OpenAPI 3.x | ~40 | Parse spec -> `api_client` + `type_def` artifacts | LOW |
| 5 | LangChain concepts docs | Markdown (structured) | ~60 | Parse h2/h3 sections -> `glossary_entry` artifacts | MEDIUM |
| 6 | LlamaIndex concepts docs | Markdown (structured) | ~40 | Parse h2/h3 sections -> `glossary_entry` artifacts | MEDIUM |
| 7 | Google ML Glossary | HTML (dl/dt/dd) | 500+ | Scrape definition list -> `glossary_entry` artifacts | MEDIUM |
| 8 | ML Ontology (OWL/RDF) | RDF/OWL | 700 | Parse RDF -> `ontology` artifact + entity extraction | HIGH |
| 9 | W&B Glossary | HTML (structured) | ~80 | Scrape -> `glossary_entry` artifacts | MEDIUM |
| 10 | MLflow Glossary | HTML | ~50 | Scrape -> `glossary_entry` artifacts | MEDIUM |
| 11 | HuggingFace Hub Docs | Markdown (mixed) | 200+ | Selective parse -> `glossary_entry` for unique terms | HIGH |
| 12 | OWASP LLM Top 10 | Markdown | 10 categories | Parse -> `guardrail` artifacts (1 per risk) | LOW |
| 13 | Anthropic API Docs | Markdown + JSON | ~35 | Parse -> `function_def` + `type_def` | MEDIUM |
| 14 | DSPy source code | Python docstrings | ~20 modules | Parse docstrings -> `glossary_entry` + `pattern` | HIGH |
| 15 | Aegis 2.0 taxonomy | Paper tables | 21 categories | Manual extract -> `safety_taxonomy` kind (proposed) | MEDIUM |

### Ingestion pipeline recommendation

```
Source -> document_loader -> chunk_strategy -> glossary_entry/ontology artifacts
  |                                               |
  +-> cex_compile.py -> kinds_meta.json update     |
  +-> cex_retriever.py index rebuild <-------------+
```

Priority: Sources 1-4 (structured, machine-readable) can be ingested with a single Python script. Sources 5-10 require light scraping. Sources 11-15 require manual curation or LLM-assisted extraction.

---

## Appendix: CEX Kind Coverage Summary

| Pillar | Kind Count | Core Kinds | Non-Core Kinds |
|--------|-----------|------------|----------------|
| P01 Knowledge | 13 | 6 | 7 |
| P02 Model | 13 | 6 | 7 |
| P03 Prompt | 10 | 6 | 4 |
| P04 Tools | 18 | 8 | 10 |
| P05 Output | 6 | 3 | 3 |
| P06 Schema | 7 | 5 | 2 |
| P07 Evaluation | 10 | 5 | 5 |
| P08 Architecture | 7 | 3 | 4 |
| P09 Config | 11 | 5 | 6 |
| P10 Memory | 10 | 5 | 5 |
| P11 Feedback | 9 | 4 | 5 |
| P12 Orchestration | 10 | 6 | 4 |
| **TOTAL** | **124** | **62** | **62** |

Note: 8 kinds have dual-pillar assignments in practice (e.g., `retriever` P04 + `retriever_config` P01). Total unique kinds in registry: 132.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.46 |
| [[taxonomy_completeness_audit]] | sibling | 0.33 |
| [[n07_memory_industry_audit]] | downstream | 0.28 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.28 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.28 |
| [[atom_32_vendor_glossaries_adk]] | sibling | 0.26 |
| [[p01_report_intent_resolution]] | sibling | 0.26 |
| [[kc_llm_agent_frameworks]] | sibling | 0.26 |
| [[p01_kc_agent]] | sibling | 0.24 |
| [[atom_05_semantic_kernel]] | sibling | 0.22 |
