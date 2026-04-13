---
id: atom_08_crewai
kind: knowledge_card
pillar: P01
quality: 8.8
title: "CrewAI Deep Vocabulary Scrape"
tags: [crewai, agent, framework-atlas, v0.100+, lancedb, flows, events]
date: 2026-04-13
version: 2.0
---

# CrewAI: A Comprehensive Guide to Agents, Tasks, and Workflows

## Introduction

CrewAI is an open-source framework designed to enable the creation of autonomous, collaborative AI agents. This document serves as a technical reference, detailing the core components, workflows, and implementation patterns of the CrewAI ecosystem. It covers agents, tasks, crews, flows, memory systems, knowledge integration, tooling, event handling, and enterprise deployment options.

---

## Core Concepts

### Agents

Agents are autonomous entities defined by:
- **Role**: Function and expertise (e.g., "Data Analyst")
- **Goal**: Specific objective to achieve
- **Backstory**: Contextual narrative shaping behavior
- **Tools**: Capabilities for task execution
- **Reasoning**: Reflective planning mechanism
- **Memory**: Access to historical data and knowledge

```python
from crewai import Agent

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze financial datasets to identify trends",
    backstory="Experienced in statistical analysis and data visualization",
    tools=["Python", "Pandas", "Tableau"]
)
```

### Tasks

Tasks represent units of work with:
- **Description**: Statement of work
- **Expected Output**: Specification for completion
- **Dependencies**: Context from other task outputs
- **Guardrails**: Validation rules with retry logic

```python
from crewai import Task

analyze_data = Task(
    description="Perform exploratory data analysis on the dataset",
    expected_output="Summary statistics and visualizations",
    dependencies=[data_preprocessing_task],
    guardrail="Ensure results meet statistical significance thresholds"
)
```

### Crews

Crews orchestrate agents and tasks through process enums:
- **Sequential**: Tasks executed in order
- **Hierarchical**: Manager agent delegates tasks
- **Consensual**: Collaborative decision-making

```python
from crewai import Crew

financial_analysis_crew = Crew(
    agents=[data_analyst, report_writer],
    tasks=[analyze_data, generate_report],
    process="sequential"
)
```

### Flows

Event-driven orchestrators with:
- **@start**: Entry point decorators
- **@listen**: React to method outputs
- **@router**: Conditional branching
- **@persist**: State persistence
- **@human_feedback**: Human input integration

```python
from crewai import Flow

financial_flow = Flow(
    name="Quarterly Analysis",
    entry_points=[@start("initiate_analysis")],
    routers=[@router("data_quality_check", condition=check_data_quality)]
)
```

---

## Advanced Features

### Knowledge Integration

- **RAG Sources**: ChromaDB-powered retrieval
- **Knowledge Cards**: Structured domain knowledge
- **Embedder Configuration**: Custom vector embedding strategies
- **Chunking Strategy**: TF-IDF-based text segmentation

```python
from crewai import Knowledge

financial_knowledge = Knowledge(
    sources=["SEC filings", "Industry reports"],
    embedder="sentence-transformers/all-mpnet-base-v2",
    chunk_size=512
)
```

### Memory Systems

Unified memory with:
- **Scopes**: Contextual restrictions (e.g., "financial")
- **Composite Scoring**: Semantic + recency + importance
- **Persistence**: LanceDB + SQLite

```python
from crewai import Memory

analysis_memory = Memory(
    scope="financial",
    scoring_strategy="composite",
    persistence="lancedb"
)
```

### Tooling

- **BaseTool**: Abstract class for tool creation
- **@tool**: Function-based tool decorators
- **LangChain Compatibility**: Seamless integration

```python
from crewai import BaseTool

class DataValidator(BaseTool):
    @tool
    def validate_dataset(self, dataset):
        """Check dataset quality and completeness"""
        # Implementation details
```

---

## Enterprise Capabilities

### CrewAI AMP Cloud

- **Pricing Tiers**: $99/month (Starter) to $120,000/year (Enterprise)
- **Features**:
  - Auto-scaling agent pools
  - Real-time monitoring
  - Advanced security controls
  - Custom LLM integrations

### Deployment Options

- **CLI Commands**:
  ```bash
  crewai create -t agent -n "Data Analyst"
  crewai run -c financial_analysis_crew
  crewai test -p "financial"
  crewai deploy -e production
  ```

- **CI/CD Integration**: N05 operations pipeline

---

## Technical Architecture

### Comparison with CEX

| Dimension          | CrewAI                          | CEX                             |
|--------------------|----------------------------------|----------------------------------|
| **Composition Unit** | Agent (role+goal+backstory)     | Nucleus (domain+sin+builder ISOs) |
| **Orchestration**   | Crew (sequential/hierarchical)  | N07 + mission_runner (wave-based) |
| **State Management**| FlowState (Pydantic)           | Git + .cex/runtime/ (file-based) |
| **Memory System**   | Unified Memory (LanceDB)        | 4-type memory (correction/preference/convention/context) |
| **Knowledge**       | RAG (ChromaDB)                  | Knowledge Cards + retriever (TF-IDF) |
| **Quality Control** | crewai test (score 1-10)        | 3-layer scoring (structural+rubric+semantic) |

---

## Glossary

**A2A**: Agent-to-Agent protocol for cross-service delegation  
**BaseEvent**: Base class for all CrewAI events  
**CrewOutput**: Execution result (raw, pydantic, json_dict)  
**FlowState**: State object managed by Flow  
**MemoryScope**: Branch restriction for memory operations  
**RecallFlow**: Multi-step deep memory retrieval  
**@router**: Flow decorator for conditional branching  
**TaskOutput**: Task execution result object  
**@tool**: Decorator for function-based tool creation  

---

## Sources

- [CrewAI Documentation -- Agents](https://docs.crewai.com/en/concepts/agents)
- [CrewAI Documentation -- Tasks](https://docs.crewai.com/en/concepts/tasks)
- [CrewAI Documentation -- Crews](https://docs.crewai.com/en/concepts/crews)
- [CrewAI Documentation -- Flows](https://docs.crewai.com/en/concepts/flows)
- [CrewAI Documentation -- Knowledge](https://docs.crewai.com/en/concepts/knowledge)
- [CrewAI Documentation -- Memory](https://docs.crewai.com/en/concepts/memory)
- [CrewAI Documentation -- Tools](https://docs.crewai.com/en/concepts/tools)
- [CrewAI Documentation -- Events](https://docs.crewai.com/en/concepts/event-listener)
- [CrewAI Documentation -- CLI](https://docs.crewai.com/en/concepts/cli)
- [CrewAI Documentation -- Testing](https://docs.crewai.com/en/concepts/testing)
- [CrewAI Documentation -- Planning](https://docs.crewai.com/en/concepts/planning)
- [CrewAI Documentation -- LLM Connections](https://docs.crewai.com/en/learn/llm-connections)
- [CrewAI GitHub Repository](https://github.com/crewAIInc/crewAI)
- [CrewAI Pricing](https://crewai.com/pricing)

---

## ENRICHMENT v2.0 -- Implementation-Level Detail (v0.100+)

---

## Agent Parameters: Complete Reference

### Required
| Parameter | Type | Description |
|-----------|------|-------------|
| `role` | str | Function and expertise label |
| `goal` | str | Individual objective |
| `backstory` | str | Context/personality enrichment |

### Execution Control
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `llm` | Union[str, LLM, Any] | `OPENAI_MODEL_NAME` env or `gpt-4` | Primary LLM |
| `function_calling_llm` | Optional[Any] | None | Separate model for tool calling |
| `max_iter` | int | 20 | Max reasoning iterations |
| `max_rpm` | Optional[int] | None | Rate limit (requests/minute) |
| `max_execution_time` | Optional[int] | None | Timeout in seconds |
| `max_retry_limit` | int | 2 | Error retry count |
| `verbose` | bool | False | Logging verbosity |
| `cache` | bool | True | Cache tool results |
| `reasoning` | bool | False | Enable pre-task reflection |
| `max_reasoning_attempts` | Optional[int] | None | Cap planning iterations |
| `inject_date` | bool | False | Auto-inject current date |
| `date_format` | str | `%Y-%m-%d` | datetime format string |
| `multimodal` | bool | False | Enable image/text processing |
| `respect_context_window` | bool | True | Auto-summarize on token overflow |
| `allow_delegation` | bool | False | Allow delegating to other agents |
| `step_callback` | Optional[Any] | None | Called after each step |
| `system_template` | Optional[str] | None | Custom system prompt |
| `prompt_template` | Optional[str] | None | Custom input format |
| `response_template` | Optional[str] | None | Custom response format |
| `knowledge_sources` | Optional[List] | None | Per-agent knowledge bases |
| `embedder` | Optional[Dict] | None | Custom embedder config |

Deprecated in v0.100+: `allow_code_execution`, `code_execution_mode` -- use E2B or Modal sandbox services.

### YAML Configuration (agents.yaml)
```yaml
# config/agents.yaml
researcher:
  role: >
    {topic} Senior Research Analyst
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You work at a leading tech think tank specializing in {topic}.

data_analyst:
  role: >
    Financial Data Analyst
  goal: >
    Analyze datasets to identify trends and anomalies
  backstory: >
    Experienced in statistical analysis and quantitative modeling.
```

Variables (`{topic}`) resolved at `crew.kickoff(inputs={'topic': 'AI'})`.

### CrewBase YAML Binding Pattern
```python
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ResearchCrew:
    agents_config = 'config/agents.yaml'
    tasks_config  = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config['researcher'], verbose=True)

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks,
                    process=Process.sequential, verbose=True)
```

Python method names MUST match YAML keys.

---

## Task Parameters: Complete Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `description` | str | Required | Task specification |
| `expected_output` | str | Required | Completion criteria |
| `name` | Optional[str] | None | Identifier for logging |
| `agent` | Optional[BaseAgent] | None | Assigned executor |
| `tools` | List[BaseTool] | [] | Available tools |
| `context` | Optional[List[Task]] | None | Dependency task outputs |
| `async_execution` | Optional[bool] | False | Non-blocking execution |
| `human_input` | Optional[bool] | False | Require manual review |
| `markdown` | Optional[bool] | False | Format output as Markdown |
| `output_file` | Optional[str] | None | Save output to path |
| `create_directory` | Optional[bool] | True | Auto-create parent dirs |
| `output_json` | Optional[Type[BaseModel]] | None | Pydantic JSON output |
| `output_pydantic` | Optional[Type[BaseModel]] | None | Structured Pydantic output |
| `callback` | Optional[Any] | None | Post-completion function |
| `guardrail` | Optional[Callable] | None | Single validator |
| `guardrails` | Optional[List[Callable]] | None | Multiple validators |
| `guardrail_max_retries` | Optional[int] | 3 | Retry attempts on failure |
| `config` | Optional[Dict] | None | Custom settings |

### YAML Configuration (tasks.yaml)
```yaml
research_task:
  description: >
    Conduct thorough research on {topic}. Use web search and academic sources.
  expected_output: >
    A 3-paragraph brief with key facts, trends, and citations.
  agent: researcher
  markdown: true
  output_file: output/research_{topic}.md

analysis_task:
  description: >
    Analyze the research brief and produce financial projections.
  expected_output: >
    Financial model in JSON with projections for 3 years.
  agent: data_analyst
  output_json: FinancialModel
```

### Guardrails: Three Implementation Patterns

Pattern 1 -- Deterministic function:
```python
from crewai.tasks.task_output import TaskOutput
from typing import Tuple, Any

def validate_word_count(result: TaskOutput) -> Tuple[bool, Any]:
    if len(result.raw.split()) <= 200:
        return (True, result.raw)
    return (False, "Output exceeds 200 words.")
```

Pattern 2 -- LLM-evaluated string:
```python
Task(guardrail="Must be professional tone, under 200 words, no bullet points")
```

Pattern 3 -- Mixed multi-guardrail list:
```python
Task(guardrails=[validate_word_count, "Must cite at least 2 sources"],
     guardrail_max_retries=5)
```

### TaskOutput Fields
| Field | Type | Content |
|-------|------|---------|
| `raw` | str | String output |
| `json_dict` | Dict | Dictionary form |
| `pydantic` | BaseModel | Validated model instance |
| `summary` | str | First 10 words auto-generated |
| `messages` | List | Full LLM conversation history |

---

## Crew Parameters: Complete Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `agents` | List[Agent] | Required | Crew members |
| `tasks` | List[Task] | Required | Work units |
| `process` | Process | sequential | Execution strategy |
| `verbose` | bool | False | Logging |
| `manager_llm` | LLM | None | LLM for hierarchical manager |
| `manager_agent` | Agent | None | Custom manager agent |
| `function_calling_llm` | LLM | None | Crew-wide tool-call LLM |
| `memory` | Memory | None | Shared memory instance |
| `cache` | bool | True | Cache tool results |
| `embedder` | Dict | OpenAI | Embedder configuration |
| `max_rpm` | int | None | Rate limit |
| `planning` | bool | False | Enable AgentPlanner |
| `planning_llm` | LLM | None | LLM for planning step |
| `step_callback` | Callable | None | After each step |
| `task_callback` | Callable | None | After each task |
| `output_log_file` | bool/str | None | Log file (`.json` ext = JSON format) |
| `share_crew` | bool | False | Opt-in telemetry |
| `knowledge_sources` | List | None | Crew-level knowledge |
| `stream` | bool | False | Enable streaming output |

### Process Types
| Value | Behavior |
|-------|----------|
| `Process.sequential` | Tasks execute in list order |
| `Process.hierarchical` | Manager agent delegates; needs `manager_llm` or `manager_agent` |

### Kickoff Methods
| Method | Type | Description |
|--------|------|-------------|
| `kickoff(inputs={})` | Sync | Standard execution |
| `kickoff_for_each(inputs=[])` | Sync | Sequential per item |
| `akickoff(inputs={})` | Native async | True async/await |
| `akickoff_for_each(inputs=[])` | Native async | Async per item |
| `kickoff_async(inputs={})` | Thread-based | `asyncio.to_thread` wrapper |
| `kickoff_for_each_async(inputs=[])` | Thread-based | Thread-based iteration |

### CrewOutput Fields
| Field | Type | Content |
|-------|------|---------|
| `raw` | str | Final string output |
| `pydantic` | BaseModel | Structured output |
| `json_dict` | Dict | JSON representation |
| `tasks_output` | List[TaskOutput] | Per-task results |
| `token_usage` | Dict | LLM performance metrics |

---

## Unified Memory System (v0.100+)

### Architecture
v0.100+ consolidates short-term, long-term, entity, and external memory types into a single `Memory` class with LLM-powered scope inference. Breaking change from prior multi-type API.

### Storage Backends
| Backend | Purpose | Default Path |
|---------|---------|-------------|
| LanceDB | Vector + metadata | `./.crewai/memory` (env: `CREWAI_STORAGE_DIR`) |
| SQLite | Flow state (`@persist`) | Alongside LanceDB |
| Custom | Implement `StorageBackend` protocol | Any |

Concurrent writes: shared locking with automatic retry.

### Embedding Providers (11+)
| Provider | Default Model | Use Case |
|----------|--------------|----------|
| OpenAI | text-embedding-3-small | Default |
| Ollama | mxbai-embed-large | Local/offline |
| Azure OpenAI | text-embedding-ada-002 | Enterprise |
| Google AI/Vertex | gemini-embedding-001 | GCP |
| Cohere | -- | Semantic search |
| VoyageAI | -- | High accuracy |
| AWS Bedrock | -- | AWS ecosystem |
| Hugging Face | -- | Open-source |
| Jina | -- | Multilingual |
| IBM WatsonX | -- | Enterprise |
| Custom callable | -- | Full control |

### Composite Scoring Weights
| Parameter | Default | Effect |
|-----------|---------|--------|
| `semantic_weight` | 0.5 | Vector similarity |
| `recency_weight` | 0.3 | Temporal decay |
| `importance_weight` | 0.2 | Saved importance |
| `recency_half_life_days` | 30 | Decay period |
| `consolidation_threshold` | 0.85 | Duplicate detection |
| `batch_dedup_threshold` | 0.98 | Near-duplicate drop (cosine) |
| `query_analysis_threshold` | 200 | LLM-skip threshold (chars) |

Formula: `score = semantic_weight * similarity + recency_weight * decay + importance_weight * importance`

### Hierarchical Scopes
Filesystem-like tree: `/`, `/project/alpha`, `/agent/researcher`. LLM auto-suggests placement. `MemorySlice` enables views across multiple disjoint scopes; optional `read_only=True`.

### RecallFlow Modes
| Mode | Latency | Method |
|------|---------|--------|
| Shallow | ~200ms | Direct vector search, no LLM calls |
| Deep (default) | Varies | Query analysis + scope selection + parallel vector search |

LLM skipped automatically for queries under 200 characters.

### Memory API
```python
from crewai.memory import Memory

mem = Memory(semantic_weight=0.5, recency_weight=0.3, importance_weight=0.2)

# Store
mem.remember("Project deadline 2026-05-01", scope="/project/alpha")
mem.remember_many(["fact1", "fact2"])   # Non-blocking background thread

# Retrieve
results = mem.recall("project deadline", depth="deep", limit=5)
facts   = mem.extract_memories("Long meeting notes text ...")

# Delete / admin
mem.forget(scope="/project/alpha")
mem.tree()
mem.info("/project")
mem.list_records(scope="/project/alpha")
mem.reset()
mem.drain_writes()
mem.close()
```

CLI: `crewai memory` (TUI), `crewai memory --storage-path ./dir`

### Non-Blocking Guarantee
`remember_many()` returns immediately. Every `recall()` auto-calls `drain_writes()` before searching. Crew shutdown flushes pending saves in `finally`.

### Privacy
```python
mem.remember("Sensitive data", source="user:alice", private=True)
# Visible only when source matches; admin override: recall(include_private=True)
```

### Memory in Crews/Agents/Flows
| Context | Usage |
|---------|-------|
| `Crew(memory=True)` | Shared across all agents |
| `Agent(memory=True)` | Per-agent scoped view |
| Flow instance | `self.remember()`, `self.recall()`, `self.extract_memories()` |

### Failure Resilience (no exceptions raised for analysis failures)
- Save analysis failure: stores at `/`, importance 0.5
- Extract failure: full content as single record
- Query analysis failure: falls back to vector search
- Storage/embedder failures DO propagate

---

## Flow System: Complete Decorator Reference

### @start() -- Entry Points
```python
from crewai.flow.flow import Flow, start, listen, router, persist

class MyFlow(Flow):
    @start()
    def begin(self):
        return "initial data"

    @start("begin")                              # Fires after 'begin' method
    def begin_after(self): pass

    @start(lambda self: self.state.get("ready")) # Callable condition
    def begin_if_ready(self): pass
```

### @listen() -- Reactive Triggers
```python
    @listen("begin")              # By name string; receives output as arg
    def process(self, output):
        return f"processed: {output}"

    @listen(begin)                # Direct reference
    def process_ref(self, output): pass
```

### @router() -- Conditional Branching
```python
    @router(begin)
    def route(self):
        return "success" if self.state.get("quality", 0) > 8 else "failed"

    @listen("success")
    def on_success(self): pass

    @listen("failed")
    def on_failed(self): pass
```

### @persist -- State Persistence
```python
@persist
class MyFlow(Flow): pass          # Class-level: all methods persisted

class MyFlow(Flow):
    @persist
    @start()
    def start_method(self): pass  # Method-level
```
Default backend: SQLiteFlowPersistence. Custom backends supported.

### @human_feedback -- HITL (v1.8.0+)
```python
    @human_feedback(
        message="Please review and approve the report:",
        emit=["approved", "needs_revision", "rejected"],
        llm="gpt-4o-mini",
        default_outcome="needs_revision"
    )
    @listen("generate_report")
    def review(self):
        pass

    @listen("approved")
    def finalize(self):
        feedback = self.last_human_feedback.feedback
        history  = self.human_feedback_history
```

### Conditional Logic: or_() and and_()
```python
from crewai.flow.flow import or_, and_

    @listen(or_(method_a, method_b))    # Fires when EITHER completes
    def on_either(self, result): pass

    @listen(and_(method_a, method_b))   # Fires only when BOTH complete
    def on_both(self): pass
```

### FlowState Variants

Unstructured (dict):
```python
class MyFlow(Flow):
    @start()
    def begin(self):
        self.state["counter"] = 0
        self.state["id"]      # Auto-generated UUID
```

Structured (Pydantic):
```python
class MyState(BaseModel):
    counter: int = 0
    message: str = ""

class MyFlow(Flow[MyState]):   # 'id' field auto-added
    @start()
    def begin(self):
        self.state.counter += 1
```

### Execution Methods
```python
result = flow.kickoff()
result = flow.kickoff(inputs={"topic": "AI"})
result = await flow.kickoff_async()

# Visualization
flow.plot("my_flow")           # Generates my_flow.html
# crewai flow plot

# Streaming
class MyFlow(Flow):
    stream = True

streaming = flow.kickoff()
for chunk in streaming:
    print(chunk.content, end="", flush=True)
result = streaming.result
```

### Built-in Flow Memory Methods
```python
class MyFlow(Flow):
    @start()
    def begin(self):
        self.remember("Project started", scope="/project", importance=0.9)
        memories = self.recall("project", limit=5, depth="deep")
        facts    = self.extract_memories("Long raw text ...")
```

---

## Event System: 80+ Event Types

All events inherit from `BaseEvent` with `timestamp` and `type` fields.

### Registration Pattern
```python
from crewai.utilities.events import BaseEventListener, crewai_event_bus
from crewai.utilities.events.crew_events import CrewKickoffStartedEvent

class MyListener(BaseEventListener):
    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(CrewKickoffStartedEvent)
        def on_start(source, event):
            print(f"Crew started at {event.timestamp}")

listener = MyListener()   # MUST instantiate -- prevents garbage collection

# Temporary handlers for tests
with crewai_event_bus.scoped_handlers():
    pass
```

### Crew Events (10)
| Event | Key Fields |
|-------|-----------|
| `CrewKickoffStartedEvent` | inputs |
| `CrewKickoffCompletedEvent` | output, token_usage |
| `CrewKickoffFailedEvent` | error |
| `CrewTestStartedEvent` | n_iterations, model |
| `CrewTestCompletedEvent` | results |
| `CrewTestFailedEvent` | error |
| `CrewTestResultEvent` | scores |
| `CrewTrainStartedEvent` | n_iterations, filename |
| `CrewTrainCompletedEvent` | -- |
| `CrewTrainFailedEvent` | error |

### Agent Events (9)
| Event | Key Fields |
|-------|-----------|
| `AgentExecutionStartedEvent` | agent_role, task_description |
| `AgentExecutionCompletedEvent` | agent_role, output |
| `AgentExecutionErrorEvent` | agent_role, error |
| `LiteAgentExecutionStartedEvent` | agent_info, tools, messages |
| `LiteAgentExecutionCompletedEvent` | agent_info, output |
| `LiteAgentExecutionErrorEvent` | agent_info, error |
| `AgentEvaluationStartedEvent` | -- |
| `AgentEvaluationCompletedEvent` | score |
| `AgentEvaluationFailedEvent` | error |

### Task Events (4)
| Event | Key Fields |
|-------|-----------|
| `TaskStartedEvent` | task_name, description |
| `TaskCompletedEvent` | task_name, output |
| `TaskFailedEvent` | task_name, error |
| `TaskEvaluationEvent` | task_name, score, feedback |

### Tool Events (6)
| Event | Key Fields |
|-------|-----------|
| `ToolUsageStartedEvent` | tool_name, input |
| `ToolUsageFinishedEvent` | tool_name, output, duration_ms |
| `ToolUsageErrorEvent` | tool_name, error |
| `ToolValidateInputErrorEvent` | tool_name, validation_error |
| `ToolExecutionErrorEvent` | tool_name, error |
| `ToolSelectionErrorEvent` | available_tools, error |

### LLM Events (5)
| Event | Key Fields |
|-------|-----------|
| `LLMCallStartedEvent` | model, messages, temperature |
| `LLMCallCompletedEvent` | model, response, token_usage |
| `LLMCallFailedEvent` | model, error |
| `LLMStreamChunkEvent` | chunk_content |
| `LLMThinkingChunkEvent` | thinking_content |

### Flow Events (9)
| Event | Key Fields |
|-------|-----------|
| `FlowCreatedEvent` | flow_name |
| `FlowStartedEvent` | flow_name, inputs |
| `FlowFinishedEvent` | flow_name, output |
| `FlowPausedEvent` | feedback_message, possible_outcomes |
| `FlowPlotEvent` | output_path |
| `MethodExecutionStartedEvent` | method_name |
| `MethodExecutionFinishedEvent` | method_name, output |
| `MethodExecutionFailedEvent` | method_name, error |
| `MethodExecutionPausedEvent` | method_name, pause_reason |

### Human-in-Loop Events (4)
| Event | Key Fields |
|-------|-----------|
| `FlowInputRequestedEvent` | question, metadata |
| `FlowInputReceivedEvent` | response (null = timed out) |
| `HumanFeedbackRequestedEvent` | message, emit_options |
| `HumanFeedbackReceivedEvent` | outcome, feedback |

### Memory Events (9)
| Event | Key Fields |
|-------|-----------|
| `MemoryQueryStartedEvent` | query, limit, score_threshold |
| `MemoryQueryCompletedEvent` | results_count, duration_ms |
| `MemoryQueryFailedEvent` | error |
| `MemorySaveStartedEvent` | content_preview, scope |
| `MemorySaveCompletedEvent` | record_id, scope, duration_ms |
| `MemorySaveFailedEvent` | error |
| `MemoryRetrievalStartedEvent` | -- |
| `MemoryRetrievalCompletedEvent` | records_count |
| `MemoryRetrievalFailedEvent` | error |

### Knowledge Events (6)
| Event | Key Fields |
|-------|-----------|
| `KnowledgeRetrievalStartedEvent` | query |
| `KnowledgeRetrievalCompletedEvent` | results_count |
| `KnowledgeQueryStartedEvent` | query |
| `KnowledgeQueryCompletedEvent` | -- |
| `KnowledgeQueryFailedEvent` | error |
| `KnowledgeSearchQueryFailedEvent` | error |

### MCP Events (7)
| Event | Key Fields |
|-------|-----------|
| `MCPConnectionStartedEvent` | server_name, url, transport_type, timeout, reconnecting |
| `MCPConnectionCompletedEvent` | duration_ms |
| `MCPConnectionFailedEvent` | error_type (timeout/authentication/network) |
| `MCPToolExecutionStartedEvent` | tool_name, server_name |
| `MCPToolExecutionCompletedEvent` | tool_name, duration_ms |
| `MCPToolExecutionFailedEvent` | tool_name, error |
| `MCPConfigFetchFailedEvent` | server_name, error |

### LLM Guardrail Events (3)
| Event | Key Fields |
|-------|-----------|
| `LLMGuardrailStartedEvent` | retry_count |
| `LLMGuardrailCompletedEvent` | -- |
| `LLMGuardrailFailedEvent` | error |

### Reasoning and Observation Events (9)
| Event | Key Fields |
|-------|-----------|
| `AgentReasoningStartedEvent` | -- |
| `AgentReasoningCompletedEvent` | plan |
| `AgentReasoningFailedEvent` | error |
| `StepObservationStartedEvent` | -- |
| `StepObservationCompletedEvent` | observation |
| `StepObservationFailedEvent` | error |
| `PlanRefinementEvent` | refined_plan |
| `PlanReplanTriggeredEvent` | reason |
| `GoalAchievedEarlyEvent` | -- |

### A2A Events (30+)
| Category | Events |
|----------|--------|
| Delegation | `A2ADelegationStartedEvent`, `A2ADelegationCompletedEvent`, `A2AParallelDelegationStartedEvent`, `A2AParallelDelegationCompletedEvent` |
| Conversation | `A2AConversationStartedEvent`, `A2AMessageSentEvent`, `A2AResponseReceivedEvent`, `A2AConversationCompletedEvent` |
| Streaming | `A2AStreamingStartedEvent`, `A2AStreamingChunkEvent` |
| Polling/Push | `A2APollingStartedEvent`, `A2APollingStatusEvent`, `A2APushNotificationRegisteredEvent`, `A2APushNotificationReceivedEvent`, `A2APushNotificationSentEvent`, `A2APushNotificationTimeoutEvent` |
| Connection | `A2AAgentCardFetchedEvent`, `A2AAuthenticationFailedEvent`, `A2AConnectionErrorEvent`, `A2ATransportNegotiatedEvent`, `A2AContentTypeNegotiatedEvent` |
| Artifacts | `A2AArtifactReceivedEvent` |
| Server Tasks | `A2AServerTaskStartedEvent`, `A2AServerTaskCompletedEvent`, `A2AServerTaskCanceledEvent`, `A2AServerTaskFailedEvent` |
| Context Lifecycle | `A2AContextCreatedEvent`, `A2AContextExpiredEvent`, `A2AContextIdleEvent`, `A2AContextCompletedEvent`, `A2AContextPrunedEvent` |

---

## CLI: Complete Reference (v0.140.0+)

| Command | Flags | Purpose |
|---------|-------|---------|
| `crewai create crew NAME` | -- | Scaffold crew project |
| `crewai create flow NAME` | -- | Scaffold flow project |
| `crewai run` | -- | Auto-detect crew/flow from pyproject.toml |
| `crewai chat` | -- | Interactive REPL (requires `chat_llm`) |
| `crewai test` | `-n` iterations (default 3), `-m` model (default gpt-4o-mini) | Evaluate performance |
| `crewai train` | `-n` iterations (default 5), `-f` filename (default trained_agents_data.pkl) | Iterative improvement |
| `crewai replay` | `-t TASK_ID` | Resume from task |
| `crewai log-tasks-outputs` | -- | View recent kickoff outputs |
| `crewai reset-memories` | `-l -s -e -k -kn -akn -a` | Clear memory stores |
| `crewai memory` | `--storage-path PATH` | Terminal TUI memory browser |
| `crewai traces enable/disable/status` | -- | Manage execution traces |
| `crewai version` | `--tools` | Show versions |
| `crewai config list/set/reset` | `KEY VALUE` | Settings in ~/.config/crewai/settings.json |
| `crewai flow plot` | -- | Interactive HTML flow visualization |
| `crewai login` | -- | OAuth2 device flow for AMP |
| `crewai deploy create/push/status/logs/list/remove` | -- | AMP deployment lifecycle |
| `crewai org list/current/switch` | `ORG_ID` | Organization management |

Config keys: `enterprise_base_url`, `oauth2_provider`, `oauth2_audience`, `oauth2_client_id`, `oauth2_domain`.
Auth note (v0.140.0+): Google login / accounts created after July 3, 2025 require updated library.

---

## Enterprise Tier: CrewAI AMP Cloud (Updated)

| Tier | Price | Features |
|------|-------|----------|
| Starter | $99/month | Auto-scaling, basic monitoring, standard LLMs |
| Pro | Custom | Advanced security, custom LLM integrations |
| Enterprise | $120,000/year | Full SLA, SSO/SAML, audit logs, dedicated infra, on-premises option |

Enterprise-only: SAML/SSO, audit logging, dedicated agent pools, on-premises deployment, OAuth2 org management via `crewai org`.

---

## Updated CEX Comparison (v2.0)

| Dimension | CrewAI | CEX |
|-----------|--------|-----|
| Composition unit | Agent (role + goal + backstory) | Nucleus (domain + sin lens + 13 builder ISOs) |
| Orchestration | Crew (sequential/hierarchical) + Flow (event-driven) | N07 + mission_runner (wave-based, session-tagged PIDs) |
| State management | FlowState: dict OR Pydantic BaseModel | Git + `.cex/runtime/` (file-based, git-backed) |
| Memory system | Unified Memory (LanceDB, scope inference, composite scoring) | 4-type memory (correction/preference/convention/context) |
| Knowledge | RAG (ChromaDB/custom) + Knowledge sources per agent | Knowledge Cards + TF-IDF retriever (2184 docs, 12K vocab) |
| Quality control | `crewai test` + LLM guardrails + HITL | 3-layer scoring (structural 30% + rubric 30% + semantic 40%) |
| Configuration | YAML (agents.yaml + tasks.yaml) + CrewBase | ISOs (13 per builder kind) + kinds_meta.json |
| Event system | 80+ typed events via crewai_event_bus | Signal writer (nucleus-level completion signals) |
| Deployment | AMP Cloud CLI deploy | boot/*.ps1 (local), dispatch.sh (session-aware) |
| Multi-agent protocol | A2A (30+ events, agent cards, push notifications) | Handoff files (n0X_task.md) + 8F pipeline |

---

## Sources (v2.0)

- [CrewAI Memory (Unified, v0.100+)](https://docs.crewai.com/concepts/memory)
- [CrewAI Events (80+ types)](https://docs.crewai.com/concepts/event-listener)
- [CrewAI Flows (Decorators + State)](https://docs.crewai.com/concepts/flows)
- [CrewAI Agents (Full Parameters)](https://docs.crewai.com/concepts/agents)
- [CrewAI Tasks (Full Parameters)](https://docs.crewai.com/concepts/tasks)
- [CrewAI Crews (Methods + Config)](https://docs.crewai.com/concepts/crews)
- [CrewAI CLI (v0.140.0+)](https://docs.crewai.com/concepts/cli)