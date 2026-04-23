---
quality: 8.8
id: spec_cexai_rebrand
kind: constraint_spec
pillar: P06
title: "Spec -- CEXAI Rebrand: Cognitive Enterprise X -> Cognitive Exchange AI"
version: 1.0.0
created: "2026-04-21"
author: n07_orchestrator
domain: brand-migration
quality_target: 9.0
status: SPEC
scope: full_repo
depends_on:
  - spec_opensource_release_v2
  - spec_hermes_assimilation
tags: [spec, rebrand, naming, migration, open-source, exchange, artificial-sins]
tldr: "Rename 'Cognitive Enterprise X' to 'Cognitive Exchange AI' across 20 source files, rewrite 8 core docs for global open-source positioning, create 3 new conceptual artifacts (Artificial Sins narrative, Exchange Protocol, Contributor Nucleus standard), validate with full recompile + doctor."
density_score: 0.95
updated: "2026-04-22"
---

# Spec -- CEXAI Rebrand: Cognitive Exchange AI

## THE PROBLEM

CEX is positioned as an "enterprise brain" targeting companies. The actual vision is
bigger: an open-source cognitive exchange where anyone -- entrepreneurs, developers,
researchers -- builds their own AI brain and optionally shares typed knowledge as
modular artifacts. The current name "Cognitive Enterprise X" limits this to enterprise
contexts and misses the exchange/sharing dimension entirely.

Three misalignments:

1. **Name mismatch**: "Enterprise" implies B2B SaaS, not open-source community
2. **Missing exchange story**: Contributors can build vertical nuclei (N08+) but no
   spec describes how they share and consume each other's typed artifacts
3. **Artificial Sins unbranded**: The 7 sin lenses are the most memorable differentiator
   but appear only in nucleus_def files -- no canonical narrative exists

## THE VISION

After this spec executes:

1. Every "Cognitive Enterprise X" reference becomes "Cognitive Exchange AI"
2. The README positions CEXAI for global open-source adoption (devs + entrepreneurs)
3. "Artificial Sins" is a canonical branded concept showing nucleus full capability
4. An Exchange Protocol spec defines how contributors share modular nuclei
5. The Contributor Nucleus standard shows Path 4 is the exchange on-ramp
6. All docs, boot prompts, and generated content reflect the new name
7. Pre-commit hook blocks the deprecated expansion from re-entering the codebase

## DECISIONS (from manifest)

```yaml
D1:  CEXAI (formal) / CEX (short form stays everywhere)
D2:  "Cognitive Exchange AI" -- headers + first mention only
D3:  "Open-source AI brain. Intelligence compounds when exchanged."
D4:  Artificial Sins = canonical, practical (sin = personality, nucleus = 12P dept)
D5:  X = exchange + your company ("CEXAI da [Brand]")
D6:  Audience = both (entrepreneurs + developers)
D7:  License = MIT (no change)
D8:  Positioning keyword = "AI brain" (not framework/platform/system)
D9:  Nucleus != Agent (12P department vs single LLM call)
D10: N00 = universal template, exchange unit; N01-N07 = convention nuclei
```

Manifest: `.cex/runtime/decisions/decision_manifest.yaml`

## COMPETITIVE CONTEXT (external research, 2026-04-21)

| Topic | Finding | Implication for CEXAI |
|-------|---------|----------------------|
| "Cognitive Exchange" trademark | Clean. No company, project, or registered trademark found. IBM dropped "cognitive computing" branding. | Name is safe. Use "CEXAI" in full (not just "CEX") to avoid overlap with CEX.io crypto exchange. |
| "Artificial Sins" trademark | Zero results in tech/AI/gaming. Completely uncontested. | Strong differentiator. Consider early trademark registration. |
| Competitor positioning | CrewAI = "collaborative intelligence", LangGraph = "stateful graphs", MetaGPT = "AI software company". None position as typed knowledge system. | CEXAI occupies a gap: no competitor treats knowledge as typed infrastructure with a taxonomy. |
| "Compound AI" | BAIR coined "Compound AI Systems" (2024). IBM/Databricks adopted. | Use "intelligence compounds" as a verb phrase ("In CEXAI, intelligence compounds when exchanged"), not as a noun. Avoids BAIR's established term. |
| "Digital asset" | Carries crypto/NFT connotation. Enterprise IP law uses "intellectual capital" or "knowledge asset". | For EN marketing: prefer "knowledge asset" or "intellectual capital". For PT-BR: "ativo digital" is fine (no crypto confusion in BR market). |
| Multi-runtime | Only ~2 projects do runtime-agnostic (Forge Orchestrator, Agent Orchestrator). Most are just model-agnostic. | CEXAI's 4-runtime sovereignty (same handoff runs on Claude/Codex/Gemini/Ollama) is ahead of market. Position as "runtime-sovereign". |
| Typed contributions | No framework has schema-validated, peer-scored community contributions. LangChain Hub is closest but untyped. | CEXAI's 293 kinds + 12 ISOs per builder + quality gates = unprecedented contribution framework. This IS the exchange edge. |
| MCP / A2A standards | Agentic AI Foundation (Linux Foundation) standardizing interop. MCP hit 97M installs Mar 2026. | CEXAI already uses MCP. Position as MCP-native, A2A-compatible. |

**Key positioning insight**: CEXAI is NOT competing with CrewAI/LangGraph/AutoGen. Those are
agent frameworks (build from scratch). CEXAI is a complete typed system (configure and use).
The exchange dimension (share typed cognition across instances) is a category CEXAI creates.

## BLAST RADIUS (measured 2026-04-21)

### Tier 1: Exact string "Cognitive Enterprise X" (12 source .md + 1 .sh)

| # | File (source) | Line | Context | Action |
|---|---------------|------|---------|--------|
| 1 | `CLAUDE.md` | 1 | Header: `# CEX -- Cognitive Enterprise X` | REWRITE line |
| 2 | `README.md` | 2 | Header: `CEX -- Cognitive Enterprise X` | REWRITE section |
| 3 | `_docs/HOME.md` | 9 | Header: `# CEX -- Cognitive Enterprise X` | REWRITE line |
| 4 | `docs/README.md` | 3 | Intro: `CEX (Cognitive Enterprise X)` | REWRITE line |
| 5 | `CHANGELOG.md` | 77 | History entry about README rewrite | REWRITE line |
| 6 | `N05_operations/P11_feedback/compliance_framework_cex_ai_act.md` | 31 | System field | REWRITE line |
| 7 | `N05_operations/P07_evals/conformity_assessment_cex_quality.md` | 6 | system_name field | REWRITE line |
| 8 | `N05_operations/P03_prompt/prompt_notebooklm_source.md` | 57 | Template: `CEX (Cognitive Enterprise X)` | REWRITE line |
| 9 | `N04_knowledge/P03_prompt/mentor_storyteller.md` | 52 | Template: `CEX (Cognitive Enterprise X)` | REWRITE line |
| 10 | `N04_knowledge/P01_knowledge/kc_bilingual_term_map.md` | 39 | Term entry | REWRITE row |
| 11 | `N03_engineering/P08_architecture/context_map_cex_bounded_contexts.md` | 9 | system_name | REWRITE line |
| 12 | `N02_marketing/P05_output/webinar_script_cex_intro.md` | 76 | Speaker line | REWRITE line |
| 13 | `_tools/cex_export_public.sh` | 68 | Comment/description | REWRITE line |

### Tier 2: Compiled YAMLs (auto-regenerated from Tier 1 sources)

| # | Compiled file | Source | Action |
|---|---------------|--------|--------|
| 1 | `N05_operations/compiled/compliance_framework_cex_ai_act.yaml` | #6 | RECOMPILE |
| 2 | `N05_operations/compiled/conformity_assessment_cex_quality.yaml` | #7 | RECOMPILE |
| 3 | `N05_operations/compiled/prompt_notebooklm_source.yaml` | #8 | RECOMPILE |
| 4 | `N04_knowledge/compiled/mentor_storyteller.yaml` | #9 | RECOMPILE |
| 5 | `N04_knowledge/compiled/kc_bilingual_term_map.yaml` | #10 | RECOMPILE |
| 6 | `N03_engineering/compiled/context_map_cex_bounded_contexts.yaml` | #11 | RECOMPILE |
| 7 | `N02_marketing/compiled/webinar_script_cex_intro.yaml` | #12 | RECOMPILE |
| 8 | `N00_genesis/P01_knowledge/compiled/ex_knowledge_card_cex_taxonomy.yaml` | source example | RECOMPILE |

### Tier 3: Generated output (regenerated by running media pipeline)

| Directory | Files | Source template | Action |
|-----------|-------|----------------|--------|
| `_output/mentor/*/en/text.md` | ~10 | `prompt_notebooklm_source.md` (#8) | REGENERATE via media pipeline |
| `_output/mentor/*/en/audio_source.md` | ~10 | same | REGENERATE |

### Tier 4: Positioning term "enterprise brain" (selective, NOT global replace)

These files use "enterprise brain" as a positioning phrase that shifts to "AI brain"
per decision D8. Only **positioning/marketing** contexts change -- technical architecture
references to "enterprise" (SLA, compliance, customers) stay.

| # | File | Line | Current | New | Action |
|---|------|------|---------|-----|--------|
| 1 | `CLAUDE.md` | 7 | `CEX is not an agent. It is an enterprise brain.` | `CEXAI is not an agent. It is an AI brain.` | REWRITE |
| 2 | `README.md` | 27 | `It is an **enterprise brain**` | `It is an **AI brain**` | REWRITE |
| 3 | `docs/concepts.md` | 5 | `multi-agent enterprise brain` | `multi-agent AI brain` | REWRITE |
| 4 | `N04_knowledge/P01_knowledge/mental_model_cex_architecture.md` | 43 | `CEX is an enterprise brain` | `CEXAI is an AI brain` | REWRITE |
| 5 | `N02_marketing/P05_output/webinar_script_cex_intro.md` | 5+112 | `enterprise brain` in title + slide | Rewrite to `AI brain` | REWRITE |
| 6 | `N02_marketing/P05_output/product_tour_cex.md` | 134+168 | `enterprise brain` | `AI brain` | REWRITE |
| 7 | `N04_knowledge/P01_knowledge/kc_concept_graph.md` | 41+86 | concept graph entries | Update term | REWRITE |
| 8 | `N04_knowledge/P01_knowledge/contributor_guide_cex.md` | 29 | `open enterprise brain` | `open-source AI brain` | REWRITE |
| 9 | `N06_commercial/P03_prompt/sales_playbook_n06.md` | 75 | `typed enterprise brain` | `typed AI brain` | REWRITE |

**NOT changed** (valid "enterprise" uses that stay):
- `N05_operations/P11_feedback/compliance_framework_cex_ai_act.md` -- "enterprise AI system" is a legal/compliance term
- `N04_knowledge/P01_knowledge/kc_bilingual_term_map.md` -- "enterprise brain" as a bilingual dictionary entry (update row, not delete)
- Any KC discussing enterprise architecture as a domain topic

### Tier 5: Retriever index + search metadata (auto-rebuilt)

| File | Action |
|------|--------|
| `.cex/retriever_index.json` | REBUILD via `python _tools/cex_retriever.py --rebuild` |

### Tier 6: Boot scripts + runtime (NO CHANGES NEEDED)

Verified: all `.ps1`, `.py`, `.sh` files use "CEX" as an acronym in variable
names (`$cexRoot`, `$env:CEX_NUCLEUS`, `CEX_ROOT`), prompt strings ("N07 Orchestrator
of CEX"), and window titles ("CEX-N07"). Per D1, CEX short form stays. Zero boot
script changes required.

| File pattern | CEX usage | Change needed |
|-------------|-----------|---------------|
| `boot/cex.ps1` | `$env:CEX_NUCLEUS`, prompt: "Orchestrator of CEX" | NONE |
| `boot/n0[1-6].ps1` | `$env:CEX_NUCLEUS`, `$env:CEX_ROOT` | NONE |
| `boot/cex_gemini.ps1` | same pattern | NONE |
| `boot/cex_codex.ps1` | same pattern | NONE |
| `_spawn/dispatch.sh` | `CEX_SESSION` | NONE |
| `_spawn/spawn_grid.ps1` | `CEX_GRID` | NONE |
| `_tools/cex_*.py` (all 50+) | "CEX" in docstrings, never "Cognitive Enterprise X" | NONE |

---

## ARTIFACTS

### Wave 1: Keyword Migration (T2 — N05, sequential, ~15 min)

**Prerequisites**: Decision manifest locked (done).

| # | Action | Path | Kind | Est. | Notes |
|---|--------|------|------|------|-------|
| 1.1 | REWRITE | `CLAUDE.md` | context_doc | 200B | Line 1 header + line 7 positioning |
| 1.2 | REWRITE | `README.md` | context_doc | 500B | Lines 2, 4, 27 + tagline |
| 1.3 | REWRITE | `_docs/HOME.md` | context_doc | 100B | Line 9 header |
| 1.4 | REWRITE | `docs/README.md` | context_doc | 200B | Line 3 intro |
| 1.5 | REWRITE | `CHANGELOG.md` | changelog | 100B | Line 77 history entry |
| 1.6 | REWRITE | `N05_operations/P11_feedback/compliance_framework_cex_ai_act.md` | compliance_framework | 50B | Line 31 |
| 1.7 | REWRITE | `N05_operations/P07_evals/conformity_assessment_cex_quality.md` | conformity_assessment | 50B | Line 6 |
| 1.8 | REWRITE | `N05_operations/P03_prompt/prompt_notebooklm_source.md` | prompt_template | 50B | Line 57 template var |
| 1.9 | REWRITE | `N04_knowledge/P03_prompt/mentor_storyteller.md` | prompt_template | 50B | Line 52 |
| 1.10 | REWRITE | `N04_knowledge/P01_knowledge/kc_bilingual_term_map.md` | knowledge_card | 100B | Line 39-40 row |
| 1.11 | REWRITE | `N03_engineering/P08_architecture/context_map_cex_bounded_contexts.md` | context_map | 50B | Line 9 |
| 1.12 | REWRITE | `N02_marketing/P05_output/webinar_script_cex_intro.md` | webinar_script | 100B | Line 5, 76, 112 |
| 1.13 | REWRITE | `_tools/cex_export_public.sh` | tool | 50B | Line 68 |
| 1.14 | REWRITE | 9 files from Tier 4 list | various | 200B each | "enterprise brain" -> "AI brain" in positioning |
| 1.15 | RECOMPILE | 8 compiled YAMLs from Tier 2 | compiled | auto | `python _tools/cex_compile.py {path}` per source |
| 1.16 | REBUILD | `.cex/retriever_index.json` | index | auto | `python _tools/cex_retriever.py --rebuild` |
| 1.17 | CREATE | `_tools/cex_deprecated_terms.txt` | config | 100B | Blocklist for pre-commit hook |

**Migration script** (dry-run → review → apply):

```bash
# Phase 1: Exact replacement "Cognitive Enterprise X" -> "Cognitive Exchange AI"
# Target: 13 source files only (Tier 1). Compiled YAMLs regenerate.
grep -rl "Cognitive Enterprise X" --include="*.md" --include="*.sh" . \
  | grep -v compiled/ | grep -v _output/ | grep -v .playwright-mcp/ \
  | while read f; do
      echo "[DRY-RUN] $f"
      grep -n "Cognitive Enterprise X" "$f"
    done

# Phase 2: After review, apply
grep -rl "Cognitive Enterprise X" --include="*.md" --include="*.sh" . \
  | grep -v compiled/ | grep -v _output/ | grep -v .playwright-mcp/ \
  | xargs sed -i 's/Cognitive Enterprise X/Cognitive Exchange AI/g'

# Phase 3: Selective "enterprise brain" -> "AI brain" (manual, file-by-file)
# Each file in Tier 4 list is reviewed individually because context matters.
# Do NOT global-replace "enterprise" -- only "enterprise brain" in positioning contexts.

# Phase 4: Recompile all affected sources
python _tools/cex_compile.py N05_operations/P11_feedback/compliance_framework_cex_ai_act.md
python _tools/cex_compile.py N05_operations/P07_evals/conformity_assessment_cex_quality.md
python _tools/cex_compile.py N05_operations/P03_prompt/prompt_notebooklm_source.md
python _tools/cex_compile.py N04_knowledge/P03_prompt/mentor_storyteller.md
python _tools/cex_compile.py N04_knowledge/P01_knowledge/kc_bilingual_term_map.md
python _tools/cex_compile.py N03_engineering/P08_architecture/context_map_cex_bounded_contexts.md
python _tools/cex_compile.py N02_marketing/P05_output/webinar_script_cex_intro.md

# Phase 5: Rebuild retriever index
python _tools/cex_retriever.py --rebuild
```

**Commit**: `[N07] rebrand: Cognitive Enterprise X -> Cognitive Exchange AI (13 source + 8 compiled)`

---

### Wave 2: Core Docs Rewrite (T3 — N04, ~30 min)

**Prerequisites**: Wave 1 migration complete.

| # | Action | Path | Kind | Est. | Notes |
|---|--------|------|------|------|-------|
| 2.1 | REWRITE | `README.md` | context_doc | 8KB | Full rewrite for global audience. See content spec below. |
| 2.2 | REWRITE | `CLAUDE.md` (header block) | context_doc | 500B | Lines 1-15: header, counter, positioning paragraph |
| 2.3 | REWRITE | `docs/README.md` | context_doc | 1KB | Intro paragraph + "X = exchange" explanation |
| 2.4 | REWRITE | `docs/concepts.md` | context_doc | 2KB | "What is CEX?" section + add "The Exchange" section |
| 2.5 | REWRITE | `docs/faq.md` | faq_entry | 1KB | Update "How is CEX different" + add "What is the exchange?" |
| 2.6 | REWRITE | `_docs/HOME.md` | context_doc | 500B | Header + tagline update |
| 2.7 | REWRITE | `_docs/SCRIPT_CEX_OVERVIEW.md` | context_doc | 500B | Positioning line update |

**README.md content spec** (most critical single file):

```
STRUCTURE (preserve section order, rewrite content):

# CEXAI -- Cognitive Exchange AI
  Tagline: "Open-source AI brain. Intelligence compounds when exchanged."
  Subtitle: "Seven Artificial Sins. Twelve pillars. 293 artifact kinds. Your brain."
  Badges: [update "Cognitive Enterprise X" in any badge alt-text]

## Why CEXAI exists
  - Same philosophy (typed infrastructure > prompt + tools)
  - NEW: "Exchange" framing -- your brain + sharing + community
  - "AI brain" not "enterprise brain" (D8)
  - "Build your Jarvis. Own your brain. Exchange cognition." (updated CTA)

## The maturity gap
  - PRESERVE table (it's architecture, not marketing)
  - Update "CEX nucleus" -> "CEXAI nucleus" in intro line only

## The Artificial Sins
  - RENAME from "The seven sins, the seven nuclei"
  - EXPAND: sin = personality layer, nucleus = full 12P department
  - Show: sin lens + role + what it optimizes + what breaks without it
  - Add: "Nucleus != Agent" comparison table (D9)
  - Add: N00 as universal template, N01-N07 as convention, N08+ as community

## The 12 pillars
  - PRESERVE table (it's taxonomy, not marketing)

## The 8-function pipeline (8F)
  - PRESERVE (foundational, no changes)

## The Exchange
  - NEW SECTION
  - What: typed artifacts as modular, shareable units of cognition
  - How: N00 is the universal mold, vertical nuclei are the exchange units
  - Why: "Intelligence multiplies when shared, not subtracted"
  - Contributor on-ramp: 4 paths from CONTRIBUTING.md
  - Anti-fragile: layer above LLMs, any runtime, your knowledge stays

## Quickstart
  - PRESERVE with minor updates (CEXAI references)

## Sovereignty: runs on your infrastructure
  - PRESERVE (key differentiator)

## Dispatch: solo, grid, crew, swarm
  - PRESERVE (operational docs)

## Architecture at a glance
  - PRESERVE tables
  - Update "Cognitive Enterprise X" in any header
```

**Commit**: `[N07] rebrand: core docs rewrite (README, CLAUDE.md, docs/, HOME)`

---

### Wave 2b: Brand Storytelling (T4 — N02, parallel with W2, ~30 min)

| # | Action | Path | Kind | Est. | Notes |
|---|--------|------|------|------|-------|
| 2b.1 | CREATE | `N00_genesis/P01_knowledge/library/domain/meta/kc_artificial_sins.md` | knowledge_card | 4KB | Canonical narrative. See content spec below. |
| 2b.2 | REWRITE | `N00_genesis/P01_knowledge/library/domain/meta/kc_cex_as_digital_asset.md` | knowledge_card | +1KB | Amplify with exchange framing. EN: use "knowledge asset" (avoids crypto connotation). PT-BR: "ativo digital" stays (no ambiguity in BR). |
| 2b.3 | REWRITE | `N02_marketing/P05_output/webinar_script_cex_intro.md` | webinar_script | 2KB | Title + hook + close updated for CEXAI |
| 2b.4 | REWRITE | `N02_marketing/P05_output/product_tour_cex.md` | product_tour | 1KB | Positioning lines update |
| 2b.5 | REWRITE | `N02_marketing/P05_output/interactive_demo_cex_builder.md` | interactive_demo | 500B | Positioning lines update |

**kc_artificial_sins.md content spec**:

```
PURPOSE: Canonical narrative for the 7 Artificial Sins branding.
NOT just sin names -- shows the full nucleus architecture per sin.

STRUCTURE:
# Artificial Sins: The Cultural DNA of CEXAI

## Why sins?
  - Optimization under ambiguity needs a heuristic
  - Industry term: agent personality / behavioral bias
  - CEX chose sins because they're memorable, universal, and honest
  - "Every department has a vice that makes it great at one thing"

## The 7 Artificial Sins

For EACH sin (N01-N07):
  | Field | Value |
  |-------|-------|
  | Sin | {Portuguese name} ({English name}) |
  | Nucleus | N0X {role} |
  | Optimizes for | {what it maximizes under ambiguity} |
  | 12-Pillar inventory | {count of specialized kinds per pillar} |
  | Key kinds | {top 5 specialized kinds in this nucleus} |
  | Runtime binding | {which CLI runtimes it can operate on} |
  | Sub-agents | {count, example names} |

Source data: N0X_{domain}/P08_architecture/nucleus_def_n0X.md (8 files)

## Nucleus != Agent

Table comparing:
  | Capability | Basic AI agent | CEXAI Nucleus |
  |------------|---------------|---------------|
  | Identity | System prompt | nucleus_def + sin lens + 12P |
  | Memory | Context window | Entity memory + episodic + procedural |
  | Tools | Flat list | MCP servers + API clients + pipelines |
  | Quality | None | 8F pipeline + quality gates + scoring |
  | Knowledge | RAG maybe | Typed KC library + embedding + retrieval |
  | Orchestration | None | Crews, dispatch, workflows |
  | Runtime | 1 provider | Any (Claude, GPT, Gemini, Ollama) |

## N00: The Universal Mold

Explain: N00 is not operational. It is the archetype.
- Defines the 12 pillar schemas all nuclei inherit
- Houses the 293 kind definitions (the type system)
- Contains golden examples for every kind
- IS the shareable exchange unit (modular, typed, runtime-agnostic)

## Customizable Convention

N01-N07 are convention nuclei (pre-built, opinionated).
N08+ are community nuclei (vertical, specialized, contributed).
Everything is overridable. The convention is the starting point, not the ceiling.
```

**Commit**: `[N02] rebrand: Artificial Sins narrative + digital asset amplification`

---

### Wave 2c: Exchange Protocol Spec (T5 — N03, parallel with W2, ~30 min)

| # | Action | Path | Kind | Est. | Notes |
|---|--------|------|------|------|-------|
| 2c.1 | CREATE | `_docs/specs/spec_exchange_protocol.md` | constraint_spec | 5KB | The exchange architecture. See content spec below. |
| 2c.2 | CREATE | `N00_genesis/P01_knowledge/library/domain/meta/kc_contributor_nucleus_standard.md` | knowledge_card | 3KB | How to build and share a vertical nucleus |
| 2c.3 | REWRITE | `_docs/specs/spec_metaphor_dictionary.md` | context_doc | +500B | Add exchange-related term mappings |

**spec_exchange_protocol.md content spec**:

```
PURPOSE: Define how CEXAI instances exchange typed cognition.
This is the architectural foundation for the "Exchange" in the name.

STRUCTURE:

# Exchange Protocol -- Sharing Typed Cognition Across CEXAI Instances

## THE PROBLEM
  - Each CEXAI instance is sovereign (your repo, your git, your brand)
  - But intelligence compounds faster when shared
  - No spec exists for how instances exchange artifacts safely

## THE EXCHANGE MODEL

### What is exchangeable?
  - N00 artifacts (kinds, schemas, builders) -- universal, brand-agnostic
  - Vertical nuclei (N08+) -- domain-specific, opt-in sharing
  - Knowledge cards -- typed, frontmatter-governed, quality-scored

### What is NOT exchangeable?
  - Brand config (brand_config.yaml) -- always private
  - Memory (P10 artifacts) -- instance-specific
  - Runtime state (.cex/runtime/) -- ephemeral
  - Secrets (P09 secret_config) -- never shared

### Exchange unit: the artifact
  - .md file with YAML frontmatter (self-describing)
  - quality field enables quality gates on import
  - kind field enables type validation on import
  - nucleus field enables routing on import

### Exchange unit: the vertical nucleus
  - Full N{XX}_{domain}/ directory (12 pillar subdirs)
  - nucleus_def (identity), agent_card (capabilities)
  - vocabulary KC (domain language)
  - Minimum: 5 required files (from CONTRIBUTING.md Path 4)
  - Maximum: full 12P with specialized kinds, builders, workflows

## EXCHANGE MECHANICS

### Pull model (git-based, decentralized)
  - Fork/clone the CEXAI repo
  - Cherry-pick artifacts from community nuclei
  - N00 is the compatibility layer (same schema, same 8F pipeline)
  - `git remote add community https://github.com/{user}/cexai`
  - `git checkout community/main -- N08_healthcare/`

### Quality gates on import
  - `cex_doctor.py` validates imported artifacts
  - `cex_score.py` scores them (quality: null on import, peer review assigns)
  - `cex_compile.py` integrates them into the local retriever index
  - 8F pipeline remains the universal protocol -- any artifact that passes
    F7 GOVERN in one instance will pass in another

### Security model
  - Private repo = sovereign (default)
  - Public nuclei = opt-in sharing (contributor decides)
  - Brand config NEVER leaves the instance
  - git history = audit trail for every exchange

## ANTI-FRAGILE BY DESIGN

### Runtime agnosticism
  - Exchanged artifacts work on any runtime (Claude, GPT, Gemini, Ollama)
  - The artifact is the contract, not the runtime
  - If a better model appears, the artifact improves (layer above)

### Neuroplastic assimilation
  - `cex_intent_resolver.py` + `prompt_compiler` adapt to new kinds
  - Adding a vertical nucleus adds its vocabulary to intent resolution
  - The system literally gets smarter with each import

## CONTRIBUTOR ON-RAMP

The 4 paths from CONTRIBUTING.md map to exchange granularity:

| Path | What you share | Exchange scope | Time |
|------|---------------|----------------|------|
| Knowledge Card | 1 typed artifact | Micro (single fact) | 30 min |
| Builder | 12 ISOs for 1 kind | Meso (production capability) | 2 hrs |
| SDK Provider | 1 runtime adapter | Infra (new runtime) | 4 hrs |
| Vertical Nucleus | Full 12P department | Macro (entire domain) | 8 hrs |

Path 4 (Vertical Nucleus) IS the exchange's killer feature:
  - Healthcare (N08), Fintech (N09), EdTech (N10), Legal (N11)...
  - Each is a full AI department, typed, scored, runtime-agnostic
  - Import it into your CEXAI instance = instant expertise in that domain
```

**Commit**: `[N03] rebrand: Exchange Protocol spec + Contributor Nucleus standard`

---

### Wave 3: Integration + Validation (T6 + T7, sequential, ~20 min)

**Prerequisites**: All Wave 2 artifacts exist.

| # | Action | Path | Kind | Est. | Notes |
|---|--------|------|------|------|-------|
| 3.1 | REWRITE | `CONTRIBUTING.md` | contributor_guide | 3KB | Exchange framing + Path 4 amplification |
| 3.2 | REWRITE | `docs/glossary.md` | glossary_entry | +500B | Add: CEXAI, Cognitive Exchange, Artificial Sins, Exchange Protocol |
| 3.3 | REWRITE | `docs/vocabulary.md` | domain_vocabulary | +500B | Add exchange-related terms |
| 3.4 | REWRITE | `_docs/specs/spec_metaphor_dictionary.md` | context_doc | +200B | Add metaphor mappings for exchange terms |
| 3.5 | REWRITE | `N00_genesis/P01_knowledge/examples/ex_knowledge_card_cex_taxonomy.md` | knowledge_card | 200B | Fix: already says "Enterprise Exchange" -- normalize |
| 3.6 | CREATE | `_tools/cex_deprecated_terms.txt` | config | 100B | Blocklist: "Cognitive Enterprise X" |
| 3.7 | TOOL RUN | `python _tools/cex_compile.py --all` | -- | auto | Recompile all modified sources |
| 3.8 | TOOL RUN | `python _tools/cex_doctor.py` | -- | auto | Verify 0 FAIL |
| 3.9 | TOOL RUN | `python _tools/cex_retriever.py --rebuild` | -- | auto | Rebuild search index |
| 3.10 | VALIDATE | `grep -r "Cognitive Enterprise X" --include="*.md" . \| grep -v compiled/ \| grep -v _output/` | -- | auto | Must return 0 results |
| 3.11 | REWRITE | `N04_knowledge/P01_knowledge/kc_bilingual_term_map.md` | knowledge_card | 200B | Add CEXAI row, update CEX row |

**CONTRIBUTING.md content spec** (exchange-framed):

```
PRESERVE: Quick Start, Path 1-3 details, Quality gates
REWRITE: Intro paragraph (add exchange framing)
EXPAND: Path 4 (Vertical Nucleus) with exchange positioning
ADD: "The Exchange" section explaining:
  - Why contribute: "Intelligence multiplies when shared"
  - What you get: your artifacts improve everyone's retriever index
  - What you keep: your brand config, your memory, your secrets
  - Community nuclei: N08+ are the exchange's value propositions
```

**Commit**: `[N07] rebrand: integration + validation (CONTRIBUTING, glossary, doctor, deprecated terms)`

---

## WAVE ORDER + TIMING

```
Wave 0: GDP (DONE -- manifest locked 2026-04-21)
  |
  v
Wave 1: Keyword Migration (T2, sequential, ~15 min)
  |  13 source files + 8 compiled + 1 retriever index
  |  Single N05 execution OR N07 direct (surgical grep-replace)
  |
  v
Wave 2: Content (T3 + T4 + T5, PARALLEL, ~30 min)
  |
  |-- T3: Core docs rewrite (N04) -- README, CLAUDE.md, docs/
  |-- T4: Brand storytelling (N02) -- Artificial Sins KC, digital asset update
  |-- T5: Exchange Protocol (N03) -- spec + contributor nucleus KC
  |
  v
Wave 3: Integration + Validation (T6 + T7, sequential, ~20 min)
  |  CONTRIBUTING rewrite, glossary, doctor, deprecated-term hook
  |
  v
DONE: git tag v10.4.0-cexai
```

## DONE WHEN

- [ ] `grep -r "Cognitive Enterprise X" --include="*.md" . | grep -v compiled/ | grep -v _output/ | grep -v .playwright-mcp/` returns **0 results**
- [ ] `python _tools/cex_doctor.py` shows **0 FAIL**
- [ ] `python _tools/cex_compile.py --all` completes without error
- [ ] README.md contains "Cognitive Exchange AI" in header
- [ ] README.md contains "Artificial Sins" section
- [ ] README.md contains "The Exchange" section
- [ ] `kc_artificial_sins.md` exists with all 7 nuclei documented
- [ ] `spec_exchange_protocol.md` exists with exchange model defined
- [ ] `kc_contributor_nucleus_standard.md` exists with Path 4 standard
- [ ] `CONTRIBUTING.md` references the exchange protocol
- [ ] `docs/glossary.md` defines CEXAI, Cognitive Exchange, Artificial Sins
- [ ] `_tools/cex_deprecated_terms.txt` exists with "Cognitive Enterprise X" blocklisted
- [ ] All 8 compiled YAMLs from Tier 2 regenerated
- [ ] Retriever index rebuilt
- [ ] Pre-commit hook validates no deprecated terms in staged files

## ROLLBACK PLAN

```bash
# If anything goes catastrophically wrong:
git log --oneline -10  # find last good commit before Wave 1
git revert HEAD~N..HEAD  # revert all rebrand commits
# OR
git tag pre-cexai-rebrand  # tag BEFORE starting Wave 1
git reset --hard pre-cexai-rebrand  # nuclear option
```

**Create the safety tag before Wave 1 starts.**

## WHAT THIS SPEC DOES NOT COVER

1. Logo / visual identity (graphic design, not CEX scope)
2. GitHub org/repo rename (URL change, separate decision)
3. Domain registration (cexai.dev, cexai.ai)
4. PyPI package rename (cex_sdk -> cexai_sdk, if published)
5. Community platform (Discord, GitHub Discussions)
6. _output/mentor regeneration (run media pipeline separately)
7. Fine-tuning data update (_data/ft/*.jsonl contains old name)
8. .playwright-mcp cache (auto-generated, ignored)

These are valid follow-ups but out of scope for this migration.

## RELATED ARTIFACTS

| Artifact | Relationship | Score |
|----------|-------------|-------|
| `spec_opensource_release_v2` | predecessor | 0.85 |
| `kc_cex_as_digital_asset` | amplified by this spec | 0.78 |
| `spec_metaphor_dictionary` | updated by this spec | 0.65 |
| `spec_seed_words` | reference (intent resolution) | 0.60 |
| `spec_n06_brand_verticalization` | format template | 0.55 |
| `nucleus_def_n0[0-7]` | source data for Artificial Sins | 0.50 |
| `CONTRIBUTING.md` | rewritten by this spec | 0.48 |
| `kc_bilingual_term_map` | updated by this spec | 0.45 |
