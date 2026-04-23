---
id: atom_08_crewai
kind: knowledge_card
pillar: P01
quality: 8.8
title: "CrewAI Deep Vocabulary Scrape"
tags: [crewai, agent, framework-atlas, v0.100+, lancedb, flows, events, a2a]
date: 2026-04-13
version: 3.0
related:
  - atom_03_openai_agents_sdk
  - p01_kc_pydantic_patterns
  - atom_07_llamaindex
  - atom_06_langchain_langgraph
  - SPEC_05_skills_runtime
  - n06_output_brand_config
  - p01_kc_agent
  - atom_09_autogen_ag2
  - p01_kc_crewai_patterns
  - atom_10_haystack_vercel
---

# CrewAI: Implementation-Level Reference (v0.100+)

## Introduction

CrewAI is an open-source framework for autonomous, collaborative AI agents. This document is a deep implementation-level reference covering agents, tasks, crews, flows, unified memory (LanceDB), knowledge sources, 80+ event types, YAML configuration patterns, enterprise deployment, and competitive context. Sourced from official CrewAI docs (April 2026).

---

## Agents

Full parameter reference:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `role` | `str` | Required | Function and expertise within the crew |
| `goal` | `str` | Required | Individual objective guiding decision-making |
| `backstory` | `str` | Required | Context and personality shaping behavior |
| `llm` | `Union[str, LLM, Any]` | `"gpt-4"` | Language model powering the agent |
| `tools` | `List[BaseTool]` | `[]` | Capabilities available for task execution |
| `function_calling_llm` | `Optional[Any]` | None | Separate LLM for tool calling |
| `max_iter` | `int` | 20 | Max iterations before forced final answer |
| `max_rpm` | `Optional[int]` | None | Rate limit for API calls |
| `max_execution_time` | `Optional[int]` | None | Timeout in seconds |
| `verbose` | `bool` | False | Enable detailed execution logs |
| `allow_delegation` | `bool` | False | Allow task delegation to other agents |
| `cache` | `bool` | True | Enable caching for tool usage |
| `max_retry_limit` | `int` | 2 | Retries on error |
| `respect_context_window` | `bool` | True | Auto-summarize when token limit exceeded |
| `use_system_prompt` | `bool` | True | System message support (disable for o1 models) |
| `reasoning` | `bool` | False | Reflect and plan before executing |
| `max_reasoning_attempts` | `Optional[int]` | None | Planning iteration limit (None = unlimited) |
| `multimodal` | `bool` | False | Support text + visual content |
| `inject_date` | `bool` | False | Auto-inject current date into tasks |
| `date_format` | `str` | `"%Y-%m-%d"` | Date format string |
| `embedder` | `Optional[Dict]` | None | Custom embedding configuration |
| `knowledge_sources` | `Optional[List]` | None | Domain-specific knowledge bases |
| `step_callback` | `Optional[Any]` | None | Called after each agent step |
| `system_template` | `Optional[str]` | None | Custom system prompt template |
| `prompt_template` | `Optional[str]` | None | Custom input format template |
| `response_template` | `Optional[str]` | None | Custom output format template |

Note: `allow_code_execution` and `code_execution_mode` are DEPRECATED. Use E2B or Modal instead.

**YAML config (config/agents.yaml):**

```yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    A seasoned researcher with a knack for uncovering
    the latest developments in {topic}.
```

**Python + YAML integration:**

```python
from crewai import Agent
from crewai.project import CrewBase, agent

@CrewBase
class MyCrew:
    agents_config = "config/agents.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config["researcher"], tools=[SerperDevTool()])
```

**Direct kickoff with structured output:**

```python
from pydantic import BaseModel

class Findings(BaseModel):
    main_points: list[str]
    key_technologies: list[str]

result = researcher.kickoff("Summarize latest AI developments", response_format=Findings)
print(result.pydantic.main_points)
```

---

## Tasks

Full parameter reference:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `description` | `str` | Required | Statement of work |
| `expected_output` | `str` | Required | Specification for completion |
| `name` | `Optional[str]` | None | Task identifier |
| `agent` | `Optional[BaseAgent]` | None | Responsible agent |
| `tools` | `List[BaseTool]` | None | Overrides agent tools for this task |
| `context` | `Optional[List[Task]]` | None | Tasks whose outputs become context |
| `async_execution` | `Optional[bool]` | False | Non-blocking execution |
| `human_input` | `Optional[bool]` | False | Human review of final answer |
| `markdown` | `Optional[bool]` | False | Return output formatted as Markdown |
| `output_file` | `Optional[str]` | None | File path for output |
| `create_directory` | `Optional[bool]` | True | Auto-create output directory |
| `output_json` | `Optional[Type[BaseModel]]` | None | Pydantic model for JSON output |
| `output_pydantic` | `Optional[Type[BaseModel]]` | None | Pydantic model for structured output |
| `callback` | `Optional[Any]` | None | Function executed after completion |
| `guardrail` | `Optional[Callable]` | None | Single validation function |
| `guardrails` | `Optional[List[Callable]]` | None | Multiple validators (takes precedence over `guardrail`) |
| `guardrail_max_retries` | `Optional[int]` | 3 | Max retries on guardrail failure |

**TaskOutput attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `description` | `str` | Task description |
| `summary` | `Optional[str]` | Auto-generated from first 10 words |
| `raw` | `str` | Default string output |
| `pydantic` | `Optional[BaseModel]` | Structured model output |
| `json_dict` | `Optional[Dict]` | Dictionary from JSON output |
| `agent` | `str` | Executing agent identifier |
| `output_format` | `OutputFormat` | RAW, JSON, or Pydantic |
| `messages` | `list[LLMMessage]` | Messages from last execution |

**Guardrail function signature:**

```python
from typing import Tuple, Any
from crewai import TaskOutput

def validate_content(result: TaskOutput) -> Tuple[bool, Any]:
    if len(result.raw.split()) > 200:
        return (False, "Content exceeds 200 words")
    return (True, result.raw.strip())

task = Task(
    description="Write content",
    expected_output="Valid output under 200 words",
    agent=agent,
    guardrail=validate_content,
    guardrail_max_retries=3
)
```

**LLM-based guardrail (string):**

```python
task = Task(
    description="Write a blog post",
    expected_output="Quality blog post",
    agent=blog_agent,
    guardrail="Must be under 200 words and contain no technical jargon"
)
```

**Multiple guardrails (execute sequentially):**

```python
task = Task(
    guardrails=[
        validate_word_count,
        validate_no_profanity,
        "Must be professionally written"
    ],
    guardrail_max_retries=3
)
```

**YAML config (config/tasks.yaml):**

```yaml
research_task:
  description: >
    Research {topic} thoroughly and gather key findings.
  expected_output: >
    Structured report with sources and key insights.
  agent: researcher
  markdown: true
  output_file: reports/research.md
  context: [prior_task]
  async_execution: false
  human_input: false
```

---

## Crews

Core parameters:

- `agents`: List of participating agents
- `tasks`: List of assigned tasks
- `process`: Process.sequential (default) or Process.hierarchical
- `verbose`: bool (default False)
- `manager_llm`: LLM for hierarchical manager (required in hierarchical mode)
- `manager_agent`: Custom manager agent instance
- `function_calling_llm`: Tool-calling LLM across all agents
- `memory`: True, False, or Memory instance
- `cache`: bool (default True)
- `embedder`: Vector embedding configuration
- `max_rpm`: Rate limit per minute
- `planning`: Activate planning capability (AgentPlanner)
- `planning_llm`: Dedicated LLM for planning
- `output_log_file`: Log destination (.txt or .json)
- `step_callback`: Called after each agent step
- `task_callback`: Called after each task completion
- `stream`: bool for real-time output
- `knowledge_sources`: Crew-level knowledge for all agents

**Kickoff variants:**

| Method | Type | Purpose |
|--------|------|---------|
| `kickoff()` | Sync | Standard execution |
| `kickoff_for_each(inputs)` | Sync | Process collection sequentially |
| `akickoff()` | Native async | True async/await execution |
| `akickoff_for_each(inputs)` | Native async | Async collection processing |
| `kickoff_async()` | Thread-based | Async wrapper around sync |
| `kickoff_for_each_async()` | Thread-based | Thread-based collection processing |

**CrewOutput attributes:** raw, pydantic, json_dict, tasks_output (list of TaskOutput), token_usage.

**Hooks:**

```python
from crewai.project import CrewBase, crew, before_kickoff, after_kickoff

@CrewBase
class MyCrew:
    @before_kickoff
    def setup(self, inputs): return inputs

    @after_kickoff
    def teardown(self, result): return result

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)
```

---

## Flows: Event-Driven Orchestration

Flows are Python classes that orchestrate stateful, branching multi-step pipelines.

### Decorator Reference

| Decorator | Purpose |
|-----------|---------|
| `@start()` | Mark entry point(s); all fire in parallel at kickoff |
| `@listen(method)` | Fire when listened method completes |
| `@router(method)` | Conditional branch based on return label string |
| `@persist` | Auto-persist state via SQLiteFlowPersistence (class or method level) |
| `@human_feedback(...)` | Pause for human approval (v1.8.0+) |

**@start() patterns:**

```python
@start()                        # unconditional
def init(self): ...

@start("prior_method")          # fires after prior_method
def init_after(self): ...
```

**@router() with labeled routes:**

```python
@router(start_method)
def route_logic(self):
    if self.state.quality > 0.8:
        return "success"
    return "retry"

@listen("success")
def handle_success(self): ...

@listen("retry")
def handle_retry(self): ...
```

**@human_feedback (v1.8.0+):**

```python
@human_feedback(
    message="Approve the generated content?",
    emit=["approved", "rejected", "needs_revision"],
    llm="gpt-4o-mini",
    default_outcome="needs_revision"
)
def review_step(self): ...
# Returns: HumanFeedbackResult with .feedback and .output
# Access: self.last_human_feedback, self.human_feedback_history
```

**@persist (SQLiteFlowPersistence default):**

```python
@persist  # class-level
class MyFlow(Flow[MyState]): ...

@persist  # method-level
@start()
def initialize(self): ...
```

### Control Flow Functions

```python
from crewai.flow.flow import or_, and_

@listen(or_(method_a, method_b))    # fires when ANY completes
def on_either(self, result): ...

@listen(and_(method_a, method_b))   # fires only when ALL complete
def on_both(self): ...
```

### State Management

**Structured (Pydantic):**

```python
from pydantic import BaseModel

class MyState(BaseModel):
    counter: int = 0
    message: str = ""

class MyFlow(Flow[MyState]):
    @start()
    def init(self):
        self.state.counter += 1
```

**Unstructured (dict):** `self.state["key"] = "value"` -- auto-UUID at `self.state["id"]`.

### Execution

```python
result = flow.kickoff()
result = await flow.kickoff_async(inputs={...})
flow.plot("diagram_name")  # generates diagram_name.html
```

### Streaming

```python
class StreamingFlow(Flow):
    stream = True

streaming = flow.kickoff()
for chunk in streaming:
    print(chunk.content, end="", flush=True)
result = streaming.result
```

### Memory Integration in Flows

```python
class ResearchFlow(Flow):
    @start()
    def gather(self):
        self.remember(findings, scope="/research/databases")

    @listen(gather)
    def write(self, findings):
        past = self.recall("benchmarks", limit=10, depth="shallow")
        facts = self.extract_memories(raw_text)
```

---

## Unified Memory System (LanceDB)

CrewAI v0.100+ uses a single Memory class backed by LanceDB, replacing separate short-term/long-term/entity types.

### Core API

| Method | Signature | Purpose |
|--------|-----------|---------|
| `remember` | (content, scope, source, private, categories, importance) | Store memory |
| `recall` | (query, limit=5, scope, depth="deep", source) | Retrieve by composite score |
| `remember_many` | (items) | Non-blocking batch save (background thread) |
| `extract_memories` | (content) | Break raw text into atomic facts |
| `forget` | (scope) | Delete memories in scope subtree |
| `drain_writes` | () | Wait for pending background saves |
| `close` | () | Drain writes + shutdown pool |
| `scope` | (path) | Create MemoryScope restricted to branch |
| `slice` | (scopes, read_only=True) | MemorySlice across multiple branches |
| `tree` | (path, max_depth) | Display hierarchical scope structure |
| `info` | (scope) | ScopeInfo with record count + metadata |
| `list_scopes` | (scope) | List immediate child scopes |
| `list_categories` | () | All category names with counts |
| `list_records` | (scope, limit) | Records in scope (newest first) |
| `reset` | (scope=None) | Clear all or specific subtree |

### Full Init Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `llm` | "gpt-4o-mini" | LLM for memory analysis |
| `storage` | "lancedb" | Backend (path, "lancedb", or StorageBackend) |
| `embedder` | None (OpenAI) | Config dict, callable, or None |
| `recency_weight` | 0.3 | Recency component of composite score |
| `semantic_weight` | 0.5 | Semantic similarity component |
| `importance_weight` | 0.2 | Importance component |
| `recency_half_life_days` | 30 | Days for exponential decay to 0.5 |
| `consolidation_threshold` | 0.85 | Similarity triggering consolidation |
| `consolidation_limit` | 5 | Max records compared during consolidation |
| `default_importance` | 0.5 | Importance when LLM skipped |
| `batch_dedup_threshold` | 0.98 | Cosine similarity for intra-batch dedup |
| `confidence_threshold_high` | 0.8 | Confidence for direct return |
| `confidence_threshold_low` | 0.5 | Confidence triggering deeper exploration |
| `complex_query_threshold` | 0.7 | Threshold for complex query exploration |
| `exploration_budget` | 1 | LLM exploration rounds in deep recall |
| `query_analysis_threshold` | 200 | Char length below which LLM analysis skipped |

### Composite Scoring Formula

score = semantic_weight * (1 / (1 + distance)) + recency_weight * (0.5 ^ (age_days / half_life_days)) + importance_weight * importance

### Recall Depths

- depth="shallow" -- Direct vector search, ~200ms, no LLM call
- depth="deep" (default) -- Multi-step: query analysis -> scope selection -> parallel search -> confidence routing -> optional recursion

Short queries (< 200 chars) skip LLM analysis even in deep mode.

### Embedding Providers

| Provider | Key | Default Model |
|----------|-----|---------------|
| OpenAI (default) | openai | text-embedding-3-small |
| Ollama | ollama | mxbai-embed-large |
| Azure OpenAI | azure | text-embedding-ada-002 |
| Google AI | google-generativeai | gemini-embedding-001 |
| Google Vertex | google-vertex | gemini-embedding-001 |
| Cohere | cohere | embed-english-v3.0 |
| VoyageAI | voyageai | voyage-3 |
| AWS Bedrock | amazon-bedrock | amazon.titan-embed-text-v1 |
| Hugging Face | huggingface | all-MiniLM-L6-v2 |
| Jina | jina | jina-embeddings-v2-base-en |
| IBM WatsonX | watsonx | ibm/slate-30m-english-rtrvr |
| Custom | custom | callable: list[str] -> list[list[float]] |

### Hierarchical Scopes

Filesystem-like tree: /, /company/engineering, /project/alpha/decisions, /agent/researcher.
Best practice: start flat, let LLM infer structure, use /{entity_type}/{identifier} pattern, keep depth <= 3.

### Consolidation Logic

On save, similar records (cosine >= 0.85) trigger LLM decision: keep, update, delete, or insert_new.
Intra-batch dedup (remember_many): items with similarity >= 0.98 silently dropped.

### Integration Patterns

```python
crew = Crew(agents=[...], tasks=[...], memory=True)

researcher = Agent(
    role="Researcher",
    memory=memory.scope("/agent/researcher")
)
```

### Storage and TUI

Default path: ./.crewai/memory (override via CREWAI_STORAGE_DIR env var or storage param).

```bash
crewai memory                               # open TUI browser
crewai memory --storage-path ./my_memory
```

---

## Knowledge Sources

RAG integration with multiple source adapters. Default embedder: OpenAI text-embedding-3-small (even when using other LLMs).

Storage locations: macOS ~/Library/Application Support/CrewAI/, Linux ~/.local/share/CrewAI/, Windows %APPDATA%\Local\CrewAI\.

### Source Types

| Class | Input |
|-------|-------|
| StringKnowledgeSource | Raw string content |
| TextFileKnowledgeSource | .txt files |
| PDFKnowledgeSource | PDF documents |
| CSVKnowledgeSource | CSV files |
| ExcelKnowledgeSource | .xlsx files |
| JSONKnowledgeSource | JSON files |
| CrewDoclingSource | Web content via Docling library |

### KnowledgeConfig Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| results_limit | 3 | Relevant documents returned |
| score_threshold | 0.35 | Minimum relevance score |
| chunk_size | varies | Text division granularity |
| chunk_overlap | varies | Context preservation between chunks |

---

## Event System: 80+ Event Types

All events inherit from BaseEvent (fields: timestamp, type). Import via crewai.utilities.events.

### Crew Events (9)

| Event | Key Fields |
|-------|-----------|
| CrewKickoffStartedEvent | crew_id, crew_name |
| CrewKickoffCompletedEvent | crew_id, output |
| CrewKickoffFailedEvent | crew_id, error |
| CrewTestStartedEvent | crew_id, n_iterations |
| CrewTestCompletedEvent | crew_id, results |
| CrewTestFailedEvent | crew_id, error |
| CrewTrainStartedEvent | crew_id, n_iterations |
| CrewTrainCompletedEvent | crew_id |
| CrewTrainFailedEvent | crew_id, error |

### Agent Events (12)

| Event | Key Fields |
|-------|-----------|
| AgentExecutionStartedEvent | agent_role, task_id |
| AgentExecutionCompletedEvent | agent_role, output |
| AgentExecutionErrorEvent | agent_role, error |
| LiteAgentExecutionStartedEvent | agent_info, tools, messages |
| LiteAgentExecutionCompletedEvent | agent_info, output |
| LiteAgentExecutionErrorEvent | agent_info, error |
| AgentEvaluationStartedEvent | agent_id, role, task_id, iteration |
| AgentEvaluationCompletedEvent | metric_category, score |
| AgentEvaluationFailedEvent | error |
| AgentReasoningStartedEvent | agent_role, task_id, attempt |
| AgentReasoningCompletedEvent | plan, readiness_status |
| AgentReasoningFailedEvent | error |

### Task Events (4)

| Event | Key Fields |
|-------|-----------|
| TaskStartedEvent | task_id, task_name |
| TaskCompletedEvent | task_id, output |
| TaskFailedEvent | task_id, error |
| TaskEvaluationEvent | task_id, score |

### Tool Events (6)

| Event | Key Fields |
|-------|-----------|
| ToolUsageStartedEvent | tool_name, input |
| ToolUsageFinishedEvent | tool_name, output, duration |
| ToolUsageErrorEvent | tool_name, error |
| ToolValidateInputErrorEvent | tool_name, error |
| ToolExecutionErrorEvent | tool_name, error |
| ToolSelectionErrorEvent | error |

### MCP Events (7)

| Event | Key Fields |
|-------|-----------|
| MCPConnectionStartedEvent | server_name, url, transport_type, timeout, reconnecting |
| MCPConnectionCompletedEvent | duration, reconnecting |
| MCPConnectionFailedEvent | error, error_type (timeout/authentication/network) |
| MCPToolExecutionStartedEvent | server_name, tool_name, arguments |
| MCPToolExecutionCompletedEvent | result, duration |
| MCPToolExecutionFailedEvent | error, error_type |
| MCPConfigFetchFailedEvent | error_type (not_connected/api_error/connection_failed) |

### Knowledge Events (6)

| Event | Key Fields |
|-------|-----------|
| KnowledgeRetrievalStartedEvent | query |
| KnowledgeRetrievalCompletedEvent | results, duration |
| KnowledgeQueryStartedEvent | query |
| KnowledgeQueryCompletedEvent | results |
| KnowledgeQueryFailedEvent | error |
| KnowledgeSearchQueryFailedEvent | error |

### LLM Guardrail Events (3)

| Event | Key Fields |
|-------|-----------|
| LLMGuardrailStartedEvent | validation_info, retry_count |
| LLMGuardrailCompletedEvent | success, results |
| LLMGuardrailFailedEvent | error |

### Flow Events (10)

| Event | Key Fields |
|-------|-----------|
| FlowCreatedEvent | flow_id, flow_name |
| FlowStartedEvent | flow_id |
| FlowFinishedEvent | flow_id, result |
| FlowPausedEvent | flow_id, method_name, outcomes |
| FlowPlotEvent | flow_id, filename |
| MethodExecutionStartedEvent | flow_id, method_name |
| MethodExecutionFinishedEvent | flow_id, method_name, output |
| MethodExecutionFailedEvent | flow_id, method_name, error |
| MethodExecutionPausedEvent | feedback_message, routing_outcomes |
| FlowInputRequestedEvent | question, metadata |

### Human Feedback Events (4)

| Event | Key Fields |
|-------|-----------|
| FlowInputReceivedEvent | user_response, response_metadata |
| HumanFeedbackRequestedEvent | method_output, feedback_message |
| HumanFeedbackReceivedEvent | raw_feedback, outcome |

### LLM Events (5)

| Event | Key Fields |
|-------|-----------|
| LLMCallStartedEvent | model, messages |
| LLMCallCompletedEvent | model, response, tokens |
| LLMCallFailedEvent | model, error |
| LLMStreamChunkEvent | chunk, model |
| LLMThinkingChunkEvent | chunk_text, response_id |

### Memory Events (9)

| Event | Key Fields |
|-------|-----------|
| MemoryQueryStartedEvent | query, limit, score_threshold |
| MemoryQueryCompletedEvent | results, query_time_ms |
| MemoryQueryFailedEvent | query, error |
| MemorySaveStartedEvent | value, metadata, agent_role |
| MemorySaveCompletedEvent | value, save_time_ms |
| MemorySaveFailedEvent | value, error |
| MemoryRetrievalStartedEvent | task_id |
| MemoryRetrievalCompletedEvent | task_id, memory_content, retrieval_time_ms |
| MemoryRetrievalFailedEvent | error |

### Observation Events (6)

| Event | Key Fields |
|-------|-----------|
| StepObservationStartedEvent | agent_role, step_number, description |
| StepObservationCompletedEvent | plan_valid, refinement_suggestions |
| StepObservationFailedEvent | error |
| PlanRefinementEvent | refinement_count, details |
| PlanReplanTriggeredEvent | replan_reason, replan_count |
| GoalAchievedEarlyEvent | remaining_steps |

### A2A Events (29)

**Delegation:** A2ADelegationStartedEvent (endpoint, task_description, agent_id, context_id, turn_data), A2ADelegationCompletedEvent (status, result, error), A2AParallelDelegationStartedEvent (endpoint_list), A2AParallelDelegationCompletedEvent (success_count, failure_count).

**Conversation:** A2AConversationStartedEvent (agent_id, endpoint, context_id), A2AMessageSentEvent (message_content, turn_number), A2AResponseReceivedEvent (response_content, status, final), A2AConversationCompletedEvent (final_status, result, total_turns), A2AStreamingStartedEvent (task_id, context_id, endpoint), A2AStreamingChunkEvent (chunk_text, index, final).

**Polling & Notifications:** A2APollingStartedEvent (polling_interval), A2APollingStatusEvent (task_state, elapsed_time, poll_count), A2APushNotificationRegisteredEvent (callback_url), A2APushNotificationReceivedEvent (state), A2APushNotificationSentEvent (delivery_status, error), A2APushNotificationTimeoutEvent (timeout_duration).

**Connection & Auth:** A2AAgentCardFetchedEvent (agent_card_metadata, cached, fetch_time), A2AAuthenticationFailedEvent (auth_type, http_status), A2AConnectionErrorEvent (error_type), A2ATransportNegotiatedEvent (protocol_details), A2AContentTypeNegotiatedEvent (input_modes, output_modes).

**Artifacts & Tasks:** A2AArtifactReceivedEvent (artifact_id, name, mime_type, size), A2AServerTaskStartedEvent (task_id, context_id), A2AServerTaskCompletedEvent (result), A2AServerTaskCanceledEvent (task_id), A2AServerTaskFailedEvent (error).

**Context Lifecycle:** A2AContextCreatedEvent (context_id, timestamp), A2AContextExpiredEvent (age, task_count), A2AContextIdleEvent (idle_duration), A2AContextCompletedEvent (total_tasks, duration), A2AContextPrunedEvent (task_count, age).

**Event listener registration:**

```python
from crewai.utilities.events import crewai_event_bus
from crewai.utilities.events.base_event_listener import BaseEventListener

class MyListener(BaseEventListener):
    def on_crew_kickoff_started(self, source, event): ...
    def on_tool_usage_finished(self, source, event): ...

crewai_event_bus.register(MyListener())
```

---

## YAML Configuration Pattern (Full Project Structure)

```
my_project/
  src/my_project/
    config/
      agents.yaml
      tasks.yaml
    crew.py
    main.py
  pyproject.toml
```

**agents.yaml + tasks.yaml + crew.py + variable injection:**

```python
@CrewBase
class LatestAiDevelopmentCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config["researcher"], tools=[SerperDevTool()])

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential)

# Variable injection:
crew.kickoff(inputs={"topic": "AI Agents"})
```

---

## Enterprise Capabilities

### Pricing Tiers

| Tier | Price | Notes |
|------|-------|-------|
| Starter | $99/month | Auto-scaling, real-time monitoring |
| Enterprise | $120,000/year | SOC2, custom LLMs, multi-tenant isolation |

### CLI Reference

```bash
crewai create crew <name>       # scaffold crew project
crewai create flow <name>       # scaffold flow project
crewai run                      # run flow or crew (auto-detect)
crewai flow kickoff             # run flow explicitly
crewai flow plot                # generate HTML visualization
crewai test -n 5                # test 5 iterations (scores 1-10)
crewai train -n 5 -f train.pkl  # train with feedback
crewai replay -t <task_id>      # replay from specific task
crewai memory                   # open memory TUI browser
crewai install                  # install dependencies
crewai deploy                   # deploy to AMP Cloud
crewai login                    # authenticate with AMP Cloud
```

### LLM Providers (via LiteLLM)

OpenAI, Azure OpenAI, Anthropic, Google Gemini, Vertex AI, Ollama, Groq, Mistral, Cohere, Bedrock, any OpenAI-compatible endpoint.

```python
from crewai import LLM

llm = LLM(model="anthropic/claude-3-5-sonnet-20241022", temperature=0.7, max_tokens=4096)
```

---

## Technical Architecture

### Comparison: CrewAI vs CEX vs LangGraph

| Dimension | CrewAI | CEX | LangGraph |
|-----------|--------|-----|-----------|
| Composition unit | Agent (role+goal+backstory) | Nucleus (domain+sin+builder ISOs) | Node (stateful function) |
| Orchestration | Crew (sequential/hierarchical) | N07 + mission_runner (wave-based) | Graph (DAG-based) |
| State management | FlowState (Pydantic) | Git + .cex/runtime/ (file-based) | StateGraph (typed dict) |
| Memory | Unified Memory (LanceDB) | 4-type file-based memory | External (none built-in) |
| Knowledge | RAG (LanceDB + embedder) | Knowledge Cards + TF-IDF retriever | External (none built-in) |
| Quality control | crewai test (score 1-10) | 3-layer scoring (structural+rubric+semantic) | None built-in |
| Event system | 80+ typed events + A2A | File-based signals | Callbacks (basic) |
| Config pattern | YAML + @CrewBase decorator | 8F pipeline + builder ISOs | Python code only |
| Persistence | SQLiteFlowPersistence + LanceDB | Git + .cex/runtime/ | External |
| Open source | Yes (Apache 2.0) | Yes (internal) | Yes (MIT) |
| Cloud offering | AMP Cloud ($99/mo+) | N/A | LangSmith + LangGraph Cloud |

---

## Glossary

**A2A**: Agent-to-Agent protocol for cross-service delegation
**AgentPlanner**: Planning module activated by planning=True in Crew
**BaseEvent**: Base class for all CrewAI events (fields: timestamp, type)
**BaseTool**: Abstract class for tool creation
**CrewBase**: Decorator base class for YAML-configured crews
**CrewOutput**: Execution result (raw, pydantic, json_dict, tasks_output, token_usage)
**FlowState**: Pydantic state object managed by Flow
**HumanFeedbackResult**: Result of @human_feedback with .feedback and .output
**LanceDB**: Vector database powering CrewAI unified memory
**MemoryScope**: Subtree-restricted view of unified memory
**MemorySlice**: Multi-branch read-across memory view
**Process**: Enum -- Process.sequential or Process.hierarchical
**SQLiteFlowPersistence**: Default state persistence for @persist decorator
**StorageBackend**: Protocol for custom memory storage backends
**TaskOutput**: Task execution result (raw, pydantic, json_dict, messages, output_format)
**and_()**: Flow combinator -- fires when ALL listened methods complete
**or_()**: Flow combinator -- fires when ANY listened method completes
**@human_feedback**: Flow decorator for pausing and collecting human approval
**@listen()**: Flow decorator -- fires when listened method completes
**@persist**: Flow decorator for automatic state persistence across restarts
**@router()**: Flow decorator for conditional branching based on return label
**@start()**: Flow decorator marking entry point
**@tool**: Decorator for function-based tool creation

---

## Sources

- [CrewAI Documentation -- Agents](https://docs.crewai.com/concepts/agents)
- [CrewAI Documentation -- Tasks](https://docs.crewai.com/concepts/tasks)
- [CrewAI Documentation -- Crews](https://docs.crewai.com/concepts/crews)
- [CrewAI Documentation -- Flows](https://docs.crewai.com/concepts/flows)
- [CrewAI Documentation -- Knowledge](https://docs.crewai.com/concepts/knowledge)
- [CrewAI Documentation -- Memory](https://docs.crewai.com/concepts/memory)
- [CrewAI Documentation -- Tools](https://docs.crewai.com/concepts/tools)
- [CrewAI Documentation -- Events](https://docs.crewai.com/concepts/event-listener)
- [CrewAI Documentation -- CLI](https://docs.crewai.com/concepts/cli)
- [CrewAI Documentation -- Testing](https://docs.crewai.com/concepts/testing)
- [CrewAI Documentation -- Planning](https://docs.crewai.com/concepts/planning)
- [CrewAI Documentation -- LLM Connections](https://docs.crewai.com/learn/llm-connections)
- [CrewAI GitHub Repository](https://github.com/crewAIInc/crewAI)
- [CrewAI Pricing](https://crewai.com/pricing)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_03_openai_agents_sdk]] | sibling | 0.33 |
| [[p01_kc_pydantic_patterns]] | sibling | 0.29 |
| [[atom_07_llamaindex]] | sibling | 0.27 |
| [[atom_06_langchain_langgraph]] | sibling | 0.26 |
| [[SPEC_05_skills_runtime]] | related | 0.26 |
| [[n06_output_brand_config]] | downstream | 0.25 |
| [[p01_kc_agent]] | sibling | 0.25 |
| [[atom_09_autogen_ag2]] | sibling | 0.24 |
| [[p01_kc_crewai_patterns]] | sibling | 0.24 |
| [[atom_10_haystack_vercel]] | sibling | 0.23 |
