---
id: atom_13_metagpt_chatdev
kind: knowledge_card
title: "Atomic Research 13: MetaGPT + ChatDev (OpenBMB/Tsinghua)"
version: "3.0.0"
quality: 8.6
tags: [metagpt, chatdev, openBMB, tsinghua, multi-agent, sops, dehallucination, chat-chain, atlas, macnet, ier, react-loop, message-pool]
pillar: P01
domain: multi-agent-frameworks
density_score: 0.95
sources:
  - "arXiv:2308.00352 (MetaGPT)"
  - "arXiv:2307.07924 (ChatDev)"
  - "arXiv:2312.17025 (Experiential Co-Learning)"
  - "arXiv:2405.04219 (IER)"
  - "arXiv:2406.07155 (MacNet)"
  - "github.com/FoundationAgents/MetaGPT"
  - "github.com/OpenBMB/ChatDev"
  - "docs.deepwisdom.ai/main/en/guide/tutorials/agent_think_act.html"
  - "github.com/geekan/MetaGPT-docs"
  - "arxiv.org/html/2312.17025v2 (ECL full paper)"
---

# Atomic Research 13: MetaGPT + ChatDev

Two Tsinghua/OpenBMB multi-agent frameworks for software development.
MetaGPT encodes SOPs as structured communication; ChatDev uses chat-chain
dialogue with communicative dehallucination. Both simulate software companies
with typed roles -- different philosophies on agent coordination.

---

## 1. MetaGPT: SOPs as Structured Communication

### 1.1 Core Thesis

**"Code = SOP(Team)"** -- encode real-world Standard Operating Procedures into
prompt sequences so LLM agents produce structured documents, not chat messages.
Eliminates the "Hi, how are you?" overhead of conversational multi-agent systems.

Paper: Hong et al., "MetaGPT: Meta Programming for a Multi-Agent Collaborative
Framework" (arXiv:2308.00352, ICLR 2024).

### 1.2 Two-Layer Architecture

| Layer | Components | Purpose |
|-------|-----------|---------|
| **Foundational** | Environment, Memory, Role, Action, Tools | Individual agent operations + system-wide info exchange |
| **Collaboration** | Shared Message Pool, Publish-Subscribe, SOPs | Multi-agent coordination via structured outputs |

### 1.3 Foundational Components

#### Environment (Shared Workspace)
- Central message pool -- single source of truth
- All agents publish structured outputs to the pool
- Any agent retrieves needed information directly (no peer queries)
- Eliminates one-to-one communication bottlenecks

#### Role (Agent Abstraction)
- `class Role` -- binds profile, actions, memory, constraints, goals
- React-style behavior loop: `_observe` -> `_think` -> `_act`
- Subscribes to upstream message types via `_watch([ActionType])`
- Each role has a domain-specific prompt prefix embedding expertise

```python
class SimpleCoder(Role):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch([UserRequirement])  # subscribe to upstream
        self.set_actions([SimpleWriteCode])  # register actions
```

#### Action (Task Execution Unit)
- `class Action` -- modular subtask with prompt template + `run()` method
- Output encapsulated in `Message(content, role, cause_by)` for routing
- `cause_by` metadata enables subscription filtering

```python
class SimpleWriteCode(Action):
    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.format(instruction=instruction)
        rsp = await self._aask(prompt)
        return parse_code(rsp)
```

#### Memory
- **Short-term**: `self.rc.memory` stores every observed `Message` in a list
- **Long-term**: summarized learnings from completed projects for future constraint updates
- Retrieved via `get_memories()` during `_act` phase

#### Tools
- Role-specific: Product Managers use web search; Engineers execute code
- Integrated directly into Action execution

### 1.3b Message Class: Full API (v0.9+)

The `Message` class is the atomic communication unit. All routing flows
through its metadata fields. Source: github.com/geekan/MetaGPT-docs/agent_communication.md

```python
class Message(BaseModel):
    id: str                             # UUID, auto-generated
    content: str                        # payload (PRD text, code, etc.)
    instruct_content: Optional[BaseModel]  # structured Pydantic output
    role: str                           # "user"|"assistant"|"system"
    cause_by: type[Action]              # WHICH Action produced this
    sent_from: str                      # Role name that sent it
    send_to: set[str]                   # target Roles (default: MESSAGE_ROUTE_TO_ALL = broadcast)
```

**Routing mechanics:**
- `cause_by` is the subscription key: `Role._watch([ActionType])` subscribes
  to all messages where `cause_by` matches a watched Action type
- `send_to` enables unicast; empty set broadcasts to all subscribers
- `instruct_content` carries structured Pydantic models alongside the
  human-readable `content` string -- dual representation per message

**RoleContext (`self.rc`) -- the per-agent working state:**

```python
class RoleContext(BaseModel):
    env: Environment           # reference to shared workspace
    memory: Memory             # short-term message list
    state: int                 # current action index (by_order mode)
    todo: Action               # action selected for this cycle
    watch: set[type[Action]]   # subscribed action types
    news: list[Message]        # unread messages from latest _observe
    react_mode: RoleReactMode  # REACT | BY_ORDER | PLAN_AND_ACT
    max_react_loop: int        # default=1 for BY_ORDER
```

### 1.3c React Modes: Role Execution Strategies

Three execution modes via `self._set_react_mode()`.
Source: docs.deepwisdom.ai/main/en/guide/tutorials/agent_think_act.html

| Mode | Behavior | Use Case | Action Selection |
|------|----------|----------|-----------------|
| `REACT` | Alternates _think -> _act; LLM picks action each turn | Dynamic tasks needing mid-stream reasoning | LLM at each step |
| `BY_ORDER` | Runs registered actions sequentially, no LLM selection | Deterministic SOP pipelines | Pre-defined order |
| `PLAN_AND_ACT` | LLM plans full sequence once, then executes steps | Long-horizon tasks needing upfront decomposition | Plan once, act many |

**`_observe` -> `_think` -> `_act` internals:**

```
_observe():
  1. Pull Messages from Environment matching self.rc.watch
  2. Deduplicate vs self.rc.memory (seen-filter)
  3. Store new messages in self.rc.news
  4. Return count (0 = nothing to do, skip cycle)

_think():
  1. BY_ORDER: pop next registered action -> self.rc.todo
  2. REACT: LLM selects from registered actions given self.rc.news context
  3. PLAN_AND_ACT: generate plan on first call; pop next step on subsequent

_act():
  1. Execute self.rc.todo.run() with memory context
  2. Wrap result: Message(content=rsp, cause_by=type(self.rc.todo))
  3. Publish Message to Environment (-> message pool)
  4. Append to self.rc.memory
```

**max_react_loop:** Default=1 for BY_ORDER (one output per activation,
assembly-line model). Set to N for REACT mode to enable multi-turn debugging
(Engineer retries code up to N times before handing off).

### 1.3d Environment Class: Message Pool Implementation

The `Environment` is the shared pub-sub broker.
Source: arXiv:2308.00352v6 + MetaGPT-docs agent_communication.md

```python
class Environment(BaseModel):
    roles: dict[str, Role]             # all active roles
    history: str                       # text log of all messages
    memory: Memory                     # global message pool (all messages)

    def publish_message(self, message: Message) -> bool:
        # 1. Add message to global memory (pool)
        self.memory.add(message)
        # 2. Append to text history
        self.history += f"\n{message}"
        # 3. Deliver to subscribed roles
        for role in self.roles.values():
            role.put_message(message)   # role buffers if cause_by in watch
        return True
```

**Pool properties:**
- Single source of truth: all agents read from the same pool
- Subscription filter: `role.put_message()` checks `cause_by in self.rc.watch`
  before buffering -- agents only see messages relevant to their subscriptions
- No point-to-point: eliminates N^2 peer routing; all communication is O(N)
- Ordered: history log preserves global causal order of all messages

### 1.4 Role Definitions (Software Company SOP)

| Role | Actions | Structured Output |
|------|---------|-------------------|
| **Product Manager** | Requirement analysis, competitive analysis | PRD (user stories, requirements pool, competitive quadrant chart) |
| **Architect** | System design, interface specification | System design doc (file lists, data structures, class diagrams, sequence flows) |
| **Project Manager** | Task decomposition, work assignment | Task distribution (by file/module, with dependencies) |
| **Engineer** | Code implementation, iterative debugging | Code files following architectural contracts |
| **QA Engineer** | Test formulation, bug detection | Unit test suites with expected behaviors |

### 1.5 Publish-Subscribe Communication

```
ProductManager --[PRD]--> Message Pool
    Architect watches [PRD] --> reads pool --> produces SystemDesign
        ProjectManager watches [SystemDesign] --> produces TaskList
            Engineer watches [TaskList] --> produces Code
                QAEngineer watches [Code] --> produces Tests
```

Key: agents activate ONLY after receiving prerequisite dependencies.
No polling, no chat -- subscription-driven activation.

### 1.6 SOPs as Prompt Sequences

Instead of emergent conversation, MetaGPT hardcodes the software development
waterfall into sequential role activations:

1. **Requirement Analysis** (PM) -> structured PRD
2. **Technical Design** (Architect) -> system components + interfaces
3. **Task Decomposition** (PM) -> granular file-level assignments
4. **Implementation** (Engineer) -> code per spec
5. **Quality Assurance** (QA) -> test cases + execution feedback

Each step produces a DOCUMENT, not a chat reply. Documents have schemas.

### 1.7 Executable Feedback Mechanism

After code generation, Engineers write and execute unit tests iteratively:
- Max 3 retry iterations
- Tests run in actual environment (not simulated)
- +4.2% Pass@1 on HumanEval, +5.4% on MBPP vs no-feedback baseline
- Human revision cost: 0.83 interventions/project (vs 2.5 for ChatDev)

### 1.8 Team Composition API

```python
team = Team()
team.hire([ProductManager(), Architect(), Engineer(), QAEngineer()])
team.invest(investment=3.0)  # budget in dollars
team.run_project("Build a snake game")
await team.run(n_round=5)
```

### 1.9 SOP-to-Prompt Compilation Process

MetaGPT's "meta-programming" is the process of encoding a real-world SOP
into executable prompt sequences. Three transformation stages:

**Stage 1: Role Profiling (SOP -> Agent Identity)**
```
SOP Step: "Product Manager writes PRD"
         |
         v
Profile Prompt: "You are a professional product manager at a software company.
Your goal is to design a concise, usable, and efficient product. Never ask for
clarification; make all decisions yourself. Output must be structured."
```
Each SOP role maps to a system-level identity prompt injected into every call.

**Stage 2: Action Templating (SOP Step -> Prompt Template)**
```
SOP Step: "PM performs competitive analysis"
         |
         v
Action Template:
  PROMPT_TEMPLATE = """
  Role: {profile}
  ATTENTION: Use markdown, be professional.
  ## Context
  Requirements: {requirements}
  ## Format example
  {format_example}
  -----
  Role: {role}; Requirements: ...
  ## {constraint}
  """
```
Templates enforce output FORMAT (competitive quadrant, user stories, etc.)
so downstream agents receive structured data, not free text.

**Stage 3: Document Schema Enforcement (Output -> Typed Artifact)**

Each Action's output maps to a Pydantic model:

| SOP Document | Pydantic Model | Key Fields |
|-------------|---------------|-----------|
| PRD | `PRD` | `goals`, `user_stories`, `requirement_pool`, `competitive_quadrant_chart` |
| System Design | `SystemDesign` | `implementation_approach`, `file_list`, `data_structures`, `api_design` |
| Task List | `Tasks` | `required_packages`, `task_list` (file-granular) |
| Code Review | `CodeSummary` | `LGTM`, `comments` |

The Pydantic model lives in `instruct_content`; the string version in `content`.
Downstream agents parse `instruct_content` for machine-readable fields,
and optionally read `content` for context. This dual representation
prevents schema failures when downstream agents receive malformed output.

**Summary: SOP -> Prompt Compilation Pipeline**

```
Real-world SOP
  1. Role profiling     -> system prompt per role (identity injection)
  2. Action templating  -> PROMPT_TEMPLATE per action (format enforcement)
  3. Schema binding     -> Pydantic model per output (type safety)
  4. Watch registration -> _watch([ActionType]) per role (dependency wiring)
  5. Team assembly      -> Team.hire([roles]) (graph construction)
                       ===
  Executable multi-agent workflow
```
Source: arXiv:2308.00352v6, section 3; github.com/geekan/MetaGPT-docs

### 1.10 Unique Concepts

| Concept | Description | Industry Parallel |
|---------|-------------|-------------------|
| **SOPs-as-prompts** | Real-world procedures encoded as prompt sequences governing agent behavior | Process mining -> prompt compilation |
| **Structured communication** | Documents/diagrams instead of natural language chat between agents | Contract-first API design |
| **Shared message pool** | Pub-sub environment replacing point-to-point dialogue | Message broker (Kafka/RabbitMQ pattern) |
| **Assembly line paradigm** | Sequential role activation with intermediate verification | CI/CD pipeline with stage gates |
| **Executable feedback** | Code execution results fed back into generation loop | Test-driven development (TDD) |
| **React mode** | Configurable agent execution strategy (REACT/BY_ORDER/PLAN_AND_ACT) | State machine / execution engine |
| **Dual-representation Message** | content (string) + instruct_content (Pydantic) per message | Schema-first API with human-readable fallback |

### 1.11 API Evolution: v0.5 -> v0.7 -> v0.8

Significant breaking changes. Source: github.com/FoundationAgents/MetaGPT/releases

| Version | Released | Key Change | Migration Impact |
|---------|----------|-----------|-----------------|
| v0.5.0 | 2023-Q4 | Incremental development (`--inc` flag) | New: project evolution without full rebuild |
| v0.7.0 | Feb 2024 | `Role._init_actions` removed -> `Role.set_actions()` | Breaking: all subclasses must update |
| v0.7.0 | Feb 2024 | Global `CONFIG` singleton removed -> per-role `Config` instances | Breaking: no more `from metagpt.config import CONFIG` |
| v0.7.0 | Feb 2024 | `Context` class introduced | Unified config + repo + workspace per Role instance |
| v0.7.0 | Feb 2024 | `mark_as_readable` / `mark_as_writable` decorators on Env | Explicit env access control; replaces implicit role permissions |
| v0.7.0 | Feb 2024 | `ActionNode` from Pydantic BaseModel | Structured sub-action trees with schema enforcement + retry |
| v0.8.0 | Mar 2024 | Data Interpreter agent (notebook + browser + shell) | SOTA on ML/math/open-ended tasks; standalone agent |
| v0.8.0 | Mar 2024 | RAG module (index + retrieve + rank) | Optional import; adds retrieval-augmented role context |
| v0.8.0 | Mar 2024 | Claude, QianFan, DashScope, Yi LLM providers | Config `llm.api_type` field selects provider |

**Context class (v0.7+)** -- per-role isolated execution environment:

```python
class Context(BaseModel):
    config: Config          # LLM settings + runtime configuration
    repo: RepoManager       # Git-aware file repository access
    workspace: WorkSpace    # Task-specific working directory
```

Each `Role` gets its own `Context`, enabling concurrent roles with
different LLM providers or configurations in the same `Team`.

**ActionNode (v0.7+)** -- schema-enforced sub-action step:

Unlike raw `Action._aask()` (returns unstructured string), `ActionNode.fill()`
calls `_aask_v1()` which enforces a Pydantic schema on LLM output via
retry-with-repair (up to N retries if validation fails):

```python
class WritePRD(Action):
    async def run(self, requirements: str) -> PRD:
        # ActionNode chain: each node = one schema-enforced LLM call
        prd = await PRD_ACTION_NODE.fill(requirements, self.llm)
        return prd

# ActionNode constructed from Pydantic model (v0.7+):
PRD_ACTION_NODE = ActionNode.from_pydantic(PRDModel)
# from_pydantic() auto-generates prompt instructions from Pydantic
# field descriptions -- Pydantic docstrings -> prompt compilation
```

`ActionNode` is the recommended pattern for SOP scenarios where outputs
map to finite-state Pydantic models. For dynamic runtime prompt generation,
`DataInterpreter` (v0.8) is preferred.
Source: github.com/FoundationAgents/MetaGPT/issues/1439

---

## 2. ChatDev: Chat Chain + Communicative Dehallucination

### 2.1 Core Thesis

Software development as multi-turn chat between role-playing agents.
Language is the unifying bridge -- agents guided in WHAT to communicate
(chat chain) and HOW to communicate (communicative dehallucination).

Paper: Qian et al., "ChatDev: Communicative Agents for Software Development"
(arXiv:2307.07924, ACL 2024).

### 2.2 Waterfall-to-Chat-Chain Decomposition

ChatDev adopts the waterfall model but decomposes each phase into atomic
chat subtasks between an Instructor and an Assistant:

```
WATERFALL PHASE          CHAT SUBTASKS
-----------------        -------------------------
Design Phase     -----> Requirements Chat (CEO<->CTO)
                         Architecture Chat (CTO<->Programmer)
Coding Phase     -----> Code Writing Chat (Programmer<->CTO)
                         Code Completion Chat (Programmer<->Reviewer)
Testing Phase    -----> Code Review (Reviewer<->Programmer) [static]
                         System Test (Tester<->Programmer) [dynamic]
Documenting      -----> Documentation Chat
```

Each subtask: T = tau(chat(Instructor, Assistant))
- tau extracts the solution (code or text) from dialogue
- Max communication rounds bounded per phase

### 2.3 Role Definitions

| Role | Function | Typical Pairing |
|------|----------|-----------------|
| **CEO** | Overall requirements, project direction | Instructor for design |
| **CTO** | Technical architecture decisions | Instructor/Assistant flexibly |
| **CPO** | Product requirements refinement | Instructor for requirements |
| **Programmer** | Code implementation | Assistant for most phases |
| **Reviewer** | Code quality, bug identification | Instructor for code review |
| **Tester** | Dynamic system validation | Instructor for testing |
| **Art Designer** | Visual asset generation | Assistant for UI |

### 2.4 Instructor-Assistant Paradigm

Every chat subtask has exactly two agents with asymmetric roles:

- **Instructor (I)**: initiates direction with instructions (->)
- **Assistant (A)**: responds with solutions (~>)
- Multi-turn: I->A, A~>I, I->A, A~>I, ... until consensus

```
Vanilla:    <I->A, A~>I> (repeat)
Enhanced:   <I->A, <A->I, I~>A> (repeat), A~>I> (repeat)
```

The "enhanced" pattern IS communicative dehallucination (see below).

### 2.5 Communicative Dehallucination

**The unique mechanism.** When an assistant receives vague instructions that
would cause hallucinated code:

1. Assistant REVERSES roles -- becomes temporary instructor
2. Proactively REQUESTS specific details from the original instructor
3. Gets clarification BEFORE generating the formal response
4. Resumes assistant role with now-precise instructions

```
Standard:  Instructor gives vague spec -> Assistant hallucinates code
Dehalluc:  Instructor gives vague spec -> Assistant asks "what exactly?"
           -> Instructor clarifies -> Assistant produces precise code
```

This is NOT self-reflection (agent talks to itself). It is communicative --
the assistant explicitly queries the instructor for missing information,
creating finer-grained information exchange.

Result: reduces incomplete, unexecutable, and inaccurate code generation.

### 2.6 Memory System

| Type | Scope | Content |
|------|-------|---------|
| **Short-term** | Within a phase | Current chat dialogue history |
| **Long-term** | Cross-phase | Solutions from prior phases (M-tilde) bridging to next phase |

Long-term memories enable "smooth transition between subtasks" -- the coding
phase inherits the design phase's architecture decisions.

### 2.7 Inception Prompting

To sustain multi-turn communication and prevent premature termination,
ChatDev uses inception prompting -- system-level instructions that keep
agents in their roles and maintain dialogue momentum until genuine consensus.

### 2.8 Unique Concepts

| Concept | Description | Industry Parallel |
|---------|-------------|-------------------|
| **Chat Chain** | Waterfall phases decomposed into atomic instructor-assistant chat subtasks | Pipeline of pair-programming sessions |
| **Communicative Dehallucination** | Role reversal where assistant requests clarification before responding | Rubber-duck debugging / requirements elicitation |
| **Instructor-Assistant paradigm** | Asymmetric 2-agent dialogue per subtask | Pair programming (driver/navigator) |
| **Inception prompting** | System prompts sustaining role-play across multi-turn dialogue | System prompt anchoring |
| **Cross-phase memory** | Prior phase solutions as long-term context for next phase | Build artifacts as pipeline inputs |

---

## 3. Experiential Co-Learning (ChatDev Extension)

Paper: Qian et al., "Experiential Co-Learning of Software-Developing Agents"
(arXiv:2312.17025, 2023). Integrated into ChatDev Jan 2024.

### 3.1 Three Modules

| Module | What it Does | Mechanism |
|--------|-------------|-----------|
| **Co-Tracking** | Joint exploration by instructor + assistant | Directed chain graph G=(N,E) of solution states; each node is a code snapshot |
| **Co-Memorizing** | Mine shortcuts from trajectories | Deduplicate graph, score nodes, extract non-adjacent high-gain paths |
| **Co-Reasoning** | Use experience pools for unseen tasks | Few-shot retrieval from instructor/assistant pools |

**Formal graph definition (arXiv:2312.17025v2):**

```
G = (N, E) where:
  N = {r_j | r_j in R} union {r_0}
      r_0   = initial empty codebase (before any instruction)
      r_j   = code snapshot after j-th instruction is applied
  E = {(r_j, i_{j+1}, r_{j+1})}
      i_{j+1} = instruction that transforms r_j -> r_{j+1}
```

Graph deduplication: MD5 hashing of code snapshots detects identical
states; duplicate nodes are merged to prevent shortcut mining over
circular paths. This bounds the graph size regardless of interaction length.

### 3.2 Shortcut Experiences

A "shortcut" is an accelerated path between non-adjacent solution states:

```
Normal:    s0 -> s1 -> s2 -> s3 -> s4 (5 steps)
Shortcut:  s0 --------> s3           (1 step, pseudo-instruction generated)
```

**Node scoring**: omega(sj) = sim(sj, task) * sim(sj, s_final) * [[sj]]
- sim() = semantic similarity via text-embedding-ada-002
- [[sj]] = 1 if code compiles, 0 otherwise
- Information gain threshold: epsilon >= 0.90

**Pseudo-instruction generation**: compare source and target code states
to produce a synthetic instruction describing the direct transformation.

### 3.3 Experience Pools

Two separate key-value stores (paper notation: M_I / M_A):
- **M_I -- Instructor pool (S_i)**: {(r_i, r_i->r_j)} -- current state maps to shortcut instruction
- **M_A -- Assistant pool (S_a)**: {(r_i->r_j, r_j)} -- shortcut instruction maps to target state

Where r_i->r_j denotes the pseudo-instruction bridging non-adjacent states.

Indexed via dense vector embeddings (text-embedding-ada-002).
Retrieval function: k(q, M) = top-k cosine similarity search.
- k_code = 1 (one code-embedding-based exemplar per query)
- k_text = 2 (two text-embedding-based exemplars per query)
- Combined: 3 few-shot examples injected as context per inference step

### 3.4 Co-Reasoning at Inference

1. Instructor receives current code state sj
2. Retrieves top-k matching instructions from S_i (k_code=1, k_text=2)
3. Uses retrieved instructions as few-shot examples
4. Assistant receives instruction, retrieves matching solutions from S_a
5. Iterates until task complete

**Granular metric breakdown (NLDD dataset, ChatGPT-3.5, arXiv:2312.17025v2):**

| Metric | Vanilla ChatDev | + Co-Learning | Delta |
|--------|-----------------|---------------|-------|
| Completeness (alpha) | 0.6131 | 0.9497 | +54.9% |
| Executability (beta) | 0.6890 | 0.9400 | +36.4% |
| Autonomy (alpha*beta*gamma) | 0.3340 | 0.7100 | +112.6% |

Autonomy = alpha * beta * gamma where gamma captures task correctness.
Overall comprehensive score: 0.4267 (vanilla) -> 0.7304 (co-learning).

**Experimental configuration:**
- Base model: ChatGPT-3.5 (gpt-3.5-turbo)
- Max interaction rounds: 5 per chat phase
- Embedding model: text-embedding-ada-002 (code + text)
- Deduplication: MD5 hash of code snapshots
- Information gain threshold: epsilon = 0.90
- Dataset: NLDD (Natural Language Driven Development), 4:1:1 train/val/test
- Execution environment: Python 3.11.4

### 3.5 Iterative Experience Refinement (IER, May 2024)

Extension of Co-Learning. Paper: arXiv:2405.04219 (OpenBMB, May 2024).

**Problem with base Co-Learning:** experience pools grow unbounded, accumulating
low-quality or rarely-used entries that degrade retrieval precision.

**IER adds four operations across task batches:**

| Operation | Description | When |
|-----------|-------------|------|
| **Acquisition** | Extract shortcut experiences from completed tasks | After each task |
| **Utilization** | Retrieve relevant experiences as few-shot context | During task execution |
| **Propagation** | Share high-quality experiences to related tasks | Between task batches |
| **Elimination** | Discard low-quality or stale experiences | Periodic heuristic pass |

**Two refinement patterns:**

```
Successive pattern:  experiences from latest task batch only
                     (focus on recency, avoid stale context)

Cumulative pattern:  integrate all historical task batch experiences
                     (full history, higher recall, more retrieval noise)
```

**Heuristic elimination rules:**
- Prioritize frequently-retrieved experiences (usage count > threshold)
- Discard experiences with quality score below floor
- Remove experiences unused across N consecutive task batches (staleness)

**Result:** IER further improves over base Co-Learning on sequential task benchmarks.
Successive pattern outperforms cumulative when task distribution shifts over time.

### 3.6 MacNet: Multi-Agent Collaboration Networks (June 2024)

Paper: arXiv:2406.07155 (OpenBMB, June 2024). ChatDev DAG extension.

**Problem with Chat Chain:** linear instructor-assistant topology limits
parallelism and cannot model non-sequential agent dependencies.

**MacNet replaces the linear chain with a DAG:**

```
Chat Chain (v1.0):   A -> B -> C -> D -> E (strictly sequential)

MacNet (v2.0):       A -+-> B -> D -+-> G
                        |           |
                        +-> C -> E -+-> H
                                |
                                +-> F (parallel branches)
```

**Key properties:**
- Directed acyclic graph: no circular dependencies, no infinite loops
- 1000+ agents: macroscale coordination without exceeding context limits
  (solved via topology-aware message routing -- agents only receive
  messages from their DAG predecessors)
- Topology-agnostic: supports chain, tree, mesh, ring, and hybrid topologies
- `generate_graph.py`: utility to generate custom graph structures

**Context limit solution:**
MacNet routes messages along DAG edges only; each agent receives the
concatenated outputs of its immediate predecessors, not the full history.
This keeps per-agent context bounded regardless of total agent count.

**ChatDev 2.0 impact:** rebranded as "Dev All through LLM-powered Multi-Agent
Collaboration" -- GUI-based no-code agent graph editor wraps MacNet.

---

## 4. Head-to-Head Comparison

| Dimension | MetaGPT | ChatDev |
|-----------|---------|---------|
| **Communication** | Structured documents via pub-sub | Natural language chat chains |
| **Agent interaction** | N-to-pool (shared message pool) | 1-to-1 instructor-assistant pairs |
| **Workflow model** | Assembly line with SOPs | Waterfall decomposed into chat subtasks |
| **Topology** | Fixed roles, sequential activation | DAG via MacNet (v2.0); chain in v1.0 |
| **Hallucination control** | Structured output schemas + executable feedback | Communicative dehallucination (role reversal) |
| **Verification** | Intermediate document schemas at each stage | Code review chat + dynamic testing chat |
| **Learning** | Long-term memory for future projects | Co-Learning + IER (shortcut pools + elimination) |
| **Executability score** | 3.75 (SoftwareDev benchmark) | 2.25 (same benchmark) |
| **Human revision cost** | 0.83 interventions/project | 2.50 interventions/project |
| **Code execution** | Engineers run + debug iteratively (3 retries) | Python 3.11.4 sandbox, temperature=0.2 |
| **Scale** | 5-7 fixed roles per project | 1000+ agents (MacNet DAG) |
| **Message routing** | cause_by subscription filter | DAG edge routing (predecessor outputs only) |
| **Composition API** | `Team.hire([roles])` + `team.run()` | Config-driven phase chains (YAML) + graph editor |
| **React modes** | REACT / BY_ORDER / PLAN_AND_ACT | Instructor-Assistant (fixed per subtask) |
| **Origin** | DeepWisdom / Tsinghua | OpenBMB / Tsinghua |
| **License** | MIT | Apache 2.0 |
| **Latest research** | Data Interpreter (arXiv:2402.18679) | MacNet + IER (arXiv:2406.07155, 2405.04219) |

---

## 5. CEX Mapping

### 5.1 Concept-to-CEX Translation

| MetaGPT/ChatDev Concept | CEX Equivalent | CEX Location |
|--------------------------|----------------|--------------|
| Role (MetaGPT) | Nucleus (N01-N07) | `N0x_*/agent_card_n0x.md` |
| Action (MetaGPT) | 8F pipeline function (F1-F8) | `.claude/rules/8f-reasoning.md` |
| Environment / Message Pool | `.cex/runtime/` (signals, handoffs, proposals) | `.cex/runtime/` |
| Publish-Subscribe | Signal writer + handoff files | `_tools/signal_writer.py` |
| SOPs-as-prompts | Builder ISOs (13 per kind) | `archetypes/builders/{kind}-builder/` |
| Structured output | Typed artifacts with YAML frontmatter | `P{01-12}_*/_schema.yaml` |
| Team.hire() | `bash _spawn/dispatch.sh grid` | `_spawn/dispatch.sh` |
| Chat Chain (ChatDev) | Wave-based dispatch (sequential phases) | `cex_mission_runner.py` |
| Instructor-Assistant | N07 handoff -> nucleus execution | `.cex/runtime/handoffs/` |
| Communicative Dehallucination | GDP (Guided Decision Protocol) | `.claude/rules/guided-decisions.md` |
| Experience Pool | Memory system (entity_memory, learning_record) | `P10_memory/`, `.cex/learning_records/` |
| Shortcut mining | `cex_evolve.py` heuristic pass | `_tools/cex_evolve.py` |
| Long-term memory | Knowledge Cards (KCs) | `P01_knowledge/library/kind/kc_*.md` |
| QA Engineer role | F7 GOVERN quality gate | 8F pipeline step 7 |
| Product Manager PRD | Mission plan + spec | `.cex/runtime/plans/` |
| Executable feedback | `cex_doctor.py` + `cex_system_test.py` | `_tools/cex_doctor.py` |

### 5.2 What CEX Could Adopt

| Pattern | From | Value for CEX | Effort |
|---------|------|---------------|--------|
| **Pub-sub message pool** | MetaGPT | Replace file-based signals with in-memory message broker for faster inter-nucleus coordination | High (architecture change) |
| **Communicative dehallucination** | ChatDev | Nuclei could request clarification from N07 mid-task instead of guessing when handoff is ambiguous | Medium (signal protocol extension) |
| **Experience pools with shortcut mining** | ChatDev Co-Learning | Mine learning_records for reusable instruction-solution pairs, inject as few-shot context | Medium (new tool) |
| **Executable feedback loop** | MetaGPT | Extend F7 GOVERN to run generated code and feed errors back to F6 PRODUCE (already partial via cex_doctor) | Low (extend existing) |
| **Structured document schemas per role** | MetaGPT | Enforce output schemas per nucleus (not just per kind) -- e.g., N01 always outputs intelligence_brief format | Low (schema extension) |

### 5.3 Key Architectural Differences

| Aspect | MetaGPT/ChatDev | CEX |
|--------|-----------------|-----|
| Agent count | 5-7 fixed roles | 7 nuclei, each with 125 sub-agent builders |
| Communication | Shared pool / chat pairs | File-based (handoffs, signals, proposals) |
| Task decomposition | Per-project (dynamic) | Per-kind (typed, 130 kinds) |
| Quality control | Executable tests | 3-layer scoring (structural + rubric + semantic) |
| Learning | Experience pools (ChatDev) / long-term memory (MetaGPT) | learning_records + knowledge_cards + memory_age decay |
| Process model | Waterfall (both) | Wave-based parallel dispatch |

---

## 6. Key Takeaways

1. **SOPs beat chat.** MetaGPT's structured communication outperforms ChatDev's
   conversational approach by 67% on executability (3.75 vs 2.25). CEX already
   follows this philosophy with typed artifacts and builder ISOs.

2. **Dehallucination is under-explored in CEX.** ChatDev's communicative
   dehallucination (assistant requests clarification) maps to GDP but only at
   the N07 level. Extending this to nucleus-to-nucleus mid-task queries would
   reduce wasted dispatch cycles.

3. **Experience mining is the next frontier.** ChatDev's co-learning framework
   (+71% comprehensive metric) suggests CEX's learning_records could be mined
   for shortcut-oriented experiences and injected as few-shot examples during
   F3 INJECT.

4. **Pub-sub > file signals.** Both frameworks use in-memory communication.
   CEX's file-based signals work but introduce I/O latency. A lightweight
   pub-sub layer (even file-watching with inotify/ReadDirectoryChanges) would
   reduce coordination overhead.

5. **Executable feedback is table stakes.** Both frameworks run generated code.
   CEX's F7 GOVERN should evolve to include code execution for code-producing
   kinds (landing_page, mcp_server, cli_tool, api_client).

---

## References

- Hong, S. et al. (2024). "MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework." ICLR 2024. arXiv:2308.00352.
- Qian, C. et al. (2024). "ChatDev: Communicative Agents for Software Development." ACL 2024. arXiv:2307.07924.
- Qian, C. et al. (2023). "Experiential Co-Learning of Software-Developing Agents." arXiv:2312.17025.
- Qian, C. et al. (2024). "Iterative Experience Refinement of Software-Developing Agents." arXiv:2405.04219.
- Qian, C. et al. (2024). "Scaling LLM-based Multi-Agent Collaboration." MacNet. arXiv:2406.07155.
- MetaGPT GitHub (FoundationAgents): https://github.com/FoundationAgents/MetaGPT
- MetaGPT Docs (agent communication): https://github.com/geekan/MetaGPT-docs/blob/main/src/en/guide/in_depth_guides/agent_communication.md
- MetaGPT Docs (think & act): https://docs.deepwisdom.ai/main/en/guide/tutorials/agent_think_act.html
- MetaGPT Docs (multi-agent 101): https://docs.deepwisdom.ai/main/en/guide/tutorials/multi_agent_101.html
- ChatDev GitHub: https://github.com/OpenBMB/ChatDev
- ChatDev MacNet branch: https://github.com/OpenBMB/ChatDev/tree/macnet
- ECL paper (HTML): https://arxiv.org/html/2312.17025v2
- MetaGPT Releases: https://github.com/FoundationAgents/MetaGPT/releases
- MetaGPT Agent Communication: https://docs.deepwisdom.ai/main/en/guide/in_depth_guides/agent_communication.html
