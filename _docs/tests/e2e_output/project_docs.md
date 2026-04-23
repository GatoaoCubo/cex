---
id: ctx_cex_new_dev_guide
kind: context_doc
title: CEX Project Guide for New Developers
version: 0.1.0
quality: 9.0
density_score: 1.0
---

## What is CEX?

CEX is a typed knowledge system that turns short natural-language intents into production-grade artifacts using LLM agents.
It defines 117 artifact kinds (knowledge cards, agents, prompts, configs, etc.), each with a dedicated builder that enforces structure, quality gates, and brand consistency.
The "X" in CEX is a variable -- once bootstrapped with `/init`, the system becomes a branded brain tailored to a specific company or creator.

## Quickstart

1. **Clone and enter the repo**
   ```bash
   git clone <repo-url> && cd cex
   ```

2. **Bootstrap your brand** -- answer ~6 questions so every output matches your identity:
   ```bash
   python _tools/cex_bootstrap.py          # or type /init in chat
   ```

3. **Run the doctor** to verify all builders and schemas are healthy:
   ```bash
   python _tools/cex_doctor.py
   ```

4. **Build your first artifact** (e.g. a knowledge card):
   ```bash
   # In a Claude Code session:
   /build knowledge_card about React server components
   ```

5. **Check system status** at any time:
   ```bash
   /status
   ```

## Architecture Overview

### Nuclei (N00--N07)

CEX splits work across 8 specialized nuclei. N07 orchestrates; the rest execute.

| Nucleus | Role | Domain |
|---------|------|--------|
| N00 | Genesis | Archetypes, schemas, molds |
| N01 | Intelligence | Research, market analysis, papers |
| N02 | Marketing | Copywriting, ads, brand voice |
| N03 | Builder | Artifact construction (the workhorse) |
| N04 | Knowledge | RAG, embeddings, taxonomy, docs |
| N05 | Operations | Code, testing, CI/CD, deploy |
| N06 | Commercial | Pricing, courses, funnels, revenue |
| N07 | Orchestrator | Dispatch, monitor, consolidate |

N07 never builds artifacts directly -- it writes handoff files and dispatches to the appropriate nucleus via `bash _spawn/dispatch.sh`.

### 8F Pipeline

Every task (build, research, write, deploy) follows the same 8-step reasoning protocol:

| Step | Name | Purpose |
|------|------|---------|
| F1 | CONSTRAIN | Resolve kind, pillar, schema, constraints |
| F2 | BECOME | Load the builder's 13 ISOs (identity, instructions, system prompt, etc.) |
| F3 | INJECT | Pull knowledge cards, examples, brand context, memory |
| F4 | REASON | Plan sections, pick approach (template / hybrid / fresh) |
| F5 | CALL | Discover tools and similar artifacts for reuse |
| F6 | PRODUCE | Generate the full artifact with frontmatter + body |
| F7 | GOVERN | Validate against quality gates; retry if below floor |
| F8 | COLLABORATE | Save, compile, git commit, send completion signal |

### Kinds and Pillars

- **117 kinds** define every artifact type (agent, prompt_template, guardrail, knowledge_card, ...).
- Each kind belongs to one of **12 pillars** (`P01_knowledge` through `P12_meta`).
- Each kind has a **builder** with 13 ISOs in `archetypes/builders/{kind}-builder/`.
- Kind metadata lives in `.cex/kinds_meta.json`; pillar schemas in `P{xx}/_schema.yaml`.

### Key Directories

| Path | Contents |
|------|----------|
| `archetypes/builders/` | 121 builders (13 ISOs each) |
| `P01_knowledge/library/` | Knowledge cards and the kind index |
| `.cex/runtime/` | Handoffs, signals, PIDs, decisions |
| `_tools/` | 58 Python tools (compile, doctor, score, etc.) |
| `_spawn/` | Dispatch scripts for multi-nucleus execution |
| `cex_sdk/` | Python SDK runtime (78 files, ~4500 lines) |
| `N01_intelligence/` -- `N07_orchestration/` | Per-nucleus working directories |

## Key Commands

| Command | What it does |
|---------|--------------|
| `/init` | Bootstrap CEX for your brand (~2 min interactive) |
| `/plan <goal>` | Decompose a goal into tasks, nuclei, and dependencies |
| `/guide [goal]` | Co-pilot mode -- guided decisions before building |
| `/spec [plan]` | Create a detailed spec from a plan |
| `/grid [spec]` | Execute a spec -- dispatch nuclei autonomously |
| `/build <intent>` | Build a single artifact via the 8F pipeline |
| `/validate [file]` | Check artifact quality against gates |
| `/mission <goal>` | Full lifecycle: plan + guide + spec + grid + consolidate |
| `/doctor` | Run full system health check |
| `/status` | Dashboard of system state |
| `/evolve [file]` | Autonomous artifact improvement loop |
| `/consolidate` | Post-dispatch: verify, score, clean up |

## Key Tools (CLI)

| Tool | Purpose |
|------|---------|
| `cex_run.py` | Unified entry: intent to prompt |
| `cex_8f_runner.py` | Full 8F pipeline execution |
| `cex_compile.py` | Compile .md to .yaml |
| `cex_doctor.py` | Builder health check |
| `cex_score.py` | Peer review scoring |
| `cex_retriever.py` | TF-IDF artifact similarity search |
| `cex_bootstrap.py` | First-run brand setup |

## Core Rules

1. **8F is mandatory** -- every task, every nucleus, no exceptions.
2. **GDP before dispatch** -- subjective decisions go to the user first, then into `decision_manifest.yaml`.
3. **N07 never builds** -- it orchestrates via dispatch.
4. **`quality: null`** -- artifacts never self-score; peer review assigns quality.
5. **ASCII-only code** -- all `.py`, `.ps1`, `.cmd`, `.sh` files must be ASCII (0x00--0x7F).
