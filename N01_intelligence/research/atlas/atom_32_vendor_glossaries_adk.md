---
id: atom_32_vendor_glossaries_adk
kind: knowledge_card
pillar: P01
domain: vendor_glossaries
title: "ATOM-32: Cloud Vendor Glossaries + Google Vertex AI ADK Deep Dive"
version: 1.0.0
date: 2026-04-13
quality: null
tags: [glossary, vendor, google, aws, azure, anthropic, huggingface, adk, agents, multi-agent, orchestration]
sources:
  - https://developers.google.com/machine-learning/glossary
  - https://developers.google.com/machine-learning/glossary/generative
  - https://adk.dev/
  - https://adk.dev/agents/multi-agents/
  - https://adk.dev/agents/llm-agents/
  - https://docs.aws.amazon.com/bedrock/latest/userguide/key-definitions.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html
  - https://learn.microsoft.com/en-us/azure/machine-learning/azure-machine-learning-glossary
  - https://platform.claude.com/docs/en/docs/about-claude/glossary
  - https://huggingface.co/docs/smolagents/reference/agents
  - https://huggingface.co/docs/smolagents/en/guided_tour
---

# ATOM-32: Cloud Vendor Glossaries + Google Vertex AI ADK

## 1. Term Counts per Vendor

| Vendor | Source | Estimated Terms | Agent-Specific Terms | Scope |
|--------|--------|----------------:|---------------------:|-------|
| **Google ML Glossary** | developers.google.com/machine-learning/glossary | ~500+ | ~30 | Full ML lifecycle: fundamentals, gen AI, agents, clustering, decision forests, metrics, fairness, TensorFlow, Google Cloud |
| **Google ADK** | adk.dev (formerly google.github.io/adk-docs) | ~85 | ~85 | Agent development: types, runtime, sessions, memory, tools, callbacks, deployment, protocols |
| **AWS Bedrock** | docs.aws.amazon.com/bedrock | ~45 | ~35 | Foundation models, agents, guardrails, knowledge bases, collaboration |
| **Azure ML** | learn.microsoft.com/azure/machine-learning | ~25 | ~5 | Platform-focused: compute, component, datastore, environment, model, workspace |
| **Anthropic Claude** | platform.claude.com/docs | ~12 | ~3 | Core LLM concepts: context window, tokens, RLHF, RAG, MCP, temperature |
| **HuggingFace smolagents** | huggingface.co/docs/smolagents | ~60 | ~60 | Agent framework: agent types, tools, models, executors, memory, prompts, multi-agent |
| **TOTAL** | | **~727** | **~218** | |

## 2. Google ML Glossary -- Category Breakdown

The Google ML Glossary is the largest single-vendor glossary with 500+ terms across these categories:

| Category | Approx. Terms | Representative Terms |
|----------|-------------:|----------------------|
| ML Fundamentals | ~145 | backpropagation, gradient descent, loss function, overfitting, regularization |
| Generative AI | ~155 | agent, agentic workflow, hallucination, prompt engineering, chain-of-thought, RLHF |
| Agent/Agentic | ~12 | agent, agentic loop, autonomous agent, action space, reflection, human-in-the-loop |
| Clustering | ~8 | centroid, k-means, hierarchical clustering |
| Decision Forests | ~10 | random forest, gradient boosted trees, bagging |
| Metrics | ~20 | accuracy, precision, recall, F1, AUC, mAP@k |
| Responsible AI | ~15 | fairness, bias, counterfactual fairness, demographic parity |
| TensorFlow | ~5 | tf.function, eager execution, SavedModel |
| Google Cloud | ~5 | Vertex AI, TPU, Cloud AI Platform |

### Key Agent Terms from Google ML Glossary

| Term | Definition (condensed) |
|------|------------------------|
| Agent | Software that reasons about inputs to plan and execute actions |
| Agentic Loop | Four-stage cycle: observe, reason, act, feedback |
| Autonomous Agent | Works toward complex goals without continuous human intervention |
| Action Space | Resources available for agent task execution |
| Reflection | Strategy improving agentic workflow quality via output examination |
| Human-in-the-Loop (HITL) | Policy ensuring people shape model behavior |
| Model Cascading | System selecting ideal model for specific inference queries |
| Model Router | Algorithm determining ideal model for inference |

## 3. Google Vertex AI ADK -- Agent Type Hierarchy (Deep Dive)

The ADK (Agent Development Kit) defines the most structured agent type hierarchy of any vendor. This is the most relevant section for CEX orchestration mapping.

### 3.1 Type Hierarchy

```
BaseAgent (abstract)
  |
  +-- LlmAgent (alias: Agent)
  |     Core LLM-powered agent with tools, instructions, model
  |     Properties: name, description, instruction, model, tools,
  |                 input_schema, output_schema, output_key,
  |                 generate_content_config, code_executor, planner,
  |                 include_contents, before_agent_callback,
  |                 after_agent_callback, disallow_transfer_to_parent,
  |                 disallow_transfer_to_peers
  |
  +-- SequentialAgent (workflow)
  |     Executes sub_agents in order, shared state via session.state
  |     Termination: after last sub-agent completes
  |
  +-- ParallelAgent (workflow)
  |     Runs sub_agents concurrently, shared session.state
  |     Events may interleave; all children read/write same state
  |
  +-- LoopAgent (workflow)
  |     Repeats sub_agents sequentially until:
  |       - max_iterations reached, OR
  |       - sub-agent returns Event with escalate=True
  |
  +-- CustomAgent (extends BaseAgent)
        User-defined logic, no LLM flow control
```

### 3.2 Communication Mechanisms

| Mechanism | Type | Description |
|-----------|------|-------------|
| **session.state** | Passive | Key-value store; agents write via `output_key`, others read |
| **Agent Transfer** | Active (LLM-driven) | LLM generates `transfer_to_agent(agent_name)` call; AutoFlow intercepts and switches context |
| **AgentTool** | Active (explicit) | Wraps a BaseAgent as a callable tool in another agent's tool list |
| **InvocationContext** | Runtime | Propagated through hierarchy; carries session, state, branch IDs |

### 3.3 Multi-Agent Patterns

| Pattern | Implementation | Description |
|---------|---------------|-------------|
| **Coordinator/Dispatcher** | LlmAgent + sub_agents | Central agent routes based on description metadata |
| **Sequential Pipeline** | SequentialAgent | Fixed-order execution, state passed via output_key |
| **Parallel Fan-Out/Gather** | ParallelAgent + SequentialAgent | Concurrent execution then aggregation step |
| **Hierarchical Decomposition** | Nested agent trees | Multi-level delegation via tool responses or state |
| **Generator-Critic** | SequentialAgent(generator, critic) | One produces, other reviews via state reference |
| **Iterative Refinement** | LoopAgent | Repeated improve cycles until convergence/escalation |
| **Human-in-the-Loop** | Callback + policy | Human decision points with optional automation |

### 3.4 ADK Runtime Concepts

| Concept | Definition |
|---------|------------|
| Session | Single ongoing interaction between user and agent system |
| SessionService | Lifecycle manager for Session objects (CRUD + events) |
| MemoryService | Long-term knowledge storage spanning multiple sessions |
| Event | Chronological entry in a Session (messages + actions) |
| State (session.state) | Per-session key-value data store |
| Memory | Searchable store across past sessions and external sources |
| Runner | Core event loop powering ADK (yield/pause/resume cycle) |
| RunConfig | Configuration for runtime behavior |
| InvocationContext | Runtime context propagated through agent hierarchy |
| Artifact | Structured data object within agent execution |
| A2A Protocol | Agent-to-Agent communication specification |
| AutoFlow | Default framework interpreting LLM transfer calls |

### 3.5 ADK Tool Types

| Tool Type | Description |
|-----------|-------------|
| Function Tools | Custom callable Python functions |
| OpenAPI Tools | REST API integration via OpenAPI specs |
| MCP Tools | Model Context Protocol extensions |
| GoogleSearchTool | Native Google Search integration |
| AgentTool | Wraps another agent as a callable tool |

### 3.6 ADK Deployment Targets

| Target | Type |
|--------|------|
| Agent Engine | Vertex AI managed service |
| Cloud Run | Serverless containers |
| GKE | Kubernetes orchestration |
| Local (`adk web`, `adk run`) | Development/testing |
| API Server (`adk api_server`) | RESTful exposure |

## 4. AWS Bedrock -- Agent Concepts

### 4.1 Core Terms (16 official key definitions)

| Term | Definition |
|------|------------|
| Foundation Model (FM) | AI model with large parameters trained on massive diverse data |
| Base Model | FM packaged by a provider, ready to use through Bedrock |
| Model Inference | Process of FM generating output from input |
| Prompt | Input provided to guide model response |
| Token | Sequence of characters interpreted as single unit of meaning |
| Model Parameters | Values defining model behavior (provider-controlled) |
| Inference Parameters | Values adjustable during inference (temperature, length, etc.) |
| Playground | GUI for experimenting with model inference |
| Embedding | Transforming input into numerical vector for similarity comparison |
| Orchestration | Coordinating between FMs and enterprise data/apps |
| Agent | Application carrying out orchestrations cyclically using FM |
| RAG | Process querying data sources to augment prompts |
| Model Customization | Adjusting parameter values using training data |
| Hyperparameters | Values controlling training process for custom models |
| Model Evaluation | Evaluating and comparing model outputs |
| Provisioned Throughput | Purchased throughput level for inference rate |

### 4.2 Agent Architecture Terms

| Term | Definition |
|------|------------|
| ActionGroup | APIs and operations an agent can perform |
| KnowledgeBase | Managed RAG capability connecting FMs to company data |
| Guardrail | Safeguard policies preventing unwanted behavior |
| Supervisor Agent | Central agent routing questions to collaborators |
| Collaborator Agent | Domain specialist sub-agent handling specific tasks |
| AgentCollaboration | Multi-agent framework with supervisor-collaborator hierarchy |
| Task Routing | Supervisor directs requests to appropriate collaborator |
| Task Decomposition | Breaking complex problems into smaller parts |
| Hierarchical Collaboration | Supervisor oversees one or more collaborators |

### 4.3 Guardrail Policy Types (6 policies)

| Policy | Description |
|--------|-------------|
| Content Filters | Detect/filter harmful content: Hate, Insults, Sexual, Violence, Misconduct, Prompt Attack |
| Word Filters | Block specific words, phrases, profanity (exact match) |
| Denied Topics | Block user-defined undesirable topics |
| Sensitive Information Filters | PII redaction |
| Contextual Grounding Checks | Reduce hallucination by grounding in context |
| Automated Reasoning Checks | Formal logic to prevent factual errors |
| Image Content Filters | Filter harmful image content |

## 5. Azure ML -- Platform Terms

Azure's glossary is notably smaller and platform-focused rather than concept-focused:

| Term | Definition |
|------|------------|
| Component | Self-contained code doing one step in an ML pipeline |
| Compute | Designated compute resource (cluster, instance, Kubernetes, attached) |
| Data | URIs (uri_folder, uri_file), Tables (mltable), Primitives (string, boolean, number) |
| Datastore | Secure connection to Azure storage (Blob, Files, ADLS, ADLS Gen2) |
| Environment | Encapsulation of ML task environment (curated or custom) |
| Model | Binary files representing an ML model (custom_model, mlflow_model, triton_model) |
| Workspace | Top-level resource: jobs, logs, metrics, models, environments |

### Azure AI Agent Service (separate from ML glossary)

Microsoft's agent capabilities are distributed across Azure AI Foundry and Azure AI Agent Service, not centralized in a single glossary. Key concepts include:
- Azure AI Agent Service (managed agent runtime)
- Semantic Kernel (SDK for agent orchestration)
- AutoGen (multi-agent framework, Microsoft Research)
- Copilot Studio (low-code agent builder)

## 6. Anthropic Claude -- Glossary Terms

Anthropic's official glossary is intentionally minimal (12 terms), focused on core LLM concepts:

| Term | Definition |
|------|------------|
| Context Window | Amount of text a model can reference when generating |
| Fine-tuning | Further training a pretrained model with additional data |
| HHH | Helpful, Honest, Harmless -- Anthropic's alignment goals |
| Latency | Time from prompt to generated output |
| LLM | Large Language Model |
| MCP | Model Context Protocol -- open standard for LLM context |
| MCP Connector | API feature connecting to MCP servers from Messages API |
| Pretraining | Initial training on large unlabeled corpus |
| RAG | Retrieval Augmented Generation |
| RLHF | Reinforcement Learning from Human Feedback |
| Temperature | Parameter controlling output randomness |
| TTFT | Time to First Token |
| Tokens | Smallest units of a language model (~3.5 English chars for Claude) |

## 7. HuggingFace smolagents -- Agent Framework Terms

### 7.1 Agent Types

| Class | Description |
|-------|-------------|
| MultiStepAgent | Base class; ReAct framework (think-act-observe cycle) |
| CodeAgent | Generates tool calls as Python code (default) |
| ToolCallingAgent | Generates tool calls as JSON (OpenAI-compatible) |

### 7.2 Model Backends (7 providers)

| Class | Backend |
|-------|---------|
| InferenceClientModel | HuggingFace Inference Providers (Cerebras, Cohere, Fireworks, etc.) |
| TransformersModel | Local transformers pipeline |
| LiteLLMModel | 100+ providers via LiteLLM |
| AzureOpenAIModel | Azure OpenAI Service |
| AmazonBedrockModel | AWS Bedrock |
| OpenAIModel | OpenAI API direct |
| MLXModel | Apple MLX local inference |

### 7.3 Code Executors (6 types)

| Executor | Environment |
|----------|-------------|
| LocalPythonExecutor | Local Python (default) |
| E2BExecutor | E2B cloud sandbox |
| DockerExecutor | Docker container with Jupyter |
| ModalExecutor | Modal cloud sandbox |
| BlaxelExecutor | Blaxel hibernating VMs |
| WasmExecutor | WebAssembly via Pyodide + Deno |

### 7.4 Memory & Prompt System

| Concept | Description |
|---------|-------------|
| AgentMemory | Stores system prompt + all steps (TaskStep, ActionStep, PlanningStep) |
| PromptTemplates | System prompt + planning + managed agent + final answer templates |
| PlanningPromptTemplate | Templates for initial plan and plan updates |
| ManagedAgentPromptTemplate | Task and report templates for managed sub-agents |
| FinalAnswerPromptTemplate | Pre/post message templates for final answer |
| step_callbacks | Callbacks triggered at each agent step |
| planning_interval | Interval for running planning steps |
| final_answer_checks | Validation functions before accepting final answer |

### 7.5 Multi-Agent System

| Concept | Description |
|---------|-------------|
| managed_agents | List of sub-agents passed to manager agent |
| name + description | Required attributes for managed agents (embedded in manager's system prompt) |
| Hierarchical multi-agent | Manager agent delegates to specialized sub-agents |

### 7.6 Tool System

| Concept | Description |
|---------|-------------|
| Tool | Atomic function with name, description, input types, output type |
| @tool decorator | Converts function to Tool with auto-extracted metadata |
| Tool subclass | Manual Tool definition via Tool base class |
| WebSearchTool | Built-in DuckDuckGo web search |
| PythonInterpreterTool | Built-in code execution |
| Transcriber | Built-in Whisper-based speech-to-text |
| load_tool (from Hub) | Load community tools from HuggingFace Hub |
| output_schema | Structured output definition (especially for MCP tools) |

## 8. Cross-Vendor Overlap Analysis

### 8.1 Universal Terms (present in 4+ vendors)

| Term | Google | AWS | Azure | Anthropic | HuggingFace | Definition Consensus |
|------|--------|-----|-------|-----------|-------------|---------------------|
| Agent | Y | Y | N* | N | Y | Software that reasons + acts autonomously |
| Token | Y | Y | N | Y | Y | Smallest processable unit of text |
| Prompt | Y | Y | N | N | Y | Input text guiding model behavior |
| RAG | Y | Y | N | Y | N | Retrieval-augmented generation |
| Embedding | Y | Y | N | N | N | Numerical vector representation |
| Fine-tuning | Y | N | N | Y | N | Further training on specific data |
| Context Window | Y | N | N | Y | N | Max tokens a model can reference |
| Temperature | Y | N | N | Y | Y | Randomness control parameter |
| Foundation Model | Y | Y | N | N | N | Large pre-trained base model |
| Inference | Y | Y | N | N | Y | Using a model to generate output |
| Hallucination | Y | N | N | N | N | Plausible but factually incorrect output |
| RLHF | Y | N | N | Y | N | Reinforcement Learning from Human Feedback |
| MCP | Y (ADK) | N | N | Y | Y | Model Context Protocol |

*Azure has agents via Azure AI Agent Service but not in the ML glossary proper.

### 8.2 Unique Terms per Vendor

| Vendor | Unique/Distinctive Terms |
|--------|-------------------------|
| **Google ML** | AI Slop, Agentic Loop, Model Cascading, Model Router, Specificational Coding, Vibe Coding, Autorater, Flash Model, Nano, NORA/ORA |
| **Google ADK** | AutoFlow, AgentTool, LoopAgent, ParallelAgent, SequentialAgent, InvocationContext, session.state, output_key, A2A Protocol, disallow_transfer_to_parent |
| **AWS Bedrock** | ActionGroup, KnowledgeBase, Guardrail (6 policy types), Supervisor Agent, Collaborator Agent, AgentCollaboration, Provisioned Throughput, Automated Reasoning Checks |
| **Azure ML** | Component, Datastore, Workspace, Curated Environment, mltable, triton_model |
| **Anthropic** | HHH, MCP Connector, TTFT |
| **HuggingFace** | CodeAgent, ToolCallingAgent, MultiStepAgent, managed_agents, @tool decorator, PythonExecutor variants (6 types), GradioUI, REMOVE_PARAMETER |

### 8.3 Multi-Agent Orchestration Comparison

| Feature | Google ADK | AWS Bedrock | HuggingFace smolagents | CEX |
|---------|-----------|-------------|----------------------|-----|
| **Hierarchy model** | Parent-child via sub_agents | Supervisor-Collaborator | Manager + managed_agents | N07 orchestrator + N01-N06 nuclei |
| **Parallel execution** | ParallelAgent (native) | Parallel execution (claimed) | Not native | dispatch.sh grid (process-level) |
| **Sequential execution** | SequentialAgent | Via supervisor routing | Not native (single ReAct loop) | Wave-based sequential dispatch |
| **Loop/iteration** | LoopAgent (native) | Not native | max_steps on agent | cex_evolve.py loop |
| **Communication** | session.state + transfer | Supervisor routing | managed_agents + memory | Handoff files + signals + git |
| **Dynamic routing** | AutoFlow + transfer_to_agent() | Supervisor LLM routing | Manager LLM routing | N07 intent resolution + kinds_meta |
| **Explicit invocation** | AgentTool wrapper | ActionGroup | Tool wrapping | dispatch.sh solo |
| **State sharing** | session.state (in-memory) | Via supervisor context | agent.memory | .cex/runtime/ (file-based) |
| **Quality gates** | Not built-in | Guardrails | final_answer_checks | cex_score.py + 3-layer scoring |
| **Guardrails** | generate_content_config safety | 6 policy types (native) | Not built-in | 8F F7 GOVERN + quality gates |

## 9. CEX Pillar Mapping

### 9.1 Vendor Terms to CEX Pillars

| CEX Pillar | Google ADK | AWS Bedrock | HuggingFace | Anthropic |
|------------|-----------|-------------|-------------|-----------|
| **P01 Knowledge** | Memory, MemoryService | KnowledgeBase, RAG | AgentMemory | RAG |
| **P02 Model** | LlmAgent, model property | Foundation Model, Base Model | InferenceClientModel, TransformersModel | LLM, Fine-tuning |
| **P03 Prompt** | instruction, global_instruction | Prompt | PromptTemplates, system_prompt | Context Window, Tokens |
| **P04 Tools** | Function Tools, OpenAPI Tools, MCP Tools, AgentTool | ActionGroup | @tool, Tool class, WebSearchTool | MCP, MCP Connector |
| **P05 Output** | output_schema, output_key | Response | final_answer, output_type | - |
| **P06 Schema** | input_schema, output_schema | - | inputs dict, output_type | - |
| **P07 Evaluation** | Evaluation Framework, Custom Metrics | Model Evaluation, Guardrails | final_answer_checks | - |
| **P08 Architecture** | Agent hierarchy, A2A Protocol | AgentCollaboration, Supervisor pattern | Multi-agent hierarchy | - |
| **P09 Config** | RunConfig, generate_content_config | Inference Parameters, Hyperparameters | executor_type, model kwargs | Temperature |
| **P10 Memory** | Session, State, Memory, MemoryService | - | AgentMemory, write_memory_to_messages | - |
| **P11 Feedback** | Callbacks (before/after agent) | Guardrail policies (6 types) | step_callbacks, planning_interval | HHH alignment |
| **P12 Orchestration** | SequentialAgent, ParallelAgent, LoopAgent, AutoFlow | Multi-agent collaboration, Task routing | managed_agents, hierarchical multi-agent | - |

### 9.2 CEX Kind Candidates from Vendor Analysis

New kinds or kind enrichments suggested by vendor glossary analysis:

| Suggested Kind | Source Vendor | CEX Pillar | Rationale |
|---------------|--------------|------------|-----------|
| agent_transfer_rule | Google ADK | P12 | AutoFlow transfer configuration (disallow_transfer_to_parent/peers) |
| guardrail_policy | AWS Bedrock | P11 | 6 policy types for content safety |
| code_executor_config | HuggingFace | P09 | 6 executor types (local, e2b, docker, modal, blaxel, wasm) |
| agent_collaboration | AWS Bedrock | P12 | Supervisor-collaborator patterns |
| session_service | Google ADK | P10 | Session lifecycle management |
| memory_service | Google ADK | P10 | Cross-session knowledge store |
| planner | Google ADK | P03 | BuiltInPlanner, PlanReActPlanner |
| a2a_protocol | Google ADK | P06 | Agent-to-Agent communication spec |

## 10. Vertex ADK vs CEX Architecture Mapping

This section maps ADK concepts directly to CEX equivalents, identifying architectural alignment and gaps.

| ADK Concept | CEX Equivalent | Alignment |
|-------------|---------------|-----------|
| LlmAgent | Nucleus (N01-N06) | HIGH -- both are LLM-powered workers with instructions |
| SequentialAgent | Wave-based dispatch | HIGH -- CEX waves = ADK sequential sub_agents |
| ParallelAgent | Grid dispatch (dispatch.sh grid) | HIGH -- both run agents concurrently |
| LoopAgent | cex_evolve.py loop | MEDIUM -- CEX loop is file-based, not in-memory |
| BaseAgent | Nucleus base concept | HIGH -- abstract worker definition |
| AutoFlow | N07 intent resolution | HIGH -- both route tasks to specialized agents |
| session.state | .cex/runtime/ files | LOW -- ADK is in-memory KV, CEX is file-based |
| AgentTool | dispatch.sh solo | MEDIUM -- both invoke a single agent synchronously |
| Agent Transfer | Handoff files | MEDIUM -- ADK is runtime transfer, CEX is file-based handoff |
| InvocationContext | Handoff frontmatter + brand config | MEDIUM -- both propagate context through hierarchy |
| Session | CEX session (git branch state) | LOW -- fundamentally different persistence models |
| Memory/MemoryService | .cex/learning_records/ + P10 | MEDIUM -- both persist cross-session knowledge |
| RunConfig | .cex/config/ YAML files | HIGH -- both configure runtime behavior |
| Callbacks | cex_hooks.py pre/post | HIGH -- both intercept agent lifecycle events |
| A2A Protocol | Signal files + dispatch protocol | MEDIUM -- CEX uses file-based signals, not wire protocol |
| Guardrails (Bedrock) | 8F F7 GOVERN + quality gates | HIGH -- both enforce output quality constraints |

### Key Architectural Insight

ADK's strength is **in-process orchestration** -- agents share memory, transfer context in-memory, and communicate via shared state objects. CEX's strength is **inter-process orchestration** -- agents are separate OS processes communicating via files, git, and signals. This gives CEX:

1. **Isolation**: A crashed nucleus does not affect others
2. **Multi-model**: Each nucleus can use a different LLM provider
3. **Persistence**: All state survives process death (git-backed)
4. **Auditability**: Every handoff and signal is a file in version control

But CEX lacks ADK's:
1. **Low-latency transfer**: File I/O is slower than in-memory state
2. **Fine-grained state sharing**: No equivalent to session.state KV
3. **Native loop/parallel primitives**: CEX relies on shell scripts, not typed agent classes

## 11. Statistical Summary

| Metric | Value |
|--------|-------|
| Vendors analyzed | 6 |
| Total glossary terms catalogued | ~727 |
| Agent-specific terms | ~218 |
| Universal terms (4+ vendors) | 13 |
| Google ML Glossary categories | 10 |
| Google ADK agent types | 5 (LlmAgent, SequentialAgent, ParallelAgent, LoopAgent, CustomAgent) |
| Google ADK multi-agent patterns | 7 |
| AWS Bedrock guardrail policies | 7 (6 text + 1 image) |
| HuggingFace agent types | 3 (MultiStepAgent, CodeAgent, ToolCallingAgent) |
| HuggingFace executor types | 6 |
| HuggingFace model backends | 7 |
| CEX pillar coverage from vendor terms | 12/12 (all pillars mapped) |
| New CEX kind candidates identified | 8 |
| High-alignment ADK-CEX mappings | 7/16 |
