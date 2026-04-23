---
id: p11_qg_shokunin_pool
kind: quality_gate
pillar: P11
title: "Gate: Shokunin Pool Admission"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
quality: 9.2
tags: [shokunin, pool, quality-gate, feedback]
tldr: "Tiered quality gate for organization pool admission: >= 9.5 golden, >= 8.0 pool, >= 7.0 experimental, < 7.0 rejected"
density_score: 0.93
source: organization-core/CLAUDE.md + records/agent_groups/edison/mental_model.yaml
domain: "feedback"
related:
  - p11_qg_cex_quality
  - p10_ax_shokunin_quality
  - bld_examples_quality_gate
  - p11_qg_creation_artifacts
  - p11_qg_marketing_artifacts
  - p08_law_shokunin
  - bld_tools_naming_rule
  - p11_qg_orchestration_artifacts
  - p11_qg_engineering_artifacts
  - p11_opt_pool_density
---

# Gate: Shokunin Pool Admission

## Definition

| Property | Value |
|----------|-------|
| Metric | 5D quality score |
| Threshold | 7.0 (min), 8.0 (pool), 9.5 (golden) |
| Operator | >= |
| Scope | All artifacts entering `records/pool/` |

## Actions

| Result | Action | Escalation |
|--------|--------|------------|
| >= 9.5 (Golden) | Pool + `archetypes/golden/` + celebrate | Propagate pattern to other agent_groups |
| >= 8.0 (Skilled) | Pool + `remember()` learning record | None |
| >= 7.0 (Learning) | Experimental only | Flag for improvement |
| < 7.0 (Rejected) | Redo from scratch | Block merge, notify author |

## Checklist

1. [ ] 12LP validation: all 12 pillars checked
2. [ ] 5D scoring: density, naming, structure, actionability, size all scored
3. [ ] No placeholders: zero Configurable/PENDING/NOTE markers
4. [ ] Duplicate check: no existing artifact with same `id` in pool
5. [ ] Schema compliance: validates against parent `_schema.yaml`

## Scoring

| Dimension | Weight | What to Check |
|-----------|--------|---------------|
| Density | 30% | Useful tokens / total tokens, no filler |
| Naming | 20% | Matches schema naming pattern exactly |
| Structure | 20% | Follows generator body_structure |
| Actionability | 20% | Reader can act without external docs |
| Size | 10% | Within `max_bytes` constraint |

## Bypass

1. Conditions: never (pool quality is non-negotiable)
2. Approver: none
3. Audit: All pool writes logged in git history with quality score in commit message

---
*Migrated from: organization Shokunin quality philosophy (CLAUDE.md + Edison mental_model.yaml)*

## Scoring Command

```bash
python _tools/cex_score.py --apply --verbose target.md
python _tools/cex_score.py --apply N0*/*.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_cex_quality]] | sibling | 0.38 |
| [[p10_ax_shokunin_quality]] | upstream | 0.34 |
| [[bld_examples_quality_gate]] | upstream | 0.32 |
| [[p11_qg_creation_artifacts]] | sibling | 0.31 |
| [[p11_qg_marketing_artifacts]] | sibling | 0.27 |
| [[p08_law_shokunin]] | upstream | 0.27 |
| [[bld_tools_naming_rule]] | upstream | 0.27 |
| [[p11_qg_orchestration_artifacts]] | sibling | 0.26 |
| [[p11_qg_engineering_artifacts]] | sibling | 0.26 |
| [[p11_opt_pool_density]] | related | 0.26 |
