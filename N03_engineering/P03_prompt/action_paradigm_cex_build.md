---
id: p03_ap_cex_build
kind: action_paradigm
8f: F6_produce
pillar: P03
title: "Action Paradigm -- CEX Build: Input to Artifact via 8F"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 8.8
tags: [action_paradigm, build, 8F, input-to-artifact, coc, N03, execution-model]
tldr: "Execution model for the CEX build action: maps any user input to a typed artifact via the 8F pipeline. Defines the precondition stack, execution phases, postconditions, and error recovery protocols."
density_score: 0.90
updated: "2026-04-17"
related:
  - p08_pat_3phase_build_protocol
  - p12_wf_builder_8f_pipeline
  - p03_sp_n03_creation_nucleus
  - p01_kc_8f_pipeline
  - agent_card_engineering_nucleus
  - skill
  - ctx_cex_new_dev_guide
  - tpl_instruction
  - p02_agent_creation_nucleus
  - p03_ch_builder_pipeline
---

# Action Paradigm: CEX Build

> **Industry equivalents:** procedure (NLU), build-target (Make/Bazel), pipeline stage (MLflow), skill (Alexa)

## Paradigm Definition

The CEX Build Paradigm is the canonical execution model for artifact construction.
It maps: `{intent, context}` → `{typed artifact, 8F trace, signal}`.

Every nucleus running a build action instantiates this paradigm.

---

## Precondition Stack

Before any build action, these must hold. Violation = reject at F1.

| # | Precondition | Check | On Fail |
|---|-------------|-------|---------|
| P1 | Intent is parseable | cex_intent_resolver.py returns tuple | Ask for clarification (GDP) |
| P2 | kind resolves to known value in kinds_meta.json | cex_intent_resolver.py confidence >= 60% | Present top-3 candidates (GDP) |
| P3 | Builder ISOs exist for the kind | archetypes/builders/{kind}-builder/ | Reject; no builder = no build |
| P4 | Pillar directory exists | N0X_{domain}/P{XX}_{name}/ | Create directory (auto-fix) |
| P5 | GDP decisions available if subjective | decision_manifest.yaml or co-pilot mode | GDP gate (never skip) |
| P6 | Token budget allocated | budget_tokens param or default 50000 | Warn + use default |

---

## Execution Phases

### Phase 1: Resolve (F1-F2)

**Action:** Map intent to typed build target.

| Step | Input | Output |
|------|-------|--------|
| F1 CONSTRAIN | raw intent | {kind, pillar, schema, constraints} |
| F2 BECOME | kind | builder_identity, 13 ISOs loaded |
| F2b SPEAK | nucleus | vocabulary KC loaded, drift guard active |

**Decision:** if confidence < 60% → GDP pause. Otherwise proceed.
**Duration:** ~5s (resolver is deterministic, no LLM call needed)

---

### Phase 2: Assemble (F3-F4)

**Action:** Gather all context needed to produce the artifact.

| Step | Input | Output |
|------|-------|--------|
| F3 INJECT | kind + domain | N context sources (KCs, examples, brand, memory) |
| F3b PERSIST | new entities found | queue writes for F8 |
| F3c GROUND | sources loaded | provenance records |
| F4 REASON | context | construction plan {N sections, approach, template_match_score} |

**Decision tree at F4:**
```
template_match_score >= 0.60 -> Template-First
template_match_score 0.30-0.59 -> Hybrid
template_match_score < 0.30 -> Fresh
```

**Duration:** ~15s (depends on context volume)

---

### Phase 3: Produce (F5-F6)

**Action:** Execute the construction plan and generate the artifact.

| Step | Input | Output |
|------|-------|--------|
| F5 CALL | construction plan | tools executed, references fetched |
| F6 PRODUCE | plan + context | draft artifact (bytes, sections, density) |

**F6 invariants:**
- `quality: null` always (INV-03)
- density_score estimated and included
- All embedded code is ASCII-only (INV-12)

**Duration:** ~30-90s (varies by kind complexity and approach)

---

### Phase 4: Gate (F7)

**Action:** Validate the draft against the 7 hard gates and quality score.

| Outcome | Condition | Action |
|---------|-----------|--------|
| PASS | gates 7/7 AND score >= 8.0 | Proceed to F8 |
| RETRY-1 | gates < 7/7 OR score 7.0-7.9 | Return to F6 with repair plan |
| RETRY-2 | Same as RETRY-1 after retry 1 | Second F6 attempt |
| REJECT | score < 7.0 OR gates fail after retry 2 | Destroy draft, rebuild from F4 |

**F7 generates a repair plan:** specific gate failures with file/line location and fix instruction.
**Duration:** ~5s (structural checks are deterministic)

---

### Phase 5: Deliver (F8)

**Action:** Persist the artifact, compile it, commit it, and signal completion.

| Step | Action | Skip condition |
|------|--------|---------------|
| Save | Write artifact to correct pillar path | never skip |
| Compile | `python _tools/cex_compile.py {path}` | skip if compile=false in handoff |
| Index | `python _tools/cex_index.py` (if available) | skip if no indexer |
| Commit | `git add + git commit "[N0X] {kind}: {slug}"` | skip if no git repo |
| Signal | `write_signal(nucleus, 'complete', score)` | skip if signal=false |

**Persistence of F3b queued writes:** execute here, before signal.

---

## Error Recovery Protocol

| Error | Phase | Recovery |
|-------|-------|---------|
| kind unknown (confidence < 60%) | F1 | GDP: present top-3 candidates |
| Builder ISOs missing | F2 | FAIL HARD — no build without builder |
| Context sources 0 (F3 returns empty) | F3 | Proceed with Fresh approach + warn |
| GDP needed but no manifest | F4 | Co-pilot: present decision points |
| F6 produces < 500 bytes | F6 | Treat as empty draft; retry from F4 |
| F7 fails after 2 retries | F7 | Destroy + return to F4 with flag: rebuild_from_scratch=true |
| Compile fails | F8 | Fix syntax error; re-run compile; max 3 attempts |
| Signal fails | F8 | Log to `.cex/runtime/signals/signal_failed.json`; N07 polls |

---

## Postconditions

After a successful build action, these must hold:

| # | Postcondition | Verified by |
|---|--------------|-------------|
| Q1 | Artifact at correct path (N0X/P{XX}/{naming_pattern}) | path check |
| Q2 | Frontmatter complete (13 fields) | cex_doctor.py |
| Q3 | quality: null | grep |
| Q4 | density_score >= 0.85 | cex_score.py |
| Q5 | Compiled YAML exists at compiled/{slug}.yaml | ls compiled/ |
| Q6 | Signal sent with score | .cex/runtime/signals/ |
| Q7 | git commit exists | git log --oneline -1 |

---

## Performance Envelope

| Metric | Target | Max | Action if exceeded |
|--------|--------|-----|--------------------|
| Total latency | < 90s | 300s | Kill + retry with simpler approach |
| Token usage | < 30K | 50K | Warn; use budget_tokens param |
| F6 retries | 0 | 2 | After 2: reject draft |
| Compile errors | 0 | 3 | After 3: flag for manual fix |

---

## Cross-References

- `N03_engineering/P08_architecture/pattern_8f_full_trace.md` — trace format for this paradigm
- `N03_engineering/P08_architecture/pattern_construction_triad.md` — Template/Hybrid/Fresh detail
- `N03_engineering/P07_evals/reasoning_trace_8f_constrain.md` — Phase 1 live example
- `N03_engineering/P07_evals/reasoning_trace_8f_govern.md` — Phase 4 live example
- `N03_engineering/P08_architecture/invariant_n03.md` — invariants this paradigm must honor

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_3phase_build_protocol]] | downstream | 0.38 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.33 |
| [[p03_sp_n03_creation_nucleus]] | related | 0.31 |
| [[p01_kc_8f_pipeline]] | upstream | 0.30 |
| [[agent_card_engineering_nucleus]] | upstream | 0.30 |
| [[skill]] | downstream | 0.29 |
| [[ctx_cex_new_dev_guide]] | related | 0.28 |
| [[tpl_instruction]] | related | 0.27 |
| [[p02_agent_creation_nucleus]] | upstream | 0.27 |
| [[p03_ch_builder_pipeline]] | related | 0.26 |
