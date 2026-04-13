---
id: n01_atom_02_mcp_protocol
kind: knowledge_card
type: research_atom
pillar: P01
title: "MCP (Model Context Protocol) -- Complete Term Registry & Specification Atlas"
version: 1.0.0
created: 2026-04-13
updated: 2026-04-13
author: n01_intelligence
domain: mcp_protocol
quality: 8.9
tags: [mcp, protocol, specification, tools, resources, prompts, sampling, a2a, interop]
tldr: "Exhaustive term-by-term extraction from the MCP 2025-11-25 spec: every object, method, content type, capability, transport, and error code defined by the protocol"
when_to_use: "Building MCP servers/clients, mapping CEX tools to MCP, understanding protocol capabilities, designing agent-to-agent interop"
keywords: [mcp, model-context-protocol, json-rpc, tools, resources, prompts, sampling, roots, elicitation, tasks, transport, stdio, streamable-http]
spec_version: "2025-11-25"
spec_url: "https://modelcontextprotocol.io/specification/2025-11-25"
schema_source: "https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-11-25/schema.ts"
density_score: null
---

# MCP (Model Context Protocol) -- Complete Specification Atlas

> **Spec version**: 2025-11-25 (latest as of April 2026)
> **Wire format**: JSON-RPC 2.0 over stdio or Streamable HTTP
> **Source of truth**: [schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-11-25/schema.ts)

---

## 1. Architecture -- Core Components

MCP follows a **client-host-server** architecture.

| Component | Role | Cardinality |
|-----------|------|-------------|
| **Host** | LLM application that creates/manages clients, enforces security, aggregates context | 1 per application |
| **Client** | Connector within the host; maintains 1:1 stateful session with a server | 1 per server connection |
| **Server** | Service providing context and capabilities via MCP primitives | N (local or remote) |

### Design Principles

1. Servers should be extremely easy to build
2. Servers should be highly composable
3. Servers cannot read the full conversation or see into other servers
4. Features are added progressively via capability negotiation

---

## 2. Protocol Layers

| Layer | Scope |
|-------|-------|
| **Base Protocol** | JSON-RPC 2.0 message types (Request, Response, Notification) |
| **Lifecycle** | initialize, initialized, ping, shutdown |
| **Authorization** | OAuth 2.1 for HTTP transports (not for stdio) |
| **Server Features** | Resources, Prompts, Tools |
| **Client Features** | Sampling, Roots, Elicitation |
| **Utilities** | Logging, Pagination, Completion, Progress, Cancellation, Tasks |

---

## 3. Base Protocol -- JSON-RPC 2.0

### 3.1 Message Types

| Type | Has `id`? | Has `method`? | Has `result`/`error`? | Direction |
|------|-----------|---------------|-----------------------|-----------|
| **Request** | YES (string or integer, never null) | YES | NO | bidirectional |
| **Response (Result)** | YES (matches request) | NO | `result: object` | reply |
| **Response (Error)** | YES (matches request) | NO | `error: {code, message, data?}` | reply |
| **Notification** | NO | YES | NO | bidirectional, no reply expected |

### 3.2 Standard Error Codes

| Code | Name | When |
|------|------|------|
| -32700 | Parse error | Invalid JSON |
| -32600 | Invalid request | Malformed JSON-RPC |
| -32601 | Method not found | Unknown method / capability not declared |
| -32602 | Invalid params | Bad parameters, unknown tool, invalid cursor |
| -32603 | Internal error | Server-side failure |
| -32002 | Resource not found | Resource URI does not resolve |
| -32042 | URLElicitationRequired | URL-mode elicitation needed before request can proceed |
| -1 | User rejected | User rejected sampling request |

### 3.3 General Fields

| Field | Type | Scope | Description |
|-------|------|-------|-------------|
| `_meta` | `object` | Any message | Reserved metadata namespace. Keys use reverse-DNS prefix + name format |
| `_meta.progressToken` | `string \| number` | Request params | Enables progress notifications for this request |
| `_meta.io.modelcontextprotocol/related-task` | `{taskId: string}` | Any message | Associates message with a task |
| `icons` | `Icon[]` | Tool, Resource, Prompt, Implementation | Visual identifiers for UI display |

### 3.4 Icon Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `src` | `string (URI)` | YES | HTTPS URL or data URI |
| `mimeType` | `string` | NO | Image MIME type (must support: image/png, image/jpeg) |
| `sizes` | `string[]` | NO | e.g. `["48x48"]`, `["any"]` for SVG |
| `theme` | `"light" \| "dark"` | NO | Preferred background theme |

### 3.5 JSON Schema Usage

- Default dialect: JSON Schema 2020-12 (when no `$schema` field)
- Implementations MUST support 2020-12
- Schemas MAY include explicit `$schema` for other dialects (e.g. draft-07)

---

## 4. Lifecycle

### 4.1 Phases

| Phase | Description |
|-------|-------------|
| **Initialization** | Version negotiation + capability exchange |
| **Operation** | Normal protocol communication |
| **Shutdown** | Transport-level disconnection |

### 4.2 Initialize Request (`initialize`)

**Direction**: Client -> Server

| Field | Type | Description |
|-------|------|-------------|
| `params.protocolVersion` | `string` | e.g. `"2025-11-25"` |
| `params.capabilities` | `ClientCapabilities` | See Section 5 |
| `params.clientInfo` | `Implementation` | See below |

### 4.3 Initialize Response

| Field | Type | Description |
|-------|------|-------------|
| `result.protocolVersion` | `string` | Negotiated version |
| `result.capabilities` | `ServerCapabilities` | See Section 6 |
| `result.serverInfo` | `Implementation` | See below |
| `result.instructions` | `string?` | Optional instructions for the client |

### 4.4 Implementation Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | YES | Machine-readable name |
| `title` | `string` | NO | Human-readable display name |
| `version` | `string` | YES | Version string |
| `description` | `string` | NO | Description of the implementation |
| `icons` | `Icon[]` | NO | Visual identifiers |
| `websiteUrl` | `string` | NO | Website URL |

### 4.5 Initialized Notification

**Method**: `notifications/initialized` -- Client -> Server after successful init.

### 4.6 Ping

**Method**: `ping` -- Bidirectional. Empty params, empty result `{}`.

### 4.7 Version Negotiation

1. Client sends its supported version (SHOULD be latest)
2. Server responds with same version if supported, otherwise its own latest
3. If client doesn't support server's version, client SHOULD disconnect

### 4.8 Shutdown

- **stdio**: Client closes stdin, waits, then SIGTERM, then SIGKILL
- **HTTP**: Close HTTP connection(s); client MAY send HTTP DELETE with session ID

---

## 5. Client Capabilities

| Capability | Sub-capability | Type | Description |
|------------|---------------|------|-------------|
| `roots` | | `object` | Client can provide filesystem roots |
| `roots` | `listChanged` | `boolean` | Client will notify when roots change |
| `sampling` | | `object` | Client supports LLM sampling requests |
| `sampling` | `tools` | `object` | Client supports tool use within sampling |
| `sampling` | `context` | `object` | Client supports includeContext (soft-deprecated) |
| `elicitation` | | `object` | Client supports server elicitation requests |
| `elicitation` | `form` | `object` | Supports form-mode elicitation |
| `elicitation` | `url` | `object` | Supports URL-mode elicitation |
| `tasks` | | `object` | Client supports task-augmented requests |
| `tasks` | `list` | `object` | Client supports tasks/list |
| `tasks` | `cancel` | `object` | Client supports tasks/cancel |
| `tasks.requests` | `sampling.createMessage` | `object` | Supports task-augmented sampling |
| `tasks.requests` | `elicitation.create` | `object` | Supports task-augmented elicitation |
| `experimental` | | `object` | Non-standard experimental features |

---

## 6. Server Capabilities

| Capability | Sub-capability | Type | Description |
|------------|---------------|------|-------------|
| `prompts` | | `object` | Server offers prompt templates |
| `prompts` | `listChanged` | `boolean` | Server notifies when prompts change |
| `resources` | | `object` | Server provides readable resources |
| `resources` | `subscribe` | `boolean` | Client can subscribe to resource changes |
| `resources` | `listChanged` | `boolean` | Server notifies when resource list changes |
| `tools` | | `object` | Server exposes callable tools |
| `tools` | `listChanged` | `boolean` | Server notifies when tool list changes |
| `logging` | | `object` | Server emits structured log messages |
| `completions` | | `object` | Server supports argument autocompletion |
| `tasks` | | `object` | Server supports task-augmented requests |
| `tasks` | `list` | `object` | Server supports tasks/list |
| `tasks` | `cancel` | `object` | Server supports tasks/cancel |
| `tasks.requests` | `tools.call` | `object` | Supports task-augmented tools/call |
| `experimental` | | `object` | Non-standard experimental features |

---

## 7. Server Features

### 7.1 Tools

**Interaction model**: Model-controlled (LLM discovers and invokes automatically).

#### 7.1.1 Tool Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | YES | Unique identifier (1-128 chars, ASCII letters/digits/`_`/`-`/`.`) |
| `title` | `string` | NO | Human-readable display name |
| `description` | `string` | NO | Human-readable description |
| `icons` | `Icon[]` | NO | Visual identifiers |
| `inputSchema` | `JSON Schema object` | YES | Parameters schema (MUST NOT be null; defaults to 2020-12) |
| `outputSchema` | `JSON Schema object` | NO | Expected structured output schema |
| `annotations` | `ToolAnnotations` | NO | Behavioral hints (UNTRUSTED unless from trusted server) |
| `execution` | `object` | NO | Execution properties |
| `execution.taskSupport` | `"forbidden" \| "optional" \| "required"` | NO | Task-augmented execution support (default: `"forbidden"`) |

#### 7.1.2 Tool Annotations (ToolAnnotations)

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `title` | `string` | -- | Human-readable tool title |
| `readOnlyHint` | `boolean` | `false` | Tool does not modify state |
| `destructiveHint` | `boolean` | `true` | Tool may perform destructive operations |
| `idempotentHint` | `boolean` | `false` | Repeated calls with same args have no additional effect |
| `openWorldHint` | `boolean` | `true` | Tool interacts with external entities beyond its control |

> Clients MUST treat annotations as untrusted unless the server is trusted.

#### 7.1.3 Tool Methods

| Method | Direction | Description |
|--------|-----------|-------------|
| `tools/list` | Client -> Server | List available tools (paginated) |
| `tools/call` | Client -> Server | Invoke a tool |
| `notifications/tools/list_changed` | Server -> Client | Tool list changed |

#### 7.1.4 CallToolResult

| Field | Type | Description |
|-------|------|-------------|
| `content` | `Content[]` | Unstructured result content (text, image, audio, resource_link, resource) |
| `structuredContent` | `object` | Structured JSON result (validated against outputSchema) |
| `isError` | `boolean` | `true` if tool execution failed |

#### 7.1.5 Content Types in Tool Results

| type | Fields | Description |
|------|--------|-------------|
| `text` | `text: string` | Plain text |
| `image` | `data: string (base64)`, `mimeType: string` | Base64-encoded image |
| `audio` | `data: string (base64)`, `mimeType: string` | Base64-encoded audio |
| `resource_link` | `uri: string`, `name: string`, `description?: string`, `mimeType?: string` | Link to a Resource |
| `resource` | `resource: {uri, mimeType, text?, blob?}` | Embedded Resource content |

All content types support optional `annotations` (see Section 7.2.5).

---

### 7.2 Resources

**Interaction model**: Application-driven (host determines how to incorporate).

#### 7.2.1 Resource Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `uri` | `string (URI)` | YES | Unique identifier (RFC 3986) |
| `name` | `string` | YES | Resource name |
| `title` | `string` | NO | Human-readable display name |
| `description` | `string` | NO | Description |
| `icons` | `Icon[]` | NO | Visual identifiers |
| `mimeType` | `string` | NO | MIME type |
| `size` | `number` | NO | Size in bytes |

#### 7.2.2 ResourceTemplate Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `uriTemplate` | `string` | YES | RFC 6570 URI template |
| `name` | `string` | YES | Template name |
| `title` | `string` | NO | Human-readable display name |
| `description` | `string` | NO | Description |
| `icons` | `Icon[]` | NO | Visual identifiers |
| `mimeType` | `string` | NO | MIME type |

#### 7.2.3 Resource Contents

| Variant | Fields | Description |
|---------|--------|-------------|
| **TextResourceContents** | `uri: string`, `mimeType?: string`, `text: string` | Text content |
| **BlobResourceContents** | `uri: string`, `mimeType?: string`, `blob: string (base64)` | Binary content |

#### 7.2.4 Resource Methods

| Method | Direction | Description |
|--------|-----------|-------------|
| `resources/list` | Client -> Server | List resources (paginated) |
| `resources/read` | Client -> Server | Read resource contents |
| `resources/templates/list` | Client -> Server | List resource templates |
| `resources/subscribe` | Client -> Server | Subscribe to resource changes |
| `resources/unsubscribe` | Client -> Server | Unsubscribe |
| `notifications/resources/list_changed` | Server -> Client | Resource list changed |
| `notifications/resources/updated` | Server -> Client | Specific resource updated |

#### 7.2.5 Resource Annotations

Annotations apply to Resources, ResourceTemplates, and all content blocks.

| Field | Type | Description |
|-------|------|-------------|
| `audience` | `("user" \| "assistant")[]` | Intended audience |
| `priority` | `number (0.0-1.0)` | Importance (1.0 = most important) |
| `lastModified` | `string (ISO 8601)` | Last modification timestamp |

#### 7.2.6 Common URI Schemes

| Scheme | Usage |
|--------|-------|
| `https://` | Web resources (client can fetch directly) |
| `file://` | Filesystem-like resources (may not be actual files) |
| `git://` | Git version control |
| Custom | Any RFC 3986-compliant scheme |

---

### 7.3 Prompts

**Interaction model**: User-controlled (user selects prompts, e.g. as slash commands).

#### 7.3.1 Prompt Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | YES | Unique identifier |
| `title` | `string` | NO | Human-readable display name |
| `description` | `string` | NO | Description |
| `icons` | `Icon[]` | NO | Visual identifiers |
| `arguments` | `PromptArgument[]` | NO | Customization arguments |

#### 7.3.2 PromptArgument

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | YES | Argument name |
| `description` | `string` | NO | Argument description |
| `required` | `boolean` | NO | Whether required |

#### 7.3.3 PromptMessage

| Field | Type | Description |
|-------|------|-------------|
| `role` | `"user" \| "assistant"` | Speaker role |
| `content` | `TextContent \| ImageContent \| AudioContent \| EmbeddedResource` | Message content |

Content types in prompts: `text`, `image`, `audio`, `resource` (same as Section 7.1.5).

#### 7.3.4 Prompt Methods

| Method | Direction | Description |
|--------|-----------|-------------|
| `prompts/list` | Client -> Server | List prompts (paginated) |
| `prompts/get` | Client -> Server | Get specific prompt with arguments |
| `notifications/prompts/list_changed` | Server -> Client | Prompt list changed |

---

## 8. Client Features

### 8.1 Sampling

**Purpose**: Servers request LLM completions through the client (server never needs API keys).

#### 8.1.1 CreateMessage Request (`sampling/createMessage`)

**Direction**: Server -> Client

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `params.messages` | `SamplingMessage[]` | YES | Conversation messages |
| `params.modelPreferences` | `ModelPreferences` | NO | Model selection hints |
| `params.systemPrompt` | `string` | NO | System prompt |
| `params.maxTokens` | `number` | YES | Maximum tokens to generate |
| `params.tools` | `SamplingTool[]` | NO | Tools available during sampling |
| `params.toolChoice` | `ToolChoice` | NO | Tool use control |
| `params.includeContext` | `"none" \| "thisServer" \| "allServers"` | NO | Context inclusion (soft-deprecated) |

#### 8.1.2 CreateMessageResult

| Field | Type | Description |
|-------|------|-------------|
| `role` | `"assistant"` | Always assistant |
| `content` | `TextContent \| ImageContent \| AudioContent \| ToolUseContent \| ToolUseContent[]` | Generated content |
| `model` | `string` | Model used |
| `stopReason` | `"endTurn" \| "toolUse" \| "maxTokens" \| string` | Why generation stopped |

#### 8.1.3 ModelPreferences

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `hints` | `ModelHint[]` | -- | Specific model suggestions |
| `costPriority` | `number` | 0-1 | Prefer cheaper models |
| `speedPriority` | `number` | 0-1 | Prefer faster models |
| `intelligencePriority` | `number` | 0-1 | Prefer more capable models |

#### 8.1.4 ModelHint

| Field | Type | Description |
|-------|------|-------------|
| `name` | `string` | Substring to match against model names (advisory) |

#### 8.1.5 ToolChoice

| Mode | Description |
|------|-------------|
| `{mode: "auto"}` | Model decides (default) |
| `{mode: "required"}` | Model MUST use at least one tool |
| `{mode: "none"}` | Model MUST NOT use tools |

#### 8.1.6 Sampling Content Types

| type | Fields | Description |
|------|--------|-------------|
| `text` | `text: string` | Text content |
| `image` | `data: string`, `mimeType: string` | Image content |
| `audio` | `data: string`, `mimeType: string` | Audio content |
| `tool_use` | `id: string`, `name: string`, `input: object` | Tool use request |
| `tool_result` | `toolUseId: string`, `content: Content[]` | Tool execution result |

**Constraint**: User messages with `tool_result` MUST contain ONLY tool results (no mixing).

#### 8.1.7 Message Roles

MCP uses two roles: `"user"` and `"assistant"`. Tool use requests come from assistant; tool results go in user messages.

---

### 8.2 Roots

**Purpose**: Clients expose filesystem boundaries to servers.

#### 8.2.1 Root Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `uri` | `string` | YES | MUST be `file://` URI |
| `name` | `string` | NO | Human-readable name |

#### 8.2.2 Root Methods

| Method | Direction | Description |
|--------|-----------|-------------|
| `roots/list` | Server -> Client | List available roots |
| `notifications/roots/list_changed` | Client -> Server | Root list changed |

---

### 8.3 Elicitation

**Purpose**: Servers request additional information from users through the client.

#### 8.3.1 Modes

| Mode | Description | Data visible to client? |
|------|-------------|------------------------|
| `form` | In-band structured data collection | YES |
| `url` | Out-of-band URL navigation for sensitive data | NO (only the URL itself) |

#### 8.3.2 Elicitation Request (`elicitation/create`)

**Direction**: Server -> Client

**Common fields**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `params.mode` | `"form" \| "url"` | NO (default: `"form"`) | Elicitation mode |
| `params.message` | `string` | YES | Human-readable explanation |

**Form-mode additional fields**:

| Field | Type | Description |
|-------|------|-------------|
| `params.requestedSchema` | `JSON Schema object` | Flat object with primitive properties only |

**URL-mode additional fields**:

| Field | Type | Description |
|-------|------|-------------|
| `params.url` | `string (URL)` | Target URL |
| `params.elicitationId` | `string` | Unique elicitation identifier |

#### 8.3.3 Supported Schema Types (Form Mode)

| Type | JSON Schema type | Supported constraints |
|------|-----------------|----------------------|
| String | `"string"` | `minLength`, `maxLength`, `pattern`, `format` (email, uri, date, date-time), `default` |
| Number | `"number"` or `"integer"` | `minimum`, `maximum`, `default` |
| Boolean | `"boolean"` | `default` |
| Enum (single) | `"string"` with `enum` or `oneOf[{const, title}]` | `default` |
| Enum (multi) | `"array"` with items `enum` or `anyOf` | `minItems`, `maxItems`, `default` |

No nested objects or complex structures allowed.

#### 8.3.4 Elicitation Response

| Field | Type | Description |
|-------|------|-------------|
| `result.action` | `"accept" \| "decline" \| "cancel"` | User's decision |
| `result.content` | `object` | Submitted data (form mode only, when accepted) |

#### 8.3.5 Elicitation Notifications & Errors

| Item | Description |
|------|-------------|
| `notifications/elicitation/complete` | Server -> Client: URL-mode elicitation completed |
| Error -32042 (`URLElicitationRequiredError`) | Request cannot proceed without URL elicitation |

---

## 9. Utilities

### 9.1 Logging

**Capability**: `logging` (server)

| Method | Direction | Description |
|--------|-----------|-------------|
| `logging/setLevel` | Client -> Server | Set minimum log level |
| `notifications/message` | Server -> Client | Log message |

**LoggingLevel enum** (syslog RFC 5424 severity):

| Level | Numeric | Description |
|-------|---------|-------------|
| `debug` | 7 | Detailed debugging |
| `info` | 6 | Informational |
| `notice` | 5 | Normal but significant |
| `warning` | 4 | Warning conditions |
| `error` | 3 | Error conditions |
| `critical` | 2 | Critical conditions |
| `alert` | 1 | Immediate action required |
| `emergency` | 0 | System unusable |

**Log message fields**: `level: LoggingLevel`, `logger?: string`, `data: any`

---

### 9.2 Pagination

**Model**: Opaque cursor-based (no page numbers).

| Field | Type | Where | Description |
|-------|------|-------|-------------|
| `cursor` | `string` | Request params | Opaque cursor from previous response |
| `nextCursor` | `string?` | Response result | Cursor for next page (absent = end) |

**Paginated operations**: `resources/list`, `resources/templates/list`, `prompts/list`, `tools/list`, `tasks/list`

---

### 9.3 Completion (Autocompletion)

**Capability**: `completions` (server)

**Method**: `completion/complete` (Client -> Server)

| Field | Type | Description |
|-------|------|-------------|
| `params.ref` | `{type: "ref/prompt", name: string} \| {type: "ref/resource", uri: string}` | What is being completed |
| `params.argument` | `{name: string, value: string}` | Current argument being typed |
| `params.context` | `{arguments: Record<string, string>}` | Previously resolved arguments |

**CompleteResult**: `{completion: {values: string[] (max 100), total?: number, hasMore: boolean}}`

---

### 9.4 Progress

**Method**: `notifications/progress` (bidirectional)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `progressToken` | `string \| number` | YES | Token from original request's `_meta.progressToken` |
| `progress` | `number` | YES | Current progress (MUST increase) |
| `total` | `number` | NO | Total expected (may be floating point) |
| `message` | `string` | NO | Human-readable status |

---

### 9.5 Cancellation

**Method**: `notifications/cancelled` (bidirectional)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `requestId` | `string \| number` | YES | ID of request to cancel |
| `reason` | `string` | NO | Cancellation reason |

**Note**: For task-augmented requests, use `tasks/cancel` instead.

---

### 9.6 Tasks (Experimental, new in 2025-11-25)

**Purpose**: Durable state machines for expensive/long-running operations.

#### 9.6.1 Task Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `taskId` | `string` | YES | Unique ID (receiver-generated) |
| `status` | `TaskStatus` | YES | Current state |
| `statusMessage` | `string` | NO | Human-readable status message |
| `createdAt` | `string (ISO 8601)` | YES | Creation timestamp |
| `lastUpdatedAt` | `string (ISO 8601)` | YES | Last update timestamp |
| `ttl` | `number \| null` | YES | Lifetime in ms from creation (null = unlimited) |
| `pollInterval` | `number` | NO | Suggested polling interval in ms |

#### 9.6.2 TaskStatus Enum

| Status | Terminal? | Description |
|--------|-----------|-------------|
| `working` | NO | Being processed |
| `input_required` | NO | Receiver needs input from requestor |
| `completed` | YES | Successfully done |
| `failed` | YES | Execution failed |
| `cancelled` | YES | Cancelled by requestor |

**Valid transitions**: `working` -> `input_required \| completed \| failed \| cancelled`; `input_required` -> `working \| completed \| failed \| cancelled`

#### 9.6.3 Task Methods

| Method | Direction | Description |
|--------|-----------|-------------|
| `tasks/get` | Requestor -> Receiver | Poll task status |
| `tasks/result` | Requestor -> Receiver | Get final result (blocks until terminal) |
| `tasks/list` | Requestor -> Receiver | List tasks (paginated) |
| `tasks/cancel` | Requestor -> Receiver | Cancel a task |
| `notifications/tasks/status` | Receiver -> Requestor | Status change notification (optional) |

#### 9.6.4 Task-Augmented Requests

Add `task: {ttl?: number}` to any supported request params. Response becomes `CreateTaskResult` instead of the normal result.

#### 9.6.5 Tool-Level Task Negotiation

| `execution.taskSupport` value | Meaning |
|-------------------------------|---------|
| `"forbidden"` (default) | Tool MUST NOT be invoked as task |
| `"optional"` | Client MAY invoke as task or normal |
| `"required"` | Client MUST invoke as task |

---

## 10. Transports

### 10.1 stdio

| Aspect | Detail |
|--------|--------|
| Launch | Client spawns server as subprocess |
| Input | Server reads JSON-RPC from stdin |
| Output | Server writes JSON-RPC to stdout |
| Logging | Server MAY write to stderr |
| Delimiter | Newline-delimited; messages MUST NOT contain embedded newlines |
| Encoding | UTF-8 |
| Shutdown | Client closes stdin -> SIGTERM -> SIGKILL |

### 10.2 Streamable HTTP

| Aspect | Detail |
|--------|--------|
| Endpoint | Single HTTP endpoint supporting POST and GET |
| Client -> Server | HTTP POST with JSON-RPC body |
| Server -> Client | Response as `application/json` or `text/event-stream` (SSE) |
| Listening | Client MAY HTTP GET to open SSE stream for server-initiated messages |
| Session | Optional `MCP-Session-Id` header (set during init response) |
| Version header | `MCP-Protocol-Version: 2025-11-25` on all requests |
| Resumability | Optional SSE event IDs + `Last-Event-ID` for reconnection |
| Session termination | Client sends HTTP DELETE with session ID |

### 10.3 Custom Transports

Any bidirectional channel preserving JSON-RPC format and lifecycle requirements.

---

## 11. Complete Method Registry

### 11.1 Server Methods (Client -> Server)

| Method | Paginated | Capability required |
|--------|-----------|-------------------|
| `initialize` | NO | -- (lifecycle) |
| `ping` | NO | -- |
| `tools/list` | YES | `tools` |
| `tools/call` | NO | `tools` |
| `resources/list` | YES | `resources` |
| `resources/read` | NO | `resources` |
| `resources/templates/list` | YES | `resources` |
| `resources/subscribe` | NO | `resources.subscribe` |
| `resources/unsubscribe` | NO | `resources.subscribe` |
| `prompts/list` | YES | `prompts` |
| `prompts/get` | NO | `prompts` |
| `completion/complete` | NO | `completions` |
| `logging/setLevel` | NO | `logging` |
| `tasks/get` | NO | `tasks` |
| `tasks/result` | NO | `tasks` |
| `tasks/list` | YES | `tasks.list` |
| `tasks/cancel` | NO | `tasks.cancel` |

### 11.2 Client Methods (Server -> Client)

| Method | Capability required |
|--------|-------------------|
| `sampling/createMessage` | `sampling` |
| `roots/list` | `roots` |
| `elicitation/create` | `elicitation` |
| `tasks/get` | `tasks` |
| `tasks/result` | `tasks` |
| `tasks/list` | `tasks.list` |
| `tasks/cancel` | `tasks.cancel` |

### 11.3 Notifications (No response expected)

| Notification | Direction | Description |
|-------------|-----------|-------------|
| `notifications/initialized` | Client -> Server | Client ready after init |
| `notifications/cancelled` | Bidirectional | Cancel in-progress request |
| `notifications/progress` | Bidirectional | Progress update |
| `notifications/message` | Server -> Client | Log message |
| `notifications/tools/list_changed` | Server -> Client | Tool list changed |
| `notifications/resources/list_changed` | Server -> Client | Resource list changed |
| `notifications/resources/updated` | Server -> Client | Specific resource updated |
| `notifications/prompts/list_changed` | Server -> Client | Prompt list changed |
| `notifications/roots/list_changed` | Client -> Server | Root list changed |
| `notifications/tasks/status` | Receiver -> Requestor | Task status changed |
| `notifications/elicitation/complete` | Server -> Client | URL elicitation completed |

---

## 12. Mapping to CEX Pillars

| MCP Concept | CEX Pillar | CEX Kind(s) | Notes |
|-------------|-----------|-------------|-------|
| **Tool** | P04 Tools | `mcp_server`, `cli_tool`, `browser_tool` | MCP tools map directly to CEX P04 tool definitions |
| **Resource** | P01 Knowledge | `knowledge_card`, `rag_source`, `context_doc` | Resources = contextual data for LLMs, like CEX KCs |
| **Prompt** | P03 Prompt | `prompt_template`, `system_prompt`, `chain` | MCP prompts = templated message workflows |
| **Sampling** | P02 Model | `agent`, `model_provider`, `fallback_chain` | Sampling = LLM inference request, maps to model layer |
| **Root** | P09 Config | `path_config`, `env_config` | Filesystem boundaries = configuration |
| **Elicitation** | P11 Feedback | `quality_gate`, `guardrail` | User input requests during execution = feedback loop |
| **Task** | P12 Orchestration | `workflow`, `schedule`, `dispatch_rule` | Long-running state machines = orchestration |
| **Transport** | P08 Architecture | `interface`, `component_map` | Transport layer = architectural interface |
| **Capability** | P06 Schema | `schema`, `interface`, `type_def` | Capability negotiation = schema/contract |
| **Content types** | P05 Output | `output_template`, `formatter` | TextContent, ImageContent, etc. = output formats |
| **Logging** | P07 Evaluation | `scoring_rubric`, `benchmark` | Structured logging = evaluation/observability |
| **Authorization** | P09 Config | `secret_config`, `env_config` | OAuth/auth = security configuration |

### CEX-MCP Integration Points

| CEX Component | MCP Role | How They Connect |
|---------------|----------|-----------------|
| `cex_router.py` | Host/Client | Routes to MCP servers as tool providers |
| `_spawn/dispatch.sh` | Host | Spawns MCP server subprocesses via stdio transport |
| Builder ISOs | Prompt templates | Could be exposed as MCP prompts |
| Knowledge Cards | Resources | Could be served as MCP resources with `file://` URIs |
| `cex_score.py` | Tool | Could be exposed as an MCP tool for external agents |
| `cex_signal_watch.py` | Task polling | Conceptually equivalent to MCP task polling pattern |
| `signal_writer.py` | Notification | Equivalent to MCP notifications between nuclei |

---

## 13. Security Model Summary

| Principle | Enforcement |
|-----------|-------------|
| User consent for all data access | Host MUST obtain explicit consent |
| User control over tool invocation | Human-in-the-loop for tool calls |
| Data privacy | Host MUST NOT transmit resource data without consent |
| Tool annotations untrusted | Client treats annotations as advisory only |
| LLM sampling controls | User approves/edits prompts and results |
| Session isolation | Servers cannot see conversation or other servers |
| DNS rebinding protection | Validate Origin header on HTTP connections |
| Credential isolation | Servers MUST NOT request passwords via form-mode elicitation |

---

## 14. Protocol Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| `2024-11-05` | 2024-11-05 | Initial public spec. HTTP+SSE transport. |
| `2025-03-26` | 2025-03-26 | Streamable HTTP replaces HTTP+SSE. Audio content. Elicitation. |
| `2025-11-25` | 2025-11-25 | Tasks (experimental). URL-mode elicitation. Tool output schemas. Structured content. Tool-level task negotiation. Icons. |

---

## 15. SDK Implementations

| SDK | Language | Repository |
|-----|----------|-----------|
| Official TypeScript SDK | TypeScript/Node.js | `@modelcontextprotocol/sdk` |
| Official Python SDK | Python | `mcp` (PyPI) |
| Official Kotlin SDK | Kotlin/JVM | `modelcontextprotocol/kotlin-sdk` |
| Official C# SDK | C#/.NET | `modelcontextprotocol/csharp-sdk` |

---

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 |
| Domain | MCP protocol specification |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
