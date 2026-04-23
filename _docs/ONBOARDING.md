# CEX Onboarding Guide

> Everything you need to understand CEX and build your first agent.

**For installation, see [QUICKSTART.md](QUICKSTART.md).**

---

## 1. What is CEX?

CEX is a typed knowledge base framework for building LLM agents. Think of it as a
compiler for AI: you write structured markdown files, and CEX validates, compiles,
and organizes them into a system any LLM can consume.

Every file in CEX follows a strict naming convention (`{layer}_{kind}_{topic}.ext`)
and contains YAML frontmatter plus a markdown body. This dual format means humans
read the `.md` and machines consume the compiled `.yaml`/`.json`.

CEX is IDE-agnostic and LLM-agnostic. It works with Claude, GPT, Gemini, local
models, or any tool that can read structured text files. No vendor lock-in.

---

## 2. Architecture

CEX has 5 layers, 12 pillars, and 8 nuclei (N00 Genesis + 7 business nuclei).

### The 5 Layers

```
L4 Root        CLAUDE.md, README.md, INDEX.md (entry points)
  |
L3 Engine      _tools/ (CLI: doctor, validate, compile, distill)
  |
L2 Instance    N01-N07 nuclei (domain-specific artifacts)
  |
L1 Schema      P01-P12 pillars (_schema.yaml + templates/ + examples/)
  |
L0 DNA         archetypes/builders/ (13 ISO files per builder type)
```

### The 12 Pillars

| ID  | Name          | What it holds                                    |
|-----|---------------|--------------------------------------------------|
| P01 | Knowledge     | Knowledge cards, RAG sources, glossary entries   |
| P02 | Model         | Agents, lenses, boot configs, mental models      |
| P03 | Prompt        | System prompts, templates, chain-of-thought      |
| P04 | Tools         | Skills, MCP servers, hooks, plugins, CLI tools   |
| P05 | Output        | Response formats, parsers, formatters            |
| P06 | Schema        | Input schemas, type definitions, validators      |
| P07 | Evals         | Unit evals, benchmarks, golden tests             |
| P08 | Architecture  | Patterns, laws, diagrams, component maps         |
| P09 | Config        | Env configs, feature flags, runtime rules        |
| P10 | Memory        | Runtime state, brain indexes, learning records   |
| P11 | Feedback      | Quality gates, guardrails, optimizers            |
| P12 | Orchestration | Workflows, DAGs, signals, handoffs               |

### The 8 Nuclei

| ID  | Domain         | Primary Pillars | Role |
|-----|----------------|-----------------|------|
| N00 | Genesis        | All (P01-P12)   | Archetype nucleus: builder definitions, pillar schemas, shared ISOs |
| N01 | Research       | P01, P07        | Intelligence, market analysis, competitor research |
| N02 | Marketing      | P03, P05        | Copywriting, campaigns, brand voice |
| N03 | Engineering    | P02, P04, P06   | Artifact construction, builders, templates |
| N04 | Knowledge Mgmt | P01, P10        | RAG, indexing, knowledge cards, taxonomy |
| N05 | Operations     | P04, P12        | Code, testing, CI/CD, deployment |
| N06 | Commercial     | P05, P09        | Pricing, courses, sales funnels |
| N07 | Administration | P08, P11, P12   | Orchestrator -- dispatches, never builds |

### How They Fit Together

Pillars define WHAT types of artifacts exist. Nuclei define WHERE domain instances
live. Builders define HOW artifacts are created (13 ISO files = factory blueprint).

---

## 3. Your First Agent

### Step 1: Find the agent builder

```bash
ls archetypes/builders/agent-builder/
```

This shows 13 ISO files that define how agents are built in CEX.

### Step 2: Read the schema

```bash
cat P02_model/_schema.yaml
```

This tells you the required fields, constraints, and naming rules for agents.

### Step 3: Read the generator

```bash
cat P02_model/_generator.md
```

The generator gives step-by-step instructions for creating a valid agent artifact.

### Step 4: Copy a template

```bash
cp P02_model/templates/tpl_agent.md \
   N03_engineering/P02_model/agent/my_agent.md
```

### Step 5: Fill in the artifact

Edit `my_agent.md`:

```yaml
---
id: my_agent
type: agent
lp: P02
quality: 8.0
keywords: [automation, task-runner, engineering]
long_tails:
  - "automate repetitive engineering tasks"
  - "run validation pipelines"
bullets:
  - "Executes validation pipelines on demand"
  - "Reports pass/fail with structured output"
  - "Integrates with CI/CD hooks"
axioms:
  - "Validate before publish"
---
```

Then write the markdown body with the agent's purpose, capabilities, and constraints.

### Step 6: Compile and validate

```bash
python _tools/cex_compile.py --all
python _tools/validate_builder.py archetypes/builders/agent-builder/
python _tools/cex_doctor.py
```

Compile generates the `.yaml` counterpart. Validate checks ISO completeness.
Doctor confirms overall structure health.

### Step 7: Check quality

Your artifact must score >= 7.0 to be accepted:

| Score | Tier     | Status       |
|-------|----------|--------------|
| 9.5+  | Golden   | Reference    |
| 8.0+  | Skilled  | Published    |
| 7.0+  | Learning | Experimental |
| < 7.0 | Rejected | Redo         |

Density must be >= 0.85. No prose blocks longer than 3 lines. Bullets max 80 chars.

---

## 4. IDE Setup

### VS Code

1. Install recommended extensions: YAML, Markdown All in One
2. Open the CEX root folder as workspace
3. Use the built-in terminal for CLI tools
4. Configure `files.associations` for `.md` files with YAML frontmatter:

```json
{
  "yaml.schemas": {
    "P01_knowledge/_schema.yaml": "P01_knowledge/**/*.yaml"
  }
}
```

### JetBrains (IntelliJ, WebStorm, PyCharm)

1. Open CEX root as project
2. Install Markdown and YAML plugins (bundled by default)
3. Use Terminal tab for CLI tools
4. Mark `_tools/` as Sources Root for Python tool support

### Cursor / Windsurf / AI-Native Editors

1. Open CEX root as workspace
2. Point the AI context at `CLAUDE.md` (it describes the full architecture)
3. The AI can read schemas, generators, and examples to produce valid artifacts
4. Use `_tools/cex_doctor.py` to validate AI-generated output

### Neovim / Terminal

1. `cd` into the CEX root
2. Use `find` or `grep` to navigate (naming convention makes this fast)
3. Run CLI tools directly: `python _tools/cex_doctor.py`
4. Recommended: `fzf` for file discovery, `bat` for syntax-highlighted reading

### Any Other Editor

CEX is plain text. Any editor that handles markdown and YAML works. The key tools
are Python scripts in `_tools/` — run them from your terminal of choice.

---

## 5. How CEX Understands You

You type 5 words. CEX delivers a professional artifact. Here's the trick nobody told you about every other AI tool: **they forward your words to the LLM as-is.** That's like handing a contractor a napkin sketch and expecting a skyscraper.

CEX doesn't forward. CEX **compiles.**

### The 5-Word-to-Artifact Pipeline

```
You type:          "make me a landing page"        (5 words)
                          |
CEX resolves:      kind = landing_page
                   pillar = P05_output
                   builder = landing-page-builder (13 components)
                          |
CEX injects:       your brand voice
                   10+ knowledge sources
                   similar examples from the library
                   audience persona
                   quality constraints
                          |
CEX compiles:      ~1,200 tokens of structured context
                          |
LLM executes:     with 100% dimensional coverage
                          |
You receive:       production-ready HTML
                   responsive, accessible, SEO-tagged
                   brand-aligned, dark mode, governed
```

**Amplification ratio: 150:1.** Your 5 words became 1,200 tokens of precision.

The raw LLM fills about 5-15% of what it actually needs from your input. CEX fills the remaining 85-95% automatically -- from your brand config, from knowledge cards, from builder blueprints, from quality gates. Every gap closed. Every dimension covered.

### What happens under the hood

| Step | What CEX does | What you see |
|------|---------------|--------------|
| F1 CONSTRAIN | Resolves your intent to a kind, pillar, and schema | Nothing -- invisible |
| F2 BECOME | Loads a specialized builder with 13 components | Nothing -- invisible |
| F3 INJECT | Assembles 10+ context sources (brand, KCs, examples) | Nothing -- invisible |
| F4 REASON | Plans the optimal approach for THIS specific kind | Nothing -- invisible |
| F5 CALL | Discovers and prepares relevant tools | Nothing -- invisible |
| F6 PRODUCE | Generates with full context loaded | You see the output |
| F7 GOVERN | Runs 7 quality gates, retries if below threshold | Output is already polished |
| F8 COLLABORATE | Saves, compiles, commits, signals | File appears in your repo |

You never need to know these steps exist. You just type what you want. The pipeline does the rest.

---

## 6. What You Can Say

CEX understands natural language in English and Portuguese. No special syntax needed. Here are the 20 most powerful trigger phrases -- each one activates a different part of the system:

### Build Things

| You say | CEX does |
|---------|----------|
| "make me a landing page" | Generates production HTML: responsive, accessible, brand-aligned |
| "create an agent" | Builds a complete agent definition with identity, tools, and constraints |
| "write a prompt template" | Produces a reusable prompt with variables, few-shot examples, and guardrails |
| "build an MCP server" | Scaffolds a Model Context Protocol server with endpoints and handlers |
| "design a workflow" | Creates an orchestration pipeline with stages, signals, and handoffs |

### Research and Analyze

| You say | CEX does |
|---------|----------|
| "research competitor pricing" | Dispatches intelligence nucleus for structured competitive analysis |
| "analyze our market" | Produces a market brief with TAM/SAM/SOM and positioning |
| "benchmark this approach" | Runs comparative evaluation with structured scoring |
| "investigate the trend" | Deep-dives into time-series patterns across multiple sources |

### Write and Persuade

| You say | CEX does |
|---------|----------|
| "write ad copy for my course" | Produces 3 A/B variants with hooks, CTAs, and funnel-stage awareness |
| "content for Instagram" | Generates a 7-day calendar with captions, hashtags, and posting times |
| "email sequence for launch" | Creates a multi-touch drip campaign with subject lines and triggers |
| "headline for the homepage" | Returns 3+ variants scored by hook strength and benefit clarity |

### Improve and Maintain

| You say | CEX does |
|---------|----------|
| "improve the weak artifacts" | Sweeps the entire repo, upgrades everything below quality threshold |
| "fix the broken tests" | Diagnoses root cause, patches code, re-runs to verify |
| "validate everything" | Runs full system diagnostics: 109 checks across 7 layers |
| "overnight improvement" | Schedules autonomous batch evolution while you sleep |

### Orchestrate

| You say | CEX does |
|---------|----------|
| "launch all nuclei" | Dispatches up to 6 specialized agents in parallel |
| "plan a brand launch" | Decomposes the goal into tasks, assigns nuclei, maps dependencies |
| "mission: build my CRM" | Full lifecycle: plan, decide, spec, dispatch, consolidate -- one command |

**Mix languages freely.** "Cria uma landing page pro meu curso" works exactly the same as "make me a landing page for my course." CEX resolves intent, not syntax.

---

## 7. CEX Teaches As It Works

Most AI tools are black boxes. You get output. You don't get smarter. CEX is different.

### The Didactic Protocol

CEX uses industry-standard terminology in its responses. When you use a casual term for the first time, CEX translates it once -- a single line, never a lecture -- then moves on:

```
You:  "roda o grid com os nuclei"
CEX:  "Dispatching grid -- 6 agents in parallel."
      (Grid = multi-agent orchestration, like running 6 specialists simultaneously)
```

After that first translation, CEX never repeats the explanation. You've learned the term. CEX remembers that you know it.

### What gets taught (and what doesn't)

| Situation | CEX teaches? | Why |
|-----------|-------------|-----|
| You use a metaphor for the first time | Yes -- one line | You need the mapping once |
| You use a metaphor you've already learned | No | Repetition is patronizing |
| You're in rapid-fire mode | No | Teaching interrupts your flow |
| You explicitly ask "what does X mean?" | Yes -- full answer | You asked directly |
| You use the correct term | Acknowledged | Reinforces good terminology |
| A misunderstanding would waste compute | Yes -- urgently | Wrong intent = wrong output |

### Your brain grows with the system

Every interaction makes CEX smarter about YOU:
- Successful outputs become examples for future generations
- Your feedback updates constraints ("too formal" -> next output is more casual)
- Quality scores accumulate, improving routing decisions
- The more you use it, the more it sounds like you

Day 1: functional. Day 30: expert. Day 365: irreplaceable.

---

*CEX Onboarding v4.0 -- Updated 2026-04-12. Install moved to [QUICKSTART.md](QUICKSTART.md).*
