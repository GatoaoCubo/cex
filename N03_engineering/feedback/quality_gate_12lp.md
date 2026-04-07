---
id: p07_qg_12_point_validation
kind: quality_gate
pillar: P07
title: 12-Point Validation Checklist (12LP)
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [quality-gate, 12lp, validation, checklist, mandatory]
tldr: 12 mandatory checkpoints every artifact must pass before save. No shortcuts. No exceptions. Run in F7 GOVERN phase.
density_score: 0.95
---

# 12-Point Validation Checklist (12LP)

Run during F7 GOVERN. Every point must PASS or the artifact cannot be saved.

## The 12 Points

| # | Check | What | PASS | FAIL |
|---|-------|------|------|------|
| 1 | **Frontmatter** | YAML frontmatter present with all required fields | All fields present | Missing id, kind, or pillar |
| 2 | **Kind Match** | Artifact kind matches target kind from intent | Exact match | Wrong kind |
| 3 | **Pillar Alignment** | File is in the correct pillar directory | P-number matches dir | Misplaced file |
| 4 | **Schema Compliance** | Content follows the pillar schema structure | Sections match schema | Missing required sections |
| 5 | **Density** | density_score >= 0.80 (tables, trees, code over prose) | >= 0.80 | Verbose, low signal |
| 6 | **Completeness** | No placeholder text left unfilled (except deliberate {{open_vars}}) | All content real | Planned/Pending finalization/Known limitation found |
| 7 | **Uniqueness** | No duplicate artifact at same path or with same id | Unique | Collision detected |
| 8 | **References** | All referenced paths/artifacts actually exist | All resolve | Broken references |
| 9 | **Boundary** | Content stays within kind boundary (does not bleed into other kinds) | Single responsibility | Scope creep |
| 10 | **Size** | File size within kind max_bytes limit | Within limit | Exceeds max |
| 11 | **Naming** | Filename follows kind naming convention from kinds_meta.json | Pattern matches | Wrong naming |
| 12 | **Self-Test** | Would this artifact be useful to a builder who has never seen it before? | Yes, standalone value | Requires tribal knowledge |

## Execution Rules

- Run ALL 12 points. Do not skip any.
- A single FAIL blocks the save.
- Points 1-4 are structural (automatable via cex_doctor.py).
- Points 5-11 are measurable (scripts can check).
- Point 12 is subjective (requires LLM judgment).

## Integration with F7 GOVERN

```
F6 PRODUCE -> artifact draft
  |
  +-> F7 GOVERN: Run 12LP
  |     |
  |     +-> 12/12 PASS: proceed to F8
  |     +-> 1+ FAIL: return to F6 with failure report
  |     |     +-> Retry 1: fix failures, re-run 12LP
  |     |     +-> Retry 2: fix remaining, re-run 12LP
  |     |     +-> Retry 3: REJECT artifact, log failure
  |
  +-> F8 COLLABORATE: save + compile + index + signal
```

## Self-Checks (SC)

Three meta-validations that run AFTER 12LP:

| SC | Question | Expected |
|----|----------|----------|
| SC_001 | Do all referenced artifacts exist? | All paths resolve |
| SC_002 | Are all templates and schemas accessible? | All loadable |
| SC_003 | Would the best builder you know be proud of this? | No hesitation |