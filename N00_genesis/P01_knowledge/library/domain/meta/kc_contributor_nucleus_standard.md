---
quality: 9.1
quality: 8.1
id: kc_contributor_nucleus_standard
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Contributor Nucleus Standard -- Building and Sharing Vertical Nuclei"
version: 1.0.0
created: 2026-04-21
updated: 2026-04-21
author: n03_engineering
domain: meta
tags: [contributor, nucleus, vertical, standard, exchange, community]
tldr: "Technical standard for building N08+ vertical nuclei: 5 required files, 12 pillar structure, vocabulary rules, assimilation review checklist."
when_to_use: "Building a new vertical nucleus; reviewing a contributed nucleus; onboarding domain experts"
keywords: [vertical-nucleus, contributor, N08, assimilation, exchange]
density_score: null
related:
  - contributor_guide_cex
  - spec_exchange_protocol
  - kc_artificial_sins
  - nucleus_def_n00
---

# Contributor Nucleus Standard

## What is a Vertical Nucleus

A vertical nucleus is a domain-specialized CEXAI fractal (N08+). Each brings domain
expertise the core team lacks -- healthcare (N08), fintech (N09), edtech (N10),
legal (N11), and any domain a contributor chooses to formalize.

**Core vs. vertical nuclei:**

| Property | Core (N01-N07) | Vertical (N08+) |
|----------|---------------|-----------------|
| Origin | Pre-built, ships with CEXAI | Community-contributed |
| Sin lens | Pre-assigned (7 canonical sins) | Contributor chooses from sin palette |
| Pillar structure | 12P mandatory | 12P mandatory (fractal compliance) |
| Domain | Generic function (research, build, ops) | Specialized domain (healthcare, fintech) |
| N00 dependency | Inherits all N00 schemas | Inherits all N00 schemas |
| Runtime | Any (Claude, GPT, Gemini, Ollama) | Any (same runtime agnosticism) |
| Exchange scope | Not exchanged (convention layer) | Primary exchange unit |

**What a vertical nucleus is NOT:**
- Not a plugin (it has full 12-pillar autonomy, not a bolt-on)
- Not an agent (it is a 12-pillar department with sub-agents, not a single LLM call)
- Not a fork (it lives inside the main CEXAI repo, governed by the same 8F pipeline)

## Minimum Viable Nucleus (5 Required Files)

These are the 5 files every vertical nucleus must include to pass assimilation
review. Without any of these, `cex_doctor.py` will report FAIL.

### File 1: `rules/n{xx}-{domain}.md`

**Purpose:** Nucleus identity, sin lens, domain scope, behavioral rules.

| Section | Required | Content |
|---------|----------|---------|
| Identity | Yes | Nucleus ID, role, domain name |
| Sin Lens | Yes | Which sin drives this nucleus (see Sin Selection Guide below) |
| Domain Scope | Yes | What this nucleus builds, what it does NOT build |
| 8F Overrides | No | Domain-specific F1-F8 behavior (defaults to N00 if omitted) |
| Routing Rules | No | When N07 should dispatch to this nucleus |

### File 2: `P02_model/nucleus_def_n{xx}.md`

**Purpose:** Machine-readable identity. The agent card system reads this to
understand what the nucleus can do.

**Required frontmatter fields (from `N00_genesis/P02_model/_schema.yaml`):**

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `p02_nd_n08` |
| `kind` | literal | `nucleus_def` |
| `pillar` | literal | `P02` |
| `nucleus_id` | string | `N08` |
| `role` | string | `healthcare` |
| `sin_lens` | string | `Methodical Gluttony` |
| `cli_binding` | string | `claude` |
| `model_tier` | enum | `sonnet` or `opus` |
| `boot_script` | path | `boot/n08.ps1` |
| `agent_card_path` | path | `N08_healthcare/P08_architecture/agent_card_n08.md` |
| `pillars_owned` | list | `[P01, P04, P06]` |
| `domain` | string | `clinical workflows, FHIR, HL7` |
| `fallback_cli` | string | `codex` |

**Body sections:** Identity table, Pillars Owned table, Crew Templates, Domain
Agents, Boot Contract, Composability matrix. See any `nucleus_def_n0{1-7}.md` for
the canonical structure.

### File 3: `P01_knowledge/kc_{domain}_vocabulary.md`

**Purpose:** Controlled vocabulary for the domain. Every domain-specific term the
nucleus uses must be defined here.

**Critical rule:** Terms in this KC must NOT conflict with the canonical vocabulary
in `p03_pc_cex_universal.md`. If your domain uses a term that already exists in the
universal vocabulary, you must either use the canonical definition or request an
exception during assimilation review.

| Section | Content |
|---------|---------|
| Canonical Terms | Domain terms + industry definitions + how the nucleus uses them |
| Cross-Nucleus Shared Terms | List of N00 terms this nucleus does NOT redefine |
| Domain-Specific Extensions | New terms this nucleus introduces to the taxonomy |
| Anti-patterns | Terms to never use (and their correct replacements) |

### File 4: `P08_architecture/agent_card_n{xx}.md`

**Purpose:** Capabilities declaration. Tells N07 and other nuclei what this nucleus
can produce, receive, and delegate.

| Section | Content |
|---------|---------|
| Capabilities | What kinds this nucleus produces |
| Inputs | What it needs from other nuclei |
| Outputs | What it sends to other nuclei |
| Tools | MCP servers, API clients, CLI tools it uses |
| Gaps | What it cannot do (routes to other nuclei) |

### File 5: `P08_architecture/component_map_n{xx}.md`

**Purpose:** What this nucleus builds -- the artifact inventory and data flow.

| Section | Content |
|---------|---------|
| Artifact Inventory | Table of kinds this nucleus produces, with pillar mapping |
| Data Flow | How artifacts flow between pillars within the nucleus |
| External Dependencies | What N00 schemas and shared builders it consumes |
| Domain Integrations | External APIs, databases, standards it connects to |

## Full Nucleus Structure

Beyond the 5 required files, a complete vertical nucleus mirrors the 12-pillar
fractal structure:

```
N08_healthcare/
  P01_knowledge/              # Domain KCs, embeddings, RAG sources
    kc_healthcare_vocabulary.md   # REQUIRED (File 3)
    kc_fhir_resources.md         # Domain knowledge
    kc_hl7_messaging.md
  P02_model/                  # Agents, nucleus def, role assignments
    nucleus_def_n08.md           # REQUIRED (File 2)
  P03_prompt/                 # System prompts, prompt templates
  P04_tools/                  # MCP configs, API clients, browser tools
  P05_output/                 # Output templates, formatters
  P06_schema/                 # Domain data contracts, validation schemas
  P07_evals/                  # Benchmarks, scoring rubrics, quality gates
  P08_architecture/           # Agent card, component map, decision records
    agent_card_n08.md            # REQUIRED (File 4)
    component_map_n08.md         # REQUIRED (File 5)
  P09_config/                 # Environment configs, rate limits
  P10_memory/                 # (typically empty -- instance-specific)
  P11_feedback/               # Learning records, regression checks
  P12_orchestration/          # Workflows, crew templates, dispatch rules
  rules/                      # Nucleus identity and behavioral rules
    n08-healthcare.md            # REQUIRED (File 1)
  compiled/                   # gitignored -- auto-generated by cex_compile
```

**Fractal compliance:** All 12 pillar directories must exist, even if empty. This
ensures `cex_doctor.py` can validate the structure and any builder ISOs that
reference pillar paths will resolve correctly.

## Sin Selection Guide

Every nucleus is driven by a sin lens -- a behavioral bias that determines what the
nucleus optimizes for when input is ambiguous. The sin is cultural DNA, not decoration.

### The 7 Sins Available

| Sin | Portuguese | Optimization bias | Best for domains that... |
|-----|-----------|-------------------|--------------------------|
| Envy | Analytical Envy | Wants what others have -- relentless comparison | Need competitive intelligence, benchmarking |
| Lust | Creative Lust | Craves novelty -- pushes creative boundaries | Produce content, marketing, design |
| Pride | Inventive Pride | Demands excellence -- refuses mediocrity | Build infrastructure, architecture, tools |
| Gluttony | Knowledge Gluttony | Consumes everything -- insatiable data hunger | Manage knowledge, research, documentation |
| Wrath | Gating Wrath | Zero tolerance for defects -- enforces quality | Handle operations, testing, compliance |
| Greed | Strategic Greed | Maximizes returns -- every action must pay off | Drive commercial, pricing, monetization |
| Sloth | Orchestrating Sloth | Seeks efficiency -- does minimum work for max result | Orchestrate, coordinate, delegate |

### Selection criteria

1. **What does ambiguity look like in your domain?** A healthcare nucleus facing
   ambiguous patient data should optimize for safety (Wrath) or thoroughness
   (Gluttony), not creativity (Lust).

2. **What is the worst failure mode?** If your domain's worst outcome is missing
   information, choose Gluttony. If it is poor quality, choose Wrath. If it is
   missed revenue, choose Greed.

3. **The sin is a heuristic, not a constraint.** It tells the LLM what to optimize
   when the user's intent is unclear. It does NOT prevent the nucleus from doing
   other things -- it biases the default behavior.

| Domain example | Recommended sin | Rationale |
|----------------|----------------|-----------|
| Healthcare | Wrath | Patient safety requires zero-defect bias |
| Fintech | Greed | Financial optimization is the core function |
| EdTech | Gluttony | Learning requires consuming and organizing knowledge |
| Legal | Envy | Precedent comparison is fundamental to legal reasoning |
| Creative/Design | Lust | Creative domains need novelty bias |
| DevOps/SRE | Wrath | Uptime demands zero-tolerance for defects |
| Research | Gluttony | Research is defined by insatiable data consumption |

## Assimilation Review Checklist

When a vertical nucleus PR is submitted, maintainers verify these gates:

### Structural gates (automated)

| # | Check | Tool | Pass condition |
|---|-------|------|----------------|
| 1 | All 12 pillar dirs exist | `ls N{XX}_{domain}/P{01..12}*/` | 12 directories found |
| 2 | 5 required files present | `cex_doctor.py` | 0 FAIL on required file checks |
| 3 | Non-ASCII compliance | `cex_sanitize.py --check --scope N{XX}/` | 0 violations in `.py`/`.ps1`/`.sh` |
| 4 | Frontmatter validity | `cex_doctor.py` | All required frontmatter fields present |
| 5 | Compilation | `cex_compile.py N{XX}_{domain}/` | 0 errors |

### Semantic gates (manual review)

| # | Check | Reviewer verifies |
|---|-------|-------------------|
| 6 | Vocabulary conflict | No terms in `kc_{domain}_vocabulary.md` redefine canonical terms |
| 7 | nucleus_def schema | Follows `N00_genesis/P02_model/_schema.yaml` structure |
| 8 | Sin lens coherence | Chosen sin matches domain's ambiguity optimization need |
| 9 | Domain scope clarity | `rules/n{xx}-{domain}.md` clearly states what the nucleus DOES and does NOT build |
| 10 | Cross-nucleus routing | Agent card specifies what flows to/from other nuclei |

### Post-merge integration

| # | Action | Command |
|---|--------|---------|
| 11 | Rebuild retriever index | `python _tools/cex_retriever.py --rebuild` |
| 12 | Update intent resolver | Add domain patterns to `p03_pc_cex_universal.md` |
| 13 | Register new kinds | Add to `.cex/kinds_meta.json` if nucleus introduces new kinds |

## Exchange Compatibility

Vertical nuclei are the primary exchange unit in the CEXAI ecosystem. Compatibility
is guaranteed by adherence to N00 schemas:

| Compatibility layer | What it ensures |
|--------------------|-----------------|
| N00 pillar schemas | Artifact structure is identical across instances |
| `kinds_meta.json` | Kind names resolve consistently |
| `p03_pc_cex_universal.md` | Intent resolution works for domain terms |
| 8F pipeline | Quality gates produce consistent results |
| Frontmatter contract | Self-describing artifacts validate anywhere |

**The exchange promise:** A nucleus that passes assimilation review in one CEXAI
instance will pass `cex_doctor.py` in any other instance running the same N00
schema version. This is the architectural guarantee that makes typed cognition
exchangeable.

See also: `_docs/specs/spec_exchange_protocol.md` (full exchange specification).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[contributor_guide_cex]] | upstream | -- |
| [[spec_exchange_protocol]] | upstream | -- |
| [[kc_artificial_sins]] | sibling | -- |
| [[nucleus_def_n00]] | reference | -- |
| [[spec_cexai_rebrand]] | parent | -- |
