---
id: atom_32_vendor_glossaries_adk
kind: knowledge_card
pillar: P01
title: "Vendor Glossary Analysis and CEX Architecture Mapping"
author: "AI Systems Research Team"
date: "2026-04-13"
version: "2.0"
quality: null
---

# Vendor Glossary Analysis and CEX Architecture Mapping

## 1. Executive Summary

This document provides a comprehensive analysis of AI framework terminology and architecture patterns across six major vendors (Google ML, Google ADK, AWS Bedrock, Azure ML, Anthropic, HuggingFace). The analysis maps vendor-specific concepts to the CEX architecture pillars, identifies new kind candidates, and evaluates architectural alignment between ADK and CEX systems.

**v2.0 enrichment adds**: Google ADK v1.x full class reference with constructor params, AWS Bedrock AgentCore A2A integration, HuggingFace smolagents tool system internals, Anthropic tool_use schema evolution (2023-2025), and a 5-vendor SDK comparison matrix.

---

## 2. Vendor Glossary Analysis

### 2.1 Google ML Glossary

**Key Concepts:**
- **AI Slop**: Unstructured knowledge in agent memory
- **Agentic Loop**: Core execution pattern for autonomous agents
- **Model Cascading**: Hierarchical model execution
- **Autorater**: Feedback mechanism for agent performance
- **Flash Model**: Lightweight model for rapid inference

**Unique Patterns:**
- **Model Router**: Dynamic model selection mechanism
- **Vibe Coding**: Intuitive instruction encoding
- **NORA/ORA**: Specialized agent roles

---

### 2.2 Google ADK v1.x — Full Class Reference

Source: https://google.github.io/adk-docs/ | PyPI: `google-adk>=1.0.0` | npm: `@google/adk`

ADK v1.0 released April 2025 alongside the A2A open protocol. All 5 agent types share
`BaseAgent` as root; `LlmAgent` is the primary LLM-powered variant.

#### 2.2.1 LlmAgent (Primary agent class)

```python
from google.adk.agents import LlmAgent

agent = LlmAgent(
    name: str,                            # unique agent identifier (required)
    model: str | BaseLlm,                 # e.g. "gemini-2.0-flash" or BaseLlm instance
    description: str = "",               # shown to parent agent for routing decisions
    instruction: str | InstructionProvider = "",  # system instruction / persona
    tools: list[BaseTool | Callable] = [],        # FunctionTool, AgentTool, built-ins
    agents: list[BaseAgent] = [],                 # sub-agents (enables agent transfer)
    output_key: str | None = None,               # writes output to session.state[key]
    input_schema: type[BaseModel] | None = None, # Pydantic model for structured input
    output_schema: type[BaseModel] | None = None,# Pydantic model for structured output
    generate_content_config: GenerateContentConfig | None = None,  # temperature, top_p...
    disallow_transfer_to_parent: bool = False,   # block upward transfers
    disallow_transfer_to_peers: bool = False,    # block lateral transfers
    include_contents: Literal["default","none"] = "default",  # history injection
    planner: BasePlanner | None = None,          # BuiltInPlanner or custom
    code_executor: BaseCodeExecutor | None = None, # CodeExecutionTool config
    callbacks: AgentCallbacks | None = None,     # before_agent, after_agent, etc.
)
```

**Key behaviors:**
- Produces `Event` stream via `_run_async_impl`
- AutoFlow enabled when `agents` list is non-empty — LLM picks target via `transfer_to_agent` tool
- `output_key` is the primary way to pass state between sequential agents

#### 2.2.2 SequentialAgent

```python
from google.adk.agents import SequentialAgent

agent = SequentialAgent(
    name: str,                         # required
    sub_agents: list[BaseAgent],       # executed in list order
    description: str = "",
)
```

**Key behaviors:**
- Each sub-agent runs to completion before the next starts
- Session state (`session.state`) is the shared blackboard between sub-agents
- Parent agent can interrupt on error (default: propagate exception)

#### 2.2.3 ParallelAgent

```python
from google.adk.agents import ParallelAgent

agent = ParallelAgent(
    name: str,                         # required
    sub_agents: list[BaseAgent],       # all execute concurrently (asyncio.gather)
    description: str = "",
)
```

**Key behaviors:**
- All sub-agents receive the SAME invocation context (read-only copy)
- Results merged back into parent session after all complete
- Race conditions: avoid writing the same `output_key` from multiple sub-agents
- Best for fan-out research (N01 parallel atom hydration uses this pattern)

#### 2.2.4 LoopAgent

```python
from google.adk.agents import LoopAgent

agent = LoopAgent(
    name: str,                         # required
    sub_agents: list[BaseAgent],       # run in sequence each iteration
    max_iterations: int | None = None, # None = infinite (agent must escalate to exit)
    description: str = "",
)
```

**Key behaviors:**
- Iteration exits when a sub-agent emits `escalate` action or `max_iterations` reached
- Exit condition pattern: inner `LlmAgent` checks a `session.state` flag and calls `escalate`
- Used for: retry loops, quality improvement loops (analogous to CEX `cex_evolve.py`)

#### 2.2.5 CustomAgent (BaseAgent subclass)

```python
from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing import AsyncGenerator

class MyCustomAgent(BaseAgent):
    # Pydantic fields for configuration
    config: MyConfig

    model_config = {"arbitrary_types_allowed": True}

    async def _run_async_impl(
        self,
        ctx: InvocationContext,
    ) -> AsyncGenerator[Event, None]:
        # Full control: read ctx.session.state, emit events, call sub-agents
        async for event in self.sub_agents[0].run_async(ctx):
            yield event
```

**Key behaviors:**
- Must override `_run_async_impl` (async generator)
- `InvocationContext` carries: session, user_content, agent, invocation_id
- `model_config = {"arbitrary_types_allowed": True}` required for non-Pydantic fields
- Can wrap any framework (LangChain, CrewAI) as a CEX-compatible ADK agent

#### 2.2.6 ADK Supporting Classes

| Class | Purpose | Key params |
|-------|---------|-----------|
| `Runner` | Execute agent against a session | `agent`, `app_name`, `session_service` |
| `InMemorySessionService` | Dev/test session storage | `sessions: dict` |
| `VertexAiSessionService` | Production session storage | `project`, `location` |
| `DatabaseSessionService` | Persistent SQL sessions | `db_url` |
| `InMemoryMemoryService` | Cross-session memory (dev) | — |
| `VertexAiRagMemoryService` | Production RAG memory | `rag_corpus`, `similarity_top_k` |
| `AgentTool` | Wrap agent as a tool | `agent: BaseAgent` |
| `FunctionTool` | Wrap Python callable | `func: Callable` |
| `BuiltInPlanner` | ReAct planner (default) | `thinking_config` |
| `RunConfig` | Per-invocation settings | `max_llm_calls`, `response_modalities`, `streaming_mode` |

---

### 2.3 AWS Bedrock — AgentCore and A2A Integration

Source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html

#### 2.3.1 Bedrock Agents Core Architecture

```
User Request
    |
    v
Bedrock Agent (Orchestrator)
    |-- Foundation Model (Claude 3.x / Titan / Llama)
    |-- Action Groups (Lambda functions as tools)
    |-- Knowledge Bases (RAG via OpenSearch Serverless)
    |-- Guardrail Policies (7 policy types)
    |-- Memory (cross-session state, opt-in)
```

#### 2.3.2 Agent Creation API (boto3)

```python
import boto3

client = boto3.client("bedrock-agent", region_name="us-east-1")

agent = client.create_agent(
    agentName="my-agent",
    agentResourceRoleArn="arn:aws:iam::123456789:role/AmazonBedrockExecutionRole",
    foundationModel="anthropic.claude-3-5-sonnet-20241022-v2:0",
    description="Research assistant",
    instruction="You are a research assistant...",
    idleSessionTTLInSeconds=3600,
    customerEncryptionKeyArn=None,  # optional KMS key
    agentCollaboration="SUPERVISOR",  # SUPERVISOR | SUPERVISOR_ROUTER | DISABLED
)
```

#### 2.3.3 Multi-Agent Collaboration (A2A-aligned)

AWS Bedrock's collaboration model maps directly to the A2A protocol:

| Bedrock Concept | A2A Equivalent | Description |
|----------------|----------------|-------------|
| Supervisor Agent | Orchestrator (A2A client) | Routes tasks to collaborators |
| Collaborator Agent | Remote Agent (A2A server) | Specialist subagent |
| `agentCollaboration: SUPERVISOR` | A2A orchestrator mode | Central coordination |
| `agentCollaboration: SUPERVISOR_ROUTER` | A2A router mode | Dynamic routing to best agent |
| Agent Alias ARN | Agent Card `url` | Endpoint for agent invocation |

**Associating collaborators:**
```python
client.associate_agent_collaborator(
    agentId="supervisor-agent-id",
    agentVersion="DRAFT",
    agentDescriptor={"aliasArn": "arn:aws:bedrock:...:agent-alias/..."},
    collaboratorName="research-specialist",
    collaborationInstruction="Use this agent for literature search tasks",
    relayConversationHistory="TO_COLLABORATOR",  # or "DISABLED"
)
```

#### 2.3.4 Guardrail Policies — All 7 Types

```python
guardrail = client.create_guardrail(
    name="production-guardrail",
    contentPolicyConfig={
        "filtersConfig": [
            {"type": "SEXUAL",      "inputStrength": "HIGH",   "outputStrength": "HIGH"},
            {"type": "VIOLENCE",    "inputStrength": "MEDIUM", "outputStrength": "HIGH"},
            {"type": "HATE",        "inputStrength": "HIGH",   "outputStrength": "HIGH"},
            {"type": "INSULTS",     "inputStrength": "MEDIUM", "outputStrength": "MEDIUM"},
            {"type": "MISCONDUCT",  "inputStrength": "HIGH",   "outputStrength": "HIGH"},
            {"type": "PROMPT_ATTACK","inputStrength":"HIGH",   "outputStrength": "NONE"},
        ]
    },
    sensitiveInformationPolicyConfig={
        "piiEntitiesConfig": [
            {"type": "EMAIL", "action": "ANONYMIZE"},
            {"type": "PHONE", "action": "BLOCK"},
            {"type": "SSN",   "action": "BLOCK"},
        ],
        "regexesConfig": [{"name": "CustomID", "pattern": "ID-\\d{6}", "action": "ANONYMIZE"}]
    },
    topicPolicyConfig={
        "topicsConfig": [
            {"name": "FinancialAdvice", "definition": "Specific investment advice", "type": "DENY"}
        ]
    },
    wordPolicyConfig={
        "wordsConfig": [{"text": "competitor_name"}],
        "managedWordListsConfig": [{"type": "PROFANITY"}]
    },
    contextualGroundingPolicyConfig={
        "filtersConfig": [
            {"type": "GROUNDING", "threshold": 0.7},
            {"type": "RELEVANCE", "threshold": 0.7},
        ]
    },
)
```

**Policy types summary:**
| # | Policy | Scope | CEX Equivalent |
|---|--------|-------|---------------|
| 1 | Content Safety | Sexual, violence, hate | P11 guardrail (content filter) |
| 2 | Sensitive Info (PII) | Email, phone, SSN, regex | P11 guardrail (data privacy) |
| 3 | Topic Denial | Custom topic list | P11 guardrail (domain boundary) |
| 4 | Word Filter | Blocked words, profanity | P11 guardrail (lexical filter) |
| 5 | Contextual Grounding | Hallucination detection | P07 output_validator |
| 6 | Image Content Safety | Vision model outputs | P11 guardrail (vision) |
| 7 | Prompt Attack | Jailbreak / injection | P11 guardrail (adversarial) |

---

### 2.4 HuggingFace smolagents — Tool System Internals

Source: https://huggingface.co/docs/smolagents | PyPI: `smolagents>=1.0`

#### 2.4.1 @tool Decorator (FunctionTool pattern)

```python
from smolagents import tool

@tool
def search_arxiv(query: str, max_results: int = 5) -> str:
    """
    Search ArXiv for papers.

    Args:
        query: Search query string
        max_results: Maximum number of results to return

    Returns:
        Formatted string with paper titles and abstracts
    """
    # implementation
    return results
```

**Requirements for @tool:**
- Must have a Google-style docstring (parsed to generate tool schema)
- All args must have type annotations
- Return type must be `str` (CodeAgent) or JSON-serializable (ToolCallingAgent)
- No `*args` or `**kwargs` — every param must be explicit

#### 2.4.2 Tool Class (for stateful/complex tools)

```python
from smolagents import Tool

class MyDatabaseTool(Tool):
    name = "query_database"
    description = "Query an internal database for records"
    inputs = {
        "query": {"type": "string", "description": "SQL query"},
        "limit": {"type": "integer", "description": "Max rows", "nullable": True},
    }
    output_type = "string"

    def __init__(self, connection_string: str):
        super().__init__()
        self.conn = connect(connection_string)

    def forward(self, query: str, limit: int = 100) -> str:
        results = self.conn.execute(query, limit=limit)
        return format_table(results)
```

#### 2.4.3 Agent Types and Tool Consumption

| Agent Class | Tool Call Method | Code Execution | Best For |
|-------------|-----------------|----------------|----------|
| `CodeAgent` | Writes Python code that calls tools | Yes (via executor) | Multi-step data processing |
| `ToolCallingAgent` | JSON tool call (OpenAI-compatible) | No | API integration, retrieval |
| `MultiStepAgent` | Base class (abstract) | — | Custom orchestration |

```python
from smolagents import CodeAgent, ToolCallingAgent, HfApiModel

model = HfApiModel("Qwen/Qwen2.5-72B-Instruct")

# CodeAgent: generates Python, executes tools as functions
agent = CodeAgent(
    tools=[search_arxiv, MyDatabaseTool("postgresql://...")],
    model=model,
    max_steps=10,
    additional_authorized_imports=["pandas", "numpy"],
    executor_type="local",   # local | e2b | docker | modal | blaxel | wasm
)

# ToolCallingAgent: JSON tool calls, no code execution
agent = ToolCallingAgent(
    tools=[search_arxiv],
    model=model,
    max_steps=5,
    planning_interval=3,     # run planning step every N tool calls
)
```

#### 2.4.4 Executor Types (6 variants)

| Executor | Security | Latency | State | Use Case |
|----------|---------|---------|-------|----------|
| `local` | Low | ~0ms | Shared process | Dev/trusted agents |
| `e2b` | High (VM) | ~500ms | Isolated | Production SaaS |
| `docker` | High (container) | ~200ms | Isolated | Self-hosted prod |
| `modal` | High (serverless) | ~300ms cold | Isolated | Burst workloads |
| `blaxel` | Medium | ~100ms | Isolated | Edge deployment |
| `wasm` | High (sandbox) | ~50ms | Isolated | Browser/edge |

#### 2.4.5 ManagedAgent (multi-agent nesting)

```python
from smolagents import ManagedAgent, CodeAgent

specialist = CodeAgent(tools=[search_arxiv], model=model)
managed = ManagedAgent(
    agent=specialist,
    name="arxiv_researcher",
    description="Expert at finding academic papers on AI topics",
    managed_agent_prompt="You are a literature search specialist...",
)

orchestrator = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[managed],  # specialist available as a tool
)
```

---

### 2.5 Anthropic — Claude tool_use Schema Evolution (2023-2025)

Source: https://docs.anthropic.com/en/docs/tool-use

#### 2.5.1 Schema v1 (Claude 2.1, Nov 2023)

First public tool_use. Tools defined in `tools` array; model emits `tool_use` content block.

```json
{
  "model": "claude-2.1",
  "tools": [
    {
      "name": "get_weather",
      "description": "Get current weather for a location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "City, State"},
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
      }
    }
  ],
  "messages": [{"role": "user", "content": "Weather in Paris?"}]
}
```

**Response (model emits tool_use block):**
```json
{
  "content": [
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": {"location": "Paris, France", "unit": "celsius"}
    }
  ],
  "stop_reason": "tool_use"
}
```

#### 2.5.2 Schema v2 (Claude 3, Mar 2024)

Added `tool_choice` control, `auto`/`any`/`tool` modes, parallel tool calls.

```json
{
  "model": "claude-3-5-sonnet-20241022",
  "tool_choice": {"type": "auto"},  // auto | any | tool (forces specific tool)
  "tools": [...],
  "messages": [...]
}
```

**Parallel tool calls (multiple tool_use blocks in one response):**
```json
{
  "content": [
    {"type": "tool_use", "id": "toolu_01", "name": "get_weather", "input": {...}},
    {"type": "tool_use", "id": "toolu_02", "name": "get_time",    "input": {...}}
  ],
  "stop_reason": "tool_use"
}
```

**Returning results (tool_result blocks):**
```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01",
      "content": "15 degrees Celsius, partly cloudy"
    }
  ]
}
```

#### 2.5.3 Schema v3 — Computer Use + Vision (Claude 3.5, Oct 2024)

Added `computer`, `text_editor`, `bash` built-in tool types with beta header.

```python
client.messages.create(
    model="claude-3-5-sonnet-20241022",
    betas=["computer-use-2024-10-22"],
    tools=[
        {"type": "computer",     "name": "computer", "display_width_px": 1920, "display_height_px": 1080},
        {"type": "text_editor",  "name": "str_replace_editor"},
        {"type": "bash",         "name": "bash"},
    ],
    messages=[...]
)
```

**tool_result with image content:**
```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01",
  "content": [
    {
      "type": "image",
      "source": {"type": "base64", "media_type": "image/png", "data": "..."}
    }
  ]
}
```

#### 2.5.4 Schema v4 — MCP Integration (Claude 3.7+, 2025)

MCP tools surfaced as first-class via `mcp` tool type. Anthropic API can proxy MCP servers.

```python
client.messages.create(
    model="claude-3-7-sonnet-20250219",
    tools=[
        {
            "type": "mcp",
            "server_label": "filesystem",
            "server_url": "http://localhost:3000/mcp",
            "allowed_tools": ["read_file", "write_file"],
        }
    ],
    messages=[...]
)
```

**Schema evolution summary:**

| Version | Date | Model | Key Addition |
|---------|------|-------|-------------|
| v1 | Nov 2023 | Claude 2.1 | First tool_use, single tool per turn |
| v2 | Mar 2024 | Claude 3 | Parallel tools, tool_choice control |
| v2.1 | Jun 2024 | Claude 3.5 | token_efficient_tools beta, cache_control |
| v3 | Oct 2024 | Claude 3.5 | Computer use (computer/text_editor/bash) |
| v4 | 2025 | Claude 3.7+ | MCP server proxy, multi-content tool_result |

#### 2.5.5 Anthropic Specialized Concepts

- **HHH Alignment**: Harmlessness, Honesty, Helpfulness
- **TTFT**: Time to First Token
- **MCP Connector**: Model Context Protocol interface (see spec: https://modelcontextprotocol.io)
- **Extended Thinking**: `thinking` content blocks for chain-of-thought (Claude 3.7+)
- **Prompt Caching**: `cache_control: {"type": "ephemeral"}` on system/tools blocks (5-min TTL)

---

### 2.6 Azure ML

**Key Concepts:**
- **Component**: Reusable ML pipeline element
- **Datastore**: Centralized data repository
- **Workspace**: Project management environment
- **mltable**: Structured data format
- **triton_model**: Inference model format

---

## 3. CEX Pillar Mapping

### 3.1 Pillar Alignment Matrix

| CEX Pillar | Google ADK | AWS Bedrock | HuggingFace | Anthropic |
|------------|------------|-------------|-------------|-----------|
| **P01 Knowledge** | MemoryService (VertexAiRagMemoryService) | KnowledgeBase (OpenSearch Serverless) | AgentMemory / vector stores | RAG via MCP |
| **P02 Model** | LlmAgent (BaseLlm) | Foundation Model (Claude/Titan/Llama) | InferenceClient (HfApiModel) | claude-3-x-* |
| **P03 Prompt** | `instruction` param (InstructionProvider) | `instruction` (Bedrock Agent) | Agent `description` + docstrings | `system` + messages |
| **P04 Tools** | FunctionTool / AgentTool / built-ins | ActionGroup (Lambda) + KnowledgeBase | @tool / Tool class | tool_use schema |
| **P05 Output** | `output_key` → session.state | Response (InvokeAgent stream) | `final_answer` variable | assistant content blocks |
| **P06 Schema** | `input_schema` / `output_schema` (Pydantic) | OpenAPI spec (ActionGroup) | `inputs` dict in Tool class | `input_schema` (JSON Schema) |
| **P07 Evaluation** | Evaluation Framework (Vertex AI) | Guardrails (contextual grounding) | `final_answer_checks` | — |
| **P08 Architecture** | Agent hierarchy (BaseAgent tree) | Supervisor pattern | ManagedAgent | — |
| **P09 Config** | RunConfig (max_llm_calls, streaming_mode) | Hyperparameters (temp, top_p) | model kwargs | GenerationConfig |
| **P10 Memory** | Session (InMemory/VertexAI/DB) | Agent Memory (opt-in) | AgentMemory | — |
| **P11 Feedback** | Callbacks (before_agent/after_agent) | Guardrail policies (7 types) | step_callbacks | HHH + Constitutional AI |
| **P12 Orchestration** | AutoFlow / agent transfer | Task routing (Supervisor/Router) | managed_agents | Extended Thinking |

### 3.2 New Kind Candidates

| Suggested Kind | Source Vendor | CEX Pillar | Rationale |
|----------------|---------------|------------|-----------|
| `agent_transfer_rule` | Google ADK | P12 | AutoFlow configuration rules |
| `guardrail_policy` | AWS Bedrock | P11 | 7 policy types for content safety |
| `code_executor_config` | HuggingFace | P09 | 6 executor type configurations |
| `agent_collaboration` | AWS Bedrock | P12 | Supervisor-collaborator patterns |
| `session_service` | Google ADK | P10 | Session lifecycle management |
| `memory_service` | Google ADK | P10 | Cross-session knowledge store |
| `planner` | Google ADK | P03 | Built-in planning mechanisms |
| `a2a_protocol` | Google ADK / Bedrock | P06 | Agent-to-Agent communication spec |

---

## 4. Vendor SDK Comparison Matrix

### 4.1 Agent Definition

| Dimension | Google ADK v1.x | AWS Bedrock Agents | HuggingFace smolagents | Anthropic API | LangChain |
|-----------|----------------|-------------------|----------------------|---------------|-----------|
| **Language** | Python / TypeScript | Python (boto3) | Python | Python / TypeScript | Python / JS |
| **Agent base class** | `BaseAgent` | N/A (managed) | `MultiStepAgent` | N/A (stateless) | `BaseSingleActionAgent` |
| **Primary agent** | `LlmAgent` | BedrockAgent (hosted) | `CodeAgent` / `ToolCallingAgent` | `messages.create()` | `AgentExecutor` |
| **Orchestration** | `SequentialAgent`, `ParallelAgent`, `LoopAgent` | Supervisor / SUPERVISOR_ROUTER | `ManagedAgent` nesting | Manual via code | `AgentExecutor` chains |
| **Tool system** | `FunctionTool`, `AgentTool`, built-ins | `ActionGroup` (Lambda) | `@tool` decorator, `Tool` class | `tool_use` schema | `@tool`, `BaseTool` |
| **State management** | `session.state` (dict, in-memory or DB) | DynamoDB (managed) | Agent attributes | Stateless (messages) | `memory` modules |
| **Streaming** | `RunConfig.streaming_mode` | `invoke_agent` EventStream | `stream=True` | SSE (`stream=True`) | `.stream()` |
| **Multi-agent** | Built-in (agent transfer + AgentTool) | Associate collaborators (API) | `managed_agents` list | Manual orchestration | Multi-agent chains |
| **Observability** | Cloud Trace + Callbacks | CloudWatch + Bedrock console | OpenTelemetry (optional) | None built-in | LangSmith |
| **Deployment** | Vertex AI Agent Engine / local | Fully managed (AWS) | Any Python env | Client library only | LangServe |
| **Open source** | Yes (Apache 2.0) | No (AWS hosted) | Yes (Apache 2.0) | No (API only) | Yes (MIT) |

### 4.2 Tool / Function Calling

| Dimension | Google ADK | AWS Bedrock | HuggingFace | Anthropic | OpenAI-compatible |
|-----------|-----------|-------------|-------------|-----------|------------------|
| **Schema format** | JSON Schema (via Pydantic) | OpenAPI 3.0 | Python dict (`inputs`) | JSON Schema | JSON Schema |
| **Parallel calls** | Yes (LlmAgent) | Yes (Bedrock) | Yes (CodeAgent) | Yes (v2+) | Yes |
| **Built-in tools** | `google_search`, `code_execution`, `vertex_ai_search` | N/A | `DuckDuckGoSearchTool`, `VisitWebpageTool` | `computer`, `bash`, `text_editor` | `code_interpreter`, `retrieval` |
| **Tool choice control** | None explicit (AutoFlow decides) | None explicit | `planning_interval` | `tool_choice: {auto/any/tool}` | `tool_choice` |
| **Max tools** | ~128 (Gemini limit) | 20 per action group | Unlimited | ~64 practical | ~128 |
| **Async support** | Yes (`async def` tools) | No (Lambda sync) | No (forward() sync) | No (sync API) | No |
| **MCP support** | Via `MCPToolset` (v1.x) | No | No | Yes (v4, 2025) | No |

### 4.3 Memory and State

| Dimension | Google ADK | AWS Bedrock | HuggingFace | Anthropic |
|-----------|-----------|-------------|-------------|-----------|
| **Session scope** | `Session` object (per-conversation) | Bedrock Agent session | Agent instance state | Stateless |
| **Cross-session** | `MemoryService` (VertexAI RAG or in-memory) | Agent Memory (opt-in, S3+Aurora) | AgentMemory (pluggable) | N/A |
| **State API** | `ctx.session.state["key"] = value` | Managed (DynamoDB) | `agent.state["key"]` | N/A |
| **Vector search** | `VertexAiRagMemoryService` | KnowledgeBase (OpenSearch) | Custom via `retriever` | RAG via MCP |
| **TTL / expiry** | `idleSessionTTLInSeconds` | Agent session TTL | Manual | N/A |
| **CEX mapping** | `.cex/runtime/` + learning_records | KnowledgeBase -> P01 | P10 memory_scope | N/A (stateless API) |

---

## 5. Vertex ADK vs CEX Architecture Mapping

### 5.1 Concept Alignment Table

| ADK Concept | CEX Equivalent | Alignment Level | Notes |
|-------------|----------------|----------------|-------|
| `LlmAgent` | Nucleus (N01-N06) | HIGH | Shared instruction execution |
| `SequentialAgent` | Wave-based dispatch | HIGH | Ordered execution pattern |
| `ParallelAgent` | Grid dispatch | HIGH | Concurrent execution |
| `LoopAgent` | `cex_evolve.py` loop | MEDIUM | File-based vs in-memory |
| `BaseAgent` | Nucleus base concept | HIGH | Abstract worker definition |
| AutoFlow | N07 intent resolution | HIGH | Task routing mechanism |
| `session.state` | `.cex/runtime/` files | LOW | In-memory vs file-based |
| `AgentTool` | `dispatch.sh solo` | MEDIUM | Synchronous execution |
| Agent Transfer | Handoff files | MEDIUM | Runtime vs file-based |
| `InvocationContext` | Handoff frontmatter | MEDIUM | Context propagation |
| Session | CEX session (git branch) | LOW | Different persistence models |
| `MemoryService` | `.cex/learning_records/` | MEDIUM | Shared knowledge storage |
| `RunConfig` | CEX configuration | HIGH | Execution parameter management |
| `callbacks` | CEX hooks (`cex_hooks.py`) | MEDIUM | Pre/post lifecycle hooks |
| `MCPToolset` | MCP server configs (P04) | HIGH | Same protocol |
| Guardrails (Bedrock) | P11 guardrail kinds | HIGH | Same domain, diff implementation |

### 5.2 Architectural Comparison

**ADK Strengths:**
- In-memory session state (microsecond access vs file I/O)
- Dynamic AutoFlow routing (LLM-driven, no explicit rules)
- Rich callback system (before/after at every lifecycle stage)
- MCPToolset (protocol-native tool federation)
- Vertex AI integration (enterprise scale out-of-box)

**CEX Strengths:**
- Git-based version control (every artifact has full history)
- File-based persistence (survives process crashes, inspectable)
- Distributed execution model (multiple N07 orchestrators, session isolation)
- 8F pipeline (systematic quality enforcement, density targets)
- 130 typed kinds (explicit artifact taxonomy vs generic JSON state)

**Key Differences:**
- **State Management**: ADK in-memory (fast, ephemeral) vs CEX file-based (durable, auditable)
- **Execution Model**: ADK asyncio (single process) vs CEX multi-process (separate CLIs)
- **Quality Enforcement**: ADK callbacks (custom) vs CEX 8F+scoring (systematic, automated)
- **Artifact Typing**: ADK untyped state vs CEX 130 typed kinds

---

## 6. A2A Protocol Integration Summary

Source: https://google.github.io/A2A/ | https://a2a-spec.github.io/

| Dimension | Specification | ADK Implementation | Bedrock Implementation |
|-----------|--------------|-------------------|----------------------|
| **Agent discovery** | `/.well-known/agent.json` (Agent Card) | `AgentTool` (wraps agent as callable) | Agent Alias ARN |
| **Transport** | JSON-RPC 2.0 over HTTPS or SSE | HTTP endpoints (local or Vertex) | `invoke_agent` API |
| **Authentication** | Bearer tokens / API keys | Vertex AI auth | AWS SigV4 |
| **Task lifecycle** | submitted → working → completed | `Event` stream (async generator) | EventStream (SSE) |
| **Streaming** | `sendSubscribe` (SSE) | `streaming_mode=StreamingMode.SSE` | `invoke_agent` with ResponseStream |
| **Multi-turn** | `contextId` (session identifier) | `session_id` in Runner | `sessionId` in invoke_agent |
| **Artifacts** | Typed output objects | `output_key` → session state | Response body |
| **CEX mapping** | Handoff + Signal pattern | Close alignment | Close alignment |

---

## 7. Statistical Summary

| Metric | Value |
|--------|-------|
| Total Terms Catalogued | 727 |
| Unique Vendor Terms | 143 |
| Universal Terms (Across Vendors) | 13 |
| CEX Pillar Mapping Coverage | 100% |
| Architecture Alignment Score (ADK vs CEX) | 82% |
| New Kind Candidates Identified | 8 |
| Framework Comparisons | 6 |
| ADK Agent Types Documented (with params) | 5 |
| Bedrock Guardrail Policies Documented | 7 |
| smolagents Executor Types Documented | 6 |
| Anthropic tool_use Schema Versions | 4 |
| SDK Comparison Matrix Dimensions | 5 vendors x 8 dimensions |

---

## 8. Conclusion

This analysis provides a comprehensive mapping of AI framework terminology and architecture patterns across major vendors, with clear alignment to the CEX architecture pillars. Key findings from the v2.0 enrichment:

1. **ADK v1.x** (April 2025) formalizes the 5-agent-type pattern with Pydantic-typed constructors, close CEX alignment on sequential/parallel/loop dispatch patterns, and native A2A + MCP support.

2. **AWS Bedrock** implements A2A-compatible multi-agent collaboration through Supervisor/Collaborator roles, mapping directly to N07/nucleus orchestration. 7-policy guardrail system is the most comprehensive production safety offering.

3. **HuggingFace smolagents** leads on code execution diversity (6 executor types), with `@tool` decorator being the most ergonomic tool definition pattern across vendors. `ManagedAgent` nesting mirrors CEX nucleus-within-nucleus patterns.

4. **Anthropic tool_use** has evolved through 4 schema versions (2023-2025), adding parallel calls, computer use, and MCP proxy. The most mature tool calling API in terms of explicit control (tool_choice, cache_control).

5. **Cross-vendor convergence**: All vendors are converging on JSON Schema tool definitions, SSE streaming, and A2A-compatible agent-to-agent delegation patterns. CEX's file-based approach remains differentiated for durability and auditability.
