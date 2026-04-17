---
id: p08_pat_8f_full_trace
kind: pattern
pillar: P08
title: "Pattern -- 8F Full Trace Template (CoC)"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 8.7
tags: [pattern, 8F, full-trace, coc, convention, f2-become, loadable-iso]
tldr: "Convention-over-Configuration pattern for the complete 8F pipeline trace. Loadable as a F2 BECOME ISO. Any nucleus that loads this pattern produces structurally compliant 8F traces without re-deriving conventions."
density_score: 0.91
---

# Pattern: 8F Full Trace Template

> **CoC intent:** This pattern IS the convention. Load it in F2 BECOME and follow it. No configuration required.

## Purpose

The 8F pipeline has 8 functions (F1-F8) plus 3 optional sub-steps (F3b, F3c, F7b).
Every nucleus executes 8F, but without a shared trace template the outputs diverge:
- Some nuclei skip F3b, others invent new sub-steps
- F7 GOVERN scores vary in format, making cross-nucleus comparisons impossible
- F8 signals lack standardized fields

This pattern freezes the output format. Every 8F run produces the same trace structure.

## Trace Template

Every 8F execution writes this trace to stdout:

```
=== 8F PIPELINE: {nucleus} | {kind} | {task_slug} ===

F1 CONSTRAIN
  kind       : {kind}
  pillar     : P{xx}
  schema     : {schema_path}
  max_bytes  : {N}
  naming     : {pattern}
  confidence : {0-100}%

F2 BECOME
  builder    : archetypes/builders/{kind}-builder/
  ISOs loaded: {N}/13
  sin_lens   : {nucleus_sin}
  identity   : {builder_role}

F2b SPEAK [optional]
  vocabulary : {kc_vocabulary_path}
  terms      : {N} canonical terms loaded
  drift_guard: active

F3 INJECT
  sources    : {N} (kc={n1}, examples={n2}, brand={n3}, memory={n4})
  match      : {template_match_score}% ({approach}: template|hybrid|fresh)
  top_source : {path}

F3b PERSIST [optional]
  entities   : {N} new entity memories queued
  facts      : {N} fact updates queued
  learnings  : {N} session learnings queued

F3c GROUND [optional]
  sources    : {N} grounded
  avg_conf   : {X}%
  freshness  : {oldest_source_date}

F4 REASON
  sections   : {N}
  approach   : {template|hybrid|fresh}
  gdp_needed : {yes|no}
  plan       : {brief}

F5 CALL
  tools      : {list}
  similar    : {N} artifacts found (scores: {range})
  pre_checks : {pass|fail}

F6 PRODUCE
  bytes      : {N}
  sections   : {N}
  density    : {score}
  draft_path : {path}

F7 GOVERN
  h01        : {pass|fail} frontmatter complete
  h02        : {pass|fail} kind matches pillar
  h03        : {pass|fail} id globally unique
  h04        : {pass|fail} quality = null
  h05        : {pass|fail} density >= 0.85
  h06        : {pass|fail} no filler prose
  h07        : {pass|fail} cross-reference present
  gates      : {N}/{total} passed
  12LP       : {N}/12 passed
  score      : {X}/10
  retry      : {N} (max 2)

F7b LEARN [optional]
  rewards    : {N} signals
  regressions: {N} detected
  trend      : {improving|stable|declining}

F8 COLLABORATE
  saved      : {path}
  compiled   : {yes|no|skipped}
  committed  : {yes|no}
  signal     : {yes|no} (score={X})

=== END 8F | elapsed={Xs} | quality=null | density={X} ===
```

## Field Contracts

| Field | Type | Required | Invariant |
|-------|------|----------|-----------|
| `kind` | string | YES | Must exist in kinds_meta.json |
| `pillar` | P01-P12 | YES | Must match kind's canonical pillar |
| `gates` | N/total | YES | total = 7 (H01-H07) |
| `12LP` | N/12 | YES | total = 12 |
| `score` | float 0-10 | YES | F7 score, NOT quality field |
| `quality` | null | YES | Never self-assign; peer review only |
| `density` | float 0-1 | YES | >= 0.85 to pass H05 |
| `retry` | int | YES | Increments if F7 fails; max = 2 |
| `compiled` | yes|no|skipped | YES | skipped = no cex_compile.py available |
| `signal` | yes|no | YES | must be yes on F8 success |

## Gate Definitions (H01-H07)

| Gate | Rule | Auto-check |
|------|------|-----------|
| H01 | Frontmatter has: id, kind, pillar, title, version, created, author, domain, quality, tags, tldr | grep frontmatter fields |
| H02 | `kind` value exists in kinds_meta.json AND pillar matches schema | cex_doctor.py --kind |
| H03 | `id` is unique across all .md files in repo | cex_doctor.py --ids |
| H04 | `quality: null` exactly | grep "quality:" |
| H05 | density_score >= 0.85 | cex_score.py field |
| H06 | No filler: "This {kind} defines", "The purpose of this artifact is" | grep filler_patterns |
| H07 | >= 1 cross-reference to another artifact in same nucleus | grep relative_path |

## CoC Application

Loading this pattern at F2 BECOME removes ambiguity:
- Every trace has the same field names in the same order
- Missing optional steps are marked `[skipped]`, not omitted
- Gate pass/fail is binary, never "partial"
- Score line is the last F7 output

```
F2 BECOME: load p08_pat_8f_full_trace.md
-> replaces: "figure out how to format my trace"
-> with: "fill in the trace template"
```

## Anti-Patterns

| Anti-Pattern | Issue | Fix |
|--------------|-------|-----|
| Inventing new sub-steps (F3d, F4a) | Breaks cross-nucleus comparison | Use optional sub-steps F3b, F3c, F7b only |
| Omitting F7 gate details | Quality score is unverifiable | Always list H01-H07 individually |
| `quality: 9.0` in F8 output | Self-scoring violation (INV-03) | quality is always null in artifacts; score is in trace only |
| Skipping F8 COLLABORATE | N07 never learns nucleus completed | Signal is mandatory if signal=true |
| Vague F3 sources | Grounding unverifiable | List each source with path + match% |

## Cross-References

- `N03_engineering/P08_architecture/invariant_n03.md` — INV-01, INV-02, INV-04 enforce trace sequencing
- `N03_engineering/P07_evals/reasoning_trace_8f_constrain.md` — F1 CONSTRAIN live example
- `N03_engineering/P07_evals/reasoning_trace_8f_govern.md` — F7 GOVERN live example
- `.claude/rules/8f-reasoning.md` — authoritative 8F specification
