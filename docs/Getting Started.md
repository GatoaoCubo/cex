# Getting Started

This guide walks you through installing CEXAI, configuring it for your brand, and running your first commands.

## Prerequisites

| Requirement | Minimum | Notes |
|-------------|---------|-------|
| Git | 2.30+ | For version control of all artifacts |
| Python | 3.10+ | SDK runtime and all tooling |
| LLM Runtime | At least one | Claude Code, Codex CLI, Gemini CLI, or Ollama |
| OS | Windows 10/11 or Linux | PowerShell boot scripts are Windows-native; bash dispatch works cross-platform |

### Runtime Options

CEXAI is runtime-agnostic. Pick any supported runtime:

| Runtime | Install | Best For |
|---------|---------|----------|
| Claude Code | `npm install -g @anthropic-ai/claude-code` | Full feature set, MCP support, sub-agents |
| Codex CLI | `npm install -g @openai/codex` | OpenAI models |
| Gemini CLI | `npm install -g @anthropic-ai/gemini-cli` | Google models |
| Ollama | [ollama.com](https://ollama.com) | Free local models, no API key needed |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/GatoaoCubo/cex.git
cd cex
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Validate your setup

```bash
python _tools/cex_setup_validator.py
```

This checks for missing dependencies, broken paths, and runtime availability.

### 4. Run diagnostics

```bash
python _tools/cex_doctor.py
```

Expect 118+ PASS results. Any FAIL will include remediation steps.

## Brand Bootstrap (`/init`)

The X in CEX is a variable -- it becomes YOUR brand identity. Before producing any artifacts, bootstrap your brand:

```
/init
```

CEXAI will ask approximately 6 questions:

1. What is your company/brand name?
2. What do you do in one sentence?
3. What are your 3 core values?
4. How would you describe your brand personality -- formal or casual? Technical or friendly?
5. Who is your ideal customer?
6. How do you make money -- subscription, one-time sales, courses?

Your answers are saved to `.cex/brand/brand_config.yaml` and auto-injected into every prompt across all nuclei.

**Why this matters:** Without brand config, every nucleus produces generic output. With it, every output matches your voice, colors, and identity. The 2-minute investment saves hours of "make it sound more like us" revisions.

## Boot Methods

| Method | Command | What It Does |
|--------|---------|-------------|
| PowerShell boot | `boot/cex.ps1` | Boot N07 orchestrator directly |
| PATH shortcut | `cex-main` | Boot N07 from any PowerShell location |
| Nucleus boot | `boot/n03.ps1` | Boot a specific nucleus (N01-N06) |

## Your First `/build`

The `/build` command produces a single artifact through the [[8F Pipeline]]:

```
/build knowledge_card about prompt engineering best practices
```

What happens behind the scenes:

1. **F1 CONSTRAIN** -- Resolves `kind=knowledge_card`, `pillar=P01`, loads schema
2. **F2 BECOME** -- Loads the knowledge-card-builder (12 ISOs)
3. **F3 INJECT** -- Assembles context from existing KCs, examples, brand config
4. **F4 REASON** -- Plans sections, approach, references
5. **F5 CALL** -- Scans for similar artifacts, prepares tools
6. **F6 PRODUCE** -- Generates the artifact with frontmatter and body
7. **F7 GOVERN** -- Validates quality gates, scores dimensions
8. **F8 COLLABORATE** -- Saves, compiles, commits, signals completion

The output is a production-quality markdown artifact with YAML frontmatter, saved to the correct pillar directory.

## Your First `/mission`

The `/mission` command is the full lifecycle shortcut -- it combines `/plan`, `/guide`, `/spec`, `/grid`, and `/consolidate`:

```
/mission build a content marketing system for my SaaS product
```

This triggers:

1. **Plan** -- Decomposes the goal into tasks, identifies which [[Architecture|nuclei]] handle each task, maps dependencies
2. **Guide** -- Asks you subjective decisions (tone, audience, style) via the Guided Decision Protocol (GDP)
3. **Spec** -- Creates a blueprint specifying exact artifacts to produce
4. **Grid** -- Dispatches up to 6 nuclei in parallel to build autonomously
5. **Consolidate** -- Verifies deliverables, scores quality, cleans up processes

## The Workflow

The standard CEXAI workflow follows this sequence:

```
/plan  -->  /guide  -->  /spec  -->  /grid  -->  /consolidate
  |           |           |          |              |
  |           |           |          |              +-> verify + score + clean
  |           |           |          +-> dispatch nuclei (autonomous)
  |           |           +-> spec blueprint (exact artifacts)
  |           +-> decisions with user (co-pilot)
  +-> decompose goal into tasks
```

User decides WHAT. LLM builds HOW. Verify together.

## Next Steps

- [[Architecture]] -- Understand the 12 pillars, 8 nuclei, and fractal structure
- [[8F Pipeline]] -- Deep dive into the reasoning protocol
- [[Commands]] -- Full command reference
- [[Kinds]] -- Browse the 300 artifact types
