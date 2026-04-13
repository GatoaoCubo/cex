---
id: atom_06_langchain_langgraph
kind: knowledge_card
pillar: P01
domain: agentic-frameworks
title: "LangChain LCEL + LangGraph + LangSmith -- Complete Vocabulary Atlas"
version: 2.0.0
quality: 8.8
tags: [langchain, langgraph, langsmith, lcel, runnable, stategraph, observability, agent-framework, langgraph-platform, pregel, hitl, datasets]
sources:
  - https://docs.langchain.com/oss/python/langgraph/graph-api
  - https://docs.langchain.com/langsmith/observability-concepts
  - https://reference.langchain.com/python/langchain_core/
  - https://docs.langchain.com/oss/python/langgraph/use-functional-api
  - https://langchain-ai.github.io/langgraph/reference/agents/
  - https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html
  - https://docs.langchain.com/langgraph-platform/deployment-options
  - https://docs.langchain.com/langgraph-platform/langgraph-server
  - https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/
  - https://docs.langchain.com/oss/python/langgraph/interrupts
  - https://docs.smith.langchain.com/evaluation/how_to_guides/manage_datasets_programmatically
  - https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client
  - https://blog.langchain.dev/langgraph-platform-ga/
date: 2026-04-13
---

# Atom 06 -- LangChain LCEL + LangGraph + LangSmith

> Exhaustive vocabulary extraction for CEX pillar mapping.
> Covers: langchain-core 0.3.x, langgraph 0.x, LangSmith SaaS.

---

## 1. LCEL Runnable Type Hierarchy

LCEL (LangChain Expression Language) is the composition protocol. Every component
implements `Runnable`, which defines invoke/batch/stream + pipe operator (`|`).

### 1.1 Runnable Interface (methods on every LCEL object)

| Method | Sync | Async | Purpose |
|--------|------|-------|---------|
| `invoke(input)` | yes | `ainvoke` | Single-input execution |
| `batch(inputs)` | yes | `abatch` | Multi-input parallel execution |
| `stream(input)` | yes | `astream` | Token-level streaming |
| `astream_events(input)` | -- | yes | Event-level streaming (v2) |
| `astream_log(input)` | -- | yes | Log-patch streaming |
| `bind(**kwargs)` | yes | -- | Bind kwargs to runnable |
| `with_config(config)` | yes | -- | Override RunnableConfig |
| `with_retry(...)` | yes | -- | Add retry policy |
| `with_fallbacks(...)` | yes | -- | Add fallback chain |
| `assign(**kwargs)` | yes | -- | Merge additional runnables into output |
| `pick(keys)` | yes | -- | Select subset of output keys |
| `pipe(other)` | yes | -- | Compose sequentially (same as `\|`) |
| `get_graph()` | yes | -- | Return graph representation |
| `get_name()` | yes | -- | Return runnable name |
| `get_input_schema()` | yes | -- | Pydantic model for input |
| `get_output_schema()` | yes | -- | Pydantic model for output |

### 1.2 Runnable Subclass Hierarchy

```
Runnable (abstract base -- langchain_core.runnables.base)
  |
  +-- RunnableSerializable (adds JSON serialization)
  |     +-- RunnableSequence          # chain: A | B | C
  |     +-- RunnableParallel          # fan-out: {"a": A, "b": B}
  |     +-- RunnableLambda            # wrap plain function
  |     +-- RunnableEach              # apply to each item
  |     +-- RunnableBinding           # bind kwargs
  |     +-- RunnableGenerator         # generator/async-generator
  |     +-- RunnableAssign            # merge keys into output
  |     +-- RunnablePick              # select output keys
  |     +-- RunnableBranch            # conditional dispatch
  |     +-- RouterRunnable            # key-based routing
  |     +-- RunnableWithFallbacks     # fallback chain
  |     +-- RunnableRetry             # retry with backoff
  |     +-- RunnableWithMessageHistory# inject chat history
  |     +-- RunnableConfigurableFields# runtime-configurable params
  |     +-- RunnableConfigurableAlternatives # swap implementations
  |     +-- DynamicRunnable           # runtime-resolved runnable
  |     +-- RunnablePassthrough       # identity (pass input through)
  |
  +-- BaseChatModel --> all chat models (ChatOpenAI, ChatAnthropic, etc.)
  +-- BaseLLM --> all completion models
  +-- BaseRetriever --> all retrievers
  +-- BaseOutputParser --> all output parsers
  +-- BasePromptTemplate --> all prompt templates
  +-- BaseTool --> all tools
```

### 1.3 Composition Primitives

| Primitive | Syntax | Semantics |
|-----------|--------|-----------|
| `RunnableSequence` | `A \| B \| C` | Serial: output(A) -> input(B) -> input(C) |
| `RunnableParallel` | `{"a": A, "b": B}` | Parallel: same input -> both, merge outputs |
| `RunnableBranch` | `RunnableBranch([(cond, A)], default=B)` | First-match conditional |
| `RunnablePassthrough` | `RunnablePassthrough()` | Identity function (pipe-through) |
| `RunnableAssign` | `.assign(key=runnable)` | Merge new keys into dict output |
| `RunnablePick` | `.pick("key")` | Select keys from dict output |
| `RunnableWithFallbacks` | `.with_fallbacks([B, C])` | Try A, on failure try B, then C |

### 1.4 Configuration

| Class | Purpose |
|-------|---------|
| `RunnableConfig` | Dict with `run_name`, `tags`, `metadata`, `callbacks`, `max_concurrency`, `recursion_limit`, `configurable` |
| `ExponentialJitterParams` | Retry backoff parameters |
| `ContextThreadPoolExecutor` | Thread pool for sync-in-async |

---

## 2. LangChain Core Components (langchain_core)

### 2.1 Messages

| Class | Role | Chunk variant |
|-------|------|---------------|
| `BaseMessage` | Abstract base | `BaseMessageChunk` |
| `HumanMessage` | User input | `HumanMessageChunk` |
| `AIMessage` | Model response | `AIMessageChunk` |
| `SystemMessage` | System instruction | `SystemMessageChunk` |
| `ToolMessage` | Tool result (has `tool_call_id`) | `ToolMessageChunk` |
| `FunctionMessage` | Legacy function result | `FunctionMessageChunk` |
| `ChatMessage` | Generic with `role` field | `ChatMessageChunk` |
| `ToolCall` | Structured tool invocation (in `AIMessage.tool_calls`) | `ToolCallChunk` |
| `InvalidToolCall` | Malformed tool call | -- |

Content block types: text, image, video, audio, file, reasoning (multimodal).

### 2.2 Prompts

| Class | Purpose |
|-------|---------|
| `BasePromptTemplate` | Abstract prompt base |
| `PromptTemplate` | String template with `{variables}` |
| `ChatPromptTemplate` | List of message templates |
| `MessagesPlaceholder` | Inject dynamic message list |
| `SystemMessagePromptTemplate` | System message template |
| `HumanMessagePromptTemplate` | Human message template |
| `AIMessagePromptTemplate` | AI message template |
| `FewShotPromptTemplate` | Few-shot with example selector |
| `FewShotChatMessagePromptTemplate` | Chat-format few-shot |
| `ImagePromptTemplate` | Image input template |
| `DictPromptTemplate` | Dict-structured template |
| `StructuredPrompt` | Pydantic-validated prompt |

### 2.3 Output Parsers

| Class | Output type |
|-------|-------------|
| `BaseOutputParser` | Abstract base |
| `StrOutputParser` | Raw string |
| `JsonOutputParser` | JSON dict |
| `PydanticOutputParser` | Pydantic model instance |
| `ListOutputParser` | List base |
| `CommaSeparatedListOutputParser` | `["a", "b", "c"]` |
| `NumberedListOutputParser` | Numbered list |
| `MarkdownListOutputParser` | Markdown bullets |
| `XMLOutputParser` | XML structure |
| `JsonOutputToolsParser` | Tool-call JSON |
| `PydanticToolsParser` | Tool-call Pydantic |
| `BaseCumulativeTransformOutputParser` | Streaming accumulator |

### 2.4 Language Models

| Class | Layer |
|-------|-------|
| `BaseLanguageModel` | Abstract root |
| `BaseLLM` | Completion models (text-in, text-out) |
| `BaseChatModel` | Chat models (messages-in, message-out) |
| `SimpleChatModel` | Minimal chat implementation |
| `LLM` | Convenience base for custom LLMs |

Key methods: `invoke`, `generate`, `predict`, `bind_tools`, `with_structured_output`.

### 2.5 Tools

| Class/Decorator | Purpose |
|-----------------|---------|
| `BaseTool` | Abstract tool base |
| `StructuredTool` | Tool with Pydantic args schema |
| `Tool` | Simple tool (string input) |
| `@tool` | Decorator to create tool from function |
| `BaseToolkit` | Collection of related tools |
| `ToolException` | Graceful tool failure |
| `InjectedToolArg` | Arg injected by runtime, hidden from LLM |
| `InjectedToolCallId` | Auto-inject tool_call_id |
| `RetrieverInput` | Pydantic model for retriever-as-tool |

### 2.6 Documents & Retrievers

| Class | Purpose |
|-------|---------|
| `Document` | Text + metadata container |
| `BaseMedia` / `Blob` | Binary media container |
| `BaseRetriever` | Abstract retriever (implements Runnable) |
| `VectorStoreRetriever` | Retriever backed by vector store |
| `BaseDocumentTransformer` | Transform documents (split, filter) |
| `BaseDocumentCompressor` | Compress/rerank documents |
| `BaseLoader` | Document loader base |

### 2.7 Embeddings & Vector Stores

| Class | Purpose |
|-------|---------|
| `Embeddings` | Abstract embedding model |
| `VectorStore` | Abstract vector store |
| `InMemoryVectorStore` | In-memory reference implementation |

### 2.8 Callbacks & Tracers

| Class | Purpose |
|-------|---------|
| `BaseCallbackHandler` | Sync callback handler |
| `AsyncCallbackHandler` | Async callback handler |
| `BaseCallbackManager` | Manages callback handlers |
| `StdOutCallbackHandler` | Print to stdout |
| `StreamingStdOutCallbackHandler` | Stream tokens to stdout |
| `FileCallbackHandler` | Write to file |
| `UsageMetadataCallbackHandler` | Track token usage |
| `BaseTracer` | Trace execution tree |
| `LangChainTracer` | Send traces to LangSmith |
| `LogStreamCallbackHandler` | Stream execution log |
| `ConsoleCallbackHandler` | Console output tracer |

Callback events: `on_llm_start`, `on_llm_end`, `on_llm_error`, `on_chat_model_start`,
`on_chain_start`, `on_chain_end`, `on_chain_error`, `on_tool_start`, `on_tool_end`,
`on_tool_error`, `on_retriever_start`, `on_retriever_end`, `on_retriever_error`,
`on_text`, `on_agent_action`, `on_agent_finish`.

### 2.9 Storage & Memory

| Class | Purpose |
|-------|---------|
| `BaseStore` | Abstract key-value store |
| `InMemoryStore` | In-memory store |
| `InMemoryByteStore` | In-memory byte store |
| `BaseChatMessageHistory` | Abstract chat history |
| `InMemoryChatMessageHistory` | In-memory chat history |
| `RecordManager` | Dedup/indexing record manager |
| `DocumentIndex` | Document indexing interface |
| `BaseCache` | LLM response cache |
| `InMemoryCache` | In-memory LLM cache |
| `BaseRateLimiter` | Rate limiting base |

### 2.10 Agents (legacy + LangGraph)

| Class | Purpose |
|-------|---------|
| `AgentAction` | Single tool call decision |
| `AgentActionMessageLog` | Agent action with message log |
| `AgentStep` | Action + observation pair |
| `AgentFinish` | Terminal agent response |
| `AgentExecutor` | Legacy agent loop (deprecated in favor of LangGraph) |

### 2.11 Example Selectors

| Class | Strategy |
|-------|----------|
| `BaseExampleSelector` | Abstract base |
| `LengthBasedExampleSelector` | Select by token budget |
| `SemanticSimilarityExampleSelector` | Select by embedding similarity |
| `MaxMarginalRelevanceExampleSelector` | MMR diversity selection |

### 2.12 Exceptions

| Exception | When |
|-----------|------|
| `LangChainException` | Base exception |
| `OutputParserException` | Parser failure |
| `ContextOverflowError` | Context window exceeded |
| `TracerException` | Tracing failure |
| `InvalidKeyException` | Bad API key |
| `IndexingException` | Indexing failure |

---

## 3. LangGraph Graph Primitives

### 3.1 Core Graph Classes

| Class | Purpose |
|-------|---------|
| `StateGraph` | Main graph builder -- nodes share typed state |
| `MessageGraph` | Convenience: state = list of messages |
| `CompiledGraph` | Executable graph (result of `.compile()`) |
| `Pregel` | Internal execution engine (inspired by Google Pregel) |

### 3.2 Graph Construction API

| Method | Purpose |
|--------|---------|
| `add_node(name, fn)` | Register a function as a named node |
| `add_edge(src, dst)` | Fixed transition from src to dst |
| `add_conditional_edges(src, fn, mapping)` | Dynamic routing based on fn return |
| `set_entry_point(name)` | (legacy) Set first node |
| `set_finish_point(name)` | (legacy) Set terminal node |
| `compile(checkpointer=, interrupt_before=, interrupt_after=)` | Build executable graph |

### 3.3 Constants & Sentinels

| Constant | Purpose |
|----------|---------|
| `START` | Virtual entry node -- represents user input |
| `END` | Virtual exit node -- represents terminal state |

### 3.4 State Definition

| Mechanism | Purpose |
|-----------|---------|
| `TypedDict` | Standard state schema (most common) |
| `Pydantic BaseModel` | Validated state schema |
| `dataclass` | State with defaults |
| `Annotation` | Attach reducers to individual fields |
| `MessagesState` | Prebuilt state: `{"messages": Annotated[list, add_messages]}` |
| `add_messages` | Prebuilt reducer: append + dedup messages |

State variants:

| Variant | Purpose |
|---------|---------|
| `InputState` | Filtered schema for graph inputs |
| `OutputState` | Filtered schema for graph outputs |
| `OverallState` | Complete internal state |
| `PrivateState` | Internal-only channels (not exposed) |

### 3.5 Reducers

A reducer is a function `(current, update) -> new` that defines how a state key
is updated when multiple nodes write to it.

| Reducer | Behavior |
|---------|----------|
| (default) | Last-write-wins (overwrite) |
| `add_messages` | Append messages, dedup by ID |
| `operator.add` | Concatenate lists |
| Custom `fn(a, b) -> c` | User-defined merge logic |
| `Overwrite` | Force overwrite, bypass reducer |

### 3.6 Control Flow Primitives

| Primitive | Purpose |
|-----------|---------|
| `Command(update=, goto=)` | Combined state update + navigation |
| `Command(resume=)` | Continue after interrupt |
| `Command(graph=Command.PARENT)` | Navigate to parent graph |
| `Send(node, state)` | Dynamic fan-out with custom state per target |

### 3.7 Nodes

Nodes are Python functions `(state) -> update` or `(state, config) -> update`.

| Node type | Source |
|-----------|--------|
| User-defined function | `add_node("name", fn)` |
| `ToolNode` | Prebuilt: execute tool calls from AIMessage |
| Subgraph | Nested compiled graph as a node |

Runtime context available to nodes:

| Object | Access |
|--------|--------|
| `RunnableConfig` | Second arg to node function |
| `context` | Via `config["context"]` (from `context_schema`) |
| `store` | Via `config["store"]` (cross-thread persistence) |
| `stream_writer` | Via `config["stream_writer"]` (custom streaming) |

### 3.8 Execution Model

| Concept | Definition |
|---------|------------|
| Super-step | One iteration over all active nodes |
| Message passing | Nodes communicate via state updates (Pregel model) |
| `recursion_limit` | Max super-steps (default: 25) |
| `GraphRecursionError` | Raised when limit exceeded |
| `langgraph_step` | Current step counter (in config metadata) |
| `RemainingSteps` | Managed value: steps until recursion limit |

Metadata injected into config:

| Key | Value |
|-----|-------|
| `langgraph_node` | Current node name |
| `langgraph_triggers` | Edges that activated current node |
| `langgraph_path` | Execution path taken |
| `langgraph_checkpoint_ns` | Checkpoint namespace |

### 3.8.1 Pregel Execution Model -- Deep Dive

LangGraph's runtime (`Pregel` class) implements the **Bulk Synchronous Parallel (BSP)**
model from Google's 2010 Pregel paper for large-scale graph computation.

**Node Activation Lifecycle (one super-step):**

```
1. All nodes start INACTIVE at graph entry
2. Input routed via START edge activates first node(s)
3. ACTIVE nodes execute: read full state -> emit partial update dict
4. Updates COLLECTED (not yet applied) -- isolation within step
5. Super-step ends: all updates applied atomically via reducers
6. Checkpoint written after step (enables interrupt/resume)
7. Nodes with pending incoming messages become ACTIVE for next step
8. Repeat until no ACTIVE nodes OR recursion_limit exceeded
```

**Transactional Guarantee:**
Super-steps in parallel branches are atomic. If any node in a parallel branch
raises an unhandled exception, NO updates from that super-step are applied --
all-or-nothing prevents partial state corruption.

**Channel Types (state key semantics):**

| Channel type | Behavior | Default reducer |
|-------------|----------|-----------------|
| LastValue | Last-write-wins per key (default) | None (overwrite) |
| Topic | Append-only with dedup by ID | `add_messages` |
| BinaryOperatorAggregate | User-defined merge function | Custom fn(a, b) -> c |
| EphemeralValue | Cleared after each super-step | -- |

**Concurrency rule:** Nodes connected by `Send` (fan-out) or via parallel
conditional edges run in the **same super-step** (concurrent). Nodes connected
by sequential edges run in **separate super-steps**.

**Termination conditions:**

| Condition | Trigger |
|-----------|---------|
| No active nodes | Normal completion -- returns final state |
| `recursion_limit` exceeded | `GraphRecursionError` raised |
| `END` edge traversed | Explicit terminal node reached |
| `interrupt(value)` called | Pause -- checkpoint written, caller receives state |

### 3.9 Persistence & Checkpointing

| Class | Purpose |
|-------|---------|
| `BaseCheckpointSaver` | Abstract checkpoint interface |
| `MemorySaver` | In-memory checkpointer (dev/test) |
| `SqliteSaver` | SQLite-backed checkpointer |
| `PostgresSaver` | Postgres-backed checkpointer (production) |
| `InMemoryCache` | Node-level result cache |

Checkpoint interface methods:

| Method | Purpose |
|--------|---------|
| `.put(config, checkpoint, metadata)` | Store checkpoint |
| `.putWrites(config, writes)` | Store pending writes |
| `.getTuple(config)` | Fetch checkpoint by thread_id + thread_ts |
| `.list(config, filter)` | List checkpoints matching criteria |

Key identifiers:

| ID | Scope |
|----|-------|
| `thread_id` | Conversation-level persistence |
| `thread_ts` | Point-in-time within a thread |
| `checkpoint_ns` | Namespace for subgraph isolation |

### 3.10 Human-in-the-Loop

| Mechanism | Purpose |
|-----------|---------|
| `interrupt(value)` | Pause execution, surface value to user |
| `interrupt_before=[nodes]` | Pause before specified nodes |
| `interrupt_after=[nodes]` | Pause after specified nodes |
| `Command(resume=value)` | Resume execution with user input |

### 3.10.1 Interrupt/Resume -- Implementation Detail

**Interrupt types:**

| Mode | Declaration | When triggered |
|------|-------------|----------------|
| **Static** | `compile(interrupt_before=["node_a"])` | Before/after specified node, always |
| **Dynamic** | `interrupt(value)` inside node body | Conditional, based on state at runtime |

**Dynamic interrupt pattern:**

```python
from langgraph.types import interrupt

def human_review_node(state):
    # Pause here -- surface data to caller
    decision = interrupt({
        "question": "Approve this action?",
        "context": state["proposed_action"]
    })
    # Execution resumes here; decision = value passed in Command(resume=...)
    return {"approved": decision == "approve"}
```

**Resume flow:**

```python
# Invoke hits interrupt -- returns state snapshot
result = graph.invoke(input_data, config)
# result["__interrupt__"] contains the interrupt value surfaced above

# User inspects and decides, then resume:
graph.invoke(Command(resume="approve"), config)
# config MUST have the same thread_id to restore from checkpoint
```

**Multiple interrupts in one node:**
LangGraph tracks a `resume` list per task. On resume, execution restarts
from the top of the node. Each `interrupt()` call is matched index-based
against the resume list -- consumed interrupts are skipped, first unconsumed halts.

**Persistence requirement:**
`interrupt` requires a `checkpointer` in `compile()`. Without it, a
`GraphInterruptException` is raised. The checkpointer stores full graph
state including all pending resume values.

**State inspection during interrupt:**

```python
# Read frozen state while graph is paused
state_snapshot = graph.get_state(config)
# state_snapshot.tasks contains pending interrupt info
```

**Internal mechanism:**
`NodeInterrupt` exception is raised by `interrupt()` internally, caught by
the Pregel engine, which writes a checkpoint and surfaces the value to the
caller. Do NOT catch `NodeInterrupt` in user code.

### 3.11 Functional API (alternative to StateGraph)

| Decorator | Purpose |
|-----------|---------|
| `@entrypoint` | Define workflow entry point (replaces StateGraph) |
| `@task` | Define individual work unit (replaces add_node) |
| `entrypoint.final` | Return value while saving different checkpoint |
| `previous` | Access return value of prior invocation (same thread) |

Task config: `@task(name=, retry_policy=, cache_policy=)`.

### 3.12 Prebuilt Components

#### create_react_agent -- Full Parameter Reference

```python
from langgraph.prebuilt import create_react_agent

graph = create_react_agent(
    model,                       # BaseChatModel -- the LLM backbone
    tools,                       # list[BaseTool | Callable]
    prompt=None,                 # str | SystemMessage | Callable | Runnable
    response_format=None,        # type[BaseModel] -- structured final output
    pre_model_hook=None,         # node fn inserted BEFORE model call
    post_model_hook=None,        # node fn inserted AFTER model call
    state_schema=MessagesState,  # TypedDict -- default uses messages reducer
    context_schema=None,         # TypedDict for read-only runtime context
    checkpointer=None,           # BaseCheckpointSaver -- enables memory/HIL
    store=None,                  # BaseStore -- cross-thread long-term memory
)
```

| Parameter | Type | Purpose |
|-----------|------|---------|
| `model` | BaseChatModel | The LLM backbone |
| `tools` | list | Tools the agent can call |
| `prompt` | str / SystemMessage / Callable / Runnable | Prepended context; string auto-converts to SystemMessage |
| `response_format` | Pydantic type | Force structured final response via `with_structured_output` |
| `pre_model_hook` | node function | Before model call -- use for message trimming, token budget |
| `post_model_hook` | node function | After model call -- use for HITL approval before tool execution |
| `state_schema` | TypedDict | Extend MessagesState with custom fields |
| `context_schema` | TypedDict | Read-only context injected via `config["context"]` |
| `checkpointer` | BaseCheckpointSaver | Required for multi-turn memory and interrupt/resume |
| `store` | BaseStore | Long-term memory across threads |

#### ToolNode -- Full Parameter Reference

```python
from langgraph.prebuilt import ToolNode

tool_node = ToolNode(
    tools,                    # list[BaseTool]
    name="tools",             # node name registered in graph
    tags=None,                # LangSmith tags attached to tool runs
    handle_tool_errors=True,  # True: catch errors -> ToolMessage(is_error=True)
                              # str: use as error message template
                              # Callable: custom error handler fn
    messages_key="messages",  # state key where messages list lives
)
```

**ToolNode behavior:**
- Reads last AIMessage from `state[messages_key]`
- Extracts all `tool_calls` from that AIMessage
- Executes all tool calls IN PARALLEL (asyncio.gather under async)
- Returns list of ToolMessages, one per tool call
- With `handle_tool_errors=True`: exceptions become ToolMessage with `is_error=True`

#### Tool Injection Annotations

| Annotation | Source | Purpose |
|-----------|--------|---------|
| `InjectedToolArg` | langchain_core | Hidden from LLM schema -- injected by runtime (e.g., user_id) |
| `InjectedToolCallId` | langchain_core | Auto-injects current `tool_call_id` into tool |
| `InjectedState` | langgraph.prebuilt | Inject full graph state into tool args at call time |
| `InjectedStore` | langgraph.prebuilt | Inject BaseStore instance into tool for memory ops |

#### Other Prebuilt Components

| Component | Purpose |
|-----------|---------|
| `MessagesState` | TypedDict: `{messages: Annotated[list[AnyMessage], add_messages]}` |
| `CachePolicy(key_func=, ttl=)` | Cache node outputs; key_func maps state to cache key |
| `ValidationNode(tools)` | Validate tool call schemas before execution; raises ToolException on invalid |
| `tools_condition(state)` | Router function: if last AIMessage has tool_calls -> "tools" else -> END |

#### Human-in-the-Loop Prebuilt Types (LangGraph Studio)

| Type | Purpose |
|------|---------|
| `HumanInterruptConfig` | Configure what triggers human review in Studio |
| `ActionRequest` | Proposed action surfaced to human reviewer |
| `HumanInterrupt` | Event type emitted when graph hits HITL gate |
| `InterruptDecision` | Human decision: accept / reject / edit / respond |

### 3.13 Advanced Patterns

| Pattern | Description |
|---------|-------------|
| Subgraph | Nested graph as a node -- separate state, checkpoint namespace |
| Map-reduce | `Send` to fan-out, reducer to merge results |
| Multi-agent handoff | Nodes return `Command(goto="other_agent")` |
| Branching | Conditional edges for dynamic routing |
| Cycles | Edges that loop back (agent loops, retry loops) |

---

## 4. LangSmith Tracing & Observability Vocabulary

### 4.1 Core Observability Concepts

| Term | Definition |
|------|------------|
| **Trace** | Collection of runs for a single operation (= OpenTelemetry trace) |
| **Run** | Single span of work within a trace (= OpenTelemetry span) |
| **Project** | Collection of traces (organizational container) |
| **Thread** | Sequence of traces for one conversation (grouped by session_id) |
| **Dataset** | Persistent storage of inputs/outputs for evaluation |

### 4.2 Run Types

| Run type | When |
|----------|------|
| `llm` | LLM/chat model invocation |
| `chain` | Chain/runnable execution |
| `tool` | Tool execution |
| `retriever` | Document retrieval |
| `embedding` | Embedding computation |
| `prompt` | Prompt formatting |
| `parser` | Output parsing |

### 4.3 Run Properties

| Property | Type | Purpose |
|----------|------|---------|
| `run_id` | UUID | Unique run identifier |
| `trace_id` | UUID | Parent trace identifier |
| `parent_run_id` | UUID | Parent run in hierarchy |
| `name` | string | Run name (function/class name) |
| `run_type` | enum | One of the run types above |
| `inputs` | dict | Input data |
| `outputs` | dict | Output data |
| `error` | string | Error message if failed |
| `start_time` | datetime | Execution start |
| `end_time` | datetime | Execution end |
| `latency` | float | Duration in seconds |
| `token_usage` | dict | `{prompt_tokens, completion_tokens, total_tokens}` |
| `tags` | list[str] | Categorical labels |
| `metadata` | dict | Arbitrary key-value context |

### 4.4 Feedback & Evaluation

| Term | Definition |
|------|------------|
| **Feedback** | Score + comment attached to a run |
| **Annotation** | Human-provided feedback (via annotation queue) |
| **Online evaluator** | Real-time LLM-as-judge assessment |
| **Offline evaluation** | Batch evaluation against dataset |
| **Annotation queue** | UI workflow for human review |
| **Feedback score** | Numeric value (e.g., 0-1, 1-5) |
| **Feedback key** | Category name (e.g., "correctness", "helpfulness") |

### 4.5 Tracing Integration

| Mechanism | Purpose |
|-----------|---------|
| `LangChainTracer` | Auto-trace LangChain runs to LangSmith |
| `@traceable` | Decorator to trace arbitrary Python functions |
| `RunTree` | Manual trace tree construction |
| `LANGSMITH_API_KEY` | Auth env var |
| `LANGSMITH_PROJECT` | Target project env var |
| `LANGSMITH_TRACING` | Enable/disable tracing env var |

### 4.6 Data Retention

- Max 25,000 runs per trace
- 400-day retention for SaaS traces
- Datasets persist independently of trace retention

---

## 5. Mapping to CEX Pillars

| LangChain/LangGraph Concept | CEX Pillar | CEX Kind | Notes |
|------------------------------|------------|----------|-------|
| **Runnable** (base interface) | P03 Prompt | `chain` | LCEL chain = CEX chain |
| **RunnableSequence** (`\|`) | P03 Prompt | `chain` | Serial composition |
| **RunnableParallel** | P12 Orchestration | `workflow` | Fan-out pattern |
| **RunnableBranch** | P12 Orchestration | `dispatch_rule` | Conditional routing |
| **RunnableWithFallbacks** | P02 Model | `fallback_chain` | Provider failover |
| **ChatPromptTemplate** | P03 Prompt | `prompt_template` | Direct equivalent |
| **MessagesPlaceholder** | P03 Prompt | `prompt_template` | Variable injection |
| **FewShotPromptTemplate** | P03 Prompt | `prompt_template` | Example injection |
| **BaseChatModel** | P02 Model | `model_provider` | LLM abstraction |
| **BaseTool / @tool** | P04 Tools | `cli_tool` / `mcp_server` | Tool definition |
| **ToolNode** | P04 Tools | `cli_tool` | Tool execution node |
| **BaseRetriever** | P01 Knowledge | `retriever_config` | RAG retrieval |
| **VectorStore** | P01 Knowledge | `embedding_config` | Vector backend |
| **Document** | P01 Knowledge | `knowledge_card` | Content container |
| **BaseOutputParser** | P05 Output | `parser` | Output extraction |
| **StrOutputParser** | P05 Output | `parser` | String output |
| **JsonOutputParser** | P05 Output | `parser` | JSON output |
| **StateGraph** | P12 Orchestration | `workflow` | Graph-based workflow |
| **CompiledGraph** | P12 Orchestration | `workflow` | Executable workflow |
| **Node** | P12 Orchestration | `workflow` | Workflow step |
| **Edge / ConditionalEdge** | P12 Orchestration | `dispatch_rule` | Transition rule |
| **Command** | P12 Orchestration | `dispatch_rule` | State + routing |
| **Send** | P12 Orchestration | `dispatch_rule` | Dynamic fan-out |
| **MessagesState** | P10 Memory | `memory_scope` | Conversation state |
| **Checkpointer** | P10 Memory | `entity_memory` | Persistence layer |
| **MemorySaver** | P10 Memory | `memory_scope` | In-memory persistence |
| **Store** | P10 Memory | `entity_memory` | Cross-thread memory |
| **interrupt** | P12 Orchestration | `workflow` | Human-in-the-loop gate |
| **BaseCallbackHandler** | P07 Evaluation | `trace_config` | Observability hook |
| **LangChainTracer** | P07 Evaluation | `trace_config` | Tracing integration |
| **Feedback** | P11 Feedback | `scoring_rubric` | Quality signal |
| **Dataset** | P07 Evaluation | `benchmark` | Test data collection |
| **Online evaluator** | P07 Evaluation | `llm_judge` | LLM-as-judge |
| **Annotation queue** | P11 Feedback | `quality_gate` | Human review workflow |
| **AgentExecutor** (legacy) | P12 Orchestration | `workflow` | Deprecated agent loop |
| **create_react_agent** | P02 Model | `agent` | Prebuilt agent graph |
| **@entrypoint** | P12 Orchestration | `workflow` | Functional API entry |
| **@task** | P12 Orchestration | `workflow` | Functional API step |
| **RunnableConfig** | P09 Config | `env_config` | Runtime configuration |
| **BaseCache** | P10 Memory | `prompt_cache` | LLM response cache |
| **BaseRateLimiter** | P09 Config | `rate_limit_config` | Rate limiting |
| **ExampleSelector** | P03 Prompt | `prompt_template` | Few-shot selection |
| **BaseDocumentTransformer** | P01 Knowledge | `chunk_strategy` | Document processing |
| **RecordManager** | P10 Memory | `knowledge_index` | Dedup/indexing |
| **BaseChatMessageHistory** | P10 Memory | `memory_scope` | Conversation history |

---

## 6. Key Architectural Patterns

### 6.1 LCEL vs LangGraph Decision Matrix

| Use case | Use LCEL | Use LangGraph |
|----------|----------|---------------|
| Linear chain (prompt -> model -> parser) | yes | overkill |
| Conditional branching | RunnableBranch | StateGraph + conditional edges |
| Cycles / loops | not possible | yes (edges can loop) |
| Human-in-the-loop | not supported | interrupt/resume |
| Multi-agent | not native | Command + multi-node |
| Persistence across turns | RunnableWithMessageHistory | Checkpointer (built-in) |
| Parallel tool execution | RunnableParallel | ToolNode (auto-parallel) |
| Complex state management | dict passing | TypedDict + reducers |

### 6.2 LangGraph Execution Model (Pregel)

```
User input
  |
  v
START --> [node_a] --> [conditional_edge] --> [node_b] --> END
                            |                     ^
                            +---> [node_c] -------+
                                     |
                                     v (cycle)
                                  [node_a]
```

Each iteration over nodes = one **super-step**. The `recursion_limit` caps total
super-steps. Nodes communicate only through the shared **State** object -- there is
no direct node-to-node messaging.

### 6.3 LangSmith Integration Points

```
Application code
  |
  +-- @traceable / LangChainTracer
  |       |
  |       v
  |   LangSmith API
  |       |
  |       +-- Project (trace container)
  |       |     +-- Trace (one operation)
  |       |           +-- Run (one span)
  |       |                 +-- inputs, outputs, latency, tokens
  |       |                 +-- Feedback (score + comment)
  |       |
  |       +-- Dataset (evaluation data)
  |       +-- Annotation Queue (human review)
  |       +-- Online Evaluator (real-time LLM judge)
  |
  +-- Evaluation harness
        +-- Offline evaluators (batch scoring against dataset)
```

---

## 7. Glossary (Quick Reference)

| Term | Definition |
|------|------------|
| LCEL | LangChain Expression Language -- composition via pipe operator |
| Runnable | Base protocol: invoke/batch/stream + composable |
| StateGraph | Graph where nodes share typed state with reducers |
| CompiledGraph | Immutable executable graph after `.compile()` |
| Node | Named function that reads/writes state |
| Edge | Directed transition between nodes |
| Conditional edge | Edge resolved by a routing function |
| Command | Combined state update + goto navigation |
| Send | Dynamic fan-out with per-target state |
| Reducer | Merge function for concurrent state writes |
| Checkpointer | Persistence backend for graph state |
| Thread | Conversation identified by thread_id |
| Interrupt | Pause graph for human input |
| Super-step | One pass over all active nodes |
| Pregel | Google's graph computation model (LangGraph inspiration) |
| Trace | Collection of runs for one operation |
| Run | Single span of work (LangSmith) |
| Feedback | Quality score attached to a run |
| ToolNode | Prebuilt node that executes tool calls |
| MessagesState | Prebuilt state: messages list with add_messages reducer |
| @entrypoint | Functional API: workflow entry decorator |
| @task | Functional API: work unit decorator |
| @traceable | LangSmith: trace arbitrary function |
| @tool | LangChain: create tool from function |
