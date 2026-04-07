---
id: p01_kc_8f_pipeline
kind: knowledge_card
type: domain
pillar: P01
title: "The 8F Pipeline — Complete Anatomy of CEX Artifact Production"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: meta
quality: 9.2
tags: [8f, pipeline, architecture, core, meta, production, builders]
tldr: "8 sequential functions (CONSTRAIN→COLLABORATE) that transform intent into validated, compiled, committed artifacts — the heartbeat of CEX"
when_to_use: "Understanding how CEX builds artifacts; onboarding new contributors; debugging pipeline failures; teaching the system to others"
keywords: [8f-pipeline, constrain, become, inject, reason, call, produce, govern, collaborate, artifact-production]
feeds_kinds: [knowledge_card, instruction, system_prompt, workflow]
linked_artifacts:
  - .claude/rules/n03-8f-enforcement.md
  - _tools/cex_8f_runner.py
  - _tools/cex_8f_motor.py
  - .claude/agents/validator.md
density_score: null
---

# The 8F Pipeline

## What It Is

The 8F Pipeline is CEX's mandatory artifact production protocol. Every artifact — from a 30-byte signal to a 5120-byte knowledge card — must pass through 8 sequential functions. No shortcuts. No exceptions. The pipeline transforms a natural language intent ("create a sales agent") into a validated, compiled, version-controlled artifact in the correct pillar directory.

The "F" stands for Function. Each function has a single responsibility, receives state from the previous function, and produces state for the next. The pipeline is implemented in `cex_8f_runner.py` as a stateful `RunState` dataclass that accumulates across all 8 phases.

## The 8 Functions — Overview

```
INTENT ──→ F1 ──→ F2 ──→ F3 ──→ F4 ──→ F5 ──→ F6 ──→ F7 ──→ F8 ──→ ARTIFACT
          CON    BEC    INJ    REA    CAL    PRO    GOV    COL
          ───    ───    ───    ───    ───    ───    ───    ───
          What   Who    Know   Plan   Scan   Make   Check  Ship
          can?   am I?  what?  how?   with?  it!    pass?  done.
```

| F# | Name | Verb | Input | Output | Metaphor |
|----|------|------|-------|--------|----------|
| F1 | CONSTRAIN | Bound | intent + kind | constraints dict | The blueprint's specs |
| F2 | BECOME | Embody | builder ISOs | identity dict | Putting on the uniform |
| F3 | INJECT | Learn | KCs + memory | knowledge dict | Loading the textbooks |
| F4 | REASON | Plan | accumulated state | reasoning plan | Architect's draft |
| F5 | CALL | Equip | tools + existing | tool_results dict | Checking the toolbox |
| F6 | PRODUCE | Generate | full prompt | artifact text | The actual construction |
| F7 | GOVERN | Validate | artifact | verdict dict | Quality inspection |
| F8 | COLLABORATE | Deliver | validated artifact | saved + compiled | Handoff to the world |

## Deep Dive — Each Function

### F1 CONSTRAIN — "What are the rules?"

**Purpose**: Load all constraints that bound what this artifact can be.

**Sources read**:
1. `.cex/kinds_meta.json` — resolves kind to pillar, max_bytes, naming pattern
2. `P{xx}/_schema.yaml` — pillar-level schema (frontmatter_required, boundary)
3. `bld_schema_{kind}.md` — builder-specific ID regex, field types
4. `bld_config_{kind}.md` — naming rules, paths, size limits

**State produced**: `constraints` dict with keys: `id_pattern`, `frontmatter_required`, `max_bytes`, `boundary`, `naming`, `config_rules`.

**Token budget** (T04): If `cex_token_budget` is available, allocates input/output token limits at this stage.

**Why it matters**: Without constraints, the LLM generates plausible-looking artifacts that fail validation. F1 prevents waste by establishing the rules before any creative work begins.

### F2 BECOME — "Who am I?"

**Purpose**: Load the builder's identity — persona, knowledge boundary, domain.

**Sources read**:
1. `bld_system_prompt_{kind}.md` — persona, voice, knowledge boundary
2. `bld_manifest_{kind}.md` — builder name, domain, pillar boundary

**State produced**: `identity` dict with keys: `system_prompt`, `persona`, `knowledge_boundary`, `builder_name`, `domain`, `pillar_boundary`.

**Optimizer hints**: If `cex_prompt_optimizer` is available, injects improvement hints from past learning records — "last time you built this kind, here's what scored low."

**Why it matters**: A knowledge_card builder writes differently from an agent builder. F2 ensures the LLM adopts the correct perspective, vocabulary, and expertise boundary before generating anything.

### F3 INJECT — "What do I know?"

**Purpose**: Load all relevant knowledge into the pipeline. The heaviest function — up to 9 knowledge sources.

**Sources read (in order)**:
1. `bld_knowledge_card_{kind}.md` — builder-specific KC
2. `P01_knowledge/library/kind/kc_{kind}.md` — dedicated kind KC (primary, 1:1)
3. Cluster domain KCs — supplementary matches (max 2)
4. `bld_examples_{kind}.md` — few-shot examples
5. `bld_memory_{kind}.md` — persistent learnings from past builds
6. `bld_architecture_{kind}.md` — patterns, dependencies
7. Domain context — from `--context` flag or nucleus seed
8. Build memory — past performance for this kind via `cex_memory`
9. Semantic retrieval — TF-IDF similar artifacts via `cex_retriever` (top 3)

**State produced**: `knowledge` dict with all loaded content.

**Template-First**: If a semantic match scores >= 60%, F4 will use it as a template rather than generating from scratch.

**Why it matters**: An LLM without domain knowledge produces generic filler. F3 ensures every build has access to the full knowledge graph — definitions, examples, past mistakes, and related artifacts.

### F4 REASON — "How should I build this?"

**Purpose**: LLM plans the artifact before generating it. Think-before-write.

**GDP Gate (T03)**: Before planning, checks `cex_gdp.GDPEnforcer` for unresolved user-scope decisions. If pending decisions exist for this kind, the pipeline **halts** with `NeedsUserDecision`. This enforces "user decides WHAT, LLM decides HOW."

**Prompt composed from**:
- Intent + Kind + Pillar
- Builder persona (from F2)
- Constraints summary (from F1)
- Knowledge excerpt (from F3)
- Task: "List frontmatter fields, decisions, tradeoffs, body structure"

**State produced**: `reasoning` dict with `plan` (LLM response) and `model_used`.

**Construction Triad**: Three approaches ranked by Template-First match score:
- `template` (>= 60%): Adapt from matched artifact
- `hybrid` (30-59%): Combine template structure with fresh content
- `fresh` (< 30%): Generate entirely from knowledge + constraints

**Why it matters**: Without F4, the LLM jumps straight from knowledge to output — producing structurally sound but strategically shallow artifacts. F4 forces architectural thinking.

### F5 CALL — "What tools and precedents exist?"

**Purpose**: Inventory available tools and scan for existing similar artifacts.

**Actions**:
1. Parse `bld_tools_{kind}.md` — available tools table (name, purpose, status)
2. Scan pillar examples dir — `P{xx}/examples/ex_{kind_slug}*.md`
3. Warn on duplicates — prevents redundant artifact creation

**State produced**: `tool_results` dict with `tools_available` and `existing_artifacts`.

**Why it matters**: Prevents blind rebuilds. If 3 similar agents already exist, F5 surfaces them so F6 can differentiate or reuse.

### F6 PRODUCE — "Build it."

**Purpose**: Compose the full prompt from all accumulated state and execute it via LLM.

**Prompt structure** (9 labeled sections):
```
# IDENTITY        ← F2 system_prompt
# CONSTRAINTS     ← F1 max_bytes, id_pattern, naming, boundary
# KNOWLEDGE       ← F3 builder KC + domain KCs + architecture + memory
# EXAMPLES        ← F3 few-shots
# PLAN            ← F4 reasoning output
# TOOLS           ← F5 available tools + existing artifacts
# OPTIMIZER HINTS ← F2 past learnings
# INSTRUCTION     ← bld_instruction (how to build)
# TEMPLATE        ← bld_output_template (output structure)
# TASK            ← intent + kind + critical output rules
# RETRY FEEDBACK  ← F7 failure details (only on retry)
```

**Critical output rules enforced**: Start with `---`, YAML frontmatter, `quality: null`, no code fences, no preamble.

**Token budget check** (T04b): After generation, verifies output doesn't exceed allocated token budget.

**State produced**: `artifact` — the raw LLM response (full .md content).

**Why it matters**: F6 is the only function that calls the LLM for generation. Everything before it prepares context; everything after it validates output. The quality of F1-F5 directly determines F6's output quality.

### F7 GOVERN — "Does it pass?"

**Purpose**: Validate the artifact against hard gates. Retry loop if it fails.

**7 Hard Gates (ALL must pass)**:

| Gate | Check | Auto-fixable? |
|------|-------|---------------|
| H01 | Frontmatter parses as valid YAML | No — structural |
| H02 | `id` matches kind's regex pattern | Yes — rename |
| H03 | `kind` field matches expected kind | Yes — fix field |
| H04 | `quality: null` (never pre-scored) | Yes — clear field |
| H05 | All required frontmatter fields present | Partially |
| H06 | Body size <= `max_bytes` | No — must trim content |
| H07 | File compiles via `cex_compile.py` | Depends on error |

**6 Soft Gates (scored 0-10, non-blocking)**:

| Gate | Dimension | Weight |
|------|-----------|--------|
| S01 | Completeness — all template sections | 25% |
| S02 | Density — no filler, >= 0.85 | 20% |
| S03 | Accuracy — matches domain reality | 20% |
| S04 | Structure — follows template | 15% |
| S05 | Integration — linked_artifacts valid | 10% |
| S06 | Freshness — dates current | 10% |

**Retry loop**: On hard gate failure, composes feedback → calls F6 again with `RETRY FEEDBACK` section. Max 2 retries. After 3 total attempts, saves as draft with issues flagged.

**State produced**: `verdict` dict with `passed`, `hard_gates`, `soft_warnings`, `issues`, `retries`.

**Why it matters**: Without F7, invalid artifacts enter the knowledge graph — wrong IDs break retrieval, missing fields break compilation, pre-scored quality breaks the peer-review trust chain.

### F8 COLLABORATE — "Ship it."

**Purpose**: Save, compile, index, commit, signal. The artifact enters the system.

**Actions (in order)**:
1. **Learning record** — captures build outcome regardless of success
2. **Save** — write `.md` to correct pillar directory (filename from `id` or intent slug)
3. **Compile** — `python _tools/cex_compile.py {path}` → `.yaml` twin
4. **Index** — `python _tools/cex_index.py` (if available) → update retriever
5. **Commit** — `git add + git commit -m "[N0x] description"`
6. **Signal** — `signal_writer.write_signal(nucleus, 'complete', score)` → notify orchestrator

**State produced**: `result` dict with `path`, `compiled`, `committed`, `mode`.

**Why it matters**: An artifact that isn't compiled can't be retrieved. One that isn't committed can be lost. One that doesn't signal leaves the orchestrator waiting. F8 closes the loop.

## Implementation Waves

The pipeline was built incrementally:

| Wave | Functions | What it added |
|------|-----------|---------------|
| Wave 1 | F1, F2, F3, F6, F8 | Core: load → generate → save |
| Wave 2 | + F4, F7 | Intelligence: planning + validation + retry |
| Wave 3 | + F5 | Awareness: tool inventory + dedup |

## The ISOs — Builder DNA

Each builder has 13 ISOs (Instruction Set Objects) mapped to functions:

| ISO File | Function | Purpose |
|----------|----------|---------|
| `bld_schema` | F1 | ID pattern, field types |
| `bld_config` | F1 | Naming, paths, size limits |
| `bld_system_prompt` | F2 | Persona, voice, knowledge boundary |
| `bld_manifest` | F2 | Builder identity, domain |
| `bld_knowledge_card` | F3 | Builder-specific knowledge |
| `bld_examples` | F3 | Few-shot examples |
| `bld_memory` | F3 | Past learnings |
| `bld_architecture` | F3 | Patterns, dependencies |
| `bld_instruction` | F6 | How to build |
| `bld_output_template` | F6 | Output structure |
| `bld_quality_gate` | F7 | Validation criteria |
| `bld_tools` | F5 | Available tools |
| `bld_collaboration` | F8 | Compilation, signaling |

## RunState — The Accumulator

```python
@dataclass
class RunState:
    intent: str          # Original user intent
    kind: str            # Resolved kind (e.g., "agent")
    pillar: str          # Resolved pillar (e.g., "P02")
    constraints: dict    # F1 output
    identity: dict       # F2 output
    knowledge: dict      # F3 output
    reasoning: dict      # F4 output
    tool_results: dict   # F5 output
    artifact: str        # F6 output (raw text)
    verdict: dict        # F7 output
    result: dict         # F8 output
    timings: dict        # Per-function timing
    errors: list         # Accumulated errors
```

Each function reads state from previous functions and writes its own. This is a **pipeline pattern** (not a chain) — each function can access ALL prior state, not just the immediately preceding output.

## 8F Trace — The Proof

Every build outputs a trace proving all 8 functions executed:

```
=== 8F PIPELINE ===
F1 CONSTRAIN: kind=agent, pillar=P02, max=5120B
F2 BECOME: agent-builder loaded (13 ISOs)
F3 INJECT: kc_agent.md + 2 examples. Match: 72%
F4 REASON: 4 sections, approach=template
F5 CALL: compile+doctor+index ready. 3 similar found.
F6 PRODUCE: 3,200 bytes, 4 sections, density=0.88
F7 GOVERN: 9.0/10. Gates: 7/7. 12LP: 12/12
F8 COLLABORATE: saved P02/agent_x.md. Compiled. Committed.
===================
```

No trace = no proof = artifact rejected.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Pipeline Phase |
|-------------|-------------|----------------|
| Skip to F6 | No constraints → invalid frontmatter, wrong naming | F1 missing |
| Generic persona | Builder writes knowledge_cards like agents | F2 missing |
| No knowledge injection | LLM hallucinates domain facts | F3 missing |
| No planning | Structurally sound but strategically shallow | F4 missing |
| Ignore existing artifacts | Duplicate work, inconsistent naming | F5 missing |
| No validation | Invalid artifacts pollute the knowledge graph | F7 missing |
| Save without compile | Artifact invisible to retriever | F8 incomplete |
| "I'll just write a quick..." | Violates pipeline mandate | All |

## Relationship to GDP

The 8F Pipeline controls HOW to build. GDP (Guided Decision Protocol) controls WHO decides WHAT. They intersect at F4:

```
User intent → GDP: "What tone? What audience?" → decision_manifest.yaml
                                                          ↓
F1 → F2 → F3 → F4 (reads manifest, GDP gate) → F5 → F6 → F7 → F8
```

If GDP has unresolved decisions, F4 raises `NeedsUserDecision` and the pipeline halts. No guessing. No assuming.
