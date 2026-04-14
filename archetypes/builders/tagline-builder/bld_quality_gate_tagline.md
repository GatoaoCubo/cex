---
id: bld_quality_gate_tagline
kind: quality_gate
pillar: P07
builder: tagline-builder
version: 1.0.0
quality: 9.1
title: "Quality Gate Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
---
# Quality Gate: Tagline Builder

## HARD gates (must pass or artifact is rejected)
1. H01: Frontmatter has id, kind, title, version, created, quality:null
2. H02: At least 5 variants across 3+ approaches
3. H03: Recommended tagline has reasoning
4. H04: No variant exceeds 15 words
5. H05: Recommended tagline passes competitor-swap test (stated explicitly)

## SOFT gates (warnings, not blockers)
1. S01: Short/medium/long variants present (all 3 lengths)
2. S02: Context adaptations for at least 3 contexts
3. S03: USP extracted and stated
4. S04: Language consistent throughout (no PT/EN mixing unless bilingual brand)
5. S05: Score breakdown present for top variants
6. S06: Emotional + functional approaches both represented

## Scoring Rubric
| Dimension | Weight | 10/10 means |
|-----------|--------|-------------|
| Memorability | 25% | Recalled unprompted after 24h |
| Differentiation | 25% | Could NOT be used by any competitor |
| Clarity | 20% | Understood in 3 seconds (billboard test) |
| Emotional Impact | 15% | Triggers specific feeling in target audience |
| Versatility | 15% | Works across hero, social, email, ad, pitch |

## Scoring Command

```bash
python _tools/cex_score.py --apply --verbose target.md
```

```bash
python _tools/cex_score.py --apply N0*/*.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `quality_gate` |
| Pillar | P07 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
