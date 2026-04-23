---
id: p01_kc_iterative_refinement_skill
kind: knowledge_card
type: domain
pillar: P01
title: "Iterative Refinement Skill"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, refinement, multi-pass, quality, focused-pass, evolution]
tldr: "Multi-pass improvement where each pass targets exactly one dimension: structure, accuracy, voice, density, format. Never mix concerns in a single pass."
when_to_use: "When an artifact scores below target quality, when evolving existing content, or as the final polish step before publishing."
keywords: [refinement, multi-pass, quality, focused-pass, evolution, polish]
density_score: 0.95
related:
  - p01_kc_refinement
  - p07_gt_stripe_pipeline
  - bld_examples_mental_model
  - n01_hybrid_review_wave1
  - bld_examples_invariant
  - bld_examples_response_format
  - bld_examples_scoring_rubric
  - bld_examples_golden_test
  - hybrid_review7_n05
  - n01_audit_voice_pipeline_builder
---

# Iterative Refinement Skill

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | One pass = one dimension. Five passes = production-ready. |
| Trigger | Quality below target, evolution cycle, pre-publish gate |
| Benefit | Each pass is measurable; improvements compound without interference |
| Risk if skipped | Single-pass edits miss structural issues, create inconsistencies |

## Pass Sequence

| Pass | Focus | What Changes | Quality Impact |
|------|-------|-------------|---------------|
| 1 | **Structure** | Sections, headings, flow, hierarchy | +0.5–1.0 |
| 2 | **Accuracy** | Facts, references, claims, data | +0.3–0.5 |
| 3 | **Voice** | Brand tone, audience calibration, consistency | +0.2–0.3 |
| 4 | **Density** | Remove filler, compress prose → tables, tighten bullets | +0.3–0.5 |
| 5 | **Format** | Frontmatter, naming, encoding, schema compliance | +0.1–0.2 |

## Pass Execution Rules

| Rule | Rationale |
|------|-----------|
| One dimension per pass | Isolates variables — know what caused improvement |
| Measure after each pass | Score delta tracks which passes have most impact |
| Stop when target reached | Don't over-polish; 9.0 is the goal, not 10.0 |
| Order matters | Structure first (fixes layout) → accuracy (fixes content) → voice → density → format |
| Never regress | Each pass must maintain or improve all prior dimensions |

## When to Apply Each Pass

| Artifact State | Start At | Reason |
|---------------|----------|--------|
| Stub (< 7.0) | Pass 1 | Needs fundamental structure |
| Draft (7.0–8.0) | Pass 2 | Structure exists, content needs verification |
| Review (8.0–8.5) | Pass 3 | Content solid, voice/density need work |
| Near-final (8.5–8.9) | Pass 4 | Polish density and formatting |
| Final (9.0+) | None | Target reached — stop |

## Measurement Framework

| Dimension | How to Measure | Tool |
|-----------|---------------|------|
| Structure | Section count, heading hierarchy, flow coherence | Manual review |
| Accuracy | Source triangulation, claim verification | `p01_kc_source_triangulation` |
| Voice | Brand alignment score, audience calibration | Brand audit |
| Density | Words per insight, filler ratio, table density | `cex_evolve.py` density_score |
| Format | Schema validation, frontmatter completeness | `cex_compile.py`, `cex_doctor.py` |

## Practical Example

```
Artifact: kc_token_budgeting.md (quality: 8.4)
  Pass 1 (Structure): Add Quick Reference, Anti-Patterns, Linked Artifacts → 8.7
  Pass 2 (Accuracy): Verify token counts against model docs → 8.8
  Pass 3 (Voice): Ensure consistent technical tone → 8.9
  Pass 4 (Density): Convert 2 prose blocks to tables → 9.1
  Pass 5 (Format): Add when_to_use, update version → 9.1 ✓ DONE
```

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Kitchen sink pass | Editing everything at once hides what worked |
| Accuracy before structure | Verifying facts in a badly organized doc = wasted effort |
| Density before voice | Compressing content before aligning tone = wrong tone, compressed |
| Infinite polish | Diminishing returns after pass 5 — ship it |
| Skipping measurement | No score delta = no evidence of improvement |

## CEX Integration

| Concept | CEX artifact / tool |
|---------|-------------------|
| Quality scoring | `cex_score.py` (per-pass measurement) |
| Automated evolution | `cex_evolve.py` (heuristic + agent modes) |
| Experiment tracking | `.cex/experiments/results.tsv` |
| Brand voice | `brand_audit.py` (voice dimension) |
| Format validation | `cex_compile.py`, `cex_doctor.py` |

## Linked Artifacts

- `p01_kc_self_healing_skill` — automated fix for specific failure modes
- `p01_kc_prompt_evolution` — versioning prompts through iterative improvement
- `p01_kc_confidence_scoring` — score each dimension's certainty

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_refinement]] | sibling | 0.49 |
| [[p07_gt_stripe_pipeline]] | downstream | 0.35 |
| [[bld_examples_mental_model]] | downstream | 0.32 |
| [[n01_hybrid_review_wave1]] | related | 0.30 |
| [[bld_examples_invariant]] | downstream | 0.28 |
| [[bld_examples_response_format]] | downstream | 0.28 |
| [[bld_examples_scoring_rubric]] | downstream | 0.28 |
| [[bld_examples_golden_test]] | downstream | 0.27 |
| [[hybrid_review7_n05]] | sibling | 0.27 |
| [[n01_audit_voice_pipeline_builder]] | downstream | 0.26 |
