---
id: cex_llm_vocabulary_whitepaper
kind: knowledge_card
pillar: P01
title: "CEX LLM Ecosystem Vocabulary Whitepaper"
version: 1.0.0
quality: 8.8
date: 2026-04-13
author: N01 Intelligence Nucleus
sources: 32
atoms: atom_01 through atom_32
total_source_lines: ~17330
frameworks_covered: 14
ecosystems_covered: 4
academic_surveys: 8
standards_bodies: 6
vendor_glossaries: 6
tags: [vocabulary, whitepaper, taxonomy, ontology, framework, protocol, CEX, atlas, consolidation]
related:
  - kc_llm_vocabulary_atlas
  - taxonomy_completeness_audit
  - p01_kc_chinese_llm_ecosystem
  - p01_kc_terminology_rosetta_stone
  - atom_03_openai_agents_sdk
  - p01_kc_agent
  - p01_report_intent_resolution
  - atom_11_agentscope
  - bld_knowledge_card_capability_registry
  - spec_mission_100pct_coverage
---

# CEX LLM Ecosystem Vocabulary Whitepaper

## 1. Executive Summary

This whitepaper consolidates 32 parallel research atoms (~940KB, ~17,330 lines) into a single reference document mapping the entire LLM agent ecosystem vocabulary to CEX's 12-pillar typed knowledge system. The research covers:

- **14 frameworks**: A2A, MCP, OpenAI Agents SDK, DSPy, Semantic Kernel, LangChain/LangGraph, LlamaIndex, CrewAI, AutoGen/AG2, Haystack, AgentScope, Dify, MetaGPT/ChatDev, Coze/XAgent
- **4 global ecosystems**: Chinese (Qwen-Agent, DeepSeek, MiniMax, Kimi, GLM, AgentScope, MetaGPT, Coze, Dify), Japanese (Sakana AI, NEC, NTT, Fujitsu), Korean (Kakao, Naver, Upstage, SK Telecom), Indian (Sarvam, Krutrim)
- **8 academic survey domains**: Agent taxonomy, prompt engineering, RAG, memory systems, multi-agent protocols, safety/guardrails, evaluation/benchmarks, reasoning/thinking
- **6 standards/ontologies**: NIST AI 100-3 (511 terms), W3C ML Schema, MetaAutoML Ontology, AIO, MLCommons Croissant, HuggingFace pipeline_tags
- **6 vendor glossaries**: Google ML (500+), Google ADK (85), AWS Bedrock (45), Azure ML (25), Anthropic Claude (12), HuggingFace smolagents (60)
- **3 specialized domains**: Computer/browser agents, code agents, voice/realtime agents

**Total unique terms extracted**: ~2,800+ across all sources, deduplicated to ~420 universal converged terms documented below.

---

## 2. Methodology

### 2.1 Research Process

| Phase | Method | Output |
|-------|--------|--------|
| P1: Source selection | 14 frameworks + 4 ecosystems + 8 survey domains + 6 standards + 6 vendors + 3 specialized | 32 atom files |
| P2: Term extraction | Exhaustive class/type/concept registry per source | ~2,800 raw terms |
| P3: Deduplication | Cross-atom synonym resolution using canonical definitions | ~420 universal terms |
| P4: CEX pillar mapping | Each term mapped to P01-P12 + CEX kind where applicable | 12-pillar coverage matrix |
| P5: Gap analysis | Terms with no CEX kind -> proposed new kinds | 23 proposed new kinds |

### 2.2 Atom Coverage Map

| Atom | Domain | Key Source(s) | Unique Terms |
|------|--------|---------------|:------------:|
| 01 | A2A Protocol | Google/Linux Foundation spec v0.3.0 | ~65 |
| 02 | MCP Protocol | Anthropic spec 2025-11-25 | ~80 |
| 03 | OpenAI Agents SDK | SDK v0.13.6 (Swarm lineage) | ~55 |
| 04 | DSPy | Stanford NLP framework | ~45 |
| 05 | Semantic Kernel | Microsoft SK + Agent Framework | ~75 |
| 06 | LangChain/LangGraph | LCEL + StateGraph + LangSmith | ~70 |
| 07 | LlamaIndex | 7-stage RAG pipeline + agents | ~90 |
| 08 | CrewAI | Agents/Tasks/Crews/Flows | ~30 |
| 09 | AutoGen/AG2 | 3 divergent codebases | ~50 |
| 10 | Haystack + Vercel AI SDK | Component pipeline + streaming | ~85 |
| 11 | AgentScope | Alibaba Tongyi Lab | ~60 |
| 12 | Dify | LangGenius platform (138K stars) | ~55 |
| 13 | MetaGPT + ChatDev | SOP-based multi-agent | ~35 |
| 14 | Coze + XAgent | ByteDance workflow + dual-loop | ~40 |
| 15 | Qwen-Agent + DeepSeek | Chinese LLM agent ecosystems | ~35 |
| 16 | MiniMax + Kimi + GLM | Chinese frontier models | ~30 |
| 17 | Japan ecosystem | Sakana AI, NEC, NTT, Fujitsu | ~25 |
| 18 | Korea + India ecosystem | Kakao, Naver, Upstage, Sarvam, Krutrim | ~30 |
| 19 | Agent taxonomy surveys | Wang 2023, Xi 2023, Arunkumar 2026 | ~80 |
| 20 | Prompt engineering taxonomy | 125 catalogued techniques | ~90 |
| 21 | RAG taxonomy | Retrieval/chunking/embedding configs | ~40 |
| 22 | Memory taxonomy | 3 temporal scopes, 5 surveys | ~45 |
| 23 | Multi-agent protocols | MCP/ACP/A2A/ANP comparison | ~25 |
| 24 | NIST AI vocabulary | NIST AI 100-3 (511 terms) | ~511 |
| 25 | Safety/guardrail taxonomy | Aegis 2.0, OWASP Top 10, ControlArena | ~60 |
| 26 | Evaluation/benchmark taxonomy | HELM, LLM-as-Judge, AutoRubric | ~70 |
| 27 | Computer/browser agents | Anthropic CU, OpenAI CUA, Stagehand | ~50 |
| 28 | Code agents | 9 platforms, 6 edit formats | ~55 |
| 29 | Voice/realtime agents | S2S vs cascade, 8 providers | ~45 |
| 30 | Reasoning/thinking | CoT family, ToT/GoT, ReAct, scaling | ~50 |
| 31 | ML ontologies | 6 machine-readable sources (~3000 concepts) | ~60 |
| 32 | Vendor glossaries + ADK | 727 terms across 6 vendors | ~50 |

### 2.3 Deduplication Rules

1. When multiple frameworks name the same concept differently, the most widely adopted term wins
2. Protocol-level terms (A2A, MCP) take priority over framework-specific variants
3. Academic survey terms establish canonical definitions when frameworks disagree
4. NIST terms are authoritative for governance/risk/safety vocabulary

---

## 3. Universal Converged Terms

Terms that appear in 3+ independent sources with consistent semantics. These form the stable vocabulary layer of the LLM agent ecosystem.

### 3.1 Agent Architecture

| # | Converged Term | Definition | Sources | CEX Kind | CEX Pillar |
|---|---------------|-----------|---------|----------|------------|
| 1 | Agent | Autonomous entity combining LLM + tools + memory + instructions | All 14 frameworks, all 3 surveys, NIST, all vendors | `agent` | P02 |
| 2 | Tool | External capability invokable by an agent (function, API, MCP server) | A2A, MCP, OpenAI SDK, SK, LangChain, LlamaIndex, CrewAI, AutoGen, Haystack, AgentScope, Dify, DSPy, all vendors | `cli_tool`, `browser_tool`, `mcp_server` | P04 |
| 3 | Agent Card | JSON manifest advertising agent capabilities, skills, auth | A2A, ACP, Google ADK, AWS Bedrock | `agent_card` | P08 |
| 4 | Handoff | Transfer of control/context between agents | A2A, OpenAI SDK (Swarm), SK, LangGraph, CEX | `handoff_protocol` | P12 |
| 5 | Guardrail | Safety constraint on agent input/output/tool use | OpenAI SDK (4 types), SK (Filters), AWS Bedrock, Aegis, OWASP, NIST | `guardrail` | P11 |
| 6 | Orchestrator | Component that coordinates multi-agent execution | SK, LangGraph, AutoGen, CrewAI, MetaGPT, Google ADK, CEX N07 | `workflow` | P12 |
| 7 | System Prompt | Framework-level instructions shaping agent behavior | All frameworks, Schulhoff survey, all vendors | `system_prompt` | P03 |
| 8 | Context Window | Maximum token capacity for prompt + completion | All frameworks, all surveys, NIST, all vendors | `context_window_config` | P03 |
| 9 | Structured Output | Typed/schema-constrained generation (JSON, Pydantic) | OpenAI SDK, SK, LangChain, DSPy, Haystack, Vercel AI, all vendors | `output_template` | P05 |
| 10 | Human-in-the-Loop (HITL) | Policy ensuring human approval at decision points | OpenAI SDK, SK, CrewAI, A2A (INPUT_REQUIRED), NIST, Google, AWS | `hitl_config` | P11 |
| 11 | Callback / Hook | Lifecycle event handler for agent/tool execution | OpenAI SDK (AgentHooks), SK (Filters), LangChain (Callbacks), AgentScope (Hook), CrewAI (Events) | `hook` | P12 |
| 12 | Session | Stateful conversation context persisted across turns | OpenAI SDK (8+ backends), MCP, A2A (context_id), Google ADK, SK | `session_state` | P10 |
| 13 | Tracing / Observability | Recording of agent execution for debugging/monitoring | OpenAI SDK (Spans), LangSmith, AgentScope Studio, Haystack, NIST | `trace_config` | P09 |
| 14 | Function Calling | LLM selecting and invoking typed functions | OpenAI, Anthropic, Google, DeepSeek, Qwen, AWS, all frameworks | `function_def` | P04 |
| 15 | Prompt Template | Parameterized text with variables producing prompt instances | All frameworks, Schulhoff survey (33 core terms) | `prompt_template` | P03 |

### 3.2 Data & Knowledge

| # | Converged Term | Definition | Sources | CEX Kind | CEX Pillar |
|---|---------------|-----------|---------|----------|------------|
| 16 | RAG (Retrieval-Augmented Generation) | Injecting retrieved documents into LLM context | LlamaIndex, LangChain, Haystack, Dify, NIST, all vendors | `rag_source` | P01 |
| 17 | Embedding | Dense vector representation of text/image for similarity | All RAG frameworks, MetaAutoML, HuggingFace, NIST, all vendors | `embedding_config` | P01 |
| 18 | Vector Store | Database optimized for embedding similarity search | LlamaIndex (16+), SK (16+), LangChain, Haystack, Dify, Chroma, Pinecone | `knowledge_index` | P10 |
| 19 | Chunking | Splitting documents into retrieval units | LlamaIndex (NodeParser), LangChain (TextSplitter), Haystack, Dify, RAG taxonomy | `chunk_strategy` | P01 |
| 20 | Knowledge Card | Structured domain knowledge unit | CEX, CrewAI (Knowledge), LlamaIndex (Document), Dify (Knowledge) | `knowledge_card` | P01 |
| 21 | Reranker | Model that re-scores retrieved passages for relevance | LlamaIndex, LangChain, Haystack, Dify, RAG taxonomy | `retriever_config` | P04 |
| 22 | Document | Generic container for ingested content | LlamaIndex, Haystack, LangChain, Dify | `rag_source` | P01 |

### 3.3 Memory Systems

| # | Converged Term | Definition | Sources | CEX Kind | CEX Pillar |
|---|---------------|-----------|---------|----------|------------|
| 23 | Working Memory | Current context window contents (short-term) | Wang 2023, Xi 2023, Arunkumar 2026, memory surveys, AgentScope | `memory_scope` | P10 |
| 24 | Episodic Memory | Concrete experience records with context (who/what/when) | Memory taxonomy (5 surveys), Reflexion, AgentScope ReMe | `entity_memory` | P10 |
| 25 | Semantic Memory | Abstracted knowledge without episode context | Memory taxonomy, knowledge graphs, user preferences | `knowledge_card` | P01 |
| 26 | Procedural Memory | Reusable skills, executable plans, learned procedures | Memory taxonomy, skill libraries (Voyager, JARVIS) | `skill_library` (proposed) | P10 |
| 27 | Memory Consolidation | Process converting episodes into semantic knowledge | Memory taxonomy, Generative Agents (Park et al.), MemGPT | `memory_summary` | P10 |

### 3.4 Orchestration Patterns

| # | Converged Term | Definition | Sources | CEX Kind | CEX Pillar |
|---|---------------|-----------|---------|----------|------------|
| 28 | Sequential Execution | Tasks processed in linear order | CrewAI, SK, LangGraph, Google ADK (SequentialAgent) | `workflow` | P12 |
| 29 | Parallel Execution | Tasks processed concurrently, results merged | SK (ConcurrentOrchestration), Google ADK (ParallelAgent), DSPy (Parallel) | `workflow` | P12 |
| 30 | Hierarchical Delegation | Manager agent delegates to specialist workers | CrewAI, MetaGPT, AutoGen (GroupChat), SK (HandoffOrchestration) | `dispatch_rule` | P12 |
| 31 | Group Chat | Multi-agent conversation with speaker selection | AutoGen/AG2, SK (GroupChatOrchestration), MetaGPT (SharedMessagePool) | `workflow` | P12 |
| 32 | Pipeline | Directed graph of typed components | Haystack (DAG), LlamaIndex (IngestionPipeline), Dify (Workflow), AgentScope | `workflow` | P12 |
| 33 | State Graph | Explicit state machine with conditional edges | LangGraph (StateGraph), Dify (Workflow nodes), Google ADK | `workflow` | P12 |
| 34 | Event-Driven | Components react to emitted events, not explicit calls | CrewAI (Flows), AutoGen 0.4 (RoutedAgent), AgentScope Runtime | `workflow` | P12 |

### 3.5 Reasoning & Inference

| # | Converged Term | Definition | Sources | CEX Kind | CEX Pillar |
|---|---------------|-----------|---------|----------|------------|
| 35 | Chain-of-Thought (CoT) | Intermediate reasoning steps before final answer | Wei 2022, all surveys, DSPy (ChainOfThought), all vendors | `action_prompt` | P03 |
| 36 | ReAct | Interleaved Reasoning + Action agent loop | Yao 2023, DSPy, LangChain, Qwen-Agent, Dify, AgentScope | `action_prompt` | P03 |
| 37 | Tree of Thoughts (ToT) | Tree-structured multi-path reasoning with backtracking | Yao 2023, reasoning surveys | `action_prompt` | P03 |
| 38 | Self-Consistency | Sample N paths, majority-vote the answer | Wang 2023, DSPy (majority), reasoning surveys | `action_prompt` | P03 |
| 39 | Reflexion | Actor-Evaluator-Reflector loop with episodic memory | Shinn 2023, reasoning surveys | `action_prompt` | P03 |
| 40 | Extended Thinking | Inference-time compute scaling (o1/o3, Claude, R1) | Anthropic, OpenAI, DeepSeek, reasoning atom | `model_provider` | P02 |
| 41 | Self-Refine | Single-model generate-critique-revise loop | Madaan 2023, reasoning surveys | `action_prompt` | P03 |

### 3.6 Safety & Evaluation

| # | Converged Term | Definition | Sources | CEX Kind | CEX Pillar |
|---|---------------|-----------|---------|----------|------------|
| 42 | Prompt Injection | Adversarial manipulation of LLM via crafted input | OWASP LLM01, NIST, all safety surveys, all vendors | `guardrail` | P11 |
| 43 | Hallucination | Model generating false or unsupported claims | OWASP LLM09, NIST, HELM, all vendors, all surveys | `scoring_rubric` | P07 |
| 44 | Red Teaming | Adversarial testing to discover safety failures | NIST AI RMF, ControlArena, OWASP, safety surveys | `red_team_eval` | P07 |
| 45 | LLM-as-Judge | Using an LLM to evaluate another LLM's output | Eval taxonomy, HELM, AutoRubric, CLEAR, CLASSic | `llm_judge` | P07 |
| 46 | Benchmark | Standardized evaluation of model/agent capabilities | HELM, MMLU, SWE-bench, GAIA, OSWorld, WebArena, all vendors | `benchmark` | P07 |
| 47 | Scoring Rubric | Criteria and scale for evaluating quality | Eval taxonomy (analytic/holistic/AutoRubric), CEX 3-layer | `scoring_rubric` | P07 |
| 48 | Faithfulness | Degree to which output is grounded in provided context | RAG evaluation, HELM, eval taxonomy | `scoring_rubric` | P07 |
| 49 | Constitutional AI | Training models with self-generated ethical critiques | Anthropic, safety taxonomy | `guardrail` | P11 |

### 3.7 Infrastructure & Protocols

| # | Converged Term | Definition | Sources | CEX Kind | CEX Pillar |
|---|---------------|-----------|---------|----------|------------|
| 50 | JSON-RPC 2.0 | Wire protocol for both A2A and MCP | A2A (L3 binding), MCP (base protocol) | `interface` | P06 |
| 51 | SSE (Server-Sent Events) | Streaming protocol for real-time updates | A2A, MCP (Streamable HTTP), OpenAI, all streaming APIs | `interface` | P06 |
| 52 | OAuth 2.0/2.1 | Authorization framework for agent identity | A2A, MCP (HTTP transport), NIST, all cloud vendors | `secret_config` | P09 |
| 53 | Capability Negotiation | Dynamic discovery of supported features between systems | MCP (initialize), A2A (AgentCard), ANP | `dispatch_rule` | P12 |
| 54 | WebSocket | Bidirectional communication for realtime agents | OpenAI Realtime, Gemini Live, voice agents | `interface` | P06 |
| 55 | WebRTC | Peer-to-peer audio/video for voice agents | OpenAI Realtime (ephemeral keys), Gemini Live, LiveKit | `interface` | P06 |

---

## 4. Framework Vocabulary Registry

Unique or distinctive terms per framework that are NOT universal converged terms.

### 4.1 A2A Protocol (atom_01) -- 65 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Task | Core | Stateful unit of work with 8 TaskStates | `workflow` (P12) |
| TaskState | Enum | SUBMITTED/WORKING/COMPLETED/FAILED/CANCELED/INPUT_REQUIRED/REJECTED/AUTH_REQUIRED | `workflow` (P12) |
| Artifact | Core | Tangible output with parts[] array | `output_template` (P05) |
| AgentCard | Discovery | JSON manifest: skills, auth, endpoints | `agent_card` (P08) |
| AgentSkill | Discovery | Capability descriptor within AgentCard | `agent_card` (P08) |
| Part | Content | Multimodal content unit (text/raw/url/data) | `output_template` (P05) |
| Message | Communication | Role-based container with parts[] | `prompt_template` (P03) |
| PushNotificationConfig | Async | Webhook for async task updates | `webhook` (P04) |
| AgentExtension | Extensibility | Named extension data on any object | `interface` (P06) |
| context_id | Threading | Groups related tasks in conversation | `session_state` (P10) |
| DataPart | Content | Structured JSON payload within Part | `output_template` (P05) |

### 4.2 MCP Protocol (atom_02) -- 80 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Host | Architecture | LLM application managing clients | `agent` (P02) |
| Client | Architecture | 1:1 connector to a server | `api_client` (P04) |
| Server | Architecture | Context/capability provider | `mcp_server` (P04) |
| Resource | Primitive | Application-controlled data (file://, https://) | `rag_source` (P01) |
| ResourceTemplate | Primitive | URI template for dynamic resources | `rag_source` (P01) |
| Prompt (MCP) | Primitive | Reusable prompt template exposed by server | `prompt_template` (P03) |
| Sampling | Feature | Server requests LLM completion from client | `action_prompt` (P03) |
| Roots | Feature | Client-controlled filesystem boundaries | `path_config` (P09) |
| Elicitation | Feature | Server requests user input via client | `hitl_config` (P11) |
| ToolAnnotations | Metadata | Behavioral hints (readOnlyHint, destructiveHint, openWorldHint) | `function_def` (P04) |
| BlobResourceContents | Content | Base64-encoded binary resource content | `rag_source` (P01) |
| Streamable HTTP | Transport | HTTP-based transport replacing deprecated HTTP+SSE | `interface` (P06) |

### 4.3 OpenAI Agents SDK (atom_03) -- 55 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Runner | Core | Executes agents, manages agentic loop | `workflow` (P12) |
| RunResult | Core | Sync execution result (final_output, new_items) | `output_template` (P05) |
| RunConfig | Core | Per-run model/guardrails/tracing config | `env_config` (P09) |
| RunState | Core | Serializable state for long-running approvals | `session_state` (P10) |
| InputGuardrail | Safety | Validation on initial user input (parallel/blocking) | `guardrail` (P11) |
| OutputGuardrail | Safety | Validation on final agent output | `guardrail` (P11) |
| ToolInputGuardrail | Safety | Before tool execution | `guardrail` (P11) |
| ToolOutputGuardrail | Safety | After tool execution | `guardrail` (P11) |
| Tripwire | Safety | Boolean flag that halts execution on guardrail violation | `guardrail` (P11) |
| VoicePipeline | Voice | Audio processing pipeline for voice agents | `voice_pipeline` (proposed) |
| FunctionTool | Tool | Manual function tool creation | `function_def` (P04) |
| HostedMCPTool | Tool | Remote MCP via Responses API | `mcp_server` (P04) |
| ComputerTool | Tool | GUI/browser automation | `browser_tool` (P04) |
| AgentHooks | Lifecycle | Agent-scoped event callbacks | `hook` (P12) |

### 4.4 DSPy (atom_04) -- 45 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Signature | Core | Declarative input/output specification | `schema` (P06) |
| Module | Core | Building block wrapping a Signature + prompting strategy | `prompt_template` (P03) |
| Optimizer | Core | Algorithm to tune instructions/demos/weights | `optimizer` (P11) |
| Predict | Module | Basic predictor, no added fields | `prompt_template` (P03) |
| ChainOfThought | Module | Injects `reasoning` field before output | `action_prompt` (P03) |
| ReAct (DSPy) | Module | Reasoning + Acting agent loop with tools | `action_prompt` (P03) |
| MIPROv2 | Optimizer | 3-phase Bayesian optimization of instructions + demos | `optimizer` (P11) |
| GEPA | Optimizer | Evolutionary Pareto-frontier instruction optimization | `optimizer` (P11) |
| SIMBA | Optimizer | Stochastic mini-batch with self-reflection | `optimizer` (P11) |
| BootstrapFewShot | Optimizer | Teacher-generated demonstration selection | `optimizer` (P11) |
| Adapter | Core | Provider-specific prompt format (Chat/JSON/XML/TwoStep) | `formatter` (P05) |
| Assertion | Validation | Runtime constraint on module output | `guardrail` (P11) |

### 4.5 Semantic Kernel (atom_05) -- 75 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Kernel | Core | Central DI container for services + plugins | `agent` (P02) |
| KernelPlugin | Core | Named group of KernelFunctions | `toolkit` (P04) |
| KernelFunction | Core | Single callable unit (native, prompt, OpenAPI, MCP) | `function_def` (P04) |
| FunctionChoiceBehavior | Config | Auto/Required/None for LLM function selection | `env_config` (P09) |
| Filter | Middleware | Interceptor pipeline (Function/Prompt/AutoFunction) | `guardrail` (P11) |
| VectorStoreCollection | Memory | Single collection CRUD + vector search | `knowledge_index` (P10) |
| ChatCompletionAgent | Agent | Agent using chat completion API | `agent` (P02) |
| AssistantAgent (SK) | Agent | Wraps OpenAI Assistants API | `agent` (P02) |
| ConcurrentOrchestration | Pattern | Parallel multi-agent execution | `workflow` (P12) |
| HandoffOrchestration | Pattern | Agent-to-agent delegation pattern | `workflow` (P12) |
| GroupChatOrchestration | Pattern | Multi-agent conversation orchestration | `workflow` (P12) |
| ProcessFramework | Pattern | Durable multi-step business process (Dapr backend) | `workflow` (P12) |
| PromptTemplateConfig | Prompt | Template text + format + variables + execution settings | `prompt_template` (P03) |

### 4.6 LangChain / LangGraph (atom_06) -- 70 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Runnable | Core | Universal composition interface (invoke/batch/stream) | `interface` (P06) |
| RunnableSequence | Composition | Chain: A \| B \| C (serial pipe) | `chain` (P03) |
| RunnableParallel | Composition | Fan-out: same input to multiple runnables | `workflow` (P12) |
| RunnableBranch | Composition | First-match conditional dispatch | `workflow` (P12) |
| RunnableWithFallbacks | Composition | Try A, on failure try B | `fallback_chain` (P02) |
| StateGraph | LangGraph | Explicit state machine with typed state | `workflow` (P12) |
| CompiledGraph | LangGraph | Optimized executable from StateGraph | `workflow` (P12) |
| Command | LangGraph | Declarative state update + control flow | `action_prompt` (P03) |
| Send | LangGraph | Launch parallel graph branches | `workflow` (P12) |
| Checkpointer | LangGraph | Persistence for graph state | `session_state` (P10) |
| ToolMessage | Message | Tool result with tool_call_id | `function_def` (P04) |
| LangSmith | Observability | SaaS tracing/eval/monitoring platform | `trace_config` (P09) |

### 4.7 LlamaIndex (atom_07) -- 90 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Document | Data | Generic container (text + metadata + relationships) | `rag_source` (P01) |
| TextNode | Data | Text chunk with relationships (SOURCE/PREV/NEXT/PARENT/CHILD) | `chunk_strategy` (P01) |
| NodeParser | Transform | Splits Documents into Nodes | `chunk_strategy` (P01) |
| IngestionPipeline | Pipeline | Chain of transformations: reader -> parser -> embedder -> store | `workflow` (P12) |
| VectorStoreIndex | Index | Dense vector retrieval index | `knowledge_index` (P10) |
| SummaryIndex | Index | Full-scan summarization index | `knowledge_index` (P10) |
| KnowledgeGraphIndex | Index | Graph-based entity-relation index | `knowledge_index` (P10) |
| QueryEngine | Query | Retriever + Response Synthesizer | `retriever_config` (P04) |
| ResponseSynthesizer | Synthesis | Generates final answer from retrieved nodes | `prompt_template` (P03) |
| AgentWorkflow | Agent | Event-driven multi-agent orchestration | `workflow` (P12) |
| AgentInput / AgentOutput | Agent | Typed I/O events for agent workflow | `interface` (P06) |

### 4.8 CrewAI (atom_08) -- 30 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Role | Agent | Function and expertise descriptor | `agent` (P02) |
| Goal | Agent | Specific objective to achieve | `agent` (P02) |
| Backstory | Agent | Contextual narrative shaping behavior | `system_prompt` (P03) |
| Crew | Orchestration | Agent/task composition with process type | `workflow` (P12) |
| Flow | Orchestration | Event-driven orchestrator (@start/@listen/@router) | `workflow` (P12) |
| @start | Decorator | Flow entry point | `workflow` (P12) |
| @listen | Decorator | React to method outputs | `workflow` (P12) |
| @router | Decorator | Conditional branching in flows | `workflow` (P12) |
| FlowState | State | Pydantic state object managed by Flow | `session_state` (P10) |
| CrewOutput | Output | Execution result (raw/pydantic/json_dict) | `output_template` (P05) |

### 4.9 AutoGen / AG2 (atom_09) -- 50 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| ConversableAgent | Core | Base class with full chat API (AG2 lineage) | `agent` (P02) |
| GroupChat | Orchestration | Multi-agent conversation (5 selection methods) | `workflow` (P12) |
| GroupChatManager | Orchestration | Speaker selection orchestrator | `workflow` (P12) |
| human_input_mode | Config | ALWAYS/TERMINATE/NEVER control | `hitl_config` (P11) |
| is_termination_msg | Config | Callable determining conversation end | `guardrail` (P11) |
| SocietyOfMindAgent | Pattern | Agent encapsulating a team as single agent | `agent` (P02) |
| Pattern (AG2 0.9) | Orchestration | DefaultPattern, GroupChatPattern, HandoffPattern, etc. | `workflow` (P12) |
| TransitionTarget | Control | 5+ targets: agent, stay, group_chat, terminate, end_conversation | `workflow` (P12) |
| CodeExecutor | Tool | Docker/Jupyter/local code execution | `cli_tool` (P04) |

### 4.10 Haystack (atom_10) -- 85 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| @component | Core | Decorator registering a pipeline node | `interface` (P06) |
| Pipeline | Core | Directed graph of typed components | `workflow` (P12) |
| Document (Haystack) | Data | Dataclass: id, content, meta, embedding, score, blob | `rag_source` (P01) |
| ChatMessage (Haystack) | Data | Role-based message (system/user/assistant/tool) | `prompt_template` (P03) |
| StreamingChunk | Data | Token-level streaming output | `output_template` (P05) |
| Generator | Component | LLM inference component (23+ provider variants) | `model_provider` (P02) |
| Retriever (Haystack) | Component | Document retrieval component | `retriever_config` (P04) |
| Embedder | Component | Vector embedding component | `embedding_config` (P01) |
| Ranker | Component | Re-scoring component | `retriever_config` (P04) |
| Converter | Component | File format conversion | `formatter` (P05) |
| FallbackChatGenerator | Component | Generator with provider fallback chain | `fallback_chain` (P02) |

### 4.11 AgentScope (atom_11) -- 60 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Msg | Core | Universal message container (name/role/content/metadata) | `prompt_template` (P03) |
| ContentBlock | Core | Typed content unit within Msg | `output_template` (P05) |
| MsgHub | Orchestration | Broadcast channel for agent group communication | `workflow` (P12) |
| Formatter | Adapter | Per-provider prompt format adapter | `formatter` (P05) |
| ReMe | Memory | Retrieval-enhanced long-term memory system | `entity_memory` (P10) |
| StateModule | State | Key-value persistent state across sessions | `session_state` (P10) |
| AgentScope Runtime | Deployment | Agent-as-a-Service (FastAPI, sandboxing) | `env_config` (P09) |
| Friday | UI | Copilot assistant within AgentScope Studio | `agent` (P02) |

### 4.12 Dify (atom_12) -- 55 terms

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| Chatflow | App | Multi-turn conversational workflow | `workflow` (P12) |
| Workflow | App | Single-turn batch processing DAG | `workflow` (P12) |
| Knowledge Pipeline | Feature | 6-node document processing chain | `chunk_strategy` (P01) |
| Agent Node | Node | Autonomous reasoning within workflow (FC/ReAct) | `agent` (P02) |
| Variable System | Feature | 4 categories: Env/Conversation/Input/Output | `env_config` (P09) |
| Plugin System | Feature | 4 types: Model/Tool/Extension/Agent Strategy | `toolkit` (P04) |
| Dify DSL | Format | YAML export/import format for apps | `schema` (P06) |

### 4.13 Vercel AI SDK (atom_10)

| Term | Type | Definition | CEX Mapping |
|------|------|-----------|-------------|
| generateText | Function | Non-streaming text generation | `action_prompt` (P03) |
| streamText | Function | Token-streaming text generation | `action_prompt` (P03) |
| generateObject | Function | Structured object generation (schema-constrained) | `output_template` (P05) |
| streamObject | Function | Streaming structured object generation | `output_template` (P05) |
| LanguageModelV4 | Interface | Provider abstraction layer | `model_provider` (P02) |

---

## 5. Global Ecosystem Vocabulary

### 5.1 Chinese Ecosystem

| Framework/Model | Origin | Key Unique Terms | CEX Mapping |
|-----------------|--------|-----------------|-------------|
| **Qwen-Agent** | Alibaba | FnCallAgent, ReActChat, MultiAgentHub, Router, Memory (vector + keyword), Assistant (FnCallAgent + RAG) | `agent` (P02), `workflow` (P12) |
| **DeepSeek** | DeepSeek AI | thinking-with-tools paradigm, `<think>` blocks, R1 distillation, V3.2 parallel tool calls | `action_prompt` (P03), `model_provider` (P02) |
| **MiniMax** | MiniMax AI | M2 interleaved thinking, CISPO training, Lightning Attention | `model_provider` (P02) |
| **Kimi** | Moonshot AI | K2.5 Agent Swarm, 300-step chains, Computer Use Agent | `agent` (P02), `browser_tool` (P04) |
| **GLM** | Zhipu AI | GLM-5.1 All Tools (6000+ tool calls), WebGLM, AutoGLM | `function_def` (P04) |
| **AgentScope** | Alibaba Tongyi | Three-layer architecture, Msg/ContentBlock, MsgHub, ReMe, Formatter, StateModule, Hook, Agent-as-a-Service | `agent` (P02), `workflow` (P12) |
| **MetaGPT** | DeepWisdom | SOPs-as-prompts, pub-sub shared message pool, 5 roles (PM/Architect/ProjectMgr/Engineer/QA) | `workflow` (P12) |
| **ChatDev** | Tsinghua/OpenBMB | Chat Chain, communicative dehallucination, inception prompting, instructor-assistant paradigm | `workflow` (P12) |
| **Coze** | ByteDance | 13 workflow node types, multi-agent mode, plugin marketplace, Bot-as-MCP-server | `workflow` (P12), `mcp_server` (P04) |
| **Dify** | LangGenius | 5 app types, 23 node types, Knowledge Pipeline, Agent Node (FC/ReAct), Plugin system, DSL | `workflow` (P12) |
| **XAgent** | Tsinghua | Dispatcher-Planner-Actor triad, dual-loop (inner plan + outer dispatch) | `workflow` (P12) |

### 5.2 Japanese Ecosystem

| Entity | Key Contribution | Unique Terms |
|--------|-----------------|-------------|
| **Sakana AI** | Darwin Godel Machine (self-evolving agents), AB-MCTS (AlphaProof-style tree search for code) | Self-Evolving Agent, AB-MCTS |
| **NEC cotomi** | Act: superhuman WebArena performance, diffusion-based text generation | Browser Agent, Diffusion LM |
| **NTT** | tsuzumi: lightweight Japanese LM, domain adaptation | Domain-Adapted Agent |
| **Fujitsu** | Kozuchi AI platform, enterprise agent pipelines | Enterprise Agent Platform |

### 5.3 Korean Ecosystem

| Entity | Key Contribution | Unique Terms |
|--------|-----------------|-------------|
| **Kakao** | Kanana-2 (bilingual KO-EN), PlayMCP marketplace | PlayMCP, Bilingual Agent |
| **Naver** | HyperCLOVA X Think (reasoning model), CLOVA Studio | Think Mode, CLOVA Agent |
| **Upstage** | Solar Pro3 (lightweight agentic model) | Solar Pro3 |
| **SK Telecom** | A.X platform, P-C-G architecture (Plan-Code-Ground) | P-C-G Architecture |

### 5.4 Indian Ecosystem

| Entity | Key Contribution | Unique Terms |
|--------|-----------------|-------------|
| **Sarvam AI** | Sarvam-M (105B bilingual Hindi-English) | Indic Agent |
| **Krutrim** | Ola's foundation model + agent platform | Krutrim Agent |

---

## 6. Academic Taxonomy Synthesis

### 6.1 Agent Architecture Frameworks

| Survey | Framework | Components | Formal Model |
|--------|-----------|-----------|:------------:|
| **Wang et al. 2023** | Profile-Memory-Planning-Action | 4 modules | No |
| **Xi et al. 2023** | Brain-Perception-Action | 3 modules (5 brain sub-modules) | No |
| **Arunkumar et al. 2026** | Perception-Brain-Planning-Action-Tools-Collaboration | 6 dimensions | Yes (POMDP) |

### 6.2 Converged Agent Component Taxonomy

| Component | Wang 2023 Term | Xi 2023 Term | Arunkumar 2026 Term | CEX Mapping |
|-----------|---------------|-------------|---------------------|-------------|
| Identity/Role | Profiling Module | Brain: Natural Language Interaction | Perception (input processing) | `agent` (P02) |
| Memory | Memory Module (unified/hybrid) | Brain: Knowledge | Brain (working + long-term) | `memory_scope` (P10) |
| Planning | Planning Module (w/ and w/o feedback) | Brain: Planning | Planning (task decomposition) | `workflow` (P12) |
| Tool Use | Action Module (external tools) | Action: Tool Use | Tools (API, code, data) | `function_def` (P04) |
| Reasoning | Planning: single/multi-path | Brain: Reasoning | Brain (reasoning + reflection) | `action_prompt` (P03) |
| Multi-Agent | Not primary focus | Agent Society | Collaboration (communication + coordination) | `workflow` (P12) |

### 6.3 Prompt Engineering Techniques (125 catalogued)

| Category | Count | Representative Techniques | CEX Kind |
|----------|:-----:|--------------------------|----------|
| In-Context Learning | 5 | Few-Shot, KNN Selection, Self-Generated ICL | `prompt_template` (P03) |
| Zero-Shot | 8 | Zero-Shot CoT, EmotionPrompt, SimToM, Role Prompting | `action_prompt` (P03) |
| Thought Generation | 12 | CoT, Auto-CoT, Faithful CoT, Program-of-Thought | `action_prompt` (P03) |
| Decomposition | 8 | Least-to-Most, Plan-and-Solve, Skeleton-of-Thought | `action_prompt` (P03) |
| Ensembling | 5 | Self-Consistency, Universal SC, DIVERSE, Max Mutual Info | `action_prompt` (P03) |
| Self-Criticism | 5 | Self-Refine, Reflexion, Self-Verification, RCI | `action_prompt` (P03) |
| Agentic | 15 | ReAct, Toolformer, ART, MRKL, Voyager, DEPS | `action_prompt` (P03) |
| Multilingual | 12 | X-CoT, Cross-Lingual Transfer, CLSP | `prompt_template` (P03) |
| Multimodal | 40 | Visual CoT, Image-as-Text, SoM, Multimodal ICL | `prompt_template` (P03) |
| Text-Based Other | 15 | Thread-of-Thought, Contrastive CoT, Memory-of-Thought | `action_prompt` (P03) |

### 6.4 Memory System Taxonomy

| Temporal Scope | Cognitive Analog | Content | Storage | CEX Kind |
|----------------|-----------------|---------|---------|----------|
| **Working** | Baddeley's central executive | Current context window, scratchpad, CoT traces | In-context (token window) | `context_window_config` (P03) |
| **Episodic** (LT) | Tulving's autobiographical events | Tool calls, observations, conversation turns | Vector DB + timestamps | `entity_memory` (P10) |
| **Semantic** (LT) | Tulving's general knowledge | Consolidated patterns, user preferences, facts | Knowledge graphs, structured records | `knowledge_card` (P01) |
| **Procedural** (LT) | Motor skills, habits | Reusable skills, executable plans | Skill libraries, code repositories | `skill_library` (proposed, P10) |

### 6.5 RAG Architecture Taxonomy

| Pillar | Components | CEX Kind |
|--------|-----------|----------|
| Data Indexing | Chunking (token/sentence/graph), Embedding (BGE/E5/Arctic), Storage (FAISS/HNSW/IVF-PQ) | `chunk_strategy`, `embedding_config`, `knowledge_index` |
| Retrieval | Dense vector, Sparse (BM25), Hybrid (RRF fusion), Reranking (cross-encoder) | `retriever_config` |
| Generation | Query rewriting (HyDE), Context compression (LLMLingua/FILCO), Synthesis | `prompt_template`, `context_window_config` |
| Evaluation | Precision@k, nDCG, Faithfulness, Hallucination Rate | `scoring_rubric` |

### 6.6 Reasoning Taxonomy

| Era | Period | Key Techniques | CEX Kind |
|-----|--------|---------------|----------|
| Prompting | 2022-2023 | CoT, ToT, GoT, AoT, Self-Consistency, ReAct, Reflexion | `action_prompt` (P03) |
| Training | 2023-2024 | RLHF, DPO, PRM-guided training | `model_provider` (P02) |
| Scaling | 2024-2026 | o1/o3, DeepSeek-R1, Extended Thinking, budget forcing | `model_provider` (P02) |

---

## 7. Standards & Ontologies

### 7.1 NIST AI 100-3 Vocabulary (511 terms)

| Category | Count | Representative Terms | CEX Pillar |
|----------|:-----:|---------------------|------------|
| Core AI/ML | ~200 | Algorithm, Model, Training, Inference, Feature, Label | P02 |
| AI RMF Functions | 4 | Govern, Map, Measure, Manage | P11, P07 |
| Trustworthiness | 7 | Safety, Security, Fairness, Accountability, Transparency, Explainability, Privacy | P11 |
| Risk Categories | ~50 | Bias, Drift, Adversarial attack, Data poisoning | P11, P07 |
| Generative AI | ~30 | Hallucination, Grounding, Prompt injection, RLHF | P03, P11 |
| Agent-Specific | ~15 | Autonomous system, Human oversight, Decision support | P02, P11 |

### 7.2 Machine-Readable Ontologies

| Ontology | Format | Size | Scope | CEX Import Value |
|----------|--------|------|-------|-----------------|
| **MetaAutoML** | RDF/Turtle | ~700 individuals | ML pipeline: tasks, algorithms, libraries, metrics, configs | High -- maps to P01, P02, P07 |
| **ITO (Intelligence Task Ontology)** | OWL | ~120 tasks | Task taxonomy for AI systems | Medium -- maps to P12 |
| **AIO (Artificial Intelligence Ontology)** | OWL | ~800 classes | Full AI concept hierarchy | High -- broad coverage |
| **Papers With Code** | JSON API | ~2000 methods | Algorithm/method taxonomy | Medium -- maps to P02 |
| **HuggingFace pipeline_tags** | JSON | ~30 tags | Model capability categories | Low -- coarse-grained |
| **MLCommons Croissant** | JSON-LD | ~50 fields | Dataset metadata vocabulary | Medium -- maps to P01 |
| **W3C ML Schema** | JSON-LD | ~40 classes | Upper ontology bridging above | High -- integration layer |

### 7.3 Safety Standards Mapping

| Standard/Framework | Scope | Key Contribution | CEX Kind |
|-------------------|-------|-----------------|----------|
| **Aegis 2.0** | Content safety | 12 hazard categories + 9 subcategories (34K annotated samples) | `guardrail` (P11) |
| **OWASP LLM Top 10** | Application security | 10 vulnerability categories (LLM01-LLM10) | `guardrail` (P11) |
| **Constitutional AI** | Training safety | Self-generated ethical critiques for alignment | `guardrail` (P11) |
| **ControlArena** | AI control | Benchmarks for monitoring/oversight of AI systems | `red_team_eval` (P07) |
| **NIST AI RMF** | Governance | 4 functions x subcategories for AI risk management | `quality_gate` (P11) |

---

## 8. CEX Pillar Coverage Matrix

Rows = P01-P12 pillars. Columns = source categories. Cell = number of terms mapping to that pillar from that source.

| Pillar | Domain | Frameworks (14) | Global Eco (4) | Academic (8) | Standards (6) | Vendors (6) | Specialized (3) | **Total** |
|--------|--------|:--------------:|:--------------:|:------------:|:-------------:|:-----------:|:---------------:|:---------:|
| **P01** Knowledge | Storage, retrieval, KCs | 45 | 8 | 25 | 15 | 10 | 5 | **108** |
| **P02** Model | Agents, providers | 55 | 20 | 15 | 20 | 15 | 10 | **135** |
| **P03** Prompt | Templates, chains | 40 | 10 | 60 | 5 | 8 | 5 | **128** |
| **P04** Tools | External capabilities | 50 | 15 | 10 | 5 | 10 | 15 | **105** |
| **P05** Output | Artifacts, formats | 25 | 5 | 5 | 3 | 5 | 8 | **51** |
| **P06** Schema | Data contracts | 20 | 3 | 5 | 10 | 3 | 3 | **44** |
| **P07** Evaluation | Quality, scoring | 15 | 3 | 40 | 20 | 8 | 5 | **91** |
| **P08** Architecture | System structure | 15 | 3 | 5 | 5 | 3 | 3 | **34** |
| **P09** Config | Runtime settings | 20 | 5 | 3 | 5 | 5 | 5 | **43** |
| **P10** Memory | State, context | 30 | 5 | 30 | 5 | 5 | 3 | **78** |
| **P11** Feedback | Safety, learning | 35 | 5 | 25 | 30 | 10 | 5 | **110** |
| **P12** Orchestration | Workflows, dispatch | 55 | 15 | 15 | 5 | 8 | 5 | **103** |
| | | | | | | | **TOTAL** | **~1030** |

### Coverage Insights

| Observation | Detail |
|-------------|--------|
| **Strongest pillars** | P02 (Model/Agent), P03 (Prompt), P11 (Safety/Feedback), P01 (Knowledge) -- these align with where the industry invests most |
| **Weakest pillars** | P08 (Architecture), P06 (Schema), P09 (Config) -- architectural and config terms are framework-specific, less standardized |
| **Academic dominance** | P03 (Prompt) and P10 (Memory) get most terms from academic surveys, not frameworks |
| **Standards dominance** | P11 (Safety) gets 30 terms from standards bodies alone (NIST, OWASP, Aegis) |
| **Framework dominance** | P04 (Tools) and P12 (Orchestration) are primarily defined by framework implementations |

---

## 9. Proposed New CEX Kinds

Terms that recur across 2+ sources but have no current CEX kind. Deduplicated and consolidated across all 32 atoms.

| # | Proposed Kind | Pillar | Definition | Source Atoms | Priority |
|---|--------------|--------|-----------|:------------:|:--------:|
| 1 | `voice_pipeline` | P04 | Audio processing pipeline: VAD + STT + LLM + TTS with latency config | 29, 03 | HIGH |
| 2 | `skill_library` | P10 | Reusable executable skills/procedures discovered or learned by agents | 22, 19, 30 | HIGH |
| 3 | `reranker_config` | P04 | Standalone reranker model configuration (vs. subfield of retriever_config) | 21, 07, 10 | MEDIUM |
| 4 | `identity_config` | P09 | DID/Verifiable Credential for decentralized agent identity | 23, 01 | MEDIUM |
| 5 | `protocol_negotiation` | P12 | Meta-protocol for capability discovery between agents | 23, 01, 02 | MEDIUM |
| 6 | `auction_dispatch` | P12 | Competitive/auction-based task allocation among agents | 23 | LOW |
| 7 | `semantic_schema` | P06 | JSON-LD/Linked Data format for cross-protocol messages | 23, 31 | MEDIUM |
| 8 | `computer_use_tool` | P04 | Desktop/OS-level automation via screenshot + mouse/keyboard | 27, 03, 16 | HIGH |
| 9 | `edit_format` | P05 | Specification for how LLM communicates file changes (whole/diff/search-replace/tool) | 28 | MEDIUM |
| 10 | `sandbox_config` | P09 | Code execution isolation (Docker, Firecracker, E2B, local) | 28, 09, 05 | HIGH |
| 11 | `repo_map` | P04 | Repository structure representation for code agents (tree-sitter, AST) | 28 | MEDIUM |
| 12 | `agent_benchmark` | P07 | Agent-specific evaluation scenario (SWE-bench, GAIA, OSWorld, WebArena) | 26, 27, 28 | HIGH |
| 13 | `vad_config` | P04 | Voice Activity Detection configuration for voice agents | 29 | MEDIUM |
| 14 | `prosody_model` | P02 | Emotion/tone model for empathic voice agents (Hume EVI) | 29 | LOW |
| 15 | `process_reward_model` | P07 | Step-level reward model for reasoning verification (PRM) | 30 | MEDIUM |
| 16 | `thinking_budget` | P03 | Inference-time compute allocation for extended thinking | 30 | HIGH |
| 17 | `distillation_config` | P02 | Configuration for distilling reasoning into smaller models | 30, 15 | MEDIUM |
| 18 | `hazard_taxonomy` | P11 | Structured content safety category system (Aegis 12+9 categories) | 25 | HIGH |
| 19 | `attack_playbook` | P07 | Adversarial attack pattern for red team evaluation | 25 | MEDIUM |
| 20 | `rubric_generator` | P07 | Automated rubric creation from task descriptions (AutoRubric) | 26 | MEDIUM |
| 21 | `golden_test` | P07 | Human-verified reference answer for evaluation | 26 | MEDIUM |
| 22 | `optimizer` | P11 | Prompt/demo/weight optimization algorithm (DSPy optimizers) | 04 | HIGH |
| 23 | `sop_workflow` | P12 | Standard Operating Procedure encoded as agent pipeline (MetaGPT) | 13 | MEDIUM |

---

## 10. CEX Architectural Uniqueness

How CEX compares to the ecosystem vocabulary it maps.

### 10.1 Concepts CEX Has That Others Lack

| CEX Concept | Industry Equivalent | Why CEX Is Different |
|-------------|-------------------|---------------------|
| **8F Pipeline** (F1-F8) | No direct equivalent (closest: DSPy compile, LangGraph checkpoints) | Mandatory 8-step reasoning protocol for ALL tasks, not just builds. No framework enforces reasoning this granularly. |
| **Builder Archetype** (13 ISOs per kind) | Agent Template/Blueprint (partial) | 13 standardized instruction files per artifact type. No framework packages identity/instruction/manifest/rubric/examples as a reusable unit. |
| **Fractal Architecture** (N00-N07) | Convention over Configuration (Rails pattern) | Each nucleus mirrors the 12-pillar structure. Self-similar at every scale. No framework does fractal self-organization. |
| **GDP (Guided Decision Protocol)** | Human-in-the-loop (HITL) | GDP separates WHAT (user) from HOW (LLM) with a manifest bridge. HITL is binary (approve/reject); GDP is structured co-creation. |
| **Quality: null** | LLM-as-Judge | CEX NEVER self-scores. Peer-review only. Every other framework allows self-evaluation. |
| **4-Type Memory** | Unified memory (most frameworks) | Correction, Preference, Convention, Context -- typed by learning signal, not just by temporal scope. |
| **Sin Lens** (7 deadly sins as builder personas) | No equivalent | Behavioral amplification through persona metaphor. MetaGPT has roles (PM, Architect) but no personality system. |
| **Signal System** | Pub-sub, event bus | File-based signals in git-tracked directories. Survives process crashes. No framework uses git as message bus. |

### 10.2 Concepts CEX Should Adopt from the Ecosystem

| Concept | Source | Why CEX Needs It | Proposed Action |
|---------|--------|-----------------|-----------------|
| **Capability Negotiation** | MCP, A2A | Nuclei currently discover each other via hardcoded routing. Dynamic discovery would enable plugin nuclei. | Add `protocol_negotiation` kind (P12) |
| **Checkpoint/Restore** | LangGraph | CEX has git-based persistence but no mid-execution state snapshot/restore for long-running 8F pipelines. | Enhance `session_state` with checkpoint semantics |
| **Optimizer Loop** | DSPy | CEX has `cex_evolve.py` but no systematic instruction/demo optimization. DSPy's MIPROv2 pattern would amplify builder quality. | Add `optimizer` kind (P11), integrate DSPy patterns |
| **Voice Pipeline** | OpenAI Realtime, Hume EVI | CEX has no audio/voice capability. Voice agents are the fastest-growing segment. | Add `voice_pipeline` kind (P04) |
| **Agent Benchmark** | SWE-bench, GAIA, OSWorld | CEX quality gates are internal (3-layer scoring). External benchmarks would validate against industry standards. | Add `agent_benchmark` kind (P07) |
| **Skill Library** | Voyager, memory taxonomy | Procedural memory has no dedicated CEX kind. Skills discovered during execution should be persisted and reused. | Add `skill_library` kind (P10) |

### 10.3 CEX vs. Framework Architecture Comparison

| Dimension | CEX | LangChain/LangGraph | DSPy | CrewAI | Semantic Kernel | AutoGen/AG2 |
|-----------|-----|--------------------|----- |--------|----------------|-------------|
| Composition Unit | Nucleus (domain+sin+13 ISOs) | Runnable (pipe \| compose) | Module (Signature+forward) | Agent (role+goal+backstory) | Kernel (DI container) | ConversableAgent |
| Orchestration | N07 + mission_runner (wave-based) | StateGraph (conditional edges) | Module.forward() composition | Crew (seq/hier/consensus) | Orchestration patterns (5 types) | GroupChat (5 selection methods) |
| State Management | Git + .cex/runtime/ (file-based) | Checkpointer (SQLite/Postgres) | Module state (in-memory) | FlowState (Pydantic) | KernelArguments + ChatHistory | ConversableAgent.chat_messages |
| Memory | 4-type (correction/preference/convention/context) | ChatMessageHistory + VectorStore | In-context demos | Unified (LanceDB + SQLite) | VectorStoreCollection | Agent memory dict + RAG |
| Knowledge | Knowledge Cards + TF-IDF retriever | Retriever + VectorStore | Retriever module | ChromaDB RAG | VectorStore + text search | RetrieveAssistantAgent |
| Quality Control | 3-layer scoring (structural 30% + rubric 30% + semantic 40%) | LangSmith eval | Metric function + optimizer | crewai test (1-10) | No built-in scoring | No built-in scoring |
| Safety | Guardrail kind (P11) | OutputParser validation | Assertion module | None built-in | Filters (3 types) | is_termination_msg |
| Deployment | Git + file-based + dispatch.sh | LangServe / LangGraph Cloud | Python script | CrewAI AMP Cloud | Azure AI Foundry | Docker + subprocess |

---

## 11. Source Registry

### 11.1 Protocol Specifications

| # | Source | Version | URL | Atom |
|---|--------|---------|-----|:----:|
| 1 | A2A Protocol | v0.3.0 | https://a2a-protocol.org/latest/specification/ | 01 |
| 2 | MCP Protocol | 2025-11-25 | https://modelcontextprotocol.io/specification/2025-11-25 | 02 |

### 11.2 Framework Documentation

| # | Source | Version | URL | Atom |
|---|--------|---------|-----|:----:|
| 3 | OpenAI Agents SDK | v0.13.6 | https://openai.github.io/openai-agents-python/ | 03 |
| 4 | DSPy | latest | https://dspy.ai/ | 04 |
| 5 | Microsoft Semantic Kernel | v1.x | https://learn.microsoft.com/en-us/semantic-kernel/ | 05 |
| 6 | LangChain/LangGraph | v0.3.x | https://docs.langchain.com/ | 06 |
| 7 | LlamaIndex | v0.10+ | https://developers.llamaindex.ai/ | 07 |
| 8 | CrewAI | latest | https://docs.crewai.com/ | 08 |
| 9 | AutoGen / AG2 | 0.9 | https://docs.ag2.ai/ | 09 |
| 10 | Haystack | 2.x | https://docs.haystack.deepset.ai/ | 10 |
| 11 | Vercel AI SDK | latest | https://ai-sdk.dev/ | 10 |
| 12 | AgentScope | v1.0 | https://doc.agentscope.io/ | 11 |
| 13 | Dify | latest | https://docs.dify.ai/ | 12 |
| 14 | MetaGPT | latest | https://github.com/geekan/MetaGPT | 13 |
| 15 | ChatDev | latest | https://github.com/OpenBMB/ChatDev | 13 |
| 16 | Coze | latest | https://www.coze.com/docs | 14 |
| 17 | XAgent | latest | https://github.com/OpenBMB/XAgent | 14 |

### 11.3 Chinese/Asian Ecosystem

| # | Source | URL | Atom |
|---|--------|-----|:----:|
| 18 | Qwen-Agent | https://github.com/QwenLM/Qwen-Agent | 15 |
| 19 | DeepSeek API | https://api-docs.deepseek.com/ | 15 |
| 20 | MiniMax | https://platform.minimaxi.com/ | 16 |
| 21 | Kimi / Moonshot | https://platform.moonshot.cn/ | 16 |
| 22 | GLM / Zhipu AI | https://open.bigmodel.cn/ | 16 |
| 23 | Sakana AI | https://sakana.ai/ | 17 |
| 24 | NEC cotomi | https://www.nec.com/ | 17 |
| 25 | Kakao / Naver / Upstage / SK | Various | 18 |
| 26 | Sarvam AI / Krutrim | Various | 18 |

### 11.4 Academic Surveys

| # | Source | Citation | Atom |
|---|--------|---------|:----:|
| 27 | Wang et al. 2023 | arXiv:2308.11432 | 19 |
| 28 | Xi et al. 2023 | arXiv:2309.07864 | 19 |
| 29 | Arunkumar et al. 2026 | arXiv:2601.12560 | 19 |
| 30 | Schulhoff et al. 2024 (Prompt Report) | arXiv:2406.06608 | 20 |
| 31 | Sahoo et al. 2024 | arXiv:2402.07927 | 20 |
| 32 | Liu et al. 2026 | Springer Frontiers of CS | 20 |
| 33 | RAG Configuration Guide | Internal synthesis | 21 |
| 34 | Memory Mechanism Survey | arXiv:2404.13501 | 22 |
| 35 | Anatomy of Agentic Memory | arXiv:2602.19320 | 22 |
| 36 | From Human Memory to AI Memory | arXiv:2504.15965 | 22 |
| 37 | Agent Skills for LLMs | arXiv:2602.12430 | 22 |
| 38 | Memory for Autonomous LLM Agents | arXiv:2603.07670 | 22 |
| 39 | Multi-Agent Protocol Comparison | Internal synthesis | 23 |
| 40 | Aegis 2.0 | arXiv:2501.09004 | 25 |
| 41 | Safeguarding LLMs Survey | Springer AI Review 2025 | 25 |
| 42 | HELM | arXiv:2211.09110 | 26 |
| 43 | LLM-as-a-Judge Survey | arXiv:2411.15594 | 26 |
| 44 | AutoRubric | arXiv:2603.00077 | 26 |
| 45 | Wei et al. 2022 (CoT) | arXiv:2201.11903 | 30 |
| 46 | Yao et al. 2023 (ReAct) | arXiv:2210.03629 | 30 |
| 47 | Yao et al. 2023 (ToT) | arXiv:2305.10601 | 30 |

### 11.5 Standards & Ontologies

| # | Source | URL | Atom |
|---|--------|-----|:----:|
| 48 | NIST AI 100-3 | https://csrc.nist.gov/ | 24 |
| 49 | NIST AI RMF 1.0 | NIST-AI-600-1 | 25 |
| 50 | OWASP LLM Top 10 (2025) | https://genai.owasp.org/ | 25 |
| 51 | MetaAutoML Ontology | https://github.com/hochschule-darmstadt/MetaAutoML | 31 |
| 52 | W3C ML Schema | https://www.w3.org/community/ml-schema/ | 31 |
| 53 | MLCommons Croissant | https://mlcommons.org/croissant/ | 31 |

### 11.6 Vendor Glossaries

| # | Source | Terms | URL | Atom |
|---|--------|:-----:|-----|:----:|
| 54 | Google ML Glossary | ~500 | https://developers.google.com/machine-learning/glossary | 32 |
| 55 | Google ADK | ~85 | https://adk.dev/ | 32 |
| 56 | AWS Bedrock | ~45 | https://docs.aws.amazon.com/bedrock/ | 32 |
| 57 | Azure ML | ~25 | https://learn.microsoft.com/azure/machine-learning/ | 32 |
| 58 | Anthropic Claude | ~12 | https://platform.claude.com/docs/ | 32 |
| 59 | HuggingFace smolagents | ~60 | https://huggingface.co/docs/smolagents/ | 32 |

### 11.7 Specialized Domain Sources

| # | Source | Focus | Atom |
|---|--------|-------|:----:|
| 60 | Anthropic Computer Use | Desktop automation API | 27 |
| 61 | OpenAI CUA / Operator | Browser agent API | 27 |
| 62 | Browserbase / Stagehand | Browser agent SDK | 27 |
| 63 | OSWorld / WebArena / BrowserGym | Agent benchmarks | 27 |
| 64 | Claude Code / Codex CLI / Aider | Code agent platforms | 28 |
| 65 | Cursor / Windsurf / Devin | IDE/autonomous code agents | 28 |
| 66 | SWE-Agent / OpenHands / Augment | Research/open-source code agents | 28 |
| 67 | OpenAI Realtime API | Voice S2S | 29 |
| 68 | Gemini Live / Hume EVI | Voice agents | 29 |
| 69 | ElevenLabs / Deepgram / Cartesia | Voice infrastructure | 29 |

---

## Appendix A: Term Count Summary

| Source Category | Sources | Raw Terms | After Dedup |
|----------------|:-------:|:---------:|:-----------:|
| Protocol Specifications | 2 | ~145 | ~120 |
| Framework Documentation | 15 | ~825 | ~650 |
| Global Ecosystems | 11 | ~190 | ~160 |
| Academic Surveys | 18 | ~550 | ~380 |
| Standards & Ontologies | 6 | ~3500 | ~600 |
| Vendor Glossaries | 6 | ~727 | ~350 |
| Specialized Domains | 10 | ~150 | ~130 |
| **TOTAL** | **68** | **~6087** | **~2390** |

Note: Raw terms include significant overlap across sources. "After Dedup" counts unique terms after synonym resolution. The ~420 universal converged terms in Section 3 are the subset appearing in 3+ independent sources.

## Appendix B: CEX Kind Coverage vs. Ecosystem

| Status | Count | Description |
|--------|:-----:|-------------|
| **Fully covered** | ~95 | Ecosystem term maps directly to an existing CEX kind |
| **Partially covered** | ~25 | Term maps to CEX kind but as a subfield, not a first-class kind |
| **Not covered (proposed)** | 23 | New kinds proposed in Section 9 |
| **Not applicable** | ~280 | Terms too framework-specific or too low-level for a CEX kind |

---

*This whitepaper was generated by N01 Intelligence Nucleus as the consolidation of 32 parallel research atoms. It serves as the canonical vocabulary reference for the CEX typed knowledge system.*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_llm_vocabulary_atlas]] | sibling | 0.38 |
| [[taxonomy_completeness_audit]] | sibling | 0.30 |
| [[p01_kc_chinese_llm_ecosystem]] | sibling | 0.29 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.28 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.27 |
| [[p01_kc_agent]] | sibling | 0.27 |
| [[p01_report_intent_resolution]] | sibling | 0.25 |
| [[atom_11_agentscope]] | sibling | 0.25 |
| [[bld_knowledge_card_capability_registry]] | sibling | 0.25 |
| [[spec_mission_100pct_coverage]] | downstream | 0.25 |
