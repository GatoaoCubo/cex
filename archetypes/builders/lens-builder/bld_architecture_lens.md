---
kind: architecture
id: bld_architecture_lens
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of lens — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Lens"
version: "1.0.0"
author: n03_builder
tags: [lens, builder, examples]
tldr: "Golden and anti-examples for lens construction, demonstrating ideal structure and common pitfalls."
domain: "lens construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - lens-builder
  - p03_sp_lens_builder
  - p03_ins_lens
  - p11_qg_lens
  - bld_memory_lens
  - bld_knowledge_card_lens
  - bld_collaboration_lens
  - p01_kc_lens
  - bld_schema_lens
  - bld_output_template_lens
---

# Architecture: lens in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 20-field metadata header (id, kind, pillar, domain, focus, bias, etc.) | lens-builder | active |
| focus_definition | What the lens examines — the specific aspect or dimension | author | active |
| filters | Criteria that determine which artifacts or data pass through the lens | author | active |
| bias_declaration | Explicit statement of the perspective inherent bias | author | active |
| applies_to | List of artifact kinds this lens can be applied to | author | active |
| interpretation_rules | How filtered data should be read through this perspective | author | active |
| weight | Relative importance of this perspective when combined with other lenses | author | active |
## Dependency Graph
```
knowledge_card  --produces-->  lens  --consumed_by-->  agent
scoring_rubric  --depends-->   lens  --applied_to-->   artifact
lens            --signals-->   analysis_result
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | lens | data_flow | domain expertise informing the perspective |
| lens | agent (P02) | consumes | agent applies lens to filter its analysis |
| lens | artifact (any) | data_flow | perspective filter applied to target artifacts |
| lens | analysis_result | produces | filtered interpretation of the examined artifact |
| scoring_rubric (P07) | lens | dependency | rubric dimensions may align with lens focus areas |
| mental_model (P02) | lens | dependency | agent mental model selects which lenses to apply |
## Boundary Table
| lens IS | lens IS NOT |
|---------|-------------|
| A declared perspective with focus, filters, and bias | An autonomous entity with capabilities (agent P02) |
| Applied to artifacts to produce filtered interpretations | A routing decision tree (mental_model P02) |
| Stateless — no memory, no execution, no side effects | A technical specification of an LLM (model_card P02) |
| Composable — multiple lenses can layer on one artifact | An evaluation framework with scoring (scoring_rubric P07) |
| Explicit about its own bias and limitations | A hidden or undeclared analytical assumption |
| Scoped to specific artifact kinds via applies_to | A universal filter applied to everything indiscriminately |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Context | knowledge_card, mental_model | Supply domain expertise and selection criteria for the lens |
| Definition | frontmatter, focus_definition, bias_declaration | Specify what the lens examines and its declared bias |
| Filtering | filters, applies_to, weight | Define what passes through and to which artifacts |
| Application | interpretation_rules | Guide how filtered data is read and understood |
| Output | analysis_result | Structured interpretation produced by applying the lens |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[lens-builder]] | upstream | 0.72 |
| [[p03_sp_lens_builder]] | upstream | 0.66 |
| [[p03_ins_lens]] | upstream | 0.65 |
| [[p11_qg_lens]] | downstream | 0.63 |
| [[bld_memory_lens]] | downstream | 0.61 |
| [[bld_knowledge_card_lens]] | upstream | 0.60 |
| [[bld_collaboration_lens]] | upstream | 0.60 |
| [[p01_kc_lens]] | upstream | 0.59 |
| [[bld_schema_lens]] | upstream | 0.57 |
| [[bld_output_template_lens]] | upstream | 0.51 |
