---
quality: 9.1
id: spec_vertical_densification
kind: constraint_spec
pillar: P06
title: "Spec -- Vertical Densification: Architecture Self-Audit, Karpathy Sweep, Cross-Synthesis, CoC Convergence"
version: 1.0.0
created: 2026-04-17
author: n07_orchestrator
domain: system-quality
quality_target: 9.0
status: SPEC
scope: N01-N06 + N05 (code hygiene)
depends_on: spec_nucleus_self_assembly
tags: [spec, densification, karpathy-loop, coc, cross-synthesis, code-hygiene, quality-sweep]
tldr: "Four-wave self-improvement: (1) fix 18 stale .py path refs, (2) Karpathy sweep on 308 unscored artifacts, (3) cross-nucleus KC synthesis into reusable shared artifacts, (4) CoC convergence via pattern/few_shot/reasoning_trace artifacts."
density_score: 0.96
updated: "2026-04-17"
---

# Spec -- Vertical Densification

## THE PROBLEM (Architecture Against Itself)

Running the new architecture (post-SELF_ASSEMBLY) against the old one reveals three classes of debt:

### Class 1: Code Debt (18 stale Python files)
STRUCT_ALIGN V2 moved root `P0x_*` → `N00_genesis/P0x_*`.
18 Python tools still point at the old paths:

| File | Stale refs | Impact |
|------|-----------|--------|
| `cex_pipeline.py` | 9 | pillar routing broken |
| `cex_forge.py` | 9 | artifact creation broken |
| `cex_init.py` | 9 | init flow broken |
| `cex_feedback.py` | 9 | quality tracking broken |
| `cex_prompt_layers.py` | 3 | layer loading fails |
| `cex_run.py` | 3 | unified entry broken |
| `cex_system_test.py` | 3 | 3 test assertions wrong |
| `cex_8f_motor.py` | 1 | KC library path wrong |
| + 10 more | 1-2 each | silent failures |

Pattern in stale code: `PILLAR_MAP = {"P01": "P01_knowledge", ...}` without `N00_genesis/` prefix.
Fix: `PILLAR_MAP = {"P01": "N00_genesis/P01_knowledge", ...}` — mechanical, no logic change.

### Class 2: Quality Debt (308 unscored artifacts)
Every artifact built in SELF_ASSEMBLY W1 has `quality: null`.
CEX rule: quality is assigned by peer review, never self-scored.
But `cex_evolve.py` provides the Karpathy loop for autonomous improvement before peer review.

Distribution of 308 unscored artifacts:
```
P01: 42  P06: 39  P09: 38  P07: 36  P10: 33  P11: 32
P04: 22  P05: 18  P03: 15  P08: 7   P12: 5   P02: 3
```

The Karpathy formula (already in CEX):
```
program.md (strategy hints, read-only)
    +
target artifact (the one being improved)
    +
cex_score.py (immutable metric)
    =
agent loop: hypothesis → apply → score → keep if better
```

Modes: `heuristic` (free, mechanical fixes) → `auto` (heuristic + agent if needed) → `agent` (full LLM loop, budget-tracked)

### Class 3: Cross-Synthesis Gap (isolated nuclei)
Each nucleus built its own KCs in isolation. No artifact yet exists that:
- Synthesizes patterns ACROSS N01-N06 (cross-domain knowledge graph)
- Encodes the 8F pipeline as a reusable `few_shot_example` any LLM can follow
- Defines the CoC conventions as a `pattern` artifact (not a rule document, but a BUILD PATTERN)
- Creates shared `mental_model` artifacts readable by Claude/Codex/Gemini/Ollama equally

This is the LLM-reusability gap: artifacts are CEX-specific, not cross-runtime portable.

---

## THE FORMULAS (already in CEX, apply them)

### Formula 1: Karpathy Loop
```python
# cex_evolve.py agent <file> --budget 30000 --target 9.0
# For each artifact below quality threshold:
score_before = cex_score(artifact)
for round in range(max_rounds=3):
    hypothesis = llm_generate(program_hints + artifact + "improve to 9.0")
    apply(hypothesis, artifact)
    score_after = cex_score(artifact)
    if score_after > score_before:
        keep(); break
    else:
        discard(); try_next_hypothesis()
```

Apply to: all 308 quality:null artifacts in W1 batches per nucleus.

### Formula 2: Construction Triad (F4 REASON)
```
Template-First (60%+ match):
  Find similar artifact in N00_genesis/P{xx}/examples/ or N0x/P{xx}/
  Adapt it: replace domain-specific content, keep structure
  Density gain: +0.08-0.12 vs fresh generation

Hybrid (30-60% match):
  Merge template sections with fresh domain content
  Use N00 archetype as structural skeleton

Fresh (<30% match):
  Generate from scratch using builder ISOs
  Reference 3+ existing artifacts for grounding
```

Apply to: new cross-synthesis artifacts in Wave 3.

### Formula 3: Density Optimization
```
density_score = (unique_content_units / total_content_units) × coverage_factor
Target: >= 0.85

Low density causes:
  - Filler sentences ("This artifact defines...")
  - Repeated headers without content
  - Prose where tables would work
  - Missing cross-references

Fix: replace prose with tables, add cross-refs, remove filler, add examples
```

Apply to: any artifact with density_score < 0.85 in W1 batch.

### Formula 4: Convention-over-Configuration (CoC)
```
Convention: every artifact follows N00_genesis structure WITHOUT explicit config
Configuration: when a nucleus OVERRIDES a convention, it must be explicit

CoC compliance check:
  - Frontmatter fields match N00_genesis/_schema.yaml
  - File naming: {kind}_{domain_suffix}.md
  - Pillar placement: N0X_{domain}/P{xx}_{name}/{kind}_{domain}.md
  - Cross-reference format: relative path, not absolute
  - Kind names: from kinds_meta.json only (no invented kinds)
```

Apply to: every new artifact via F7 GOVERN + new `pattern` artifacts that encode the convention.

---

## THE VISION

After this spec executes:

1. **All 18 stale .py files updated** → pillar routing works correctly for all tools
2. **308 artifacts scored and improved** → quality baseline established
3. **Cross-nucleus synthesis artifacts** → shared knowledge graph + universal patterns that any LLM runtime can consume
4. **Purposeful lines in every artifact** → no filler, tables > prose, cross-references present
5. **CoC pattern artifacts** → the conventions are encoded as BUILD ARTIFACTS, not just documentation

The distinction at (3): artifacts written in **ubiquitous language** (F2b SPEAK protocol) are portable across runtimes. An artifact that says "use the 8F pipeline" is CEX-specific. An artifact that says "use this intent_resolution → retrieval → generation → validation sequence with these interfaces" is universally readable.

---

## WAVE STRUCTURE

### Wave 0: N07 Orchestration (15 min)

Pre-dispatch work: write per-nucleus handoffs, verify tool state.

```bash
# Verify 18 stale files list
python _tools/cex_migrate_paths.py --dry-run   # if exists
# else: manual grep audit per file

# Verify evolve tool functional
python _tools/cex_evolve.py report
```

### Wave 1: N05 Code Hygiene (30 min, sequential prerequisite)

Fix all 18 stale Python files. This unblocks cex_pipeline, cex_forge, cex_init, cex_run.

**Mechanical fix pattern** (no logic change — only the dict/constant changes):

```python
# BEFORE (stale pattern in all 18 files):
PILLAR_MAP = {
    "P01": "P01_knowledge",
    "P02": "P02_model",
    ...
}
# or:
pillar_path = CEX_ROOT / "P01_knowledge" / ...
# or:
dirs = ["P01_knowledge", "P02_model", ...]

# AFTER:
PILLAR_MAP = {
    "P01": "N00_genesis/P01_knowledge",
    "P02": "N00_genesis/P02_model",
    ...
}
# or:
pillar_path = CEX_ROOT / "N00_genesis" / "P01_knowledge" / ...
# or:
dirs = ["N00_genesis/P01_knowledge", "N00_genesis/P02_model", ...]
```

After fixing: run `python _tools/cex_system_test.py` to verify 0 new failures.

Files to fix:

| File | Stale refs | Fix type |
|------|-----------|---------|
| `_tools/cex_pipeline.py` | 9 | PILLAR_MAP dict |
| `_tools/cex_forge.py` | 9 | PILLAR_MAP dict |
| `_tools/cex_init.py` | 9 | PILLAR_MAP dict |
| `_tools/cex_feedback.py` | 9 | PILLAR_MAP dict |
| `_tools/cex_prompt_layers.py` | 3 | pillar dir list |
| `_tools/cex_run.py` | 3 | pillar dir refs |
| `_tools/cex_system_test.py` | 3 | test assertions |
| `_tools/cex_8f_motor.py` | 1 | KC_LIBRARY_PATH |
| `_tools/cex_ft_dataset.py` | 1 | pillar path |
| `_tools/cex_handoff_composer.py` | 2 | pillar refs |
| `_tools/cex_preflight.py` | 2 | pillar scan |
| `_tools/cex_reranker.py` | 1 | pillar path |
| `_tools/cex_research.py` | 1 | pillar ref |
| `_tools/cex_source_harvester.py` | 2 | pillar scan |
| `_tools/cex_stats.py` | 2 | pillar count |
| `_tools/distill.py` | 5 | pillar dirs |
| `_tools/notebooklm_create.py` | 1 | path ref |
| `_tools/notebooklm_paste.py` | 1 | path ref |

Commit: `[N05] code-hygiene: update 18 stale P0x paths to N00_genesis/P0x`

### Wave 2: Quality Sweep — Karpathy Loop (all nuclei parallel, 60 min)

Each nucleus runs the Karpathy loop on its own W1 artifacts.

**Per nucleus execution:**
```bash
# Step 1: heuristic pass (free, mechanical fixes)
find N0X_{domain} -name "*.md" -not -path "*/compiled/*" \
  | xargs -I{} python _tools/cex_evolve.py heuristic {}

# Step 2: score all (assigns numeric quality score)
find N0X_{domain} -name "*.md" -not -path "*/compiled/*" \
  | python _tools/cex_score.py --apply

# Step 3: agent loop on artifacts still below 8.5
find N0X_{domain} -name "*.md" -not -path "*/compiled/*" \
  | xargs grep -l "quality: null\|quality: 0\." 2>/dev/null \
  | head -20 \
  | xargs -I{} python _tools/cex_evolve.py auto {} --budget 20000 --target 8.5

# Step 4: compile + signal
python _tools/cex_compile.py --all
python -c "from _tools.signal_writer import write_signal; write_signal('n0X', 'complete', 9.0)"
```

**Densification rules (apply during agent loop):**
1. Replace prose paragraphs with structured tables where content is tabular
2. Add cross-references: every artifact must reference >= 1 related artifact in its nucleus
3. Remove filler: "This {kind} defines...", "The purpose of this artifact is..." → delete
4. Add examples: if `kind=knowledge_card` and no example block → add `## Example` section
5. Add anti-patterns: if `kind=knowledge_card` → add `## Anti-Patterns` with 2-3 entries

### Wave 3: Cross-Nucleus Synthesis (N04 primary, N01 support, 45 min)

Create shared artifacts synthesized FROM existing nucleus KCs — not invented, derived.
These are the "reusable by any LLM" artifacts.

**Synthesis method (Template-First):**
```
Source: collect all kc_{domain}_vocabulary.md files (N01-N06)
         + top KCs from each nucleus P01 (ranked by density_score)
Method:  find overlapping concepts across >= 3 nuclei
         → synthesize into a shared artifact
         → place in N04_knowledge (the knowledge nucleus owns cross-domain synthesis)
```

**Artifacts to create:**

| Action | Path | Kind | Source | Notes |
|--------|------|------|--------|-------|
| CREATE | N04_knowledge/P01_knowledge/knowledge_graph_cex_domains.md | knowledge_graph | N01-N06 vocab KCs | Cross-domain concept map |
| CREATE | N04_knowledge/P01_knowledge/ontology_cex_taxonomy.md | ontology | kinds_meta.json + pillar schemas | Formal CEX taxonomy for any LLM |
| CREATE | N00_genesis/P03_prompt/few_shot_example_8f_research.md | few_shot_example | N01 artifacts | 8F applied to research task |
| CREATE | N00_genesis/P03_prompt/few_shot_example_8f_build.md | few_shot_example | N03 artifacts | 8F applied to build task |
| CREATE | N00_genesis/P03_prompt/few_shot_example_8f_deploy.md | few_shot_example | N05 artifacts | 8F applied to ops task |
| CREATE | N00_genesis/P08_architecture/pattern_coc_nucleus.md | pattern | N00 structure | CoC convention for nucleus structure |
| CREATE | N00_genesis/P08_architecture/pattern_portfolio_assembly.md | pattern | spec_nucleus_self_assembly | Portfolio assembly build pattern |
| CREATE | N04_knowledge/P10_memory/knowledge_graph_cross_nucleus.md | knowledge_graph | all nuclei P01 | Shared entity graph N01-N06 |
| CREATE | N00_genesis/P02_model/mental_model_8f_pipeline.md | mental_model | 8f-reasoning.md | 8F as a mental model for any LLM |
| CREATE | N00_genesis/P02_model/mental_model_cex_architecture.md | mental_model | CLAUDE.md + nucleus_defs | CEX system model for any runtime |

**What makes these "reusable by any LLM":**
- Written in ubiquitous language (no CEX-internal metaphors)
- Self-contained: every term is defined in the artifact itself
- Structured data: tables over prose, explicit interfaces
- No assumed context: a model that has never seen CEX before can follow them
- Portable format: valid markdown + frontmatter → readable by Claude/Codex/Gemini/Ollama

### Wave 4: CoC Convergence (N03, 30 min)

Create the build patterns that ENCODE the conventions — not as documentation, but as executable artifacts that F2 BECOME can load.

**Convention artifacts:**
```
A pattern artifact answers: "given this input, produce this output following these conventions"
A few_shot_example answers: "here is what a correct execution looks like"
A reasoning_trace answers: "here is how I thought through this"
```

| Action | Path | Kind | Notes |
|--------|------|------|-------|
| CREATE | N03_engineering/P08_architecture/pattern_8f_full_trace.md | pattern | Complete 8F trace template |
| CREATE | N03_engineering/P08_architecture/pattern_nucleus_instantiation.md | pattern | How to instantiate N00 mold into a nucleus |
| CREATE | N03_engineering/P07_evals/reasoning_trace_8f_constrain.md | reasoning_trace | F1 CONSTRAIN example trace |
| CREATE | N03_engineering/P07_evals/reasoning_trace_8f_govern.md | reasoning_trace | F7 GOVERN example trace |
| CREATE | N03_engineering/P03_prompt/few_shot_example_schema_design.md | few_shot_example | P06 schema design example |
| CREATE | N03_engineering/P03_prompt/action_paradigm_cex_build.md | action_paradigm | Build action paradigm: input→8F→artifact |
| REWRITE | N03_engineering/P08_architecture/invariant_n03.md | invariant | Add F2b SPEAK + ubiquitous language invariants |

### Wave 5: N07 Consolidation (15 min)

```bash
# Final quality sweep
python _tools/cex_evolve.py sweep --target 9.0 --max-rounds 1

# Verify doctor
python _tools/cex_doctor.py

# Compile all
python _tools/cex_compile.py --all

# Verify system tests pass with new paths
python _tools/cex_system_test.py

# Commit
git add -A && git commit -m "[N07] VERTICAL_DENSIFICATION: 308 scored, 18 paths fixed, 10 cross-synthesis artifacts, CoC patterns"
```

---

## DECISIONS (Autonomous)

| Decision | Authority | Rationale |
|----------|-----------|-----------|
| heuristic before agent | N07 (cost) | heuristic is free; agent only if still below 8.5 |
| N04 owns cross-synthesis | N07 (arch) | Knowledge Gluttony nucleus owns the synthesis layer |
| few_shot_examples in N00_genesis | N07 (arch) | Shared resources belong in the archetype, not a nucleus |
| pattern artifacts in N03_engineering | N07 (arch) | Engineering nucleus defines build conventions |
| Wave 1 sequential | N07 (dependency) | Stale paths block tools used in Waves 2-4 |
| No new kinds invented | All nuclei | Only kinds from kinds_meta.json; if new kind needed → add to kinds_meta first |

---

## ACCEPTANCE CRITERIA

```
Wave 1:
  - [ ] 18 Python files updated (grep for old pattern returns 0)
  - [ ] python _tools/cex_system_test.py passes with no new failures
  - [ ] cex_pipeline.py pillar routing returns N00_genesis paths

Wave 2:
  - [ ] quality: null artifact count drops from 308 to < 50
  - [ ] avg density_score across W1 artifacts >= 0.85
  - [ ] 0 artifacts with density < 0.75

Wave 3:
  - [ ] 10 cross-synthesis artifacts created
  - [ ] knowledge_graph_cex_domains.md covers >= 6 domain nodes
  - [ ] ontology_cex_taxonomy.md covers all 12 pillars + 257 kinds
  - [ ] few_shot_examples pass cex_compile.py without error

Wave 4:
  - [ ] pattern_8f_full_trace.md loadable as F2 BECOME ISO
  - [ ] action_paradigm_cex_build.md covers all 8F functions
  - [ ] reasoning_traces have >= 3 steps with explicit F-annotation

Final:
  - [ ] cex_doctor.py: 0 FAIL (currently 0)
  - [ ] cex_flywheel_audit.py: >= 97% (currently 94%)
  - [ ] All new artifacts compile without error
  - [ ] git log shows structured wave commits
```

---

## ADDRESSING THE BROADER QUESTION

**"ir alem criando possivelmente mais do que so os gaps restantes"**

The cross-synthesis phase (Wave 3) goes beyond gap-filling.
It creates artifacts that DIDN'T EXIST in the original architecture:
- A `knowledge_graph` that maps ALL nucleus domains against each other
- `few_shot_examples` for the 8F pipeline (previously only documented, never exemplified)
- `mental_model` artifacts for CEX's architecture (any LLM can load these to understand CEX)
- An `ontology` that formalizes the 257-kind taxonomy as a navigable structure

These are not filling gaps — they are EMERGENT artifacts from synthesis.
They exist because we now have enough nucleus-specific KCs to triangulate shared patterns.
Cross-nucleus data yields artifacts no single nucleus could produce alone.

**"sem alucinacoes, aprimoramento verticalizado"**

Anti-hallucination rule for all nuclei in this spec:
1. Every new artifact MUST cite >= 1 source artifact from its nucleus (chain of custody)
2. No statistics without a source KC backing them
3. No "best practices" without referencing which pillar/kind encodes them
4. Template-First: if >= 60% match exists, ADAPT it — don't invent

**"convergir tudo para se conectar durante a 8F e alem pelo CoC"**

The CoC convergence (Wave 4) encodes the conventions as artifacts.
Once `pattern_8f_full_trace.md` exists, it becomes a F2 BECOME loadable ISO.
Every nucleus that runs 8F can load this pattern and follow it exactly —
not because they were told to, but because the pattern IS the convention.

This is CoC in practice: the convention is in the code (artifacts), not in documentation.

---

## PROPERTIES

| Property | Value |
|----------|-------|
| Total artifacts | 308 improved + 18 files fixed + 17 new artifacts |
| Waves | 5 (W0 N07, W1 N05 sequential, W2 all parallel, W3 N04+N01, W4 N03, W5 N07) |
| Est. execution time | 3-4 hours total |
| Model | Opus (N03, N07) + Sonnet (N01, N02, N04, N05, N06) |
| Quality gate | heuristic pass: free | agent pass: 20K tokens budget per nucleus |
| Blocking | Wave 1 (path fix) must complete before Wave 2 |
| Anti-hallucination | every artifact cites >= 1 source; no invented kinds |
