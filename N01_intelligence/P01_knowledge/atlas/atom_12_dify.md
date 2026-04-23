---
id: atom_12_dify
kind: knowledge_card
pillar: P01
title: "Dify (LangGenius) Platform -- Deep Vocabulary Atlas"
version: 1.2.0
quality: 8.8
tags: [dify, langgenius, workflow, agent, rag, knowledge-pipeline, low-code, agentic-workflow, plugin-sdk, mcp-server, reverse-invocation, variable-syntax, agent-strategy]
date: 2026-04-13
sources:
  - https://docs.dify.ai/
  - https://github.com/langgenius/dify
  - https://docs.dify.ai/en/use-dify/getting-started/key-concepts
  - https://docs.dify.ai/en/use-dify/nodes/agent
  - https://dify.ai/blog/dify-agent-node-introduction-when-workflows-learn-autonomous-reasoning
  - https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/knowledge-pipeline-orchestration
  - https://docs.dify.ai/en/use-dify/knowledge/create-knowledge/setting-indexing-methods
  - https://langgenius.github.io/dify-plugin-sdks/schema/
  - https://legacy-docs.dify.ai/plugins/schema-definition/manifest
  - https://docs.dify.ai/en/develop-plugin/dev-guides-and-walkthroughs/tool-plugin
  - https://docs.dify.ai/en/develop-plugin/features-and-specs/plugin-types/persistent-storage-kv
  - https://docs.dify.ai/en/develop-plugin/features-and-specs/advanced-development/reverse-invocation-tool
  - https://docs.dify.ai/en/use-dify/publish/publish-mcp
  - https://dify.ai/blog/v1-6-0-built-in-two-way-mcp-support
  - https://docs.dify.ai/versions/3-0-x/en/user-guide/workflow/variables
  - https://legacy-docs.dify.ai/plugins/schema-definition/agent
  - https://docs.dify.ai/en/develop-plugin/dev-guides-and-walkthroughs/agent-strategy-plugin
  - https://docs.dify.ai/en/develop-plugin/features-and-specs/plugin-types/general-specifications
  - https://docs.dify.ai/en/use-dify/nodes/template
  - https://legacy-docs.dify.ai/guides/workflow/variables
  - https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/create-knowledge-pipeline
related:
  - workflow-node-builder
  - visual-workflow-builder
  - bld_instruction_visual_workflow
  - bld_collaboration_workflow_node
  - kc_visual_workflow
  - cex_llm_vocabulary_whitepaper
  - atom_03_openai_agents_sdk
  - atom_07_llamaindex
  - bld_examples_workflow_node
  - p01_kc_workflow
---

# Dify (LangGenius) Platform -- Deep Vocabulary Atlas

## 1. Platform Overview

| Dimension | Detail |
|-----------|--------|
| Org | LangGenius Inc. |
| Repo | `langgenius/dify` (Apache 2.0 + additional conditions) |
| Stars | 138K+ (2026-04) |
| Stack | Python (API), TypeScript/React (Web), Docker, pnpm, Vite |
| Core pitch | Open-source LLM app development platform: visual workflow builder + RAG pipeline + agent capabilities + model management + observability |
| Deployment | Dify Cloud (SaaS), Docker Compose self-hosted, Kubernetes (Helm charts), AWS/Azure/GCP Terraform, AWS Marketplace AMI |
| Plugin system | Marketplace + open community: Model, Tool, Extension, Agent Strategy |
| DSL format | YAML (Dify DSL) -- export/import apps across instances |

### Architecture Layers

```
Publishing Layer       Web App | API | MCP Server | Embedding | Marketplace
                         |
Application Layer      Chatbot | Agent | Text Generator | Chatflow | Workflow
                         |
Orchestration Layer    Visual Canvas (DAG editor) + Node Library
                         |
Knowledge Layer        Knowledge Pipeline + RAG (Vector/Full-Text/Hybrid)
                         |
Model Layer            Multi-provider routing (hundreds of LLMs)
                         |
Plugin Layer           Model | Tool | Extension | Agent Strategy
                         |
Observability Layer    Logs | Dashboard | Annotations | Integrations
```

---

## 2. Application Types

Dify offers 5 application types. Workflow and Chatflow are the current recommended types; the other three are legacy interfaces on the same engine.

| Type | Turn model | Memory | End node | Trigger support | Use case |
|------|-----------|--------|----------|----------------|----------|
| **Workflow** | Single-run (start-to-finish) | None (variables reset per run) | End / Output | User Input, Webhook, Schedule, Plugin | Report generation, batch processing, data pipelines |
| **Chatflow** | Multi-turn conversation | Conversation variables persist across turns | Answer (streaming) | User Input only | Chatbots, assistants, customer service |
| **Chatbot** | Multi-turn | Built-in | -- | -- | Legacy simple chatbot |
| **Agent** | Multi-turn | Built-in | -- | -- | Legacy agent (ReAct/FC) |
| **Text Generator** | Single-turn | None | -- | -- | Legacy completion interface |

### Chatflow vs Workflow -- Key Differences

| Dimension | Workflow | Chatflow |
|-----------|----------|----------|
| System vars | `sys.user_id`, `sys.app_id`, `sys.workflow_id`, `sys.workflow_run_id`, `sys.timestamp` | All of the above + `sys.query`, `sys.files`, `sys.dialogue_count`, `sys.conversation_id` |
| Conversation variables | Not available | String, Number, Object, Array -- persist across turns |
| Variable Assigner | N/A | Writes to conversation variables (overwrite, append, arithmetic, etc.) |
| Output node | End / Output | Answer (streaming with variable ordering) |
| Trigger nodes | User Input, Webhook, Schedule, Plugin | User Input only |
| Memory in LLM nodes | Not available | TokenBufferMemory -- retains conversation history |

---

## 3. Complete Node Type Registry

### 3.1 Start / Trigger Nodes

| Node | Description | Available in |
|------|-------------|-------------|
| **User Input** | Defines input fields (text, paragraph, select, number, checkbox, JSON, file, file list) collected from end users | Workflow + Chatflow |
| **Webhook Trigger** | Listens for external HTTP requests; extracts query params, headers, body; supports JSON, form-data, multipart, text/plain | Workflow only |
| **Schedule Trigger** | Runs workflow on cron schedule | Workflow only |
| **Plugin Trigger** | Custom trigger via installed plugin | Workflow only |

**Webhook details**: Configurable HTTP method, content-type, parameter extraction (query/header/body), custom response codes (200-399), auth handling, parallel triggers supported.

### 3.2 LLM & Reasoning Nodes

| Node | Description | Key config |
|------|-------------|-----------|
| **LLM** | Core language model invocation: system/user/assistant messages, Jinja2 templating, context variables for RAG, structured output (JSON Schema), streaming, vision/multimodal, memory (Chatflow only) | Model selection, temperature, top_p, frequency/presence penalty, presets (Precise/Balanced/Creative), retry + fallback (default value, error route, alt model) |
| **Agent** | Autonomous reasoning node: LLM + tool calling in iterative loop (Think-Act-Observe) | Strategy (Function Calling / ReAct / custom plugin), tool list, max iterations (3-15), TokenBufferMemory, output: final answer + tool outputs + reasoning trace + iteration count |
| **Question Classifier** | LLM-based semantic routing: classifies input into user-defined categories, each category becomes a distinct output path | Model selection, category labels + descriptions, classification instructions for edge cases |
| **Parameter Extractor** | Extracts structured JSON from unstructured text via LLM | Parameter definitions (name, type, required), inference mode (Function Call / Prompt-based), memory toggle, output: `__is_success` + `__reason` |

### 3.3 Knowledge & Retrieval Nodes

| Node | Description | Key config |
|------|-------------|-----------|
| **Knowledge Retrieval** | Queries one or more knowledge bases simultaneously, returns ranked document chunks | Text/image query, multiple KB selection, rerank settings (Weighted Score / Rerank Model), Top K, score threshold, metadata filtering (manual/auto) |

Output: `result` -- array of `{content, metadata, title, ...}`, optional `files` for images.

### 3.4 Data Processing Nodes

| Node | Description | Key config |
|------|-------------|-----------|
| **Code** | Python or JavaScript in sandboxed execution; access to json, math, datetime, re, numpy, pandas, lodash, moment | Input/output variable declaration; limits: 80K char strings, numbers -999999999..999999999, 5-level nesting max; retry up to 10x |
| **Template** | Jinja2 templating: variable substitution, conditionals, loops, filters (upper, round, replace, strftime, default) | Input variables from any upstream node; max output 80K chars (configurable via `TEMPLATE_TRANSFORM_MAX_LENGTH`) |
| **Document Extractor** | Converts uploaded files to text: TXT, MD, HTML, DOCX, DOC (Unstructured API), PDF (pypdfium2), Excel, CSV, PPT, EML, MSG, EPUB, VTT, JSON, YAML | Single file (string) or multiple (array); output: `text` string or array |
| **HTTP Request** | External API calls: GET, HEAD, POST, PUT, PATCH, DELETE; variable substitution in URL/headers/body; nested access `{{api_response.data.items[0].id}}` | Auth (None/Basic/Bearer/Custom/API Key), timeout (connect/read/write), body types (JSON/Form/Binary/Raw), SSL toggle, retry up to 10x, error paths |
| **Tool** | Connects to external services via installed tools (built-in, third-party, custom) | Auth credentials, tool description, parameter config (auto-generated or manual) |
| **List Operator** | Array manipulation: filter (content type, MIME, extension, size, filename, transfer method), sort (asc/desc), select (first/last N items, first/last record) | Input: `array[string\|number\|file\|boolean]`; output: `result`, `first_record`, `last_record` |

### 3.5 Flow Control Nodes

| Node | Description | Key config |
|------|-------------|-----------|
| **If-Else** | Conditional branching: IF / ELIF (multiple) / ELSE paths | Operators: contains, not contains, starts with, ends with, is, is not, is empty, is not empty, >, <, =, !=; combine with AND/OR logic |
| **Iteration** | Processes arrays by applying workflow steps to each element; parallel mode (up to 10 concurrent) or sequential | Input: array variable; built-in: `items` (current element), `index` (position); error handling: terminate / continue on error / remove failed; output: result array |
| **Loop** | Progressive refinement: each cycle builds on previous results; state persists across cycles | Loop variables (persist + accumulate), termination condition (expression-based, e.g. `quality_score > 0.9`), max loop count (safety limit), Exit Loop node |
| **Variable Aggregator** | Merges outputs from multiple conditional branches into single variable reference | All inputs must share same data type; outputs whichever branch actually executed; multi-group support (v0.6.10+) |
| **Variable Assigner** | Writes to conversation variables (Chatflow only): overwrite, clear, set, arithmetic (+,-,*,/), append, extend, remove first/last | String ops, Number arithmetic, Boolean set, Object overwrite, Array CRUD |

### 3.6 Output & Interaction Nodes

| Node | Description | Key config |
|------|-------------|-----------|
| **Answer** | Chatflow output: streaming text + images + files; variable sequence determines streaming order; multiple Answer nodes per chatflow; supports markdown | `{{variable}}` substitution, citation tracking from Knowledge Retrieval |
| **Output / End** | Workflow terminal: returns final results | Output variable mapping |
| **Human Input** | Pauses workflow for human review/approval: customizable form via web app or email, action buttons for routing (approve/reject/regenerate), timeout with fallback | Delivery: web app / email; markdown forms; pre-filled fields; first-response-wins; timeout handling |

---

## 4. Agent Strategies -- Full Registry

### Built-in Strategies

| Strategy | Mechanism | Best for |
|----------|-----------|----------|
| **Function Calling** | Passes tool definitions via model's native `tools` parameter; model selects and parameterizes functions directly | GPT-4, Claude 3.5+, models with robust FC support |
| **ReAct** (Reason + Act) | Structured prompt: Thought -> Action -> Observation cycle; explicit reasoning trace | Models without native FC; when reasoning visibility needed |

### Plugin-Extensible Strategies (via Marketplace)

| Strategy | Abbreviation | Description |
|----------|-------------|-------------|
| **Chain-of-Thought** | CoT | Sequential reasoning steps before final answer |
| **Tree-of-Thought** | ToT | Branching exploration of multiple reasoning paths |
| **Graph-of-Thought** | GoT | Non-linear reasoning with backtracking and merging |
| **Backbone-of-Thought** | BoT | Structured problem decomposition framework |
| **Semantic Kernel** | SK | Microsoft's planner/skill architecture |
| **Custom** | -- | Developer-defined via Agent Strategy Plugin SDK |

### Agent Node Execution Phases

```
1. INITIALIZATION
   |-- Establish parameters, tools, context
   |-- Load strategy plugin
   |
2. ITERATIVE LOOP (up to max_iterations)
   |-- LLM receives prompt + available tools
   |-- Parse response for tool requirements
   |-- Execute tool(s) with parameters
   |-- Update context with observations
   |-- Check completion condition
   |
3. FINAL RESPONSE
   |-- Return completed result
   |-- OR hit iteration limit -> return partial
```

### Agent Output Variables

| Variable | Description |
|----------|-------------|
| `final_answer` | Agent's completed response |
| `tool_outputs` | Results from each tool call |
| `reasoning_trace` | Detailed thought chain (ReAct) |
| `iteration_count` | Number of loops executed |
| `success_status` | Whether agent completed successfully |
| `agent_logs` | Metadata for debugging |

---

## 5. Knowledge System -- Full Vocabulary

### 5.1 Knowledge Base Lifecycle

```
Data Source -> Knowledge Pipeline -> Knowledge Base -> Knowledge Retrieval Node -> LLM Node (context)
```

### 5.2 Data Sources

| Source | Method |
|--------|--------|
| File Upload | Local files via drag-and-drop (max 50 files, 15MB each) |
| Notion | Online document sync with automatic updates |
| Web Crawler | Jina Reader, Firecrawl -- web content to markdown |
| Online Drive | Google Drive, Dropbox, OneDrive integration |
| API | External Knowledge API for custom data sources |

### 5.3 Knowledge Pipeline Nodes

The Knowledge Pipeline is a visual workflow for data ingestion and processing (introduced v1.9.0).

| Pipeline Node | Purpose | Options |
|---------------|---------|---------|
| **Data Source** | Ingest raw data | File Upload, Notion, Web Crawler, Online Drive |
| **Dify Extractor** | Built-in document parser | DOC, PDF, images; optimized for complex layouts |
| **Unstructured** | Third-party extraction | Customizable strategies, element-level metadata |
| **Generic Doc Processor** | Standard format parsing | PDF, XLSX, DOCX |
| **General Chunker** | Fixed-size segmentation | Customizable delimiters, chunk size, overlap |
| **Parent-Child Chunker** | Dual-layer chunking | Parent (broad context) + Child (precise match) |
| **Q&A Processor** | Spreadsheet Q&A pairs | Specialized for FAQ-style knowledge |
| **Knowledge Base Node** | Storage + retrieval config | Chunk structure, index method, retrieval settings |

### 5.4 Indexing Methods

| Method | How it works | Cost |
|--------|-------------|------|
| **High Quality** | Embedding-based vectorization using configured embedding model | Higher (API calls to embedding model) |
| **Economical** | Keyword extraction (top 10 keywords per chunk) via inverted index | Lower (no embedding model needed) |

### 5.5 Retrieval Modes

| Mode | Mechanism | Reranking |
|------|-----------|-----------|
| **Vector Search** | Embed query -> cosine/dot similarity against chunk vectors; finds semantic matches even without keyword overlap | Optional Rerank Model |
| **Full-Text Search** | Inverted index keyword matching (standard search engine technique); exact term matching | No reranking |
| **Hybrid Search** | Runs both Vector + Full-Text simultaneously; merges results | Weighted Score (semantic vs keyword balance slider) OR Rerank Model |

### 5.6 Retrieval Configuration

| Parameter | Description |
|-----------|-------------|
| **Top K** | Maximum number of chunks to return after reranking |
| **Score Threshold** | Minimum similarity score to include a chunk |
| **Rerank Model** | Third-party model for result re-ordering (e.g., Cohere rerank) |
| **Weighted Score** | Semantic vs keyword balance (0.0-1.0 slider) in Hybrid mode |
| **Metadata Filtering** | Manual or automatic filtering by document metadata fields |

### 5.7 Chunk Structure Types

| Structure | Description |
|-----------|-------------|
| **General** | Standard flat chunks with configurable size |
| **Parent-Child** | Hierarchical: parent chunks for context, child chunks for precision |
| **Q&A** | Question-answer pairs extracted from spreadsheets |

### 5.8 Multimodal Knowledge

Vision-capable embedding models enable cross-modal image-text retrieval. Images in documents are embedded alongside text chunks.

---

## 6. Variable System

### 6.1 Variable Categories

| Category | Scope | Mutability | Available in |
|----------|-------|-----------|-------------|
| **Input Variables** | Set at app start by end user | Immutable during run | Workflow + Chatflow |
| **Output Variables** | Generated by node execution | Immutable (per node) | Workflow + Chatflow |
| **Environment Variables** | App-level sensitive data (API keys) | Read-only | Workflow + Chatflow |
| **Conversation Variables** | Session-persistent across turns | Writable via Variable Assigner | Chatflow only |

### 6.2 System Variables (Workflow)

| Variable | Type | Description |
|----------|------|-------------|
| `sys.user_id` | String | Unique user identifier |
| `sys.app_id` | String | Application identifier |
| `sys.workflow_id` | String | Workflow definition ID |
| `sys.workflow_run_id` | String | Runtime execution ID |
| `sys.timestamp` | Number | Execution timestamp |
| `sys.files` | Array[File] | Legacy file upload variable |

### 6.3 System Variables (Chatflow-specific additions)

| Variable | Type | Description |
|----------|------|-------------|
| `sys.query` | String | User's chat message content |
| `sys.files` | Array[File] | User-uploaded files (when enabled) |
| `sys.dialogue_count` | Number | Conversation turn counter |
| `sys.conversation_id` | String | Session identifier |

### 6.4 Variable Referencing

- Dropdown selector in node config UI
- `/` slash notation in text inputs
- `{{variable_name}}` in prompts and templates
- Dot notation for nested access: `{{node.output.field}}`
- Bracket notation for arrays: `{{items[0].title}}`

---

## 7. Plugin System

### 7.1 Plugin Types

| Type | Purpose | Extensibility |
|------|---------|--------------|
| **Model** | Add LLM/embedding/rerank providers (OpenAI, Anthropic, local) | Cannot extend other plugin types |
| **Tool** | External service integration (search, DB, API) + optional endpoint | Most common plugin type |
| **Agent Strategy** | Custom reasoning algorithms (CoT, ToT, GoT, BoT) | Defines standard I/O + reasoning loop |
| **Extension** | Simple HTTP service to extend platform | Lightweight, endpoint-only |

### 7.2 Plugin Development

- CLI scaffolding tools for all 4 types
- Configuration forms (YAML manifest)
- Visualization components
- Persistent storage API
- Reverse invocation of Dify services (App, Model, Node, Tool)
- Plugin signing for third-party verification
- Marketplace publishing or GitHub distribution

### 7.3 Marketplace Ecosystem

- Official plugins (LangGenius maintained)
- Partner solutions (verified)
- Community contributions (open PR-based publishing)
- Categories: Models, Tools, Agent Strategies, Extensions, Bundles

---

## 8. Publishing & Deployment

| Method | Description | Auth |
|--------|-------------|------|
| **Web App (Chat)** | Hosted chat interface with conversation history | Configurable access control |
| **Web App (Workflow)** | Single-run form interface | Configurable access control |
| **API** | RESTful endpoints for all app types (chat, completion, workflow) | API key based |
| **MCP Server** | Expose app as MCP server for Claude Desktop, Cursor, etc. | MCP protocol |
| **Website Embedding** | iframe/script embed: floating button, inline, or custom styled | Configurable |
| **Marketplace** | Publish app for discovery by other Dify users | Review process |

---

## 9. Observability & Monitoring

| Feature | Description |
|---------|-------------|
| **Dashboard** | Usage metrics, token consumption, response times |
| **Logs** | Full execution traces per workflow run |
| **Run History** | Replay past executions with input/output snapshots |
| **Single Node Debug** | Test individual nodes in isolation |
| **Variable Inspector** | Real-time data flow visualization |
| **Annotation System** | Human feedback loop for quality improvement |
| **External Integrations** | LangSmith, Langfuse, Arize, Phoenix, Opik, W&B Weave, Alibaba Cloud |

---

## 10. Error Handling

| Node | Error strategy |
|------|---------------|
| LLM | Retry (count, interval, backoff), fallback: default value / error route / alternative model |
| Code | Retry up to 10x (max 5000ms interval), fallback path |
| HTTP Request | Retry up to 10x, error branch routing |
| Iteration | Terminate / Continue on Error / Remove Failed |
| Loop | Max iteration limit as safety valve |
| Agent | Max iterations cap to prevent infinite loops |

---

## 11. CEX Mapping

### 11.1 Concept Mapping

| Dify Term | CEX Equivalent | Notes |
|-----------|---------------|-------|
| Workflow | 8F Pipeline | Both are DAG-based processing chains |
| Chatflow | Chatflow has no direct CEX analog | CEX is artifact-centric, not conversation-centric |
| Node | 8F Function (F1-F8) | Dify nodes are visual; CEX functions are reasoning steps |
| Agent Node | Nucleus (N01-N06) | Both delegate autonomous reasoning to specialized units |
| Agent Strategy | 8F reasoning protocol | Dify pluggable; CEX fixed (8F) but extensible per domain |
| Knowledge Base | P01_knowledge library | Both store structured knowledge for retrieval |
| Knowledge Retrieval Node | F3 INJECT | Both retrieve context before reasoning |
| Knowledge Pipeline | cex_compile.py + cex_retriever.py | Data ingestion + indexing pipelines |
| LLM Node | F6 PRODUCE | Core generation step |
| Question Classifier | F1 CONSTRAIN (intent resolution) | Both route input to correct handler |
| If-Else | GDP decision gates | Conditional routing based on context |
| Iteration / Loop | cex_evolve.py cycles | Iterative refinement patterns |
| Variable Aggregator | Signal consolidation | Merge outputs from parallel branches |
| Human Input | GDP (Guided Decision Protocol) | Both pause for human judgment |
| Tool Node | F5 CALL | External capability invocation |
| Code Node | _tools/*.py | Custom data transformation |
| Template Node | Jinja2 in cex_crew_runner.py | Prompt composition via templating |
| Document Extractor | cex_retriever.py ingestion | File-to-text conversion |
| HTTP Request | api_client kind (P04) | External API integration |
| Parameter Extractor | cex_8f_motor.py intent parser | Structured extraction from natural language |
| Answer / Output | F8 COLLABORATE output | Final artifact delivery |
| Webhook Trigger | _spawn/dispatch.sh | External event triggering execution |
| Plugin (Model) | .cex/config/nucleus_models.yaml | Model provider configuration |
| Plugin (Tool) | P04_tools builders | Tool integration layer |
| Plugin (Agent Strategy) | .claude/rules/8f-reasoning.md | Reasoning protocol definition |
| Dify DSL (YAML) | CEX frontmatter + compiled YAML | Portable artifact representation |
| Conversation Variable | .cex/runtime/ session state | Persistent state across interactions |
| Environment Variable | .cex/config/ | Sensitive configuration |
| Reranking | cex_retriever.py TF-IDF ranking | Result quality optimization |
| Marketplace | archetypes/builders/ | Reusable component library |

### 11.2 Architectural Parallels

| Pattern | Dify | CEX |
|---------|------|-----|
| Visual orchestration | Canvas DAG editor | /mission + /grid dispatch |
| Autonomous reasoning | Agent Node (ReAct/FC) | Nucleus with 8F pipeline |
| Knowledge injection | Knowledge Retrieval -> LLM context | F3 INJECT -> F6 PRODUCE |
| Quality loop | Loop node with score threshold | F7 GOVERN retry (max 2) |
| Human-in-the-loop | Human Input node | GDP (Guided Decision Protocol) |
| Multi-agent | Multiple Agent nodes in workflow | Grid dispatch (up to 6 parallel nuclei) |
| Plugin extensibility | 4 plugin types + Marketplace | Builders (125) + archetypes |
| Error resilience | Per-node retry + fallback chains | cex_router.py fallback chains |

### 11.3 Gaps -- What Dify Has That CEX Lacks

| Dify capability | CEX status |
|----------------|------------|
| Visual DAG canvas | No GUI -- CLI/file-based orchestration |
| Real-time streaming Answer | No streaming -- batch artifact output |
| Webhook/Schedule triggers | Manual dispatch only (dispatch.sh) |
| Conversation memory across turns | Session state in .cex/runtime/ (simpler) |
| Marketplace for plugins | No marketplace -- git-based sharing |
| Web app hosting built-in | No hosting -- artifacts are files |
| MCP Server publishing | MCP consumer only (not publisher) |

### 11.4 Gaps -- What CEX Has That Dify Lacks

| CEX capability | Dify status |
|---------------|------------|
| Typed artifact system (130 kinds) | Untyped -- all outputs are strings/JSON |
| Quality scoring (3-layer: structural + rubric + semantic) | No built-in quality gates |
| Builder archetypes (13 ISOs per kind) | No builder specialization |
| Fractal nucleus architecture (7 specialized domains) | Flat -- all agents are equal |
| Brand injection across all outputs | No brand awareness |
| 8F mandatory reasoning trace | Optional -- depends on prompt design |
| Autonomous evolution (cex_evolve.py) | No self-improvement loop |
| Git-native version control per artifact | Version control at app level only |

---

## 12. Model Provider Ecosystem

Dify supports "hundreds of proprietary/open-source LLMs from dozens of inference providers" via the Model Plugin system:

| Category | Examples |
|----------|---------|
| Proprietary | OpenAI (GPT-4/4o), Anthropic (Claude 3.5/4), Google (Gemini), Mistral |
| Open-source | Llama 3, Qwen, DeepSeek, Yi |
| Local inference | Ollama, LocalAI, Xinference, vLLM |
| Embedding | OpenAI Ada, Cohere Embed, local models |
| Reranking | Cohere Rerank, cross-encoder models |
| Speech | Whisper (STT), TTS providers |
| Vision | GPT-4V, Claude vision, multimodal models |

---

## 13. Quick Reference -- All Node Types (Sorted)

| # | Node | Category | Workflow | Chatflow |
|---|------|----------|----------|----------|
| 1 | User Input | Start | Yes | Yes |
| 2 | Webhook Trigger | Start | Yes | No |
| 3 | Schedule Trigger | Start | Yes | No |
| 4 | Plugin Trigger | Start | Yes | No |
| 5 | LLM | Reasoning | Yes | Yes |
| 6 | Agent | Reasoning | Yes | Yes |
| 7 | Question Classifier | Reasoning | Yes | Yes |
| 8 | Parameter Extractor | Reasoning | Yes | Yes |
| 9 | Knowledge Retrieval | Knowledge | Yes | Yes |
| 10 | Code | Processing | Yes | Yes |
| 11 | Template | Processing | Yes | Yes |
| 12 | Document Extractor | Processing | Yes | Yes |
| 13 | HTTP Request | Processing | Yes | Yes |
| 14 | Tool | Processing | Yes | Yes |
| 15 | List Operator | Processing | Yes | Yes |
| 16 | If-Else | Flow Control | Yes | Yes |
| 17 | Iteration | Flow Control | Yes | Yes |
| 18 | Loop | Flow Control | Yes | Yes |
| 19 | Variable Aggregator | Flow Control | Yes | Yes |
| 20 | Variable Assigner | Flow Control | No | Yes |
| 21 | Answer | Output | No | Yes |
| 22 | Output / End | Output | Yes | No |
| 23 | Human Input | Interaction | Yes | Yes |

**Total: 23 node types** across 6 categories.

---

## 14. Plugin Development SDK -- Full Schema Reference

### 14.1 Manifest Schema (root)

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `version` | string (semver) | Yes | e.g. `0.0.1` |
| `type` | string | Yes | Always `"plugin"` (future: `"bundle"`) |
| `author` | string | Yes | Marketplace org identifier |
| `name` | string | Yes | Pattern: `^[a-z0-9_-]{1,128}$` |
| `label` | I18nObject | Yes | Multi-lang display names |
| `description` | I18nObject | Yes | Multi-lang descriptions |
| `icon` | string | Yes | Asset path (e.g. `"icon.svg"`) |
| `icon_dark` | string | No | Dark-mode variant |
| `created_at` | RFC3339 datetime | Yes | Must not exceed current time |
| `repo` | string | No | Repository URL |
| `resource` | PluginResourceRequirements | No | Memory + permission config |
| `plugins` | Plugins | Yes | Extension manifests (see 14.2) |
| `meta` | Meta | Yes | Runtime metadata |
| `privacy` | string | No | Path or URL to privacy policy |

**I18nObject supported locales**: `en_US`, `zh_Hans`, `ja_JP`, `pt_BR`

### 14.2 Plugins Object

```yaml
plugins:
  tools:            # list[string] -- paths to provider YAML files
  models:           # list[string] -- paths to model YAML files
  endpoints:        # list[string] -- paths to endpoint YAML files
  agent_strategies: # list[string] -- paths to strategy YAML files
```

**Constraints**:
- Cannot declare both `tools` AND `models` simultaneously
- Cannot declare both `models` AND `endpoints` simultaneously
- Minimum one extension type required
- One provider per extension type (v1.x)

### 14.3 Resource Object

```yaml
resource:
  memory: 10485760          # bytes (int64)
  permission:
    tool:
      enabled: true
    model:
      enabled: true
      llm: true
      text_embedding: true
      rerank: true
      tts: true
      speech2text: true
      moderation: true
    endpoint:
      enabled: true
    app:
      enabled: true
    storage:
      enabled: true
      size: 1048576          # bytes (int64)
```

### 14.4 Meta Object

```yaml
meta:
  version: "0.0.1"
  arch: [amd64, arm64]
  runner:
    language: python
    version: "3.12"
    entrypoint: "main"
```

### 14.5 Tool Plugin File Layout

```
plugin_name/
  _assets/icon.svg
  provider/
    {provider_name}.yaml    # provider config
    {provider_name}.py      # ToolProvider subclass
  tools/
    {tool_name}.yaml        # tool config
    {tool_name}.py          # Tool subclass
  manifest.yaml
  requirements.txt
```

**Provider YAML fields**:

| Field | Type | Description |
|-------|------|-------------|
| `identity.author` | string | Plugin author |
| `identity.name` | string | Provider identifier |
| `identity.label` | I18nObject | Display name |
| `identity.description` | I18nObject | Human + LLM descriptions |
| `identity.icon` | string | Asset path |
| `identity.tags` | list[string] | Marketplace categories |
| `credentials_for_provider` | map[name: ProviderConfig] | Auth fields |
| `tools` | list[string] | Tool YAML file paths |
| `extra.python.source` | string | Provider implementation path |

**Tool YAML fields**:

| Field | Type | Description |
|-------|------|-------------|
| `identity.name` | string | Tool identifier |
| `identity.author` | string | Plugin author |
| `identity.label` | I18nObject | Display name |
| `description.human` | I18nObject | Human-readable description |
| `description.llm` | string | LLM-facing usage instruction |
| `parameters` | list[ToolParameter] | Input specs |
| `output_schema` | JSON Schema dict | Structured output definition |
| `has_runtime_parameters` | bool | Dynamic params flag |
| `extra.python.source` | string | Implementation file path |

### 14.6 ToolParameter Types (full enum)

| Type | Description |
|------|-------------|
| `string` | Plain text |
| `number` | Numeric (supports min/max/precision) |
| `boolean` | True/false |
| `select` | Dropdown with options list |
| `secret-input` | Masked credential field |
| `text-input` | Multi-line text |
| `file` | Single file upload |
| `files` | Multiple file upload |
| `app-selector` | Select a Dify app |
| `model-selector` | Select a model config (scoped by model type) |
| `array[tools]` | Array of ToolEntity references |
| `any` | Untyped passthrough |
| `object` | Structured JSON object |
| `array` | Generic array |
| `dynamic-select` | Dynamically populated dropdown |
| `checkbox` | Boolean checkbox |

**Parameter `form` values**:
- `llm` -- agent-inferred (not shown in UI, sent to model as tool param)
- `form` -- user-input (shown in configuration form)
- `schema` -- validated against JSON schema

### 14.7 Credential Form Types (ProviderConfig)

| Type | Behavior | Use case |
|------|----------|----------|
| `text-input` | Visible text field | Usernames, endpoint URLs |
| `secret-input` | Masked/encrypted storage | API keys, passwords, tokens |
| `select` | Dropdown from predefined options | Region, model tier |
| `radio` | Radio button group | Mutually exclusive config |
| `switch` | Toggle boolean | Feature flags, enable/disable |

### 14.8 Tool Implementation (Python)

```python
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GoogleSearchTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage]:
        query = tool_parameters.get("query")
        results = self._do_search(query)
        yield self.create_json_message({"results": results})
        # Other return types:
        # yield self.create_text_message("plain text result")
        # yield self.create_link_message("https://example.com")
        # yield self.create_image_message(image_bytes, "image/png")
        # yield self.create_blob_message(data_bytes, "application/pdf")
```

**Provider credential validation**:

```python
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class GoogleProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict) -> None:
        try:
            GoogleSearchTool.from_credentials(credentials).invoke(
                tool_parameters={"query": "test", "num_results": 1}
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
```

### 14.9 Model Provider Plugin Schema

**AIModelEntity fields**:

| Field | Type | Description |
|-------|------|-------------|
| `model` | string | Model identifier |
| `model_type` | ModelType enum | llm / text-embedding / rerank / tts / speech2text / moderation / text2img |
| `features` | list[string] | tool-call, vision, stream-tool-call, document, video, audio, structured-output |
| `fetch_from` | enum | `predefined-model` or `customizable-model` |
| `model_properties.context_size` | int | Max context window tokens |
| `model_properties.max_chunks` | int | For embedding models |
| `parameter_rules` | list[ParameterRule] | temperature, top_p, top_k, penalties, max_tokens |
| `pricing.input` | decimal | Cost per 1K input tokens |
| `pricing.output` | decimal | Cost per 1K output tokens |
| `pricing.currency` | string | e.g. `"USD"` |

---

## 15. Reverse Invocation API

Plugins call back into Dify via `self.session.*`, gaining access to all models, tools, apps, and nodes configured in the workspace.

### 15.1 Tool Invocation (`session.tool`)

```python
# Built-in tool (format: org/plugin/provider)
results = self.session.tool.invoke_builtin_tool(
    provider="langgenius/google/google",
    tool_name="google_search",
    parameters={"query": "AI news", "num_results": 5}
)

# Workflow-as-tool
results = self.session.tool.invoke_workflow_tool(
    provider="workflow_provider_id",
    tool_name="tool_name",
    parameters={"key": "value"}
)

# Custom/API tool (OpenAPI spec operation_id)
results = self.session.tool.invoke_api_tool(
    provider="custom_provider_id",
    tool_name="operation_id",
    parameters={"param": "value"}
)
```

All return `Generator[ToolInvokeMessage, None, None]`.

### 15.2 Model Invocation (`session.model`)

```python
# LLM
response = self.session.model.llm.invoke(
    model_config=LLMModelConfig(
        provider="openai", model="gpt-4o", mode="chat",
        completion_params={"temperature": 0.7}
    ),
    prompt_messages=[
        SystemPromptMessage(content="You are helpful"),
        UserPromptMessage(content="Hello")
    ],
    tools=None, stream=True
)
# Also available:
self.session.model.text_embedding.invoke(model_config, texts)
self.session.model.rerank.invoke(model_config, query, docs)
self.session.model.tts.invoke(model_config, ...)
self.session.model.speech2text.invoke(model_config, ...)
self.session.model.moderation.invoke(model_config, ...)
```

### 15.3 App Invocation (`session.app`)

```python
# Chatflow/Chatbot
response = self.session.app.chat.invoke(
    app_id="app-uuid",
    inputs={"key": "value"},
    query="user question",
    response_mode="blocking",    # or "streaming"
    conversation_id=None         # None = new conversation
)

# Workflow
result = self.session.app.workflow.invoke(
    app_id="app-uuid",
    inputs={"field": "value"}
)
```

### 15.4 Persistent Storage (`session.storage`)

```python
# Set (value must be bytes)
self.session.storage.set("cache_key", json.dumps(data).encode("utf-8"))

# Get (returns bytes or None)
raw = self.session.storage.get("cache_key")
if raw:
    data = json.loads(raw.decode("utf-8"))

# Delete
self.session.storage.delete("cache_key")
```

**Constraints**:
- Values must be `bytes`; encode strings via `.encode("utf-8")`
- Scope: workspace-level (shared across plugin instances in same workspace)
- Size limit: declared via `resource.permission.storage.size` in manifest (int64 bytes)
- No TTL -- data persists until explicitly deleted

---

## 16. Agent Strategy Plugin Schema

### 16.1 Strategy YAML Structure

```yaml
identity:
  author: langgenius
  name: function_calling
  label:
    en_US: Function Calling
  description:
    en_US: "Tool-native FC strategy for models with native function calling support"
  icon: icon.svg
parameters:
  - name: model
    type: model-selector
    scope: tool-call&llm         # restricts to FC-capable models
    required: true
    label:
      en_US: Model
  - name: tools
    type: array[tools]
    required: true
    label:
      en_US: Tools
  - name: query
    type: string
    required: true
    label:
      en_US: Query
  - name: max_iterations
    type: number
    required: false
    default: 5
    min: 1
    max: 50
    label:
      en_US: Max Iterations
features:
  - history-messages             # injects conversation history into context
output_schema:
  type: object
  properties:
    text:
      type: string
    files:
      type: array
has_runtime_parameters: false
extra:
  python:
    source: strategies/function_calling.py
```

### 16.2 Strategy Implementation

```python
from collections.abc import Generator
from dify_plugin import AgentStrategy
from dify_plugin.entities.agent import AgentInvokeMessage, LogMessageStatus

class FunctionCallingStrategy(AgentStrategy):
    def _invoke(self, parameters: dict) -> Generator[AgentInvokeMessage]:
        query = parameters["query"]
        model_config = parameters["model"]
        tools = parameters["tools"]
        max_iterations = parameters.get("max_iterations", 5)
        history = parameters.get("history", [])  # from history-messages feature

        messages = self._build_messages(query, history)

        for iteration in range(max_iterations):
            log = self.create_log_message(
                label=f"Iteration {iteration + 1}",
                data={"iteration": iteration},
                status=LogMessageStatus.START
            )
            yield log

            response = self.session.model.llm.invoke(
                model_config=model_config,
                prompt_messages=messages,
                tools=tools,
                stream=False
            )

            if response.message.tool_calls:
                for tc in response.message.tool_calls:
                    yield self.finish_log_message(log, status=LogMessageStatus.SUCCESS)
                    # invoke tool and add observation to messages
                    tool_result = self.session.tool.invoke_builtin_tool(
                        provider=tc.function.name,
                        tool_name=tc.function.name,
                        parameters=tc.function.arguments
                    )
                    messages.append(AssistantPromptMessage(tool_calls=[tc]))
                    messages.append(ToolPromptMessage(content=str(tool_result)))
            else:
                yield self.finish_log_message(log, status=LogMessageStatus.SUCCESS)
                yield self.create_text_message(response.message.content)
                return

        yield self.create_text_message("Max iterations reached.")
```

### 16.3 AgentInvokeMessage Types

| Type | Factory method | Purpose |
|------|---------------|---------|
| TextMessage | `create_text_message(text)` | Final answer text |
| LogMessage | `create_log_message(label, data, status)` | UI tree visualization node |
| ToolInvokeMessage | from `session.tool.*` calls | Tool result passthrough |

**LogMessageStatus values**: `START`, `SUCCESS`, `ERROR`, `STOP`

---

## 17. MCP Two-Way Support (v1.6.0+)

### 17.1 Architecture Overview

Dify supports bidirectional MCP since v1.6.0 (2025):

```
[External MCP Client]              [Dify]                [External MCP Server]
  Claude Desktop  <--MCP Server--  Dify Workflow/Chat
  Cursor          <--MCP Server--  Dify Workflow/Chat
                                   Dify Tools >---MCP Client-->  Linear
                                               >---MCP Client-->  Notion
                                               >---MCP Client-->  Zapier (8000+ apps)
                                               >---MCP Client-->  Composio
```

### 17.2 Dify as MCP Server (Publishing Workflows)

**Configuration steps**:
1. Open app > Publish > MCP Server
2. Enable the module (off by default)
3. Set endpoint name and describe input parameters in JSON schema
4. Dify issues unique server URL containing embedded auth token
5. Treat URL as an API key -- regenerate button invalidates previous URL

**Client integration**:

| Client | Config method |
|--------|--------------|
| Claude Desktop | Profile > Settings > Integrations > Add > paste server URL |
| Cursor | `.cursor/mcp.json` with `{ "mcpServers": { "name": { "url": "..." } } }` |
| Any MCP client | HTTP SSE or StreamableHTTP transport with server URL |

**Supported app types**: Both Workflow and Chatflow apps
**Protocol version**: `2025-03-26`
**Best practices**: Specific parameter descriptions improve AI invocation quality; split complex workflows for lower latency

### 17.3 Dify as MCP Client (Consuming External Servers)

**Setup**: Tools > MCP > Add MCP Server
**Transport**: HTTP-based only (no stdio/local)

**In-workflow usage**:

| Usage pattern | Node type | When to use |
|---------------|-----------|-------------|
| Dynamic tool selection | Agent node | Complex tasks where AI chooses which MCP tool to invoke |
| Precise invocation | MCP node (standalone) | Standardized, strictly-ordered tool calls |

---

## 18. Knowledge Pipeline -- Internal Data Flow

### 18.1 Full Pipeline Sequence

```
[Data Source Node]
        |
        | raw documents
        v
[Extractor Node]                   choose one:
  - Dify Extractor                   built-in; PDF/DOCX/images; complex layouts
  - Unstructured                     strategy: auto | hi_res | fast | ocr_only
  - Generic Doc Processor            standard: PDF, XLSX, DOCX
        |
        | {x} Content (structured text + optional image refs)
        v
[Chunker Node]                     choose one:
  - General Chunker               -> Array[Chunk]      (flat segments)
  - Parent-Child Chunker          -> Array[ParentChunk] (hierarchical)
  - Q&A Processor                 -> Array[QAChunk]    (question-answer pairs)
        |
        | typed array of chunks
        v
[Knowledge Base Node]              indexing + vector/keyword storage
        |
        v
[User Input Node]                  optional: per-pipeline input fields
        |
        v
[Test & Publish]                   validation + single-file test run
```

### 18.2 Chunker Configuration

**General Chunker**:

| Parameter | Type | Description |
|-----------|------|-------------|
| `chunk_size` | int | Max characters per chunk |
| `chunk_overlap` | int | Overlap chars between adjacent chunks |
| `separators` | list[string] | Custom delimiters (e.g. `["\n\n", "\n", " "]`) |
| `preprocessing_rules` | list | Remove extra whitespace, URLs, emails |

**Parent-Child Chunker**:

| Parameter | Type | Options |
|-----------|------|---------|
| `parent_mode` | enum | `full_doc` (whole doc as parent) or `paragraph` (paragraph as parent) |
| `child_chunk_size` | int | Max chars for child (retrieval) chunks |

**Q&A Processor**: Input is a spreadsheet with Question/Answer columns. Each Q-A pair becomes one QAChunk. Questions are embedded for retrieval; answers are the returned content.

### 18.3 Knowledge Base Node Config Schema

| Parameter | Options | Description |
|-----------|---------|-------------|
| `indexing_technique` | `high_quality`, `economy` | Embedding vs keyword index |
| `retrieval_model` | `semantic_search`, `full_text_search`, `hybrid_search` | Query matching strategy |
| `reranking_enable` | bool | Enable post-retrieval reranking |
| `reranking_mode` | `reranking_model`, `weighted_score` | Rerank method |
| `weights.semantic_weight` | float 0.0-1.0 | Hybrid mode semantic component weight |
| `weights.keyword_weight` | float 0.0-1.0 | Hybrid mode keyword component weight |
| `top_k` | int | Max chunks returned per query |
| `score_threshold_enabled` | bool | Enable minimum similarity filter |
| `score_threshold` | float 0.0-1.0 | Min similarity to include a chunk |
| `summary_enabled` | bool | Auto-generate chunk summary |

**Multimodal constraints**: Vision-capable embedding model required for image retrieval; vision rerank model required for image reranking; max 10 images per chunk.

**Immutability**: Chunk structure (General/Parent-Child/Q&A) cannot be changed after publishing. Re-create the pipeline to change structure.

### 18.4 User Input Node (Pipeline-specific)

**Scope types**:

| Scope | Availability |
|-------|-------------|
| Unique | Only for the connected data source node |
| Global | Accessible by all nodes in the pipeline |

**Supported field types**: Text (max 256 chars), Paragraph, Select, Boolean, Number, Single file, File List

Each field: `variable_name`, `display_name`, `required/optional`, `default_value`, `placeholder`, `tooltip`

---

## 19. Variable System -- Complete Syntax Reference

### 19.1 Referencing Syntax Forms

| Form | Syntax | Example |
|------|--------|---------|
| Simple node output | `{{node_name.output_var}}` | `{{llm_1.text}}` |
| Dot notation (nested) | `{{node.var.field}}` | `{{http_req.body.data.items}}` |
| Array bracket access | `{{node.var[n]}}` | `{{results[0].title}}` |
| Chained deep access | `{{node.var[n].field.sub}}` | `{{api.response[2].meta.url}}` |
| System variable | `{{sys.var_name}}` | `{{sys.query}}`, `{{sys.conversation_id}}` |
| Environment variable | `{{env.VAR_NAME}}` | `{{env.OPENAI_API_KEY}}` |
| Conversation variable | `{{conv_var_name}}` | `{{user_language}}` (Chatflow only) |
| Slash UI trigger | `/` then select | Node config dropdown picker |

**In Jinja2 contexts** (Template node, LLM prompt fields):
```jinja2
{{ start.user_input | upper }}
{{ items | length }}
{{ data | default("fallback_value") }}
{{ timestamp | strftime("%Y-%m-%d") }}
{% for item in results %}{{ item.title }}{% endfor %}
{% if score > 0.9 %}High confidence{% else %}Low confidence{% endif %}
```

### 19.2 Variable Scoping Rules

| Category | Read scope | Write scope | Persists |
|----------|-----------|-------------|---------|
| Input variables (start node) | All nodes downstream | Immutable | Per run |
| Node output variables | All downstream nodes | Set by node only | Per run |
| System variables (`sys.*`) | All nodes globally | Platform-managed | Per run |
| Environment variables (`env.*`) | All nodes globally | Read-only | Permanent |
| Conversation variables | All nodes globally | Variable Assigner node | Per session |

**Naming rules**: Node names must be unique within an app to prevent variable reference collisions.

### 19.3 Variable Assigner Write Operations

| Data type | Available operations |
|-----------|---------------------|
| String | Overwrite, Clear, Set (if empty), Append (concatenate) |
| Number | Overwrite, Clear, Set (if empty), +, -, *, / arithmetic |
| Boolean | Set to true or false |
| Object | Overwrite entire object |
| Array[any] | Append item, Extend (concat arrays), Remove first, Remove last |

### 19.4 Node Output Variable Reference

| Node | Output variable | Type |
|------|--------------|----|
| LLM | `text`, `usage`, `finish_reason` | string, object, string |
| Agent | `final_answer`, `tool_outputs`, `reasoning_trace`, `iteration_count`, `success_status`, `agent_logs` | string, array, string, number, bool, array |
| Knowledge Retrieval | `result`, `files` | array[chunk], array[file] |
| Code | User-declared outputs | any |
| Template | `output` | string |
| HTTP Request | `body`, `status_code`, `headers` | string/object, number, object |
| Parameter Extractor | Declared params + `__is_success`, `__reason` | mixed, bool, string |
| Question Classifier | `class_name` | string |
| Iteration | `output` | array |
| Document Extractor | `text` | string or array[string] |
| List Operator | `result`, `first_record`, `last_record` | array, item, item |
| Variable Aggregator | `output` | type of active branch |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-node-builder]] | downstream | 0.29 |
| [[visual-workflow-builder]] | downstream | 0.27 |
| [[bld_instruction_visual_workflow]] | downstream | 0.27 |
| [[bld_collaboration_workflow_node]] | downstream | 0.25 |
| [[kc_visual_workflow]] | sibling | 0.25 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.24 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.23 |
| [[atom_07_llamaindex]] | sibling | 0.22 |
| [[bld_examples_workflow_node]] | downstream | 0.22 |
| [[p01_kc_workflow]] | sibling | 0.22 |
