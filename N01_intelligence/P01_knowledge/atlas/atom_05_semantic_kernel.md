---
id: atom_05_semantic_kernel
kind: knowledge_card
pillar: P01
domain: agentic_frameworks
title: "ATOM-05: Microsoft Semantic Kernel -- Full Vocabulary Atlas"
version: 2.0.0
date: 2026-04-13
quality: 8.8
tags: [semantic-kernel, microsoft, agent-framework, autogen, vocabulary, atlas, process-framework, mcp, vector-store]
sources:
  - https://learn.microsoft.com/en-us/semantic-kernel/overview/
  - https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel
  - https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/
  - https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/
  - https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/filters
  - https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-types/chat-completion-agent
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-types/assistant-agent
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-types/azure-ai-agent
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-types/responses-agent
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/process/process-framework
  - https://learn.microsoft.com/en-us/semantic-kernel/frameworks/process/examples/example-first-process
  - https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-mcp-plugins
  - https://github.com/microsoft/semantic-kernel
  - https://github.com/microsoft/semantic-kernel/blob/main/docs/decisions/0070-declarative-agent-schema.md
  - https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/
  - https://devblogs.microsoft.com/semantic-kernel/building-a-model-context-protocol-server-with-semantic-kernel/
  - https://cloudsummit.eu/blog/microsoft-agent-framework-production-ready-convergence-autogen-semantic-kernel
  - https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-roadmap-h1-2025-accelerating-agents-processes-and-integration/
related:
  - atom_07_llamaindex
  - atom_03_openai_agents_sdk
  - atom_11_agentscope
  - p09_lpt_landing_page_template
  - atom_09_autogen_ag2
  - p05_output_visual_report
  - bld_collaboration_ontology
  - bld_collaboration_connector
  - p01_kc_function_def
  - landing_page_petshop_crm
---

# ATOM-05: Microsoft Semantic Kernel -- Full Vocabulary Atlas

## 1. Framework Identity

| Property | Value |
|----------|-------|
| Name | Microsoft Semantic Kernel |
| GitHub Stars | ~27,700 (Apr 2026) |
| Languages | C#, Python, Java |
| License | MIT |
| First Release | 2023 |
| Current Status | Production (v1.x+), part of Microsoft Agent Framework |
| Parent Umbrella | Microsoft Agent Framework (Oct 2025 merger with AutoGen) |
| Positioning | Model-agnostic SDK for building, orchestrating, and deploying AI agents |

Semantic Kernel is a lightweight, open-source development kit that serves as enterprise-grade middleware
for integrating LLMs into applications. It provides the Kernel (DI container) at its center, with
Plugins, AI Services, Filters, Memory (Vector Stores), Agent Framework, and Process Framework as
the major subsystems. Microsoft and Fortune 500 companies use it in production.

---

## 2. Full Type Registry

### 2.1 Core Kernel

| Term | Type | Description |
|------|------|-------------|
| `Kernel` | Class | Central DI container managing all services and plugins. The hub of every SK app. |
| `Kernel.CreateBuilder()` | Factory | .NET builder pattern for configuring a Kernel before `.Build()`. |
| `Kernel.builder()` | Factory | Java builder pattern. |
| `KernelArguments` | Class | Parameter bag passed to functions and agents for execution settings. |
| `KernelPluginCollection` | Class | Collection of plugins registered with the kernel. |
| `KernelPluginFactory` | Class | Factory for creating `KernelPlugin` instances from objects, types, or OpenAPI specs. |
| `KernelPlugin` | Class | A named group of `KernelFunction`s exposed to the AI for orchestration. |
| `KernelFunction` | Class | Single callable unit within a plugin -- native code, prompt, or imported from OpenAPI/MCP. |
| `@kernel_function` | Decorator (Python) | Marks a method as a kernel function with description metadata. |
| `[KernelFunction]` | Attribute (C#) | Marks a method as a kernel function. |
| `@DefineKernelFunction` | Annotation (Java) | Java equivalent of `@kernel_function`. |
| `@KernelFunctionParameter` | Annotation (Java) | Metadata for function parameters in Java. |
| `[Description]` | Attribute (C#) | Semantic description for functions/parameters consumed by the LLM. |
| `FunctionChoiceBehavior` | Class | Controls how the LLM selects functions -- `Auto()`, `Required()`, `None()`. |
| `FunctionChoiceBehavior.Auto()` | Config | Lets the LLM autonomously decide which functions to call. |
| `FunctionCallContent` | Class | Represents a function call request from the LLM. |
| `FunctionResultContent` | Class | Represents the result of a function call returned to the LLM. |
| `FunctionResult` | Class | Wrapper for the result of a `KernelFunction` invocation. |
| `InvocationContext` | Class (Java) | Wraps invocation settings including `ToolCallBehavior` and return mode. |
| `InvocationReturnMode` | Enum (Java) | Controls what the agent returns -- e.g., `LAST_MESSAGE_ONLY`. |
| `ToolCallBehavior` | Class (Java) | Java equivalent of `FunctionChoiceBehavior`. |

### 2.2 AI Services

| Term | Type | Description |
|------|------|-------------|
| `IChatCompletionService` | Interface (C#) | Core service for chat-based inference. |
| `ChatCompletionService` | Interface (Java) | Java chat completion contract. |
| `AzureChatCompletion` | Connector | Azure OpenAI chat completion connector. |
| `OpenAIChatCompletion` | Connector | OpenAI direct API connector. |
| Text Generation | Service | Text completion (non-chat) service. |
| Embedding Generation | Service (Experimental) | Vector embedding generation. |
| Text-to-Image | Service (Experimental) | Image generation from text prompts. |
| Image-to-Text | Service (Experimental) | Image understanding / captioning. |
| Text-to-Audio | Service (Experimental) | TTS service. |
| Audio-to-Text | Service (Experimental) | STT / transcription service. |
| Realtime | Service (Experimental, Python only) | Real-time streaming audio/video. |
| Service Selector | Pattern | Logic for choosing among multiple registered AI services. |
| `serviceId` | Parameter | String identifier for targeting a specific service in multi-service kernels. |

### 2.3 Prompt Templates

| Term | Type | Description |
|------|------|-------------|
| `PromptTemplateConfig` | Class | Configuration: template text, format, input variables, execution settings. |
| `KernelPromptTemplate` | Class | Wraps a `PromptTemplateConfig` for rendering. |
| `HandlebarsPromptTemplate` | Class | Handlebars-based template renderer. |
| `InputVariable` | Class | Declares a named input with description, type, default, JSON schema. |
| `PromptExecutionSettings` | Class | Base execution settings (temperature, top_p, etc.). |
| `OpenAIPromptExecutionSettings` | Class | OpenAI-specific settings including `FunctionChoiceBehavior`. |
| `AzureChatPromptExecutionSettings` | Class | Azure-specific execution settings. |
| Template Formats | Enum-like | `"semantic-kernel"` (built-in), `"handlebars"`, `"jinja2"`, `"liquid"`. |
| `{{$variable}}` | Syntax | SK template variable interpolation. |
| `{{plugin.function}}` | Syntax | SK template function call. |

### 2.4 Chat History & Content

| Term | Type | Description |
|------|------|-------------|
| `ChatHistory` | Class | Ordered list of chat messages for multi-turn conversations. |
| `ChatMessageContent` | Class | Single message with role, content, and metadata. |
| `StreamingChatMessageContent` | Class | Streaming variant for token-by-token delivery. |
| `AuthorRole` | Enum | `User`, `Assistant`, `System`, `Tool`. |
| `AnnotationContent` | Class | Annotation items (e.g., Bing grounding links). |
| `StreamingAnnotationContent` | Class | Streaming variant of annotation content. |
| `AgentResponseItem<T>` | Class | Wraps agent response with thread context. |

### 2.5 Filters (Middleware Pipeline)

| Term | Type | Description |
|------|------|-------------|
| `IFunctionInvocationFilter` | Interface (C#) | Runs on every `KernelFunction` invocation -- logging, caching, error handling. |
| `IPromptRenderFilter` | Interface (C#) | Runs before prompt rendering -- PII redaction, semantic caching, prompt modification. |
| `IAutoFunctionInvocationFilter` | Interface (C#) | Runs during automatic function calling -- early termination, iteration control. |
| `FunctionInvocationContext` | Class | Context passed to function invocation filters. |
| `PromptRenderContext` | Class | Context passed to prompt render filters. |
| `AutoFunctionInvocationContext` | Class | Context for auto-function filters -- includes chat history, function list, iteration count. |
| `FilterTypes` | Enum (Python) | `FUNCTION_INVOCATION`, `PROMPT_RENDERING`, `AUTO_FUNCTION_INVOCATION`. |
| `context.Terminate` | Property | Set `true` to stop auto-function-calling loop. |
| `context.IsStreaming` | Property | Indicates streaming vs. non-streaming invocation mode. |
| `context.RenderedPrompt` | Property | The rendered prompt text (modifiable in prompt render filter). |
| `kernel.add_filter()` | Method (Python) | Registers a filter function with the kernel. |
| `@kernel.filter()` | Decorator (Python) | Decorator-based filter registration. |

### 2.6 Vector Store Connectors (Memory)

| Term | Type | Description |
|------|------|-------------|
| `VectorStore` | Abstract Class | Cross-collection operations: list names, get collections. |
| `VectorStoreCollection<TKey, TRecord>` | Abstract Class (C#) | Single collection: CRUD + vector search. Inherits `IVectorSearchable<TRecord>`. |
| `IVectorSearchable<TRecord>` | Interface (C#) | Vector search capability -- `SearchAsync()`. |
| `VectorSearchBase` | Class (Python) | Base for vector search with `VectorizedSearchMixin`, `VectorizableTextSearchMixin`. |
| `VectorizedSearch<Record>` | Interface (Java) | Vector search by embedding vector. |
| `VectorizableTextSearch<Record>` | Interface (Java) | Vector search by text (DB generates embedding). |
| `VectorStoreField` | Annotation (Python) | Marks model fields as `'key'`, `'data'`, or `'vector'`. |
| `[VectorStoreKey]` | Attribute (C#) | Marks the key field. |
| `[VectorStoreData]` | Attribute (C#) | Marks a data field. Options: `IsIndexed`, `IsFullTextIndexed`. |
| `[VectorStoreVector]` | Attribute (C#) | Marks a vector field with `Dimensions`, `DistanceFunction`, `IndexKind`. |
| `@VectorStoreRecordKey` | Annotation (Java) | Java key field marker. |
| `@VectorStoreRecordData` | Annotation (Java) | Java data field marker. |
| `@VectorStoreRecordVector` | Annotation (Java) | Java vector field marker. |
| `@vectorstoremodel` | Decorator (Python) | Marks a dataclass as a vector store model. |
| `DistanceFunction` | Enum | `CosineSimilarity`, `DotProduct`, `EuclideanDistance`, etc. |
| `IndexKind` | Enum | `Hnsw`, `Flat`, `IvfFlat`, etc. |
| `VectorStoreRecordDefinition` | Class | Alternative to annotations for schema definition. |
| `EnsureCollectionExistsAsync()` | Method | Creates collection if it does not exist. |
| `Upsert` / `Get` / `Delete` | Methods | Standard CRUD operations on records. |
| `SearchAsync` | Method | Perform vector similarity search. |
| `create_search_function()` | Method (Python) | Creates a kernel function from a vector collection for RAG. |

**Out-of-the-box connectors (status as of Apr 2026):**

| Connector | .NET Status | Python Status | Java Status | NuGet Package | Key Type |
|-----------|-------------|---------------|-------------|---------------|----------|
| Azure AI Search | GA | RC | Preview | `...Connectors.AzureAISearch` | `string` |
| Azure Cosmos DB MongoDB | Preview | Preview | -- | `...Connectors.AzureCosmosDBMongoDB` | `string` |
| Azure Cosmos DB NoSQL | Preview | Preview | -- | `...Connectors.AzureCosmosDBNoSQL` | `string` |
| Chroma | Preview | Preview | -- | `...Connectors.Chroma` | `string` |
| Elasticsearch | Preview | Preview | -- | `...Connectors.Elasticsearch` | `string` |
| Faiss | -- | Preview | -- | (Python only, in-process) | `int` |
| In-Memory / Volatile | Preview | RC | -- | `...Connectors.InMemory` | any |
| Milvus | Preview | Preview | -- | `...Connectors.Milvus` | `string` |
| MongoDB Atlas | Preview | Preview | -- | `...Connectors.MongoDB` | `string` |
| Pinecone | Preview | Preview | -- | `...Connectors.Pinecone` | `string` |
| Postgres + pgvector | Preview | RC | -- | `...Connectors.Postgres` | `string`/`long` |
| Qdrant | Preview | RC | -- | `...Connectors.Qdrant` | `Guid`/`ulong` |
| Redis | Preview | Preview | -- | `...Connectors.Redis` | `string` |
| SQL Server | Preview | -- | -- | `...Connectors.SqlServer` | `string` |
| SQLite | Preview | Preview | -- | `...Connectors.Sqlite` | `string` |
| Weaviate | Preview | Preview | -- | `...Connectors.Weaviate` | `Guid` |
| JDBC MySQL | -- | -- | Preview | `semantickernel-data-jdbc` | `string` |
| JDBC PostgreSQL | -- | -- | Preview | `semantickernel-data-jdbc` | `string` |

All package names are prefixed `Microsoft.SemanticKernel` and require `--prerelease` flag except Azure AI Search.

**Connection pattern -- C# (Qdrant example):**

```csharp
// Via VectorStore abstraction
var vectorStore = new QdrantVectorStore(new QdrantClient("localhost"), ownsClient: true);
var collection = vectorStore.GetCollection<ulong, Hotel>("skhotels");
await collection.EnsureCollectionExistsAsync();

// Via Kernel DI (recommended for app integration)
builder.Services.AddQdrantVectorStore("localhost");
```

**Connection pattern -- Python (collection-first):**

```python
from semantic_kernel.connectors.qdrant import QdrantCollection

collection = QdrantCollection[str, Hotel](
    record_type=Hotel,
    collection_name="skhotels",
    # host="localhost", port=6333  optional, defaults to localhost
)
await collection.ensure_collection_exists()
```

**Data model annotation schema -- field-level config:**

| C# Attribute | Python VectorStoreField arg | Description |
|---|---|---|
| `[VectorStoreKey]` | `VectorStoreField('key')` | Primary key |
| `[VectorStoreData(IsIndexed = true)]` | `VectorStoreField('data', is_filterable=True)` | Filterable data |
| `[VectorStoreData(IsFullTextIndexed = true)]` | `VectorStoreField('data', is_full_text_searchable=True)` | Full-text indexed |
| `[VectorStoreVector(Dimensions: N, DistanceFunction = X, IndexKind = Y)]` | `VectorStoreField('vector', dimensions=N, distance_function=X, index_kind=Y)` | Vector field |

**DistanceFunction values:** `CosineSimilarity`, `DotProduct`, `EuclideanDistance`, `ManhattanDistance`, `HammingDistance`

**IndexKind values:** `Hnsw`, `Flat`, `IvfFlat`, `DiskAnn`, `QuantizedFlat`

**Schema-without-annotations alternative (VectorStoreRecordDefinition -- C#):**

```csharp
var definition = new VectorStoreRecordDefinition
{
    Properties = new List<VectorStoreRecordProperty>
    {
        new VectorStoreRecordKeyProperty("HotelId", typeof(ulong)),
        new VectorStoreRecordDataProperty("HotelName", typeof(string)) { IsIndexed = true },
        new VectorStoreRecordVectorProperty("DescriptionEmbedding", typeof(ReadOnlyMemory<float>))
            { Dimensions = 1536, DistanceFunction = DistanceFunction.CosineSimilarity, IndexKind = IndexKind.Hnsw }
    }
};
var collection = vectorStore.GetCollection<ulong, Hotel>("skhotels", definition);
```

**RAG via create_search_function (Python):**

```python
collection.create_search_function(
    function_name="hotel_search",
    description="Search hotels by description",
    search_type="vector",           # or "keyword_hybrid"
    parameters=[...],               # KernelParameterMetadata list
    string_mapper=lambda x: f"{x.record.hotel_name}: {x.record.description}",
)
# Registers the function directly on the kernel for LLM function calling
kernel.add_plugin(collection, plugin_name="memory")
```

**Legacy memory stores** (deprecated, replaced by Vector Store abstraction):
`IMemoryStore`, `MemoryRecord`, `ISemanticTextMemory` -- superseded by `VectorStore` + `VectorStoreCollection`.

### 2.7 Enterprise Readiness

| Term | Description |
|------|-------------|
| Telemetry | OpenTelemetry integration for distributed tracing. |
| Hooks | Legacy event-based extensibility (replaced by Filters). |
| Filters | Primary middleware pipeline for security, logging, responsible AI. |
| Responsible AI | PII detection/redaction, content safety, prompt injection protection. |
| Semantic Caching | Cache LLM responses by semantic similarity using filters + vector stores. |

### 2.8 MCP Integration (Bidirectional Bridge)

SK is a bidirectional MCP bridge: it can act as an MCP **host** (consuming MCP servers as plugins) and as an MCP **server** (exposing SK functions to any MCP client).

#### Direction 1: MCP Server -> SK Plugin (Consuming MCP)

| Term | Type | Description |
|------|------|-------------|
| `MCPStdioPlugin` | Class (Python) | Connects to a local MCP server via subprocess stdio transport. |
| `MCPSsePlugin` | Class (Python) | Connects to a remote MCP server via SSE over HTTPS. |
| `MCPStreamableHttpPlugin` | Class (Python) | Connects via HTTP streaming (newer MCP transport). |
| `load_tools` | Option (bool) | Load tools from MCP server on connect (default: True). |
| `load_prompts` | Option (bool) | Load prompt templates from MCP server (default: True). |
| `request_timeout` | Option (float) | Per-request timeout in seconds for MCP calls. |

**Python -- import a local MCP server (stdio):**

```python
from semantic_kernel.connectors.mcp import MCPStdioPlugin

# pip install semantic-kernel[mcp]
async with MCPStdioPlugin(
    name="Github",
    description="Github Plugin",
    command="docker",
    args=["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"],
    env={"GITHUB_PERSONAL_ACCESS_TOKEN": "..."},
) as github_plugin:
    kernel.add_plugin(github_plugin)
```

**Python -- import a remote MCP server (SSE):**

```python
from semantic_kernel.connectors.mcp import MCPSsePlugin

async with MCPSsePlugin(
    name="RemoteTools",
    description="Remote MCP Tools",
    url="http://localhost:8080",
    load_prompts=False,     # skip if server has no prompts
    request_timeout=30.0,
) as remote_plugin:
    kernel.add_plugin(remote_plugin)
```

#### Direction 2: SK -> MCP Server (Exposing SK)

| Term | Type | Description |
|------|------|-------------|
| `.AddMcpServer()` | Extension (C#) | Registers SK functions as MCP tools in ASP.NET DI. |
| `.WithStdioServerTransport()` | Extension (C#) | Adds stdio transport (for Claude Desktop / local MCP clients). |
| `.WithTools(kernel)` | Extension (C#) | Exposes all kernel plugin functions as MCP tools. |
| `kernel.as_mcp_server()` | Method (Python) | Returns an MCP server instance exposing kernel functions. |

**C# -- expose SK plugins as MCP server:**

```csharp
// Register SK plugin
kernelBuilder.Plugins.AddFromType<DateTimeUtils>();
Kernel kernel = kernelBuilder.Build();

// Build MCP server
var builder = Host.CreateEmptyApplicationBuilder(settings: null);
builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()  // or .WithHttpTransport() for SSE
    .WithTools(kernel);           // all KernelFunctions become MCP Tools

await builder.Build().RunAsync();
```

**MCP Tool Schema Auto-generation:** `[KernelFunction]` + `[Description]` attributes are automatically converted to MCP Tool JSON Schema, enabling seamless discovery by any MCP host (Claude Desktop, Cursor, VS Code).

**Supported MCP transports:** `stdio` (local processes), `SSE` (HTTP server-sent events), `StreamableHttp` (newer streaming HTTP).

---

## 3. Agent Framework (Detailed)

### 3.1 Agent Types

| Agent Type | Class | Backend | Status |
|------------|-------|---------|--------|
| Chat Completion Agent | `ChatCompletionAgent` | Any chat completion service | Release Candidate |
| OpenAI Assistant Agent | `OpenAIAssistantAgent` | OpenAI Assistants API | Release Candidate |
| Azure Assistant Agent | `AzureAssistantAgent` | Azure OpenAI Assistants API | Release Candidate |
| Azure AI Agent | `AzureAIAgent` | Azure AI Agent Service (Foundry) | Experimental |
| OpenAI Responses Agent | `OpenAIResponsesAgent` | OpenAI Responses API | Experimental |
| Azure Responses Agent | `AzureResponsesAgent` | Azure OpenAI Responses API | Experimental |

### 3.2 Agent Core Abstractions

| Term | Type | Description |
|------|------|-------------|
| `Agent` | Base Class | Abstract base for all agents with `Id`, `Name`, `Instructions`. |
| `AgentThread` | Abstract | Thread abstraction for conversation state management. |
| `ChatHistoryAgentThread` | Class | Local in-memory thread for `ChatCompletionAgent`. |
| `OpenAIAssistantAgentThread` | Class | Remote thread backed by OpenAI Assistants API. |
| `AzureAIAgentThread` | Class | Thread backed by Azure AI Agent Service. |
| `AssistantAgentThread` | Class (Python) | Alias/convenience for OpenAI assistant threads. |
| `ResponsesAgentThread` | Class | Thread for Responses API with `previous_response_id` chaining. |
| `AgentRegistry` | Class | Factory for creating agents from declarative YAML specs. |
| `AgentResponseItem<T>` | Class | Response wrapper including thread reference. |
| `invoke()` | Method | Non-streaming agent invocation returning `AsyncIterable`. |
| `invoke_stream()` | Method | Streaming variant returning `AsyncIterable[StreamingChatMessageContent]`. |
| `get_response()` | Method (Python) | Convenience single-response method. |
| `on_intermediate_message` | Callback | Receives intermediate `FunctionCallContent`/`FunctionResultContent` during invocation. |

### 3.3 Agent Tools (AzureAIAgent)

| Tool | Class/Type | Description |
|------|-----------|-------------|
| Code Interpreter | `CodeInterpreterTool` / `CodeInterpreterToolDefinition` | Sandboxed Python execution. |
| File Search | `FileSearchTool` / `FileSearchToolDefinition` | RAG over uploaded files via vector stores. |
| OpenAPI | `OpenApiTool` / `OpenApiToolDefinition` | External API integration via OpenAPI spec. |
| Azure AI Search | `AzureAISearchTool` / `AzureAISearchToolDefinition` | Search over Azure AI Search indices. |
| Bing Grounding | `BingGroundingTool` | Web search grounding with citation annotations. |
| Azure Functions | Integration | Serverless function execution. |
| Kernel Plugins | `plugins=[...]` | SK plugins registered as agent tools. |

### 3.4 Agent Tools (OpenAIResponsesAgent)

| Tool | Description |
|------|-------------|
| Web Search | Built-in web search capability. |
| File Search | File-based RAG. |
| Computer Use | Experimental computer control tool. |
| Kernel Plugins | SK plugins as function tools. |

### 3.5 Declarative Agent Specs (Full YAML Schema)

Agents are defined in YAML and instantiated via `AgentRegistry.create_from_yaml()` (Python) or loaded via `AgentRegistry` factory (C#). Schema ADR: `docs/decisions/0070-declarative-agent-schema.md`.

**Top-level schema (all agent types):**

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `type` | string | No | `chat_completion_agent` | Agent type identifier |
| `name` | string | Yes | -- | Unique agent name/identifier |
| `description` | string | No | -- | Human-readable purpose description |
| `instructions` | string | No | -- | System prompt / behavior guidance |
| `model` | object | No | -- | Model configuration block |
| `tools` | list | No | `[]` | List of tools (for assistant-type agents) |
| `metadata` | object | No | `{}` | Arbitrary key-value pairs |

**`type` allowed values:**

| Value | Agent Class | Backend |
|-------|-------------|---------|
| `chat_completion_agent` | `ChatCompletionAgent` | Any IChatCompletionService |
| `openai_assistant` | `OpenAIAssistantAgent` | OpenAI Assistants API |
| `azure_assistant` | `AzureAssistantAgent` | Azure OpenAI Assistants API |
| `foundry_agent` | `AzureAIAgent` | Azure AI Foundry Agent Service |
| `openai_responses` | `OpenAIResponsesAgent` | OpenAI Responses API |
| `bedrock_agent` | `BedrockAgent` | Amazon Bedrock Agent Service |
| *(custom)* | (registered type) | via `@register_agent_type` decorator |

**`model` block schema:**

```yaml
model:
  id: gpt-4o-mini            # Model deployment name or model ID
  options:
    temperature: 0.4          # float 0.0-2.0
    top_p: 1.0                # float 0.0-1.0
    max_tokens: 2048          # int
    function_choice_behavior: # ChatCompletionAgent only
      type: auto              # auto | required | none
      functions:              # restrict to specific functions (optional)
        - PluginName.FunctionName
```

**ChatCompletionAgent -- minimal spec:**

```yaml
type: chat_completion_agent
name: Parrot
instructions: Repeat the user message in pirate voice.
```

**ChatCompletionAgent -- full spec with function restrictions:**

```yaml
name: RestaurantHost
description: Answers menu questions and takes reservations
model:
  id: gpt-4o-mini
  options:
    temperature: 0.4
    function_choice_behavior:
      type: auto
      functions:
        - MenuPlugin.GetSpecials
        - MenuPlugin.GetItemPrice
        - ReservationPlugin.BookTable
instructions: |
  You are a friendly restaurant host. Answer questions about the menu
  and help guests make reservations.
metadata:
  version: "1.2"
  owner: "restaurant-team"
```

**OpenAIAssistantAgent spec (tools as JSON schema strings):**

```yaml
name: DataAnalyst
type: openai_assistant
description: Analyzes CSV data files
model:
  id: gpt-4o
  options:
    temperature: 0.2
tools:
  - type: code_interpreter      # built-in tool
  - type: file_search           # built-in tool
  - type: function
    name: MenuPlugin-GetSpecials
    description: List today's menu specials
    parameters: '{"type":"object","properties":{},"required":[]}'
  - type: function
    name: MenuPlugin-GetItemPrice
    description: Get the price of a menu item
    parameters: '{"type":"object","properties":{"menuItem":{"type":"string","description":"The menu item name"}},"required":["menuItem"]}'
instructions: Analyze uploaded files and answer data questions.
```

**Registering custom agent types (Python):**

```python
from semantic_kernel.agents import register_agent_type, Agent

@register_agent_type("my_custom_agent")
class MyCustomAgent(Agent):
    ...

# Now usable in YAML:
# type: my_custom_agent
```

**Runtime instantiation:**

```python
from semantic_kernel.agents import AgentRegistry

agent = await AgentRegistry.create_from_yaml(
    yaml_str=open("agent_spec.yaml").read(),
    kernel=kernel,                    # kernel with pre-loaded plugins
)
# OR from file:
agent = await AgentRegistry.create_from_file("agent_spec.yaml", kernel=kernel)
```

**Key constraint:** Tools referenced in YAML must already exist as plugins in the `Kernel` instance at instantiation time. The loader does NOT create functions from spec -- it resolves by name.

---

## 4. Agent Orchestration Patterns

| Pattern | Class | Description |
|---------|-------|-------------|
| Concurrent | `ConcurrentOrchestration` | Broadcasts task to all agents; collects results independently. |
| Sequential | `SequentialOrchestration` | Passes output from one agent to the next in order. |
| Handoff | `HandoffOrchestration` | Dynamically passes control based on context or rules. |
| Group Chat | `GroupChatOrchestration` | All agents in a shared conversation with a group manager. |
| Magentic | `MagenticOrchestration` | Inspired by MagenticOne -- Orchestrator coordinates specialist workers. |

### Orchestration Infrastructure

| Term | Type | Description |
|------|------|-------------|
| `InProcessRuntime` | Class | In-process agent runtime for orchestration execution. |
| `OrchestrationResult<T>` | Class | Wrapper for orchestration output. |
| `runtime.start()` / `runtime.StartAsync()` | Method | Starts the orchestration runtime. |
| `runtime.stop_when_idle()` / `runtime.RunUntilIdleAsync()` | Method | Waits for all agents to complete. |
| `orchestration.invoke()` / `InvokeAsync()` | Method | Submits a task to the orchestration. |

### Legacy Multi-Agent (deprecated, replaced by orchestration)

| Term | Status | Description |
|------|--------|-------------|
| `AgentGroupChat` | Legacy | Group chat container for multi-agent collaboration. |
| `AgentChannel` | Legacy | Communication channel between agents. |
| `SelectionStrategy` | Legacy | Strategy for selecting next agent speaker. |
| `TerminationStrategy` | Legacy | Strategy for ending group chat. |

**Status**: Orchestration patterns are **Experimental**. All share a unified construction/invocation interface.

---

## 5. Process Framework (Full API Reference)

**Status**: Experimental as of Apr 2026. GA targeted Q2 2026. Subject to breaking changes.

### 5.1 Core Concepts

| Term | Type | Description |
|------|------|-------------|
| Process | Concept | A structured sequence of steps achieving a specific business goal. |
| Step | Concept | An activity with defined inputs/outputs. Must contain at least one `KernelFunction`. |
| Pattern | Concept | Sequence type: sequential, parallel, fan-in/fan-out, map-reduce. |
| Event | Concept | Triggers transitions between steps. Steps emit events; other steps listen for them. |
| State | Concept | Stateful steps persist data across invocations (checkpoint/restore). |

### 5.2 Type Registry

| Term | Type | Description |
|------|------|-------------|
| `KernelProcess` | Class | The built process object ready for execution. |
| `KernelProcessStep` | Class | Base for stateless steps. Subclass this and add `[KernelFunction]` methods. |
| `KernelProcessStep<TState>` | Generic Class (C#) | Base for stateful steps with typed state `TState`. |
| `KernelProcessStep[TState]` | Generic Class (Python) | Python stateful step base. |
| `KernelProcessStepState<TState>` | Class | Carries the persistent state into/out of `ActivateAsync`. |
| `KernelProcessStepContext` | Class | Injected into KernelFunctions -- allows manual event emission. |
| `ProcessBuilder` | Class | Fluent API for wiring steps and events. |
| `KernelProcessEvent` | Class | Event message with `Id` (string) and `Data` (any serializable object). |

### 5.3 ProcessBuilder API

| Method | Signature | Description |
|--------|-----------|-------------|
| `AddStepFromType<T>` (C#) | `-> ProcessStepBuilder` | Registers a step type; returns a builder handle. |
| `add_step` (Python) | `add_step(StepClass) -> ProcessStepBuilder` | Registers a step type. |
| `OnInputEvent` (C#) | `OnInputEvent(string id) -> ProcessStepEdgeBuilder` | Routes external events by ID into the process. |
| `on_input_event` (Python) | `on_input_event(id) -> ProcessStepEdgeBuilder` | Python equivalent. |
| `Build` / `build` | `-> KernelProcess` | Compiles the wired process into a runnable artifact. |

### 5.4 Step Edge Builder (Event Routing)

| Method | Description |
|--------|-------------|
| `SendEventTo(target)` / `send_event_to(target)` | Routes event data to a target step. |
| `OnFunctionResult()` / `on_function_result()` | Fires when a KernelFunction returns (captures return value). |
| `OnEvent(eventId)` / `on_event(eventId)` | Fires when a step manually emits a named event. |
| `function_name=` | Disambiguate target function when step has multiple KernelFunctions. |
| `parameter_name=` | Disambiguate target parameter when function has multiple inputs. |

### 5.5 Step State Management

Steps can be stateless (`KernelProcessStep`) or stateful (`KernelProcessStep<TState>`):

```csharp
// C# -- stateful step with persisted ChatHistory
public class GenerateDocumentationStep : KernelProcessStep<DocumentationState>
{
    private DocumentationState _state = new();

    // Called on step activation -- restore persisted state
    override public ValueTask ActivateAsync(KernelProcessStepState<DocumentationState> state)
    {
        this._state = state.State!;
        this._state.ChatHistory ??= new ChatHistory(systemPrompt);
        return base.ActivateAsync(state);
    }

    [KernelFunction]
    public async Task GenerateDocumentationAsync(
        Kernel kernel,
        KernelProcessStepContext context,   // injected -- enables EmitEventAsync
        string productInfo)
    {
        this._state.ChatHistory!.AddUserMessage(productInfo);
        var response = await kernel.GetRequiredService<IChatCompletionService>()
            .GetChatMessageContentAsync(this._state.ChatHistory!);
        await context.EmitEventAsync("DocumentationGenerated", response.Content);
    }
}
```

```python
# Python -- stateful step with pydantic model
class DocumentationState(BaseModel):
    chat_history: ChatHistory | None = None

class GenerateDocumentationStep(KernelProcessStep[DocumentationState]):
    state: DocumentationState = Field(default_factory=DocumentationState)

    async def activate(self, state: KernelProcessStepState[DocumentationState]):
        self.state = state.state
        if self.state.chat_history is None:
            self.state.chat_history = ChatHistory(system_message=system_prompt)

    @kernel_function
    async def generate_documentation(
        self,
        context: KernelProcessStepContext,   # injected
        product_info: str,
        kernel: Kernel                       # injected
    ) -> None:
        self.state.chat_history.add_user_message(product_info)
        response = await chat_service.get_chat_message_content(...)
        await context.emit_event(process_event="documentation_generated", data=str(response))
```

### 5.6 Process Execution

**C# (StartAsync):**

```csharp
var process = processBuilder.Build();
await process.StartAsync(
    kernel,
    new KernelProcessEvent { Id = "Start", Data = "Product Name" }
);
```

**Python (async context manager):**

```python
from semantic_kernel.processes.local_runtime import KernelProcessEvent, start

async with await start(
    process=kernel_process,
    kernel=kernel,
    initial_event=KernelProcessEvent(id="Start", data="Product Name"),
) as process_context:
    final_state = await process_context.get_state()
```

### 5.7 Supported Execution Patterns

| Pattern | Description |
|---------|-------------|
| Sequential | A -> B -> C (default; OnFunctionResult chain) |
| Parallel / Fan-Out | A -> [B, C, D] simultaneously (SendEventTo multiple targets) |
| Fan-In | [B, C, D] -> E (step waits for all upstream events) |
| Map-Reduce | Distribute over collection, aggregate results |
| Conditional | Step emits different events based on logic (OnEvent discrimination) |
| Loop / Retry | Step emits event back to itself or to an upstream step |
| Human-in-the-Loop | Process pauses; external event resumes it |

### 5.8 Deployment Options

| Option | Package | Description |
|--------|---------|-------------|
| Local (in-process) | `Microsoft.SemanticKernel.Process.LocalRuntime` v1.46.0-alpha | Default; runs in memory, no external dependencies |
| Dapr | `Microsoft.SemanticKernel.Process.Runtime.Dapr` v1.46.0-alpha | Distributed sidecar; enables cloud-scale stateful processes |
| Orleans | (experimental) | .NET Orleans actor model; cluster-based distributed execution |

**Python local runtime:**

```bash
pip install semantic-kernel==1.20.0   # includes processes support
```

### 5.9 Process Framework vs. Orchestration Patterns

| Dimension | Process Framework | Agent Orchestration Patterns |
|-----------|------------------|-----------------------------|
| Control flow | Code-defined step graph | Agent-runtime managed |
| State | Explicit per-step state + checkpointing | Thread-based conversation state |
| Trigger | External event (`KernelProcessEvent`) | Direct `invoke()` call |
| Cloud scale | Dapr / Orleans runtimes | InProcessRuntime only (Apr 2026) |
| Primary use | Business process automation | Multi-agent collaboration |
| Status | Experimental | Experimental |

---

## 6. AutoGen Merger -> Microsoft Agent Framework 1.0

### Timeline

| Date | Event |
|------|-------|
| May 2025 | Azure AI Foundry Agent Service GA (10,000+ orgs) |
| Oct 1, 2025 | Microsoft Agent Framework public preview -- merges AutoGen + Semantic Kernel |
| Oct 2025 | AutoGen enters maintenance mode (bug fixes only, no new features) |
| Q1 2026 | **Agent Framework 1.0 GA** (.NET + Python) -- stable APIs, long-term support |
| Q2 2026 | Process Framework GA target |

### Agent Framework 1.0 -- GA Features

| Feature | Status | Description |
|---------|--------|-------------|
| Single Agent + Service Connectors | GA | Core agent class with all provider connectors |
| Multi-agent orchestration (5 patterns) | GA | Sequential, Concurrent, Handoff, GroupChat, Magentic |
| Graph-based workflow engine | GA | Deterministic, repeatable, checkpointable processes |
| Declarative agents + workflows (YAML) | GA | `AgentRegistry.create_from_yaml()` |
| MCP tool discovery | GA | Import/export via MCPStdioPlugin, MCPStreamableHttpPlugin |
| Pluggable memory architecture | GA | Conversational history + key-value + vector retrieval |
| Middleware hooks | GA | Intercept and transform agent behavior |
| Checkpointing + hydration | GA | Long-running process resume from checkpoint |

### Agent Framework 1.0 -- Preview Features (not GA)

| Feature | Description |
|---------|-------------|
| DevUI | Browser-based local debugger for visualizing agent execution |
| Foundry Hosted Agent | Managed agents on Microsoft Foundry or Azure Durable Functions |
| Foundry Tools / Memory / Observability | Deep integration with managed Azure ecosystems |
| AG-UI / CopilotKit / ChatKit | Frontend adapters for streaming agent output |
| Skills | Reusable domain capability packages |
| GitHub Copilot SDK + Claude Code SDK | Agent harness integrations |
| A2A Protocol | Agent-to-Agent cross-runtime collaboration (announced, not released) |

### First-Party Model Connectors (1.0 GA)

| Provider | Connector |
|---------|-----------|
| Microsoft Azure OpenAI | `AzureChatCompletion` |
| OpenAI | `OpenAIChatCompletion` |
| Microsoft Foundry | `FoundryChatClient` |
| Anthropic Claude | First-party connector (added in 1.0) |
| Amazon Bedrock | `BedrockAgent` + connector |
| Google Gemini | First-party connector (added in 1.0) |
| Ollama (local) | First-party connector (added in 1.0) |

### Package Names (1.0)

| Language | Package | Class |
|----------|---------|-------|
| .NET | `Microsoft.Agents.AI` | `Agent` |
| .NET | `Microsoft.Agents.AI.OpenAI` (prerelease) | OpenAI adapter |
| Python | `agent-framework` (PyPI) | `Agent`, `FoundryChatClient` |

### What Came From Where

| From AutoGen | From Semantic Kernel |
|-------------|---------------------|
| Multi-agent orchestration patterns | Kernel (DI container) |
| Group chat collaboration | Plugin architecture |
| Dynamic workflow generation | AI service connectors |
| MagenticOne pattern (Orchestrator + specialists) | Thread-based state management |
| Event-driven multi-agent models | Enterprise integration (telemetry, filters) |
| Research-grade experimentation | Production-grade stability and SLAs |

### Vocabulary Migration Guide

| Old AutoGen Term | Old SK Term | Agent Framework 1.0 Term | Notes |
|-----------------|-------------|--------------------------|-------|
| `AssistantAgent` | -- | `ChatAgent` / `AzureAIAgent` | Depends on backend |
| `FunctionTool` | `KernelFunction` | `@ai_function` / `KernelFunction` | Both valid in SK path |
| Event-driven models | -- | Graph-based Workflow APIs | Process Framework |
| -- | `Kernel` | `Agent` abstraction | Kernel still exists under hood |
| -- | Plugins | Tools (MCP or OpenAPI) | Plugins also still valid in SK |
| Group chat | `AgentGroupChat` (legacy) | `GroupChatOrchestration` | Unified orchestration API |
| -- | Conversations / Memory | Agent Threads | `AgentThread` hierarchy |
| `UserProxyAgent` | -- | Human-in-the-loop callback | `on_intermediate_message` |
| `MultimodalConversableAgent` | -- | `ChatCompletionAgent` + multimodal service | Any multimodal IChatCompletionService |

### Migration Resources

- **SK -> Agent Framework migration guide**: Microsoft Learn (step-by-step)
- **AutoGen 0.2 -> Agent Framework migration guide**: walkthrough + analysis tool
- **AG2 fork**: community-maintained AutoGen 0.2 compatible fork (`autogen` / `pyautogen` on PyPI, 20K+ Discord members, independent roadmap)

### AG2 Community Fork

AG2 inherited from AutoGen 0.2:
- `autogen` and `pyautogen` PyPI package names
- 20,000+ member Discord community
- Backward compatibility with AutoGen 0.2 API surface
- Independent governance and roadmap (not Microsoft-controlled)

---

## 7. NuGet / PyPI Package Map

### .NET Packages

| Package | Contents |
|---------|----------|
| `Microsoft.SemanticKernel` | Core Kernel, plugins, services, prompts |
| `Microsoft.SemanticKernel.Agents.Abstractions` | Agent base abstractions |
| `Microsoft.SemanticKernel.Agents.Core` | `ChatCompletionAgent` |
| `Microsoft.SemanticKernel.Agents.OpenAI` | `OpenAIAssistantAgent` |
| `Microsoft.SemanticKernel.Agents.AzureAI` | `AzureAIAgent` |
| `Microsoft.SemanticKernel.Agents.Orchestration` | Orchestration patterns |
| `Microsoft.SemanticKernel.Agents.Runtime.InProcess` | `InProcessRuntime` |
| `Microsoft.SemanticKernel.Connectors.OpenAI` | OpenAI connector |
| `Microsoft.SemanticKernel.Connectors.Qdrant` | Qdrant vector store |
| `Microsoft.Extensions.VectorData.Abstractions` | Vector Store abstractions |

### Python Package

| Package | Contents |
|---------|----------|
| `semantic-kernel` | Everything: Kernel, agents, connectors, vector stores, orchestration |
| `semantic_kernel.agents` | All agent types and orchestration |
| `semantic_kernel.connectors.ai.open_ai` | OpenAI/Azure OpenAI connectors |
| `semantic_kernel.data.vector` | Vector store abstractions |
| `semantic_kernel.functions` | `@kernel_function`, `KernelArguments` |
| `semantic_kernel.filters` | Filter types and contexts |
| `semantic_kernel.prompt_template` | Template config and rendering |
| `semantic_kernel.contents` | Chat content types |

### Java Packages

| Package | Contents |
|---------|----------|
| `semantickernel-api` | Core abstractions |
| `semantickernel-agents-core` | `ChatCompletionAgent` |
| `semantickernel-aiservices-openai` | OpenAI service integration |

---

## 8. Mapping to CEX Pillars

| CEX Pillar | SK Equivalent | Key Terms |
|------------|---------------|-----------|
| **P01 Knowledge** | Vector Store Connectors, Memory | `VectorStore`, `VectorStoreCollection`, RAG, embedding generation, `ISemanticTextMemory` (legacy) |
| **P02 Model** | AI Services, Kernel | `Kernel`, `IChatCompletionService`, service selectors, model connectors |
| **P03 Prompt** | Prompt Templates | `PromptTemplateConfig`, `KernelPromptTemplate`, `HandlebarsPromptTemplate`, template formats |
| **P04 Tools** | Plugins, MCP | `KernelPlugin`, `@kernel_function`, `kernel.as_mcp_server()`, OpenAPI imports |
| **P05 Output** | Agent Responses | `ChatMessageContent`, `StreamingChatMessageContent`, `AgentResponseItem` |
| **P06 Schema** | Data Models, Type Annotations | `VectorStoreField`, `[VectorStoreKey]`, `InputVariable`, JSON schema |
| **P07 Evaluation** | Filters, Quality | `IPromptRenderFilter`, `IAutoFunctionInvocationFilter`, content safety filters |
| **P08 Architecture** | Agent Framework | `Agent`, `AgentThread`, orchestration patterns, Process Framework |
| **P09 Config** | Execution Settings | `PromptExecutionSettings`, `KernelArguments`, service configuration, `serviceId` |
| **P10 Memory** | Vector Store + Chat History | `ChatHistory`, `VectorStoreCollection`, `AgentThread` (remote state) |
| **P11 Feedback** | Filters Pipeline | `IFunctionInvocationFilter`, semantic caching, retry filters, PII detection |
| **P12 Orchestration** | Agent Orchestration + Process Framework | `SequentialOrchestration`, `ConcurrentOrchestration`, `HandoffOrchestration`, `GroupChatOrchestration`, `MagenticOrchestration`, `InProcessRuntime` |

---

## 9. Complete Vocabulary Index (Alphabetical)

| Term | Category | First Appeared |
|------|----------|---------------|
| `Agent` | Agent Framework | 2024 |
| `AgentChannel` | Agent Framework (legacy) | 2024 |
| `AgentGroupChat` | Agent Framework (legacy) | 2024 |
| `AgentRegistry` | Agent Framework | 2025 |
| `AgentResponseItem<T>` | Agent Framework | 2025 |
| `AgentThread` | Agent Framework | 2025 |
| `AnnotationContent` | Content Types | 2025 |
| `AssistantAgentThread` | Agent Types | 2025 |
| `AuthorRole` | Content Types | 2023 |
| `AutoFunctionInvocationContext` | Filters | 2024 |
| `AzureAIAgent` | Agent Types | 2025 |
| `AzureAIAgentSettings` | Agent Config | 2025 |
| `AzureAIAgentThread` | Agent Types | 2025 |
| `AzureAISearchTool` | Agent Tools | 2025 |
| `AzureAssistantAgent` | Agent Types (Python) | 2024 |
| `AzureChatCompletion` | AI Services | 2023 |
| `AzureChatPromptExecutionSettings` | Prompt Config | 2023 |
| `AzureResponsesAgent` | Agent Types | 2025 |
| `BingGroundingTool` | Agent Tools | 2025 |
| `ChatCompletionAgent` | Agent Types | 2024 |
| `ChatHistory` | Content Types | 2023 |
| `ChatHistoryAgentThread` | Agent Types | 2025 |
| `ChatMessageContent` | Content Types | 2023 |
| `CodeInterpreterTool` | Agent Tools | 2024 |
| `ConcurrentOrchestration` | Orchestration | 2025 |
| `DistanceFunction` | Vector Store | 2024 |
| `FileSearchTool` | Agent Tools | 2024 |
| `FilterTypes` | Filters (Python) | 2024 |
| `FunctionCallContent` | Content Types | 2024 |
| `FunctionChoiceBehavior` | Kernel | 2024 |
| `FunctionInvocationContext` | Filters | 2024 |
| `FunctionResult` | Kernel | 2023 |
| `FunctionResultContent` | Content Types | 2024 |
| `GroupChatOrchestration` | Orchestration | 2025 |
| `HandlebarsPromptTemplate` | Prompt Templates | 2024 |
| `HandoffOrchestration` | Orchestration | 2025 |
| `IAutoFunctionInvocationFilter` | Filters (C#) | 2024 |
| `IChatCompletionService` | AI Services (C#) | 2023 |
| `IFunctionInvocationFilter` | Filters (C#) | 2024 |
| `IPromptRenderFilter` | Filters (C#) | 2024 |
| `IVectorSearchable<T>` | Vector Store (C#) | 2024 |
| `InProcessRuntime` | Orchestration | 2025 |
| `IndexKind` | Vector Store | 2024 |
| `InputVariable` | Prompt Templates | 2023 |
| `InvocationContext` | Kernel (Java) | 2024 |
| `Kernel` | Core | 2023 |
| `KernelArguments` | Core | 2023 |
| `KernelFunction` | Core | 2023 |
| `KernelPlugin` | Core | 2023 |
| `KernelPluginCollection` | Core | 2023 |
| `KernelPluginFactory` | Core | 2023 |
| `KernelProcess` | Process Framework | 2024 |
| `KernelProcessStep` | Process Framework | 2024 |
| `KernelPromptTemplate` | Prompt Templates | 2023 |
| `MagenticOrchestration` | Orchestration | 2025 |
| `OpenAIAssistantAgent` | Agent Types | 2024 |
| `OpenAIAssistantAgentThread` | Agent Types | 2025 |
| `OpenAIChatCompletion` | AI Services | 2023 |
| `OpenAIChatPromptExecutionSettings` | Prompt Config | 2023 |
| `OpenAIResponsesAgent` | Agent Types | 2025 |
| `OpenApiTool` | Agent Tools | 2025 |
| `OrchestrationResult<T>` | Orchestration | 2025 |
| `ProcessBuilder` | Process Framework | 2024 |
| `PromptExecutionSettings` | Prompt Config | 2023 |
| `PromptRenderContext` | Filters | 2024 |
| `PromptTemplateConfig` | Prompt Templates | 2023 |
| `ResponsesAgentThread` | Agent Types | 2025 |
| `SelectionStrategy` | Agent Framework (legacy) | 2024 |
| `SequentialOrchestration` | Orchestration | 2025 |
| `StreamingChatMessageContent` | Content Types | 2023 |
| `TerminationStrategy` | Agent Framework (legacy) | 2024 |
| `ToolCallBehavior` | Kernel (Java) | 2024 |
| `VectorStore` | Vector Store | 2024 |
| `VectorStoreCollection` | Vector Store | 2024 |
| `VectorStoreField` | Vector Store (Python) | 2024 |
| `VectorStoreRecordDefinition` | Vector Store | 2024 |
| `@kernel_function` | Core (Python) | 2023 |
| `@vectorstoremodel` | Vector Store (Python) | 2024 |
| `kernel.as_mcp_server()` | MCP Integration | 2025 |
| `KernelProcess` | Process Framework | 2024 |
| `KernelProcessEvent` | Process Framework | 2024 |
| `KernelProcessStep` | Process Framework | 2024 |
| `KernelProcessStep<TState>` | Process Framework | 2024 |
| `KernelProcessStepContext` | Process Framework | 2024 |
| `KernelProcessStepState<TState>` | Process Framework | 2024 |
| `MCPSsePlugin` | MCP Integration (Python) | 2025 |
| `MCPStdioPlugin` | MCP Integration (Python) | 2025 |
| `MCPStreamableHttpPlugin` | MCP Integration (Python) | 2025 |
| `ProcessBuilder` | Process Framework | 2024 |
| `@register_agent_type` | Agent Framework (Python) | 2025 |
| `.AddMcpServer()` | MCP Integration (.NET) | 2025 |
| `.WithStdioServerTransport()` | MCP Integration (.NET) | 2025 |
| `.WithTools(kernel)` | MCP Integration (.NET) | 2025 |

---

## 10. Key Design Principles

1. **Kernel as DI Container**: Everything flows through the Kernel -- services, plugins, filters. Lightweight, transient, model-agnostic.
2. **Plugin = Semantic Function Group**: Not just code -- plugins carry semantic descriptions for LLM function calling. Native, OpenAPI, and MCP sources.
3. **Filters = Middleware**: Three-layer pipeline (function invocation, prompt render, auto-function invocation) replaces old hooks. Enterprise security layer.
4. **Thread Abstraction**: Unified `AgentThread` interface hides backend differences (local, OpenAI, Azure, Responses API).
5. **Orchestration Patterns**: Technology-agnostic coordination (Sequential, Concurrent, Handoff, Group Chat, Magentic) with unified invoke interface.
6. **Vector Store Abstraction**: Model-first approach with annotations. Swap between 16+ database backends without code changes.
7. **Declarative Agents**: YAML specs for portable, auditable agent definitions. Runtime-resolved tools and plugins.
8. **MCP Native**: Bidirectional MCP -- export kernel as MCP server, import MCP servers as plugins.

---

## 11. Comparison: SK vs. CEX Architecture

| Aspect | Semantic Kernel | CEX |
|--------|----------------|-----|
| Central Hub | `Kernel` (DI container) | `N07` (Orchestrator nucleus) |
| Agent Definition | Agent classes + YAML specs | Builder ISOs (13 per kind) + agent cards |
| Plugin System | `KernelPlugin` + `@kernel_function` | Builders (126) + `_tools/*.py` (79) |
| Orchestration | 5 patterns (Concurrent, Sequential, Handoff, GroupChat, Magentic) | Grid dispatch + wave-based multi-nucleus |
| Memory | Vector Store Connectors (18+ backends) | `P10_memory/` + `cex_retriever.py` (TF-IDF) |
| Quality Gate | Filters pipeline | 8F F7 GOVERN (3-layer scoring) |
| Template System | PromptTemplateConfig (SK/Handlebars/Jinja2/Liquid) | Prompt Compiler (`p03_pc_cex_universal.md`) |
| Process Automation | Process Framework (Step/Process/Event) | 8F Pipeline (F1-F8) |
| State Management | AgentThread (local/remote) | `.cex/runtime/` (handoffs, signals, PIDs) |
| Middleware | 3 filter types | Pre/post hooks (`cex_hooks.py`) |
| Multi-Model | Service selector + multiple AI services | `nucleus_models.yaml` + `cex_router.py` |
| MCP Support | Native bidirectional (MCPStdioPlugin + .WithTools) | Via N05 tool integrations |
| Declarative Agents | YAML spec + AgentRegistry (7 types) | Handoff files + agent cards |
| Process Runtimes | Local + Dapr + Orleans | In-process only (single machine) |

---

## 12. Competitive Comparison: SK vs. LangChain vs. LlamaIndex

### Agent + Orchestration

| Dimension | Semantic Kernel | LangChain | LlamaIndex |
|-----------|----------------|-----------|------------|
| Primary language | C#, Python, Java | Python, JS | Python |
| Agent paradigm | Event-driven + typed steps | Chain-based / LCEL | Query pipeline + agents |
| Orchestration patterns | 5 named (Concurrent, Sequential, Handoff, GroupChat, Magentic) | LangGraph (graph-based) | Workflow (event-driven, similar to SK Process) |
| Process / workflow engine | Process Framework (Dapr/Orleans) | LangGraph Cloud (hosted) | LlamaIndex Workflow |
| Declarative agents | YAML via AgentRegistry | LangGraph human-in-loop / state machines | AgentRunner config |
| Human-in-the-loop | Process Framework pause/resume | LangGraph `interrupt()` | Query engine callbacks |
| Multi-agent | 5 orchestration classes | LangGraph multi-agent graphs | AgentWorkflow |

### Memory / Vector Store

| Dimension | Semantic Kernel | LangChain | LlamaIndex |
|-----------|----------------|-----------|------------|
| Vector store abstraction | Unified `VectorStore` + 18 connectors | 60+ vector store integrations | 40+ vector stores |
| Embedding generation | Via `IEmbeddingGenerationService` | Via `Embeddings` base class | Via `EmbedModel` |
| RAG approach | `IVectorSearchable` -> Text Search -> RAG | `VectorStoreRetriever` -> `RetrievalQA` | `VectorStoreIndex` -> `QueryEngine` |
| Memory types | Vector + Chat History + AgentThread | Buffer, Summary, Vector, Entity memories | Chat memory + vector index |
| Schema-first | Yes (annotations / record definition) | No (document-oriented) | No (node-oriented) |

### Enterprise Readiness

| Dimension | Semantic Kernel | LangChain | LlamaIndex |
|-----------|----------------|-----------|------------|
| Observability | OpenTelemetry native | LangSmith (proprietary) | LlamaTrace / Arize |
| Security middleware | 3 filter types (PII, content safety, semantic cache) | Custom callbacks | Callbacks only |
| MCP support | Native bidirectional (Apr 2026) | MCP via community packages | MCP via community packages |
| Multi-language | C# + Python + Java | Python + JS | Python only |
| Microsoft ecosystem | Deep (Azure OpenAI, Foundry, CosmosDB) | No native Azure integration | No native Azure integration |
| License | MIT | MIT | MIT |
| Production readiness | GA (1.0 Apr 2026) | GA (v0.3 stable) | GA (v0.12 stable) |

### When to Choose SK vs. Alternatives

| Choose SK when... | Choose LangChain when... | Choose LlamaIndex when... |
|-------------------|-------------------------|--------------------------|
| C# / .NET is your primary stack | Python-first, broad community | Document-heavy RAG is the core use case |
| Deep Azure / Microsoft integration needed | LangSmith observability is critical | Query pipeline composition is the primary pattern |
| Enterprise security filters are required | Maximum ecosystem breadth needed | Index abstraction over multiple data sources |
| Process Framework for business automation | LangGraph for stateful multi-agent graphs | Already using LlamaIndex's node/document model |
| Declarative YAML agent portability | Fast prototyping with minimal boilerplate | LlamaParse for complex PDF ingestion |

---

## 13. Package Installation Reference

### Install by feature (Python)

```bash
# Core SK
pip install semantic-kernel

# With MCP support
pip install semantic-kernel[mcp]

# Specific vector store extras
pip install semantic-kernel[qdrant]
pip install semantic-kernel[redis]
pip install semantic-kernel[chroma]
pip install semantic-kernel[pinecone]
pip install semantic-kernel[weaviate]
pip install semantic-kernel[azure_cosmos_db]

# Process Framework (included in main package)
# semantic_kernel.processes

# Agent Framework 1.0 (Microsoft Agent Framework)
pip install agent-framework
```

### Install by feature (.NET)

```bash
# Core
dotnet add package Microsoft.SemanticKernel

# Agents
dotnet add package Microsoft.SemanticKernel.Agents.Core
dotnet add package Microsoft.SemanticKernel.Agents.OpenAI
dotnet add package Microsoft.SemanticKernel.Agents.AzureAI
dotnet add package Microsoft.SemanticKernel.Agents.Orchestration
dotnet add package Microsoft.SemanticKernel.Agents.Runtime.InProcess

# Process Framework
dotnet add package Microsoft.SemanticKernel.Process.LocalRuntime --version 1.46.0-alpha
dotnet add package Microsoft.SemanticKernel.Process.Runtime.Dapr --version 1.46.0-alpha

# Vector Store abstractions
dotnet add package Microsoft.Extensions.VectorData.Abstractions

# Vector Store connectors (each separate, most need --prerelease)
dotnet add package Microsoft.SemanticKernel.Connectors.Qdrant --prerelease
dotnet add package Microsoft.SemanticKernel.Connectors.Postgres --prerelease
dotnet add package Microsoft.SemanticKernel.Connectors.AzureAISearch
dotnet add package Microsoft.SemanticKernel.Connectors.InMemory --prerelease

# MCP server (C# -- uses official MCP SDK)
dotnet add package ModelContextProtocol

# Agent Framework 1.0 (.NET)
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.OpenAI --prerelease
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_07_llamaindex]] | sibling | 0.22 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.22 |
| [[atom_11_agentscope]] | sibling | 0.20 |
| [[p09_lpt_landing_page_template]] | downstream | 0.19 |
| [[atom_09_autogen_ag2]] | sibling | 0.19 |
| [[p05_output_visual_report]] | downstream | 0.19 |
| [[bld_collaboration_ontology]] | downstream | 0.18 |
| [[bld_collaboration_connector]] | downstream | 0.18 |
| [[p01_kc_function_def]] | sibling | 0.18 |
| [[landing_page_petshop_crm]] | downstream | 0.17 |
