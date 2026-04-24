---
id: atom_03_openai_agents_sdk
kind: knowledge_card
8f: F3_inject
pillar: P01
domain: multi-agent orchestration
title: "OpenAI Agents SDK -- Deep Vocabulary Atlas"
version: 2.0.0
quality: 8.8
tags: [openai, agents-sdk, multi-agent, orchestration, swarm, a2a, vocabulary, voice, changelog, temporal]
sources:
  - https://openai.github.io/openai-agents-python/
  - https://github.com/openai/openai-agents-python
  - https://openai.github.io/openai-agents-python/agents/
  - https://openai.github.io/openai-agents-python/running_agents/
  - https://openai.github.io/openai-agents-python/tools/
  - https://openai.github.io/openai-agents-python/guardrails/
  - https://openai.github.io/openai-agents-python/handoffs/
  - https://openai.github.io/openai-agents-python/tracing/
  - https://openai.github.io/openai-agents-python/sessions/
  - https://openai.github.io/openai-agents-python/voice/pipeline/
  - https://openai.github.io/openai-agents-python/ref/voice/pipeline/
  - https://openai.github.io/openai-agents-python/ref/voice/workflow/
  - https://openai.github.io/openai-agents-python/mcp/
  - https://openai.github.io/openai-agents-python/context/
  - https://openai.github.io/openai-agents-python/results/
  - https://openai.github.io/openai-agents-python/ref/result/
  - https://openai.github.io/openai-agents-python/streaming/
  - https://openai.github.io/openai-agents-python/human_in_the_loop/
  - https://openai.github.io/openai-agents-python/release/
  - https://github.com/openai/openai-agents-python/releases
  - https://temporal.io/blog/announcing-openai-agents-sdk-integration
date_researched: 2026-04-13
date_enriched: 2026-04-13
sdk_version: v0.13.6
python_requires: ">=3.10"
lineage: "Swarm (Oct 2024, experimental) -> Agents SDK (Mar 2025, production)"
related:
  - p01_kc_agent
  - p01_kc_handoff_protocol
  - p01_kc_terminology_openai_canonical
  - p01_kc_claude_agent_sdk_patterns
  - capability-registry-builder
  - p01_kc_agent_card
  - cex_llm_vocabulary_whitepaper
  - bld_config_capability_registry
  - atom_09_autogen_ag2
  - atom_05_semantic_kernel
---

# OpenAI Agents SDK -- Deep Vocabulary Atlas

> **Scope**: Exhaustive class/type/concept registry for `openai-agents` Python SDK.
> Covers every public primitive, pattern, and integration point as of v0.13.6.

---

## 1. Lineage: Swarm to Agents SDK

| Dimension | Swarm (Oct 2024) | Agents SDK (Mar 2025+) |
|-----------|-------------------|------------------------|
| Status | Experimental, educational | Production-grade, actively maintained |
| Primitives | Agent + Handoff | Agent + Handoff + Guardrail + Tracing + Session |
| Tools | Function tools only | Function + Hosted + MCP + Computer + Shell + Codex |
| Safety | None built-in | Input/Output/Tool guardrails, tripwires |
| Observability | None | Full tracing with spans, exporters |
| Voice | None | VoicePipeline + RealtimeAgent |
| Session | None | 8+ backends (SQLite, Redis, SQLAlchemy, Dapr, etc.) |
| API | Chat Completions | Responses API (primary) + Chat Completions (fallback) |
| Design patterns | Routing, handoffs | + Prompt chaining, parallelization, orchestrator-workers, evaluator-optimizer |

Swarm's two core abstractions (Agent + Handoff) were preserved verbatim.
The SDK added guardrails, tracing, sessions, voice, and hosted tools.
Breaking change in v0.6.0 (Nov 2025): handoff history collapsed into single context message.

---

## 2. Full Class/Type Registry

### 2.1 Core Primitives

| Class | Module | Purpose | CEX Pillar |
|-------|--------|---------|------------|
| `Agent` | `agents` | LLM + instructions + tools + handoffs -- the fundamental unit | P02 (agent) |
| `Runner` | `agents` | Executes agents, manages loop lifecycle | P12 (orchestration) |
| `RunResult` | `agents` | Sync execution result (final_output, new_items, last_agent) | P05 (output) |
| `RunResultStreaming` | `agents` | Async streaming result with stream_events() | P05 (output) |
| `RunResultBase` | `agents` | Shared base for RunResult and RunResultStreaming | P05 (output) |
| `RunConfig` | `agents` | Per-run configuration (model, guardrails, tracing, etc.) | P09 (config) |
| `RunState` | `agents` | Serializable execution state for long-running approvals | P10 (memory) |
| `RunContextWrapper[T]` | `agents` | Generic context wrapper -- dependency injection for tools/hooks | P10 (memory) |
| `ToolContext[T]` | `agents` | Extends RunContextWrapper with tool_name, tool_call_id, tool_arguments | P04 (tools) |
| `Handoff` | `agents` | Dataclass: delegation mechanism with routing logic | P12 (orchestration) |
| `HandoffInputData` | `agents` | input_history + pre_handoff_items + new_items + run_context | P12 (orchestration) |

### 2.2 Agent Parameters (complete)

| Parameter | Type | Purpose |
|-----------|------|---------|
| `name` | `str` | Human-readable identifier |
| `instructions` | `str \| Callable` | System prompt or dynamic callback |
| `model` | `str \| Model` | LLM to use |
| `tools` | `list[Tool]` | Capabilities the agent can invoke |
| `handoffs` | `list[Agent \| Handoff]` | Delegation targets |
| `handoff_description` | `str` | Brief summary for handoff targeting |
| `model_settings` | `ModelSettings` | temperature, top_p, tool_choice, etc. |
| `output_type` | `type` | Pydantic model / dataclass for structured output |
| `prompt` | `dict` | OpenAI Responses API prompt configuration |
| `input_guardrails` | `list[InputGuardrail]` | Validation on initial user input |
| `output_guardrails` | `list[OutputGuardrail]` | Validation on final agent output |
| `hooks` | `AgentHooks` | Agent-scoped lifecycle callbacks |
| `mcp_servers` | `list[MCPServer]` | MCP-backed tool servers |
| `mcp_config` | `dict` | MCP schema conversion + error config |
| `tool_use_behavior` | `str` | Control if tool results loop back or end run |
| `reset_tool_choice` | `bool` | Prevents tool-use infinite loops (default True) |

**Methods**:
- `clone(**overrides)` -- duplicate Agent, change any properties
- `as_tool(tool_name, tool_description, needs_approval, ...)` -- expose agent as callable tool

### 2.3 Tool Types

| Class | Category | Purpose | CEX Pillar |
|-------|----------|---------|------------|
| `FunctionTool` | Local | Manual function tool creation | P04 |
| `@function_tool` | Local | Decorator wrapping Python functions as tools | P04 |
| `WebSearchTool` | Hosted | Agent searches the web | P04 |
| `FileSearchTool` | Hosted | Retrieves from OpenAI Vector Stores | P04 |
| `CodeInterpreterTool` | Hosted | Sandboxed code execution | P04 |
| `ImageGenerationTool` | Hosted | Generates images from prompts | P04 |
| `HostedMCPTool` | Hosted | Remote MCP server via Responses API | P04 |
| `ToolSearchTool` | Hosted | Deferred/lazy tool loading | P04 |
| `ComputerTool` | Local | GUI/browser automation | P04 |
| `ShellTool` | Local | Shell command execution | P04 |
| `LocalShellTool` | Local | Legacy local shell (deprecated) | P04 |
| `ApplyPatchTool` | Local | File diff application | P04 |
| `McpTool` | Protocol | Tool backed by MCP server | P04 |
| `codex_tool()` | Factory | Workspace-scoped task delegation to Codex | P04 |

**Function tool parameters**:

| Parameter | Purpose |
|-----------|---------|
| `name_override` | Custom tool name |
| `defer_loading` | Lazy schema surface loading |
| `timeout` | Per-call timeout |
| `timeout_behavior` | "error_as_result" or "raise_exception" |
| `failure_error_function` | Custom error responses |
| `use_docstring_info` | Parse docstrings for schema |
| `parameters` | Pydantic model for structured input |
| `include_input_schema` | Include JSON Schema in tool definition |
| `input_builder` | Customize argument mapping |
| `needs_approval` | Human-in-the-loop gate |
| `is_enabled` | Conditional runtime enabling |

### 2.4 Guardrail Types

| Class | Scope | Runs When | CEX Pillar |
|-------|-------|-----------|------------|
| `InputGuardrail` | Agent | Before agent execution (parallel or blocking) | P11 (guardrail) |
| `OutputGuardrail` | Agent | After final agent output | P11 (guardrail) |
| `ToolInputGuardrail` | Tool | Before tool execution | P11 (guardrail) |
| `ToolOutputGuardrail` | Tool | After tool execution | P11 (guardrail) |
| `GuardrailFunctionOutput` | Return type | Contains output_info + tripwire_triggered | P11 |
| `InputGuardrailResult` | Result | Wraps GuardrailFunctionOutput for input | P11 |
| `OutputGuardrailResult` | Result | Wraps GuardrailFunctionOutput for output | P11 |

**Decorators**: `@input_guardrail`, `@output_guardrail`, `@tool_input_guardrail`, `@tool_output_guardrail`

**Exceptions**:
- `InputGuardrailTripwireTriggered` -- halts execution when input fails validation
- `OutputGuardrailTripwireTriggered` -- halts execution when output fails validation

**Execution modes**:
- Parallel (default): guardrail runs concurrent with agent -- best latency, but agent may consume tokens before cancellation
- Blocking: guardrail completes before agent starts -- prevents wasted tokens if tripwire triggers

**Workflow boundaries**: Input guardrails run only on the FIRST agent. Output guardrails run only on the LAST agent. For per-tool checks in multi-agent flows, use tool guardrails.

### 2.5 Model Layer

| Class | Purpose | CEX Pillar |
|-------|---------|------------|
| `Model` | Base interface for all model implementations | P02 |
| `OpenAIResponsesModel` | Responses API (recommended) | P02 |
| `OpenAIChatCompletionsModel` | Chat Completions API (fallback) | P02 |
| `OpenAIResponsesWSModel` | WebSocket-based Responses model | P02 |
| `ModelProvider` | Interface: maps model names to implementations | P02 |
| `OpenAIProvider` | Default provider with configurable transport | P02 |
| `MultiProvider` | Routes prefix-based names (e.g. "openai/...", "any-llm/...") | P02 |
| `AnyLLMProvider` | Third-party adapter for Any-LLM | P02 |
| `LiteLLMProvider` | Third-party adapter for LiteLLM routing | P02 |
| `ModelSettings` | temperature, reasoning, tool_choice, truncation, store, prompt caching, logprobs, retry | P09 |
| `ModelRetrySettings` | max_attempts, backoff strategy, policy callbacks | P09 |
| `ModelRetryBackoffSettings` | initial_delay, max_delay, multiplier, jitter | P09 |

**Global config functions**:
- `set_default_openai_key(key)`
- `set_default_openai_client(client: AsyncOpenAI)`
- `set_default_openai_api("responses" | "chat_completions")`
- `set_default_openai_responses_transport("http" | "websocket")`

**Environment variables**: `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_ORG_ID`, `OPENAI_PROJECT_ID`, `OPENAI_DEFAULT_MODEL`

### 2.6 Session Layer

| Class | Backend | CEX Pillar |
|-------|---------|------------|
| `Session` | Protocol (base interface) | P10 |
| `SessionABC` | Abstract base class | P10 |
| `SQLiteSession` | File-backed or in-memory SQLite | P10 |
| `AsyncSQLiteSession` | Async SQLite via aiosqlite | P10 |
| `RedisSession` | Distributed Redis | P10 |
| `SQLAlchemySession` | Production DB via SQLAlchemy | P10 |
| `DaprSession` | Cloud-native Dapr sidecars | P10 |
| `OpenAIConversationsSession` | OpenAI Conversations API backend | P10 |
| `OpenAIResponsesCompactionSession` | Auto-compaction wrapper | P10 |
| `AdvancedSQLiteSession` | Enhanced: branching support | P10 |
| `EncryptedSession` | Transparent encryption wrapper | P10 |

**Session methods**:
- `get_items(limit=None)` -- retrieve conversation history
- `add_items(items)` -- store new items
- `pop_item()` -- remove most recent
- `clear_session()` -- erase all
- `run_compaction()` -- trigger history compaction

**Session config**: `session_id`, `session_settings`, `session_input_callback`, `ttl`, `encryption_key`, `should_trigger_compaction`

### 2.7 Tracing/Observability

| Class/Function | Purpose | CEX Pillar |
|----------------|---------|------------|
| `trace()` | Context manager for creating traces | P07 |
| `Trace` | End-to-end operation (workflow_name, trace_id, group_id) | P07 |
| `Span` | Timed operation within a trace (started_at, ended_at, span_data) | P07 |
| `TraceProvider` | Creates traces during initialization | P07 |
| `TracingProcessor` | Interface for custom trace handling | P07 |
| `BatchTraceProcessor` | Exports traces/spans in batches | P07 |
| `BackendSpanExporter` | Sends to OpenAI backend | P07 |

**Span factory functions** (auto-wrap operations):

| Factory | What it wraps |
|---------|---------------|
| `agent_span()` | Agent execution |
| `generation_span()` | LLM inference call |
| `function_span()` | Tool function call |
| `guardrail_span()` | Guardrail evaluation |
| `handoff_span()` | Agent-to-agent handoff |
| `transcription_span()` | Speech-to-text |
| `speech_span()` | Text-to-speech |
| `speech_group_span()` | Related audio grouping |
| `custom_span()` | User-defined tracking |

**Trace config functions**:
- `add_trace_processor(processor)` -- augment default pipeline
- `set_trace_processors(processors)` -- replace defaults
- `flush_traces()` -- block until buffered traces export
- `set_tracing_disabled(disabled)` -- global on/off
- `set_tracing_export_api_key(key)` -- alternate API key for export

**Identifiers**: `trace_id` (format: `trace_<32_alphanumeric>`), `span_id`, `group_id`

**Trace properties**: `workflow_name`, `trace_id`, `group_id`, `disabled`, `metadata`

### 2.8 Streaming Events

| Event Class | Level | Purpose |
|-------------|-------|---------|
| `StreamEvent` | Base | Base type for all streaming updates |
| `RawResponsesStreamEvent` | Low | Raw LLM events (response.created, response.output_text.delta) |
| `RunItemStreamEvent` | High | Semantic events for completed items |
| `AgentUpdatedStreamEvent` | High | Current agent changed (handoff occurred) |

**RunItemStreamEvent.name values**:
- `message_output_created`
- `handoff_requested`
- `handoff_occured` (intentional misspelling, backward compat)
- `tool_called`
- `tool_search_called`
- `tool_search_output_created`
- `tool_output`
- `reasoning_item_created`
- `mcp_approval_requested`
- `mcp_approval_response`
- `mcp_list_tools`

**RunResult items** (`new_items` field):
- `MessageOutputItem`
- `ToolCallItem`
- `HandoffCallItem`
- `ToolApprovalItem`
- `ReasoningItem` (implied by `reasoning_item_created`)

### 2.9 Hooks / Lifecycle

| Hook Class | Scope | CEX Pillar |
|------------|-------|------------|
| `RunHooks` | Entire Runner.run() invocation | P12 |
| `AgentHooks` | Specific agent instance | P02 |
| `AgentHookContext` | Context wrapper for agent hooks | P10 |

**RunHooks methods**:
- `on_agent_start(context, agent)`
- `on_agent_end(context, agent, output)`
- `on_llm_start(context, agent)`
- `on_llm_end(context, agent, response)`
- `on_tool_start(context, agent)`
- `on_tool_end(context, agent)`
- `on_handoff(context, agent)`

### 2.10 Human-in-the-Loop

| Term | Purpose |
|------|---------|
| `needs_approval` | Parameter on tools -- `True`, or async per-call function |
| `ToolApprovalItem` | Dataclass in `result.interruptions` with approval details |
| `RunState` | Serializable state for durable long-running approvals |
| `state.approve()` | Resolve pending approval positively |
| `state.reject()` | Resolve pending approval negatively |
| `always_approve` | Sticky approval persisting across serialization |
| `always_reject` | Sticky rejection persisting across serialization |
| `rejection_message` | Custom per-call rejection text |
| `on_approval` | Callback for auto-approval (Shell/Patch tools) |
| `on_approval_request` | Callback for hosted MCP tools |
| `require_approval` | MCP server parameter: "always" / "never" / per-tool map |

**RunState serialization**: `to_state()`, `to_string()`, `from_string()`, `to_json()`, `from_json()`

### 2.11 MCP Integration

| Class | Transport | CEX Pillar |
|-------|-----------|------------|
| `MCPServerStdio` | Local subprocess via stdin/stdout | P04 |
| `MCPServerSse` | HTTP + Server-Sent Events (deprecated) | P04 |
| `MCPServerStreamableHttp` | HTTP streamable connections | P04 |
| `MCPServerManager` | Coordinates multiple servers | P04 |
| `HostedMCPTool` | Remote MCP via Responses API | P04 |

**MCP config parameters**:
- `cache_tools_list` -- cache list_tools() for reduced latency
- `invalidate_tools_cache()` -- force fresh tool list
- `tool_filter` -- static or dynamic via `create_static_tool_filter()`
- `tool_meta_resolver` -- inject metadata into `_meta` payloads
- `convert_schemas_to_strict` -- best-effort JSON schema conversion
- `failure_error_function` -- error surfacing to model
- `require_approval` -- HITL policies

### 2.12 Voice Pipeline

| Class | Purpose | CEX Pillar |
|-------|---------|------------|
| `VoicePipeline` | 3-step: STT -> agent -> TTS | P05 |
| `VoicePipelineConfig` | Model providers, tracing, STT/TTS settings | P09 |
| `VoiceWorkflowBase` | Base class for voice workflow logic | P12 |
| `SingleAgentVoiceWorkflow` | Simple single-agent voice workflow | P12 |
| `AudioInput` | Complete audio buffer (push-to-talk) | P05 |
| `StreamedAudioInput` | Progressive audio chunks with activity detection | P05 |
| `StreamedAudioResult` | Pipeline result with event streaming | P05 |
| `STTModel` | Speech-to-text model interface | P02 |
| `TTSModel` | Text-to-speech model interface | P02 |
| `VoiceModelProvider` | Maps model names to STT/TTS implementations | P02 |
| `RealtimeAgent` | Voice agent using gpt-realtime-1.5 | P02 |

**Voice stream event types**:
- `VoiceStreamEventAudio` -- audio output chunks
- `VoiceStreamEventLifecycle` -- turn started/ended
- `VoiceStreamEventError` -- error notifications

### 2.13 RunConfig (complete parameters)

| Parameter | Purpose |
|-----------|---------|
| `model` | Override default LLM across all agents |
| `model_provider` | Provider for resolving model names |
| `model_settings` | Global temperature, top_p, etc. |
| `session_settings` | History retrieval behavior |
| `input_guardrails` | Global safety checks on input |
| `output_guardrails` | Global safety checks on output |
| `handoff_input_filter` | Transform handoff payloads |
| `call_model_input_filter` | Modify prepared input before LLM call |
| `reasoning_item_id_policy` | "preserve" or "omit" reasoning IDs |
| `tracing_disabled` | Disable tracing |
| `tracing` | Trace-specific settings dict |
| `trace_metadata` | Metadata attached to traces |
| `trace_include_sensitive_data` | Include sensitive data in traces |
| `tool_error_formatter` | Custom rejection messages |
| `max_turns` | Interaction limit |
| `error_handlers` | Dict mapping error kinds to recovery callbacks |
| `conversation_id` | Server-managed conversation resource |
| `previous_response_id` | Response chaining identifier |
| `auto_previous_response_id` | Enable chaining automatically |
| `nest_handoff_history` | Collapse prior transcript in handoffs |
| `handoff_history_mapper` | Custom history mapping function |

### 2.14 Global Configuration

| Function | Purpose |
|----------|---------|
| `set_default_openai_key()` | API key for LLM + tracing |
| `set_default_openai_client()` | Custom AsyncOpenAI instance |
| `set_default_openai_api()` | "responses" or "chat_completions" |
| `set_default_openai_responses_transport()` | "http" or "websocket" |
| `set_tracing_export_api_key()` | Dedicated tracing API key |
| `set_tracing_disabled()` | Global tracing on/off |
| `set_trace_processors()` | Replace trace processors |
| `enable_verbose_stdout_logging()` | Debug logging to stdout |

**Environment variables**:

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | Default API key |
| `OPENAI_BASE_URL` | Custom endpoint |
| `OPENAI_ORG_ID` | Organization |
| `OPENAI_PROJECT_ID` | Project |
| `OPENAI_DEFAULT_MODEL` | Default model name |
| `OPENAI_AGENTS_TRACE_INCLUDE_SENSITIVE_DATA` | 0/1 |
| `OPENAI_AGENTS_DONT_LOG_MODEL_DATA` | Prevent LLM I/O logging (default 1) |
| `OPENAI_AGENTS_DONT_LOG_TOOL_DATA` | Prevent tool data logging (default 1) |

**Logger names**: `openai.agents`, `openai.agents.tracing`

### 2.15 ResponsesWebSocketSession

| Member | Purpose |
|--------|---------|
| `ResponsesWebSocketSession` | Pin runs to shared WebSocket provider |
| `aclose()` | Close cached provider + WS connections |
| `run()` | Runner.run with session's RunConfig |
| `run_streamed()` | Runner.run_streamed with session's RunConfig |

### 2.16 Exceptions

| Exception | Trigger |
|-----------|---------|
| `InputGuardrailTripwireTriggered` | Input guardrail tripwire fires |
| `OutputGuardrailTripwireTriggered` | Output guardrail tripwire fires |
| `MaxTurnsExceeded` | Agent loop exceeds max_turns |

---

## 3. Handoff Protocol Vocabulary

The handoff system is the SDK's core multi-agent primitive, inherited from Swarm.

### 3.1 handoff() Factory Function

```
handoff(
    agent: Agent,
    tool_name_override: str | None,        # default: transfer_to_{agent.name}
    tool_description_override: str | None,
    on_handoff: Callable | None,           # callback on invocation
    input_type: type | None,               # Pydantic model for tool-call args
    input_filter: Callable | None,         # transform HandoffInputData
    is_enabled: bool | Callable,           # dynamic enable/disable
    nest_handoff_history: bool | None,     # per-call history nesting override
) -> Handoff
```

### 3.2 HandoffInputData Fields

| Field | Type | Purpose |
|-------|------|---------|
| `input_history` | list | Pre-run conversation history |
| `pre_handoff_items` | list | Items generated before handoff invocation |
| `new_items` | list | Items from current turn |
| `input_items` | list | Optional filtered items for next agent |
| `run_context` | RunContextWrapper | Active context wrapper |

### 3.3 Handoff Configuration

| Config | Level | Purpose |
|--------|-------|---------|
| `handoff_description` | Agent | Hint text for handoff targeting |
| `nest_handoff_history` | RunConfig | Collapse prior transcript into summary |
| `handoff_history_mapper` | RunConfig | Custom function replacing generated messages |
| `handoff_input_filter` | RunConfig | Global input filter for all handoffs |
| `input_filter` | Per-Handoff | Per-handoff input transformation |

### 3.4 Handoff vs Agent-as-Tool

| Pattern | Control | History | Use When |
|---------|---------|---------|----------|
| **Handoff** | Full transfer -- receiving agent responds directly | Shared or nested | Specialist takes over conversation |
| **Agent.as_tool()** | Orchestrator keeps control | Isolated (by default) | Sub-task, return result to orchestrator |

---

## 4. Guardrail Types and Interface

### 4.1 Type Taxonomy

```
Guardrail
  +-- InputGuardrail          (agent-level, on user input)
  |     +-- parallel mode     (concurrent with agent, default)
  |     +-- blocking mode     (before agent starts)
  +-- OutputGuardrail         (agent-level, on final output)
  +-- ToolInputGuardrail      (tool-level, before tool execution)
  +-- ToolOutputGuardrail     (tool-level, after tool execution)
```

### 4.2 Guardrail Function Signature

```python
@input_guardrail
async def check(ctx: RunContextWrapper, agent: Agent, input: str | list) -> GuardrailFunctionOutput:
    return GuardrailFunctionOutput(
        output_info={"reason": "..."},
        tripwire_triggered=False
    )
```

### 4.3 Tripwire Mechanics

1. Guardrail returns `GuardrailFunctionOutput(tripwire_triggered=True)`
2. SDK wraps in `InputGuardrailResult` or `OutputGuardrailResult`
3. SDK raises `InputGuardrailTripwireTriggered` or `OutputGuardrailTripwireTriggered`
4. Execution halts immediately

### 4.4 Workflow Boundaries

- Input guardrails: ONLY on the first agent in a chain
- Output guardrails: ONLY on the last agent in a chain
- Tool guardrails: on ANY agent that calls the guarded tool
- For multi-agent per-tool safety: use tool guardrails, not agent guardrails

---

## 5. Tracing / Observability Terms

### 5.1 Hierarchy

```
Trace (workflow_name, trace_id, group_id)
  +-- agent_span
  |     +-- generation_span (LLM call)
  |     +-- function_span (tool call)
  |     +-- guardrail_span
  |     +-- handoff_span
  +-- agent_span (after handoff)
  |     +-- generation_span
  |     ...
  +-- custom_span (user-defined)
```

### 5.2 Processing Pipeline

```
Span created -> TracingProcessor.on_span_start()
                  -> TracingProcessor.on_span_end()
                    -> BatchTraceProcessor (batches)
                      -> BackendSpanExporter (sends to OpenAI)
```

### 5.3 Integration Points

- OpenAI Dashboard: native visualization
- Custom exporters: implement `TracingProcessor`
- OpenTelemetry: bridge via custom processor
- Logfire, LangSmith, Braintrust: community integrations

---

## 6. Voice Pipeline Terms

### 6.1 Pipeline Architecture

```
Audio In -> STTModel -> VoiceWorkflowBase -> TTSModel -> Audio Out
             |              |                   |
        transcription   agent logic         speech
           span           spans              span
```

### 6.2 Two Voice Modes

| Mode | Class | Model | How It Works |
|------|-------|-------|-------------|
| Pipeline | `VoicePipeline` | Any text agent | STT -> Agent.run() -> TTS (3 steps) |
| Realtime | `RealtimeAgent` | gpt-realtime-1.5 | Direct audio-to-audio (native) |

### 6.3 Input Modes

| Class | Use Case | Activity Detection |
|-------|----------|-------------------|
| `AudioInput` | Pre-recorded / push-to-talk | None (complete buffer) |
| `StreamedAudioInput` | Live microphone | Yes (auto speaker-end detection) |

### 6.4 Output Events

| Event | Content |
|-------|---------|
| `VoiceStreamEventAudio` | Audio output chunks (PCM, 24kHz mono) |
| `VoiceStreamEventLifecycle` | Turn started / turn ended |
| `VoiceStreamEventError` | Error notifications |

---

## 7. Design Patterns (from Anthropic influence)

The SDK implements five established multi-agent patterns:

| Pattern | SDK Implementation |
|---------|-------------------|
| **Prompt Chaining** | Sequential Agent.run() calls, output of A feeds input of B |
| **Routing** | Handoffs with conditional is_enabled or dynamic instructions |
| **Parallelization** | Multiple Agent.as_tool() calls in single turn |
| **Orchestrator-Workers** | Manager agent with handoffs or as_tool to specialists |
| **Evaluator-Optimizer** | Output guardrail + retry loop (F7 GOVERN equivalent) |

---

## 8. Mapping to CEX Pillars

| OpenAI Agents SDK Concept | CEX Pillar | CEX Kind |
|---------------------------|------------|----------|
| Agent | P02 Model | `agent` |
| Agent.name + instructions | P03 Prompt | `system_prompt` |
| Agent.tools | P04 Tools | `cli_tool`, `browser_tool` |
| Agent.output_type | P06 Schema | `type_def` |
| Agent.handoffs | P12 Orchestration | `workflow`, `dispatch_rule` |
| Agent.input_guardrails | P11 Feedback | `guardrail` |
| Agent.output_guardrails | P11 Feedback | `quality_gate` |
| Runner | P12 Orchestration | `workflow` |
| RunConfig | P09 Config | `env_config` |
| RunResult | P05 Output | `output_template` |
| Session | P10 Memory | `memory_scope`, `entity_memory` |
| Trace / Span | P07 Evaluation | `benchmark`, `trace_config` |
| ModelProvider | P02 Model | `model_provider` |
| ModelSettings | P09 Config | `rate_limit_config` |
| MCPServer | P04 Tools | `mcp_server` |
| Handoff | P12 Orchestration | `dispatch_rule` |
| HandoffInputData | P12 Orchestration | `handoff` (CEX uses .md handoffs) |
| VoicePipeline | P05 Output | `output_template` |
| FunctionTool | P04 Tools | `cli_tool` |
| FileSearchTool | P01 Knowledge | `rag_source` |
| WebSearchTool | P04 Tools | `browser_tool` |
| RunHooks | P12 Orchestration | `workflow` (lifecycle) |
| AgentHooks | P02 Model | `agent` (hooks property) |
| ToolApprovalItem | P11 Feedback | `guardrail` (approval gate) |

---

## 9. Vocabulary Cross-Reference (SDK term -> Industry term)

| SDK Term | Industry Standard | Notes |
|----------|-------------------|-------|
| Agent | Agent (A2A, AutoGen) | Universal term |
| Handoff | Agent transfer / delegation | Swarm-originated term, now standard |
| Guardrail | Safety filter / validator | NeMo Guardrails uses same term |
| Tripwire | Circuit breaker / fail-fast | SDK-specific metaphor |
| Runner | Orchestrator / executor | LangGraph: "graph.invoke()", CrewAI: "crew.kickoff()" |
| RunConfig | Run settings / execution config | LangChain: "RunnableConfig" |
| Session | Conversation memory / thread | LangGraph: "checkpointer", AutoGen: "ConversableAgent.chat_messages" |
| Trace | Trace (OpenTelemetry) | Standard OTEL term |
| Span | Span (OpenTelemetry) | Standard OTEL term |
| ModelProvider | Model router / gateway | LiteLLM: "Router", CEX: "cex_router.py" |
| FunctionTool | Tool / function calling | Universal since GPT-3.5 |
| MCPServer | MCP server (Anthropic standard) | Cross-vendor protocol |
| VoicePipeline | Voice agent / speech pipeline | Emerging pattern |
| needs_approval | Human-in-the-loop gate | Standard HITL pattern |
| output_type | Structured output / response model | Pydantic-based, Instructor pattern |
| clone() | Agent forking / templating | CEX: archetype -> instance |
| as_tool() | Agent-as-tool / nested agent | AutoGen: "nested chat" |

---

## 10. SDK Technical Specs

| Spec | Value |
|------|-------|
| Package | `openai-agents` (PyPI) |
| Version | v0.13.6 (81 releases) |
| Python | >= 3.10 |
| Core deps | Pydantic, Requests, MCP Python SDK |
| Optional: voice | WebSockets |
| Optional: redis | redis, SQLAlchemy |
| API primary | OpenAI Responses API |
| API fallback | Chat Completions API |
| Transport | HTTP (default), WebSocket (opt-in) |
| Multi-provider | MultiProvider, AnyLLMProvider, LiteLLMProvider |
| Tracing backend | OpenAI Dashboard (default), custom exporters |
| License | MIT |

---

## 11. Key Differences from CEX Architecture

| Dimension | OpenAI Agents SDK | CEX |
|-----------|-------------------|-----|
| Agent definition | Python class (runtime) | 13 ISOs per kind (static + compiled) |
| Handoff | In-process function call | File-based .md handoff + dispatch.sh |
| Guardrail | Code decorator/class | 8F pipeline F7 GOVERN + quality gates |
| Session | DB-backed (SQLite/Redis/etc) | File-based (.cex/runtime/) |
| Tracing | OpenTelemetry-like spans | git log + signal files + cex_doctor |
| Multi-agent | Single process, shared memory | Multi-process, file-based coordination |
| Tool calling | Python function + MCP | Python tools + MCP + CLI tools |
| Model routing | ModelProvider interface | cex_router.py + nucleus_models.yaml |
| Quality control | Output guardrails | 3-layer scoring (structural + rubric + semantic) |
| Orchestration | Runner.run() loop | N07 dispatch grid + wave planning |

---

---

## 12. Breaking Changes Changelog (v0.1 -- v0.13)

Source: https://openai.github.io/openai-agents-python/release/ + GitHub releases

| Version | Breaking Change | Migration |
|---------|----------------|-----------|
| v0.1.0 | `MCPServer.list_tools()` signature expanded -- added required `run_context` and `agent` params | Update any custom MCP server subclasses |
| v0.2.0 | Methods accepting `Agent` now accept `AgentBase` (typing-only change) | Adjust type hints if using strict typing |
| v0.3.0 | Realtime API migrated to `gpt-realtime` model and GA interface | Update RealtimeAgent model strings |
| v0.4.0 | `openai` package v1.x no longer supported -- requires `openai>=2.0` | `pip install "openai>=2.0"` |
| v0.6.0 | Handoff history now packaged as single assistant message; default transcript includes introductory context before conversation block | Audit handoff history consumers |
| v0.7.0 | Nested handoff history no longer default -- was enabled, now opt-in | Add `RunConfig(nest_handoff_history=True)` to restore |
| v0.7.0 | `reasoning.effort` default changed to `"none"` for `gpt-5.1`/`gpt-5.2` (was `"low"`) | Set `model_settings=ModelSettings(reasoning={"effort":"low"})` explicitly if needed |
| v0.8.0 | Sync function tools now run via `asyncio.to_thread()` on worker threads (not event loop thread) | Migrate thread-local state dependencies to async |
| v0.8.0 | MCP error handling now configurable -- default returns model-visible error instead of failing run | Set `mcp_config={"failure_error_function": None}` to restore fail-fast |
| v0.9.0 | Python 3.9 support dropped (EOL) | Upgrade runtime to Python >= 3.10 |
| v0.9.0 | `Agent#as_tool()` return type narrowed from `Tool` to `FunctionTool` | Update type annotations that relied on broader `Tool` union |
| v0.10.0 -- v0.13.x | No public-interface breaking changes | -- |

**Release cadence note**: Minor version bumps (Y in 0.Y.x) signal possible breaking changes to public non-beta APIs. Pin to 0.Y.x to avoid unintended breaks.

---

## 13. Voice Pipeline -- Full Implementation Reference

### 13.1 VoicePipelineConfig (complete fields)

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `model_provider` | `VoiceModelProvider` | `OpenAIVoiceModelProvider()` | STT + TTS provider |
| `tracing_disabled` | `bool` | `False` | Disable all pipeline tracing |
| `tracing` | `TracingConfig \| None` | `None` | Tracing config (reuses main tracing system) |
| `trace_include_sensitive_data` | `bool` | `True` | Include text content in traces |
| `trace_include_sensitive_audio_data` | `bool` | `True` | Include audio bytes in traces |
| `workflow_name` | `str` | `"Voice Agent"` | Trace workflow label |
| `group_id` | `str` | `gen_group_id()` | Links multiple traces from same conversation |
| `trace_metadata` | `dict[str, Any] \| None` | `None` | Extra trace metadata |
| `stt_settings` | `STTModelSettings` | `STTModelSettings()` | Speech-to-text config |
| `tts_settings` | `TTSModelSettings` | `TTSModelSettings()` | Text-to-speech config |

### 13.2 STTModelSettings

| Field | Type | Purpose |
|-------|------|---------|
| `language` | `str \| None` | BCP-47 language code hint (e.g. "en", "pt") |
| `prompt` | `str \| None` | Context/hint for transcription accuracy |
| `temperature` | `float \| None` | Randomness in transcription (0.0 = deterministic) |
| `turn_detection` | `dict \| None` | Activity detection config for StreamedAudioInput |

### 13.3 TTSModelSettings

| Field | Type | Purpose |
|-------|------|---------|
| `voice` | `str \| None` | Voice selection (defaults to `DEFAULT_VOICE` constant) |
| `instructions` | `str \| None` | Extra instructions passed to speech API |

### 13.4 OpenAIVoiceModelProvider (constructor params)

| Parameter | Type | Purpose |
|-----------|------|---------|
| `api_key` | `str \| None` | OpenAI API key (falls back to env) |
| `base_url` | `str \| None` | Custom endpoint URL |
| `openai_client` | `AsyncOpenAI \| None` | Pre-built client instance |
| `organization` | `str \| None` | OpenAI organization ID |
| `project` | `str \| None` | OpenAI project ID |

Methods: `get_stt_model(model_name)` -> `STTModel`, `get_tts_model(model_name)` -> `TTSModel`

### 13.5 OpenAISTTModel (implementation)

| Member | Detail |
|--------|--------|
| Constructor | `model: str`, `openai_client: AsyncOpenAI` |
| `model_name` | Property: returns model string |
| `transcribe(audio, settings)` | Async: transcribes complete AudioInput, returns text |
| `create_session(settings)` | Async: creates streaming transcription session for StreamedAudioInput |
| Output format | Plain text string from Whisper-family models |

Supported models: `whisper-1`, `gpt-4o-audio-preview`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`

### 13.6 OpenAITTSModel (implementation)

| Member | Detail |
|--------|--------|
| Constructor | `model: str`, `openai_client: AsyncOpenAI` |
| `model_name` | Property: returns model string |
| `run(text, settings)` | Async generator: yields 1024-byte PCM chunks at 24kHz mono |
| Audio format | PCM signed 16-bit, 24000 Hz, 1 channel |

### 13.7 SingleAgentVoiceWorkflow

`SingleAgentVoiceWorkflow` wraps a single text-based `Agent` for use in a `VoicePipeline`.
It handles session state, tool integration, and multi-turn handoffs within the voice loop.

```python
from agents.voice import SingleAgentVoiceWorkflow, VoicePipeline, AudioInput

# Any text agent works -- same as a non-voice agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful voice assistant. Be concise.",
    model="gpt-4.1",
    tools=[get_weather],
    handoffs=[spanish_agent],   # handoffs work in voice too
)

pipeline = VoicePipeline(
    workflow=SingleAgentVoiceWorkflow(agent),
    config=VoicePipelineConfig(
        stt_settings=STTModelSettings(language="en"),
        tts_settings=TTSModelSettings(voice="alloy"),
    ),
)

# Push-to-talk mode
audio_input = AudioInput(buffer=pcm_bytes)
result = await pipeline.run(audio_input)

# Stream audio output
async for event in result.stream():
    if event.type == "voice_stream_event_audio":
        speaker.write(event.data)       # 1024-byte PCM chunk
    elif event.type == "voice_stream_event_lifecycle":
        print(event.event)              # "turn_started" or "turn_ended"
```

### 13.8 Custom VoiceWorkflow

For multi-agent or conditional voice flows, subclass `VoiceWorkflowBase`:

```python
from agents.voice import VoiceWorkflowBase, VoiceWorkflowCallbacks

class MyVoiceWorkflow(VoiceWorkflowBase):
    async def run(self, transcription: str, callbacks: VoiceWorkflowCallbacks):
        # Route to different agents based on transcription
        result = await Runner.run(routing_agent, transcription)
        await callbacks.on_text(result.final_output)
```

### 13.9 Voice Pipeline Limitations (as of v0.13.6)

- No built-in interruption support for `StreamedAudioInput` (user cannot interrupt mid-speech)
- `RealtimeAgent` (gpt-realtime-1.5) is a separate path -- does NOT use VoicePipeline
- Voice tracing spans: `transcription_span`, `speech_span`, `speech_group_span` auto-created
- Install: `pip install "openai-agents[voice]"` (WebSockets optional dep)

---

## 14. Responses API Integration Map

The Responses API is the primary (recommended) transport for the SDK. Key integration points:

### 14.1 Server-Managed Conversation State

Two mutually exclusive strategies for cross-turn continuity via OpenAI servers (no local session needed):

| Strategy | Parameter | How It Works |
|----------|-----------|-------------|
| Response chaining | `previous_response_id` | Pass `result.last_response_id` to next `Runner.run()` call |
| Auto-chaining | `auto_previous_response_id=True` | SDK automatically threads response IDs across turns |
| Named conversation | `conversation_id` | Server creates a named resource; reuse same ID across workers/services |

**Constraint**: `conversation_id` and `previous_response_id` are mutually exclusive. Neither can combine with local `Session` in the same run.

### 14.2 Response-Chaining Pattern

```python
config = RunConfig(auto_previous_response_id=True)

# Turn 1
result = await Runner.run(agent, "Hello", run_config=config)

# Turn 2 -- SDK automatically links to previous response
result = await Runner.run(agent, "Follow up", run_config=config)
# result.last_response_id tracks the chain
```

### 14.3 call_model_input_filter

Hook executed immediately before each LLM call. Receives fully prepared items (including session history) and can trim, inject, or transform:

```python
def trim_old_items(ctx, agent, input_data):
    # Keep only last 10 items to reduce token burn
    return ModelInputData(input=input_data.input[-10:])

config = RunConfig(call_model_input_filter=trim_old_items)
```

### 14.4 Responses API-Only Features

| Feature | Why Responses-only |
|---------|-------------------|
| `ToolSearchTool` | Deferred tool loading via server |
| `conversation_id` | Server-managed conversation resource |
| `previous_response_id` | Response chain pointer |
| `store=True` in ModelSettings | Server-side response storage |
| `truncation="auto"` in ModelSettings | Server drops oldest items on overflow |
| `HostedMCPTool` | Remote MCP via server-side execution |
| WebSocket transport | `OpenAIResponsesWSModel` + `ResponsesWebSocketSession` |

### 14.5 Responses API vs Chat Completions Compatibility

| Capability | Responses API | Chat Completions |
|-----------|---------------|-----------------|
| SDK recommended | YES | Fallback only |
| Hosted tools | YES | NO |
| MCP (hosted) | YES | NO |
| should_replay_reasoning_content | NO | YES (v0.10+) |
| Response chaining | YES | NO |
| Structured outputs | YES | YES |
| Streaming | YES | YES |
| Default model | gpt-4.1 | gpt-4.1 |

---

## 15. Third-Party Adapters & Community Extensions

### 15.1 Official Third-Party Adapters (bundled in SDK)

| Adapter | Install | Model Prefix | Status |
|---------|---------|-------------|--------|
| LiteLLM | `openai-agents[litellm]` | `litellm/...` | Beta (best-effort) |
| Any-LLM | `openai-agents[any-llm]` | `any-llm/...` | Beta (best-effort) |

**LiteLLM usage** -- routes to 100+ providers (Anthropic, Gemini, Bedrock, etc.):

```python
from agents.extensions.models.litellm_provider import LitellmModel

agent = Agent(
    model=LitellmModel(model="anthropic/claude-3-5-sonnet"),
    instructions="...",
)
# Or via MultiProvider prefix:
# model="litellm/anthropic/claude-3-5-sonnet"
```

**Any-LLM usage** -- adapter-managed routing with compatibility layers:

```python
from agents.extensions.models.anyllm_provider import AnyLLMModel

agent = Agent(model=AnyLLMModel(model="gpt-4o"), instructions="...")
```

**Recent update (v0.10+)**: `should_replay_reasoning_content` flag on Chat Completions integrations enables reasoning-content replay for DeepSeek/vLLM chains via LiteLLM.

### 15.2 MultiProvider Prefix Routing

`MultiProvider` enables prefix-based routing in a single grid -- different agents can use different providers:

```python
from agents import MultiProvider

provider = MultiProvider(openai_api_key="...", openai_base_url="...")
# Use: model="openai/gpt-4.1" or model="litellm/anthropic/claude-3-opus"
config = RunConfig(model_provider=provider)
```

Config options: `openai_prefix_mode` ("error" | "ignore"), `unknown_prefix_mode` ("error" | "ignore")

### 15.3 Community Observability Integrations

| Integration | Method | What It Captures |
|-------------|--------|-----------------|
| Logfire (Pydantic) | Custom `TracingProcessor` | All spans + agent events |
| LangSmith | Custom `TracingProcessor` | Traces mapped to LangSmith run format |
| Braintrust | Custom `TracingProcessor` | Evals + traces |
| OpenTelemetry | Bridge processor | Standard OTEL spans for Jaeger/Tempo/etc. |

### 15.4 Temporal Workflow Integration

As of 2026, Temporal.io announced an official integration for durable, fault-tolerant agent workflows:

- Source: https://temporal.io/blog/announcing-openai-agents-sdk-integration
- Wraps `Runner.run()` calls as Temporal Activities
- Provides retry policies, timeouts, and versioning for multi-step agent pipelines
- Enables long-running HITL workflows with persistent `RunState` across Temporal checkpoints

### 15.5 Install Extras Matrix

| Extra | Package | What It Enables |
|-------|---------|----------------|
| `[voice]` | WebSockets | VoicePipeline + StreamedAudioInput |
| `[litellm]` | litellm | 100+ provider routing |
| `[any-llm]` | any-llm | Any-LLM adapter |
| `[all]` | all above | Full feature set |

---

*Research conducted 2026-04-13. Enriched 2026-04-13 (Wave 2 hydration). SDK version v0.13.6.*
*Sources: official docs at openai.github.io/openai-agents-python, release page, GitHub releases, Temporal blog.*
*Next atom candidates: Google ADK (atom_04), LangGraph (atom_05), CrewAI (atom_06).*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent]] | sibling | 0.35 |
| [[p01_kc_handoff_protocol]] | sibling | 0.34 |
| [[p01_kc_terminology_openai_canonical]] | sibling | 0.34 |
| [[p01_kc_claude_agent_sdk_patterns]] | sibling | 0.31 |
| [[capability-registry-builder]] | downstream | 0.30 |
| [[p01_kc_agent_card]] | sibling | 0.28 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.28 |
| [[bld_config_capability_registry]] | downstream | 0.27 |
| [[atom_09_autogen_ag2]] | sibling | 0.26 |
| [[atom_05_semantic_kernel]] | sibling | 0.26 |
