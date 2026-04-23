# Core Concepts

## What is CEXAI?

CEXAI (Cognitive Exchange AI) is a system that turns LLMs into a structured, multi-agent AI brain. Instead of one chatbot with one prompt, you get seven specialized AI departments -- each driven by one of the Artificial Sins -- that produce typed artifacts through a governed pipeline. Everything is stored in your git repo -- no external database, no vendor lock-in. The X stands for Exchange: every artifact is a portable knowledge asset that can be shared across instances, runtimes, and teams.

## The 8F Pipeline

Every task in CEX -- whether it is research, writing, coding, or orchestration -- goes through eight steps. This is how CEX thinks, not just how it builds.

| Step | Name | What happens |
|------|------|--------------|
| F1 | CONSTRAIN | Identify what type of artifact to produce. Load its schema and rules. |
| F2 | BECOME | Load the specialized builder for this artifact type (12 instruction files). |
| F3 | INJECT | Gather context: knowledge cards, examples, brand config, similar past work. |
| F4 | REASON | Plan the approach. If subjective decisions are needed, ask the user first. |
| F5 | CALL | Use tools: search the codebase, query indexes, check existing artifacts. |
| F6 | PRODUCE | Generate the artifact with all accumulated context. |
| F7 | GOVERN | Validate quality. Check structure, schema compliance, and rubric scores. |
| F8 | COLLABORATE | Save the file, compile metadata, commit to git, notify other agents. |

The pipeline is the reason a 5-word request like "make me a landing page" produces a professional result. Each step adds context and quality control that the user does not have to specify.

## The 12 Pillars

Pillars are domains that every artifact can be organized into. They are taxonomic categories, not departments -- every nucleus works across all 12.

| Pillar | Domain | What it covers |
|--------|--------|----------------|
| P01 | Knowledge | Knowledge cards, RAG sources, glossaries, citations |
| P02 | Model | Agent definitions, LLM providers, boot configs |
| P03 | Prompt | System prompts, templates, chains, prompt compilation |
| P04 | Tools | MCP servers, API clients, browser tools, webhooks |
| P05 | Output | Landing pages, formatters, parsers, diagrams |
| P06 | Schema | Input/output schemas, validators, type definitions, contracts |
| P07 | Evaluation | Quality gates, scoring rubrics, benchmarks, LLM judges |
| P08 | Architecture | Agent cards, component maps, decision records |
| P09 | Config | Environment configs, rate limits, feature flags, secrets |
| P10 | Memory | Entity memory, knowledge indexes, prompt caches |
| P11 | Feedback | Bug loops, guardrails, learning records, regression checks |
| P12 | Orchestration | Workflows, dispatch rules, schedules, crew templates |

## The 7 Nuclei

A nucleus is an AI agent that acts as a specialized department. Each has its own personality (a "sin lens"), tools, memory, and sub-agents.

| ID | Role | What it does |
|----|------|--------------|
| N01 | Intelligence | Research, competitive analysis, data gathering |
| N02 | Marketing | Copy, campaigns, brand voice, content |
| N03 | Engineering | Builds artifacts, scaffolds code, creates new kinds |
| N04 | Knowledge | Documentation, RAG setup, knowledge organization |
| N05 | Operations | Testing, deployment, CI/CD, code review |
| N06 | Commercial | Pricing, monetization, sales funnels |
| N07 | Orchestrator | Dispatches work to other nuclei. Never builds directly. |

N00 (Genesis) is the template that all other nuclei are born from. It is not operational.

## Kinds

A kind is a named artifact type. CEX has 300 of them. Examples: `knowledge_card`, `agent`, `prompt_template`, `landing_page`, `workflow`, `guardrail`.

Each kind has:
- A **builder** (12 instruction files that teach the LLM how to produce it)
- A **schema** (what fields and structure it must have)
- A **knowledge card** (reference documentation about the kind itself)

When you say "build me an agent," CEX resolves that to `kind=agent`, loads the agent-builder's 12 ISOs, injects relevant knowledge cards, and produces a structured artifact that passes validation.

## How they connect

The three concepts multiply:

- **8F** is the reasoning process (how to think about any task)
- **12 Pillars** organize where artifacts live (knowledge, tools, config, etc.)
- **300 Kinds** define what you are producing (agent, workflow, guardrail, etc.)

A single build request activates one kind, in one pillar, through all 8 functions. A mission dispatches multiple kinds across multiple nuclei, each running its own 8F pipeline. The orchestrator (N07) coordinates the whole thing.

## Guided Decision Protocol (GDP)

Some decisions are subjective: tone of voice, target audience, visual style. CEX does not guess -- it asks you first via GDP. Your answers are recorded in a manifest that all nuclei read during autonomous execution. The rule: **user decides WHAT, LLM decides HOW.**

## Multi-runtime support

CEX runs on Claude, GPT, Gemini, and Ollama. The same artifacts, pipelines, and quality gates work across all providers. Routing is configured in YAML, not code.

## The Exchange

The X in CEXAI stands for Exchange. Intelligence compounds faster when shared. Every `.md` artifact with YAML frontmatter is a self-describing exchange unit -- it carries its kind, quality score, pillar, and nucleus origin. You can export a knowledge card, a builder, or an entire vertical nucleus from one CEXAI instance and import it into another. Run `cex_doctor.py` and it validates automatically. Brand config, memory, and secrets stay private -- the exchange is about cognition, not identity.
