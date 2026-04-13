---
id: atom_13_metagpt_chatdev
kind: knowledge_card
title: "Atomic Research 13: MetaGPT + ChatDev (OpenBMB/Tsinghua)"
version: "2.0.0"
quality: 8.9
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
    send_to: set[str]                   # target Roles (empty = broadcast)
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

### 1.9 Unique Concepts

| Concept | Description | Industry Parallel |
|---------|-------------|-------------------|
| **SOPs-as-prompts** | Real-world procedures encoded as prompt sequences governing agent behavior | Process mining -> prompt compilation |
| **Structured communication** | Documents/diagrams instead of natural language chat between agents | Contract-first API design |
| **Shared message pool** | Pub-sub environment replacing point-to-point dialogue | Message broker (Kafka/RabbitMQ pattern) |
| **Assembly line paradigm** | Sequential role activation with intermediate verification | CI/CD pipeline with stage gates |
| **Executable feedback** | Code execution results fed back into generation loop | Test-driven development (TDD) |

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

Two separate key-value stores:
- **Instructor pool (S_i)**: current_solution -> instruction (what to tell the assistant)
- **Assistant pool (S_a)**: instruction -> resulting_solution (how to respond)

Indexed via dense vector embeddings. Retrieved via top-k similarity search.

### 3.4 Co-Reasoning at Inference

1. Instructor receives current code state sj
2. Retrieves top-k matching instructions from S_i (k_code=1, k_text=2)
3. Uses retrieved instructions as few-shot examples
4. Assistant receives instruction, retrieves matching solutions from S_a
5. Iterates until task complete

Result: comprehensive metric jumps from 0.4267 (vanilla ChatDev) to 0.7304.

---

## 4. Head-to-Head Comparison

| Dimension | MetaGPT | ChatDev |
|-----------|---------|---------|
| **Communication** | Structured documents via pub-sub | Natural language chat chains |
| **Agent interaction** | N-to-pool (shared message pool) | 1-to-1 (instructor-assistant pairs) |
| **Workflow model** | Assembly line with SOPs | Waterfall decomposed into chat subtasks |
| **Hallucination control** | Structured output schemas + executable feedback | Communicative dehallucination (role reversal) |
| **Verification** | Intermediate document standards at each stage | Code review chat + dynamic testing chat |
| **Learning** | Long-term memory for future projects | Experiential co-learning with shortcut pools |
| **Executability score** | 3.75 (SoftwareDev benchmark) | 2.25 (same benchmark) |
| **Human revision cost** | 0.83 interventions/project | 2.50 interventions/project |
| **Code execution** | Engineers run + debug iteratively (3 retries) | Python 3.11.4 sandbox, temperature=0.2 |
| **Composition API** | `Team.hire([roles])` + `team.run()` | Config-driven phase chains (YAML) |
| **Origin** | DeepWisdom / Tsinghua | OpenBMB / Tsinghua |
| **License** | MIT | Apache 2.0 |

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
- MetaGPT GitHub: https://github.com/geekan/MetaGPT
- MetaGPT Docs: https://docs.deepwisdom.ai/main/en/guide/tutorials/multi_agent_101.html
- ChatDev GitHub: https://github.com/OpenBMB/ChatDev
