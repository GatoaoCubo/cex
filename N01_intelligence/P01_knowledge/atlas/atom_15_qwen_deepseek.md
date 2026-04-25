---
id: atom_15_qwen_deepseek
kind: knowledge_card
8f: F3_inject
title: "Atomic Research 15: Qwen-Agent + DeepSeek Tool-Calling Specs"
version: "1.2.0"
quality: 8.9
tags: [qwen, deepseek, tool-calling, function-calling, mcp, reasoning, agent-framework, hermes, strict-mode, agentic-training, grpo, budget-tokens, rolling-checkpoint]
pillar: P01
domain: llm-agent-tooling
density_score: 0.97
sources:
  - https://github.com/QwenLM/Qwen-Agent
  - https://api-docs.deepseek.com/guides/tool_calls
  - https://api-docs.deepseek.com/guides/thinking_mode
  - https://api-docs.deepseek.com/guides/reasoning_model
  - https://api-docs.deepseek.com/api-reference
  - https://deepwiki.com/QwenLM/Qwen-Agent
  - https://deepwiki.com/QwenLM/Qwen-Agent/4.4-mcp-integration
  - https://deepwiki.com/QwenLM/Qwen-Agent/5.3-mcp-tool-integration
  - https://deepwiki.com/QwenLM/Qwen3/4.3-function-calling-and-tool-use
  - https://chat-deep.ai/docs/deepseek-tool-calls/
  - https://api-docs.deepseek.com/news/news251201
  - https://huggingface.co/deepseek-ai/DeepSeek-V3.2
  - https://arxiv.org/abs/2512.02556
  - https://docs.vllm.ai/en/latest/features/tool_calling/
  - https://github.com/vllm-project/vllm/issues/19056
  - https://github.com/NousResearch/Hermes-Function-Calling
  - https://kili-technology.com/blog/data-story-deepseek-v3-2
  - https://lawwu.github.io/til/posts/2025-05-02-qwen3-chat-prompt-template/index.html
  - https://huggingface.co/blog/qwen-3-chat-template-deep-dive
related:
  - p01_kc_function_def
  - p01_kc_agent
  - atom_03_openai_agents_sdk
  - p01_kc_tool_use
  - p01_kc_terminology_openai_canonical
  - atom_16_minimax_kimi_glm
  - atom_11_agentscope
  - p01_kc_server_tools
  - p01_kc_openai_api_patterns
  - p03_pt_sdk_agent_builder
---

# Atomic Research 15: Qwen-Agent + DeepSeek Tool-Calling Specs

Two Chinese-origin LLM ecosystems with distinct tool-calling architectures.
Qwen-Agent is a full agent framework (like LangChain) with native MCP.
DeepSeek is an API-first provider with a unique thinking-with-tools paradigm.

---

## 1. Qwen-Agent Framework

### 1.1 Architecture Overview

Qwen-Agent is a Python framework built on three atomic components:

| Component | Base Class | Role |
|-----------|-----------|------|
| LLMs | `BaseChatModel` | Model backends (DashScope, OpenAI-compat, local) |
| Tools | `BaseTool` | Callable capabilities with schema |
| Agents | `Agent` | Orchestration loops combining LLMs + Tools |

### 1.2 Agent Class Hierarchy

```
Agent (abstract: run(), _run(), _call_llm(), _call_tool(), _detect_tool())
  |-- BasicAgent          # Direct LLM pass-through, no tools
  |-- FnCallAgent         # Iterative tool-calling loop (max 8 iterations)
  |     |-- Assistant     # FnCallAgent + RAG via Memory component
  |-- ReActChat           # Text-based ReAct pattern (Thought-Action-Observation)
  |-- MultiAgentHub       # Orchestrates multiple agents with selection logic
  |-- Router              # Routes tasks to specialized agents
  |-- GroupChat           # Multi-agent conversation
```

**FnCallAgent loop**: call LLM -> parse `function_call` -> execute tool -> append `FUNCTION` message -> repeat until no tool calls or `MAX_LLM_CALL_PER_RUN=8`.

**ReActChat**: NOT recommended for Qwen3 reasoning models because the model may output ReAct stopwords inside `<think>` blocks, causing premature truncation.

### 1.3 Tool System

**Registration via decorator**:
```python
from qwen_agent.tools import BaseTool, register_tool

@register_tool('my_tool')
class MyTool(BaseTool):
    description = 'Tool description for the agent'
    parameters = [
        {'name': 'query', 'type': 'string', 'description': 'Search query', 'required': True}
    ]

    def call(self, params: str, **kwargs) -> str:
        args = json.loads(params)
        return do_something(args['query'])
```

- `TOOL_REGISTRY`: global dict for runtime lookup by string name
- `BaseToolWithFileAccess`: subclass for file-aware operations
- Three init formats: string name, dict config, direct instance

**Built-in tools**: `code_interpreter` (Docker sandbox + Jupyter kernel), `mcp_manager`, `doc_parser` (PDF/DOCX/PPTX/HTML), `retrieval` (vector/keyword/hybrid RAG), `storage` (file KV).

### 1.4 Function Calling Templates

| Template | Parser flag | Use case | Parallel calls |
|----------|-----------|----------|----------------|
| NousFnCallPrompt | `--tool-call-parser hermes` | Default for Qwen3 | Yes |
| ReActPrompt | N/A (text-based) | Legacy, avoid for Qwen3 | No |

Qwen3 uses **ChatML format with XML-structured tool definitions**:

```xml
<tools>
{"type": "function", "function": {"name": "fn", "parameters": {...}}}
</tools>
```

Tool calls emitted as:
```xml
<tool_call>
{"name": "fn", "arguments": {...}}
</tool_call>
```

Tool responses:
```xml
<tool_response>
{result_data}
</tool_response>
```

#### 1.4.1 Hermes NousFnCallPrompt: Full System Prompt Format

The NousFnCallPrompt injects a structured preamble into the system message:

```
You are a function-calling AI. Tools are provided inside <tools>...</tools>.
When appropriate, call a tool by emitting a <tool_call>{...}</tool_call> JSON object.
After a tool responds (as <tool_response>), continue reasoning inside <think>
and produce the final answer.
```

**Parallel calls** are emitted as consecutive `<tool_call>` blocks in a single assistant turn:
```xml
<tool_call>
{"name": "fn_a", "arguments": {"x": 1}}
</tool_call>
<tool_call>
{"name": "fn_b", "arguments": {"y": 2}}
</tool_call>
```

**vLLM serving command** with Hermes parser enabled:
```bash
vllm serve Qwen/Qwen3-8B --enable-auto-tool-choice --tool-call-parser hermes
```

**Known tokenizer bug (vLLM issue #19056)**: Qwen3's tokenizer has a special token `}` with
token ID 9207. The Hermes streaming parser (`extract_tool_calls_streaming`) truncates on this
token, producing broken JSON output in tool calls. Workaround: use non-streaming mode or
patch the parser to handle ID 9207 as literal `}`.

**ChatML message roles for tool flow**:
- `<|im_start|>system` -- tool schema injection
- `<|im_start|>assistant` -- tool call emission (`<tool_call>`)
- `<|im_start|>tool` -- tool response injection (`<tool_response>`)
- Token ID 151668 -- closing `</think>` tag; parser uses this to split reasoning from output

#### 1.4.2 Qwen3 Context Management: Rolling Checkpoint and No Default System Prompt

**No default system prompt**: Qwen3 ships WITHOUT a built-in system prompt (unlike Qwen2.5
which included "You are a helpful assistant" by default). Operators MUST inject the system
message explicitly or tool schemas will not be present in context.
Source: lawwu.github.io/til/posts/2025-05-02-qwen3-chat-prompt-template/

**Rolling checkpoint algorithm** (chat template, Hugging Face blog on Qwen3 template):
1. Traverse messages in REVERSE order
2. Find the latest non-tool-call user turn (the "checkpoint")
3. All messages BEFORE the checkpoint: `<think>` blocks compressed or removed to save tokens
4. All messages AT/AFTER the checkpoint: full `<think>` blocks preserved
5. Effect: prevents unbounded reasoning-token growth in long conversations

**Implication**: In a 10-turn conversation, only the current active reasoning block is fully
preserved. Prior `reasoning_content` from earlier turns is pruned from context. CEX sessions
relying on Qwen3 should not depend on recovering full CoT from previous turns -- only
`content` fields are reliable across turn boundaries.

### 1.5 reasoning_content Field

For reasoning models (QwQ, QvQ, Qwen3), messages carry an optional `reasoning_content` field separate from `content`.

**thought_in_content parameter**:
- `True`: content = `<think>reasoning</think>answer` (single field)
- `False`: separate `reasoning_content` and `content` fields

**Critical**: When using function calling, the client MUST pass back `reasoning_content` in conversation history. Ignoring it (standard OpenAI format) causes severe output anomalies.

Token ID `151668` marks the closing `</think>` tag for parser detection.

#### 1.5.1 reasoning_content Lifecycle: Full Multi-Turn Message Structure

**Qwen3 -- multi-turn tool-calling with reasoning**:

Turn 1 assistant response (from API):
```json
{
  "role": "assistant",
  "reasoning_content": "I need to call fn_a to get X...",
  "content": null,
  "tool_calls": [{"id": "call_1", "function": {"name": "fn_a", "arguments": "{}"}}]
}
```

Turn 2 request (include reasoning_content during active tool loop, strip for new question):
```json
[
  {"role": "user", "content": "Original question"},
  {"role": "assistant", "reasoning_content": "I need to call fn_a...", "content": null, "tool_calls": [...]},
  {"role": "tool", "tool_call_id": "call_1", "content": "tool result"}
]
```

**Rules**:
- INCLUDE `reasoning_content` in history while tool loop is in progress
- STRIP `reasoning_content` when starting a new user question (HTTP 400 otherwise)
- `enable_thinking=False` in `chat_template_kwargs` disables reasoning for simple tasks
- Context preservation: Qwen generates fresh CoT each turn; does NOT accumulate prior reasoning

**OpenAI o-series comparison**: OpenAI does NOT expose raw `reasoning_content` to API users.
They expose `reasoning_summary` (model-generated summary). Attempting to extract raw CoT
may violate their AUP. DeepSeek and Qwen both expose full raw `reasoning_content`.

### 1.6 MCP Integration

Qwen-Agent has first-class MCP support via `mcp_manager` singleton:

- **Three transport protocols**: stdio, SSE, streamable-http
- **Dynamic tool discovery**: tools discovered at runtime from connected servers
- **Naming convention**: `server_name-tool_name` avoids collisions
- **Async architecture**: MCP runs in daemon thread with own event loop, uses `asyncio.run_coroutine_threadsafe()` for cross-thread execution
- Install: `pip install -U "qwen-agent[gui,rag,code_interpreter,mcp]"`

Config structure:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-filesystem"],
      "env": {"ALLOWED_DIRS": "/data"}
    }
  }
}
```

#### 1.6.1 MCP Manager Singleton: Implementation Architecture

**Singleton pattern** (`MCPManager._instance` class variable, `__new__` method):
```python
class MCPManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized"):
            return  # guard against re-init on repeated MCPManager() calls
        self._initialized = True
        self.loop = asyncio.new_event_loop()
        self.loop_thread = threading.Thread(target=self.loop.run_forever, daemon=True)
        self.loop_thread.start()
        self.clients = {}   # client_id -> MCPClient
        self.processes = [] # subprocess handles for cleanup
        atexit.register(self._cleanup)
```

**Subprocess monkey-patching** (lines 57-71): For stdio-based MCP servers, the manager monkey-patches `subprocess.Popen` during server startup to intercept and record all spawned process handles. This ensures every child process is tracked in `self.processes` for coordinated cleanup on exit -- without this, orphaned server processes survive the Python process.

**Atexit cleanup sequence** (registered in `__init__`):
```python
def _cleanup(self):
    # 1. Gracefully close all MCPClient sessions (async, 1-second window)
    future = asyncio.run_coroutine_threadsafe(self._close_all_clients(), self.loop)
    try:
        future.result(timeout=1.0)
    except Exception:
        pass  # proceed to force-kill regardless
    # 2. Force-terminate remaining stdio subprocesses
    for proc in self.processes:
        try:
            proc.terminate()
        except Exception:
            pass
    # 3. Stop background event loop
    self.loop.call_soon_threadsafe(self.loop.stop)
    # 4. Wait for loop thread to fully exit
    self.loop_thread.join(timeout=5.0)
```

**Cross-thread execution via run_coroutine_threadsafe**:
```python
future = asyncio.run_coroutine_threadsafe(
    mcp_client.call_tool(tool_name, args),
    self.loop
)
result = future.result()  # blocks caller thread until coroutine completes
```

**Connection lifecycle**:
1. `connect()` -- initialize MCPClient based on transport type
   - `stdio` transport: triggered by `command` field in config (spawns subprocess)
   - `SSE` transport: triggered by `url` field (HTTP streaming)
   - `streamable-http`: triggered by `url` + `type == "streamable-http"`
2. `discover_tools()` -- query server for available tools, build registry
3. `call_tool()` -- submit via `run_coroutine_threadsafe`, block for result
4. `disconnect()` -- clean up connection and subprocess

**Automatic reconnection protocol**:
1. Ping session before each tool call
2. On ping failure: create new MCPClient with same ID
3. Reconnect using stored config parameters
4. Replace stale entry in `self.clients` dict
5. Retry original tool call on fresh connection
- SSE timeout: `sse_read_timeout` (default 300 seconds)

**Thread safety**: Singleton prevents race conditions on manager access. All async operations
isolated in daemon thread. `future.result()` synchronizes caller. No shared state mutation
outside the event loop thread.

### 1.7 LLM Backends

| Backend | Class | Use case |
|---------|-------|----------|
| DashScope (Alibaba Cloud) | `QwenChatAtDS` | Primary cloud API |
| OpenAI-compatible | `TextChatAtOAI` | vLLM, Ollama, any OpenAI-compat server |
| OpenVINO | `OpenVINO` | Intel local inference |
| Transformers | `Transformers` | HuggingFace local inference |

Config: `{"model": "qwen3-32b", "api_key": "...", "model_server": "http://localhost:11434/v1", "generate_cfg": {...}}`

`use_raw_api=True` enables vLLM native tool parsing instead of prompt-engineering-based function calling.

### 1.8 RAG Capabilities

Built into `Assistant` class:
1. Documents parsed/chunked by `DocParser`
2. Indexed via vector embeddings
3. Retrieved chunks prepended to system message
4. Handles documents up to 1M tokens

Memory agent for QwQ/QvQ/Qwen3 uses `qwen-turbo` with explicit `max_input_tokens: 30000`.

---

## 2. DeepSeek Tool-Calling

### 2.1 API Surface

OpenAI-compatible API at `https://api.deepseek.com`.

| Model ID | Mode | Context | Tool calls |
|----------|------|---------|------------|
| `deepseek-chat` | Non-thinking (V3.2) | 128K | Yes |
| `deepseek-reasoner` | Thinking (V3.2) | 128K | Yes |

Both model IDs point to DeepSeek-V3.2 (685B parameters, MoE, MIT license).

### 2.2 Standard Tool Call Flow (Non-Thinking)

Standard OpenAI-compatible flow:
1. Define tools in `tools` array (max 128 functions, name max 64 chars)
2. Send request with `tool_choice`: `auto` | `required` | `none` | `{"type":"function","function":{"name":"..."}}`
3. Response contains `message.tool_calls` array
4. Execute function, return `{"role":"tool","tool_call_id":"call_xxx","content":"result"}`
5. Send updated history for final answer

Supports **parallel tool calls** (multiple `tool_calls` in single response).

### 2.3 Thinking-With-Tools (Unique to DeepSeek V3.2)

**The key innovation**: Previous reasoning models reason first, THEN execute tools. DeepSeek V3.2 reasons WHILE executing tools, maintaining chain-of-thought across multiple tool calls.

Enable via:
- Set model to `deepseek-reasoner`, OR
- Pass `extra_body={"thinking": {"type": "enabled"}}`

**Multi-turn flow within a single question**:
```
Turn 1.1: Model reasons -> emits reasoning_content + tool_calls
Turn 1.2: App executes tools -> returns results
Turn 1.3: Model continues reasoning with tool results -> may call more tools
Turn 1.N: Model outputs final content (no more tool_calls)
```

**Response message structure**:
```json
{
  "role": "assistant",
  "reasoning_content": "Let me check the exchange rate...",
  "content": null,
  "tool_calls": [{"id": "call_abc", "type": "function", "function": {"name": "lookup_fx_rate", "arguments": "{\"pair\":\"EUR/USD\"}"}}]
}
```

**Critical implementation rules**:
1. During active thinking+tool loop: INCLUDE `reasoning_content` when appending assistant message (append `response.choices[0].message` directly)
2. For new user questions: REMOVE old `reasoning_content` from prior turns (API returns 400 error if `reasoning_content` appears in input)
3. Max tokens: 64K including reasoning content

#### 2.3.1 DeepSeek reasoning_content Lifecycle: Complete Message Sequence

**Within a single question (tool loop in progress)**:
```python
# Turn 1: model returns tool call with reasoning
resp = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "What is EUR/USD rate?"}],
    tools=[...]
)
# resp.choices[0].message has: reasoning_content + tool_calls + content=None

# Turn 2: pass back the FULL assistant message including reasoning_content
messages = [
    {"role": "user", "content": "What is EUR/USD rate?"},
    resp.choices[0].message,  # includes reasoning_content -- REQUIRED during loop
    {"role": "tool", "tool_call_id": "call_abc", "content": "1.0842"}
]
resp2 = client.chat.completions.create(model="deepseek-reasoner", messages=messages, tools=[...])
# resp2.choices[0].message.content = final answer (no more tool_calls)
```

**Starting a new question (strip old reasoning)**:
```python
# WRONG -- 400 error: reasoning_content in input for new question
messages = [
    {"role": "user", "content": "Previous question"},
    {"role": "assistant", "reasoning_content": "...", "content": "Previous answer"},
    {"role": "user", "content": "New question"}  # 400 if prior msg has reasoning_content
]

# CORRECT -- strip reasoning_content from prior assistant turns
messages = [
    {"role": "user", "content": "Previous question"},
    {"role": "assistant", "content": "Previous answer"},  # reasoning_content stripped
    {"role": "user", "content": "New question"}
]
```

**Error when mishandled**: HTTP 400: "Missing `reasoning_content` field in the assistant
message at message index [X]" OR HTTP 400 for unexpected `reasoning_content` in input.

#### 2.3.2 reasoning_content: Streaming, budget_tokens, and Token Limits

**Token limits**:
- Default max `reasoning_content` length: ~32K tokens
- Extended max: up to 64K tokens combined (reasoning + content)
- If `max_tokens` is too low, reasoning may be truncated and final answer omitted
- Recommended allocation: set `max_tokens` >= 8000 for tool-calling scenarios

**budget_tokens parameter** (source: api-docs.deepseek.com/api-reference):
- Controls how many tokens the model may allocate to the reasoning phase
- Acts as a soft ceiling within the overall `max_tokens` budget
- If set too low, reasoning is abbreviated -- acceptable for simple questions, risky for complex chains
- If unset, the model manages allocation automatically (proportional to inferred task complexity)
- Practical guidance: `budget_tokens` ~70% of `max_tokens` for balanced reasoning+answer

**Streaming `reasoning_content`** (source: api-docs.deepseek.com/guides/reasoning_model):
```python
with client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    stream=True,
    stream_options={"include_usage": True}  # required to get usage stats in final chunk
) as stream:
    for chunk in stream:
        delta = chunk.choices[0].delta if chunk.choices else None
        if delta and delta.reasoning_content:
            print(f"[thinking] {delta.reasoning_content}", end="", flush=True)
        if delta and delta.content:
            print(f"[answer] {delta.content}", end="", flush=True)
        if chunk.usage:  # final streaming chunk only
            print(f"\nTotal tokens: {chunk.usage.total_tokens}")
```

**Note**: Without `stream_options={"include_usage": True}`, the final usage summary chunk
is suppressed. Usage data (prompt_tokens, completion_tokens, total_tokens) is unavailable
in mid-stream deltas -- it only arrives in the terminal chunk.

### 2.4 Strict Mode (Beta)

Base URL: `https://api.deepseek.com/beta`

Set `"strict": true` on function definitions. Enforces JSON Schema compliance:
- Supported types: object, string, number, integer, boolean, array, enum, anyOf, $ref, $def
- ALL object properties must be in `required`
- `additionalProperties` must be `false`
- `pattern` and `format` supported for strings
- `minLength`/`maxLength` NOT supported

#### 2.4.1 Strict Mode: Full JSON Schema Support Matrix

**Enabling strict mode** (beta endpoint required):
```python
client = OpenAI(base_url="https://api.deepseek.com/beta", api_key="...")
tools = [{
    "type": "function",
    "function": {
        "strict": True,        # enable strict validation
        "name": "get_weather",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "pattern": "^[A-Z][a-z]+$"},
                "format": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["city", "format"],    # ALL properties must be listed
            "additionalProperties": False       # REQUIRED in strict mode
        }
    }
}]
```

**Full support matrix**:

| JSON Schema Feature | Strict Supported | Notes |
|--------------------|-----------------|-------|
| `object` | Yes | Must declare all props in `required` + `additionalProperties: false` |
| `string` | Yes | Base type |
| `number` | Yes | Supports `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `multipleOf` |
| `integer` | Yes | Same numeric constraints as number |
| `boolean` | Yes | Standard |
| `array` | Yes | `minItems`/`maxItems` NOT supported |
| `enum` | Yes | Restricts to predefined values |
| `anyOf` | Yes | Multiple valid type alternatives |
| `$ref` | Yes | Reusable schema module references |
| `$def` | Yes | Recursive structure definitions |
| `pattern` (string regex) | Yes | Validated at inference time |
| `format` (string) | Yes | email, hostname, ipv4, ipv6, uuid |
| `minLength` / `maxLength` | **No** | Not supported |
| `minItems` / `maxItems` | **No** | Not supported |
| `additionalProperties: true` | **No** | Must be false |

**Error format**: HTTP 400 returned if schema does not conform or uses unsupported features.
Server validates schema at request time, not at generation time.

**Performance**: Strict mode adds inference-time schema validation overhead but guarantees
100% compliance with declared schema -- eliminates post-processing validation failures.

### 2.5 Agentic Training Pipeline

V3.2 introduced massive agent training data synthesis (source: arXiv 2512.02556):
- **1,827 distinct environments** (not just "1,800+")
- **85,000+ complex instructions** across 4 agent categories
- Improved tool-use compliance and generalization across all task types

#### 2.5.1 Training Data Breakdown by Category

| Category | Count | Source Method |
|----------|-------|--------------|
| Code Agent | 24,667 | GitHub issue-PR pairs, filtered by heuristics + LLM judgment |
| Search Agent | 50,275 | Multi-agent pipeline sampling long-tail entities across domains |
| Code Interpreter | 5,908 | Jupyter Notebook environments (math, logic, data science) |
| General Agent | 4,417 | Synthesized from 1,827 task-oriented environments |
| **Total** | **85,267** | |

**Code Agent**: Built from millions of GitHub issue-PR pairs. Each environment requires
executable setup with dependency resolution and test validation.

**Search Agent**: Multi-language, multi-difficulty. QA pairs verified through search tool
validation. Largest category (59% of training data).

**Code Interpreter**: Jupyter-based environments focused on problems spanning mathematics,
logic, and data science. Iterative execution with output validation.

**General Agent**: "Hard to solve but easy to verify" task design. Categories include
travel planning, multi-step reasoning. Iterative difficulty escalation with human annotators
and verification agents ensuring data quality.

**Search agent verification pipeline** (5-stage hard-negative filtering):
1. Sample long-tail informative entities from large-scale web corpora
2. Question-construction agent explores entity using configurable search tools
3. Multiple answer-generation agents produce diverse candidate responses
4. Verification agent retains ONLY samples where: ground truth is correct AND all model-generated candidates are verifiably incorrect
5. Result: questions that are "hard to solve, easy to verify" -- oracle has answer, model cannot trivially succeed

**Code agent correctness filter** (zero-tolerance dual check):
```
ACCEPT if: patch produces non-zero false-to-positive tests (issue fixed)
REJECT if: any pass-to-fail tests (regression introduced)
# Both conditions enforced simultaneously -- correctness AND non-regression
```

**RL training (GRPO -- Group Relative Policy Optimization)**:
- Algorithm: GRPO (Group Relative Policy Optimization, DeepSeek's RL variant)
- Reward types: rule-based outcome rewards (code: tests pass/fail) + generative reward models (search: answer quality scoring)
- Design principle: all tasks must be "hard to solve, easy to verify" -- enables scalable RL without expensive human labeling at each step
- Unified training: reasoning + agentic tasks + human alignment in single RL stage (not separate phases)
- Cold-start: DeepSeek-V3 methodology used to unify reasoning and tool-use within single trajectories BEFORE full RL begins

**Training methodology**:
- All domains support both thinking and non-thinking modes simultaneously
- Six specialized training domains: mathematics, programming, general logical reasoning,
  general agentic tasks, agentic coding, agentic search
- Post-training: over 10% of pre-training compute dedicated to reinforcement learning
- Key innovation: reasoning integrated INTO tool execution (not sequential think-then-act)

### 2.6 Model Architecture (V3.2)

| Spec | Value |
|------|-------|
| Parameters | 685B (MoE) |
| Context window | 128K tokens |
| Tokenizer | Byte-level BPE, 128K vocabulary |
| Attention | DeepSeek Sparse Attention (DSA) |
| Tensor types | BF16, F8_E4M3, F32 |
| License | MIT |
| Chat template | Custom Python (`encoding_dsv32.py`), no Jinja |
| High-compute variant | V3.2-Speciale (surpasses GPT-5 on reasoning) |

**Note**: The 128K BPE vocabulary is confirmed from the V3 technical report. The 151K figure may refer to a different tokenizer variant or total special tokens count -- the official HuggingFace model card does not confirm 151K.

#### 2.6.1 V3.2-Speciale Benchmark Performance

V3.2-Speciale is the high-compute variant of DeepSeek-V3.2, unlocked by extended reasoning budget:

| Benchmark | Score | Context |
|-----------|-------|---------|
| IMO 2025 | Gold medal | International Mathematical Olympiad |
| IOI 2025 | Gold medal | International Olympiad in Informatics |
| Tau2Bench (agentic RL) | Significant gain over SFT-only | Airline + retail tool-use scenarios |
| MCP-Mark | Improved | Model Context Protocol tool-calling fidelity |
| MCP-Universe | Improved | Out-of-domain MCP tool generalization |
| SWE-bench Verified | SOTA (open-source) | Real-world GitHub issue repair |

**V3.2 vs V3 agentic benchmark** (Tau2Bench): RL-trained V3.2 substantially outperforms
V3 SFT-only baseline on held-out (not seen in training) agentic environments, demonstrating
that GRPO generalizes beyond training distribution -- not just memorization.
Source: arXiv 2512.02556, kili-technology.com/blog/data-story-deepseek-v3-2

**V3.2 vs competitors on coding agents** (SWE-bench):
- Outperforms all open-weight models
- Competitive with GPT-4o and Claude 3.5 Sonnet on code repair tasks
- V3.2-Speciale closes gap to GPT-5 on mathematical olympiad benchmarks

### 2.7 Unsupported Parameters in Reasoning Mode

Temperature, top_p, presence_penalty, frequency_penalty, logprobs, top_logprobs -- all silently ignored or error in reasoning mode. FIM (Fill-in-Middle) also unsupported.

---

## 3. Comparative Analysis

### 3.1 Tool-Calling Architecture Comparison

| Dimension | Qwen-Agent | DeepSeek API |
|-----------|-----------|--------------|
| Type | Full framework (like LangChain) | API-first (like OpenAI) |
| Tool definition | `BaseTool` class + `@register_tool` | JSON Schema in `tools` array |
| Max tools | Unlimited (registry) | 128 per request |
| Parallel calls | Yes (Hermes template) | Yes (multi tool_calls) |
| MCP support | Native (stdio/SSE/streamable-http) | None (API-only) |
| Code interpreter | Built-in (Docker + Jupyter) | Not available |
| Reasoning + tools | Separate `reasoning_content` field | Thinking-with-tools (interleaved) |
| RAG | Built-in (1M token docs) | Not available (BYO) |
| Local inference | Yes (vLLM, Ollama, OpenVINO, HF) | No (API only, or self-host 685B) |
| Agent loop | FnCallAgent (8 iterations max) | Client-side loop (no limit) |

### 3.2 Thinking + Tool Integration Models

| Aspect | Qwen3 | DeepSeek V3.2 |
|--------|-------|---------------|
| Thinking format | `<think>...</think>` in content, or separate `reasoning_content` | `reasoning_content` field always separate |
| Thinking during tools | Thinks before tool call, stops thinking, calls tool | Thinks WHILE calling tools (interleaved) |
| History handling | Must pass back `reasoning_content` | Must pass back during loop, strip for new question |
| Parser | Token ID 151668 (`</think>` tag) | API-managed (no client parsing) |
| Stopword risk | ReAct stopwords inside `<think>` cause issues | No risk (API handles parsing) |

### 3.3 Unique Concepts

| Concept | Source | Description |
|---------|--------|-------------|
| **Thinking-with-tools** | DeepSeek V3.2 | Reasoning interleaved with tool execution, not sequential |
| **Hermes template** | Qwen3 | XML-based function calling format avoiding ReAct stopword issues |
| **thought_in_content** | Qwen-Agent | Toggle: thinking in content field vs separate reasoning_content |
| **Strict mode** | DeepSeek beta | Schema-enforced tool argument validation |
| **Agent training synthesis** | DeepSeek V3.2 | 1800+ envs, 85K+ instructions for tool-use training data |
| **MCP daemon thread** | Qwen-Agent | Async MCP in background thread with cross-thread coroutine dispatch |
| **DeepSeek Sparse Attention** | DeepSeek V3.2 | Efficient attention for long-context tool-use scenarios |
| **MAX_LLM_CALL_PER_RUN** | Qwen-Agent | Hard cap at 8 LLM calls per agent run (prevents infinite loops) |
| **use_raw_api** | Qwen-Agent | Bypass prompt engineering, use vLLM native tool parsing directly |
| **GRPO** | DeepSeek V3.2 | Group Relative Policy Optimization -- RL unifying reasoning + agentic + alignment in single stage |
| **MCPManager `__new__`** | Qwen-Agent | Python singleton via `__new__` + `_initialized` guard + asyncio daemon + atexit cleanup |
| **subprocess monkey-patch** | Qwen-Agent | Intercepts all `Popen` calls during stdio MCP server startup for coordinated process cleanup |
| **Hard-to-solve, easy-to-verify** | DeepSeek V3.2 | Task design principle: scalable RL without per-step human evaluation |
| **vLLM token ID 9207 bug** | vLLM/Qwen3 | Hermes streaming parser truncates on special `}` token -- use non-streaming mode as workaround |

---

## 4. CEX Kind Mapping

| Qwen/DeepSeek Concept | CEX Kind | CEX Pillar | Notes |
|------------------------|----------|------------|-------|
| FnCallAgent / Assistant | `agent` | P02 | Agent with tool-calling capability |
| BaseTool / @register_tool | `function_def` | P04 | Tool definition with schema |
| Tool registry (TOOL_REGISTRY) | `toolkit` | P04 | Collection of registered tools |
| MCP server config | `mcp_server` | P04 | External tool via MCP protocol |
| Code Interpreter | `code_executor` | P04 | Sandboxed code execution |
| NousFnCallPrompt | `prompt_template` | P03 | Function calling prompt format |
| reasoning_content | No direct kind | P03 | Chain-of-thought field in message format |
| ReActChat | `agent` | P02 | Agent with ReAct reasoning pattern |
| Strict mode schema | `validation_schema` | P06 | JSON Schema enforcement on tool args |
| Agent training data | `eval_dataset` | P07 | 85K instructions for tool-use training |
| thinking-with-tools | `workflow` | P12 | Interleaved reasoning + tool execution pattern |
| tool_choice parameter | `dispatch_rule` | P12 | Controls when model invokes tools |
| DashScope / API backend | `model_provider` | P02 | LLM API provider configuration |
| RAG (Qwen-Agent) | `retriever_config` + `chunk_strategy` | P01 | Built-in retrieval pipeline |
| Memory component | `memory_scope` | P10 | Agent memory with file injection |

---

## 5. Integration Notes for CEX

### 5.1 Qwen-Agent as Local Builder Backend

Qwen-Agent can serve as a CEX nucleus backend when running Qwen3 locally via Ollama:
- Use `TextChatAtOAI` with `model_server: http://localhost:11434/v1`
- Enable `use_raw_api=True` for Ollama native tool parsing
- FnCallAgent loop (8 max) maps well to CEX 8F pipeline iterations
- MCP integration allows CEX tools to be exposed as MCP servers

### 5.2 DeepSeek as API Provider

DeepSeek fits CEX `model_provider` config:
- OpenAI-compatible API -- works with existing `cex_router.py`
- `deepseek-chat` for non-thinking tool calls (fast, cheap)
- `deepseek-reasoner` for thinking-with-tools (quality, expensive)
- 128 tool limit is sufficient for CEX (150 tools total)
- Strict mode useful for `validation_schema` enforcement

### 5.3 reasoning_content Handling

Both Qwen and DeepSeek require careful `reasoning_content` management:
- CEX message format should preserve `reasoning_content` in conversation history
- Strip on new user turn (DeepSeek) or risk 400 errors
- Qwen's `thought_in_content` toggle maps to CEX `generate_cfg` in provider config

### 5.4 Thinking-With-Tools for CEX Missions

DeepSeek's interleaved reasoning+tools pattern maps to CEX mission execution:
- F4 REASON can invoke F5 CALL tools mid-reasoning
- Multi-turn within single question = single 8F pass with tool calls
- The `while tool_calls` loop in client code mirrors FnCallAgent's iteration loop

---

## 6. Key Takeaways

1. **Qwen-Agent is a framework; DeepSeek is an API.** Different integration patterns for CEX.
2. **Thinking-with-tools** (DeepSeek) is architecturally distinct from think-then-act (everyone else). It allows reasoning to incorporate tool results before reaching conclusions.
3. **Hermes template** (Qwen3) solves the ReAct stopword problem -- use `--tool-call-parser hermes` for any Qwen3 deployment.
4. **reasoning_content** is a cross-ecosystem pattern (Qwen, DeepSeek, OpenAI o-series) that CEX must handle uniformly in its message format.
5. **MCP is Qwen-native, absent in DeepSeek.** For CEX, Qwen-Agent is the better local MCP bridge.
6. **128 tool limit** (DeepSeek) and **8 iteration limit** (Qwen FnCallAgent) are hard constraints that CEX dispatch must respect.
7. **V3.2-Speciale** claims GPT-5 level reasoning -- monitor for CEX nucleus routing as a high-compute option.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_function_def]] | sibling | 0.30 |
| [[p01_kc_agent]] | sibling | 0.29 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.29 |
| [[p01_kc_tool_use]] | sibling | 0.29 |
| [[p01_kc_terminology_openai_canonical]] | sibling | 0.28 |
| [[atom_16_minimax_kimi_glm]] | sibling | 0.26 |
| [[atom_11_agentscope]] | sibling | 0.25 |
| [[p01_kc_server_tools]] | sibling | 0.25 |
| [[p01_kc_openai_api_patterns]] | sibling | 0.25 |
| [[p03_pt_sdk_agent_builder]] | downstream | 0.24 |
