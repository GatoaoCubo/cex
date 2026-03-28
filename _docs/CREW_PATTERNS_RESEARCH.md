# Crew Orchestration Patterns Research
**SHAKA Wave 6A** | 2026-03-28 | CEX Crew Runner Pre-Implementation

---

## 1. CrewAI

**Model**: Hierarchical container (Crew > Agent > Task).

### Composition
```python
researcher = Agent(role="Researcher", goal="...", backstory="...")
task = Task(description="...", expected_output="...", agent=researcher)
crew = Crew(agents=[researcher], tasks=[task], process=Process.sequential)
crew.kickoff()
```

### Data Flow: Agent A → Agent B
Sequential: automatic. Output of task N is injected as context into task N+1.
Non-sequential: explicit via `context=[task_a, task_b]` — task waits for all deps.
```python
write_task = Task(description="Write blog", agent=writer,
                  context=[research_task, ops_task])  # waits for both
```

### Structured Output
`output_pydantic=BlogModel` forces typed output between tasks — reliable chaining.

### Memory
Three tiers: short-term (in-run), long-term (cross-run via DB), entity (named things).
Shared across all agents in the Crew automatically.

### Hierarchical Mode
Manager agent (LLM-based) orchestrates: selects which agent handles each task,
validates outputs, re-delegates on failure. Overhead: extra LLM calls per task.

| Dimension | CrewAI |
|-----------|--------|
| Composition | Crew wraps Agents+Tasks; Process defines execution order |
| State | Task output auto-propagates; explicit `context=[]` for DAG deps |
| Dependency | Declared via task ordering or `context` param |
| Parallelism | `async_execution=True` on tasks + `context` to merge |
| Quality | Hierarchical manager validates; no built-in score gate |
| Fallback | Manager can re-delegate; sequential has no retry |
| Context | Shared Memory object; no per-agent budget control |

**Trade-off**: Simple pipelines are clean. Hierarchical adds LLM overhead per step.
`output_pydantic` is the key pattern for reliable inter-agent typed data.

---

## 2. DSPy

**Model**: Composable Python modules with declarative I/O signatures.

### Composition (Forward Pass)
```python
class Pipeline(dspy.Module):
    def __init__(self):
        self.step1 = dspy.ChainOfThought("question -> analysis")
        self.step2 = dspy.ReAct("analysis, tools -> answer", tools=[search])

    def forward(self, question):
        analysis = self.step1(question=question).analysis
        return self.step2(analysis=analysis)
```
State flows as Python variables — explicit, no magic. The forward pass is traced
at compile time for optimization.

### Signatures (I/O Contracts)
```python
class Classify(dspy.Signature):
    """Classify sentiment."""
    sentence: str = dspy.InputField()
    sentiment: Literal["pos","neg"] = dspy.OutputField()
    confidence: float = dspy.OutputField()
```
Signatures are the contract between modules. Change signature → type error at run time.

### Built-in Patterns
| Pattern | Use Case | Cost |
|---------|----------|------|
| `Predict` | Basic inference | 1x |
| `ChainOfThought` | Step-by-step reasoning | 1.5x tokens |
| `ProgramOfThought` | Code execution path | 2x + exec risk |
| `ReAct` | Tool-calling agent | variable (tools) |
| `MultiChainComparison` | Voting over N outputs | Nx |

### Optimizers
Auto-tune prompts/demos without manual engineering:
`BootstrapFewShot` → `COPRO` → `MIPROv2` (increasing compute, increasing quality).
Requires labeled training set (~20-50 examples).

| Dimension | DSPy |
|-----------|------|
| Composition | Python Module.forward() — full control flow |
| State | Explicit Python vars; no shared state object |
| Dependency | Implicit (call order in forward()) |
| Parallelism | Manual (asyncio); no built-in |
| Quality | Optimizers improve quality offline; no runtime gate |
| Fallback | Python try/except — framework-agnostic |
| Context | No budget control; track_usage=True for monitoring |

**Trade-off**: Maximum flexibility and optimizability. No runtime orchestration —
all control flow is plain Python. Best when you own the full pipeline in one module.

---

## 3. LangGraph

**Model**: Explicit DAG — StateGraph with typed state, nodes as functions, edges as routing.

### Core Pattern
```python
from langgraph.graph import StateGraph, MessagesState, START, END

class State(TypedDict):
    messages: list
    quality_score: float
    retry_count: int

graph = StateGraph(State)
graph.add_node("analyze", analyze_fn)
graph.add_node("build", build_fn)
graph.add_node("review", review_fn)

# Conditional routing
def route_after_review(state: State):
    if state["quality_score"] >= 8.0:
        return "end"
    elif state["retry_count"] < 3:
        return "retry"
    return "end"

graph.add_conditional_edges("review", route_after_review,
                             {"end": END, "retry": "build"})
compiled = graph.compile(checkpointer=MemorySaver())
```

### Human-in-the-Loop
`interrupt()` inside a node pauses execution. State is checkpointed.
Human modifies state → `Command(resume=updated_state)` to continue.

### Checkpointing
`MemorySaver` (dev) or `PostgresSaver` (prod). Every node execution is persisted.
Resume from any checkpoint: `graph.invoke(None, config={"thread_id": "run-42"})`.

| Dimension | LangGraph |
|-----------|-----------|
| Composition | Explicit DAG — nodes + edges declared upfront |
| State | Single typed dict flows through all nodes; nodes return partials |
| Dependency | Graph edges (fixed or conditional) |
| Parallelism | Parallel branches via fan-out edges (built-in) |
| Quality | Conditional edges enable score-based routing (retry loops) |
| Fallback | Conditional edges → retry node or fallback branch |
| Context | State carries all context; no automatic budget management |

**Trade-off**: Most explicit and auditable. High setup cost. Shines for:
long-running pipelines, retry loops, human-in-the-loop, production persistence.
Conditional edges are the key pattern for quality gates.

---

## 4. AutoGen

**Model**: Multi-agent conversation — teams of agents exchange messages.

### GroupChat Patterns
```python
# Round Robin: fixed order
team = RoundRobinGroupChat([agent_a, agent_b], termination_condition=MaxTurns(4))

# Selector: LLM picks next speaker based on context
team = SelectorGroupChat(
    [planner, coder, reviewer],
    model_client=model,
    selector_prompt="Given the task and history, who speaks next?"
)
await team.run(task="Build feature X")
```

### Speaker Selection
`SelectorGroupChat` uses an LLM call after each message to pick next agent.
Context: full conversation history + agent descriptions.
Cost: +1 LLM call per turn for orchestration. Intelligent but expensive.

### Nested Conversations
```python
# Inner team handles subtask, result injected into outer conversation
inner_team = RoundRobinGroupChat([specialist_a, specialist_b])
# Outer agent triggers inner_team.run() and receives final summary
```
Nested context: inner conversation is summarized/injected into outer agent's messages.

### State Persistence
Conversation history persists within team across multiple `run()` calls.
`team.reset()` clears all context. No built-in structured state — messages only.

| Dimension | AutoGen |
|-----------|---------|
| Composition | Team wraps agents; conversation is the pipeline |
| State | Message history (unstructured); no typed state |
| Dependency | Implicit via message flow; speaker selection decides order |
| Parallelism | Not built-in (Swarm uses sequential handoffs) |
| Quality | No quality gates; termination by condition only |
| Fallback | No retry logic; new turn with corrective message |
| Context | Full history passed each turn; grows unboundedly |

**Trade-off**: Natural for open-ended collaboration. Weak for structured pipelines
where typed data must flow reliably. Context grows with every turn (expensive).
Best for exploratory/creative tasks, not deterministic build pipelines.

---

## 5. CEX Recommendation

CEX builders are specialists: each loads ~13 files (~30KB, ~7500 tokens).
The Crew Runner must pipeline them deterministically with quality control.

### 1. Pattern: LangGraph-inspired explicit DAG (not full LangGraph)
Implement a lightweight StateGraph internally. Each builder = node.
Edges are declared as JSON config — not hardcoded. Reason: conditional routing
for quality gates (score < 7.0 → retry same node, score >= 8.0 → next node).
CrewAI-style sequential is too rigid; AutoGen message-passing is too unstructured.

### 2. State Flow: Typed Pydantic models (CrewAI pattern)
```python
class BuilderOutput(BaseModel):
    content: str
    quality_score: float
    metadata: dict

class RunState(BaseModel):
    inputs: dict
    outputs: dict[str, BuilderOutput]  # keyed by builder_id
    current_step: str
    retry_count: int
```
Each builder receives typed input, returns typed output. No string-passing.

### 3. Execution Plan Format: JSON DAG
```json
{
  "steps": [
    {"id": "outline", "builder": "outline_builder", "inputs": ["$user_request"]},
    {"id": "draft",   "builder": "draft_builder",   "inputs": ["$outline.content"],
     "depends_on": ["outline"]},
    {"id": "review",  "builder": "review_builder",  "inputs": ["$draft.content"],
     "depends_on": ["draft"], "gate": {"min_score": 7.0, "max_retries": 2}}
  ]
}
```
DAG over linear list: enables parallel branches (fan-out) when builders are independent.

### 4. Context Budget Strategy
Each builder gets a **fixed token slice**: 7500 tokens for its 13 ISO files.
State passed in: only the fields declared in builder's input signature (not full history).
Pattern: DSPy signatures for I/O contracts — builder declares what it needs,
runner injects only that. Prevents context bloat across 5+ builder chain.

### 5. Fallback Strategy
LangGraph conditional edge pattern:
```
builder_result.score >= 7.0  → advance to next step
builder_result.score < 7.0 and retry_count < 2 → retry same builder with feedback
retry_count >= 2 → emit DEGRADED output, advance (never block pipeline)
```
Never halt the pipeline. Degrade gracefully. Log failures with score for post-analysis.
CrewAI's "skip and continue" is correct; AutoGen's "new message" is too unstructured.

---

*Sources: CrewAI docs (crewai.com/docs), DSPy docs (dspy.ai), LangGraph (langchain-ai.github.io/langgraph), AutoGen (microsoft.github.io/autogen), community articles 2025.*
