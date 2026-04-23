# Standards, Chinese Ecosystem, Academic & GitHub Taxonomy
> Sources: Official specs, Chinese repos, papers, GitHub repos | Scraped: 2026-03-29
> Method: mcp__fetch__fetch + gh CLI + WebFetch (firecrawl token invalid — used fallbacks)

---

## 1. Standards & Specs

| Standard | Term | Definition / Role | URL |
|---|---|---|---|
| MCP (Anthropic) | Tool | Callable function exposed by server to LLM client | modelcontextprotocol.io |
| MCP | Resource | Data/content source the server exposes (files, DB, APIs) | modelcontextprotocol.io |
| MCP | Prompt | Reusable prompt template exposed by server | modelcontextprotocol.io |
| MCP | Server | Process that exposes Tools, Resources, and Prompts | modelcontextprotocol.io |
| MCP | Client | LLM host that connects to MCP servers | modelcontextprotocol.io |
| MCP | Transport | Communication layer (stdio, SSE, HTTP) | modelcontextprotocol.io |
| MCP | Capability | Feature flag negotiated at initialization | modelcontextprotocol.io |
| MCP | Session | Stateful connection between client and server | modelcontextprotocol.io |
| MCP | Message | JSON-RPC 2.0 request/response/notification unit | modelcontextprotocol.io |
| MCP | Protocol Version | `2025-11-25` (current); YYYY-MM-DD format | modelcontextprotocol.io |
| A2A (Google) | Agent | Autonomous opaque unit with skills and identity | github.com/google/A2A |
| A2A | Task | Unit of work assigned to an agent; has lifecycle | github.com/google/A2A |
| A2A | AgentCard | Metadata describing agent's capabilities and endpoint | github.com/google/A2A |
| A2A | AgentSkill | Specific capability an agent advertises | github.com/google/A2A |
| A2A | Message | Conversational exchange between user and agent | github.com/google/A2A |
| A2A | Artifact | Output produced by a task (text, file, data) | github.com/google/A2A |
| A2A | Part | Typed content unit within Message/Artifact (TextPart, FilePart, DataPart) | github.com/google/A2A |
| A2A | TaskState | submitted / working / input-required / completed / failed / canceled | github.com/google/A2A |
| A2A | PushNotification | Webhook callback for async task status updates | github.com/google/A2A |
| JSON Schema | Schema | JSON document defining structure/constraints of JSON data | json-schema.org |
| JSON Schema | Instance | JSON value being validated against a schema | json-schema.org |
| JSON Schema | Vocabulary | Named set of keywords with defined semantics | json-schema.org |
| JSON Schema | Dialect | Set of vocabularies identified in a meta-schema | json-schema.org |
| JSON Schema | $ref | JSON Pointer reference to another schema | json-schema.org |
| JSON Schema | $defs | Reusable schema definitions within a schema document | json-schema.org |
| JSON Schema | $schema | URI identifying the meta-schema / dialect | json-schema.org |
| JSON Schema | $id | Canonical URI identifier for a schema | json-schema.org |
| JSON Schema | annotation | Non-validating metadata attached to a schema | json-schema.org |
| JSON Schema | keyword | Named rule or annotation in a schema (type, properties, etc.) | json-schema.org |
| JSON Schema | allOf / anyOf / oneOf / not | Boolean schema combinators | json-schema.org |
| OpenAPI 3.1 | Operation | Single API action defined on a path (GET, POST, etc.) | spec.openapis.org |
| OpenAPI 3.1 | Path Item | All operations available on a URL path | spec.openapis.org |
| OpenAPI 3.1 | Parameter | Named input: query / path / header / cookie | spec.openapis.org |
| OpenAPI 3.1 | Request Body | Payload of a request operation | spec.openapis.org |
| OpenAPI 3.1 | Response | Expected output for a status code | spec.openapis.org |
| OpenAPI 3.1 | Schema Object | Data type definition, based on JSON Schema | spec.openapis.org |
| OpenAPI 3.1 | Components | Reusable definitions (schemas, responses, params, etc.) | spec.openapis.org |
| OpenAPI 3.1 | Security Scheme | Auth mechanism: apiKey / http / oauth2 / openIdConnect | spec.openapis.org |
| OpenAPI 3.1 | Server | Base URL + variable substitution for API endpoints | spec.openapis.org |
| OpenAPI 3.1 | Webhook | Out-of-band callback definition | spec.openapis.org |
| OpenAPI 3.1 | operationId | Unique case-sensitive identifier for an operation | spec.openapis.org |
| OpenAPI 3.1 | $ref | Reference Object pointing to a component | spec.openapis.org |
| JSON-LD 1.1 | @context | Mapping of terms to IRIs; establishes vocabulary | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | @id | IRI uniquely identifying a node | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | @type | RDF type of a node or value | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | @graph | Named graph containing a set of nodes | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | @value | Typed or language-tagged literal value | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | @vocab | Default vocabulary prefix for unmapped terms | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | Node | JSON-LD object representing a resource | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | IRI | Internationalized Resource Identifier (global unique ID) | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | Linked Data | Web of machine-readable, interlinked structured data | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | compaction | Simplifying JSON-LD using a context | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | expansion | Removing context to produce full IRI representation | w3.org/TR/json-ld11 |
| JSON-LD 1.1 | framing | Reshaping JSON-LD into a desired tree structure | w3.org/TR/json-ld11 |

---

## 2. Chinese Ecosystem (English naming)

| Repo | Term | Class / Concept | Stars | Category |
|---|---|---|---|---|
| QwenLM/Qwen-Agent | Agent | Base agent class with planning + memory + tool use | ~22K | Alibaba |
| QwenLM/Qwen-Agent | Tool | Callable function exposed to the agent | ~22K | Alibaba |
| QwenLM/Qwen-Agent | Function Calling | Mechanism for LLM to call external functions | ~22K | Alibaba |
| QwenLM/Qwen-Agent | MCP | Model Context Protocol integration | ~22K | Alibaba |
| QwenLM/Qwen-Agent | Code Interpreter | Built-in tool for executing Python code | ~22K | Alibaba |
| QwenLM/Qwen-Agent | RAG | Retrieval-Augmented Generation pipeline | ~22K | Alibaba |
| QwenLM/Qwen-Agent | Memory | Agent memory for multi-turn conversation | ~22K | Alibaba |
| QwenLM/Qwen-Agent | reasoning_content | Field for chain-of-thought / scratchpad content | ~22K | Alibaba |
| InternLM/lagent | Agent | Base class (PyTorch-inspired layer analogy) | ~7K | Shanghai AI Lab |
| InternLM/lagent | AgentMessage | Typed message unit with sender/receiver/content | ~7K | Shanghai AI Lab |
| InternLM/lagent | Memory | State store; auto-populated on forward pass | ~7K | Shanghai AI Lab |
| InternLM/lagent | Action | Executable unit that agents can perform | ~7K | Shanghai AI Lab |
| InternLM/lagent | Tool | External callable registered with agent | ~7K | Shanghai AI Lab |
| InternLM/lagent | AgentStatusCode | Enum: END, STREAM, ERROR, etc. | ~7K | Shanghai AI Lab |
| InternLM/lagent | pre_hooks / post_hooks | Lifecycle hooks for message processing | ~7K | Shanghai AI Lab |
| modelscope/agentscope | Agent | Core abstraction for both single and multi-agent | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | Tool | Skill callable by agents | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | Skill | Higher-level reusable capability | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | Memory | Agent state persistence | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | Planning | Strategy layer for multi-step task decomposition | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | ReAct agent | Built-in ReAct (Reasoning+Action) agent pattern | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | message hub | Central bus for flexible multi-agent communication | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | workflow | Structured execution graph for agent tasks | ~9K | Alibaba/ModelScope |
| modelscope/agentscope | human-in-the-loop | Built-in steering from human operator | ~9K | Alibaba/ModelScope |
| geekan/MetaGPT | Role | LLM-backed persona (ProductManager, Architect, etc.) | ~55K | Independent |
| geekan/MetaGPT | Action | Atomic task a Role can execute | ~55K | Independent |
| geekan/MetaGPT | Message | Communication unit between Roles | ~55K | Independent |
| geekan/MetaGPT | Environment | Shared context where Roles interact | ~55K | Independent |
| geekan/MetaGPT | Memory | Role's history of messages and observations | ~55K | Independent |
| geekan/MetaGPT | Team | Collection of Roles working on a goal | ~55K | Independent |
| geekan/MetaGPT | SOP | Standard Operating Procedure — structured workflow | ~55K | Independent |
| geekan/MetaGPT | Workflow | Sequence of actions and roles | ~55K | Independent |
| OpenBMB/ChatDev | Agent | Role-playing LLM agent (CEO, CTO, Programmer…) | ~27K | Tsinghua/OpenBMB |
| OpenBMB/ChatDev | Role | Agent identity/persona in virtual company | ~27K | Tsinghua/OpenBMB |
| OpenBMB/ChatDev | Workflow | Multi-agent orchestration definition | ~27K | Tsinghua/OpenBMB |
| OpenBMB/ChatDev | Task | Software development objective | ~27K | Tsinghua/OpenBMB |
| OpenBMB/ChatDev | MacNet | Directed acyclic graph of communicative agents | ~27K | Tsinghua/OpenBMB |
| OpenBMB/ChatDev | Orchestrator | Central coordinator (puppeteer pattern, RL-trained) | ~27K | Tsinghua/OpenBMB |
| deepseek-ai/DeepSeek-V3 | (base model — no framework abstractions) | — | ~100K | DeepSeek AI |
| THUDM/ChatGLM3 | Tool Use | Function calling capability for bilingual LLM | ~14K | Tsinghua |

> **Finding**: Chinese repos universally adopt English naming conventions identical to Western frameworks. No unique Chinese-exclusive terms detected. They add `reasoning_content`, `MacNet`, `SOP`, and `Puppeteer` as original contributions but build on the same core vocabulary: Agent, Tool, Memory, Action, Role, Message, Workflow.

---

## 3. Academic Origins

| Term | Paper | Year | Authors | Status |
|---|---|---|---|---|
| Tool use (LLMs) | Toolformer: Language Models Can Teach Themselves to Use Tools | 2023 | Schick, Dwivedi-Yu et al. (Meta) | **Adopted — industry standard** |
| API call | Toolformer | 2023 | Schick et al. | Adopted (often called "function call") |
| Self-supervised tool learning | Toolformer | 2023 | Schick et al. | Niche (training method) |
| ReAct (Reasoning + Acting) | ReAct: Synergizing Reasoning and Acting in Language Models | 2022 | Yao, Zhao et al. (Princeton/Google) | **Adopted — core pattern** |
| Thought / Action / Observation | ReAct | 2022 | Yao et al. | **Adopted — universal loop** |
| Reasoning trace | ReAct | 2022 | Yao et al. | Adopted |
| Chain-of-Thought (CoT) | Chain-of-Thought Prompting Elicits Reasoning in LLMs | 2022 | Wei et al. (Google) | **Adopted — universal term** |
| Few-shot prompting | Chain-of-Thought | 2022 | Wei et al. | Adopted |
| Tree of Thoughts (ToT) | Tree of Thoughts: Deliberate Problem Solving with LLMs | 2023 | Yao et al. (Princeton) | Adopted (niche for search tasks) |
| Deliberate problem solving | Tree of Thoughts | 2023 | Yao et al. | Niche |
| Backtracking (in LLM search) | Tree of Thoughts | 2023 | Yao et al. | Niche |
| Retrieval-Augmented Generation (RAG) | Retrieval-Augmented Generation for Knowledge-Intensive NLP | 2020 | Lewis et al. (Facebook AI) | **Adopted — universal term** |
| Retriever | RAG paper | 2020 | Lewis et al. | **Adopted** |
| Generator | RAG paper | 2020 | Lewis et al. | Adopted |
| Knowledge-intensive NLP | RAG paper | 2020 | Lewis et al. | Academic; "RAG" replaced it |
| Reward model | Deep RLHF (Learning to Summarize with Human Feedback) | 2020–2022 | Stiennon / Christiano et al. | **Adopted** |
| Human feedback | RLHF | 2017–2022 | Christiano et al. | **Adopted** |
| Preference | RLHF | 2017–2022 | Christiano et al. | **Adopted** |
| Constitutional AI | Constitutional AI: Harmlessness from AI Feedback | 2022 | Bai et al. (Anthropic) | Adopted (Anthropic-centric) |
| Critique / Revision | Constitutional AI | 2022 | Bai et al. | Niche |
| Harmlessness / Helpfulness | Constitutional AI | 2022 | Bai et al. | **Adopted — alignment vocabulary** |
| Direct Preference Optimization (DPO) | Direct Preference Optimization: Your LM is Secretly a Reward Model | 2023 | Rafailov et al. (Stanford) | **Adopted — fine-tuning standard** |
| Policy (LLM as) | DPO | 2023 | Rafailov et al. | Adopted |
| Preference data | DPO | 2023 | Rafailov et al. | Adopted |
| Structured generation | Outlines / multiple papers | 2023+ | dottxt team | **Adopted** |
| Constrained decoding | Outlines et al. | 2023+ | — | Adopted |
| Module (LLM program) | DSPy: Compiling Declarative LM Calls | 2023 | Khattab et al. (Stanford) | Adopted (DSPy ecosystem) |
| Signature (input→output) | DSPy | 2023 | Khattab et al. | Adopted (DSPy ecosystem) |
| Optimizer / Teleprompter | DSPy | 2023 | Khattab et al. | Niche (DSPy-specific) |
| Demonstrate-Search-Predict (DSP) | DSP paper | 2022 | Khattab et al. | Superseded by DSPy |

---

## 4. GitHub Core Abstractions (>5K stars)

| Repo | Stars | Core Classes / Abstractions | Category |
|---|---|---|---|
| langchain-ai/langchain | 131K | Chain, Agent, Tool, Retriever, Memory, Prompt, LLM, ChatModel, Embedding, VectorStore, Document, Loader, OutputParser, Callback, Runnable (LCEL), Toolkit, Tracer | Agent Engineering Platform |
| microsoft/autogen | 56K | AssistantAgent, UserProxyAgent, ConversableAgent, GroupChat, Agent, Message, Tool, McpWorkbench, Task, Runtime, StdioServerParams | Multi-agent Framework |
| mem0ai/mem0 | 51K | Memory, UserMemory, SessionMemory, AgentState, MemoryLayer, add/get/search/update/delete, UserID | Memory Layer |
| run-llama/llama_index | 48K | Index, QueryEngine, Retriever, Node, Document, Loader, Embedding, VectorStore, LLM, Agent, Tool, Workflow, Parse, Extract, Pipeline | RAG + Agent Framework |
| crewAIInc/crewAI | 47K | Crew, Agent, Task, Tool, Process (sequential/hierarchical), Role, Goal, Backstory, Flow (event-driven), KickOff | Multi-agent Orchestration |
| BerriAI/litellm | 41K | completion, embedding, Router, Proxy, Gateway, model, messages, cost tracking, guardrails, loadbalancing, logging | LLM Gateway / Router |
| stanfordnlp/dspy | 33K | Module, Signature, Predict, ChainOfThought, ReAct, Retrieve, Teleprompter, Optimizer, Example, Assertion | LM Programming |
| microsoft/semantic-kernel | 27K | Kernel, Plugin, Function, Memory, Prompt, Agent, Process, Filter, Connector, PromptTemplate, ChatHistory | Enterprise Agent SDK |
| dottxt-ai/outlines | 13K | model, output_type, StructuredGenerator, regex, JSON schema, grammar, constrained decoding, FSM | Structured Output |
| jxnl/instructor | 12K | Instructor, response_model, BaseModel (Pydantic), structured output, retry, validation, patch | Structured Extraction |

---

## 5. Universal Terms (appear in 5+ sources)

| Term | Sources Count | Sources | Category | CEX Kind Match |
|---|---|---|---|---|
| **Agent** | 13 | MCP, A2A, Qwen-Agent, lagent, AgentScope, MetaGPT, ChatDev, LangChain, LlamaIndex, CrewAI, AutoGen, Semantic-Kernel, mem0 | Entity | P-kind: intelligent actor |
| **Tool** | 12 | MCP (core), A2A (AgentSkill), Qwen-Agent, lagent, AgentScope, MetaGPT, LangChain, LlamaIndex, CrewAI, AutoGen, Semantic-Kernel, Toolformer | Capability | P04_tools |
| **Memory** | 9 | lagent, AgentScope, MetaGPT, LangChain, LlamaIndex, AutoGen, Semantic-Kernel, mem0, Qwen-Agent | State | P01_knowledge |
| **Workflow** | 9 | A2A, AgentScope, ChatDev, MetaGPT, LangChain (LangGraph), LlamaIndex, CrewAI, Semantic-Kernel (Process), AgentScope | Orchestration | N05_operations |
| **Message** | 8 | A2A (core), lagent (AgentMessage), AgentScope (message hub), MetaGPT, LangChain, AutoGen, ChatGLM3, MCP | Communication | P05_output |
| **Schema** | 8 | JSON Schema (core), OpenAPI (Schema Object), MCP (JSON-RPC), A2A, instructor, outlines, JSON-LD (node), LangChain | Structure | P06_schema |
| **RAG** | 7 | Lewis et al. 2020 (coined), Qwen-Agent, LlamaIndex, LangChain, AgentScope, DSPy (Retrieve), mem0 | Pattern | P01_knowledge |
| **Prompt** | 7 | MCP (resource type), LangChain, LlamaIndex, Semantic-Kernel, DSPy (Signature), AutoGen, Qwen-Agent | Instruction | P03_prompt |
| **Task** | 7 | A2A (core lifecycle), CrewAI (core), AutoGen, LangChain, MetaGPT, ChatDev, lagent | Work Unit | N05_operations |
| **Role** | 6 | MetaGPT (core), ChatDev (core), CrewAI (Agent.role), A2A (AgentCard), AgentScope, OpenAPI (tag grouping) | Identity | P01_knowledge |
| **Action** | 6 | lagent (core), AgentScope, MetaGPT (core), ChatDev, ReAct paper, DSPy (ReAct) | Execution | P04_tools |
| **Embedding** | 5 | LangChain, LlamaIndex, Semantic-Kernel, mem0, litellm | Representation | P02_model |
| **Function / Function Calling** | 5 | Qwen-Agent (core), OpenAPI (operation), MCP (tool impl), LangChain (ToolCall), Semantic-Kernel (Plugin.Function) | Invocation | P04_tools |
| **Retriever** | 5 | RAG paper (coined), LangChain, LlamaIndex, DSPy (Retrieve), mem0 | Data Access | P01_knowledge |
| **Structured Output** | 5 | outlines, instructor, OpenAPI (Schema), JSON Schema, MCP (tool result) | Data Shape | P06_schema |

---

## 6. CEX Validation Matrix

> Maps CEX knowledge layers (P01–P06 + N01–N07) to source coverage

| CEX Layer | Provider (OpenAI/Anthropic/etc.) | Framework (LangChain/LlamaIndex) | Standard (MCP/A2A/OpenAPI) | Chinese (Qwen/MetaGPT/lagent) | Paper (coined term) | TOTAL sources |
|---|---|---|---|---|---|---|
| **P01_knowledge** (Memory, RAG, Retriever, Role) | ✓ | ✓ ✓ ✓ | ✓ (MCP Resource) | ✓ ✓ ✓ | ✓ RAG-Lewis2020 | **5+** |
| **P02_model** (Embedding, LLM, ChatModel) | ✓ | ✓ ✓ | ✓ (OpenAPI server) | ✓ | — | **4+** |
| **P03_prompt** (Prompt, Template, Signature) | ✓ | ✓ ✓ | ✓ (MCP Prompt) | ✓ | ✓ CoT-Wei2022 | **5+** |
| **P04_tools** (Tool, Action, Function, Plugin) | ✓ | ✓ ✓ ✓ | ✓ (MCP Tool) | ✓ ✓ ✓ | ✓ Toolformer2023 | **6+** |
| **P05_output** (Message, Response, Artifact) | ✓ | ✓ ✓ | ✓ (A2A Artifact, OpenAPI Response) | ✓ ✓ | — | **4+** |
| **P06_schema** (Schema, $ref, Type, Format) | ✓ | ✓ (instructor, outlines) | ✓ (JSON Schema, OpenAPI) | ✓ (MCP input schema) | ✓ DSPy Signature | **5+** |
| **N01_intelligence** (Agent, Reasoning, ReAct) | ✓ | ✓ ✓ ✓ | ✓ (A2A Agent) | ✓ ✓ ✓ | ✓ ReAct-Yao2022 | **6+** |
| **N03_engineering** (Workflow, Process, Pipeline) | ✓ | ✓ ✓ ✓ | ✓ (A2A Task lifecycle) | ✓ ✓ ✓ | ✓ DSPy | **6+** |
| **N05_operations** (Task, Orchestration, Flow) | ✓ | ✓ ✓ | ✓ (A2A Task states) | ✓ ✓ | — | **4+** |

---

## 7. Key Observations

### A. Convergence on Core 8 Terms
Every source category (standard, Chinese, paper, GitHub) uses these exact terms in English:
**Agent · Tool · Memory · Message · Schema · Prompt · Workflow · Task**

### B. MCP + A2A Are Emerging Standards
- **MCP** (2024): Tool/Resource/Prompt triad — already integrated by Qwen-Agent, AgentScope, AutoGen, Semantic Kernel
- **A2A** (2025): Agent/Task/AgentCard — adopted by AgentScope, LangGraph, BeeAI
- Both define wire-level contracts (JSON-RPC 2.0, HTTPS+SSE)

### C. Chinese Repos = Western Vocabulary
No divergence. Qwen, MetaGPT, lagent, AgentScope all use the exact same English terms for Agent/Tool/Memory/Action/Role. Original Chinese contributions:
- `reasoning_content` (Qwen — chain-of-thought field)
- `MacNet` (ChatDev — DAG topology for multi-agent)
- `SOP` as a formal agent concept (MetaGPT)
- `Puppeteer` (ChatDev — RL-trained orchestrator)

### D. Paper Terms That Became Industry Standard
| Paper Term | Now Called | Status |
|---|---|---|
| "use tool" (Toolformer) | function calling / tool use | Universal |
| ReAct loop | Thought/Action/Observation | Universal |
| Chain-of-Thought | CoT / reasoning | Universal |
| Retrieval-Augmented Generation | RAG | Universal |
| Direct Preference Optimization | DPO / RLHF alternative | Standard training term |
| Structured generation | structured outputs | Universal |

### E. CEX Coverage: All 15 Universal Terms Are Well-Sourced
No CEX layer lacks multi-source validation. P04_tools (Tool) has the highest coverage at 6+ independent sources.

---

*Generated by research_agent C research run — 2026-03-29*
*Sources: 5 standards specs + 7 Chinese repos + 8 papers + 10 GitHub repos = 30 sources total*
