---
id: atom_15_qwen_deepseek
kind: knowledge_card
title: "Atomic Research 15: Qwen-Agent + DeepSeek Tool-Calling Specs"
version: "1.1.0"
quality: 8.9
tags: [qwen, deepseek, tool-calling, function-calling, mcp, reasoning, agent-framework, hermes, strict-mode, agentic-training]
pillar: P01
domain: llm-agent-tooling
density_score: 0.95
sources:
  - https://github.com/QwenLM/Qwen-Agent
  - https://api-docs.deepseek.com/guides/tool_calls
  - https://api-docs.deepseek.com/guides/thinking_mode
  - https://api-docs.deepseek.com/guides/reasoning_model
  - https://deepwiki.com/QwenLM/Qwen-Agent
  - https://deepwiki.com/QwenLM/Qwen-Agent/4.4-mcp-integration
  - https://deepwiki.com/QwenLM/Qwen3/4.3-function-calling-and-tool-use
  - https://chat-deep.ai/docs/deepseek-tool-calls/
  - https://api-docs.deepseek.com/news/news251201
  - https://huggingface.co/deepseek-ai/DeepSeek-V3.2
  - https://arxiv.org/abs/2512.02556
  - https://docs.vllm.ai/en/latest/features/tool_calling/
  - https://github.com/vllm-project/vllm/issues/19056
  - https://github.com/NousResearch/Hermes-Function-Calling
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

### 1.5 reasoning_content Field

For reasoning models (QwQ, QvQ, Qwen3), messages carry an optional `reasoning_content` field separate from `content`.

**thought_in_content parameter**:
- `True`: content = `<think>reasoning</think>answer` (single field)
- `False`: separate `reasoning_content` and `content` fields

**Critical**: When using function calling, the client MUST pass back `reasoning_content` in conversation history. Ignoring it (standard OpenAI format) causes severe output anomalies.

Token ID `151668` marks the closing `</think>` tag for parser detection.

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

### 2.4 Strict Mode (Beta)

Base URL: `https://api.deepseek.com/beta`

Set `"strict": true` on function definitions. Enforces JSON Schema compliance:
- Supported types: object, string, number, integer, boolean, array, enum, anyOf, $ref, $def
- ALL object properties must be in `required`
- `additionalProperties` must be `false`
- `pattern` and `format` supported for strings
- `minLength`/`maxLength` NOT supported

### 2.5 Agentic Training Pipeline

V3.2 introduced massive agent training data synthesis:
- 1,800+ environments
- 85,000+ complex instructions
- Improved tool-use compliance and generalization

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
- 128 tool limit is sufficient for CEX (79 tools total)
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
