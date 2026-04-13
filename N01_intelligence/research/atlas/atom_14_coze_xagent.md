---
id: atom_14_coze_xagent
kind: knowledge_card
pillar: P01
quality: null
density_score: 0.91
title: "Atomic Research 14: Coze (ByteDance) + XAgent (Tsinghua/OpenBMB)"
version: 1.0.0
author: N01
tags: [coze, xagent, bytedance, tsinghua, openbmb, multi-agent, workflow, dual-loop, atlas]
tldr: "Coze is ByteDance's visual agent platform with 13 workflow node types, multi-agent orchestration, and persistent planning. XAgent is Tsinghua/OpenBMB's autonomous agent with a Dispatcher-Planner-Actor triad and dual-loop (outer=planning, inner=execution) mechanism. Both contribute novel patterns CEX can absorb."
domain: intelligence
created: 2026-04-13
updated: 2026-04-13
sources:
  - https://github.com/coze-dev/coze-studio
  - https://github.com/OpenBMB/XAgent
  - https://aixsociety.com/bytedances-coze-2-0-transforming-ai-from-chat-tool-to-intelligent-work-partner/
  - https://blog.x-agent.net/blog/xagent/
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

### 3.6 AskForHumanHelp

Explicit human-in-the-loop tool. When the Actor encounters insufficient information or ambiguous scenarios, it can invoke `AskForHumanHelp` to request guidance rather than proceeding with guesses.

**CEX mapping**: GDP (Guided Decision Protocol). CEX's F4 REASON step includes a `NeedsUserDecision` gate that halts the pipeline when subjective decisions are required. The key difference: XAgent's human help is reactive (ask when stuck); CEX's GDP is proactive (ask before building).

| Dimension | XAgent AskForHumanHelp | CEX GDP |
|-----------|------------------------|---------|
| Trigger | Actor stuck / ambiguous | F4 detects subjective decision |
| Timing | During execution (reactive) | Before execution (proactive) |
| Scope | Single subtask | Entire mission (decision manifest) |
| Persistence | Per-session | `decision_manifest.yaml` (persisted) |

## 4. Unique Concepts Not in CEX

### 4.1 From Coze

| Concept | Description | CEX gap / opportunity |
|---------|-------------|----------------------|
| **NL2SQL Database node** | Natural language queries against structured databases | CEX is filesystem-only. Adding a DB layer with NL2SQL would enable structured analytics. |
| **Card UI primitive** | Rich structured response components (title, image, CTA) | CEX output is Markdown-first. Cards would enhance P05 output kinds for web/app delivery. |
| **Skills Marketplace** | Monetizable reusable skill modules | CEX builders are reusable but not marketplace-ready. Distribution model exists in spec but no runtime. |
| **Message node (mid-workflow streaming)** | Output to user during workflow execution | CEX workflows run to completion. Mid-stream user feedback is a gap. |
| **Question node (mid-workflow user input)** | Pause workflow for user input | GDP only gates at F4. A per-node pause/resume would add flexibility. |
| **Intent Recognition node** | Built-in NLU classification within workflows | CEX has `cex_intent_resolver.py` but not as a composable workflow node. |
| **Persistent Planning** | Days/weeks-long autonomous plans with proactive updates | CEX missions are session-scoped. True persistent plans (across sessions) need state serialization. |

### 4.2 From XAgent

| Concept | Description | CEX gap / opportunity |
|---------|-------------|----------------------|
| **Explicit Dual-Loop** | Formal inner/outer loop separation with milestone tracking | CEX has an implicit dual loop (N07 + nuclei) but no formal milestone protocol. |
| **Dynamic Dispatcher** | Route by task analysis, not fixed domain | CEX routes by pillar/nucleus domain. Dynamic routing by task complexity/type would improve flexibility. |
| **Containerized ToolServer** | Docker-isolated tool execution | CEX tools run in host environment. Container isolation would improve safety for untrusted operations. |
| **Milestone protocol** | Structured progress checkpoints within plans | CEX uses git commits as implicit milestones. Explicit milestone objects would improve observability. |
| **ReACT inner loop** | Formal Reason-Act-Observe cycle per subtask | CEX's 8F is richer (8 steps vs 3) but less iterative. ReACT's observe-and-retry is more adaptive. |

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
