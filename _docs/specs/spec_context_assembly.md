---
id: spec_context_assembly
kind: context_doc
title: Context Assembly Specification
version: 1.0.0
quality: 9.0
created: 2026-04-07
density_score: 1.0
---

# Context Assembly Specification

## What This Solves

An LLM with no context produces generic output. The same LLM with the right artifacts pre-loaded produces specialized output. CEX assembles context automatically so the user inputs nothing beyond intent.

## Architecture

```
BASE LAYER (read-only molds)
  archetypes/builders/{kind}-builder/    13 components per kind
  P{01-12}_*/_schema.yaml               structure contracts
  P{01-12}_*/templates/                  output patterns
  P01_knowledge/library/                 knowledge base
  .claude/rules/                         behavioral constraints

INSTANCE LAYER (filled per agent)
  N{01-06}_*/                            domain-specific artifacts
    agents/                              identity
    prompts/                             system + action prompts
    knowledge/                           domain KCs
    schemas/                             data contracts
    output/                              produced artifacts
    orchestration/                       workflows + dispatch rules
    quality/                             gates + rubrics
    ...                                  (mirrors 12 categories)

RUNTIME LAYER (assembled per task)
  .cex/runtime/handoffs/                 task + references
  .cex/runtime/decisions/                user preferences (GDP)
  .cex/runtime/signals/                  completion signals
  .cex/config/                           model routing, themes
```

## Two-Phase Assembly

### Phase 1: Boot (agent self-assembles base context)

On startup, each agent loads its own artifacts automatically:

| Source | What loads | How |
|--------|-----------|-----|
| CLAUDE.md | System overview, commands, constraints | Claude Code reads on startup |
| agent_card_{id}.md | Agent's own capability manifest | --append-system-prompt |
| .claude/rules/{id}*.md | Behavioral rules for this agent | Claude Code reads on startup |
| Sin identity | Role personality via system prompt | --append-system-prompt |

The agent starts knowing: what it has, what it can build, what rules apply. Zero discovery needed.

### Phase 2: Task (orchestrator assembles mission context)

When N07 dispatches a task, the handoff includes:

| Section | Content | Purpose |
|---------|---------|---------|
| Task | What to produce | Intent |
| Decisions | User preferences from GDP | Constraints |
| Relevant artifacts | Paths to builders, KCs, templates | Pre-selected references |
| Expected output | File path, kind, format | Target |

The agent reads the handoff, reads the referenced artifacts, and produces. No wandering, no discovery loops.

## How Context Gets Selected

### Orchestrator selection (Phase 2)

```
Intent: "create landing page for pet shop"
  |
  F1 CONSTRAIN: kind=landing_page, pillar=P05
  |
  Select from base layer:
    archetypes/builders/landing-page-builder/   (13 components)
    P01_knowledge/library/kind/kc_landing_page.md
    P05_output/templates/tpl_landing_page.md
    P06_schema/contracts/landing_page_schema.yaml
  |
  Select from instance layer (if target agent = N02):
    N02_marketing/P01_knowledge/kc_*.md (relevant domain KCs)
    N02_marketing/P05_output/ (examples of prior output)
  |
  Assemble handoff with all references
  |
  Dispatch to agent
```

### Agent self-selection (Phase 1 + during task)

```
Agent boots with deck (knows capabilities)
  |
  Reads handoff (knows task + references)
  |
  Pipeline step F3 INJECT:
    Load referenced builder components (13 files)
    Load referenced KCs
    Load template
    Load brand_config (if bootstrapped, fills {{BRAND_*}} variables)
    Load memory (past corrections, preferences)
  |
  All context assembled. Agent produces with full hand.
```

## Template Variables (autonomous freedom)

Artifacts contain intentionally open fields:

| Variable | Filled by | When |
|----------|-----------|------|
| {{BRAND_NAME}} | /init bootstrap | Once, permanent |
| {{BRAND_TONE}} | /init bootstrap | Once, permanent |
| {{TARGET_AUDIENCE}} | LLM decision | Per task, contextual |
| {{PRICING_MODEL}} | LLM or GDP | Per task or user choice |
| {{CTA_TEXT}} | LLM decision | Per output, contextual |

Variables the user filled at /init are permanent context. Variables the LLM fills are autonomous decisions based on task context. The user never needs to input beyond initial brand setup.

## Why This Works on Any Model

| Component | What it provides | Model-independent? |
|-----------|-----------------|-------------------|
| Builder components | Structure, examples, quality gates | YES -- just .md files |
| KCs | Domain knowledge in tables | YES -- structured data |
| Templates | Output patterns with variables | YES -- fill-in-the-blank |
| Schemas | Data contracts | YES -- YAML validation |
| Rules | Behavioral constraints | YES -- natural language |
| Brand config | Identity variables | YES -- key-value pairs |

The context does the specialization. The model does the generation. A smaller model with full context outperforms a larger model with no context.

## Fractal Structure

The base layer and instance layer share the same 12-category structure:

| Category | Base layer (mold) | Instance layer (filled) |
|----------|------------------|------------------------|
| Knowledge | KC templates + library | Domain-specific KCs |
| Model | Agent definitions | Configured agents |
| Prompt | Prompt templates | Domain prompts |
| Tools | Tool definitions | Configured tools |
| Output | Output templates | Produced artifacts |
| Schema | Contract definitions | Domain schemas |
| Evaluation | Quality gate templates | Domain gates |
| Architecture | Component maps | Agent cards |
| Config | Config templates | Active configs |
| Memory | Memory type definitions | Domain memories |
| Feedback | Feedback templates | Quality records |
| Orchestration | Workflow templates | Domain workflows |

Each agent is a filled instance of the universal mold. The mold guarantees structure. The fill guarantees specialization.
