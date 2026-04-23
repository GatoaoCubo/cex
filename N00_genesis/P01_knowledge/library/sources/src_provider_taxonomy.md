# Provider Official Taxonomy
> Sources: Official docs only | Scraped: 2026-03-29
> Method: WebFetch (firecrawl token unavailable — fallback to WebFetch)
> OpenAI: 403 blocked, populated from SDK training knowledge (accurate as of 2025)

---

## Anthropic (platform.claude.com / docs.anthropic.com)

### Tool Use

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `tool` | Tool Definition | /docs/en/agents-and-tools/tool-use | Object in the `tools` array defining a callable function (name, description, input_schema) |
| `tool_use` | Content Block | /docs/en/agents-and-tools/tool-use | Block type in Claude's response when invoking a tool; contains `id`, `name`, `input` |
| `tool_result` | Content Block | /docs/en/agents-and-tools/tool-use | Block sent by developer returning tool execution result to Claude; contains `tool_use_id`, `content` |
| `tool_choice` | Request Parameter | /docs/en/agents-and-tools/tool-use | Controls tool selection: `auto` (model decides), `any` (must use a tool), `tool` (specific tool), `none` (no tools) |
| `stop_reason` | Response Field | /docs/en/agents-and-tools/tool-use | Why generation stopped; value `"tool_use"` signals a pending tool call |
| `client tools` | Tool Category | /docs/en/agents-and-tools/tool-use | Tools whose code executes in the developer's application (user-defined + Anthropic-schema tools like bash, text_editor) |
| `server tools` | Tool Category | /docs/en/agents-and-tools/tool-use | Tools that execute on Anthropic's infrastructure; results returned directly without developer handling |
| `strict` | Tool Parameter | /docs/en/agents-and-tools/tool-use/strict-tool-use | Add to tool definition to guarantee schema conformance; ensures tool calls always match schema exactly |
| `web_search_20260209` | Server Tool Type | /docs/en/agents-and-tools/tool-use | Built-in server tool for web search; `{"type": "web_search_20260209", "name": "web_search"}` |
| `web_fetch` | Server Tool Type | /docs/en/agents-and-tools/tool-use | Built-in server tool for fetching web content |
| `code_execution` | Server Tool Type | /docs/en/agents-and-tools/tool-use | Built-in server tool for executing code on Anthropic infrastructure |
| `tool_search` | Server Tool Type | /docs/en/agents-and-tools/tool-use | Built-in server tool for searching tools |
| `input_schema` | Tool Field | /docs/en/agents-and-tools/tool-use | JSON Schema object defining expected parameters for a tool |
| `agentic loop` | Concept | /docs/en/agents-and-tools/tool-use | Cycle: Claude returns tool_use → developer executes → returns tool_result → repeat until done |
| `parallel_tool_use` | Behavior | /docs/en/agents-and-tools/tool-use | Claude can request multiple tool calls in a single response (multiple tool_use blocks) |

### Computer Use

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `computer_20251124` | Tool Type | /docs/en/build-with-claude/computer-use | Latest computer use tool; requires beta header `computer-use-2025-11-24`; supports Claude Opus 4.6, Sonnet 4.6, Opus 4.5 |
| `computer_20250124` | Tool Type | /docs/en/build-with-claude/computer-use | Previous computer use tool version; supports Claude 4 + Sonnet 3.7 |
| `text_editor_20250728` | Tool Type | /docs/en/build-with-claude/computer-use | Text editor tool; standard name `str_replace_based_edit_tool` |
| `bash_20250124` | Tool Type | /docs/en/build-with-claude/computer-use | Bash shell tool for command execution |
| `str_replace_based_edit_tool` | Tool Name | /docs/en/build-with-claude/computer-use | Canonical name for the text editor tool instance |
| `computer-use-2025-11-24` | Beta Header | /docs/en/build-with-claude/computer-use | Required `anthropic-beta` header value for latest computer use tools |
| `computer-use-2025-01-24` | Beta Header | /docs/en/build-with-claude/computer-use | Beta header for previous computer use tool version |
| `screenshot` | Action | /docs/en/build-with-claude/computer-use | Capture current display state — available in all tool versions |
| `left_click` | Action | /docs/en/build-with-claude/computer-use | Click at coordinates `[x, y]`; accepts `text` for modifier keys |
| `right_click` | Action | /docs/en/build-with-claude/computer-use | Right mouse button click; available in `computer_20250124`+ |
| `middle_click` | Action | /docs/en/build-with-claude/computer-use | Middle mouse button click |
| `double_click` | Action | /docs/en/build-with-claude/computer-use | Double click at coordinates |
| `triple_click` | Action | /docs/en/build-with-claude/computer-use | Triple click (e.g., select all text in field) |
| `type` | Action | /docs/en/build-with-claude/computer-use | Type a text string |
| `key` | Action | /docs/en/build-with-claude/computer-use | Press a key or key combination (e.g., "ctrl+s") |
| `mouse_move` | Action | /docs/en/build-with-claude/computer-use | Move cursor to coordinates without clicking |
| `left_click_drag` | Action | /docs/en/build-with-claude/computer-use | Click and drag between coordinates; `computer_20250124`+ |
| `scroll` | Action | /docs/en/build-with-claude/computer-use | Scroll with direction and amount; `computer_20250124`+ |
| `hold_key` | Action | /docs/en/build-with-claude/computer-use | Hold a key for specified duration (seconds); `computer_20250124`+ |
| `wait` | Action | /docs/en/build-with-claude/computer-use | Pause between actions; `computer_20250124`+ |
| `left_mouse_down` | Action | /docs/en/build-with-claude/computer-use | Fine-grained mouse press; `computer_20250124`+ |
| `left_mouse_up` | Action | /docs/en/build-with-claude/computer-use | Fine-grained mouse release; `computer_20250124`+ |
| `zoom` | Action | /docs/en/build-with-claude/computer-use | View a specific screen region at full resolution; `computer_20251124` only; requires `enable_zoom: true` |
| `display_width_px` | Tool Parameter | /docs/en/build-with-claude/computer-use | Required: display width in pixels |
| `display_height_px` | Tool Parameter | /docs/en/build-with-claude/computer-use | Required: display height in pixels |
| `enable_zoom` | Tool Parameter | /docs/en/build-with-claude/computer-use | Optional: enables zoom action on `computer_20251124` |

### Prompt Caching

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `cache_control` | Request Object | /docs/en/build-with-claude/prompt-caching | Object placed on content blocks to control caching behavior; `{"type": "ephemeral"}` or `{"type": "ephemeral", "ttl": "1h"}` |
| `ephemeral` | Cache Type | /docs/en/build-with-claude/prompt-caching | Currently the only supported cache_control type |
| `ttl` | Cache Parameter | /docs/en/build-with-claude/prompt-caching | Time-to-live for cached content: `"5m"` (default, 1.25x price) or `"1h"` (2x price) |
| `cache_creation_input_tokens` | Usage Field | /docs/en/build-with-claude/prompt-caching | Tokens written to cache (new cache creation); priced at 1.25x–2x base depending on TTL |
| `cache_read_input_tokens` | Usage Field | /docs/en/build-with-claude/prompt-caching | Tokens retrieved from existing cache; priced at 0.1x base |
| `input_tokens` | Usage Field | /docs/en/build-with-claude/prompt-caching | Tokens after last cache breakpoint (not cacheable); priced at base rate |
| `cache breakpoint` | Concept | /docs/en/build-with-claude/prompt-caching | Position in content marked with cache_control; max 4 per request |
| `ephemeral_5m_input_tokens` | Usage Sub-field | /docs/en/build-with-claude/prompt-caching | Tokens cached with 5m TTL (in `cache_creation` sub-object for 1h caching requests) |
| `ephemeral_1h_input_tokens` | Usage Sub-field | /docs/en/build-with-claude/prompt-caching | Tokens cached with 1h TTL (in `cache_creation` sub-object) |

---

## OpenAI (platform.openai.com)
> Note: Direct docs access returned 403. Data from SDK/API knowledge (training data, accurate as of 2025).

### Function Calling

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `function` | Tool Type | /docs/guides/function-calling | Legacy tool type (pre-2023); now wrapped in `tool` objects |
| `tool` | Request Object | /docs/guides/function-calling | Wrapper for a function definition: `{"type": "function", "function": {...}}` |
| `tool_choice` | Request Parameter | /docs/guides/function-calling | Controls selection: `"auto"`, `"none"`, `"required"`, or `{"type": "function", "function": {"name": "..."}}` |
| `tool_calls` | Response Field | /docs/guides/function-calling | Array in assistant message containing function invocations; each has `id`, `type`, `function` |
| `parallel_tool_calls` | Request Parameter | /docs/guides/function-calling | Boolean; enables model to call multiple functions simultaneously (default: true) |
| `name` | Function Field | /docs/guides/function-calling | Function identifier string |
| `description` | Function Field | /docs/guides/function-calling | Natural language description helping model decide when to call |
| `parameters` | Function Field | /docs/guides/function-calling | JSON Schema defining expected arguments |
| `strict` | Function Field | /docs/guides/function-calling | Boolean; enforces strict JSON Schema adherence in tool calls |
| `arguments` | Response Field | /docs/guides/function-calling | JSON string of arguments in a tool_call response |
| `tool_call_id` | Message Field | /docs/guides/function-calling | ID matching a tool_call; required in tool result messages |

### Structured Outputs

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `response_format` | Request Parameter | /docs/guides/structured-outputs | Object controlling output format: `{"type": "json_schema", "json_schema": {...}}` |
| `json_schema` | Format Type | /docs/guides/structured-outputs | Response format value specifying a JSON Schema for the output |
| `strict` | Schema Field | /docs/guides/structured-outputs | Boolean in json_schema; when true, guarantees schema compliance |
| `refusal` | Response Field | /docs/guides/structured-outputs | Field in parsed response when model refuses to generate structured output |
| `json_object` | Format Type | /docs/guides/structured-outputs | Older response_format type; guarantees valid JSON but no schema enforcement |

### Assistants API

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `Assistant` | Resource | /docs/assistants/overview | Persistent AI entity with instructions, model, and tools configured |
| `Thread` | Resource | /docs/assistants/overview | Conversation container holding messages; persists independently of runs |
| `Message` | Resource | /docs/assistants/overview | Individual message within a Thread; has role (user/assistant), content, attachments |
| `Run` | Resource | /docs/assistants/overview | Execution of an Assistant on a Thread; stateful lifecycle (queued → in_progress → completed) |
| `Run Step` | Resource | /docs/assistants/overview | Individual operation within a Run; types: `message_creation`, `tool_calls` |
| `code_interpreter` | Tool Type | /docs/assistants/overview | Built-in tool allowing Assistant to write and execute Python code in a sandbox |
| `file_search` | Tool Type | /docs/assistants/overview | Built-in tool enabling retrieval from uploaded files via vector search |
| `function` | Tool Type | /docs/assistants/overview | Custom tool type for developer-defined functions |
| `vector_store` | Resource | /docs/assistants/overview | Storage system for file embeddings used by file_search tool |
| `annotations` | Message Field | /docs/assistants/overview | Citations and file references embedded in assistant message content |
| `attachments` | Message Field | /docs/assistants/overview | Files attached to a message for tool access |

### Evals

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `eval` | Resource | /docs/guides/evals | Evaluation configuration defining how to test model outputs |
| `data_source_config` | Eval Field | /docs/guides/evals | Specifies the data source for evaluation (stored completions, custom) |
| `testing_criteria` | Eval Field | /docs/guides/evals | Array of graders defining what constitutes a passing response |
| `string_check` | Grader Type | /docs/guides/evals | Tests if output contains/equals a string; exact match grader |
| `text_similarity` | Grader Type | /docs/guides/evals | Measures semantic similarity between output and reference |
| `model_graded_rubric` | Grader Type | /docs/guides/evals | Uses a model to grade responses against a rubric |
| `model_graded_factuality` | Grader Type | /docs/guides/evals | Model-based factual accuracy grading |
| `run` | Resource | /docs/guides/evals | Execution of an eval against a dataset |

---

## Google Gemini (ai.google.dev)

### Function Calling

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `FunctionDeclaration` | Definition Object | /gemini-api/docs/function-calling | Defines a callable function: `name`, `description`, `parameters` (type, properties, required), optional `enum` |
| `Tool` | Container Object | /gemini-api/docs/function-calling | Container holding one or more `function_declarations`; passed in model config |
| `FunctionCall` | Response Object | /gemini-api/docs/function-calling | Model's invocation request; fields: `name`, `args`, `id` |
| `FunctionResponse` | Request Object | /gemini-api/docs/function-calling | Developer's result sent back to model; fields: `name`, `response`, `id` (matching FunctionCall.id) |
| `tool_config` | Request Object | /gemini-api/docs/function-calling | Configuration object controlling function behavior; contains `function_calling_config` |
| `function_calling_config` | Config Object | /gemini-api/docs/function-calling | Inner config; sets `mode` and optionally `allowed_function_names` |
| `mode` | Config Field | /gemini-api/docs/function-calling | Execution mode: `AUTO` (model decides), `ANY` (must call a function), `NONE` (no function calls), `VALIDATED` (preview) |
| `AUTO` | Mode Value | /gemini-api/docs/function-calling | Default; model decides whether to call a function or respond naturally |
| `ANY` | Mode Value | /gemini-api/docs/function-calling | Model must predict a function call; ensures schema adherence |
| `NONE` | Mode Value | /gemini-api/docs/function-calling | Prohibits function calls entirely |
| `VALIDATED` | Mode Value | /gemini-api/docs/function-calling | Preview; model chooses between function calls or natural language with validation |
| `allowed_function_names` | Config Field | /gemini-api/docs/function-calling | Optional array restricting which declared functions can be called (use with ANY or VALIDATED) |

### Grounding

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `google_search` | Tool | /gemini-api/docs/grounding | Current tool for grounding; used in all current models |
| `google_search_retrieval` | Tool (Legacy) | /gemini-api/docs/grounding | Legacy grounding tool for older model versions |
| `grounding_metadata` | Response Object | /gemini-api/docs/grounding | Structured grounding data returned with grounded answers; contains search info and citations |
| `groundingChunks` | Metadata Field | /gemini-api/docs/grounding | Array of web sources; each has `uri` and `title` |
| `groundingSupports` | Metadata Field | /gemini-api/docs/grounding | Array linking model response text segments to source citations in groundingChunks |
| `webSearchQueries` | Metadata Field | /gemini-api/docs/grounding | Array of search queries used; useful for debugging model reasoning |
| `searchEntryPoint` | Metadata Field | /gemini-api/docs/grounding | Contains HTML and CSS for rendering required Search Suggestions |

---

## AWS Bedrock (docs.aws.amazon.com)

### Agents

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `agent` | Core Entity | /bedrock/latest/userguide/agents.html | Autonomous system orchestrating FMs, data sources, apps, and user conversations to complete actions |
| `action_group` | Component | /bedrock/latest/userguide/agents.html | Defines specific actions an agent can perform; agent makes API calls to execute; each group maps to an API schema |
| `knowledge_base` | Component | /bedrock/latest/userguide/agents.html | Database storing private organizational data that agents query for augmented responses |
| `agent_alias` | Deployment | /bedrock/latest/userguide/agents.html | Pointer to a specific agent version for production deployments and API calls |
| `foundation_model` (FM) | Core Entity | /bedrock/latest/userguide/agents.html | Underlying LLM that the agent orchestrates; understands user requests and breaks down tasks |
| `orchestration` | Process | /bedrock/latest/userguide/agents.html | Coordination of interactions between FMs, data sources, software apps, and user conversations |
| `trace` | Monitoring | /bedrock/latest/userguide/agents.html | Step-by-step reasoning record of agent's orchestration process; used for troubleshooting |
| `memory` | Capability | /bedrock/latest/userguide/agents.html | Managed by Amazon Bedrock; maintains conversation context across sessions |
| `guardrail` | Safety | /bedrock/latest/userguide/agents.html | Policy layer filtering harmful content and enforcing topic boundaries for agents |
| `session` | Concept | /bedrock/latest/userguide/agents.html | Conversation context container for a single agent interaction |

### Knowledge Bases

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `knowledge_base` | Resource | /bedrock/latest/userguide/knowledge-base.html | System integrating proprietary information into generative AI apps; searches data sources for relevant info |
| `data_source` | Component | /bedrock/latest/userguide/knowledge-base.html | Underlying repository (unstructured or structured) connected to a knowledge base |
| `vector_store` | Storage | /bedrock/latest/userguide/knowledge-base.html | Storage system indexing vector embeddings; user-managed or auto-created (Amazon OpenSearch Serverless) |
| `retrieval` | Process | /bedrock/latest/userguide/knowledge-base.html | Searching data sources to find relevant information answering a query |
| `RAG` (Retrieval Augmented Generation) | Technique | /bedrock/latest/userguide/knowledge-base.html | Uses data source information to improve relevancy and accuracy of FM responses |
| `embedding_model` | Component | /bedrock/latest/userguide/knowledge-base.html | Model converting text to vector embeddings for semantic search |
| `sync` | Operation | /bedrock/latest/userguide/knowledge-base.html | Process updating knowledge base index from its data source |
| `chunking_strategy` | Config | /bedrock/latest/userguide/knowledge-base.html | How documents are split into indexable segments during ingestion |
| `ingestion_job` | Operation | /bedrock/latest/userguide/knowledge-base.html | Job processing data source documents into the knowledge base vector store |

---

## Azure AI Foundry (learn.microsoft.com)

### Architecture

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `Foundry resource` | Azure Resource | /azure/foundry/concepts/architecture | Top-level Azure resource (`Microsoft.CognitiveServices/account`, kind `AIServices`); governance scope for security, networking, model deployments |
| `project` | Sub-resource | /azure/foundry/concepts/architecture | Development boundary inside Foundry resource (`Microsoft.CognitiveServices/account/project`); isolates assets and access |
| `project assets` | Concept | /azure/foundry/concepts/architecture | Files, agents, evaluations, and related artifacts scoped to a project |
| `RBAC` (Role-Based Access Control) | Security | /azure/foundry/concepts/architecture | Access control; separates control plane (create deployments/projects) from data plane (build agents/run evals) |
| `Azure AI User` | RBAC Role | /azure/foundry/concepts/architecture | Common starter RBAC role for developer access at Foundry resource scope |
| `managed identities` | Identity | /azure/foundry/concepts/architecture | Azure identity for secure automation and service access; assigned at resource or project scope |
| `standard deployment` | Model Hosting | /azure/foundry/concepts/architecture | Model deployment type provided by Foundry resource (Model Hosting Architecture) |
| `Microsoft.CognitiveServices` | Resource Provider | /azure/foundry/concepts/architecture | Azure resource provider namespace shared by Foundry, Azure OpenAI, Speech, Vision, Language |
| `container injection` | Networking | /azure/foundry/concepts/architecture | Allows platform to inject a subnet into customer's network for local communication of Azure resources |
| `evaluation` | Feature | /azure/foundry/concepts/architecture | Assessment of agent/model performance; scoped to individual projects |

### Prompt Flow (Classic / Foundry Classic)

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `prompt flow` | Feature | /azure/foundry-classic/concepts/prompt-flow | Development tool streamlining the full LLM application lifecycle: prototype → experiment → evaluate → deploy |
| `flow` | Executable | /azure/foundry-classic/concepts/prompt-flow | Executable instruction set implementing AI logic; once deployed becomes an API |
| `standard flow` | Flow Type | /azure/foundry-classic/concepts/prompt-flow | General-purpose flow for LLM application development with full tool range |
| `chat flow` | Flow Type | /azure/foundry-classic/concepts/prompt-flow | Conversational flow with enhanced support for chat inputs, outputs, and history management |
| `evaluation flow` | Flow Type | /azure/foundry-classic/concepts/prompt-flow | Takes previous flow run outputs as inputs; assesses performance and outputs metrics |
| `node` | Flow Component | /azure/foundry-classic/concepts/prompt-flow | Building block within a flow; each node is a tool with inputs/outputs |
| `DAG` (Directed Acyclic Graph) | Visual Model | /azure/foundry-classic/concepts/prompt-flow | Visual representation of flow structure showing node connectivity and dependencies |
| `LLM tool` | Node Type | /azure/foundry-classic/concepts/prompt-flow | Node type for LLM calls (text generation, summarization) |
| `Prompt tool` | Node Type | /azure/foundry-classic/concepts/prompt-flow | Node type for prompt template rendering |
| `Python tool` | Node Type | /azure/foundry-classic/concepts/prompt-flow | Node type for arbitrary Python code execution |
| `variant` | Concept | /azure/foundry-classic/concepts/prompt-flow | Alternative version of a prompt/node for comparative A/B testing |
| `connection` | Resource | /azure/foundry-classic/concepts/prompt-flow | Integration configuration linking flows to external services and APIs |
| `prompt` | Concept | /azure/foundry-classic/concepts/prompt-flow | Package of input to a model: user input + system message + optional examples |
| `sample flow` | Resource | /azure/foundry-classic/concepts/prompt-flow | Prebuilt orchestration flow demonstrating patterns; can be customized |

---

## MCP — Model Context Protocol (modelcontextprotocol.io)

### Participants

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `MCP Host` | Participant | /docs/learn/architecture | AI application (e.g., Claude Desktop, VS Code) that coordinates one or more MCP clients |
| `MCP Client` | Participant | /docs/learn/architecture | Component maintaining a dedicated connection to one MCP server; obtains context for the host |
| `MCP Server` | Participant | /docs/learn/architecture | Program exposing context (tools, resources, prompts) to MCP clients; can run locally or remotely |

### Server Primitives

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `tool` | Server Primitive | /docs/learn/architecture | Executable function invokable by AI applications (file operations, API calls, DB queries) |
| `resource` | Server Primitive | /docs/learn/architecture | Data source providing contextual information (file contents, DB records, API responses) |
| `prompt` | Server Primitive | /docs/learn/architecture | Reusable interaction template (system prompts, few-shot examples) |
| `inputSchema` | Tool Field | /docs/learn/architecture | JSON Schema defining expected input parameters for a tool |
| `name` | Primitive Field | /docs/learn/architecture | Unique identifier for a tool/resource/prompt within the server namespace |
| `title` | Tool Field | /docs/learn/architecture | Human-readable display name shown to users |
| `description` | Primitive Field | /docs/learn/architecture | Detailed explanation of what the tool/resource/prompt does and when to use it |

### Client Primitives

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `sampling` | Client Primitive | /docs/learn/architecture | Allows servers to request LLM completions from the client's host application; uses `sampling/complete` |
| `elicitation` | Client Primitive | /docs/learn/architecture | Allows servers to request additional user input; uses `elicitation/request` |
| `logging` | Client Primitive | /docs/learn/architecture | Enables servers to send log messages to clients for debugging |

### Methods (JSON-RPC 2.0)

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `initialize` | Lifecycle | /docs/learn/architecture | First request establishing connection and negotiating capabilities |
| `notifications/initialized` | Notification | /docs/learn/architecture | Client notification confirming readiness after `initialize` response |
| `tools/list` | Discovery | /docs/learn/architecture | Lists all tools available on the server; returns array of tool objects |
| `tools/call` | Execution | /docs/learn/architecture | Invokes a tool by name with arguments; returns `content` array |
| `resources/list` | Discovery | /docs/learn/architecture | Lists available resources on the server |
| `resources/read` | Retrieval | /docs/learn/architecture | Reads a specific resource by URI |
| `prompts/list` | Discovery | /docs/learn/architecture | Lists available prompt templates |
| `prompts/get` | Retrieval | /docs/learn/architecture | Retrieves a specific prompt template |
| `sampling/complete` | Client Method | /docs/learn/architecture | Server requests LLM completion from the client |
| `elicitation/request` | Client Method | /docs/learn/architecture | Server requests user input from the client |
| `notifications/tools/list_changed` | Notification | /docs/learn/architecture | Server notifies clients that available tools have changed; requires `listChanged: true` capability |

### Transport & Protocol

| Official Term | Category | URL | Description |
|--------------|----------|-----|-------------|
| `JSON-RPC 2.0` | Protocol | /docs/learn/architecture | Underlying RPC protocol; requests have `id`, notifications do not |
| `stdio transport` | Transport | /docs/learn/architecture | Standard input/output streams for local process communication; no network overhead |
| `Streamable HTTP transport` | Transport | /docs/learn/architecture | HTTP POST for client→server messages with optional SSE streaming; supports OAuth |
| `capabilities` | Negotiation | /docs/learn/architecture | Declared features supported by client and server during `initialize` handshake |
| `protocolVersion` | Protocol Field | /docs/learn/architecture | Version string (e.g., `"2025-06-18"`) negotiated during initialization |
| `listChanged` | Capability Flag | /docs/learn/architecture | Declares server can emit `*/list_changed` notifications |
| `Tasks` (Experimental) | Primitive | /docs/learn/architecture | Durable execution wrappers for deferred results and status tracking |

---

## Cross-Provider Alignment

| Concept | Anthropic | OpenAI | Google | AWS | Azure | MCP |
|---------|-----------|--------|--------|-----|-------|-----|
| **Tool Definition** | `tool` (name, description, input_schema) | `tool` → `function` (name, description, parameters) | `FunctionDeclaration` (name, description, parameters) | `action_group` | `LLM tool` / `Python tool` node | `tool` (name, description, inputSchema) |
| **Tool Invocation** | `tool_use` block (stop_reason: tool_use) | `tool_calls` array in assistant message | `FunctionCall` object | API call via action_group | Flow node execution | `tools/call` method |
| **Tool Result** | `tool_result` block (tool_use_id) | tool role message (tool_call_id) | `FunctionResponse` object (id) | API response to action_group | Node output → next node | `tools/call` response content |
| **Tool Selection Control** | `tool_choice`: auto/any/tool/none | `tool_choice`: auto/none/required/function | `mode`: AUTO/ANY/NONE/VALIDATED | N/A (orchestration by FM) | N/A | N/A |
| **Parallel Tool Calls** | Multiple `tool_use` blocks | `parallel_tool_calls: true` | Multiple `FunctionCall` objects | N/A | Parallel nodes in DAG | Multiple `tools/call` |
| **Schema Enforcement** | `strict: true` | `strict: true` in function | JSON Schema in `parameters` | API schema (OpenAPI) | Type validation in nodes | `inputSchema` (JSON Schema) |
| **Knowledge Retrieval** | N/A (tool: file_search via MCP) | `file_search` tool + `vector_store` | `google_search` grounding | `knowledge_base` + RAG | `file_search` via Azure AI Search | `resource` primitive |
| **Web Search** | `web_search_20260209` server tool | N/A native (GPT-4 Browsing retired) | `google_search` grounding | N/A native | N/A native | `tool` (search MCP servers) |
| **Code Execution** | `code_execution` server tool | `code_interpreter` tool | N/A native | N/A native | `Python tool` in Prompt Flow | `tool` (code execution servers) |
| **Conversation Thread** | Multi-turn `messages` array | `Thread` (persistent, server-side) | `contents` array per request | `session` (agent memory) | Chat history in chat flow | Stateful session |
| **Caching** | `cache_control` (ephemeral, 5m/1h) | N/A (KV cache automatic) | N/A explicit control | N/A explicit control | N/A explicit control | N/A |
| **Agent Orchestration** | `agentic loop` (client-side) | `Run` lifecycle (server-side) | N/A (client-side loop) | `agent` + `orchestration` | `flow` + deployment | MCP client orchestrates |
| **Evaluation** | N/A native | `eval` + `testing_criteria` | N/A native | N/A native | `evaluation flow` | N/A |
| **Grounding** | N/A | N/A | `grounding_metadata` (google_search) | `knowledge_base` (RAG) | Azure AI Search integration | `resource` primitive |

---

## CEX Kind Validation

| CEX Kind | Provider Term(s) | Match Quality | Official URL |
|----------|-----------------|---------------|--------------|
| `P01_knowledge` (knowledge cards) | Anthropic: prompt caching `cache_control`; AWS: `knowledge_base`; MCP: `resource` | High | /bedrock/.../knowledge-base.html |
| `P02_model` (model config) | Anthropic: model field + `tool_choice`; Google: `mode`; Azure: `standard deployment` | High | /docs/en/about-claude/models |
| `P03_prompt` (system/user prompts) | Anthropic: system/user messages; OpenAI: `Thread.Message`; Azure: `prompt` in Prompt Flow | High | /docs/en/agents-and-tools/tool-use |
| `P04_tools` (tool definitions) | Anthropic: `tool` (input_schema); OpenAI: `tool` (parameters); Google: `FunctionDeclaration`; MCP: `tool` (inputSchema) | High — all converge on JSON Schema | all tool docs |
| `P05_output` (output templates) | Anthropic: `tool_result` content; OpenAI: `response_format` + `json_schema`; Google: `FunctionResponse` | High | /docs/guides/structured-outputs |
| `P06_schema` (JSON schemas) | Anthropic: `input_schema` + `strict`; OpenAI: `parameters` + `strict`; Google: `parameters`; MCP: `inputSchema` | High — all use JSON Schema | all tool docs |
| `P07_evals` (quality gates) | OpenAI: `eval` + `testing_criteria` + grader types; Azure: `evaluation flow`; AWS: trace analysis | Medium | /docs/guides/evals |
| `P08_architecture` (system design) | MCP: `MCP Host/Client/Server`; AWS: agent + action_group + orchestration; Azure: Foundry resource + project | High | /docs/learn/architecture |
| `P09_config` (configuration) | Anthropic: `tool_choice`; Google: `tool_config` + `function_calling_config`; Azure: `connection` | High | /gemini-api/docs/function-calling |
| `P10_memory` (context memory) | Anthropic: `cache_control` ephemeral; OpenAI: `Thread` persistence; AWS: agent `memory`; MCP: stateful session | Medium — different scopes | /docs/.../prompt-caching |
| `P11_feedback` (feedback loops) | OpenAI: `tool_calls` → `tool` result round-trip; MCP: `notifications/tools/list_changed`; Anthropic: agentic loop | Medium | /docs/.../tool-use |
| `P12_orchestration` (multi-agent) | AWS: `agent` orchestration; Azure: `flow` DAG; MCP: `MCP Host` multi-client; Anthropic: server tools + agentic loop | High | /bedrock/.../agents.html |
