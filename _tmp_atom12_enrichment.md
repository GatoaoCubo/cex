
### 14.1 Manifest Schema (Complete Field Reference)

The plugin manifest (`manifest.yaml`) is read by the Dify plugin daemon at startup.

```yaml
version: 0.0.1                    # semver -- plugin version
type: plugin                      # always "plugin"
author: your-handle               # alphanumeric + hyphens
name: my-plugin                   # ^[a-z0-9_-]{1,128}$
label:
  en_US: "My Plugin"
  zh_Hans: "..."
  pt_BR: "..."
  ja_JP: "..."
description:
  en_US: "What this plugin does"
icon: icon.svg
resource:
  memory: 268435456               # bytes; 256MB default
permission:
  tool:
    enabled: true                 # can register tool providers
  model:
    enabled: false                # can register model providers
  llm:
    enabled: true                 # can invoke LLMs via reverse call
  endpoint:
    enabled: true                 # can register HTTP endpoints
  app:
    enabled: true                 # can invoke Dify apps
  storage:
    enabled: true                 # persistent KV storage
    size: 1048576                 # bytes (1KB - 1GB)
plugins:
  tools:
    - provider/my_provider.yaml
meta:
  version: 0.0.2                  # manifest spec version
  minimum_dify_version: "1.6.0"
  arch:
    - amd64
    - arm64
  runner:
    language: python
    version: "3.12"
    entrypoint: main
created_at: 2025-01-24T13:25:50.107915+09:00
privacy: PRIVACY.md
verified: false
```

### 14.2 meta.version Compatibility Table

| meta.version | New capability | Older plugin on newer Dify |
|---|---|---|
| 0.0.2 | Supports `mcp` ToolProviderType | Older version disables MCP tools |
| 0.0.1 | Initial release | N/A |

### 14.3 SDK / Dify Version Matrix

| Dify Version | SDK Version | Feature Unlocked |
|---|---|---|
| 1.2.0 | 0.2.0 | Application info fetching |
| 1.4.0 | 0.3.1 | OAuth plugin support |
| 1.5.1 | 0.4.0 | Dynamic-select parameters + LLM structured output |
| 1.6.0 | 0.4.1 | Dark-icon manifest + native MCP server |
| 1.7.0 | 0.4.2 | OAuth functionality |
| 1.8.1 | 0.4.4 | Filename in MultiModalPromptMessageContent |
| 1.9.0 | 0.5.0 | Datasource (Knowledge Pipeline) plugins |
| 1.10.0 | 0.6.0 | Trigger plugin type |
| 1.11.0 | 0.7.0 | Multimodal reranking + embeddings |

Source: https://github.com/langgenius/dify-plugin-sdks

### 14.4 Tool Provider YAML Schema

```yaml
identity:
  author: your-handle
  name: provider-name
  label:
    en_US: "Provider Display Name"
  description:
    en_US: "What this provider does"
  icon: icon.svg
  tags: [search, productivity]
credentials_for_provider:
  api_key:
    type: secret-input
    required: true
    label:
      en_US: "API Key"
    placeholder:
      en_US: "sk-..."
    help:
      en_US: "Obtain from settings page"
tools:
  - tools/my_tool.yaml
```

### 14.5 Tool YAML Schema

```yaml
identity:
  name: tool-name
  author: your-handle
  label:
    en_US: "Tool Display Name"
description:
  human:
    en_US: "Human-readable description shown in UI"
  llm: "Terse description optimized for LLM tool selection"
parameters:
  - name: query
    type: string
    required: true
    label:
      en_US: "Search Query"
    llm_description: "The search query string"
    form: llm
  - name: limit
    type: number
    required: false
    default: 10
    min: 1
    max: 100
    form: form
output_schema:
  type: object
  properties:
    result_count:
      type: number
      description: "Number of results found"
    results:
      type: array
      description: "Search results array"
```

### 14.6 Parameter Types -- Complete Enumeration

| Type | Usage | Notes |
|---|---|---|
| `secret-input` | API keys, passwords | Masked in UI, not logged |
| `text-input` | Short text strings | Single line |
| `string` | General string | Multi-context |
| `number` | Integers + floats | Supports min/max/precision |
| `boolean` | True/false toggle | -- |
| `checkbox` | UI toggle in form | Alias for boolean |
| `select` | Enum dropdown | Requires `options` list |
| `file` | Single file upload | MIME type filtering |
| `files` | Multiple file upload | Array of files |
| `app-selector` | Pick a Dify app | Reverse-invocation context |
| `model-selector` | Pick model + provider | Provider + model combo |
| `tools_selector` | Pick tool(s) | Agent strategy use case |
| `dynamic-select` | Runtime-populated dropdown | SDK 0.4.0+ (Dify 1.5.1+) |
| `object` | JSON object | Nested structure |
| `array` | JSON array | Typed elements |
| `any` | Unconstrained | Escape hatch |

Parameter `form` values: `llm` (LLM fills) | `form` (user fills in settings) | `schema` (auto-generated)

### 14.7 ToolInvokeMessage -- Return Types

| Factory Method | When to Use |
|---|---|
| `create_text_message(text)` | Plain text result |
| `create_link_message(link)` | Clickable URL |
| `create_image_message(image)` | Image URL -- auto-downloaded by Dify |
| `create_blob_message(blob, meta)` | Raw binary; `meta` must include `mime_type` |
| `create_json_message(json)` | Structured data for workflow variables |
| `create_variable_message(name, value)` | Named output variable (non-streaming) |
| `create_stream_variable_message(name, value)` | Streaming string (typewriter); strings only |

**Critical**: Even with `output_schema` in YAML, you must call `create_variable_message()` to emit the value.

Source: https://docs.dify.ai/plugin-dev-en/0411-tool

### 14.8 Python Tool Class Structure

```python
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class MyTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict,
    ) -> Generator[ToolInvokeMessage, None, None]:
        query = tool_parameters.get("query", "")
        # perform work ...
        yield self.create_text_message("Result text")
        yield self.create_json_message({"count": 5})
        yield self.create_variable_message("result_count", 5)
```

### 14.9 Reverse Invocation -- Plugin Calling Dify Services

| Service | Access Pattern | Use Case |
|---|---|---|
| LLM | `self.session.model.llm.invoke(...)` | Run an LLM within a tool |
| Embedding | `self.session.model.text_embedding.invoke(...)` | Embed text |
| Reranker | `self.session.model.rerank.invoke(...)` | Rerank results |
| TTS | `self.session.model.tts.invoke(...)` | Text-to-speech |
| Tool | `self.session.tool.invoke(ptype, provider, name, params)` | Call another tool |
| App | `self.session.app.invoke(app_id, inputs, mode)` | Run a Dify app |
| Storage | `self.session.storage.get/set/del(key)` | KV persistent storage |

`ToolProviderType` enum: `builtin` | `workflow` | `api` | `app` | `mcp` (meta.version 0.0.2+)

Source: https://docs.dify.ai/en/develop-plugin/features-and-specs/advanced-development/reverse-invocation-tool

### 14.10 Agent Strategy Plugin

```python
from dify_plugin import AgentStrategy
from dify_plugin.entities.agent import AgentInvokeMessage

class MyAgentStrategy(AgentStrategy):
    def _invoke(self, parameters, user_id, session):
        # session.tools -> available tools list
        # parameters["model_config"] -> LLM config
        # session.model.llm.invoke(...) -> call LLM
        # session.tool.invoke(...) -> call a tool
        yield AgentInvokeMessage.answer("Final response")
```

YAML declares `features: ["history-messages"]` to receive conversation history.

Source: https://docs.dify.ai/en/develop-plugin/dev-guides-and-walkthroughs/agent-strategy-plugin

---

## 15. MCP Server Publishing -- Implementation Details (v1.6.0+)

### 15.1 Feature Summary

Native two-way MCP introduced in Dify v1.6.0:
- **Inbound**: Import any external MCP server as a Tool (via Tools page)
- **Outbound**: Expose any Dify agent or workflow as a standard MCP server

Protocol version: **2025-03-26** (Streamable HTTP transport only).

Source: https://dify.ai/blog/v1-6-0-built-in-two-way-mcp-support

### 15.2 Exposing a Dify App as MCP Server

Two configuration fields in Publish settings:

| Field | Purpose |
|---|---|
| Service description | Natural-language purpose -- external LLMs use this to decide when to invoke |
| Parameter documentation | Description of every Start node input -- ensures correct client values |

On save: Dify generates a unique server URL with embedded credentials. Regeneration immediately invalidates previous URL. Disabled by default per app.

### 15.3 Server URL Properties

| Property | Detail |
|---|---|
| Transport | Streamable HTTP (protocol 2025-03-26) |
| Auth | Credentials embedded in URL |
| Security | Treat as API key; regenerate if compromised |
| Scope | One URL per app; exposes one MCP tool |
| Default state | Disabled -- must be explicitly enabled |

### 15.4 Compatible Clients

| Client | Configuration |
|---|---|
| Claude Desktop | Profile > Settings > Integrations > add URL |
| Cursor | `.cursor/mcp.json`: `{"mcpServers": {"name": {"url": "..."}}}` |
| Any MCP-compatible | Standard Streamable HTTP (2025-03-26) |

Source: https://docs.dify.ai/en/use-dify/publish/publish-mcp

### 15.5 Consuming External MCP Servers in Dify

1. Tools page > Add MCP server URL
2. Server's tools become available in Agent nodes and Tool nodes
3. Notable integrations: Linear, Notion, Zapier (8,000+ apps), Composio

### 15.6 MCP vs REST API Comparison

| Dimension | Dify REST API | Dify MCP Server |
|---|---|---|
| Client type | Custom code | AI agents, Claude Desktop, Cursor |
| Auth | Explicit header | Embedded in URL |
| Discovery | Manual API docs | Automatic via MCP tool listing |
| Composition | Manual wiring | Host LLM decides call timing |
| Protocol | REST/SSE | MCP Streamable HTTP |
| Best for | Programmatic integrations | LLM-driven orchestration |

---

## 16. Knowledge Pipeline -- Detailed Architecture (v1.9.0+)

### 16.1 Pipeline Execution Flow

```
Data Source Node
    |
    v
Document Processing (select one or chain multiple):
    +-- Dify Extractor: built-in DOC/PDF/image parser (complex layouts)
    +-- Unstructured: third-party, customizable extraction strategies
    +-- Generic Doc Processor: standard PDF/XLSX/DOCX
    |
    v
Chunking (select one):
    +-- General Chunker: fixed-size with delimiter and overlap
    +-- Parent-Child Chunker: hierarchical dual-layer
    +-- Q&A Processor: spreadsheet question-answer pairs
    |
    v
Knowledge Base Node
    config: index method + retrieval strategy + embedding model
```

### 16.2 Chunking Configuration

**General Chunker:**

| Config | Description |
|---|---|
| max_chunk_length | Max chars per chunk |
| overlap | Chars carried between adjacent chunks |
| delimiters | Custom split list (e.g., `\n\n`, `. `) |

**Parent-Child Chunker:**
- Parent: larger context-rich segment (provided alongside child during retrieval)
- Child: smaller precision segment (matched during retrieval)
- Retrieval returns: child match + parent context block

**Q&A Processor:**
- Input: CSV/XLSX where each row = question + answer
- Question indexed for retrieval; answer returned as chunk content
- Best fit: FAQ bases, customer support knowledge

### 16.3 Image Handling

| Rule | Detail |
|---|---|
| Max images per chunk | 10 |
| Auto-extraction trigger | Markdown-referenced images under 2MB |
| URL behavior | Remain in text; safely removable without affecting indexes |
| Cross-modal retrieval | Requires multimodal embedding model (Vision icon) |
| Multimodal reranking | Requires multimodal reranking model (v1.11.0+, SDK 0.7.0+) |

### 16.4 Retrieval Strategy Selection Guide

| Scenario | Recommended Mode |
|---|---|
| Semantic similarity primary | Vector Search |
| Exact term matching required | Full-Text Search |
| Mixed semantic + exact queries | Hybrid + Weighted Score |
| High-precision production | Hybrid + Rerank Model |
| Zero embedding cost | Full-Text (Economical index) |

---

## 17. Variable Referencing -- Complete Syntax Guide

### 17.1 Reference Methods

| Method | Syntax | Context |
|---|---|---|
| UI dropdown | Click `+` in input field | Any node config panel |
| Slash trigger | `/` in text inputs | Node prompts, settings |
| Mustache | `{{variable_name}}` | Prompts, Template node, Answer node |
| Dot access | `{{node_id.outputs.field}}` | Nested upstream node output |
| Bracket array | `{{items[0].title}}` | Array variable indexing |
| Jinja2 | `{{ var \| filter }}`, `{% if %}`, `{% for %}` | Template node body only |
| HTTP nested | `{{api_response.data.items[0].id}}` | HTTP Request response body |

### 17.2 Variable Scoping Rules

1. **Upstream-only**: Only variables from nodes that execute BEFORE can be referenced
2. **Conversation variable**: Readable anywhere in Chatflow; writable only via Variable Assigner
3. **Environment variable**: Read-only; available in all nodes, both app types
4. **Input variable**: Immutable once run starts; set by end user at trigger time

### 17.3 Variable Types by Scope

| Variable Class | Scope | Writable by | Available in |
|---|---|---|---|
| `sys.*` | Run-level | Nobody during run | Workflow + Chatflow |
| `{node_id}.outputs.*` | DAG-upstream | Nobody (immutable per node) | Workflow + Chatflow |
| `env.*` | App-level | Admin pre-run | Workflow + Chatflow |
| `conversation.*` | Session | Variable Assigner | Chatflow only |
| `inputs.*` | Run-level | End user at trigger | Workflow + Chatflow |

Source: https://docs.dify.ai/versions/3-0-x/en/user-guide/workflow/variables

### 17.4 Jinja2 Filters (Template Node)

| Filter | Example | Effect |
|---|---|---|
| `upper` / `lower` | `{{ text \| upper }}` | Case transform |
| `round` | `{{ num \| round(2) }}` | Float precision |
| `replace` | `{{ text \| replace("a","b") }}` | Substitution |
| `strftime` | `{{ ts \| strftime("%Y-%m-%d") }}` | Date format |
| `default` | `{{ val \| default("N/A") }}` | Fallback value |
| `length` | `{{ arr \| length }}` | Item count |
| `first` / `last` | `{{ arr \| first }}` | Head/tail |
| `join` | `{{ arr \| join(", ") }}` | Array to string |

### 17.5 Variable Assigner Operations (Chatflow only)

| Type | Operations |
|---|---|
| String | Overwrite, Clear, Set |
| Number | Overwrite, Add, Subtract, Multiply, Divide, Clear |
| Boolean | Set true / Set false |
| Object | Overwrite entire object |
| Array | Append element, Extend (concat), Remove first, Remove last, Clear |
