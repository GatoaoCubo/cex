---
id: atom_11_agentscope
kind: knowledge_card
8f: F3_inject
title: "Atomic Research: AgentScope (Alibaba Tongyi Lab)"
version: "1.0.0"
quality: 8.9
tags: [agentscope, alibaba, tongyi, multi-agent, framework, atlas, vocabulary, chinese-ai]
pillar: P01
domain: llm-agent-frameworks
density_score: 0.95
sources:
  - "https://github.com/agentscope-ai/agentscope"
  - "https://arxiv.org/abs/2402.14034"
  - "https://arxiv.org/html/2508.16279v1"
  - "https://arxiv.org/abs/2501.12851"
  - "https://doc.agentscope.io/"
  - "https://docs.agentscope.io/"
  - "https://github.com/agentscope-ai/agentscope-runtime"
  - "https://runtime.agentscope.io/"
  - "https://github.com/agentscope-ai/ReMe"
  - "https://deepwiki.com/agentscope-ai/agentscope"
related:
  - atom_03_openai_agents_sdk
  - cex_llm_vocabulary_whitepaper
  - atom_07_llamaindex
  - p01_kc_agent
  - p01_kc_chinese_llm_ecosystem
  - atom_05_semantic_kernel
  - bld_collaboration_agent
  - atom_09_autogen_ag2
  - p03_ch_kc_to_notebooklm
  - p01_kc_terminology_anthropic_canonical
---

# Atomic Research: AgentScope (Alibaba Tongyi Lab)

Deep-dive extraction of AgentScope's complete vocabulary, type system, architecture,
and unique concepts. Covers AgentScope Core (v1.0, Sep 2025), AgentScope Runtime (v1.1,
Feb 2026), and ReMe memory system. Origin: Alibaba Tongyi Lab (Dawei Gao et al.).

Papers: arXiv:2402.14034 (original, Feb 2024), arXiv:2508.16279 (v1.0, Aug 2025).

---

## 1. Architecture Overview

AgentScope uses a **three-layer architecture** with three independent modules:

| Layer | Module | Purpose |
|-------|--------|---------|
| Core Framework | `agentscope` | Agent development "language": agents, messages, pipelines, tools, memory |
| Runtime | `agentscope-runtime` | Production deployment: Agent-as-a-Service, sandboxing, state persistence |
| Studio | AgentScope Studio | Observability UI: tracing, evaluation, chat interface, Friday copilot |

Design philosophy: **developer-centric**, procedure-oriented message exchange,
async-first (Python 3.10+ asyncio), convention-over-configuration.

Original (v0.x) used an **Actor-based distributed model** with RPC and placeholder
mechanism for automatic parallelism. v1.0 shifted to FastAPI-based Agent-as-a-Service.

---

## 2. Full Type Registry

### 2.1 Message Types

| Type | Class | Fields | Purpose |
|------|-------|--------|---------|
| **Msg** | `Msg` | `name`, `role`, `content`, `metadata`, `id`, `timestamp`, `invocation_id` | Universal data container for all agent communication |
| **ChatResponse** | `ChatResponse` | `content` (ContentBlock seq), `id`, `created_at`, `type` ("chat"), `usage`, `metadata` | Unified LLM response wrapper across providers |
| **ServiceResponse** | `ServiceResponse` | (status, content) | Return type from service functions (tools) |
| **ChatUsage** | `ChatUsage` | `prompt_tokens`, `completion_tokens`, `total_tokens` | Token accounting per LLM call |

**Msg.role** values: `"user"`, `"assistant"`, `"system"`

**Msg.content**: Either a plain string OR a list of `ContentBlock` objects (multimodal).

### 2.2 ContentBlock Types (TypedDicts)

| Block Type | Fields | Purpose |
|------------|--------|---------|
| **TextBlock** | `{"type": "text", "text": str}` | Plain text content |
| **ThinkingBlock** | `{"type": "thinking", "thinking": str}` | Chain-of-thought / reasoning trace |
| **ToolUseBlock** | `{"type": "tool_use", "id": str, "name": str, "input": dict}` | Tool invocation request |
| **ToolResultBlock** | `{"type": "tool_result", "id": str, "name": str, "output": str\|list}` | Tool execution result |
| **ImageBlock** | `{"type": "image", "source": URLSource\|Base64Source}` | Image content |
| **AudioBlock** | `{"type": "audio", "source": URLSource\|Base64Source}` | Audio content |
| **VideoBlock** | `{"type": "video", "source": URLSource\|Base64Source}` | Video content |

Media source types: **URLSource** (URL reference), **Base64Source** (inline encoded).

### 2.3 Agent Classes

| Class | Parent | Purpose | Key Methods |
|-------|--------|---------|-------------|
| **AgentBase** | `StateModule` | Abstract root of all agents | `reply()`, `observe()`, `print()`, `handle_interrupt()` |
| **ReActAgentBase** | `AgentBase` | Adds reasoning/acting separation | `_reasoning()`, `_acting()` |
| **ReActAgent** | `ReActAgentBase` | Production ReAct implementation with 5 components | Model + Formatter + Memory + Toolkit + optional LTM |
| **UserAgent** | `AgentBase` | Human-in-the-loop proxy | Collects human input in pipelines |
| **A2AAgent** | `AgentBase` | Remote agent proxy via A2A protocol | Card resolvers, protocol adaptation |
| **DialogAgent** | `AgentBase` | Role-customizable via system prompt | Simple conversational agent |
| **DictDialogAgent** | `AgentBase` | Dictionary-format structured responses | JSON output agent |
| **VoiceAgent** | `AgentBase` | Voice I/O agent | TTS + realtime audio |
| **RealtimeVoiceAgent** | `AgentBase` | Streaming voice conversations | WebRTC/event-based |
| **DeepResearchAgent** | `ReActAgentBase` | Multi-step research with reflection | Query expansion, tree-structured ReAct |
| **BrowserAgent** | `ReActAgentBase` | Web automation via Playwright MCP | Subtask decomposition, multi-tab, long-page chunking |
| **MetaPlannerAgent** | `ReActAgentBase` | Dual-mode: lightweight ReAct or planning-execution | `RoadmapManager`, `WorkerManager`, dynamic worker instantiation |
| **ProgrammerAgent** | `AgentBase` | Code generation + execution | (v0.x, may be deprecated in v1.0) |
| **TextToImageAgent** | `AgentBase` | Image generation | (v0.x, may be deprecated in v1.0) |

**Agent lifecycle**: `observe()` -> `reply()` -> optional `handle_interrupt()` (async cancellation).

### 2.4 Pipeline / Orchestration Classes

| Class/Function | Type | Purpose |
|----------------|------|---------|
| **SequentialPipeline** | Class | Chain agents in order; output of N becomes input of N+1 |
| **sequential_pipeline()** | Function | Functional equivalent of SequentialPipeline |
| **FanoutPipeline** | Class | Distribute same input to multiple agents concurrently |
| **fanout_pipeline()** | Function | Functional equivalent; `enable_gather=True` for concurrent, `False` for sequential |
| **MsgHub** | Async context manager | Broadcast messages among participant group |
| **ChatRoom** | Class | Realtime voice agent orchestration with event forwarding |
| **stream_printing_messages()** | Async generator | Yields `(Msg, bool)` tuples for UI streaming; `bool` = is_last_chunk |

**MsgHub methods**: `add(agent)`, `delete(agent)`, `broadcast(msg)`, `set_auto_broadcast(bool)`

**MsgHub behavior**: On context entry, each participant subscribes to all others' outputs
via `observe()`. When any participant calls `reply()`, the result auto-broadcasts to
all other participants. Dynamic add/delete mid-session is supported.

**Conditional/Iterative patterns** (v0.x, documented but not explicitly classed in v1.0):
- if-else pipelines
- switch-case pipelines
- while-loop pipelines
- for-loop pipelines

**Routing mechanisms** (v1.0):
- Structured output routing (Pydantic `Literal` types)
- Tool-based routing (agents wrapped as tool functions)
- Agent-as-tool pattern (factory function registered as tool)

### 2.5 Model Classes

| Class | Purpose |
|-------|---------|
| **ChatModelBase** | Abstract interface for all chat LLMs |
| **DashScopeChatModel** | Alibaba DashScope / Qwen models |
| **OpenAIChatModel** | OpenAI GPT models |
| **GeminiChatModel** | Google Gemini models |
| **AnthropicChatModel** | Anthropic Claude models |
| **OllamaChatModel** | Local Ollama models |
| **TTSModelBase** | Text-to-speech synthesis |
| **EmbeddingModelBase** | Semantic embedding models |
| **RealtimeModelBase** | Streaming/realtime model interface |

Supported providers (v1.0): OpenAI, DeepSeek, vLLM, DashScope, Anthropic, Gemini, Ollama.

### 2.6 Formatter Classes

Formatters convert `Msg` history to provider-specific API formats.

| Chat Formatter | MultiAgent Formatter | Provider |
|----------------|---------------------|----------|
| **DashScopeChatFormatter** | **DashScopeMultiAgentFormatter** | Alibaba DashScope |
| **OpenAIChatFormatter** | **OpenAIMultiAgentFormatter** | OpenAI |
| **AnthropicChatFormatter** | **AnthropicMultiAgentFormatter** | Anthropic |
| **GeminiChatFormatter** | **GeminiMultiAgentFormatter** | Google Gemini |
| **OllamaChatFormatter** | **OllamaMultiAgentFormatter** | Ollama |
| **DeepSeekChatFormatter** | **DeepSeekMultiAgentFormatter** | DeepSeek |
| **A2AChatFormatter** | -- | Agent-to-Agent protocol |

**Rule**: Use `ChatFormatter` for 2-party conversations. Use `MultiAgentFormatter`
for 3+ participants (adds name prefixes + history wrapping for speaker identification).

### 2.7 Memory Classes

| Class | Layer | Backend | Purpose |
|-------|-------|---------|---------|
| **MemoryBase** | Abstract | -- | Base interface for all memory |
| **InMemoryMemory** | Short-term | In-process | Default buffer for dialogue history |
| **AsyncSQLAlchemyMemory** | Short-term | SQLite/PostgreSQL/MySQL | Async DB-backed storage |
| **RedisMemory** | Short-term | Redis | Distributed session state |
| **LongTermMemoryBase** | Long-term | Abstract | Cross-session persistence base |
| **Mem0LongTermMemory** | Long-term | Mem0 | Semantic indexing via mem0 library |
| **ReMePersonalLongTermMemory** | Long-term | ReMe | Personal memory with profile management |

**Short-term memory methods**: `add()`, `delete()`, `delete_by_mark()`, `size()`, `clear()`,
`get_memory()`, `update_messages_mark()`, `update_compressed_summary()`, `state_dict()`, `load_state_dict()`

**Long-term memory methods (dual-mode)**:
- Developer-controlled: `record()`, `retrieve()`
- Agent-controlled: `record_to_memory()`, `retrieve_from_memory()`

**LTM control modes** on ReActAgent: `agent_control`, `static_control`, `both`

**Mark system**: String labels on messages for categorization/filtering (unique to AgentScope).

### 2.8 Memory Compression

| Component | Purpose |
|-----------|---------|
| **CompressionConfig** | Triggers auto-compression when token count exceeds threshold |
| **SummarySchema** | Pydantic BaseModel structuring compressed memory |
| **keep_recent** | Parameter preserving N most recent messages uncompressed |

**SummarySchema fields**: `task_overview`, `current_state`, `important_discoveries`,
`next_steps`, `context_to_preserve`

Compression types (from paper): "dynamic compression" (real-time semantic extraction),
"hybrid compression" (combining summarization + selective retention).

### 2.9 Tool System

| Class/Function | Purpose |
|----------------|---------|
| **Toolkit** | Central tool manager: registration, schema generation, execution |
| **ToolFunction** | Wrapper around callable with metadata |
| **register_tool_function()** | Register a Python function as agent tool |
| **execute_tool_function()** | Unified async generator for heterogeneous tool outputs |
| **register_mcp_client()** | Register an MCP protocol client |
| **create_tool_group()** | Group-wise tool management (mitigates paradox-of-choice) |
| **update_tool_groups()** | Update active tool groups |
| **reset_equipped_tools()** | Dynamic tool provisioning at runtime |
| **execute_python_code** | Built-in: sandboxed Python execution |
| **execute_shell_command** | Built-in: shell command execution |
| **HttpStatelessClient** | MCP stateless client for transactional services |
| **StatefulClientBase** | MCP stateful client for persistent connections |
| **get_callable_function()** | Extract MCP tools as local callable functions |

**Tool vs Service Function**: Service functions return `ServiceResponse`. Tools are
"processed service functions" with JSON schema descriptions for LLM understanding.
The **ServiceFactory** auto-converts services to OpenAI-compatible JSON schema format.

**parallel_tool_calls**: Parameter enabling parallel tool execution via `asyncio.gather()`.

### 2.10 State Management

| Class/Method | Purpose |
|--------------|---------|
| **StateModule** | Base class for all stateful components (agents, memory, toolkit) |
| **register_state(attr_name, custom_to_json, custom_from_json)** | Mark attribute for serialization |
| **state_dict()** | Export state as dictionary |
| **load_state_dict(state_dict, strict)** | Restore from saved state |
| **SessionBase** | Abstract session persistence |
| **JSONSession** | JSON file-based session storage |
| **RedisSession** | Redis-backed session for distributed deployments |

**Automatic nesting**: StateModule children are auto-included in parent's `state_dict()`.
All of `AgentBase`, `MemoryBase`, `LongTermMemoryBase`, `Toolkit` inherit StateModule.

### 2.11 Hook System

**10 hooks across 5 core functions** (5 pre/post pairs):

| # | Hook Name | Available On | What It Intercepts |
|---|-----------|-------------|-------------------|
| 1 | **pre_reply** | AgentBase+ | Before agent generates response |
| 2 | **post_reply** | AgentBase+ | After agent response is generated |
| 3 | **pre_observe** | AgentBase+ | Before agent receives broadcast message |
| 4 | **post_observe** | AgentBase+ | After message stored in agent memory |
| 5 | **pre_print** | AgentBase+ | Before console/queue output |
| 6 | **post_print** | AgentBase+ | After output delivery |
| 7 | **pre_reasoning** | ReActAgentBase+ | Before `_reasoning()` (thinking + tool selection) |
| 8 | **post_reasoning** | ReActAgentBase+ | After reasoning step completes |
| 9 | **pre_acting** | ReActAgentBase+ | Before `_acting()` (tool execution) |
| 10 | **post_acting** | ReActAgentBase+ | After tool calls return results |

**Canonical type signatures**:
```python
# Pre-hook (hooks 1, 3, 5, 7, 9)
def pre_hook(self: AgentBase, kwargs: dict[str, Any]) -> dict[str, Any] | None:
    ...  # return modified kwargs to replace, or None for pass-through

# Post-hook (hooks 2, 4, 6, 8, 10)
def post_hook(self: AgentBase, kwargs: dict[str, Any], output: Any) -> Any:
    ...  # return replacement output, or None for pass-through
```

**Registration levels**:
- Class-level (all instances): `AgentBase.register_class_hook(hook_type, hook_name, hook)`
- Instance-level (single agent): `agent.register_instance_hook(hook_type, hook_name, hook)`
- Removal: `remove_class_hook()`, `remove_instance_hook()`, `clear_class_hooks()`, `clear_instance_hooks()`

**Execution order**: Class hooks (insertion order) -> Instance hooks (insertion order) -> Core method -> Class post-hooks -> Instance post-hooks.

**Chaining behavior**: Non-`None` return propagates to next hook; all-`None` chain passes original args unchanged.

**Storage implementation**: Six `OrderedDict` class attributes + six `OrderedDict` instance attributes per agent. Deterministic ordering for predictable distributed behavior.

**Critical constraint**: Never call the wrapped method inside its own hook (infinite loop).

**ReMe integration (5-step pre_reasoning sequence)**:
`ReMeLight.pre_reasoning_hook()` is registered as a `pre_reasoning` hook on ReActAgent.
Full execution order before each reasoning step:
1. `compact_tool_result()` -- truncate long tool outputs, cache to `tool_result/<uuid>.txt`
2. `check_context()` -- token-count current context via ContextChecker
3. `compact_memory()` -- if threshold exceeded, generate structured summary (Goal/Progress/Decisions/NextSteps)
4. `summary_memory()` (async) -- persist summary to `memory/YYYY-MM-DD.md`
5. `mark_messages_compressed()` -- save raw dialog to `dialog/YYYY-MM-DD.jsonl`; mark with `_MemoryMark.COMPRESSED`

**Registration code pattern**:
```python
# Class-level -- applies to ALL instances of this class
def audit_hook(agent, kwargs):
    return kwargs  # or None for pass-through

AgentBase.register_class_hook(
    hook_type="pre_reply",
    hook_name="audit",
    hook=audit_hook,
)

# Instance-level -- applies to ONE specific agent
agent.register_instance_hook(
    hook_type="post_reply",
    hook_name="log_msg",
    hook=lambda agent, kwargs, msg: msg,
)
```

### 2.12 Planning System

| Class | Purpose |
|-------|---------|
| **PlanNotebook** | Structured task planning integration with ReActAgent |
| **Plan** | Hierarchical task plan |
| **SubTask** | Individual task unit within a plan |
| **RoadmapManager** | Hierarchical decomposition in MetaPlannerAgent |
| **WorkerManager** | Dynamic worker instantiation in MetaPlannerAgent |

Hints are injected as system messages per reasoning step.

### 2.13 Evaluation Framework

| Class | Purpose |
|-------|---------|
| **Task** | Evaluation unit: unique ID, input, ground truth, metrics, metadata |
| **SolutionOutput** | Agent output: success flag, final output, complete trajectory + tool trajectory |
| **MetricBase** | Abstract metric interface; `__call__(output: SolutionOutput) -> MetricResult` |
| **MetricResult** | Categorical/numerical metric with score + message + timestamp |
| **BenchmarkBase** | Dataset of Tasks; implements iterator interface for systematic agent testing |
| **GeneralEvaluator** | Sequential, debugging-focused; iterates tasks, calls solution fn, persists via FileEvaluatorStorage |
| **RayEvaluator** | Distributed via Ray; drop-in replacement for GeneralEvaluator; distributes tasks across CPU/GPU workers |
| **EvaluatorStorageBase** | Persistent result storage with checkpoint resumption |
| **OpenJudgeMetric** | Adapter wrapping OpenJudge's 50+ professional graders for subjective quality assessment |

**ACEBench -- Full Specification** (arXiv:2501.12851):

Dataset: **2,000 annotated entries** in Chinese + English parallel versions.

| Category | Description | Evaluation Method | Metric |
|----------|-------------|-------------------|--------|
| **Normal** | Single-turn + multi-turn tool usage in unambiguous scenarios. Subtypes: atomic, similar-API, preference, multi-turn | AST parsing vs ground truth; multiple valid answer pools | Binary accuracy (1=match, 0=mismatch) |
| **Special** | Imperfect instructions: missing parameters, format errors, task-function mismatches | 3 problem-identification capabilities assessed per case | Binary accuracy per capability |
| **Agent** | Multi-turn, multi-step real-world simulations; GPT-4o as user simulator | End-to-End accuracy (instance attrs) + Process accuracy (n/m: actual/ideal function calls) | E2E accuracy + Process accuracy |

**Overall accuracy formula**: Weighted combination using sqrt(sample_size) as coefficients across the 3 data types.

**LLM leaderboard results** (combined CN+EN):
| Model | Overall Accuracy |
|-------|-----------------|
| GPT-4o | 85.4% |
| GPT-4-Turbo | 84.5% |
| Qwen2.5-Coder-32B | 79.6% (best open-source) |

**Key finding**: Fine-tuned tool models degrade significantly on Special data -- task-specific optimization causes generalization loss.

**Integration**: Observability pipeline auto-collects OTel telemetry (LLM calls, tool usage, token counts) during evaluation runs.

### 2.14 Observability / Tracing

| Component | Purpose |
|-----------|---------|
| **@trace_llm** | Decorator for ChatModelBase calls |
| **@trace_reply** | Decorator for AgentBase.reply() |
| **@trace_format** | Decorator for FormatterBase.format() |
| **@trace** | Generic span wrapper |
| **agentscope.init()** | Entry point: sets metadata, logging, OTLP config |

Backends: AgentScope Studio, Alibaba CloudMonitor, Arize-Phoenix, Langfuse.
Protocol: OpenTelemetry (OTel).

### 2.15 RAG Components

| Class | Purpose |
|-------|---------|
| **KnowledgeBase** | Semantic retrieval interface |
| **SimpleKnowledgeBase** | Basic implementation |
| **VectorStore** | Embedding storage abstraction |
| **DocumentReader** | Multi-format file parser |

Supports LlamaIndex and LangChain as backend RAG frameworks.
Knowledge Bank = collection of knowledge containers, configured via JSON.

### 2.16 Configuration

| Component | Purpose |
|-----------|---------|
| **model_configs** | JSON: model parameters, API endpoints, provider details |
| **agent_configs** | JSON: agent characteristics, system prompts, tool bindings |
| **agentscope.init()** | Loads configs, sets file storage, logging, supported platforms |
| **_ConfigCls** | Thread-safe ContextVar: `run_id`, `project`, `name`, `created_at`, `trace_enabled` |

---

## 3. AgentScope Runtime (Production Layer)

Separate package: `agentscope-runtime` (v1.0 Dec 2025, v1.1 Feb 2026).

### 3.1 Core Classes

| Class | Purpose |
|-------|---------|
| **AgentApp** | Primary abstraction -- directly inherits FastAPI (v1.1+) |
| **RedisSession** | State persistence: conversation history, agent snapshots, multi-session coordination |
| **A2ARegistry** | Abstract base for service registration/discovery backends |
| **A2ATransportsProperties** | Transport endpoint descriptor: host/port/path, TLS flags, protocol type |
| **AgentCardWithRuntimeConfig** | Configuration bundle: agent_card + registry list + task_timeout |

**AgentApp lifecycle**: Init (lifespan) -> Query (`@agent_app.query()`) -> Shutdown.
Primary endpoint: `/process` via SSE streaming.

**v1.1 key change**: AgentApp now directly inherits FastAPI (not factory pattern).
Enables seamless access to the full FastAPI ecosystem (middleware, routers, dependency injection).

### 3.2 Sandbox Types

| Sandbox | Sync | Async (v1.1) | Purpose |
|---------|------|--------------|---------|
| **BaseSandbox** | Yes | **BaseSandboxAsync** | Python/shell execution |
| **GuiSandbox** | Yes | **GuiSandboxAsync** | Desktop GUI interaction |
| **FilesystemSandbox** | Yes | **FilesystemSandboxAsync** | File operations |
| **BrowserSandbox** | Yes | **BrowserSandboxAsync** | Web automation |
| **MobileSandbox** | Yes | **MobileSandboxAsync** | Mobile app testing |
| **TrainingSandbox** | Yes | -- | ML model training |
| **AgentbaySandbox** | Yes | -- | Specialized environment |

Container backends: Docker (default), gVisor, BoxLite, Kubernetes, Alibaba Cloud ACK.

**v1.1 async sandboxes**: `run_ipython_cell` and `run_shell_command` enhanced for non-blocking
concurrent execution in async programs. Enables parallel tool calls across multiple sandboxes.

### 3.3 Distributed Interrupt Service (v1.1 NEW)

New service enabling:
- Manual task preemption during long-running agent execution
- Customizable state persistence before interrupt
- Recovery logic injection on resume
- Greater developer control over multi-step agentic workflows

### 3.4 A2A Registry Service (v1.1)

Plugin-based service registration and discovery. Agents register with centralized registries
(e.g., Nacos) on startup. Configured via `a2a_config` parameter in AgentApp.

| Component | Purpose |
|-----------|---------|
| **A2ARegistry** | Abstract base class; requires `registry_name()` + `register()` |
| **NacosRegistry** | Nacos v3.1.0+ dynamic service discovery backend |
| **A2ATransportsProperties** | host/port/path + TLS + transport type (JSONRPC) |

**Registration flow** (async, non-blocking):
1. Agent Card Publication -- metadata (name, version, capabilities)
2. Endpoint Registration -- connection info + protocol config
3. Background execution -- failures log warnings without blocking startup

**Nacos env vars**: `A2A_REGISTRY_ENABLED`, `NACOS_SERVER_ADDR`, auth credentials.
Custom registries: inherit `A2ARegistry`, implement required methods.

### 3.5 Framework Compatibility

| Framework | Messages | Tools |
|-----------|----------|-------|
| AgentScope | Full | Full |
| LangGraph | Full | In Progress |
| Microsoft Agent | Full | Full |
| Agno | Full | Full |
| AutoGen | In Progress | Full |

### 3.6 Response Streaming Format

JSON lines via SSE with fields: `sequence_number`, `object`, `status`, payload.
Compatible with OpenAI SDK response format.

---

## 4. ReMe Memory System

Separate package: `agentscope-ai/ReMe` ("Remember Me, Refine Me").

### 4.1 Architecture Layers

| Layer | Purpose |
|-------|---------|
| **ReMe Class** | Public API methods |
| **Handler Layer** | Low-level operations |
| **Agent Layer** | Specialized memory agents |
| **Storage Layer** | Vector stores, embeddings, profile files |

### 4.2 Core Classes

| Class | Purpose |
|-------|---------|
| **ReMeLight** | File-based memory management (lightweight) |
| **ReMe** | Vector-based memory management (full) |
| **ReMeApp** | Service wrapper: HTTP / MCP / Python API |
| **ReMeInMemoryMemory** | Extends AgentScope's InMemoryMemory with token-aware management |
| **Application** | Lifecycle orchestrator for services |
| **ServiceContext** | Runtime registry holding component instances |

### 4.3 Memory Type Agents

| Agent Type | Agent Classes | Purpose |
|------------|---------------|---------|
| Personal Memory | **PersonalSummarizer**, **PersonalRetriever**, **ProfileHandler** | User preferences, habits, profile JSON |
| Procedural Memory | **ProceduralSummarizer**, **ProceduralRetriever** | Task success/failure patterns, lessons learned |
| Tool Memory | **ParseToolCallResultOp**, **SummaryToolMemoryOp**, **ToolRetriever** | Tool usage patterns, cost metrics, execution guidelines |
| Working Memory | **ReMeInMemoryMemory**, **Compactor**, **ContextChecker** | Short-term context, token management, compression |

### 4.4 Storage

| Component | Purpose |
|-----------|---------|
| **FileStore** | MEMORY.md + daily journal files (`memory/YYYY-MM-DD.md`) |
| **FileWatcher** | Auto-indexes markdown files on filesystem changes |
| **ToolResultCompactor** | Caches truncated tool outputs |
| **BaseVectorStore** | Interface for vector backends |
| Vector backends | Local, ChromaDB, Qdrant, Elasticsearch |
| **MemoryHandler** | Converts memory objects to VectorNode entries |

### 4.5 Memory Schema Objects

| Schema | Source | Purpose |
|--------|--------|---------|
| **PersonalMemory** | `reme_ai/schema/memory.py:157-172` | User preference memory |
| **TaskMemory** | `reme_ai/schema/memory.py:93-104` | Task execution memory |
| **ToolMemory** | `reme_ai/schema/memory.py:205-220` | Tool usage memory |

### 4.6 Search / Retrieval

- **MemorySearch**: Hybrid vector + BM25 ranking (`vector_weight` default 0.7)
- **retrieve_memory()**: Semantic search with LLM synthesis + time-aware filtering
- Per-memory-type retrievers with metadata filtering

### 4.7 Flow Orchestration

Expression-based flows: `>>` (sequential), `|` (parallel).
Named flows: `retrieve_personal_memory`, `summary_task_memory`, etc.
**BaseOp**: Template method pattern for all operations, with lazy-loaded properties.

### 4.8 Registry Pattern

**RegistryFactory**: Singleton mapping backends to implementations.
Per-type registries: `llms`, `as_llms`, `embedding_models`, `vector_stores`, `file_stores`.
Registration via `@R.<registry>.register(name)` decorator.

### 4.9 Token Management

| Component | Purpose |
|-----------|---------|
| **TokenCounter** | Pluggable token counting implementations |
| **rule_token_counter** | AgentScope model compatibility |
| **hf_token_counter_utils** | Hugging Face tokenizer support |
| **memory_compact_threshold** | Triggers compaction when exceeded |
| **max_messages_in_context** | Message window retention limit |
| **truncate_text_utils** | Automatic token-aware truncation |

### 4.10 File Storage Layout

```
.reme/
  MEMORY.md                  # Long-term facts and insights
  profile/<user>.json        # Personal memory profiles
memory/
  YYYY-MM-DD.md              # Daily interaction journals (compressed summaries)
dialog/
  YYYY-MM-DD.jsonl           # Raw conversation records (full fidelity, JSONL format)
tool_result/
  <uuid>.txt                 # Cached/truncated tool outputs (TTL-managed)
```

**Two-track persistence**: `memory/` stores human-readable summarized insights;
`dialog/` stores full raw JSONL for replay/audit. Messages marked `_MemoryMark.COMPRESSED`
indicate the summary exists in `memory/`; raw record is in `dialog/`.

**Memory mark taxonomy**:
| Mark | Value | Meaning |
|------|-------|---------|
| `_MemoryMark.HINT` | "hint" | Temporary contextual guidance injected per step |
| `_MemoryMark.COMPRESSED` | "compressed" | Message replaced by summary; raw in dialog/ |

---

## 5. Distributed Architecture (v0.x Actor Model)

The original paper (2402.14034) described an Actor-based distributed system:

| Component | Purpose |
|-----------|---------|
| **to_dist()** | Convert local agent to distributed agent (single function call) |
| **AgentServerLauncher** | Remote machine: receives requests, auto-initializes agents |
| **Placeholder** | Novel data structure: allows main process to continue without blocking |
| **RPC** | Inter-agent communication protocol |
| **ASDiGraph** | DAG representation for multi-agent workflow graphs |

**Placeholder mechanism**: Preserves information for later value retrieval. Main process
continues execution; temporary blocking only occurs when actual values are needed for
decision-making (conditionals).

**DAG node types**: Model nodes, Service nodes, Agent nodes, Pipeline nodes, Message nodes, Copy nodes.

**Execution modes**: Direct-run (topological order) or To-Python compiler (DAG -> Python script).

v1.0 replaced this with FastAPI-based Agent-as-a-Service (AgentScope Runtime).

---

## 6. Fault Tolerance

| Error Type | Resolution |
|------------|------------|
| Accessibility errors | Auto-retry with configurable max_retries |
| Rule-resolvable errors | Rule-based correction without LLM call |
| Model-resolvable errors | LLM self-critique / pairwise critique |
| Unresolvable errors | Human-augmented critique |

**Customizable handlers**: `parse_func`, `fault_handler`, `max_retries` parameters.
**Response parsers**: Markdown fenced code blocks, JSON objects, tagged contents.

---

## 7. Unique Chinese-Origin Concepts

Concepts that originated in AgentScope or have distinct Chinese AI ecosystem context:

| Concept | Description | Unique Aspect |
|---------|-------------|---------------|
| **DashScope integration** | Native Alibaba Cloud LLM API | First-class Qwen model support; all Chinese models via DashScope |
| **Mark system** | String labels on messages for categorization | Unique per-message tagging not seen in Western frameworks |
| **Service vs Tool distinction** | Services return ServiceResponse; Tools are "processed services" with JSON schema | Explicit separation (most frameworks conflate these) |
| **Placeholder mechanism** | Non-blocking data structure for distributed agents | Novel contribution for automatic parallelism |
| **ReMe ("Remember Me, Refine Me")** | 4-type memory taxonomy: personal, procedural, tool, working | More granular than Western memory systems (LangChain has 1-2 types) |
| **Group-wise tool management** | Tool groups to mitigate "paradox of choice" | Addresses tool overload problem explicitly |
| **Friday** | Built-in Studio copilot agent | Meta-agent that helps build agents |
| **Dynamic compression** | Real-time semantic extraction during conversations | Distinguished from batch summarization |
| **Hybrid compression** | Combining summarization + selective retention | Two-strategy memory compression |
| **ACEBench** | Multi-domain evaluation for tool usage + collaboration | Chinese ecosystem-specific benchmark |
| **Tuner module** | Model adaptation/finetuning integration | Native finetuning loop inside agent framework |
| **Trinity-RFT** | Agentic RL (reinforcement learning from trajectories) | RL integrated directly into agent framework |
| **ASDiGraph** | DAG compiler: JSON -> Python script for agent workflows | Visual-to-code compilation |
| **Knowledge Bank** | Collection of knowledge containers with weighted fusion | Multi-RAG-object result fusion |
| **ModelScope ecosystem** | Integration with Alibaba's model hub | Chinese model ecosystem bridge |
| **Tongyi (Tongyi Qianwen)** | Alibaba's foundational model family | Deep integration: DashScope API is the native provider |

---

## 8. CEX Kind Mapping

| AgentScope Concept | CEX Kind | CEX Pillar | Notes |
|-------------------|----------|------------|-------|
| AgentBase / ReActAgent | `agent` | P02 | Direct mapping |
| A2AAgent | `handoff_protocol` | P02/P06 | A2A protocol proxy |
| Msg | `message_type` | P06 | Universal message container |
| ContentBlock (TextBlock, ToolUseBlock, etc.) | `type_def` | P06 | Typed message content blocks |
| SequentialPipeline | `chain` | P03 | Sequential agent composition |
| FanoutPipeline | `workflow` | P12 | Concurrent fan-out |
| MsgHub | `workflow_primitive` | P12 | Broadcast orchestration |
| ChatRoom | `workflow_primitive` | P12 | Realtime voice orchestration |
| ChatModelBase + providers | `model_provider` | P02 | Multi-provider abstraction |
| FormatterBase + providers | `formatter` | P05 | Provider-specific formatting |
| Toolkit / ToolFunction | `toolkit` / `function_def` | P04 | Tool management |
| MCP integration | `mcp_server` | P04 | MCP client support |
| InMemoryMemory | `memory_scope` | P10 | Short-term buffer |
| RedisMemory | `memory_scope` | P10 | Distributed short-term |
| LongTermMemoryBase / Mem0 | `entity_memory` | P10 | Cross-session persistence |
| ReMe | `entity_memory` + `memory_summary` | P10 | 4-type memory taxonomy |
| CompressionConfig / SummarySchema | `memory_summary` | P10 | Memory compression |
| StateModule / state_dict | `session_state` | P10 | Agent state persistence |
| JSONSession / RedisSession | `session_state` | P10 | Session storage backends |
| Hook system (pre/post_reply, etc.) | `hook` | P04/P07 | Non-invasive extensibility |
| PlanNotebook / Plan / SubTask | `action_prompt` | P03 | Hierarchical task planning |
| MetaPlannerAgent | `agent` + `workflow` | P02/P12 | Dual-mode planning agent |
| DeepResearchAgent | `research_pipeline` | P04 | Tree-structured research |
| BrowserAgent | `browser_tool` | P04 | Web automation |
| Task / SolutionOutput / MetricBase | `benchmark` / `scoring_rubric` | P07 | Evaluation framework |
| ACEBench | `benchmark` | P07 | Built-in agent benchmark |
| KnowledgeBase / VectorStore | `knowledge_index` / `vector_store` | P01/P10 | RAG components |
| DocumentReader | `document_loader` | P04 | File ingestion |
| ServiceFactory | `function_def` | P04 | Service-to-tool conversion |
| AgentApp (Runtime) | `agent_card` | P08 | Agent-as-a-Service deployment |
| Sandbox types | `code_executor` | P04 | Secure execution environments |
| @trace decorators | `trace_config` | P07 | OpenTelemetry observability |
| agentscope.init() | `boot_config` | P02 | Framework initialization |
| model_configs / agent_configs | `env_config` | P09 | Runtime configuration |
| Placeholder (v0.x distributed) | `workflow_primitive` | P12 | Non-blocking async data |
| AgentServerLauncher (v0.x) | `deployment_config` | P08 | Distributed agent server |
| to_dist() (v0.x) | -- | -- | Local-to-distributed conversion (no CEX equivalent) |

---

## 9. Protocol Support

| Protocol | Support Level | Implementation |
|----------|--------------|----------------|
| **A2A (Agent-to-Agent)** | Native (Dec 2025) | A2AAgent + A2AChatFormatter |
| **MCP (Model Context Protocol)** | Native | HttpStatelessClient, StatefulClientBase, get_callable_function |
| **OpenAI API** | Compatible | Response format, tool calling schema |
| **SSE (Server-Sent Events)** | Native | AgentApp streaming via /process endpoint |
| **OpenTelemetry** | Native | @trace decorators, OTLP export |
| **FastAPI** | Native (Runtime) | AgentApp extends FastAPI directly |

---

## 10. Comparison: AgentScope vs Major Frameworks

| Dimension | AgentScope | LangGraph | CrewAI | AutoGen |
|-----------|------------|-----------|--------|---------|
| Message type | `Msg` (typed ContentBlocks) | dict-based | string | dict-based |
| Multi-agent broadcast | MsgHub (auto) | Manual edges | Implicit crew | GroupChat |
| Memory compression | Dynamic + Hybrid | Manual | None built-in | None built-in |
| Tool management | Toolkit + groups | ToolNode | Tool decorator | FunctionMap |
| State persistence | StateModule (nested) | Checkpointer | None built-in | None built-in |
| Distributed mode | Actor/Placeholder (v0.x), FastAPI (v1.0) | None | None | None |
| Formatter abstraction | Per-provider Chat + MultiAgent | None (tied to provider) | None | None |
| Hook system | 10 hook types, class + instance | Interrupts only | None | None |
| Planning | PlanNotebook + MetaPlanner | Subgraph | Hierarchical Crew | None built-in |
| Evaluation | ACEBench + MetricBase + Ray | None built-in | None built-in | None built-in |
| Voice/Realtime | Native (VoiceAgent, ChatRoom) | None | None | None |
| Sandbox execution | 7 sandbox types | None | None | Docker only |

---

## 11. Key Architectural Insights

1. **Formatter as first-class concern**: AgentScope is the only framework that
   treats provider-specific message formatting as an explicit, pluggable layer.
   This is architecturally significant -- it means the same agent code works
   across providers without modification.

2. **Mark-based message filtering**: The `mark` system on messages enables
   fine-grained memory queries without separate index structures. No other
   major framework has this.

3. **Service vs Tool separation**: Explicitly distinguishing raw service functions
   from LLM-consumable tools (with JSON schema) is a clean architectural boundary
   that most frameworks blur.

4. **ReMe's 4-type memory**: Personal + Procedural + Tool + Working memory is
   the most granular memory taxonomy in any agent framework. Most have at most
   "short-term" and "long-term".

5. **Non-blocking Placeholder**: The v0.x distributed architecture's Placeholder
   mechanism for automatic parallelism is a genuine novelty -- it allows
   centralized sequential code to execute with distributed parallelism.

6. **Group-wise tool management**: Explicitly addressing "paradox of choice"
   (too many tools degrade LLM performance) via tool groups is a practical
   insight not found in other frameworks.

7. **Dual-mode LTM control**: Agent-controlled vs developer-controlled memory
   access acknowledges that different use cases need different control points.

8. **Hook-based extensibility via metaclass**: The 10-hook system with class/instance
   separation and OrderedDict ordering is the most sophisticated hook system
   in any agent framework.

---

## 12. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v0.x | Feb 2024 | Original: Actor-based distribution, RPC, Placeholder, ASDiGraph |
| v1.0 | Sep 2025 | Major rewrite: async-first, ContentBlock, Formatter abstraction, ReMe, Runtime split |
| Runtime v1.0 | Dec 2025 | Agent-as-a-Service, sandbox types, A2A protocol, cross-framework compat |
| Runtime v1.1 | Feb 2026 | FastAPI direct inheritance, Distributed Interrupt Service, async sandboxes, A2A Registry (Nacos) |

---

## 13. A2A Protocol Deep Dive

A2A (Agent-to-Agent) protocol: open standard for cross-framework agent communication.
AgentScope added native A2A support in Runtime v1.0 (Dec 2025).

### 13.1 AgentCard Schema

The AgentCard is the agent's "business card" -- a JSON file at `/.well-known/agent-card.json`.

| Field | Type | Purpose |
|-------|------|---------|
| `name` | string | Agent identifier |
| `url` | string | RPC service endpoint |
| `description` | string | Agent purpose/behavior |
| `version` | string | Release version |
| `capabilities` | object | Feature support configuration |
| `default_input_modes` | array | Accepted formats (e.g., "text/plain") |
| `default_output_modes` | array | Response formats |
| `skills` | array | Available agent capability list |

### 13.2 A2AChatFormatter

`A2AChatFormatter` handles bidirectional protocol conversion:
- AgentScope `Msg` -> A2A `Message` format (for sending to remote agents)
- A2A `Message` -> `Msg` format (for receiving from remote agents)
- A2A `Task` responses -> `Msg` (for task-oriented interactions)
- Multimodal content: text, images, audio, video passthrough

**Distinction from standard formatters**: Unlike provider-specific formatters
(OpenAI/Anthropic/etc.), A2AChatFormatter handles protocol-level serialization
to the JSON-RPC A2A wire format, not LLM API format.

### 13.3 A2AAgent Implementation

```python
agent = A2AAgent(agent_card=agent_card)
```

Supported patterns:
1. **Chatbot scenario**: Direct conversation with remote A2A agent
2. **Tool function**: Encapsulate A2AAgent as a tool in Toolkit for handoff/router patterns

**Behavior note**: `observe()` calls store messages locally and send them together during `reply()`.
This batching differs from local agents where `observe()` and `reply()` are independent.

### 13.4 Card Resolver Classes

| Class | Backend | Purpose |
|-------|---------|---------|
| **FileAgentCardResolver** | Local JSON file | Load AgentCard from filesystem |
| **WellKnownAgentCardResolver** | HTTP fetch | Fetch from `/.well-known/agent-card.json` at remote URL |
| **NacosAgentCardResolver** | Nacos v3.1.0+ | Retrieve from Nacos Agent Registry |
| **AgentCardResolverBase** | Abstract | Base class for custom resolvers |

### 13.5 Protocol Flow

```
User message
    |
    v
A2AAgent.reply()
    |-- Batch observed messages + new message
    |-- A2AChatFormatter: Msg list -> A2A JSON-RPC Message
    |-- HTTP/SSE call to remote agent's /process endpoint
    |
    v
Remote Agent (any A2A-compliant framework)
    |-- Processes A2A Message
    |-- Returns A2A Task response via SSE
    |
    v
A2AChatFormatter: A2A Task response -> Msg
    |
    v
Return to local pipeline
```

### 13.6 A2A vs MCP Positioning

| Dimension | A2A | MCP |
|-----------|-----|-----|
| Target | Agent-to-Agent (peer interaction) | Model-to-Context (tool/data access) |
| Protocol | JSON-RPC over HTTP/SSE | JSON-RPC over stdio/HTTP |
| Discovery | AgentCard at .well-known/ | Tool schema from server |
| Direction | Bidirectional (both sides are agents) | Unidirectional (model calls server) |
| AgentScope support | A2AAgent + A2AChatFormatter | HttpStatelessClient + StatefulClientBase |

---

## 14. Sources

- [GitHub: agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)
- [GitHub: agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)
- [GitHub: agentscope-ai/ReMe](https://github.com/agentscope-ai/ReMe)
- [Paper: AgentScope v0.x (arXiv:2402.14034)](https://arxiv.org/abs/2402.14034)
- [Paper: AgentScope 1.0 (arXiv:2508.16279)](https://arxiv.org/html/2508.16279v1)
- [Paper: ACEBench (arXiv:2501.12851)](https://arxiv.org/abs/2501.12851)
- [Docs: doc.agentscope.io](https://doc.agentscope.io/)
- [Docs: docs.agentscope.io](https://docs.agentscope.io/)
- [Runtime docs: runtime.agentscope.io](https://runtime.agentscope.io/)
- [DeepWiki: agentscope-ai/agentscope](https://deepwiki.com/agentscope-ai/agentscope)
- [DeepWiki: agentscope-ai/ReMe](https://deepwiki.com/agentscope-ai/ReMe)
- [ReMe docs: reme.agentscope.io](https://reme.agentscope.io/)
- [MarkTechPost: Production AgentScope Workflows](https://www.marktechpost.com/2026/04/01/how-to-build-production-ready-agentscope-workflows-with-react-agents-custom-tools-multi-agent-debate-structured-output-and-concurrent-pipelines/)
- [Alibaba Cloud Blog: Upgraded AgentScope](https://www.alibabacloud.com/blog/multilingual-cosyvoice-3-upgraded-agentscope-for-production-grade-ai-agents-enterprise-ready-ai-coding_602746)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_03_openai_agents_sdk]] | sibling | 0.29 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.26 |
| [[atom_07_llamaindex]] | sibling | 0.24 |
| [[p01_kc_agent]] | sibling | 0.22 |
| [[p01_kc_chinese_llm_ecosystem]] | sibling | 0.21 |
| [[atom_05_semantic_kernel]] | sibling | 0.19 |
| [[bld_collaboration_agent]] | downstream | 0.19 |
| [[atom_09_autogen_ag2]] | sibling | 0.19 |
| [[p03_ch_kc_to_notebooklm]] | downstream | 0.19 |
| [[p01_kc_terminology_anthropic_canonical]] | sibling | 0.19 |
