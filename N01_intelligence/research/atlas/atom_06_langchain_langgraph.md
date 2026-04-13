---
id: atom_06_langchain_langgraph
kind: knowledge_card
pillar: P01
domain: agentic-frameworks
title: "LangChain LCEL + LangGraph + LangSmith -- Complete Vocabulary Atlas"
version: 2.1.0
quality: 8.8
tags: [langchain, langgraph, langsmith, lcel, runnable, stategraph, observability, agent-framework, langgraph-platform, pregel, hitl, datasets, store-api, sdk-reference, task-parallelism, experiments]
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

### 3.8.2 Task-Level Parallelism Inside a Super-Step

When multiple nodes are activated within the **same super-step** (via `Send` fan-out
or parallel conditional edges), LangGraph executes them as concurrent tasks.

**Concurrency mechanism:**

| Invocation mode | Parallelism |
|----------------|-------------|
| `graph.invoke(...)` (sync) | `ThreadPoolExecutor` via `ContextThreadPoolExecutor` |
| `graph.ainvoke(...)` (async) | `asyncio.gather` -- true coroutine parallelism |

**Fan-out + reduce pattern:**

```python
# Map phase: Send creates N tasks in ONE super-step
def dispatch_node(state):
    return [Send("worker", {"item": x}) for x in state["items"]]

# Each worker runs concurrently -- isolated state copies
def worker_node(state):
    return {"results": [process(state["item"])]}

# Reduce phase: reducer merges N results in NEXT super-step
# Requires Annotated reducer on the aggregation key:
# results: Annotated[list, operator.add]
```

**Isolation guarantee:**
- Each `Send` task receives its own state copy
- Updates from concurrent tasks are COLLECTED then merged atomically
- A task exception does NOT abort sibling tasks in async mode
- `recursion_limit` counts super-steps, NOT individual tasks -- 100 Send tasks = 1 step

**Scheduler internals (Pregel.stream):**

| Phase | What happens |
|-------|-------------|
| 1. Preprocess | Resolve active nodes from pending channel writes |
| 2. Collect tasks | Build Task objects for all active nodes this step |
| 3. Execute | Run tasks via ThreadPool (sync) or gather (async) |
| 4. Apply writes | Apply all updates atomically via reducers |
| 5. Checkpoint | Write state snapshot to checkpointer |
| 6. Yield | Surface values/updates/messages to caller |
| 7. Loop | Back to step 1 with new active-node set |

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
| NodeInterrupt | Internal exception raised by interrupt() -- do not catch in user code |
| BSP | Bulk Synchronous Parallel -- the Pregel execution model |
| Assistant | LangGraph Platform: named versioned config of a graph |
| Thread (Platform) | LangGraph Platform: conversation container across runs |
| Run (Platform) | LangGraph Platform: single graph invocation |
| Cron | LangGraph Platform: scheduled periodic run |
| Store | LangGraph Platform: cross-thread long-term memory (key-value namespace) |
| DataType.kv | LangSmith dataset type: arbitrary key-value (most common) |
| evaluate() | LangSmith: sync evaluation function against a dataset |
| aevaluate() | LangSmith: async evaluation function (preferred for large datasets) |

---

## 8. LangGraph Platform (Cloud Deployment)

LangGraph Platform (GA: 2025) is the production infrastructure layer for deploying
stateful, long-running agents. Built on top of the Agent Server, it provides
REST API, persistence, scheduling, and streaming capabilities.
Source: https://blog.langchain.dev/langgraph-platform-ga/

### 8.1 Deployment Tiers

| Tier | Who manages infra | Where data runs | Cost |
|------|------------------|-----------------|------|
| **Self-Hosted Lite** | You | Your infra | Free (up to 1M nodes executed) |
| **Self-Hosted Enterprise** | You | Your infra | Enterprise license |
| **BYOC (Bring Your Own Cloud)** | LangChain managed | Your cloud account | Enterprise |
| **Cloud SaaS** | LangChain fully managed | LangChain cloud | Plus/Enterprise plan |

### 8.2 Agent Server Architecture

```
                    CONTROL PLANE (LangSmith)
                    +---------------------------+
                    | - Deployment management   |
                    | - Auth (X-Api-Key header) |
                    | - Studio UI               |
                    +---------------------------+
                              |
                    DATA PLANE (Agent Server)
                    +---------------------------+
                    | LangGraph Server          |
                    |  - REST API (/docs)       |
                    |  - Task queue workers     |
                    |                           |
                    | PostgreSQL (persistent)   |
                    |  - Assistants             |
                    |  - Threads                |
                    |  - Runs                   |
                    |  - Store (long-term mem)  |
                    |                           |
                    | Redis (ephemeral)         |
                    |  - Queue coordination     |
                    |  - Worker communication   |
                    +---------------------------+
```

### 8.3 REST API Resource Groups

| Resource | Endpoint prefix | Definition |
|----------|----------------|------------|
| **Assistants** | `/assistants` | Named, versioned config of a graph (graph_id + config + metadata) |
| **Threads** | `/threads` | Conversation container -- accumulates state across runs |
| **Thread Runs** | `/threads/{id}/runs` | Invoke a graph on a thread (stateful) |
| **Stateless Runs** | `/runs` | Invoke graph with no state persistence |
| **Crons** | `/crons` | Schedule periodic runs with cron expression |
| **Store** | `/store` | Long-term memory namespace operations (cross-thread KV) |
| **Meta** | `/info`, `/ok` | Server health + version metadata |

### 8.4 Run Execution Modes

| Mode | API call | Behavior |
|------|----------|---------|
| **Synchronous** | `POST /runs/wait` | Blocks until complete, returns final state |
| **Streaming** | `POST /runs/stream` | Server-Sent Events (SSE) with intermediate values |
| **Background** | `POST /runs` | Returns run_id immediately; poll for status |
| **Cron** | `POST /crons` | Scheduled background run on cron expression |

### 8.5 Streaming Event Types (SSE)

| Stream mode | Content |
|-------------|---------|
| `values` | Full state snapshot after each super-step |
| `updates` | Incremental state updates from each node |
| `messages` | Token-level streaming from model nodes |
| `events` | LangChain callback events (on_llm_start, on_chain_end, etc.) |
| `debug` | Internal debug events |
| `custom` | Custom events via `stream_writer` in node |

### 8.6 LangGraph CLI

```bash
langgraph dev          # Local dev server with hot reload
langgraph build        # Build Docker image for deployment
langgraph deploy       # Deploy to LangSmith Cloud SaaS
langgraph up           # Start via Docker Compose (self-hosted)
langgraph dockerfile   # Generate Dockerfile for custom builds
```

### 8.7 Python SDK (langgraph-sdk)

```python
from langgraph_sdk import get_client

client = get_client(
    url="http://localhost:2024",   # local dev or deployed URL
    api_key="lsv2_..."             # LangSmith API key (X-Api-Key header)
)

# Create a thread + stream a run
thread = await client.threads.create()
async for chunk in client.runs.stream(
    thread["thread_id"],
    assistant_id="my-agent",
    input={"messages": [{"role": "user", "content": "Hello"}]},
    stream_mode="values",
):
    print(chunk.data)
```

### 8.8 CEX Pillar Mapping (LangGraph Platform)

| Platform Concept | CEX Kind | Pillar |
|-----------------|----------|--------|
| Assistant | `agent_card` | P08 |
| Thread | `session_state` | P10 |
| Run (background) | `spawn_config` | P12 |
| Cron job | `schedule` | P12 |
| Store namespace | `entity_memory` | P10 |
| Streaming (SSE) | `streaming_config` | P09 |

### 8.9 Python SDK Full Method Reference (langgraph-sdk)

Complete method table for `LangGraphClient` (async) / `SyncLangGraphClient`.

#### Threads namespace

| Method | Signature | Returns |
|--------|-----------|---------|
| `create` | `(metadata=None, config=None, if_exists="raise")` | Thread |
| `get` | `(thread_id)` | Thread |
| `update` | `(thread_id, metadata=None)` | Thread |
| `delete` | `(thread_id)` | None |
| `search` | `(metadata=None, status=None, limit=10, offset=0)` | list[Thread] |
| `copy` | `(thread_id)` | Thread |
| `get_state` | `(thread_id, checkpoint_id=None, subgraphs=False)` | ThreadState |
| `update_state` | `(thread_id, values, as_node=None, checkpoint_id=None)` | dict |
| `get_history` | `(thread_id, limit=10, before=None, metadata=None)` | Iterator[ThreadState] |
| `patch_state` | `(thread_id, metadata)` | dict |

#### Runs namespace

| Method | Signature | Returns |
|--------|-----------|---------|
| `create` | `(thread_id, assistant_id, *, input, config, metadata, stream_mode, interrupt_before, interrupt_after, multitask_strategy)` | Run |
| `stream` | `(thread_id, assistant_id, *, input, stream_mode, config, ...)` | AsyncIterator[StreamPart] |
| `wait` | `(thread_id, assistant_id, *, input, config, ...)` | dict |
| `get` | `(thread_id, run_id)` | Run |
| `list` | `(thread_id, *, limit=10, offset=0)` | list[Run] |
| `cancel` | `(thread_id, run_id, *, wait=False, action="interrupt")` | None |
| `join` | `(thread_id, run_id)` | dict |
| `join_stream` | `(thread_id, run_id)` | AsyncIterator[StreamPart] |
| `delete` | `(thread_id, run_id)` | None |

**Multitask strategies (when thread has a run in progress):**

| Strategy | Behavior |
|----------|---------|
| `"reject"` | Raise error (default) |
| `"enqueue"` | Queue behind current run |
| `"interrupt"` | Cancel current, start new |
| `"rollback"` | Cancel current, restore prior state, start new |

#### Assistants namespace

| Method | Signature | Returns |
|--------|-----------|---------|
| `create` | `(graph_id, config=None, metadata=None, name=None)` | Assistant |
| `get` | `(assistant_id)` | Assistant |
| `update` | `(assistant_id, config=None, metadata=None, name=None)` | Assistant |
| `delete` | `(assistant_id)` | None |
| `search` | `(metadata=None, graph_id=None, limit=10, offset=0)` | list[Assistant] |
| `get_schemas` | `(assistant_id)` | dict (input/output/config schemas) |
| `get_subgraphs` | `(assistant_id, namespace=None, recurse=False)` | dict[str, SubgraphSchemas] |
| `create_version` | `(assistant_id, config=None, metadata=None)` | Assistant |
| `get_versions` | `(assistant_id, metadata=None, limit=10, offset=0)` | list[AssistantVersion] |
| `set_latest` | `(assistant_id, version)` | Assistant |

#### Crons namespace

| Method | Signature | Returns |
|--------|-----------|---------|
| `create` | `(assistant_id, schedule, payload=None, metadata=None)` | Cron |
| `create_for_thread` | `(thread_id, assistant_id, schedule, payload=None)` | Cron |
| `delete` | `(cron_id)` | None |
| `search` | `(thread_id=None, assistant_id=None, limit=10, offset=0)` | list[Cron] |

Schedule format: standard cron string, e.g., `"0 9 * * 1"` = every Monday at 09:00 UTC.

#### Store namespace (SDK)

| Method | Signature | Returns |
|--------|-----------|---------|
| `put_item` | `(namespace: tuple[str, ...], key: str, value: dict)` | None |
| `get_item` | `(namespace: tuple[str, ...], key: str)` | Item |
| `delete_item` | `(namespace: tuple[str, ...], key: str)` | None |
| `search_items` | `(namespace_prefix: tuple, query: str=None, limit: int=10, offset: int=0)` | list[Item] |
| `list_namespaces` | `(prefix: tuple=None, suffix: tuple=None, max_depth: int=None, limit: int=10)` | list[tuple] |

**Item schema:**

| Field | Type | Description |
|-------|------|-------------|
| `namespace` | tuple[str, ...] | Hierarchical path, e.g., `("users", "u123", "preferences")` |
| `key` | str | Identifier within namespace |
| `value` | dict | Arbitrary JSON payload |
| `created_at` | datetime | Creation timestamp |
| `updated_at` | datetime | Last-write timestamp |

#### StreamPart schema

```python
class StreamPart:
    event: str    # "values" | "updates" | "messages" | "error" | "end" | custom
    data: Any     # shape depends on stream_mode; "end" has data=None
```

---

## 9. LangSmith Dataset Management API (Deep Dive)

### 9.1 Client Initialization

```python
from langsmith import Client
import os

client = Client(
    api_url="https://api.smith.langchain.com",  # default SaaS endpoint
    api_key=os.environ["LANGSMITH_API_KEY"],
)
```

### 9.2 Dataset Operations

| Method | Parameters | Returns |
|--------|-----------|---------|
| `create_dataset` | `name, description="", data_type=DataType.kv` | Dataset |
| `read_dataset` | `dataset_id=None, dataset_name=None` | Dataset |
| `list_datasets` | `dataset_name=None, data_type=None, metadata=None` | Iterator[Dataset] |
| `delete_dataset` | `dataset_id` | None |
| `clone_public_dataset` | `token_or_url, source_api_url=None` | Dataset |

**Dataset data types (DataType enum):**

| Value | Use case |
|-------|----------|
| `DataType.kv` | Arbitrary key-value inputs/outputs (most common) |
| `DataType.llm` | LLM completion pairs (prompt_text -> completion_text) |
| `DataType.chat` | Chat message pairs (messages list -> generation) |

### 9.3 Example (Row) Operations

| Method | Parameters | Returns |
|--------|-----------|---------|
| `create_example` | `inputs, outputs=None, dataset_id, metadata=None` | Example |
| `create_examples` | `inputs, outputs=None, dataset_id, metadata=None` | CreateExamplesResponse |
| `list_examples` | `dataset_id=None, as_of=None, splits=None, metadata=None` | Iterator[Example] |
| `read_example` | `example_id` | Example |
| `update_example` | `example_id, inputs=None, outputs=None, metadata=None` | Example |
| `delete_examples` | `example_ids: list[UUID]` | None |

**Batch creation (preferred for large datasets):**

```python
# Single request for multiple rows
client.create_examples(
    inputs=[{"question": q} for q in questions],
    outputs=[{"answer": a} for a in answers],
    dataset_id=dataset.id,
    metadata=[{"source": "v1"} for _ in questions],
)
```

### 9.4 Evaluation API

| Function | Import | Purpose |
|----------|--------|---------|
| `evaluate` | `from langsmith import evaluate` | Sync evaluation on dataset |
| `aevaluate` | `from langsmith import aevaluate` | Async evaluation (preferred for large sets) |
| `client.evaluate` | SDK v1.x+ preferred method | Same as above via Client |

**evaluate() parameters:**

```python
from langsmith import evaluate

results = evaluate(
    target,                       # Callable or LangChain Runnable
    data,                         # Dataset name/ID or list[Example]
    evaluators=[correctness_fn],  # list[Callable] -- per-example scorers
    summary_evaluators=[agg_fn],  # list[Callable] -- aggregate scorers
    metadata={"model": "gpt-4o"}, # Stored with experiment
    experiment_prefix="my-run-v1",
    max_concurrency=4,            # Parallel example evaluation
    num_repetitions=1,            # Run each example N times
    blocking=True,                # Wait for all results
)
```

**Evaluator function signature:**

```python
from langsmith.schemas import Run, Example
from langsmith.evaluation import EvaluationResult

def correctness_evaluator(run: Run, example: Example) -> EvaluationResult:
    score = 1.0 if run.outputs["answer"] == example.outputs["answer"] else 0.0
    return EvaluationResult(key="correctness", score=score)
```

### 9.5 Dataset Versioning

| Feature | API |
|---------|-----|
| Tag a version | `client.create_tag(dataset_id, name="v1.0")` |
| Pin eval to version | `data="my-dataset:v1.0"` in `evaluate()` |
| List examples at version | `client.list_examples(dataset_id, as_of="v1.0")` |

### 9.6 CEX Pillar Mapping (LangSmith Datasets)

| LangSmith Concept | CEX Kind | Pillar |
|-------------------|----------|--------|
| Dataset | `benchmark` | P07 |
| Example (row) | `eval_dataset` entry | P07 |
| Evaluator function | `llm_judge` or `scoring_rubric` | P07 |
| Annotation queue | `quality_gate` | P11 |
| Experiment result | `benchmark` (output) | P07 |
| Summary evaluator | `scoring_rubric` (aggregate) | P07 |

---

## 10. Comparative Context (vs. Alternatives)

| Dimension | LangGraph | CrewAI | AutoGen | Semantic Kernel |
|-----------|-----------|--------|---------|-----------------|
| Graph model | Pregel BSP (super-steps) | Role-based crews | Conversation protocol | Plugin + planner |
| State management | TypedDict + reducers | Agent memory dicts | ConversableAgent vars | SKContext |
| HITL | interrupt() / resume | Manual callback | Human proxy agent | Plan interrupts |
| Persistence | Checkpointer (Postgres/SQLite) | Memory backends | Memory DB | SK memory store |
| Cloud deployment | LangGraph Platform (GA 2025) | Self-managed | AutoGen Studio | Azure AI Foundry |
| Observability | LangSmith (native) | LangSmith / custom | OTel compatible | Azure AppInsights |
| Multi-agent | Command + Send primitives | Hierarchical crews | GroupChat | Orchestrator pattern |
| Evaluation | LangSmith datasets + evaluate() | Custom | Custom | Promptflow |
| Long-term memory | InMemoryStore / PostgresStore | Custom dict | Memory DB | SK memory |
| Task parallelism | asyncio.gather + Send fan-out | CrewAI parallel tasks | Async GroupChat | SK parallel steps |

---

## 11. LangGraph Store API -- Cross-Thread Long-Term Memory

`BaseStore` / `InMemoryStore` provides persistent key-value memory that survives
across threads and graph invocations. Distinct from `Checkpointer` (which stores
checkpoint-scoped state per thread).

### 11.1 In-Graph Store Access

```python
from langgraph.store.memory import InMemoryStore
from langgraph.store.postgres import PostgresStore  # production

# Pass store at compile time
store = InMemoryStore()
graph = graph_builder.compile(store=store)

# Access inside a node via config or InjectedStore annotation
def memory_node(state, config):
    store = config.get("store")  # BaseStore instance
    items = store.search(("users", state["user_id"]), query="preferences")
    return {"context": [i.value for i in items]}

# Or via InjectedStore annotation (preferred):
from langgraph.prebuilt import InjectedStore
from langchain_core.tools import tool

@tool
def save_memory(content: str, store: Annotated[BaseStore, InjectedStore()]) -> str:
    store.put(("memories", "shared"), content[:20], {"text": content})
    return "saved"
```

### 11.2 BaseStore Interface

| Method | Signature | Returns |
|--------|-----------|---------|
| `put` | `(namespace: tuple[str, ...], key: str, value: dict, index: list[str]=None)` | None |
| `get` | `(namespace: tuple[str, ...], key: str)` | Item or None |
| `delete` | `(namespace: tuple[str, ...], key: str)` | None |
| `search` | `(namespace_prefix: tuple[str, ...], *, query: str=None, limit: int=10, offset: int=0, filter: dict=None)` | list[Item] |
| `list_namespaces` | `(*, prefix: tuple=None, suffix: tuple=None, max_depth: int=None, limit: int=100)` | list[tuple[str, ...]] |
| `aput` | async variant of `put` | None |
| `aget` | async variant of `get` | Item or None |
| `adelete` | async variant of `delete` | None |
| `asearch` | async variant of `search` | list[Item] |
| `alist_namespaces` | async variant of `list_namespaces` | list[tuple] |
| `batch` | `(ops: Iterable[Op])` | list[Result] -- atomic batch ops |
| `abatch` | async variant of `batch` | list[Result] |

### 11.3 Namespace Design Patterns

Namespaces are tuples. Convention: `(domain, entity_id, category)`.

| Pattern | Namespace | Purpose |
|---------|-----------|---------|
| User preferences | `("users", user_id, "prefs")` | Per-user settings |
| Shared facts | `("facts", "global")` | System-wide knowledge |
| Agent working memory | `("agents", agent_id, "scratchpad")` | Per-agent temp state |
| Conversation summaries | `("threads", thread_id, "summary")` | Compressed history |
| Org-scoped memory | `("org", org_id, "policies")` | Multi-tenant isolation |

**Semantic search:** When `PostgresStore` with `pgvector` is used, `query=` performs
approximate nearest-neighbor search over embedded `value` fields specified in `index`.

### 11.4 Backends

| Backend | Class | Production ready | Semantic search |
|---------|-------|-----------------|-----------------|
| In-memory | `InMemoryStore` | Dev/test only | No |
| PostgreSQL | `PostgresStore` | Yes | Yes (pgvector) |
| Redis | `RedisStore` (community) | Yes | With RediSearch |
| Custom | Implement `BaseStore` | User-managed | User-managed |

### 11.5 CEX Pillar Mapping (Store)

| Store Concept | CEX Kind | Pillar |
|--------------|----------|--------|
| `BaseStore` | `entity_memory` | P10 |
| Namespace | `memory_scope` | P10 |
| `put` / `get` / `search` | `retriever_config` | P01 |
| PostgresStore + pgvector | `embedding_config` | P01 |
| `batch` ops | `workflow` (atomic ops) | P12 |

---

## 12. LangSmith Experiments API

Experiments are named evaluation runs against a dataset.
Source: https://docs.smith.langchain.com/evaluation/how_to_guides/run_experiments_programmatically

### 12.1 Experiment Concepts

| Term | Definition |
|------|------------|
| **Experiment** | One `evaluate()` call -- a batch of target fn runs against a dataset |
| **Experiment prefix** | Human-readable name prefix (e.g., `"gpt-4o-v2"`) |
| **ExperimentResults** | Object returned by `evaluate()` -- iterable of `ExperimentResultRow` |
| **ExperimentResultRow** | Single example result: `run`, `example`, `evaluation_results` |
| **ComparativeExperiment** | Side-by-side comparison of 2+ experiments on same dataset |

### 12.2 Running Experiments

```python
from langsmith import evaluate, aevaluate

# Sync -- blocks until complete
results = evaluate(
    target_fn,                        # Callable or Runnable
    data="my-dataset",                # Dataset name, ID, or list[Example]
    evaluators=[correctness_fn],      # Per-example scorers
    summary_evaluators=[aggregate_fn],# Whole-experiment scorers
    experiment_prefix="my-run",       # Appears in UI as "my-run-<timestamp>"
    metadata={"model": "gpt-4o"},     # Stored with every run
    max_concurrency=4,                # Parallel example evaluation
    num_repetitions=1,                # Run each example N times
    blocking=True,                    # False = fire-and-forget
    load_nested=False,                # Include nested runs in results
)

# Async -- preferred for large datasets
results = await aevaluate(target_fn, data="my-dataset", evaluators=[fn])
```

### 12.3 Summary Evaluator Pattern

```python
from langsmith.schemas import Example, Run
from langsmith.evaluation import EvaluationResult, EvaluationResults

def agg_score(runs: list[Run], examples: list[Example]) -> EvaluationResults:
    avg = sum(r.feedback_stats["correctness"]["avg"] for r in runs) / len(runs)
    return EvaluationResults(results=[EvaluationResult(key="avg_correctness", score=avg)])
```

### 12.4 Comparative Experiments

```python
from langsmith import evaluate

# Run two experiments then compare
exp1 = evaluate(fn_v1, data="my-dataset", experiment_prefix="v1")
exp2 = evaluate(fn_v2, data="my-dataset", experiment_prefix="v2")

# Compare in UI: annotate both with same dataset to enable side-by-side view
# Programmatic comparison:
from langsmith import Client
client = Client()
results = client.get_pairwise_evaluations(
    [exp1.experiment_name, exp2.experiment_name]
)
```

### 12.5 Online Evaluation (real-time LLM judge)

```python
# Configure online evaluator on LangSmith project (SDK or UI)
client.create_evaluator(
    project_name="my-project",
    criteria="Is the response helpful? Reply YES or NO.",
    evaluator_type="LangChainStringEvaluator",
    name="helpfulness",
    feedback_key="helpfulness",
)
# Fires after every traced run -- no code changes needed in application
```

### 12.6 CEX Mapping (Experiments)

| LangSmith Concept | CEX Kind | Pillar |
|------------------|----------|--------|
| Experiment | `benchmark` | P07 |
| Per-example evaluator | `llm_judge` or `scoring_rubric` | P07 |
| Summary evaluator | `scoring_rubric` (aggregate) | P07 |
| ComparativeExperiment | `benchmark` (multi-variant) | P07 |
| Online evaluator | `llm_judge` (streaming) | P07 |
| ExperimentResultRow | `eval_dataset` row | P07 |
