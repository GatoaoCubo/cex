---
kind: knowledge_card
id: bld_knowledge_card_quality_gate
pillar: P11
llm_function: INJECT
purpose: Domain knowledge for quality_gate production — atomic searchable facts
sources: quality-gate-builder MANIFEST.md + SCHEMA.md
quality: 9.1
title: "Knowledge Card Quality Gate"
version: "1.0.0"
author: n03_builder
tags: [quality_gate, builder, examples]
tldr: "Golden and anti-examples for quality gate construction, demonstrating ideal structure and common pitfalls."
domain: "quality gate construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p11_qg_quality_gate
  - bld_schema_quality_gate
  - bld_memory_quality_gate
  - p03_ins_quality_gate
  - p03_sp_quality_gate_builder
  - bld_collaboration_quality_gate
  - quality-gate-builder
  - bld_meta_quality_gates_builder
  - p11_qg_creation_artifacts
  - p11_qg_kind_builder
---

# Domain Knowledge: quality_gate
## Executive Summary
Quality gates are numeric scoring barriers that block or score artifacts before they ship. Each gate is HARD (binary AND — one failure zeroes the final score) or SOFT (weighted dimension contributing to a 0–10 score). Gates govern one domain and never self-score (`quality: null` always). A gate is a policy; a validator implements it; a rubric defines the scoring dimensions.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (governance) |
| ID pattern | `p11_qg_{gate_slug}` |
| Required frontmatter fields | 12 |
| HARD gates | 8–10 required; universal H01–H06 always present |
| SOFT gates | 5–20; each weight >= 0.5; weights sum == 100% |
| Max body | 4096 bytes |
| Body sections | 5 (Definition, HARD Gates, SOFT Scoring, Actions, Bypass) |
| Score tiers | GOLDEN >= 9.5 / PUBLISH >= 8.0 / REVIEW >= 7.0 / REJECT < 7.0 |
| Naming | `p11_qg_{slug}.md` |
## Patterns
| Pattern | Rule |
|---------|------|
| HARD gate failure | Sets final score to 0 regardless of all SOFT scores |
| Universal HARD gates | H01 (frontmatter parses), H02 (ID regex), H03 (ID == filename), H04 (kind literal), H05 (quality null), H06 (required fields present) |
| SOFT weight minimum | >= 0.5; weight 1.0 = high utility impact; weight 0.5 = polish |
| Weights invariant | Sum of all SOFT weights MUST equal 100% |
| Scoring formula | `final = hard_pass ? sum(gate * weight) / sum(weights) : 0` |
| Threshold rule | Must be numeric — no vague qualifiers ("good", "acceptable") |
| Bypass conditions | Must include: condition + approver + audit_log + expiry |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| SOFT weight < 0.5 | Creates invisible low-signal dimensions |
| Weights not summing to 100% | Breaks scoring formula invariant; validator rejects |
| Missing H01–H06 | Gate is structurally incomplete; kind-specific gates cannot replace universals |
| `quality` field non-null | Self-scoring forbidden by schema |
| Bypass without expiry | Audit trail incomplete; bypass becomes permanent |
| Vague threshold ("high quality") | Not computable; validator cannot determine pass/fail |
| > 12 HARD gates | Diminishing returns; creates unnecessary brittleness |
| Gate checks producer, not artifact | Gates evaluate the artifact output, not who made it |
## Application
1. Identify the artifact kind this gate protects — sets the `domain` field
2. Write frontmatter: 12 required fields; `quality: null`; `id` matches `p11_qg_{slug}` pattern
3. Write `## Definition` — metric, threshold (numeric), operator, scope
4. Write `## HARD Gates` — include H01–H06 universals; add kind-specific gates up to 10 total
5. Write `## SOFT Scoring` — assign weight >= 0.5 per dimension; verify sum == 100%
6. Write `## Actions` — map score ranges to GOLDEN / PUBLISH / REVIEW / REJECT tiers
7. Write `## Bypass` — condition + approver + audit_log + expiry; mark H01 and H05 as never-bypassable
8. Verify body <= 4096 bytes; `id` equals filename stem
## References
- quality-gate-builder MANIFEST.md v1.0.0
- quality_gate SCHEMA.md v2.0.0
- Boundary: quality_gate (policy) vs validator (P06, enforcement code) vs scoring_rubric (P07, dimension criteria)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_quality_gate]] | related | 0.52 |
| [[bld_schema_quality_gate]] | upstream | 0.50 |
| [[bld_memory_quality_gate]] | upstream | 0.48 |
| [[p03_ins_quality_gate]] | related | 0.46 |
| [[p03_sp_quality_gate_builder]] | upstream | 0.44 |
| [[bld_collaboration_quality_gate]] | related | 0.44 |
| [[quality-gate-builder]] | related | 0.42 |
| [[bld_meta_quality_gates_builder]] | related | 0.40 |
| [[p11_qg_creation_artifacts]] | related | 0.38 |
| [[p11_qg_kind_builder]] | related | 0.38 |
