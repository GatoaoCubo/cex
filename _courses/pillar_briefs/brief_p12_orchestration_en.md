---
quality: 8.1
id: kc_pillar_brief_p12_orchestration_en
kind: knowledge_card
pillar: P12
title: "P12 Orchestration — Your AI's Conductor"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p12, orchestration, multi-agent, crew, workflow, swarm, llm-engineering]
tldr: "P12 Orchestration is the coordination layer for multi-agent AI systems — workflows, DAGs, crews, swarms, handoffs, signals, and dispatch rules that compose individual agents into coherent systems that produce more than any single agent can."
source_concepts: [kc_lens_index, mentor_context]
related:
  - kc_pillar_brief_p12_orchestration_pt
  - kc_pillar_brief_p08_architecture_en
  - kc_pillar_brief_p11_feedback_en
  - kc_pillar_brief_p02_model_en
  - n00_p12_kind_index
density_score: 0.89
updated: "2026-04-22"
---

# P12 Orchestration — Your AI's Conductor: How Multiple Agents Coordinate to Produce a Symphony

---

## The Universal Principle: One Agent Is a Soloist. Many Agents Are an Orchestra.

There is a ceiling to what a single AI agent can produce, no matter how capable the underlying model. The ceiling is not intelligence — it is **attention span.** A single agent with a 200K context window can handle complex single-domain tasks with remarkable depth. But ask it to simultaneously research competitors, write marketing copy, design a landing page, configure infrastructure, and draft a pricing strategy — and you will observe exactly what happens when a soloist tries to perform all the parts of a symphony at once: chaos, or shallow coverage.

Orchestration is the engineering discipline that breaks the single-agent ceiling. The conductor metaphor is exact: the conductor does not play any instrument. The conductor coordinates the sections — ensuring the strings come in on cue, the brass do not drown out the woodwinds, the tempo accelerates precisely where the score demands. The result is a coherent whole that no individual instrument could produce.

P12 Orchestration is the systematic engineering of that conductor layer. It provides the building blocks for composing individual agents (each excellent at their domain) into coherent multi-agent systems that produce emergent capabilities — outputs that emerge from the interaction between agents rather than from any single agent's capability.

This is the future of AI engineering, and it is not a distant future. **Multi-agent patterns are already live in production:**

- **LangChain's LangGraph** — stateful multi-agent workflows with conditional edges
- **AutoGen** — conversational multi-agent programming
- **CrewAI** — role-based agent crews with sequential/hierarchical/consensus topologies
- **OpenAI Assistants with handoffs** — structured agent-to-agent transfer
- **Anthropic's multi-agent guidance** — orchestrator + subagent patterns
- **Google's ADK** — agent development kit with supervisor patterns
- **Microsoft's Semantic Kernel** — planner + executor multi-agent coordination

P12's 16 kinds give these patterns canonical names and systematic relationships. The orchestration patterns are universal — they work with any underlying LLM, any agent framework, any deployment environment.

**The critical insight:** orchestration is not about making agents "smarter." It is about **specialization + coordination.** A researcher agent that does nothing but research is far more effective at research than a generalist agent. An orchestrator that does nothing but coordinate is far more effective at coordination than a jack-of-all-trades. The performance improvement from specialization is multiplicative, not additive.

---

## What This Pillar Does

P12 Orchestration addresses five core multi-agent engineering challenges:

**Challenge 1: Defining work units** — What does one agent actually do? How is a task described, bounded, and transferred? Kinds: `handoff`, `dispatch_rule`, `signal`.

**Challenge 2: Defining coordination topology** — Do agents work sequentially, in parallel, or with manager-worker hierarchies? Kinds: `workflow`, `dag`, `crew_template`, `collaboration_pattern`, `spawn_config`.

**Challenge 3: Defining temporal triggers** — When does a workflow start? What events trigger which agents? Kinds: `schedule`, `pipeline_template`.

**Challenge 4: Maintaining state across boundaries** — What happens if an agent fails mid-workflow? How do you restart without losing progress? Kinds: `checkpoint`, `workflow_node`, `workflow_primitive`.

**Challenge 5: Scaling crews and swarms** — How do you run 50 agents producing 50 independent artifacts simultaneously? Kinds: `spawn_config`, `team_charter`, `visual_workflow`.

In the 8F pipeline, P12 artifacts map primarily to the PRODUCE (F6) and COLLABORATE (F8) functions. Orchestration artifacts are not built to sit in a knowledge base — they are built to run. A workflow is executable. A handoff is actionable. A signal is emitted and consumed. This makes P12 the most operationally dense pillar in the 12-pillar taxonomy.

---

## All 16 Kinds in P12 — Universal Capability Reference

| Kind | Universal Capability | Topology |
|------|---------------------|---------|
| `workflow` | Sequential/parallel step execution plan | Linear/branching |
| `dag` | Dependency graph (who depends on whom) | Directed acyclic graph |
| `spawn_config` | Agent group launch configuration | N agents, any topology |
| `signal` | Inter-agent completion/error notification | Point-to-point |
| `handoff` | Task + context package for agent-to-agent transfer | Point-to-point |
| `dispatch_rule` | Intent-to-agent routing rule | Router pattern |
| `checkpoint` | Workflow state snapshot for recovery | State persistence |
| `schedule` | Temporal trigger (cron, event-driven) | Time-based |
| `pipeline_template` | Scenario-indexed agent pipeline recipe | Sequential with revision loops |
| `crew_template` | Reusable multi-role team blueprint | Sequential/hierarchical/consensus |
| `team_charter` | Mission contract for a crew instance | Instance configuration |
| `visual_workflow` | GUI-based workflow editor configuration | Visual definition |
| `workflow_node` | Typed node in a workflow graph | Graph element |
| `workflow_primitive` | Step/Parallel/Loop/Condition/Router primitives | Execution primitive |
| `collaboration_pattern` | Multi-agent coordination topology definition | Pattern library |
| `renewal_workflow` | Contract renewal/lifecycle workflow | Business process |

---

## Key Engineering Patterns — Universal, Works With Any AI

### Pattern 1: The Dispatch Topology Spectrum

The single most important design decision in multi-agent systems is the coordination topology. Five options exist, each with distinct tradeoffs:

```
TOPOLOGY 1: SEQUENTIAL (pipeline)
  Agent A → Agent B → Agent C
  Use when: each step depends on the prior output
  Strength: maximum coherence, easy to debug
  Weakness: total latency = sum of all step latencies
  Example: research → write → review → publish

TOPOLOGY 2: PARALLEL (grid)
  Agent A ─┐
  Agent B ─┤→ Aggregator → Output
  Agent C ─┘
  Use when: tasks are independent and can run simultaneously
  Strength: total latency = max of parallel step latencies
  Weakness: aggregation is a single point of failure
  Example: 6 agents each building one section of a report

TOPOLOGY 3: HIERARCHICAL (manager-worker)
  Orchestrator
  ├─ Worker A
  ├─ Worker B
  └─ Worker C
  Use when: workers need dynamic direction based on intermediate results
  Strength: adaptive to intermediate discoveries
  Weakness: orchestrator becomes a bottleneck
  Example: research orchestrator directs specialized research agents

TOPOLOGY 4: CONSENSUS
  Agent A ─┐
  Agent B ─┤→ Vote/Merge → Output
  Agent C ─┘
  Use when: reducing bias through diverse perspectives
  Strength: higher quality for high-stakes decisions
  Weakness: 3x more tokens consumed than solo
  Example: 3 reviewers independently score an artifact, median wins

TOPOLOGY 5: SWARM
  N identical agents, N independent outputs
  No handoffs between agents
  Use when: coverage breadth > coherence
  Strength: embarrassingly parallel, scales linearly
  Weakness: no cross-agent coordination
  Example: 50 agents each analyze one company in a 50-company competitor list
```

**The practical decision framework:**
- 1 artifact, 1 kind → solo builder (no orchestration needed)
- N artifacts, independent → parallel grid (P12 `spawn_config`)
- 1 coherent package needing N roles → crew (P12 `crew_template`)
- N independent packages → swarm (P12 `spawn_config` with swarm mode)

**Try this now (any AI):**
Take a complex task you normally assign to a single AI session. Decompose it into 3-5 sub-tasks. Assign each sub-task to a separate AI conversation. Run them in parallel (different tabs/sessions). Compare the output quality to your single-session approach. You will observe the specialization dividend.

### Pattern 2: The Handoff Contract — Eliminating Discovery Turns

The handoff is the unit of work transfer between agents. The quality of the handoff determines whether the receiving agent spends its tokens doing work or asking clarifying questions. The principle: **everything the agent needs, nothing it should have to discover.**

```markdown
# handoff template

## Target: N03 Engineering
## Mission: FRACTAL_FILL_W3

## Task
Build 3 agent_card artifacts for N03, N04, N05. Each card documents
the nucleus's full capability inventory, tools, memory scope, and quality gates.

## Pre-loaded Context (READ THESE FIRST)
1. archetypes/builders/agent_card-builder/  (12 ISOs — your builder)
2. N03_engineering/P08_architecture/         (existing artifacts in your pillar)
3. N00_genesis/P02_model/kind_index.md      (all P02 kinds for reference)
4. .cex/kinds_meta.json                      (kind registry for validation)

## Decisions Made (do NOT re-ask)
See: .cex/runtime/decisions/decision_manifest.yaml
- Format: structured tables preferred over prose
- Language: EN
- Quality bar: 9.0

## Expected Outputs
1. N03_engineering/P08_architecture/agent_card_n03.md   (kind: agent_card)
2. N04_knowledge/P08_architecture/agent_card_n04.md     (kind: agent_card)
3. N05_operations/P08_architecture/agent_card_n05.md    (kind: agent_card)

## Commit Format
[N03] F8: agent_card: N03, N04, N05 (quality: {score})

## Signal on Complete
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', {score})"
```

The five components of a good handoff:
1. **Pre-loaded context** — exact file paths, not abstract descriptions
2. **Decision manifest** — subjective decisions already made by the user
3. **Expected outputs** — exact file paths and kinds expected
4. **Commit format** — how to structure the git commit
5. **Signal spec** — how to announce completion to the orchestrator

A handoff without any of these five forces the receiving agent to either guess or ask — both waste tokens and reduce quality.

### Pattern 3: The Crew Pattern — Specialized Roles with Handoffs

A `crew_template` defines a reusable team topology: who the roles are, in what order they execute, and what each role hands off to the next.

```yaml
# crew_template: product launch
process: sequential
roles:
  - role_name: researcher
    nucleus: n01
    goal: "research target audience, competitors, positioning"
    tools: [search_tool, knowledge_index]
    handoff_target: copywriter
    output: research_brief.md

  - role_name: copywriter
    nucleus: n02
    goal: "write launch copy based on research brief"
    tools: [brand_config, few_shot_examples]
    handoff_target: qa_reviewer
    input: research_brief.md
    output: copy_package.md

  - role_name: qa_reviewer
    nucleus: n05
    goal: "review copy against brand guidelines and quality gate"
    tools: [quality_gate, guardrail]
    handoff_target: null      # final role — signals complete
    input: copy_package.md
    output: review_report.md
```

The `process: sequential` topology means each role waits for the prior role to complete before starting. This is appropriate when role B genuinely needs role A's output to do its work. If roles are independent, use parallel topology instead.

**When crews outperform solo agents:**
- When 3+ distinct domains are required (research + writing + QA)
- When the output is a coherent package (not just independent artifacts)
- When quality improves through iterative handoff-and-review cycles
- When the task exceeds a single agent's depth at quality

**When crews add overhead without value:**
- When 1 artifact of 1 kind is needed (use solo builder)
- When all sub-tasks are independent (use grid/swarm)
- When roles do not actually consume each other's outputs

### Pattern 4: Grid of Crews — Maximum Parallelism with Maximum Coherence

The highest-leverage orchestration pattern combines parallel dispatch (grid) with internal coherence (crews):

```
N07 dispatches a grid with 3 cells:

  grid cell 1: crew(product_launch) + charter_product_A
               researcher → copywriter → QA
               
  grid cell 2: crew(product_launch) + charter_product_B  
               researcher → copywriter → QA
               
  grid cell 3: crew(product_launch) + charter_product_C
               researcher → copywriter → QA

Total concurrency:
  - 3 simultaneous crews (grid parallelism)
  - Within each crew: sequential (handoff-dependent)
  - At any moment: 3 active roles (one per crew)

Total output: 3 complete, coherent product launch packages
  in the time it would take 1 crew to produce 1 package.
```

This is the pattern that transforms overnight single-agent runs into production-scale AI factories. The bottleneck is no longer model capability or token limits — it is task definition quality and handoff contract completeness.

### Pattern 5: Signals — The Nervous System of Multi-Agent Coordination

A `signal` is the minimal viable inter-agent communication primitive: a structured event that announces state change without carrying the full output.

```json
{
  "signal_type": "complete",
  "nucleus": "n03",
  "mission": "FRACTAL_FILL_W3",
  "quality_score": 9.1,
  "artifacts_produced": [
    "N03_engineering/P08_architecture/agent_card_n03.md",
    "N04_knowledge/P08_architecture/agent_card_n04.md"
  ],
  "timestamp": "2026-04-22T14:33:21Z",
  "session_id": "sess_n07_042201"
}
```

The orchestrator polls for signals rather than maintaining live connections to all agents. This is the correct architecture for long-running multi-agent systems: the agents operate independently, signal on completion, and the orchestrator consolidates asynchronously. No blocking. No tight coupling. Agents can run on different machines, different processes, even different runtimes.

Signal taxonomy:
- `complete` — successful completion, quality score attached
- `error` — unrecoverable failure, error details attached
- `progress` — intermediate progress report (optional, for long-running tasks)
- `needs_input` — agent blocked waiting for human decision
- `warning` — completed but with concerns (below quality target)

### Pattern 6: Checkpoint-Based Recovery

Multi-agent systems fail. Networks drop. Processes crash. Models return errors. Without checkpoints, a workflow failure at step 7 of 10 means re-running all 10 steps. With checkpoints, you restart from step 7.

```yaml
# checkpoint pattern
id: ckpt_wave3_step_7
workflow_ref: wf_fractal_fill_wave3
step: 7
state:
  completed_nuclei: [n01, n02, n03]
  pending_nuclei: [n04, n05, n06]
  artifacts_produced:
    - N01_intelligence/P01_knowledge/kc_competitive_analysis.md
    - N02_marketing/P03_prompt/pt_launch_campaign.md
    - N03_engineering/P08_architecture/agent_card_n03.md
  quality_scores: {n01: 9.1, n02: 8.8, n03: 9.3}
recovery_instructions: "resume from N04; N01-N03 artifacts are committed and verified"
timestamp: "2026-04-22T11:45:00Z"
```

The checkpoint is written after each agent successfully completes and commits. On failure recovery: read the latest checkpoint, dispatch only the pending nuclei, skip the completed ones.

### Pattern 7: Pipeline Templates — Scenario-Indexed Agent Recipes

A `pipeline_template` is a pre-designed agent pipeline for a common development scenario. Unlike a `crew_template` (which defines fixed roles), a pipeline_template defines a scenario-indexed recipe with built-in revision loops:

```yaml
# pipeline_template: bug-fix scenario
id: pt_bug_fix
scenario: bug_fix
stages:
  1_triage:
    agent: diagnostic_specialist
    output: triage_report.md
    revision_loop: none
    
  2_reproduce:
    agent: test_engineer
    input: triage_report.md
    output: reproduction_case.py
    revision_loop:
      max_iterations: 3
      trigger: "test fails to reproduce bug"
      
  3_fix:
    agent: engineer
    input: [triage_report.md, reproduction_case.py]
    output: fix.diff
    revision_loop:
      max_iterations: 5
      trigger: "fix breaks existing tests"
      
  4_verify:
    agent: qa_engineer
    input: [reproduction_case.py, fix.diff]
    output: verification_report.md
    gate: "all existing tests pass + bug reproduction fails"
```

Pipeline templates encode the operational wisdom of experienced engineering teams into a reusable artifact. This is the OpenCode-Hermes pattern: instead of each AI deployment reinventing its bug-fix process, the industry converges on proven recipes.

---

## Architecture Deep Dive

### The Orchestration Stack

P12 artifacts compose into an orchestration stack with four layers:

```
LAYER 4: TEMPORAL COORDINATION
  schedule (when to run)
  pipeline_template (which scenario recipe to use)
      |
      v
LAYER 3: TEAM COORDINATION
  crew_template (role topology)
  team_charter (mission instance)
  spawn_config (how many, what mode)
      |
      v
LAYER 2: EXECUTION COORDINATION
  workflow (step sequence)
  dag (dependency graph)
  dispatch_rule (intent → agent routing)
      |
      v
LAYER 1: AGENT COMMUNICATION
  handoff (task transfer)
  signal (completion notification)
  checkpoint (state snapshot)
  workflow_node / workflow_primitive (execution atoms)
```

The data flow is top-down at start and bottom-up at completion: the schedule triggers the pipeline, which instantiates a crew, which runs a workflow, which dispatches tasks via handoffs, which agents complete and signal back up the stack.

### The Boundary Between P12 and Neighboring Pillars

| What you want | Correct pillar | Why |
|--------------|---------------|-----|
| Agent identity and capability | P02 | Who the agent is |
| How the agent decides | P03 | Chain, planning strategy |
| Agent tools and APIs | P04 | What the agent can call |
| System architecture diagrams | P08 | Static structure, not execution |
| Config for how agents run | P09 | Operating parameters |
| Quality gates on outputs | P11 | Feedback, not coordination |
| Execution coordination | P12 | This pillar |

The key distinction between P12 and P03: P03 `chain` is a prompt chain (output A becomes input B within a single agent context). P12 `workflow` is an agent chain (agent A produces an artifact that becomes the starting context for agent B — a different agent, possibly a different process, possibly a different machine).

### Why Multi-Agent Systems Outperform Single-Agent Systems

The performance advantage of well-designed multi-agent systems comes from four compounding effects:

**1. Specialization** — An agent with a 200K context window focused exclusively on research can load 10x more research context than a generalist agent splitting attention across research + writing + QA. The research output is deeper.

**2. Parallelism** — 6 specialist agents running simultaneously complete in the time one generalist agent takes. The latency improvement is not additive — it is architectural.

**3. Review loops** — When one agent's output is the input to a second agent (the reviewer), the review quality is higher than self-review. The reviewer can see errors the original agent cannot, because the reviewer has different context loaded.

**4. Accumulation** — Each agent in a pipeline adds value to the artifact. The final output has received research depth, writing quality, code correctness, and QA rigor — each from an agent that specialized in exactly that function.

The compounding math: 3 specialist agents, each at 85% quality on their domain, produce a combined output at ~95% quality (because errors in one domain are caught by the specialist in the next domain). 1 generalist agent producing 85% quality across all domains produces... 85% quality. The gap widens with complexity.

---

## Real Examples from N00_genesis

### workflow in practice

File: `N00_genesis/P12_orchestration/ex_workflow_content_factory.md`

A content factory workflow: brief → research → write → review → format → publish. Six steps, three agents (N01 for research, N02 for write, N05 for review/format). The workflow defines the sequence, the input/output contracts between steps, error handling for each step, and total timeout. This artifact is reusable — the same workflow runs for every content piece; only the charter changes.

### crew_template in practice

File: `N00_genesis/P12_orchestration/kind_crew_template/kind_manifest_n00.md`

A crew_template with process: sequential, 3 roles (researcher → copywriter → QA), memory configuration (shared entity_memory for brand facts), and isolation: worktree (each role gets its own git worktree to prevent conflicts). The template is instantiated with a `team_charter` that specifies the mission, budget, and deadline — the same template runs for every product launch.

### dag in practice

File: `N00_genesis/P12_orchestration/ex_dag_content_factory.md`

A DAG that maps the dependency structure of a content factory mission: the landing page cannot start until competitive research completes, the email sequence cannot start until the brand voice document completes, but the blog content and social media content can run in parallel once the keyword research completes. The DAG makes these dependencies explicit and enables the orchestrator to maximize parallelism without violating dependencies.

---

## Anti-Patterns — Universal Multi-Agent Engineering Mistakes

**Anti-pattern 1: Orchestrator that also builds**
The orchestrator that dispatches tasks to workers AND produces artifacts itself is doing two jobs — badly. The orchestrator's context fills with building-related content, leaving less room for coordination. The builds are shallower because the builder's context fills with coordination overhead. Separate roles completely: N07 orchestrates, N01-N06 build.

**Anti-pattern 2: Handoff without artifact references**
"Build a landing page for the product" is not a handoff — it is a vague request. A real handoff includes exact file paths for the builder to read, the decision manifest, expected output paths, and commit format. Without artifact references, the receiving agent spends half its tokens on discovery rather than production.

**Anti-pattern 3: Synchronous blocking orchestrator**
An orchestrator that dispatches a task and then blocks (waits) for that task to complete before dispatching the next one is running sequential dispatch on a system designed for parallelism. Dispatch all independent tasks, then poll for completion signals while doing other work.

**Anti-pattern 4: Missing checkpoints in long-running workflows**
A 6-agent, 2-hour workflow without checkpoints. When agent 5 fails at hour 1:45, you re-run the entire 2 hours. Write checkpoints after each successful agent completion. Recovery restarts from the last checkpoint.

**Anti-pattern 5: Grid without rate limit config**
Dispatching 6 parallel agents that all use the same API provider, without reading `rate_limit_config` first. 6 agents × 50 RPM each = 300 RPM total, hitting a provider limit of 50 RPM. The grid collapses in 429 storms. Always read P09 rate limits before dispatching P12 grids.

**Anti-pattern 6: Crew with unnecessary sequential steps**
Using `process: sequential` for steps that are actually independent. If the copywriter does not actually need the researcher's brief to start writing (they could start with a placeholder), run them in parallel and let the copywriter update their copy when the brief arrives. Unnecessary sequential execution doubles latency.

**Anti-pattern 7: Signal-free completion**
Agents that complete their work and exit without emitting a signal. The orchestrator has no way to know they are done. It either polls endlessly (inefficient) or assumes completion after a timeout (unreliable). Every agent MUST emit a completion signal — it takes 5 lines of code and is non-negotiable.

**Anti-pattern 8: Crew for single-artifact tasks**
Spinning up a 4-role crew to produce 1 knowledge card. The coordination overhead (4 agents' boot costs, handoff latency, checkpoint management) exceeds the value of the task. Crew overhead is justified only when the output is a multi-domain package.

---

## Cross-Pillar Connections

P12 is the operational hub that consumes inputs from every other pillar and produces work distributed back to those pillars:

| P12 reads from | Pillar | What it reads |
|---------------|--------|--------------|
| Agent identities | P02 | Who can be dispatched to which role |
| Rate limits | P09 | How many agents can run concurrently |
| Quality signals | P11 | Whether to proceed to next wave |
| Memory state | P10 | Session state for checkpoint recovery |
| Tool registries | P04 | Which tools each agent has access to |

| P12 writes to | Pillar | What it produces |
|--------------|--------|----------------|
| Artifacts of every kind | P01-P11 | Dispatched agents produce content in all pillars |
| Learning records | P10 | Mission outcomes feed memory |
| Incident reports | P11 | Workflow failures become incident records |

**The most critical cross-pillar insight:** P12 orchestration is the pillar that makes P01-P11 compound. Without P12, you have excellent individual tools — good knowledge cards (P01), well-designed agents (P02), powerful prompts (P03), capable tools (P04), quality gates (P11), memory systems (P10). With P12, those tools coordinate into a production AI factory that operates continuously, improves autonomously, and scales horizontally. P12 is the integration layer that transforms a collection of excellent parts into a system greater than their sum.

---

## Try This Now — P12 Exercises for Any AI System

**Exercise 1: Task Decomposition to Topology (45 minutes)**
Take a complex task you currently assign to a single AI session. Decompose it into subtasks. For each subtask: which topology applies (sequential, parallel, crew, swarm)? Draw the dependency graph. Estimate the latency improvement from parallelizing independent subtasks.

**Exercise 2: Write Your First Handoff (30 minutes)**
Write a handoff document for a task you would normally give as a vague prompt to an AI. Include: exact artifact references, decisions already made, expected outputs, commit format, signal spec. Give it to the AI. Observe the difference in response quality versus your vague prompt.

**Exercise 3: Crew Template Design (1 hour)**
Design a crew for a recurring multi-domain task in your work. Define: roles (3-4 max), topology (sequential/hierarchical/consensus), handoff contracts between roles, shared context. Write it as a YAML crew_template. Instantiate it with a team_charter for a specific instance.

**Exercise 4: Signal Audit (30 minutes)**
Audit every multi-step AI workflow you currently run. For each step: is there a completion signal? How does the next step know the prior step completed? If the answer is "I check manually," you have an automation gap. Spec a signal for each step.

**Exercise 5: Grid of Crews Design (2 hours)**
Take a task that needs to be done N times with slight variations (e.g., analyze 5 competitors, generate content for 3 market segments, onboard 4 different customer types). Design a crew template for one instance. Then design a grid that runs N instances of that crew in parallel. Estimate the time savings versus sequential solo execution.

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p12_orchestration_pt]] | sibling (PT-BR) | 1.00 |
| [[kc_pillar_brief_p02_model_en]] | upstream | 0.52 |
| [[kc_pillar_brief_p08_architecture_en]] | upstream | 0.48 |
| [[kc_pillar_brief_p11_feedback_en]] | upstream | 0.48 |
| [[kc_pillar_brief_p09_config_en]] | upstream | 0.45 |
| [[n00_p12_kind_index]] | upstream | 0.72 |
| [[n00_workflow_manifest]] | upstream | 0.58 |
| [[n00_crew_template_manifest]] | upstream | 0.55 |
| [[n00_handoff_manifest]] | upstream | 0.55 |
| [[mentor_context]] | upstream | 0.42 |
