---
kind: architecture
id: bld_architecture_quality_gate
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of quality_gate — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Quality Gate"
version: "1.0.0"
author: n03_builder
tags: [quality_gate, builder, examples]
tldr: "Golden and anti-examples for quality gate construction, demonstrating ideal structure and common pitfalls."
domain: "quality gate construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_validator
  - p03_sp_quality_gate_builder
  - p03_ins_quality_gate
  - bld_collaboration_quality_gate
  - quality-gate-builder
  - p01_kc_validator
  - bld_architecture_scoring_rubric
  - p01_kc_quality_gate
  - bld_knowledge_card_quality_gate
  - bld_memory_quality_gate
---

# Architecture: quality_gate in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_kind, pass_threshold, etc.) | quality-gate-builder | active |
| hard_gates | Blocking checks that must pass — artifact rejected on failure | author | active |
| soft_gates | Score-contributing checks that degrade quality score but do not block | author | active |
| scoring_formula | Weighted combination of soft gate scores into final quality number | author | active |
| pass_threshold | Minimum score required to pass the gate | author | active |
| bypass_policy | Conditions and audit requirements for overriding a failed gate | author | active |
## Dependency Graph
```
artifact (any)  --evaluated_by-->  quality_gate  --produces-->    pass_fail_result
scoring_rubric  --depends-->       quality_gate  --signals-->     gate_event
validator       --depends-->       quality_gate
```
| From | To | Type | Data |
|------|----|------|------|
| artifact (any) | quality_gate | data_flow | artifact submitted for quality evaluation |
| quality_gate | pass_fail_result | produces | boolean pass/fail plus numeric score |
| scoring_rubric (P07) | quality_gate | dependency | rubric dimensions inform gate criteria |
| validator (P06) | quality_gate | dependency | validators implement individual hard gate checks |
| quality_gate | gate_event (P12) | signals | emitted on pass, fail, or bypass |
| quality_gate | lifecycle_rule (P11) | data_flow | gate scores may trigger lifecycle transitions |
## Boundary Table
| quality_gate IS | quality_gate IS NOT |
|-----------------|---------------------|
| A barrier with HARD (block) and SOFT (score) checks | A technical pass/fail validation rule (validator P06) |
| Produces a numeric quality score from weighted formula | An evaluation criteria framework (scoring_rubric P07) |
| Applied before artifact is accepted into a pool or promoted | A fix-verify cycle for broken artifacts (bugloop P11) |
| Includes bypass policy with audit trail | A safety restriction on agent behavior (guardrail P11) |
| Targets a specific artifact kind with kind-aware criteria | A continuous optimization loop (optimizer P11) |
| Binary outcome (pass/fail) plus score for ranking | A subjective review without numeric scoring |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | artifact, scoring_rubric | Artifact under evaluation and criteria reference |
| Hard Checks | hard_gates, validator | Blocking checks that must pass |
| Soft Checks | soft_gates, scoring_formula | Score-contributing checks with weighted combination |
| Decision | pass_threshold, bypass_policy | Pass/fail determination and override rules |
| Output | pass_fail_result, gate_event | Result delivered and event signaled downstream |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_validator]] | sibling | 0.43 |
| [[p03_sp_quality_gate_builder]] | upstream | 0.43 |
| [[p03_ins_quality_gate]] | downstream | 0.37 |
| [[bld_collaboration_quality_gate]] | downstream | 0.36 |
| [[quality-gate-builder]] | downstream | 0.36 |
| [[p01_kc_validator]] | upstream | 0.35 |
| [[bld_architecture_scoring_rubric]] | sibling | 0.34 |
| [[p01_kc_quality_gate]] | downstream | 0.33 |
| [[bld_knowledge_card_quality_gate]] | downstream | 0.32 |
| [[bld_memory_quality_gate]] | downstream | 0.32 |
