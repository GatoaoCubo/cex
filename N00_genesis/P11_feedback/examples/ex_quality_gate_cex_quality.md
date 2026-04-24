---
id: p11_qg_cex_quality
kind: quality_gate
8f: F7_govern
pillar: P11
title: "CEX Pre-Commit Quality Gate"
version: "1.0.0"
created: "2026-03-22"
updated: "2026-03-22"
author: knowledge_agent
domain: meta
quality: 9.2
tags: [quality-gate, pre-commit, validation, scoring, anti-fragility]
tldr: "Gate pre-commit com 5 checks (naming, size, density, schema, generator) + scoring formula + auto-reject criteria"
when_to_use: "Antes de mergear qualquer novo artefato CEX no pool"
keywords: [quality-gate, pre-commit-check, scoring-formula, auto-reject]
long_tails:
  - como validar qualidade de artefatos antes do merge
  - formula de scoring para knowledge cards AI
axioms:
  - Nenhum artefato entra no pool sem passar pelo gate
  - Score < 8.0 = rejeicao automatica sem excecao
density_score: 0.90
related:
  - p11_qg_shokunin_pool
  - p11_lc_cex_lifecycle
  - p11_qg_creation_artifacts
  - p07_qg_12_point_validation
  - p01_kc_artifact_quality_evaluation_methods
  - bld_examples_quality_gate
  - p11_qg_artifact
  - p11_qg_kind_builder
  - p03_sp_verification_agent
  - p04_ct_cex_doctor
---

# CEX Quality Gate

## Purpose
Pre-commit gate para novos artefatos CEX — rejeita antes de entrar no pool.

## Checklist (ALL must pass)

### C1: Naming Compliance
1. [ ] Filename matches `_schema.yaml` naming pattern for its type
2. [ ] Prefix = `{lp_lower}_{type_abbrev}_`
3. [ ] No spaces, uppercase, or special chars (kebab OK for topic)
4. **Auto-check**: `validate_examples.py` type matching

### C2: Size Constraint
1. [ ] File size <= `max_bytes` from schema constraints
2. [ ] If no constraint defined, max 4096 bytes default
3. **Auto-check**: `validate_examples.py` size check

### C3: Density Threshold
1. [ ] Content density >= `density_min` from schema (or 0.85 target)
2. [ ] No empty sections, no placeholder text (Configurable, PENDING, ...)
3. [ ] Each bullet carries actionable data (Specificity Test)
4. **Auto-check**: `validate_examples.py` density estimation

### C4: Schema Compliance
1. [ ] Parent LP has valid `_schema.yaml` (passes `validate_schema.py`)
2. [ ] Type exists in schema types dict
3. [ ] All `frontmatter_required` fields present if applicable

### C5: Generator Alignment
1. [ ] Parent LP has `_generator.md` that covers this type
2. [ ] Example follows generator's PASSO A PASSO structure
3. **Manual check**: review against generator sections

## Auto-Reject Criteria

Immediate rejection if ANY of these:
1. File has no content (0 bytes or only whitespace)
2. Filename doesn't match any schema type naming pattern
3. Size exceeds 2x the `max_bytes` constraint
4. Contains placeholder markers: `Configurable`, `PENDING`, `NOTE`, `...`, `placeholder`
5. Density below 0.5 (excessive boilerplate)
6. Duplicate `id` of existing example

## Tiered Review

| Score | Tier | Decision | Action |
|-------|------|----------|--------|
| < 8.0 | Rejected | REJECT | Do not merge. Author must fix and resubmit |
| 8.0-8.9 | Skilled | ACCEPT | Merge. Eligible for pool and learning memory |
| 9.0-9.4 | Quality | ACCEPT | Merge. Meets CEX quality target. |
| >= 9.5 | Golden | ACCEPT+PROMOTE | Merge + copy to `archetypes/golden/` + celebrate |

## Scoring Guide

| Dimension | Weight | What to Check |
|-----------|--------|---------------|
| Naming | 20% | Schema pattern match, prefix correctness |
| Size | 10% | Within constraints, not bloated |
| Density | 30% | Data per line, no filler, specificity |
| Structure | 20% | Follows body_structure from schema/generator |
| Actionability | 20% | Reader can act without external docs |

**Formula**: `score = (naming * 0.2) + (size * 0.1) + (density * 0.3) + (structure * 0.2) + (actionability * 0.2)`

Each dimension scored 0-10. Final score = weighted sum.

## Integration

```bash
# Pre-commit (run doctor + score)
cd /path/to/cex
python _tools/cex_doctor.py && \
python _tools/cex_score.py --apply <artifact.md>

# Compile after save
python _tools/cex_compile.py <artifact.md>

# Exit code 0 = all pass, 1 = failures found
```

## Escalation

1. 3+ consecutive rejections on same LP -> flag schema/generator for review
2. Golden promotion requires 2 independent validation passes
3. Disputes: author can request manual review with justification

---
*Quality Gate v1.0 | CEX Anti-Fragility Layer | 2026-03-22*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_shokunin_pool]] | sibling | 0.32 |
| [[p11_lc_cex_lifecycle]] | related | 0.25 |
| [[p11_qg_creation_artifacts]] | sibling | 0.24 |
| [[p07_qg_12_point_validation]] | sibling | 0.23 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.23 |
| [[bld_examples_quality_gate]] | upstream | 0.22 |
| [[p11_qg_artifact]] | sibling | 0.21 |
| [[p11_qg_kind_builder]] | sibling | 0.21 |
| [[p03_sp_verification_agent]] | upstream | 0.21 |
| [[p04_ct_cex_doctor]] | upstream | 0.21 |
