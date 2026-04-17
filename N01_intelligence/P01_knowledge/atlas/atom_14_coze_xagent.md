---
id: atom_14_coze_xagent
kind: knowledge_card
pillar: P01
quality: 8.9
density_score: 0.93
title: "Atomic Research 14: Coze (ByteDance) + XAgent (Tsinghua/OpenBMB)"
version: 2.0.0
author: N01
tags: [coze, xagent, bytedance, tsinghua, openbmb, multi-agent, workflow, dual-loop, atlas, toolserver, docker, persistent-planning, skills-marketplace]
tldr: "Coze is ByteDance's visual agent platform (Go/Hertz backend, React+TypeScript frontend, Docker Compose self-hosting) with 13 workflow node types, Skills Marketplace API, and persistent planning. XAgent is Tsinghua/OpenBMB's autonomous agent with Dispatcher-Planner-Actor triad, dual-loop state machine (outer=planning, inner=ReACT execution), Docker-containerized ToolServer (Manager+Monitor+Node tiers), and AskForHumanHelp HITL protocol."
domain: intelligence
created: 2026-04-13
updated: 2026-04-13
sources:
  - https://github.com/coze-dev/coze-studio
  - https://github.com/OpenBMB/XAgent
  - https://aixsociety.com/bytedances-coze-2-0-transforming-ai-from-chat-tool-to-intelligent-work-partner/
  - https://blog.x-agent.net/blog/xagent/
  - https://docs.coze.com/guides/plugin_tools
  - https://docs.coze.com/guides/use_local_plugin
  - https://github.com/coze-dev/coze-py
  - https://xagent-doc.readthedocs.io/en/latest/source/ToolServer/README.html
  - https://github.com/OpenBMB/XAgent/blob/main/ToolServer/README.md
  - https://jimmysong.io/blog/open-source-ai-agent-workflow-comparison/
  - https://test-news.aibase.com/news/19989
---

# Atomic Research 14: Coze (ByteDance) + XAgent (Tsinghua/OpenBMB)

## 1. Platform Overview

| Dimension | Coze (ByteDance) | XAgent (OpenBMB/Tsinghua) |
|-----------|-------------------|---------------------------|
| Type | Visual agent development platform (no-code/low-code) | Autonomous LLM-driven agent framework |
| Open-source | Coze Studio + Coze Loop (July 2025) | Full OSS (MIT, since Oct 2023) |
| Backend | Go (microservices, DDD) | Python |
| Frontend | React + TypeScript | Web GUI + CLI |
| Primary model | Doubao (ByteDance in-house) + pluggable | GPT-4 primary, pluggable LLMs |
| Deployment | SaaS + self-hosted (Coze Studio) | Docker-containerized (ToolServer) |
| Architecture | Visual DAG workflow + multi-agent orchestration | Dispatcher-Planner-Actor triad + dual-loop |

## 2. Coze -- Core Concepts

### 2.1 Bot (Agent)

The top-level entity. A Bot combines: a system prompt, attached plugins, workflows, knowledge bases, and memory. Bots can be published to channels (Discord, Telegram, Slack, web embed). In Coze 2.0, bots gain persistent planning and skill composition.

**CEX mapping**: Closest to `agent` (P02) + `agent_card` (P08). CEX separates definition (agent) from deployment spec (agent_card); Coze bundles both into a single Bot entity.

### 2.2 Plugin

External capability integration. Plugins connect to third-party APIs (Yelp, Google, custom REST endpoints) and expose structured actions the Bot can invoke. Plugins require auth configuration and are managed via a Plugin Store.

**CEX mapping**: `cli_tool` / `api_client` / `mcp_server` (P04). CEX's tool pillar serves the same purpose. Coze's Plugin Store is analogous to CEX's tool registry pattern but with a marketplace layer.

### 2.3 Workflow

A visual DAG of executable nodes that implements business logic. Workflows are the core automation primitive -- drag-and-drop canvas, typed inputs/outputs, branching, loops. Workflows can be nested (a Workflow node inside another workflow).

**CEX mapping**: `workflow` (P12). CEX workflows are YAML-defined; Coze workflows are visual-first. The node type diversity (13 types) exceeds CEX's current workflow expressiveness.

### 2.4 Workflow Node Types (13)

| Node | Purpose | CEX equivalent |
|------|---------|----------------|
| **Start** | Entry point, receives user input | 8F F1 CONSTRAIN (implicit) |
| **End** | Returns final result | 8F F8 COLLABORATE (implicit) |
| **LLM** | Invokes a language model with prompt + temperature | `prompt_template` (P03) + model call |
| **Code** | Python/JS execution for data transforms | `cli_tool` (P04) or inline script |
| **Knowledge** | RAG recall from knowledge base | `rag_source` + `chunk_strategy` (P01) |
| **Database** | Read/write structured data via NL2SQL | No direct equivalent -- gap |
| **Plugin** | Calls external API via plugin | `api_client` / `mcp_server` (P04) |
| **Condition** | If-else branching | Workflow conditional (P12) |
| **Loop** | Repeat N times or until condition | Workflow loop (P12) |
| **Intent Recognition** | Classify user intent against presets | `cex_intent_resolver.py` pattern |
| **Text Processing** | String manipulation on variables | Inline in code node (CEX) |
| **Message** | Mid-workflow output to user (streaming) | No direct equivalent -- gap |
| **Question** | Ask user mid-workflow, collect answer | GDP `NeedsUserDecision` gate (F4) |
| **Variable** | Read/write bot-level variables | Memory scope (P10) |
| **Workflow** | Nested sub-workflow execution | Dispatch sub-workflow (P12) |

### 2.5 Knowledge Base

RAG-powered retrieval to combat hallucination. Supports document upload (PDF, DOCX, TXT), automatic chunking, and embedding. Knowledge nodes in workflows recall top-K paragraphs by semantic similarity.

**CEX mapping**: `knowledge_card` + `embedding_config` + `chunk_strategy` + `rag_source` (P01). CEX has richer typing (separate artifacts per concern); Coze bundles into a single "Knowledge Base" resource.

### 2.6 Multi-Agent Mode

Orchestration of multiple specialized Bots. Each node in a multi-agent graph is a full Bot with its own prompt, skills, and knowledge. Control flow uses **jump conditions** (keyword-based or LLM-evaluated) to route between bots.

| Pattern | Coze implementation | CEX equivalent |
|---------|---------------------|----------------|
| Supervisor | One bot dispatches to specialist bots | N07 orchestrator dispatching to N01-N06 |
| Keyword routing | Jump conditions on message content | Intent resolution (F1) |
| Handoff | Bot-to-bot with context passing | Handoff files in `.cex/runtime/handoffs/` |
| Parallel | Multiple bots run concurrently | Grid dispatch (`dispatch.sh grid`) |

**CEX mapping**: CEX's nucleus-based multi-agent is structurally similar but uses filesystem-based handoffs and git-based coordination rather than in-process message passing. Coze's jump conditions are simpler (keyword match) vs CEX's intent resolution (taxonomy-based).

### 2.7 Exploration Mode

The agent executes tasks reactively based on user input. Standard chatbot behavior -- user asks, agent acts. No upfront planning.

**CEX mapping**: Direct `/build` command -- single-shot 8F execution without mission decomposition.

### 2.8 Planning Mode

The agent generates a step-by-step plan, presents it for user approval, and seeks input throughout execution. Collaborative, not autonomous.

**CEX mapping**: `/guide` + `/plan` + `/spec` workflow. CEX's GDP (Guided Decision Protocol) serves the same purpose -- plan first, get user approval, then execute. Coze calls it "Planning Mode"; CEX calls it "co-pilot mode".

### 2.9 Card

Structured UI response format. Cards display titles, descriptions, images, and action buttons. Used for rich bot responses that go beyond plain text (restaurant recommendations, product listings, etc.). Data-bound to API responses.

**CEX mapping**: `output_template` (P05). CEX output templates define structure but lack a native "Card" UI primitive. This is a gap -- CEX artifacts are Markdown-first, not UI-component-first.

### 2.10 Database

Structured data storage accessible to bots and workflows. Users can upload CSV files that are auto-converted to cloud-hosted databases. The Database node supports NL2SQL (natural language to SQL) for read/write operations.

**CEX mapping**: No direct equivalent. CEX uses filesystem (Markdown/YAML) as its data layer. A structured database layer with NL2SQL is a significant architectural difference. Closest CEX pattern: `entity_memory` (P10) for structured entity storage, but without SQL querying.

### 2.11 Skills Marketplace (Coze 2.0)

Reusable skill modules packaged from professional expertise. Skills can be combined, shared, and monetized. Covers domains: marketing, legal, finance, education.

**CEX mapping**: `archetypes/builders/` (shared skills via ISOs). CEX's builder system is the closest analog -- each builder is a reusable "skill" with 13 components. CEX lacks a marketplace/monetization layer.

### 2.12 Persistent Planning (Coze 2.0)

Long-running autonomous plans that execute over days/weeks. The agent breaks complex objectives into tasks, executes autonomously, and provides proactive updates.

**CEX mapping**: `/mission` + `cex_mission_runner.py` + overnight loops. CEX's mission system supports multi-wave autonomous execution. Coze's "Agent Plan" is the consumer-facing equivalent.

**Agent Plan state lifecycle:**

| State | Description | Trigger |
|-------|-------------|---------|
| `draft` | Plan generated, awaiting user approval | Bot receives complex multi-step objective |
| `approved` | User reviewed and accepted plan | User clicks "Approve" or sends confirmation |
| `executing` | Bot autonomously executing task queue | After approval |
| `paused` | Waiting for user input at a Question node | Bot hits ambiguity requiring human decision |
| `completed` | All tasks finished, final report sent | All subtasks resolved |
| `failed` | Unrecoverable error | Tool timeout, permission denied, model error |

Key implementation characteristics:
- Plans survive session boundaries (state persisted server-side)
- Proactive push notifications when milestones complete
- Strategy adaptation on feedback: if a subtask fails, the planner re-decomposes
- Integration with Coze Skills: each plan step can invoke a marketplace skill module

**Comparison vs CEX mission runner:**

| Dimension | Coze Agent Plan | CEX cex_mission_runner.py |
|-----------|----------------|--------------------------|
| Persistence | Cross-session (cloud DB) | In-process (wave polling) |
| Human gate | Question node (mid-plan) | GDP at F4 (pre-execution) |
| Proactive updates | Push notifications | git log + signal polling |
| Failure recovery | Re-decompose subtask | Quality gate retry (max 2) |
| Session scope | Unlimited (days/weeks) | Session-scoped (hours) |

### 2.13 Coze Studio Self-Hosting Architecture

Open-sourced July 25, 2025 under Apache 2.0. Coze Studio is the self-hosted edition of the Coze platform.
Source: https://test-news.aibase.com/news/19989

**Technology stack:**

| Layer | Technology |
|-------|-----------|
| Backend | Go + Hertz framework (microservices, DDD) |
| Frontend | React + TypeScript monorepo (Rush + PNPM) |
| Data | PostgreSQL/MySQL + Redis + Elasticsearch |
| Deployment | Docker Compose (coze-server + db + redis + elasticsearch) |
| Min hardware | 2 cores, 4 GB RAM |

**Service decomposition (Docker Compose):**
```
coze-server   -- Main application server (Go/Hertz)
db            -- Relational database (PostgreSQL)
redis         -- Session + cache layer
elasticsearch -- Knowledge base full-text + vector search
```

**Coze Loop** (co-released): Evaluation and testing harness for bots. Provides dataset-driven batch testing, quality scoring, and regression tracking. Closest CEX equivalent: `cex_score.py` + `cex_quality_monitor.py`.

**CEX mapping**: CEX has no self-hosting web UI. Coze Studio fills the "visual workflow editor" gap that CEX's YAML-first approach leaves open. The DDD microservices architecture mirrors CEX's pillar-based separation of concerns.

### 2.14 Plugin Development API

Coze defines a **Plugin** as a named collection of **Tools**. Each Tool is one API endpoint.
Source: https://docs.coze.com/guides/plugin_tools

**Plugin creation flow:**
1. Register plugin (name, description, icon)
2. Add tools -- each tool maps to one REST endpoint (URL + method + auth)
3. Define input/output schema (JSON Schema)
4. Set auth: none / API key / OAuth2

**Local Plugin via API** (self-hosted / test mode):
- Run a local HTTP server that Coze calls via ngrok tunnel or public URL
- Allows testing tools locally before publishing to Plugin Store
- Auth via shared secret header
- Source: https://docs.coze.com/guides/use_local_plugin

**Python SDK (`coze-py`) -- programmatic access:**
Source: https://github.com/coze-dev/coze-py

```python
from cozepy import Coze, TokenAuth

client = Coze(auth=TokenAuth(token="PAT_xxx"), base_url="https://api.coze.com")

# Trigger a workflow run
run = client.workflows.runs.create(
    workflow_id="wf_xxx",
    parameters={"input": "user text"}
)

# Stream chat with a bot
for event in client.chat.stream(
    bot_id="bot_xxx",
    user_id="user_001",
    additional_messages=[{"role": "user", "content": "analyze this"}]
):
    print(event.message.content)
```

**CEX mapping**: `api_client` (P04) + `mcp_server` (P04). The Plugin auth model (API key / OAuth2 / local) is richer than CEX's current MCP auth pattern. `coze-py` is the programmatic surface CEX nuclei would use to call Coze bots as tools.

## 3. XAgent -- Core Concepts

### 3.1 Dispatcher

Dynamic task routing layer. Instantiates appropriate agent types based on task characteristics. Enables extensibility -- new agent types can be added without modifying core infrastructure.

**CEX mapping**: N07 orchestrator + `cex_router.py`. CEX's dispatch is nucleus-based (N01-N06 by domain); XAgent's Dispatcher is more dynamic (agent type by task characteristics). CEX routes by domain taxonomy; XAgent routes by task analysis.

### 3.2 Planner (Outer Loop)

High-level strategic planning. Decomposes complex objectives into subtasks, establishes milestones, and manages the overall problem-solving sequence. Operates the **outer loop** -- the supervisory layer that mirrors human strategic thinking.

| Planner capability | XAgent | CEX equivalent |
|--------------------|--------|----------------|
| Task decomposition | Subtasks + milestones | `/plan` + mission waves |
| Plan refinement | Iterative based on execution feedback | `/consolidate` + re-dispatch |
| Progress tracking | Milestone completion | Signal watch + git log polling |
| Failure recovery | Re-plan on subtask failure | Quality gate retry (F7, max 2) |

**CEX mapping**: `/plan` + `/spec` + wave planning in N07. CEX's planning is currently less formalized than XAgent's -- CEX plans are Markdown specs, while XAgent has structured plan objects with milestones.

### 3.3 Actor (Inner Loop)

Tactical execution layer. Operates the **inner loop** -- focused on granular task execution using ToolServer resources. The Actor uses ReACT-style reasoning (Reason-Act-Observe) to solve individual subtasks.

**CEX mapping**: Individual nucleus (N01-N06) executing 8F pipeline on a single artifact. The 8F pipeline (F1-F8) is CEX's equivalent of the Actor's inner loop -- constrain, reason, produce, validate.

### 3.4 Dual-Loop Mechanism

The defining architectural pattern. Two nested control loops:

```
OUTER LOOP (Planner)
  |-- Decompose task into subtasks
  |-- Set milestones
  |-- Monitor inner loop results
  |-- Refine plan based on feedback
  |
  +-- INNER LOOP (Actor) [per subtask]
        |-- Receive subtask from Planner
        |-- ReACT: Reason -> Act -> Observe
        |-- Use ToolServer tools
        |-- Report result to Planner
        |-- If stuck: AskForHumanHelp
```

**CEX mapping**: CEX has an analogous but differently structured dual loop:

| Loop level | XAgent | CEX |
|------------|--------|-----|
| Outer | Planner: decompose + milestone + refine | N07: /plan + wave dispatch + consolidate |
| Inner | Actor: ReACT + tools + report | Nucleus: 8F pipeline (F1-F8) + signal |
| Feedback | Actor result -> Planner refinement | Signal + git commit -> N07 polling |
| Human gate | AskForHumanHelp tool | GDP NeedsUserDecision (F4) |

Key difference: XAgent's loops are in-process (same runtime); CEX's loops are inter-process (filesystem + git + signals).

**Dual-Loop State Machine (formal):**

```
OUTER LOOP (Planner)
  States: INIT -> DECOMPOSING -> PLANNING -> DISPATCHING -> MONITORING -> REFINING -> COMPLETE | FAILED

  INIT
    -> DECOMPOSING   (task received)

  DECOMPOSING
    -> PLANNING      (subtasks + milestones generated)

  PLANNING
    -> DISPATCHING   (subtask queue ready)

  DISPATCHING
    -> MONITORING    (Actor activated for next subtask)

  MONITORING
    -> DISPATCHING   (Actor reported subtask success, more subtasks remain)
    -> REFINING      (Actor reported subtask failure)
    -> COMPLETE      (all subtasks succeeded)
    -> FAILED        (max retries exceeded or unrecoverable error)

  REFINING
    -> PLANNING      (re-decompose around failed subtask)
    -> FAILED        (refinement not possible)

INNER LOOP (Actor) -- per subtask
  States: IDLE -> REASONING -> ACTING -> OBSERVING -> REPORTING | ASKING

  IDLE
    -> REASONING     (subtask received from Planner)

  REASONING  [Thought step in ReACT]
    -> ACTING        (tool selected, arguments formed)
    -> ASKING        (insufficient info detected)
    -> REPORTING     (answer directly available, no tool needed)

  ACTING  [Action step in ReACT]
    -> OBSERVING     (tool call executed)

  OBSERVING  [Observation step in ReACT]
    -> REASONING     (observation processed, continue loop)
    -> REPORTING     (task solved)

  REPORTING
    -> IDLE          (result returned to Planner)

  ASKING  [AskForHumanHelp]
    -> REASONING     (human response received as Observation)
```

**Inner loop max iterations**: configurable via `max_iter` in XAgent config (default: 10 per subtask). After max_iter, Actor reports failure to Planner.

### 3.5 ToolServer

Containerized tool execution environment. Five tool categories:

| Tool | Purpose | CEX equivalent |
|------|---------|----------------|
| File Editor | Text/file manipulation | Native filesystem access |
| Python Notebook | Code execution + visualization | `cli_tool` (P04) / inline code |
| Web Browser | Information retrieval | `browser_tool` (P04) / MCP |
| Shell | System command execution | Bash tool (native) |
| Rapid API | External API integration | `api_client` (P04) / MCP servers |

**CEX mapping**: CEX nuclei have direct tool access (Claude Code's native tools + MCP servers). XAgent's Docker containerization provides stronger isolation. CEX's safety model relies on git (rollback) rather than containers (isolation).

### 3.5a ToolServer Docker Implementation (Deep Dive)

Source: https://xagent-doc.readthedocs.io/en/latest/source/ToolServer/README.html
Source: https://github.com/OpenBMB/XAgent/blob/main/ToolServer/README.md

**Three-tier containerized architecture:**

```
ToolServerManager   (port 8090)
  -- Creates/manages ToolServerNode instances per XAgent session
  -- Exposes REST API: POST /get_toolserver (allocate node), DELETE /release (free node)
  -- Reads manager.yml for node lifecycle config
  |
  +-- ToolServerNode (one Docker container per Agent session)
  |     -- Provides isolated execution environment
  |     -- Exposes the 5 tool endpoints (file/notebook/browser/shell/rapidapi)
  |     -- node.privileged: true (default) enables nested Docker-in-Docker
  |
  +-- ToolServerMonitor
        -- Polls node health at configurable interval
        -- Auto-removes idle nodes after idling_close_minutes (default: 30)
        -- Prevents resource leak from abandoned sessions
```

**Docker Compose service map:**

| Service | Image | Role |
|---------|-------|------|
| `toolserver_manager` | `xagent/toolserver-manager` | Node lifecycle manager |
| `toolserver_monitor` | `xagent/toolserver-monitor` | Health + idle cleanup |
| `toolserver_node` | `xagent/toolserver-node` | Tool execution sandbox |

**Configuration files (assets/config/):**

| File | Key settings |
|------|-------------|
| `manager.yml` | `node.privileged` (Docker-in-Docker), `node.image`, `node.mem_limit` |
| `monitor.yml` | `idling_close_minutes`, `poll_interval_seconds` |
| `node.yml` | `api_keys.bing_search`, `api_keys.rapid_api`, timeout overrides |
| `docker-compose.yml` | `-t <seconds>` on ToolServerManager command = API timeout |

**Security note (CVE-2026-3954):** Path traversal vulnerability in ToolServerNode's `/upload_file` endpoint allows arbitrary file write outside the container filesystem. Mitigation: disable `node.privileged`, pin to patched image version, restrict network egress.

**Lifecycle sequence:**

```
XAgent startup
  -> POST ToolServerManager /get_toolserver
  -> Manager spawns ToolServerNode container
  -> Node registers with Manager, returns endpoint URL
  -> Actor uses Node URL for all tool calls during session
  -> Session ends or idle timeout
  -> Monitor detects idle -> DELETE /release
  -> Manager kills + removes Node container
```

**CEX mapping**: CEX nuclei run in the host process with no container isolation. The ToolServer pattern (one sandbox per session) would map to one Docker container per nucleus dispatch. CEX could adopt this for production deployments to prevent nucleus tool calls from affecting host state.

### 3.6 AskForHumanHelp

Explicit human-in-the-loop tool. When the Actor encounters insufficient information or ambiguous scenarios, it can invoke `AskForHumanHelp` to request guidance rather than proceeding with guesses.

**Protocol implementation:**

The tool is a standard XAgent tool, callable like any ToolServer tool. When invoked:
1. Actor pauses inner loop execution
2. System presents question to human via web UI or CLI prompt
3. Human types response (no timeout -- waits indefinitely)
4. Response is injected as an Observation into the ReACT loop
5. Actor resumes from the Observation step

**Typical information elicited:**
- Preferred location / region ("Which city should I search in?")
- Budget constraints ("What is your maximum budget?")
- Culinary / preference details ("Do you have dietary restrictions?")
- Ambiguous specification ("Did you mean the Python library or the CLI tool?")

**NOT used for:** capability failures (tool errors, model refusals) -- those trigger retry logic, not human help.

**CEX mapping**: GDP (Guided Decision Protocol). CEX's F4 REASON step includes a `NeedsUserDecision` gate that halts the pipeline when subjective decisions are required. The key difference: XAgent's human help is reactive (ask when stuck); CEX's GDP is proactive (ask before building).

| Dimension | XAgent AskForHumanHelp | CEX GDP |
|-----------|------------------------|---------|
| Trigger | Actor stuck / ambiguous (reactive) | F4 detects subjective decision (proactive) |
| Timing | During execution | Before execution |
| Scope | Single subtask | Entire mission (decision manifest) |
| Persistence | Per-session only | `decision_manifest.yaml` (persisted) |
| Resume mechanism | Observation injected into ReACT | Nucleus continues after GDP gate clears |
| Who initiates | Actor autonomously | N07 enforces before dispatch |

## 4. Unique Concepts Not in CEX

### 4.1 From Coze

| Concept | Description | CEX gap / opportunity |
|---------|-------------|----------------------|
| **NL2SQL Database node** | Natural language queries against structured databases | CEX is filesystem-only. Adding a DB layer with NL2SQL would enable structured analytics. |
| **Card UI primitive** | Rich structured response components (title, image, CTA) | CEX output is Markdown-first. Cards would enhance P05 output kinds for web/app delivery. |
| **Skills Marketplace** | Monetizable reusable skill modules with Plugin Store | CEX builders are reusable but not marketplace-ready. `coze-py` SDK enables programmatic integration. |
| **Message node (mid-workflow streaming)** | Output to user during workflow execution | CEX workflows run to completion. Mid-stream user feedback is a gap. |
| **Question node (mid-workflow user input)** | Pause workflow for user input | GDP only gates at F4. A per-node pause/resume would add flexibility. |
| **Intent Recognition node** | Built-in NLU classification within workflows | CEX has `cex_intent_resolver.py` but not as a composable workflow node. |
| **Persistent Planning (Agent Plan)** | Days/weeks-long plans with 6-state lifecycle (draft/approved/executing/paused/completed/failed) | CEX missions are session-scoped. True persistent plans need state serialization + push notifications. |
| **Coze Studio self-hosting** | Go/Hertz backend, React+TS frontend, Docker Compose (4 services) | CEX has no web UI. Studio fills the visual workflow editor gap entirely. |
| **Plugin auth model** | Three-mode: none / API key / OAuth2 + local test via ngrok | CEX MCP auth is simpler. OAuth2 support would unlock enterprise integrations. |

### 4.2 From XAgent

| Concept | Description | CEX gap / opportunity |
|---------|-------------|----------------------|
| **Formal Dual-Loop state machine** | 7-state outer loop (INIT->DECOMPOSING->PLANNING->DISPATCHING->MONITORING->REFINING->COMPLETE) + 6-state inner loop (IDLE->REASONING->ACTING->OBSERVING->REPORTING/ASKING) | CEX has an implicit dual loop (N07 + nuclei) but no formal state machine with named transitions. |
| **Dynamic Dispatcher** | Route by task analysis, not fixed domain | CEX routes by pillar/nucleus domain. Dynamic routing by task complexity/type would improve flexibility. |
| **Containerized ToolServer** | Three-tier Docker: Manager + Monitor (auto-cleanup) + Node (per-session sandbox) | CEX tools run in host environment. Manager+Monitor pattern would prevent resource leaks from orphaned nuclei. |
| **Milestone protocol** | Structured progress checkpoints within plans | CEX uses git commits as implicit milestones. Explicit milestone objects would improve observability. |
| **ReACT inner loop** | Formal Reason-Act-Observe cycle per subtask, max_iter configurable | CEX's 8F is richer (8 steps vs 3) but less iterative. ReACT's observe-and-retry is more adaptive. |
| **Reactive AskForHumanHelp** | Mid-execution HITL: pauses ReACT, injects human answer as Observation | CEX GDP is proactive (pre-execution). Reactive mid-execution pause complements but does not replace GDP. |
| **ToolServer session isolation** | One Docker container per agent session; idle cleanup via Monitor | CEX nuclei share host environment. Session isolation would prevent cross-nucleus state contamination. |

## 5. Architecture Comparison

```
COZE                              XAGENT                           CEX
====                              ======                           ===
Bot                               --                               agent (P02)
  +-- Prompt                        Dispatcher                     N07 orchestrator
  +-- Plugin                          |                              |
  +-- Workflow (13 nodes)            Planner (outer loop)           /plan + /spec
  |     +-- LLM Node                   |                             |
  |     +-- Code Node                Actor (inner loop)             Nucleus (8F)
  |     +-- Knowledge Node             |                             |
  |     +-- Database Node            ToolServer                    MCP + native tools
  |     +-- Condition/Loop             |                             |
  +-- Knowledge Base                AskForHumanHelp                GDP (F4)
  +-- Memory                         |                              |
  +-- Card (output)               Result -> Planner refine        Signal -> N07 consolidate
  |
  Multi-Agent Mode                                                 Grid dispatch
    +-- Jump Conditions                                            Intent resolution
    +-- Supervisor Bot                                             N07 orchestrator
```

## 6. Lessons for CEX

### 6.1 Absorb from Coze

1. **Workflow node diversity**: CEX workflows need typed nodes (LLM, Code, Knowledge, Database, Condition, Loop, Message, Question). Current YAML-only workflows lack composable node types.
2. **Mid-execution user interaction**: The Question node pattern (pause-for-input) could extend GDP beyond F4 to any pipeline step.
3. **NL2SQL for structured data**: Adding a database layer would unlock analytics use cases that filesystem artifacts cannot serve.
4. **Card output format**: A `card` kind in P05 for structured UI responses would bridge the gap between Markdown artifacts and interactive frontends.

### 6.2 Absorb from XAgent

1. **Formalize the dual loop**: Name CEX's existing pattern explicitly. N07 wave dispatch = outer loop. Nucleus 8F = inner loop. Add milestone objects.
2. **Dynamic routing**: Enhance `cex_router.py` to consider task complexity, not just domain, when selecting a nucleus.
3. **Container isolation**: For production deployments, wrap nucleus tool execution in Docker containers (ToolServer pattern).
4. **Reactive human help**: Complement GDP's proactive decisions with a reactive "AskForHumanHelp" tool that nuclei can invoke mid-execution when stuck.

## 7. Term Mapping (Quick Reference)

| Coze term | XAgent term | CEX term | Industry term |
|-----------|-------------|----------|---------------|
| Bot | -- | agent (P02) | Agent |
| Plugin | Tool (ToolServer) | cli_tool / mcp_server (P04) | Tool |
| Workflow | -- | workflow (P12) | DAG / Pipeline |
| Knowledge Base | -- | rag_source + chunk_strategy (P01) | RAG Knowledge Store |
| Multi-Agent Mode | -- | Grid dispatch | Multi-agent orchestration |
| Exploration Mode | -- | /build (direct) | Reactive execution |
| Planning Mode | Planner (outer loop) | /plan + /guide | Plan-then-execute |
| Card | -- | output_template (P05) | Rich message / Adaptive Card |
| Database | -- | (gap) | Structured data store |
| LLM Node | -- | prompt_template (P03) | LLM invocation node |
| -- | Dispatcher | N07 + cex_router.py | Task router / Orchestrator |
| -- | Planner | /plan + /spec | Strategic planner |
| -- | Actor | Nucleus (N01-N06) | Task executor |
| -- | ToolServer | MCP servers + native tools | Sandboxed tool runtime |
| -- | Dual-Loop | N07 waves + 8F pipeline | Hierarchical control loop |
| -- | AskForHumanHelp | GDP NeedsUserDecision | Human-in-the-loop |
| Jump Condition | -- | Intent resolution (F1) | Routing predicate |
| Skills Marketplace | -- | Builder archetypes | Skill marketplace |
| Persistent Planning | -- | /mission + overnight | Long-horizon planning |
| Question Node | -- | GDP gate (F4) | Interactive breakpoint |
| Message Node | -- | (gap) | Streaming mid-output |

## 8. Maturity Assessment

| Dimension | Coze | XAgent | CEX |
|-----------|------|--------|-----|
| Visual workflow authoring | 9/10 (native) | 2/10 (CLI-only) | 3/10 (YAML-defined) |
| Multi-agent orchestration | 8/10 (built-in) | 4/10 (Dispatcher) | 7/10 (grid dispatch) |
| Tool ecosystem | 8/10 (Plugin Store) | 6/10 (ToolServer) | 6/10 (MCP + native) |
| Human-in-the-loop | 7/10 (Question node + Planning Mode) | 7/10 (AskForHumanHelp) | 8/10 (GDP + manifest) |
| Autonomous execution | 7/10 (Persistent Planning) | 8/10 (dual-loop) | 7/10 (mission runner) |
| Quality pipeline | 3/10 (no formal scoring) | 3/10 (no formal scoring) | 9/10 (8F + 3-layer scoring) |
| Typed knowledge | 4/10 (Knowledge Base) | 2/10 (ad-hoc) | 9/10 (130 kinds, schemas) |
| Safety / isolation | 5/10 (cloud SaaS) | 8/10 (Docker containers) | 4/10 (host + git rollback) |
| Open-source maturity | 6/10 (Studio July 2025) | 5/10 (dormant since 2024) | 5/10 (private) |

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 |
| Domain | intelligence / competitive analysis |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
