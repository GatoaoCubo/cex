# CEX Onboarding Guide

> Everything you need to go from zero to your first working agent.

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

## 2. Five-Minute Setup

### Prerequisites

- Python 3.10+
- Git
- Any code editor

### Install

```bash
git clone https://github.com/your-org/cex.git
cd cex
```

### Bootstrap a new project

```bash
python _tools/bootstrap.py --name MyProject --lps P01,P02,P03 --with-examples
```

This creates `MyProject/` with schemas, generators, templates, and examples for
the selected pillars. For all 12 pillars:

```bash
python _tools/bootstrap.py --name MyProject
```

### Validate the structure

```bash
python _tools/cex_doctor.py
```

Doctor checks folder structure, schema presence, and naming compliance.

### Create your first artifact

```bash
cp MyProject/P01_knowledge/templates/tpl_knowledge_card_domain.md \
   MyProject/P01_knowledge/my_first_card.md
```

Edit the file, fill in the YAML frontmatter, and compile:

```bash
python _tools/cex_compile.py --all
```

---

## 3. Architecture

CEX has 5 layers, 12 pillars, and 7 business nuclei.

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

### The 7 Nuclei (Business Domains)

| ID  | Domain         | Primary Pillars |
|-----|----------------|-----------------|
| N01 | Research       | P01, P07        |
| N02 | Marketing      | P03, P05        |
| N03 | Engineering    | P02, P04, P06   |
| N04 | Knowledge Mgmt | P01, P10        |
| N05 | Operations     | P04, P12        |
| N06 | Commercial     | P05, P09        |
| N07 | Administration | P08, P11, P12   |

### How They Fit Together

Pillars define WHAT types of artifacts exist. Nuclei define WHERE domain instances
live. Builders define HOW artifacts are created (13 ISO files = factory blueprint).

---

## 4. Your First Agent

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

Density must be >= 0.8. No prose blocks longer than 3 lines. Bullets max 80 chars.

---

## 5. IDE Setup

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

*CEX Onboarding v1.0*
