---
id: n00_readme
kind: context_doc
pillar: P01
nucleus: n00
title: "N00 Genesis -- Nucleus Instantiation Guide"
version: 1.0
quality: 9.1
tags: [n00, genesis, archetype, instantiation, cex]
density_score: 1.0
related:
  - p08_pat_nucleus_fractal
  - bld_knowledge_card_nucleus_def
  - p10_entity_cex_system
  - kc_nucleus_def
  - bld_system_prompt_nucleus_def
  - nucleus-def-builder
  - spec_cex_system_map
  - p01_kc_cex_project_overview
  - p01_kg_cex_system_architecture
  - bld_collaboration_nucleus_def
---

<!-- 8F: F1=context_doc P01 F2=context-doc-builder F3=kinds_meta+pillar_schemas F4=plan F5=scan F6=produce F7=gate F8=save -->

## What is N00 Genesis?

N00_genesis is the **pre-sin archetype** from which all CEX nuclei (N01-N07) are born.
It holds the canonical vocabulary of the entire system: 12 pillar kind indexes and
257 kind manifests that define every artifact type the system can produce.

N00 has no sin lens and no operational role. It is the uninstantiated template --
a convention-over-configuration hierarchy that every active nucleus inherits and fills
with its own domain context, sin lens, and model tier.

## The 12 Pillars

| Pillar | Name | Kinds | Description |
|--------|------|-------|-------------|
| P01 | Knowledge | 28 | Facts, RAG sources, domain verticals, retrieval configs |
| P02 | Model | 22 | Agent definitions, model providers, architectures |
| P03 | Prompt | 20 | Templates, chains, reasoning strategies, system prompts |
| P04 | Tools | 34 | API clients, browser automation, MCP servers, search |
| P05 | Output | 23 | Landing pages, pitch decks, guides, press releases |
| P06 | Schema | 8 | Data contracts, types, validation, API references |
| P07 | Evals | 23 | Benchmarks, LLM judges, scoring rubrics, eval datasets |
| P08 | Architecture | 12 | Agent cards, ADRs, diagrams, capability registries |
| P09 | Config | 28 | Env vars, rate limits, secrets, RBAC, feature flags |
| P10 | Memory | 18 | Entity memories, knowledge indexes, session state |
| P11 | Feedback | 26 | Quality gates, guardrails, compliance, bug loops |
| P12 | Orchestration | 15 | Workflows, DAGs, crew templates, dispatch rules |

Each pillar directory contains:
- `kind_index.md` -- master index of all kinds in that pillar
- `kind_{name}/kind_manifest_n00.md` -- canonical manifest per kind

## How to Instantiate a New Nucleus

### Step 1: Choose a sin lens

Each nucleus runs on one of the seven deadly sins as its cultural DNA.
The sin determines what the nucleus optimizes for under ambiguous input.

| Sin | Lens | Optimizes for |
|-----|------|---------------|
| Envy | Analytical Envy | Competitive intelligence, gap analysis |
| Lust | Creative Lust | Seductive copy, brand desire |
| Pride | Inventive Pride | Elegant engineering, zero waste |
| Gluttony | Knowledge Gluttony | Comprehensive indexing, maximum recall |
| Wrath | Gating Wrath | Quality enforcement, ruthless filtering |
| Greed | Strategic Greed | Revenue maximization, monetization |
| Sloth | Orchestrating Sloth | Minimal effort, maximum delegation |

### Step 2: Choose primary pillars

Not every nucleus owns all 12 pillars. Choose 2-4 primary pillars that match the nucleus role.

| Domain | Suggested primary pillars |
|--------|--------------------------|
| Intelligence/research | P01, P07, P08 |
| Marketing/copy | P03, P05, P12 |
| Engineering/build | P02, P04, P06 |
| Knowledge/docs | P01, P10, P05 |
| Operations/deploy | P09, P04, P07 |
| Commercial/sales | P11, P03, P05 |
| Orchestration | P12, P02, P08 |

### Step 3: Choose model tier

| Tier | Models | Use when |
|------|--------|----------|
| Opus | claude-opus-4-7 (1M ctx) | Complex builds, orchestration, long-form reasoning |
| Sonnet | claude-sonnet-4-6 (200K ctx) | Standard operations, research, copy |
| Haiku | claude-haiku-4-5 (200K ctx) | Fast classification, routing, simple transforms |

### Step 4: Create the nucleus directory structure

```bash
# Create the 12 pillar subdirectories (mirrors N00)
mkdir -p N0{X}_{role}/P{01..12}_{name}

# Required files per nucleus (minimum viable set):
# 1. Identity
N0X_{role}/rules/n0X-{role}.md          # nucleus rules + sin lens
N0X_{role}/P08_architecture/nucleus_def_n0X.md  # machine-readable identity
N0X_{role}/P08_architecture/agent_card_n0X.md   # deployment spec

# 2. Boot
boot/n0X.ps1                             # PowerShell boot wrapper

# 3. Memory (optional but recommended)
N0X_{role}/P10_memory/memory_scope_n0X.md  # what this nucleus remembers
```

### Step 5: Inject the sin lens

The sin lens is declared in `nucleus_def_n0X.md` and injected into:
- The system prompt (`P03_*/system_prompt_n0X.md`)
- The agent card (`P08_*/agent_card_n0X.md`)
- The nucleus rules (`rules/n0X-*.md`)

Sin lens injection changes how the nucleus interprets ambiguous input.
Same task, different sin = different artifact produced.

### Step 6: Register in `.cex/P09_config/nucleus_models.yaml`

```yaml
n0X:
  role: {role_name}
  model: claude-sonnet-4-6        # or opus, haiku
  context: 200000                  # or 1000000 for Opus
  sin_lens: {sin_name}
  primary_pillars: [P01, P07]
  fallback_chain:
    - claude
    - gemini
    - ollama
```

### Step 7: Fill primary pillar kinds

Start with the most impactful kinds for your nucleus domain.
Consult each pillar's `kind_index.md` for the ranked list.

Priority order for a new nucleus:
1. `nucleus_def` (P02) -- the machine-readable identity contract
2. `agent_card` (P08) -- the deployment spec
3. `system_prompt` (P03) -- the voice and constraints
4. `knowledge_card` (P01) -- domain knowledge base
5. `prompt_template` (P03) -- operational templates
6. `quality_gate` (P11) -- quality enforcement

## Convention-Over-Configuration Hierarchy

CEX follows the convention-over-configuration pattern (Rails pattern):
- N00 defines the schema and structure (the convention)
- N01-N07 inherit the schema and fill the variables (the configuration)
- Instances don't redeclare what is already declared in N00

This means:
- Every kind_manifest in N00 is the source of truth for that kind's schema
- Nucleus instances only override what is specific to their domain
- N07 orchestrates; it never reads N01-N06 rules directly (lean boot)

## 8F Pipeline Applied to Nucleus Instantiation

```
F1 CONSTRAIN  -> resolve: nucleus_id, sin_lens, model_tier, primary_pillars
F2 BECOME     -> load: N00_genesis kind manifests for your primary pillars
F3 INJECT     -> assemble: brand_config + decision_manifest + sin_lens seed
F4 REASON     -> plan: which kinds to fill first? 12-pillar priority map
F5 CALL       -> tools: cex_bootstrap.py --nucleus n0X --sin {sin}
F6 PRODUCE    -> generate: nucleus_def + agent_card + system_prompt + rules
F7 GOVERN     -> validate: all required files present? quality > 8.0?
F8 COLLABORATE-> commit: [N0X] nucleus bootstrap complete. Signal n07.
```

## Build a kind via 8F

```python
# Discover available builders
python _tools/cex_8f_runner.py "your intent" --discover

# Build a specific kind
python _tools/cex_8f_runner.py "your intent" --kind knowledge_card --execute

# Query similar artifacts
python _tools/cex_retriever.py --query "your topic" --top-k 5
```

## References

| Resource | Path |
|----------|------|
| Kinds meta (257 kinds) | `.cex/kinds_meta.json` |
| Pillar schemas | `P{01-12}_*/_schema.yaml` |
| 8F pipeline rules | `.claude/rules/8f-reasoning.md` |
| Orchestrator rules | `.claude/rules/n07-orchestrator.md` |
| Boot scripts | `boot/n0{1-7}.ps1` |
| Nucleus config | `.cex/P09_config/nucleus_models.yaml` |
| Brand config | `.cex/brand/brand_config.yaml` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_nucleus_fractal]] | downstream | 0.40 |
| [[bld_knowledge_card_nucleus_def]] | related | 0.39 |
| [[p10_entity_cex_system]] | downstream | 0.37 |
| [[kc_nucleus_def]] | related | 0.36 |
| [[bld_system_prompt_nucleus_def]] | downstream | 0.33 |
| [[nucleus-def-builder]] | downstream | 0.32 |
| [[spec_cex_system_map]] | sibling | 0.31 |
| [[p01_kc_cex_project_overview]] | related | 0.30 |
| [[p01_kg_cex_system_architecture]] | related | 0.30 |
| [[bld_collaboration_nucleus_def]] | downstream | 0.29 |
