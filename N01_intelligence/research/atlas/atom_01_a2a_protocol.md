---
id: atom_01_a2a_protocol
kind: knowledge_card
pillar: P01
title: "A2A Protocol -- Complete Term Registry and Architecture Atlas"
version: 0.3.0
quality: 8.8
tags: [a2a, agent-to-agent, google, protocol, interoperability, json-rpc, grpc, agent-card]
sources:
  - https://a2a-protocol.org/latest/specification/
  - https://github.com/a2aproject/A2A
  - https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto
  - https://github.com/a2aproject/A2A/blob/main/docs/specification.md
  - https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
  - https://a2a-protocol.org/latest/topics/key-concepts/
  - https://agent2agent.info/docs/concepts/agentcard/
  - https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a-protocol-contract.html
date: 2026-04-13
spec_version: "0.3.0"
protobuf_package: "lf.a2a.v1"
governance: "Linux Foundation, contributed by Google"
license: "Apache-2.0"
---

# A2A Protocol -- Complete Term Registry and Architecture Atlas

## 1. Protocol Overview

The Agent2Agent (A2A) Protocol is an open standard enabling communication and
interoperability between opaque agentic applications. Introduced by Google in
April 2025, governed by the Linux Foundation. The canonical definition lives in
`specification/a2a.proto` (protobuf package `lf.a2a.v1`).

**Design Principles:**

| # | Principle | Detail |
|---|-----------|--------|
| 1 | Embrace agentic capabilities | Agents collaborate in unstructured modalities |
| 2 | Build on existing standards | HTTP, SSE, JSON-RPC 2.0, gRPC, protobuf |
| 3 | Secure by default | Enterprise-grade auth (OAuth2, mTLS, OIDC) |
| 4 | Long-running tasks | Hours/days with real-time feedback + state |
| 5 | Modality agnostic | Text, audio, video, structured data, files |

**Three-Layer Architecture:**

| Layer | Name | Purpose |
|-------|------|---------|
| L1 | Canonical Data Model | Protocol-agnostic structures (protobuf messages) |
| L2 | Abstract Operations | Binding-independent capabilities (11 operations) |
| L3 | Protocol Bindings | JSON-RPC 2.0, gRPC, HTTP+JSON/REST |

**Actors:**

| Actor | Role |
|-------|------|
| User | End user (human or automated service) initiating requests |
| A2A Client (Client Agent) | Application/agent that acts on behalf of the user |
| A2A Server (Remote Agent) | Agent exposing HTTP endpoint implementing A2A |

---

## 2. Full Term Registry

### 2.1 Core Data Types

#### Task

The stateful unit of work. Server-generated ID, defined lifecycle.

| Field | Type | Req | Description | Protocol Flow |
|-------|------|-----|-------------|---------------|
| id | string | Y | Unique task identifier (server-generated) | Created by SendMessage response |
| context_id | string | N | Groups related tasks in conversation | Threading multi-turn |
| status | TaskStatus | Y | Current lifecycle state | Updated by server during processing |
| artifacts | Artifact[] | N | Generated outputs | Populated during WORKING/COMPLETED |
| history | Message[] | N | Conversation message history | Trimmed by history_length param |
| metadata | map<string,Value> | N | Key-value context | Passed through request/response |

#### TaskStatus

| Field | Type | Req | Description | Protocol Flow |
|-------|------|-----|-------------|---------------|
| state | TaskState | Y | Current lifecycle state enum | Every status update |
| message | string | N | Human-readable status description | Optional context |
| timestamp | Timestamp | Y | Last status update time (ISO 8601) | Server-set |

#### TaskState (Enum)

| Value | Int | Description | Terminal? | Transition From |
|-------|-----|-------------|-----------|-----------------|
| UNSPECIFIED | 0 | Default/unknown | - | - |
| SUBMITTED | 1 | Task initialized, queued | N | (initial) |
| WORKING | 2 | Processing in progress | N | SUBMITTED, INPUT_REQUIRED |
| COMPLETED | 3 | Successfully finished | Y | WORKING |
| FAILED | 4 | Execution error occurred | Y | WORKING, SUBMITTED |
| CANCELED | 5 | Client-initiated cancellation | Y | SUBMITTED, WORKING, INPUT_REQUIRED |
| INPUT_REQUIRED | 6 | Awaiting additional user input | N | WORKING |
| REJECTED | 7 | Agent declined to process | Y | SUBMITTED |
| AUTH_REQUIRED | 8 | Awaiting authentication/authorization | N | SUBMITTED, WORKING |

#### Message

| Field | Type | Req | Description | Protocol Flow |
|-------|------|-----|-------------|---------------|
| message_id | string | N | Unique message identifier | Idempotency key |
| context_id | string | N | Associated conversation context | Threading |
| task_id | string | N | Associated task reference | Follow-up messages |
| role | Role | Y | "user" or "agent" | Every message |
| parts | Part[] | Y | Content parts (multimodal) | Payload carrier |
| metadata | map<string,Value> | N | Custom key-value data | Pass-through |
| extensions | AgentExtension[] | N | Extension declarations | Extensibility |
| reference_task_ids | string[] | N | Related task references | Cross-task linking |

#### Role (Enum)

| Value | Int | Description |
|-------|-----|-------------|
| UNSPECIFIED | 0 | Default |
| USER | 1 | Message from client/user |
| AGENT | 2 | Message from A2A server |

#### Part

Fundamental content container. Uses oneof for content type.

| Field | Type | Req | Description | Protocol Flow |
|-------|------|-----|-------------|---------------|
| text | string | oneof | Plain text content | Most common |
| raw | bytes | oneof | Inline binary data | File uploads |
| url | string | oneof | URI to external content | Large files |
| data | Struct | oneof | Structured JSON values | Typed payloads |
| metadata | map<string,Value> | N | Part-level metadata | Context |
| filename | string | N | Human-readable filename | File parts |
| media_type | string | N | MIME type (e.g., "text/plain") | Content negotiation |

#### Artifact

Tangible output generated by agent during task processing.

| Field | Type | Req | Description | Protocol Flow |
|-------|------|-----|-------------|---------------|
| artifact_id | string | Y | Unique artifact identifier | Created during WORKING |
| name | string | N | Human-readable name | Display |
| description | string | N | Purpose/content description | Discovery |
| parts | Part[] | Y | Artifact content parts | Payload |
| metadata | map<string,Value> | N | Custom properties | Pass-through |
| extensions | AgentExtension[] | N | Extension data | Extensibility |

### 2.2 Agent Discovery Types

#### AgentCard

JSON metadata document at `/.well-known/agent-card.json`. The agent's "business card."

| Field | Type | Req | Description | Protocol Flow |
|-------|------|-----|-------------|---------------|
| name | string | Y | Display name | Discovery |
| description | string | N | Purpose description | Discovery |
| supported_interfaces | AgentInterface[] | Y | Protocol endpoints (ordered) | Connection |
| provider | AgentProvider | N | Organization info | Trust |
| version | string | Y | Card version | Compatibility |
| documentation_url | string | N | External docs link | Reference |
| capabilities | AgentCapabilities | Y | Feature support matrix | Negotiation |
| security_schemes | map<string,SecurityScheme> | N | Auth requirements (named) | Authentication |
| security_requirements | SecurityRequirement[] | N | Applied auth scopes | Authorization |
| default_input_modes | string[] | N | Default accepted MIME types | Content negotiation |
| default_output_modes | string[] | N | Default produced MIME types | Content negotiation |
| skills | AgentSkill[] | N | Available operations | Capability routing |
| signatures | AgentCardSignature[] | N | Cryptographic verification | Trust |
| icon_url | string | N | Agent branding image | UI display |

#### AgentInterface

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| url | string | Y | Service endpoint URL |
| protocol_binding | string | Y | "jsonrpc", "grpc", "rest" |
| tenant | string | N | Default tenant identifier |
| protocol_version | string | N | A2A version (e.g., "0.3") |

#### AgentProvider

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| url | string | N | Provider website |
| organization | string | N | Organization name |

#### AgentCapabilities

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| streaming | bool | N | Supports SSE updates |
| push_notifications | bool | N | Webhook delivery supported |
| extensions | AgentExtension[] | N | Supported extensions |
| extended_agent_card | bool | N | Authenticated card available |

#### AgentSkill

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| id | string | Y | Skill identifier |
| name | string | Y | Display name |
| description | string | N | Purpose/behavior |
| tags | string[] | N | Discovery keywords |
| examples | string[] | N | Sample prompts |
| input_modes | string[] | N | Accepted MIME types (skill-specific) |
| output_modes | string[] | N | Produced MIME types (skill-specific) |
| security_requirements | SecurityRequirement[] | N | Skill-level auth |

#### AgentExtension

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| uri | string | Y | Extension identifier URI |
| description | string | N | Purpose |
| required | bool | N | Must support to interact |
| params | Struct | N | Extension parameters |

#### AgentCardSignature (JWS Compact Serialization)

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| protected | string | Y | Base64url-encoded JWS header |
| signature | string | Y | Base64url-encoded signature |
| header | Struct | N | Unprotected JWS header |

### 2.3 Security Scheme Types

SecurityScheme is a discriminated union (oneof):

#### APIKeySecurityScheme

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| description | string | N | Usage instructions |
| location | string | Y | "header" or "query" |
| name | string | Y | Header/parameter name |

#### HTTPAuthSecurityScheme

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| description | string | N | Usage guidance |
| scheme | string | Y | "bearer", "basic", etc. |
| bearer_format | string | N | Token format (e.g., "JWT") |

#### OAuth2SecurityScheme

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| description | string | N | Documentation |
| flows | OAuthFlows | Y | Authorization flow variants |
| oauth2_metadata_url | string | N | RFC 8414 metadata endpoint |

#### OpenIdConnectSecurityScheme

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| description | string | N | Documentation |
| open_id_connect_url | string | Y | OIDC discovery endpoint |

#### MutualTlsSecurityScheme

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| description | string | N | Certificate requirements |

### 2.4 OAuth Flow Types

OAuthFlows is a discriminated union (oneof):

#### AuthorizationCodeOAuthFlow

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| authorization_url | string | Y | Auth endpoint |
| token_url | string | Y | Token exchange URL |
| refresh_url | string | N | Refresh token endpoint |
| scopes | map<string,string> | Y | Scope definitions |
| pkce_required | bool | N | PKCE enforcement |

#### ClientCredentialsOAuthFlow

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| token_url | string | Y | Token acquisition endpoint |
| refresh_url | string | N | Token refresh endpoint |
| scopes | map<string,string> | Y | Available scopes |

#### ImplicitOAuthFlow (DEPRECATED)

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| authorization_url | string | Y | Auth endpoint |
| refresh_url | string | N | Refresh endpoint |
| scopes | map<string,string> | Y | Scopes |

#### PasswordOAuthFlow (DEPRECATED)

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| token_url | string | Y | Token endpoint |
| refresh_url | string | N | Refresh endpoint |
| scopes | map<string,string> | Y | Scopes |

#### DeviceCodeOAuthFlow

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| device_authorization_url | string | Y | Device code endpoint |
| token_url | string | Y | Token exchange URL |
| refresh_url | string | N | Refresh endpoint |
| scopes | map<string,string> | Y | Scopes |

### 2.5 Security Enforcement Types

#### SecurityRequirement

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| schemes | map<string,StringList> | Y | Scheme name -> required scopes |

#### AuthenticationInfo

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| scheme | string | Y | Scheme name (references security_schemes) |
| credentials | string | N | Auth credentials |

### 2.6 Push Notification Types

#### TaskPushNotificationConfig

| Field | Type | Req | Description | Protocol Flow |
|-------|------|-----|-------------|---------------|
| tenant | string | N | Tenant scope | Multi-tenancy |
| id | string | Y | Config identifier (server-generated) | CRUD reference |
| task_id | string | Y | Associated task | Binding |
| url | string | Y | Webhook callback endpoint | Delivery target |
| token | string | N | Opaque validation token | Client-set, echoed back |
| authentication | AuthenticationInfo | N | Webhook auth details | Outbound auth |

### 2.7 Request/Response Types

#### SendMessageRequest

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| tenant | string | N | Tenant identifier |
| message | Message | Y | Content to send |
| configuration | SendMessageConfiguration | N | Execution options |
| metadata | map<string,Value> | N | Custom context |

#### SendMessageConfiguration

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| accepted_output_modes | string[] | N | Desired response MIME types |
| task_push_notification_config | TaskPushNotificationConfig | N | Webhook setup |
| history_length | int32 | N | Max messages in response |
| return_immediately | bool | N | Async (true) vs blocking (false) |

#### SendMessageResponse (oneof payload)

| Variant | Type | When |
|---------|------|------|
| task | Task | Server created/updated a task |
| message | Message | Server responds directly (stateless) |

#### StreamResponse (oneof payload)

| Variant | Type | When |
|---------|------|------|
| task | Task | Initial task state |
| message | Message | Direct message response |
| status_update | TaskStatusUpdateEvent | State transition |
| artifact_update | TaskArtifactUpdateEvent | New/updated artifact |

#### GetTaskRequest

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| tenant | string | N | Tenant scope |
| id | string | Y | Task identifier |
| history_length | int32 | N | Max history messages |

#### ListTasksRequest

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| tenant | string | N | Tenant scope |
| context_id | string | N | Filter by conversation |
| status | TaskState | N | Filter by state |
| page_size | int32 | N | Max results (1-100) |
| page_token | string | N | Pagination cursor |
| history_length | int32 | N | Message inclusion limit |
| status_timestamp_after | Timestamp | N | Filter by update time |
| include_artifacts | bool | N | Include outputs in response |

#### ListTasksResponse

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| tasks | Task[] | Y | Matching tasks |
| next_page_token | string | Y | Cursor (empty = last page) |
| page_size | int32 | Y | Returned count |
| total_size | int32 | Y | Total available |

#### CancelTaskRequest

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| tenant | string | N | Tenant scope |
| id | string | Y | Task identifier |
| metadata | map<string,Value> | N | Context |

#### SubscribeToTaskRequest

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| tenant | string | N | Tenant scope |
| id | string | Y | Task identifier |

#### GetExtendedAgentCardRequest

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| tenant | string | N | Tenant scope |

### 2.8 Streaming Event Types

#### TaskStatusUpdateEvent

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| task_id | string | Y | Associated task |
| context_id | string | N | Conversation context |
| status | TaskStatus | Y | New status |
| metadata | map<string,Value> | N | Event context |

#### TaskArtifactUpdateEvent

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| task_id | string | Y | Associated task |
| context_id | string | N | Conversation context |
| artifact | Artifact | Y | New/updated artifact |
| append | bool | N | Append to existing artifact |
| last_chunk | bool | N | Final chunk indicator |
| metadata | map<string,Value> | N | Event context |

### 2.9 Utility Types

#### StringList

| Field | Type | Description |
|-------|------|-------------|
| list | string[] | Generic string list (used in SecurityRequirement) |

---

## 3. Message Flow Diagrams

### 3.1 Synchronous Request/Response

```
Client                                          Server
  |                                               |
  |  POST /.well-known/agent-card.json            |
  |---------------------------------------------->|
  |  AgentCard (capabilities, skills, auth)       |
  |<----------------------------------------------|
  |                                               |
  |  JSON-RPC: sendMessage(Message)               |
  |---------------------------------------------->|
  |                                               |
  |  SendMessageResponse(Task | Message)          |
  |<----------------------------------------------|
  |                                               |
  |  [if Task returned, poll:]                    |
  |  JSON-RPC: getTask(id)                        |
  |---------------------------------------------->|
  |  Task (status=WORKING)                        |
  |<----------------------------------------------|
  |                                               |
  |  JSON-RPC: getTask(id)                        |
  |---------------------------------------------->|
  |  Task (status=COMPLETED, artifacts=[...])     |
  |<----------------------------------------------|
```

### 3.2 Streaming (SSE)

```
Client                                          Server
  |                                               |
  |  JSON-RPC: sendStreamingMessage(Message)      |
  |---------------------------------------------->|
  |                                               |
  |  event: task                                  |
  |  data: {id:"t1", status:{state:SUBMITTED}}    |
  |<----------------------------------------------|
  |                                               |
  |  event: status_update                         |
  |  data: {task_id:"t1", status:{state:WORKING}} |
  |<----------------------------------------------|
  |                                               |
  |  event: artifact_update                       |
  |  data: {task_id:"t1", artifact:{...},         |
  |         last_chunk:false}                     |
  |<----------------------------------------------|
  |                                               |
  |  event: artifact_update                       |
  |  data: {task_id:"t1", artifact:{...},         |
  |         last_chunk:true}                      |
  |<----------------------------------------------|
  |                                               |
  |  event: status_update                         |
  |  data: {task_id:"t1", status:{state:COMPLETED}|
  |<----------------------------------------------|
  |  [SSE stream closes]                          |
```

### 3.3 Push Notifications (Async)

```
Client                                          Server
  |                                               |
  |  sendMessage(msg, config:{                    |
  |    return_immediately: true,                  |
  |    task_push_notification_config: {           |
  |      url: "https://client/webhook",           |
  |      authentication: {...}                    |
  |    }                                          |
  |  })                                           |
  |---------------------------------------------->|
  |  Task (status=SUBMITTED)                      |
  |<----------------------------------------------|
  |                                               |
  |  [Server processes asynchronously...]         |
  |                                               |
  |  POST https://client/webhook                  |
  |  {TaskStatusUpdateEvent: WORKING}             |
  |<----------------------------------------------|
  |                                               |
  |  POST https://client/webhook                  |
  |  {TaskArtifactUpdateEvent: {...}}             |
  |<----------------------------------------------|
  |                                               |
  |  POST https://client/webhook                  |
  |  {TaskStatusUpdateEvent: COMPLETED}           |
  |<----------------------------------------------|
```

### 3.4 Multi-Turn Conversation

```
Client                                          Server
  |                                               |
  |  sendMessage(msg_1)                           |
  |---------------------------------------------->|
  |  Task(id:t1, context_id:ctx1,                 |
  |       status:INPUT_REQUIRED)                  |
  |<----------------------------------------------|
  |                                               |
  |  sendMessage(msg_2, task_id:t1, ctx:ctx1)     |
  |---------------------------------------------->|
  |  Task(id:t1, context_id:ctx1,                 |
  |       status:COMPLETED, artifacts:[...])      |
  |<----------------------------------------------|
```

### 3.5 Task Lifecycle State Machine

```
                    +---> REJECTED (terminal)
                    |
(new) ---> SUBMITTED ---+---> WORKING ---+---> COMPLETED (terminal)
                    |        |    ^      |
                    |        |    |      +---> FAILED (terminal)
                    |        v    |
                    |   INPUT_REQUIRED
                    |        |
                    |        v
                    |   AUTH_REQUIRED
                    |
                    +---> CANCELED (terminal)
                          (from any non-terminal)
```

---

## 4. Agent Card Schema (Complete)

### 4.1 Discovery Mechanism

| Aspect | Detail |
|--------|--------|
| Standard URL | `https://<base_url>/.well-known/agent-card.json` |
| HTTP Method | GET (unauthenticated for public card) |
| RFC | 8615 (Well-Known URIs) |
| Extended Card | GET via `getExtendedAgentCard` (authenticated) |
| Format | JSON with camelCase field names |

### 4.2 Full Field Hierarchy

```
AgentCard
+-- name: string (required)
+-- description: string
+-- supported_interfaces: AgentInterface[] (required)
|   +-- url: string (required)
|   +-- protocol_binding: string (required) ["jsonrpc"|"grpc"|"rest"]
|   +-- tenant: string
|   +-- protocol_version: string
+-- provider: AgentProvider
|   +-- url: string
|   +-- organization: string
+-- version: string (required)
+-- documentation_url: string
+-- capabilities: AgentCapabilities (required)
|   +-- streaming: bool
|   +-- push_notifications: bool
|   +-- extensions: AgentExtension[]
|   +-- extended_agent_card: bool
+-- security_schemes: map<string, SecurityScheme>
|   +-- [name]: APIKeySecurityScheme | HTTPAuthSecurityScheme |
|               OAuth2SecurityScheme | OpenIdConnectSecurityScheme |
|               MutualTlsSecurityScheme
+-- security_requirements: SecurityRequirement[]
|   +-- schemes: map<string, StringList>
+-- default_input_modes: string[] (MIME types)
+-- default_output_modes: string[] (MIME types)
+-- skills: AgentSkill[]
|   +-- id: string (required)
|   +-- name: string (required)
|   +-- description: string
|   +-- tags: string[]
|   +-- examples: string[]
|   +-- input_modes: string[]
|   +-- output_modes: string[]
|   +-- security_requirements: SecurityRequirement[]
+-- signatures: AgentCardSignature[]
|   +-- protected: string (required, base64url JWS header)
|   +-- signature: string (required, base64url)
|   +-- header: Struct
+-- icon_url: string
```

### 4.3 Example Agent Card (JSON-RPC binding)

```json
{
  "name": "Research Agent",
  "description": "Deep research across academic papers",
  "version": "1.0.0",
  "supportedInterfaces": [
    {
      "url": "https://research.example.com/a2a",
      "protocolBinding": "jsonrpc",
      "protocolVersion": "0.3"
    }
  ],
  "capabilities": {
    "streaming": true,
    "pushNotifications": true,
    "extendedAgentCard": false
  },
  "defaultInputModes": ["text/plain", "application/json"],
  "defaultOutputModes": ["text/plain", "text/markdown"],
  "skills": [
    {
      "id": "paper_search",
      "name": "Academic Paper Search",
      "description": "Search and summarize academic papers",
      "tags": ["research", "papers", "academic"],
      "examples": ["Find papers on transformer architectures"]
    }
  ],
  "securitySchemes": {
    "bearer": {
      "type": "http",
      "scheme": "bearer",
      "bearerFormat": "JWT"
    }
  },
  "securityRequirements": [
    { "bearer": [] }
  ]
}
```

---

## 5. Protocol Operations (Layer 2)

### 5.1 A2AService RPC Methods

| # | Method | Request | Response | Streaming | Description |
|---|--------|---------|----------|-----------|-------------|
| 1 | SendMessage | SendMessageRequest | SendMessageResponse | No | Send message, get Task or Message |
| 2 | SendStreamingMessage | SendMessageRequest | stream StreamResponse | Server | Real-time SSE updates |
| 3 | GetTask | GetTaskRequest | Task | No | Retrieve task state |
| 4 | ListTasks | ListTasksRequest | ListTasksResponse | No | Paginated task listing |
| 5 | CancelTask | CancelTaskRequest | Task | No | Request task cancellation |
| 6 | SubscribeToTask | SubscribeToTaskRequest | stream StreamResponse | Server | Monitor non-terminal task |
| 7 | CreateTaskPushNotificationConfig | TaskPushNotificationConfig | TaskPushNotificationConfig | No | Register webhook |
| 8 | GetTaskPushNotificationConfig | GetTaskPushNotificationConfigRequest | TaskPushNotificationConfig | No | Read webhook config |
| 9 | ListTaskPushNotificationConfigs | ListTaskPushNotificationConfigsRequest | ListTaskPushNotificationConfigsResponse | No | List webhooks |
| 10 | DeleteTaskPushNotificationConfig | DeleteTaskPushNotificationConfigRequest | google.protobuf.Empty | No | Remove webhook |
| 11 | GetExtendedAgentCard | GetExtendedAgentCardRequest | AgentCard | No | Authenticated card |

### 5.2 JSON-RPC Method Names

| Operation | JSON-RPC Method |
|-----------|----------------|
| SendMessage | `sendMessage` |
| SendStreamingMessage | `sendStreamingMessage` |
| GetTask | `getTask` |
| ListTasks | `listTasks` |
| CancelTask | `cancelTask` |
| SubscribeToTask | `subscribeToTask` |
| CreateTaskPushNotificationConfig | `createTaskPushNotificationConfig` |
| GetTaskPushNotificationConfig | `getTaskPushNotificationConfig` |
| ListTaskPushNotificationConfigs | `listTaskPushNotificationConfigs` |
| DeleteTaskPushNotificationConfig | `deleteTaskPushNotificationConfig` |
| GetExtendedAgentCard | `getExtendedAgentCard` |

### 5.3 HTTP/REST Endpoint Patterns

| Method | Path | Operation |
|--------|------|-----------|
| POST | /tenants/{tenant}/messages | sendMessage |
| POST | /tenants/{tenant}/messages:stream | sendStreamingMessage |
| GET | /tenants/{tenant}/tasks/{id} | getTask |
| GET | /tenants/{tenant}/tasks | listTasks |
| DELETE | /tenants/{tenant}/tasks/{id} | cancelTask |
| GET | /tenants/{tenant}/tasks/{id}:subscribe | subscribeToTask (SSE) |
| POST | /tenants/{tenant}/tasks/{taskId}/pushNotificationConfigs | createPushNotif |
| GET | /tenants/{tenant}/tasks/{taskId}/pushNotificationConfigs/{id} | getPushNotif |
| GET | /tenants/{tenant}/tasks/{taskId}/pushNotificationConfigs | listPushNotifs |
| DELETE | /tenants/{tenant}/tasks/{taskId}/pushNotificationConfigs/{id} | deletePushNotif |
| GET | /tenants/{tenant}/agentCard:extended | getExtendedAgentCard |

### 5.4 Service Parameters (Headers)

| Header | Description | Example |
|--------|-------------|---------|
| A2A-Version | Protocol version negotiation | "0.3" |
| A2A-Extensions | Comma-separated extension URIs | "urn:a2a:ext:tracing" |

### 5.5 gRPC Metadata Keys

| Key | Maps To |
|-----|---------|
| a2a-version | A2A-Version header |
| a2a-extensions | A2A-Extensions header |

---

## 6. Error Codes

### 6.1 A2A-Specific Errors

| Error Name | Description | When |
|------------|-------------|------|
| TaskNotFoundError | Task ID invalid, expired, or inaccessible | getTask, cancelTask with bad ID |
| TaskNotCancelableError | Task in terminal state | cancelTask on COMPLETED/FAILED |
| PushNotificationNotSupportedError | Agent lacks push capability | createPushNotif when not supported |
| UnsupportedOperationError | Feature not implemented | Any unsupported method |
| ContentTypeNotSupportedError | MIME type not accepted | Part with unsupported media_type |
| InvalidAgentResponseError | Agent response malformed | Server-side processing error |
| ExtendedAgentCardNotConfiguredError | Extended card unavailable | getExtendedAgentCard when not configured |
| ExtensionSupportRequiredError | Required extension not declared | Missing required extension |
| VersionNotSupportedError | Protocol version mismatch | Version negotiation failure |

### 6.2 HTTP Status Code Mappings

| HTTP Code | Meaning |
|-----------|---------|
| 200 | Success (JSON-RPC errors still return 200) |
| 400 | Bad Request / Validation error |
| 401 | Unauthorized (missing auth) |
| 403 | Forbidden (insufficient permissions) |
| 404 | Not Found |
| 429 | Rate limited (AWS: ThrottlingException) |
| 500 | Internal Server Error |

### 6.3 AWS-Specific JSON-RPC Error Codes

| Code | Exception | HTTP Equivalent |
|------|-----------|-----------------|
| -32501 | ResourceNotFoundException | 404 |
| -32052 | ValidationException | 400 |
| -32053 | ThrottlingException | 429 |
| -32054 | ResourceConflictException | 409 |
| -32055 | RuntimeClientError | 424 |

---

## 7. Authentication Mechanisms

| Scheme Type | Auth Header | Use Case |
|-------------|-------------|----------|
| API Key | Custom header or query param | Simple machine-to-machine |
| HTTP Bearer | `Authorization: Bearer <token>` | JWT/OAuth tokens |
| HTTP Basic | `Authorization: Basic <b64>` | Username/password |
| OAuth 2.0 (AuthCode) | `Authorization: Bearer <token>` | User-delegated access (3-legged) |
| OAuth 2.0 (Client Credentials) | `Authorization: Bearer <token>` | Machine-to-machine (2-legged) |
| OAuth 2.0 (Device Code) | `Authorization: Bearer <token>` | IoT/CLI devices |
| OpenID Connect | `Authorization: Bearer <token>` | Identity + auth combined |
| Mutual TLS | Client certificate | Zero-trust environments |
| AWS SigV4 | `Authorization: AWS4-HMAC-SHA256 ...` | AWS Bedrock integration |

---

## 8. Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| 0.1 | Apr 2025 | Initial release. JSON-RPC only. Basic Task/Message/Part model. |
| 0.2 | May 2025 | Stateless interactions (Message-only responses). OpenAPI-like auth formalization. Python SDK release. |
| 0.3 | 2025-2026 | gRPC binding. Agent Card signing. Protobuf as canonical source. HTTP/REST binding. Extensions mechanism. Multi-tenant support. DeviceCode OAuth. PKCE. |

---

## 9. A2A vs MCP Comparison

| Dimension | A2A | MCP (Anthropic) |
|-----------|-----|-----------------|
| Purpose | Agent-to-agent communication | Agent-to-tool communication |
| Topology | Many-to-many mesh | Hub-and-spoke (host -> servers) |
| Discovery | Agent Card at well-known URL | Server capabilities via initialize |
| Task model | Stateful tasks with lifecycle | Stateless tool calls |
| Streaming | SSE + gRPC server streaming | SSE (stdio or HTTP) |
| Auth | OAuth2, mTLS, OIDC, API key | OAuth2 (streamable HTTP) |
| Async | Push notifications + polling | No native async |
| Output | Artifacts (typed, multi-part) | Tool results (content array) |
| Complementary | Uses MCP for tool access | Uses A2A for agent delegation |

---

## 10. CEX Pillar Mapping

How each A2A concept maps to the CEX 12-pillar architecture:

| A2A Concept | CEX Pillar | CEX Kind | Rationale |
|-------------|-----------|----------|-----------|
| AgentCard | P08 Architecture | agent_card | Agent metadata descriptor, capability manifest |
| AgentSkill | P02 Model | agent | Discrete capability = CEX agent definition |
| Task | P12 Orchestration | workflow | Stateful unit of work with lifecycle |
| TaskState | P12 Orchestration | dispatch_rule | State machine governing task flow |
| Message | P03 Prompt | prompt_template | Communication turn with role + content |
| Part (text) | P03 Prompt | action_prompt | Text content payload |
| Part (data) | P06 Schema | input_schema | Structured JSON payload |
| Part (file) | P05 Output | output_template | File/binary content |
| Artifact | P05 Output | output_template | Generated output with typed parts |
| SecurityScheme | P09 Config | secret_config | Auth configuration per scheme |
| OAuth2 flows | P09 Config | env_config | Runtime auth environment |
| Push notifications | P09 Config | webhook | Async callback configuration |
| Agent discovery | P10 Memory | knowledge_index | Registry of known agents |
| context_id | P10 Memory | memory_scope | Conversation threading state |
| Extensions | P06 Schema | interface | Protocol extension contracts |
| Error codes | P11 Feedback | quality_gate | Error handling and validation |
| Streaming (SSE) | P04 Tools | api_client | Real-time transport mechanism |
| gRPC binding | P04 Tools | api_client | Binary transport mechanism |
| JSON-RPC binding | P04 Tools | api_client | Text transport mechanism |
| AgentProvider | P08 Architecture | component_map | Organization/provider metadata |
| AgentInterface | P08 Architecture | interface | Endpoint + binding declaration |
| AgentCapabilities | P08 Architecture | agent_card | Feature negotiation matrix |
| Multi-tenancy | P09 Config | env_config | Tenant isolation configuration |
| Task history | P10 Memory | entity_memory | Conversation message persistence |
| Pagination | P06 Schema | validation_schema | List query constraints |
| Content negotiation | P06 Schema | type_def | MIME type compatibility contract |
| Card signing | P09 Config | secret_config | Cryptographic trust chain |

---

## 11. Implementation Ecosystem

### 11.1 Official SDKs

| Language | Package | Source |
|----------|---------|--------|
| Python | `pip install a2a-sdk` | a2aproject/a2a-python |
| Go | `go get` | a2aproject/a2a-go |
| JavaScript | npm | a2aproject/a2a-js |
| Java | Maven | a2aproject/a2a-java |
| .NET | NuGet | a2aproject/a2a-dotnet |

### 11.2 Platform Integrations

| Platform | Integration |
|----------|-------------|
| Google Vertex AI (Agent Engine) | Native A2A endpoint support |
| AWS Bedrock AgentCore | A2A protocol contract for containers |
| LangChain/LangGraph | A2A endpoint in Agent Server |
| Microsoft Semantic Kernel | A2A client/server adapters |
| CrewAI, AutoGen | Community adapters |

### 11.3 Industry Partners (50+)

Atlassian, Box, Cohere, Intuit, LangChain, MongoDB, PayPal, Salesforce,
SAP (Joule), ServiceNow, UKG, Workday, Auth0, Microsoft (Azure AI Foundry),
Zoom, plus consulting firms: Accenture, BCG, Capgemini, Cognizant, Deloitte,
HCLTech, Infosys, KPMG, McKinsey, PwC, TCS, Wipro.

---

## 12. Key Protocol Patterns

### 12.1 Stateless vs Stateful

| Pattern | SendMessage returns | Use case |
|---------|-------------------|----------|
| Stateless | Message (direct) | Simple Q&A, no task tracking needed |
| Stateful | Task (with ID) | Long-running work, multi-turn, async |

### 12.2 Content Negotiation

Client specifies `accepted_output_modes` in SendMessageConfiguration.
Server checks against `default_output_modes` and skill-level `output_modes`.
If no overlap, server returns ContentTypeNotSupportedError.

### 12.3 Idempotency

Messages carry `message_id`. Resending same ID = same result (no duplicate processing).

### 12.4 Multi-Tenancy

All operations accept optional `tenant` parameter for workspace isolation.
AgentInterface declares default tenant. REST paths include `/tenants/{tenant}/`.

### 12.5 Extension Protocol

1. Server declares extensions in AgentCard `capabilities.extensions[]`
2. Client sends `A2A-Extensions` header with required URIs
3. If server requires extension client lacks: ExtensionSupportRequiredError
4. Extensions use semantic versioning; breaking changes = major bump

---

## 13. Glossary (Alphabetical)

| Term | Definition |
|------|------------|
| A2A Client | Application acting on behalf of user, sends messages to server |
| A2A Server | Agent exposing HTTP endpoint implementing A2A protocol |
| Agent Card | JSON metadata document describing agent identity and capabilities |
| Agent Extension | Custom protocol extension declared in AgentCard |
| Agent Interface | URL + protocol binding + version for connecting to agent |
| Agent Provider | Organization/company behind an agent |
| Agent Skill | Discrete capability an agent can perform |
| Artifact | Tangible output generated by agent during task processing |
| Capability | Feature flag in AgentCard (streaming, push, extended card) |
| Content Negotiation | MIME type matching between client and server |
| Context ID | Server-generated identifier grouping related tasks |
| Extended Agent Card | Authenticated version of AgentCard with additional detail |
| Message | Single communication turn with role (user/agent) and parts |
| Multi-Turn | Conversation continuity via context_id and task_id |
| Part | Fundamental content container (text/raw/url/data) |
| Protocol Binding | Concrete transport mapping (JSON-RPC, gRPC, REST) |
| Push Notification | Webhook-based async delivery of task events |
| Role | Message sender type: USER or AGENT |
| Security Requirement | Applied auth scopes for card or skill |
| Security Scheme | Authentication mechanism definition |
| SSE (Server-Sent Events) | HTTP streaming for real-time task updates |
| Task | Stateful unit of work with unique ID and lifecycle |
| Task State | Lifecycle enum (SUBMITTED -> WORKING -> COMPLETED/FAILED) |
| Tenant | Workspace isolation identifier for multi-tenancy |
| Well-Known URL | `/.well-known/agent-card.json` per RFC 8615 |
