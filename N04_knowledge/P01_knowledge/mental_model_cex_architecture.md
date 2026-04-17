---
id: mental_model_cex_architecture
kind: mental_model
pillar: P01
nucleus: n04
title: "Mental Model -- CEX Architecture for Any LLM or Engineer"
version: 1.0.0
quality: 9.1
tags: [mental_model, architecture, cex, 8F, nucleus, knowledge_management, ubiquitous_language, cross_synthesis]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "CEX = enterprise knowledge factory. Core analogy: 8F pipeline x 12 pillars x 257 kinds = the factory floor. Seven sin-lens nuclei produce typed artifacts through a universal reasoning protocol. Any LLM can load this model and immediately navigate CEX as a senior engineer would."
density_score: 0.91
sources:
  - CLAUDE.md
  - .claude/rules/ubiquitous-language.md
  - N04_knowledge/P01_knowledge/kc_knowledge_vocabulary.md
  - N01_intelligence/P01_knowledge/kc_intelligence_vocabulary.md
  - N03_engineering/P01_knowledge/kc_engineering_vocabulary.md
  - N02_marketing/P01_knowledge/kc_marketing_vocabulary.md
  - N05_operations/P01_knowledge/kc_operations_vocabulary.md
  - N06_commercial/P01_knowledge/kc_commercial_vocabulary.md
---

# Mental Model: CEX Architecture

## The Core Analogy

**CEX is not an agent. CEX is an enterprise brain.**

Most "AI agents" = system prompt + tools.
CEX = typed infrastructure for enterprises that compounds over time.

The factory floor metaphor:
```
8F pipeline (HOW to think)
    x
12 pillars (WHERE knowledge lives)
    x
257 kinds (WHAT is being produced)
    =
The factory floor (the product CEX delivers)
```

Every piece of work in CEX is a `kind` produced by a `builder` following the `8F pipeline`
and stored in one of the 12 `pillars`. This triple determines everything else automatically
(convention_over_configuration).

---

## The Factory Floor (12 Pillars x 257 Kinds)

| Pillar | Domain | Representative Kinds |
|--------|--------|---------------------|
| P01 Knowledge | Storage, retrieval, KCs | `knowledge_card`, `glossary_entry`, `rag_source` |
| P02 Model | Agent definitions, providers | `agent`, `model_provider`, `boot_config` |
| P03 Prompt | Templates, chains, compilers | `prompt_template`, `system_prompt`, `chain` |
| P04 Tools | External capabilities | `cli_tool`, `browser_tool`, `mcp_server` |
| P05 Output | Production artifacts | `landing_page`, `diagram`, `formatter` |
| P06 Schema | Data contracts | `input_schema`, `type_def`, `validation_schema` |
| P07 Evaluation | Quality, scoring, testing | `quality_gate`, `benchmark`, `llm_judge` |
| P08 Architecture | System structure | `agent_card`, `decision_record`, `pattern` |
| P09 Config | Runtime settings | `env_config`, `feature_flag`, `rate_limit_config` |
| P10 Memory | State, context, indexing | `knowledge_index`, `entity_memory`, `memory_summary` |
| P11 Feedback | Learning, correction | `bugloop`, `learning_record`, `reward_signal` |
| P12 Orchestration | Workflows, dispatch | `workflow`, `schedule`, `crew_template` |

**Navigation rule:** given a task, map it to a pillar first, then select the kind.
The kind determines the builder. The builder runs 8F. The output lands in the pillar directory.
No configuration required -- this IS the convention.

---

## The 8F Universal Reasoning Protocol

Every nucleus follows the same 8 functions for every task. Never fewer, never reordered.

| Function | What It Does | Key Output |
|----------|-------------|-----------|
| F1 CONSTRAIN | Resolve kind + pillar + schema from user intent | `{kind, pillar, max_bytes, naming}` |
| F2 BECOME | Load builder identity (13 ISOs per kind) | Builder system prompt + role |
| F2b SPEAK | Load controlled vocabulary KC | Canonical term set for all subsequent output |
| F3 INJECT | Assemble context (KCs, examples, memory, brand) | 10+ grounded sources |
| F4 REASON | Plan sections, approach (Template-First/Hybrid/Fresh) | Section plan, dependency map |
| F5 CALL | Execute tools (compile, index, retrieve) | Pre-conditions validated |
| F6 PRODUCE | Generate complete artifact with frontmatter + body | Draft (target density >= 0.85) |
| F7 GOVERN | Quality gate: 7 hard gates + 12LP + 5D scoring | Score >= 8.0 to proceed |
| F8 COLLABORATE | Save, compile, commit, signal | Artifact persisted + nucleus signaled |

**Why 8F matters:** a 5-word user input ("make me a landing page") enters at F1.
8F adds the 1M-token reasoning that the user cannot. The output is a professional,
production-ready artifact. The 8F pipeline IS the force multiplier.

---

## The Seven Nuclei (Sin-Lens System)

Each nucleus optimizes for a different dimension of enterprise intelligence.
The "sin" is not a flaw -- it is the nucleus's drive: what it maximizes when
input is ambiguous.

| Nucleus | Domain | Sin Lens | Optimization Target |
|---------|--------|----------|---------------------|
| N01 | Intelligence | Analytical Envy | Most complete, sourced research |
| N02 | Marketing | Creative Lust | Most compelling, converting copy |
| N03 | Engineering | Inventive Pride | Most correct, testable artifacts |
| N04 | Knowledge | Knowledge Gluttony | Most complete knowledge retrieval surface |
| N05 | Operations | Gating Wrath | Strictest quality gates, zero tolerance |
| N06 | Commercial | Strategic Greed | Maximum revenue per artifact |
| N07 | Orchestrator | Orchestrating Sloth | Minimum intervention per coordinated outcome |

**Routing rule:** map user intent to domain, select nucleus, dispatch.
The nucleus's sin lens determines HOW it interprets ambiguous inputs.
N04 (Knowledge Gluttony) ingest every source, index everything, never stop.

---

## N00 Genesis: The Archetype Mold (Convention over Configuration)

N00 Genesis is the pre-sin archetype: the template from which N01-N07 are born.

```
N00_genesis/         <- the mold
    P01_knowledge/   <- canonical KC library (424 KCs, source of truth)
    P02_model/       <- base agent definitions
    P03_prompt/      <- universal prompt layers (257-kind intent resolution)
    ...P12           <- all 12 pillars defined here first
    archetypes/      <- 259 builders (13 ISOs each = 3381 total ISOs)
    boot/            <- session startup artifacts

N0X_{domain}/        <- instance of N00 mold
    P01_knowledge/   <- nucleus-specific KCs (overrides or extends N00)
    ...P12           <- same 12 pillars, nucleus-specific content
    rules/           <- nucleus identity + sin lens + routing rules
    crews/           <- composable crew definitions
```

CoC principle: every artifact follows N00_genesis structure WITHOUT explicit config.
A new artifact in N03_engineering/P06_schema/ just works because N00 defines the
P06 schema (pun intended). Explicit config is only needed when OVERRIDING convention.

**Key implication for any LLM:** to understand any artifact's context, find its
counterpart in N00_genesis. The archetype is the documentation.

---

## The Ubiquitous Language Layer (L0/L1/L2 Transmutation Pipeline)

User input is always vague. CEX transmutes it into precise builder dispatch:

```
User: "document our API" (vague)
    |
    L0: cex_intent_resolver.py    -- Python, 0 tokens, maps to {kind, pillar, nucleus, verb}
    |                                result: {kind=api_reference, pillar=P05, nucleus=N03, verb=create}
    |
    L1: p03_pc_cex_universal.md   -- 257-kind bilingual (PT+EN) intent resolution table
    |                                confirms: api_reference is the right kind
    |
    L2: kc_{domain}_vocabulary.md -- per-nucleus controlled vocabulary overlay
    |                                N03 loads kc_engineering_vocabulary.md
    |
    v
Precise builder dispatch: api-reference-builder, P05, N03
```

This pipeline is why CEX does not hallucinate kinds. L0 is deterministic.
L1 covers all 257 kinds in both Portuguese and English. L2 adds domain precision.

---

## How Nuclei Communicate (LLM-to-LLM Interoperability)

Nuclei never share a context window. They communicate via:

| Channel | When | Format |
|---------|------|--------|
| Handoff file | N07 -> N0X task assignment | `.cex/runtime/handoffs/n0X_task.md` (frontmatter + body) |
| Signal | N0X -> N07 completion | `write_signal(nucleus, event, quality_score)` |
| Artifact (compiled) | Any nucleus -> any nucleus | `kind_{domain}.md` + `compiled/kind_{domain}.yaml` |
| Decision manifest | User -> all nuclei (via N07) | `.cex/runtime/decisions/decision_manifest.yaml` |

**Ubiquitous language contract:** every handoff uses canonical kind/pillar/nucleus names.
"Build a research card for competitor scan" is WRONG (kind drift).
"Produce kind=knowledge_card, pillar=P01, domain=competitive-intelligence, nucleus=N01" is CORRECT.
The canonical form is unambiguous to ANY LLM on ANY runtime (Claude/Codex/Gemini/Ollama).

---

## The Quality System

| Layer | Tool | Gate |
|-------|------|------|
| Structural (30%) | `cex_score.py` L1 | frontmatter fields present, naming correct |
| Rubric (30%) | `cex_score.py` L2 | 7 hard gates, 12LP checklist, 5D dimensions |
| Semantic (40%) | `cex_score.py` L3 | LLM evaluation (only runs when L1+L2 >= 8.5) |
| Density | `density_score` field | >= 0.85 (tables > prose, no filler) |
| Peer review | `cex_score.py --apply` | quality != null only after peer assignment |

**Key invariant:** quality is NEVER self-assigned. `quality: null` = built, not yet peer-reviewed.
`cex_evolve.py` runs the Karpathy loop to improve artifacts heuristically before peer review.

---

## Anti-Patterns (What CEX Is NOT)

| Anti-Pattern | CEX Behavior |
|-------------|-------------|
| Single system prompt agent | 259 typed builders, each with 13 ISOs |
| Untyped knowledge ("just docs") | 257 kinds, each with schema + builder + KC |
| N07 builds artifacts directly | N07 NEVER builds; dispatches to N01-N06 |
| Self-scored quality | quality: null until peer review |
| Invented kinds | Only kinds from `.cex/kinds_meta.json` |
| Monolingual prompts | PT+EN bilingual intent resolution (L1) |
| Runtime lock-in | Claude/Codex/Gemini/Ollama all supported |

---

## How to Navigate CEX (For Any LLM)

1. **Identify the task domain** -> select nucleus (N01-N06) or let N07 route
2. **Map to kind** -> check `.cex/kinds_meta.json` (257 entries)
3. **Find the pillar** -> kind's frontmatter has `pillar: Pxx`
4. **Load builder** -> `archetypes/builders/{kind}-builder/` (13 ISOs)
5. **Run 8F** -> follow F1-F8, never skip F7 GOVERN
6. **Save to pillar** -> `N0X_{domain}/P{xx}_{name}/{kind}_{domain}.md`
7. **Signal** -> `write_signal(nucleus, event, score)`

No other configuration needed. The convention IS the documentation.
